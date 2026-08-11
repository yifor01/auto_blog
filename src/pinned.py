"""頂尖 AI 公司官方 blog 免評分置頂挑選。

命中 config `pinned_organizations` 的 RSS/blog/cn_labs 來源當天（±1 天，容忍 UTC 時差）
發布項目，繞過評分直接生成，frontmatter 標 pinned。挑選為純函式、確定性，
score 階段（排除 pool）與 generate 階段（挑生成對象）呼叫同一份邏輯保持一致。
"""

from __future__ import annotations

from datetime import date

from src.models import ContentItem, ScoredItem, SourceType

# 允許前一天發布：pipeline 於 UTC 18:00 跑當日，官方 blog 常在收集時間之後發布、
# 隔天才進 raw，嚴格 == target_date 會漏掉大半
PINNED_WINDOW_DAYS = 1

PINNED_LLM_REASON = "📌 頂尖 AI 公司官方發布"


def _org_hit(org: str, pinned_orgs: list[str]) -> bool:
    if not org:
        return False
    org_lower = org.lower()
    return any(p.lower() in org_lower for p in pinned_orgs)


def select_pinned(
    items: list[ContentItem], target_date: date, config: dict
) -> list[ContentItem]:
    """挑出應置頂生成的官方 blog 項目（依日期新→舊，上限 pinned_daily_limit）。"""
    pinned_orgs = config.get("pinned_organizations", [])
    limit = config.get("pinned_daily_limit", 5)
    if not pinned_orgs:
        return []

    hits = [
        it
        for it in items
        if it.source in (SourceType.RSS, SourceType.BLOG, SourceType.CN_LABS)
        and abs((target_date - it.published_date).days) <= PINNED_WINDOW_DAYS
        and _org_hit(it.organization, pinned_orgs)
    ]
    hits.sort(key=lambda it: it.published_date, reverse=True)
    return hits[:limit]


def to_pinned_scored(item: ContentItem) -> ScoredItem:
    """包成 pseudo-ScoredItem 走現有 generator（分數 0、理由標明置頂）。"""
    return ScoredItem(item=item, rule_score=0.0, rule_reasons=["pinned"], llm_reason=PINNED_LLM_REASON)
