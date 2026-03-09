"""LLM-based deep scoring for pre-filtered items."""

from __future__ import annotations

import json
import os
import re
import time

from rich.progress import BarColumn, MofNCompleteColumn, Progress, SpinnerColumn, TextColumn, TimeRemainingColumn

from src.logger import get_logger
from src.models import ScoredItem
from src.utils import console, llm_chat, load_config

_logger = get_logger("scoring.scorer")
_json_mode = os.environ.get("AUTOPB_LOG_FORMAT", "").lower() == "json"

ABSTRACT_MIN_LEN_FOR_LLM = 50

SCORING_SYSTEM_PROMPT = """你是一位 GenAI 領域的資深研究員和技術部落客。你的任務是評估一篇 AI 相關內容的「部落格寫作價值」。

你的目標讀者是 GenAI 領域的工程師、研究者和技術管理者，他們關注最新的模型架構、訓練技術、部署方案和產業動態。

請從以下 5 個維度評分 (每個 0-20 分):

1. **新穎性 (Novelty)** — 是否提出過去沒有的新想法/新方法/新架構？舊瓶新酒得低分。
2. **影響力 (Impact)** — 對 AI 產業或研究社群的潛在影響有多大？會改變大家的工作方式嗎？
3. **話題性 (Trending)** — 是否與當前 AI 社群熱議的話題相關？社群訊號（upvotes/stars/points）越高代表越熱門。
4. **實用性 (Practicality)** — 工程師能否立即從中受益？有開源工具/程式碼嗎？
5. **部落格適合度 (Blog-worthiness)** — 這個主題適合寫成引人入勝的科技部落格文章嗎？目標讀者會感興趣嗎？

評分錨點：0-5 = 無/極低、6-10 = 普通、11-15 = 高、16-20 = 頂尖突破

以下類型應給低分：純行銷公告、已廣泛報導的舊聞重發、無實質技術內容的產品宣傳。

嚴格用 JSON 回覆，不要加任何其他文字：
{
  "novelty": <int 0-20>,
  "impact": <int 0-20>,
  "trending": <int 0-20>,
  "practicality": <int 0-20>,
  "blog_worthiness": <int 0-20>,
  "reason": "<一句話解釋為什麼這篇值得/不值得寫成部落格>"
}"""


def llm_score_item(item: ScoredItem) -> ScoredItem:
    """用 LLM 對單個 item 深度評分。"""
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

    signals_str = f"\n**社群訊號**: {', '.join(signals)}" if signals else ""

    user_msg = f"""請評估以下內容的部落格寫作價值：

**標題**: {item.item.title}
**來源**: {item.item.source_name}
**URL**: {item.item.url}
**發布日期**: {item.item.published_date}
**機構**: {item.item.organization}
**作者**: {', '.join(item.item.authors[:5])}
**摘要**: {item.item.abstract[:2000]}
**標籤**: {', '.join(item.item.tags)}{signals_str}
"""

    try:
        response = llm_chat(
            messages=[
                {"role": "system", "content": SCORING_SYSTEM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
            temperature=0.3,
            max_tokens=500,
        )

        scores = _parse_score_json(response)
        if scores:
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
        else:
            _logger.warning("Failed to parse LLM score", extra={"title": item.item.title[:80]})

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


def batch_llm_score(
    items: list[ScoredItem],
    config: dict | None = None,
) -> list[ScoredItem]:
    """批量 LLM 評分，只對 top_k 個 items。含 rate limiting delay 與 Rich 進度條。"""
    if config is None:
        config = load_config()

    llm_top_k = config.get("scoring", {}).get("llm_top_k", 20)
    candidates = items[:llm_top_k]
    delay = config.get("llm", {}).get("request_delay_seconds", 10)

    _logger.info("LLM batch scoring started", extra={"candidate_count": len(candidates), "delay_seconds": delay})

    scored = []
    if _json_mode:
        for i, item in enumerate(candidates):
            abstract_len = len(item.item.abstract.strip())
            if abstract_len < ABSTRACT_MIN_LEN_FOR_LLM:
                _logger.warning(
                    "Skipping LLM scoring: abstract too short",
                    extra={"title": item.item.title[:80], "source": item.item.source.value, "abstract_len": abstract_len},
                )
                scored.append(item)
                continue
            scored_item = llm_score_item(item)
            _logger.debug(
                f"({i+1}/{len(candidates)}) [{scored_item.item.source.value}] "
                f"{scored_item.item.title[:50]} → LLM {scored_item.llm_score}, "
                f"總分 {round(scored_item.total_score)}",
                extra={
                    "title": scored_item.item.title[:80],
                    "source": scored_item.item.source.value,
                    "llm_score": scored_item.llm_score,
                    "total_score": round(scored_item.total_score),
                },
            )
            scored.append(scored_item)
            if i < len(candidates) - 1:
                time.sleep(delay)
    else:
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            MofNCompleteColumn(),
            TimeRemainingColumn(),
            console=console,
            transient=False,
        ) as progress:
            task = progress.add_task("LLM 評分中...", total=len(candidates))
            for i, item in enumerate(candidates):
                progress.update(task, description=f"[cyan]評分[/cyan] {item.item.title[:45]}...")
                abstract_len = len(item.item.abstract.strip())
                if abstract_len < ABSTRACT_MIN_LEN_FOR_LLM:
                    _logger.warning(
                        "Skipping LLM scoring: abstract too short",
                        extra={"title": item.item.title[:80], "source": item.item.source.value, "abstract_len": abstract_len},
                    )
                    scored.append(item)
                    progress.advance(task)
                    continue
                scored_item = llm_score_item(item)
                scored.append(scored_item)
                progress.advance(task)
                if i < len(candidates) - 1:
                    time.sleep(delay)

    scored.sort(key=lambda x: x.total_score, reverse=True)

    final_top_k = config.get("scoring", {}).get("final_top_k", 5)
    top = scored[:final_top_k]

    _logger.info("LLM batch scoring complete", extra={"selected_count": len(top)})
    for i, s in enumerate(top, 1):
        _logger.debug("Top item", extra={"rank": i, "title": s.item.title[:60], "total_score": round(s.total_score)})

    return top
