"""LLM-based deep scoring for pre-filtered items."""

from __future__ import annotations

import json
import os
import re
import time

from rich.progress import BarColumn, MofNCompleteColumn, Progress, SpinnerColumn, TextColumn, TimeRemainingColumn

from src.logger import get_logger
from src.models import ScoredItem
from src.utils import claude_code_generate, console, llm_chat, load_config

_logger = get_logger("scoring.scorer")
_json_mode = os.environ.get("AUTOPB_LOG_FORMAT", "").lower() == "json"

ABSTRACT_MIN_LEN_FOR_LLM = 50

SCORING_SYSTEM_PROMPT = """你是一位 GenAI 領域的資深研究員和技術部落客。你的任務是評估一篇 AI 相關內容的「部落格寫作價值」。

你的目標讀者是 GenAI 領域的工程師、研究者和技術管理者，他們關注最新的模型架構、訓練技術、部署方案和產業動態。

請從以下 5 個維度評分（每個 0-20 分）。**務必使用 0-20 全距，敢給低分也敢給滿分，不要把分數全擠在 12-16。** 每個維度的落點參考：

1. **新穎性 (Novelty)** — 抄既有方法=0-4；常見改良或微調=5-9；明顯的新方法=10-14；全新架構或範式轉移=15-20。
2. **影響力 (Impact)** — 個人玩具=0-4；小眾有用=5-9；影響特定領域=10-14；可能改變整個產業做法=15-20。
3. **話題性 (Trending)** — 無社群訊號且冷門=0-6；中等熱度=7-12；明顯熱門且踩中當前焦點（Agent、推理、多模態、開源模型等）=13-20。社群訊號（upvotes/stars/points）僅供此維度參考，勿影響其他維度。
4. **實用性 (Practicality)** — 純理論難落地=0-5；概念可參考=6-11；有程式碼或可複現=12-16；開箱即用的工具=17-20。
5. **部落格適合度 (Blog-worthiness)** — 純行銷或無技術=0-6；尚可=7-12；有清楚故事與技術深度=13-20。此維度評「能否寫成一篇好文章」，請獨立判斷，勿直接取其他維度平均。

以下類型一律給低分：純行銷公告、已廣泛報導的舊聞重發、無實質技術內容的產品宣傳、僅微調 benchmark 但無方法創新的 incremental work、包裝既有工具的 wrapper 專案。

尺度錨定範例（協助校準，非輸出格式）：
- 某公司宣布新版 API 上線、無技術細節 → 新穎 2、影響 5、話題 6、實用 4、適合度 3
- 開源新 attention 架構、附訓練程式碼、HF 80 upvotes → 新穎 17、影響 15、話題 16、實用 18、適合度 18

嚴格只回覆以下 JSON 物件，不要加任何其他文字、不要加註解、不要包在 markdown code block 裡：
{
  "novelty": <int 0-20>,
  "impact": <int 0-20>,
  "trending": <int 0-20>,
  "practicality": <int 0-20>,
  "blog_worthiness": <int 0-20>,
  "reason": "<繁體中文一句話，≤40 字，點出核心貢獻或扣分主因>"
}"""


def _build_item_block(item: ScoredItem) -> str:
    """把單筆素材組成評分用的文字區塊。逐篇與批次共用，兩條路徑看到的素材必須逐字相同。"""
    # 收集社群訊號
    metadata = item.item.raw_metadata
    signals = []
    if metadata.get("upvotes"):
        signals.append(f"HF upvotes: {metadata['upvotes']}")
    if metadata.get("stars_today"):
        signals.append(f"GitHub stars today: {metadata['stars_today']}")
    if metadata.get("total_stars"):
        signals.append(f"GitHub total stars: {metadata['total_stars']}")
    if metadata.get("points"):
        signals.append(f"HN points: {metadata['points']}")
    if metadata.get("num_comments"):
        signals.append(f"Comments: {metadata['num_comments']}")
    if metadata.get("score"):
        signals.append(f"Reddit score: {metadata['score']}")

    signals_str = (
        f"\n**社群訊號**: {', '.join(signals)}"
        "\n（量級參考：HF upvotes 通常 0-100、GitHub stars 可達數萬、"
        "HN/Reddit points 數百即算熱門；請依相對熱度判斷話題性，勿被絕對數字大小誤導）"
    ) if signals else ""

    return f"""**標題**: {item.item.title}
**來源**: {item.item.source_name}
**機構**: {item.item.organization}
**作者**: {', '.join(item.item.authors[:5])}
**摘要**: {item.item.abstract[:1500]}
**標籤**: {', '.join(item.item.tags)}{signals_str}
"""


