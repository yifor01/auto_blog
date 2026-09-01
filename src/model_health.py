"""OpenRouter fallback chain 健康檢查（零 LLM 判斷，純實測）。

存在理由：generation 與 scoring 主力都改走 Claude Code CLI 之後，`llm.scoring_models` /
`llm.generation_models` 變成**冷路徑**——平常不執行，會靜默腐爛，等 CLI 真的掛掉那天
才發現備援也是死的。這支就是定期去踩一次那條路。

判準刻意用**真實的評分 prompt + 真實的 validator**（5 維皆為數字），不是 `_probe_model`
的「有沒有回應」。2026-09-01 實測，只看有沒有回應會漏掉兩種壞法：
  - `nvidia/nemotron-3.5-lightning` 回 "Here's a thinking process:..."（推理外洩）
  - `inclusionai/ling-3.0-flash-fin` 回空字串
兩者在 `_probe_model` 的 "Reply with OK" 下都是活的。
"""

from __future__ import annotations

from dataclasses import dataclass

from src.logger import get_logger
from src.scoring.scorer import SCORING_SYSTEM_PROMPT, _parse_score_json
from src.utils import discover_free_models, get_llm_client, load_config

_logger = get_logger("model_health")

_DIMENSIONS = ("novelty", "impact", "trending", "practicality", "blog_worthiness")

# 固定素材，讓跨週的結果可比。內容不重要，能不能照契約吐 JSON 才重要。
PROBE_USER_MSG = """請評估以下內容的部落格寫作價值（只依標題與摘要判斷技術價值）：

**標題**: Attention Is All You Need
**來源**: arXiv
**機構**: Google
**作者**: Ashish Vaswani
**摘要**: We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments show these models to be superior in quality while being more parallelizable and requiring significantly less time to train.
**標籤**: transformer, attention
"""

# 狀態語意：ok / gone 是結論，busy 是「今天忙」不代表該換掉，bad_output 才是該換的。
STATUS_OK = "ok"
STATUS_GONE = "gone"          # 404，下架
STATUS_BUSY = "busy"          # 429，上游池限流；換 key 無效但明天可能又活
STATUS_BAD_OUTPUT = "bad"     # 有回應但不照契約（推理外洩 / 空字串 / 非 JSON）
STATUS_ERROR = "error"


@dataclass
class ProbeResult:
    model: str
    status: str
    detail: str = ""
    elapsed: float = 0.0

    @property
    def usable(self) -> bool:
        return self.status == STATUS_OK


def probe_scoring_model(model: str, timeout: float = 90.0, attempts: int = 2) -> ProbeResult:
    """用真實評分 prompt 實打，判斷這個 model 現在能不能當評分 fallback。

    `attempts=2` 與 `scorer.py` 的外層 retry 一致，判準才等於生產環境。單次 probe 會製造
    假警報：`openrouter/free` 每次呼叫隨機換 model（實測 10 次 7 次合格），單次探測等於
    擲骰子；一般 :free model 也會偶發回空字串。
    """
    last = ProbeResult(model, STATUS_ERROR, "未執行")
    for _ in range(max(1, attempts)):
        last = _probe_once(model, timeout)
        if last.usable:
            return last
        # 下架與限流是結論，重試沒有意義
        if last.status in (STATUS_GONE, STATUS_BUSY):
            return last
    return last


def _probe_once(model: str, timeout: float) -> ProbeResult:
    import time

    t = time.time()
    try:
        resp = get_llm_client(model).with_options(timeout=timeout).chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SCORING_SYSTEM_PROMPT},
                {"role": "user", "content": PROBE_USER_MSG},
            ],
            temperature=0.3,
            max_tokens=1200,
        )
    except Exception as e:
        err = str(e)
        el = time.time() - t
        if "404" in err:
            return ProbeResult(model, STATUS_GONE, err[:200], el)
        if "429" in err:
            # provider_name 只出現在上游池限流的 body 裡；有它代表換 key 沒用
            upstream = ""
            for token in ("provider_name", "Provider returned error"):
                if token in err:
                    upstream = "上游池限流"
                    break
            return ProbeResult(model, STATUS_BUSY, (upstream or "限流") + " " + err[:150], el)
        return ProbeResult(model, STATUS_ERROR, err[:200], el)

    el = time.time() - t
    choices = getattr(resp, "choices", None) or []
    content = ""
    if choices:
        content = (getattr(choices[0].message, "content", "") or "").strip()
    if not content:
        return ProbeResult(model, STATUS_BAD_OUTPUT, "回空字串", el)

    scores = _parse_score_json(content)
    if not isinstance(scores, dict):
        return ProbeResult(model, STATUS_BAD_OUTPUT, f"非 JSON：{content[:80]!r}", el)
    missing = [d for d in _DIMENSIONS if not isinstance(scores.get(d), (int, float))]
    if missing:
        return ProbeResult(model, STATUS_BAD_OUTPUT, f"缺維度 {missing}", el)
    return ProbeResult(model, STATUS_OK, "", el)