def _apply_scores(item: ScoredItem, scores: dict) -> None:
    """把解析好的 5 維分數寫回 item。逐篇與批次共用，確保兩條路徑的加總規則一致。"""
    item.llm_reason = scores.get("reason", "")
    item.novelty = scores.get("novelty", 0)
    item.impact = scores.get("impact", 0)
    item.trending = scores.get("trending", 0)
    item.practicality = scores.get("practicality", 0)
    item.blog_worthiness = scores.get("blog_worthiness", 0)
    # 自行加總，不信任 LLM 計算的 total
    item.llm_score = sum([
        item.novelty or 0,
        item.impact or 0,
        item.trending or 0,
        item.practicality or 0,
        item.blog_worthiness or 0,
    ])


def llm_score_item(item: ScoredItem) -> ScoredItem:
    """用 LLM 對單個 item 深度評分（OpenRouter 逐篇路徑）。"""
    user_msg = (
        "請評估以下內容的部落格寫作價值（只依標題與摘要判斷技術價值）：\n\n"
        + _build_item_block(item)
    )

    try:
        scores = None
        last_response = ""
        # 外層最多 2 次 attempt；llm_chat 帶 validate 會在單一 model 吐爛 JSON 時原地降級
        # 下一 model，故不需在外層重打整條 chain（避免每日 50 次額度被 27 次請求燒光）。
        for _parse_attempt in range(2):
            response = llm_chat(
                messages=[
                    {"role": "system", "content": SCORING_SYSTEM_PROMPT},
                    {"role": "user", "content": user_msg},
                ],
                temperature=0.3,
                # reasoning model（gpt-oss 系列）的推理 token 也算進 max_tokens，
                # 500 會被推理吃光導致 content 為空白燒請求，故留推理空間
                max_tokens=1200,
                validate=lambda t: _parse_score_json(t) is not None,
            )
            last_response = response
            scores = _parse_score_json(response)
            if scores:
                break
            if _parse_attempt < 1:
                _logger.debug("LLM score parse failed, retrying", extra={"title": item.item.title[:80]})

        if scores:
            _apply_scores(item, scores)
        else:
            _logger.warning(
                "Failed to parse LLM score",
                extra={
                    "title": item.item.title[:80],
                    "raw_response": (last_response or "")[:500],
                },
            )

    except Exception as e:
        _logger.error("LLM scoring error", extra={"title": item.item.title[:80], "error": str(e)})

    return item


def _parse_score_json(text: str) -> dict | None:
    """從 LLM 回覆中提取 JSON（處理 markdown code block 和其他噪音）。"""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    patterns = [
        r"```json\s*(.*?)\s*```",
        r"```\s*(.*?)\s*```",
        r"\{[^{}]*\}",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1) if match.lastindex else match.group())
            except json.JSONDecodeError:
                continue
    return None

# ──────────────────────────────────────────────────────────
# 批次評分（Claude Code CLI，headless）
# ──────────────────────────────────────────────────────────

SCORE_BATCH_END_MARKER = "===END==="

# 分隔行必須獨佔一行。素材摘要可能引用「===SCORE」這種字串，只有獨佔一行的才算分隔。
_SCORE_MARKER_RE = re.compile(r"^===SCORE (\d+)===[ \t]*$", re.MULTILINE)

_SCORE_DIMENSIONS = ("novelty", "impact", "trending", "practicality", "blog_worthiness")

SCORE_BATCH_CONTRACT = f"""

# ══ 批次輸出契約（本次為批次模式，務必嚴格遵守）══

你這次會一次收到「多筆」素材，每筆以 `### 素材 N` 標示。請為**每一筆**各給一組 5 維分數，
逐筆套用上面全部的評分規範（落點參考、一律低分的類型、尺度錨定，一項都不能少）。

輸出格式（唯一合法格式，不得偏離）：

===SCORE 1===
{{"novelty": 12, "impact": 10, "trending": 8, "practicality": 15, "blog_worthiness": 13, "reason": "一句話理由"}}
===SCORE 2===
{{"novelty": 3, "impact": 5, "trending": 6, "practicality": 4, "blog_worthiness": 3, "reason": "一句話理由"}}
...
{SCORE_BATCH_END_MARKER}

硬性規則：
- 分隔行 `===SCORE N===` 必須獨佔一行，前後不得有任何字元，N 對應素材編號。
- 分隔行之後只放那一筆的 JSON 物件，不要加註解、不要包在 markdown code block 裡。
- 每筆都要評，不得因為素材相似就合併、略過或寫「同上」。
- 你一次看得到全部素材，請做相對比較把分數拉開；整批擠在 12-16 視為未完成任務。
- 不要在第一個 `===SCORE 1===` 之前輸出任何字元；全部評完後最後一行輸出 `{SCORE_BATCH_END_MARKER}`。
"""


def build_score_batch_prompt(items: list[ScoredItem]) -> str:
    """把多筆素材組成單一 prompt。

    `claude -p` 沒有 system / user 訊息之分，整份從 stdin 進去，因此規範與素材串在一起送。
    """
    blocks = [f"### 素材 {n}\n{_build_item_block(it)}" for n, it in enumerate(items, 1)]
    materials = "\n\n---\n\n".join(blocks)
    return (
        f"{SCORING_SYSTEM_PROMPT}{SCORE_BATCH_CONTRACT}\n\n"
        f"# ══ 素材 ══\n\n"
        f"請評估以下 {len(items)} 筆素材的部落格寫作價值（只依標題與摘要判斷技術價值）。\n\n"
        f"{materials}\n\n請依批次輸出契約，逐筆輸出。"
    )


def parse_score_batch_output(output: str, expected: int) -> dict[int, dict]:
    """把批次輸出切成 {素材編號: 分數 dict}。缺漏不是例外，只是該 key 不存在。

    兩道防線：
    - 超出範圍的編號直接丟掉——模型偶爾會多評一筆不存在的素材，放行會讓對齊錯位，
      把 A 的分數寫到 B 身上。
    - 5 個維度沒到齊的整筆視為缺漏。逐篇路徑只要是合法 JSON 就收，但批次一筆殘缺
      會被 `_apply_scores` 補成 0 分而靜默沉底；退回逐篇重評才是對的。
    """
    if not output:
        return {}
    parts = _SCORE_MARKER_RE.split(output)
    # split 後：[前導雜訊, idx1, body1, idx2, body2, ...]。前導雜訊直接丟。
    found: dict[int, dict] = {}
    for i in range(1, len(parts) - 1, 2):
        idx = int(parts[i])
        if not 1 <= idx <= expected:
            continue
        body = parts[i + 1].replace(SCORE_BATCH_END_MARKER, "").strip()
        scores = _parse_score_json(body) if body else None
        if not isinstance(scores, dict):
            continue
        if not all(isinstance(scores.get(d), (int, float)) for d in _SCORE_DIMENSIONS):
            continue
        found[idx] = scores
    return found


def score_items_batch(items: list[ScoredItem], model: str, timeout: float) -> list[ScoredItem]:
    """一次 CLI session 評完整批，就地寫回分數，回傳「沒拿到分數」的 items。

    這裡不自己 fallback：批次層只負責「批次拿到什麼」，補救策略屬於上層。
    """
    prompt = build_score_batch_prompt(items)
    output = claude_code_generate(prompt, model=model, timeout=timeout)
    scores_by_idx = parse_score_batch_output(output, expected=len(items))

    missing: list[ScoredItem] = []
    for n, it in enumerate(items, 1):
        scores = scores_by_idx.get(n)
        if not scores:
            missing.append(it)
            continue
        _apply_scores(it, scores)

    if missing:
        _logger.warning(
            "批次評分缺漏，退回逐篇",
            extra={"missing": len(missing), "batch_size": len(items), "model": model},
        )
    return missing