def check_scoring_chain(
    config: dict | None = None,
    candidate_limit: int = 8,
    timeout: float = 90.0,
) -> dict:
    """實測 configured chain，chain 有洞時再從免費池找替補候選。

    回傳 {'configured': [ProbeResult], 'candidates': [ProbeResult], 'broken': [ProbeResult]}。
    `broken` 只收 gone / bad_output——busy 是今天忙，不是該換掉的理由。
    """
    if config is None:
        config = load_config()
    chain = list((config.get("llm") or {}).get("scoring_models") or [])

    configured = [probe_scoring_model(m, timeout) for m in chain]
    for r in configured:
        _logger.info("chain probe", extra={"model": r.model, "status": r.status, "detail": r.detail[:120]})

    broken = [r for r in configured if r.status in (STATUS_GONE, STATUS_BAD_OUTPUT)]

    candidates: list[ProbeResult] = []
    if broken:
        # 只在 chain 真的有洞時才燒額度探索替補
        pool = [m for m in discover_free_models(limit=candidate_limit * 2) if m not in chain]
        for m in pool[:candidate_limit]:
            r = probe_scoring_model(m, timeout)
            candidates.append(r)
            _logger.info("candidate probe", extra={"model": r.model, "status": r.status})

    return {"configured": configured, "candidates": candidates, "broken": broken}


_STATUS_LABEL = {
    STATUS_OK: "✅ 可用",
    STATUS_GONE: "❌ 下架",
    STATUS_BUSY: "⏳ 限流",
    STATUS_BAD_OUTPUT: "⚠️ 輸出不合契約",
    STATUS_ERROR: "❌ 錯誤",
}


def render_report(result: dict) -> str:
    """產出 markdown 報告，直接當 GitHub Issue 內文用。"""
    lines = ["## OpenRouter 評分 fallback chain 健康檢查", ""]
    lines.append("判準：能否對真實評分 prompt 吐出 5 維皆為數字的 JSON。")
    lines.append("")
    lines.append("### 目前 config 的 chain")
    lines.append("")
    lines.append("| # | model | 狀態 | 耗時 | 備註 |")
    lines.append("|---|-------|------|------|------|")
    for i, r in enumerate(result["configured"], 1):
        lines.append(
            f"| {i} | `{r.model}` | {_STATUS_LABEL.get(r.status, r.status)} | {r.elapsed:.1f}s | {r.detail[:90]} |"
        )

    broken = result["broken"]
    if not broken:
        lines += ["", "chain 沒有需要更換的項目。限流（⏳）是當下忙碌，不是該換掉的理由。"]
        return "\n".join(lines)

    lines += ["", f"### 需要更換：{len(broken)} 個", ""]
    for r in broken:
        lines.append(f"- `{r.model}` — {_STATUS_LABEL.get(r.status, r.status)}：{r.detail[:120]}")

    usable = [r for r in result["candidates"] if r.usable]
    lines += ["", "### 免費池實測可用的替補候選", ""]
    if usable:
        lines.append("| model | 耗時 |")
        lines.append("|-------|------|")
        for r in sorted(usable, key=lambda x: x.elapsed):
            lines.append(f"| `{r.model}` | {r.elapsed:.1f}s |")
        lines += [
            "",
            "**選 model 硬規則**：同一條 chain 的 fallback 必須掛在不同上游 provider。",
            ":free 變體的上游只能從 429 body 的 `provider_name` 實測得知，models API 查不到——",
            "換上去之後請留意後續幾天的 log。",
        ]
    else:
        lines.append("免費池裡沒有實測可用的替補。chain 全空時 `llm_chat` 會走 `openrouter/free` 保底。")

    lines += ["", "改完 `config.yaml` 的 `llm.scoring_models` 後關掉這個 issue。"]
    return "\n".join(lines)