def _score_via_claude_code(items: list[ScoredItem], batch_cfg: dict) -> list[ScoredItem]:
    """走 CLI 批次評分，回傳需要逐筆補救的 items。"""
    model = batch_cfg.get("model", "sonnet")
    batch_size = max(1, int(batch_cfg.get("batch_size", 20)))
    timeout = float(batch_cfg.get("timeout_seconds", 900))
    batches = [items[i:i + batch_size] for i in range(0, len(items), batch_size)]

    _logger.info(
        "批次評分開始",
        extra={"count": len(items), "batches": len(batches), "batch_size": batch_size, "model": model},
    )

    missing: list[ScoredItem] = []
    for n, batch in enumerate(batches, 1):
        if not _json_mode:
            console.print(f"[cyan]批次評分[/cyan] {n}/{len(batches)}（{len(batch)} 筆）...")
        missing.extend(score_items_batch(batch, model, timeout))
    return missing


def _score_sequentially(items: list[ScoredItem], delay: float) -> None:
    """逐筆走 OpenRouter，就地寫回分數。批次停用時的預設路徑，也是批次缺漏時的補救。"""
    if not items:
        return

    if _json_mode:
        for i, item in enumerate(items):
            scored_item = llm_score_item(item)
            _logger.debug(
                f"({i+1}/{len(items)}) [{scored_item.item.source.value}] "
                f"{scored_item.item.title[:50]} → LLM {scored_item.llm_score}, "
                f"總分 {round(scored_item.total_score)}",
                extra={
                    "title": scored_item.item.title[:80],
                    "source": scored_item.item.source.value,
                    "llm_score": scored_item.llm_score,
                    "total_score": round(scored_item.total_score),
                },
            )
            if i < len(items) - 1:
                time.sleep(delay)
        return

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        MofNCompleteColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=False,
    ) as progress:
        task = progress.add_task("LLM 評分中...", total=len(items))
        for i, item in enumerate(items):
            progress.update(task, description=f"[cyan]評分[/cyan] {item.item.title[:45]}...")
            llm_score_item(item)
            progress.advance(task)
            if i < len(items) - 1:
                time.sleep(delay)


def batch_llm_score(
    items: list[ScoredItem],
    config: dict | None = None,
) -> list[ScoredItem]:
    """批量 LLM 評分，只對 top_k 個 items，回傳分數最高的 final_top_k。

    由 `scoring.batch_scoring.enabled` 分流成兩條路徑，回傳結構完全相同，切換只需改那個
    bool：批次走 Claude Code CLI（一個 session 評多筆），逐篇走 OpenRouter chain。
    **fallback 粒度是「筆」不是「批」**——整批重跑會把已評好的也重評，燒額度又可能更差。
    """
    if config is None:
        config = load_config()

    llm_top_k = config.get("scoring", {}).get("llm_top_k", 20)
    candidates = items[:llm_top_k]
    delay = config.get("llm", {}).get("request_delay_seconds", 10)

    _logger.info("LLM batch scoring started", extra={"candidate_count": len(candidates), "delay_seconds": delay})

    # 摘要太短的不送 LLM（兩條路徑一致），留原樣參與後面的排序
    eligible = []
    for item in candidates:
        abstract_len = len(item.item.abstract.strip())
        if abstract_len < ABSTRACT_MIN_LEN_FOR_LLM:
            _logger.warning(
                "Skipping LLM scoring: abstract too short",
                extra={
                    "title": item.item.title[:80],
                    "source": item.item.source.value,
                    "abstract_len": abstract_len,
                },
            )
            continue
        eligible.append(item)

    pending = eligible
    # 與 batch_generation 並列放在 llm 底下，兩者是同一套 CLI 機制的兩個開關
    batch_cfg = (config.get("llm") or {}).get("batch_scoring") or {}
    if batch_cfg.get("enabled") and eligible:
        pending = _score_via_claude_code(eligible, batch_cfg)

    _score_sequentially(pending, delay)

    # llm_score_item / _apply_scores 都是就地改寫，candidates 已帶上分數
    scored = sorted(candidates, key=lambda x: x.total_score, reverse=True)

    final_top_k = config.get("scoring", {}).get("final_top_k", 5)
    top = scored[:final_top_k]

    _logger.info("LLM batch scoring complete", extra={"selected_count": len(top)})
    for i, s in enumerate(top, 1):
        _logger.debug("Top item", extra={"rank": i, "title": s.item.title[:60], "total_score": round(s.total_score)})

    return top
