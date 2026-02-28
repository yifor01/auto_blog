"""每日精選摘要生成器（模板式，不需 LLM）。"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from src.models import ScoredItem
from src.utils import DIGESTS_DIR


def generate_digest(items: list[ScoredItem], target_date: date) -> str:
    """根據 scored items 生成 Markdown 每日摘要。

    結構：
    - Top Picks（total_score > 80）完整卡片
    - Worth Watching 表格
    - Quick Stats
    """
    date_str = target_date.isoformat()

    # 按 total_score 降序
    sorted_items = sorted(items, key=lambda x: x.total_score, reverse=True)

    top_picks = [it for it in sorted_items if it.total_score > 80]
    worth_watching = [it for it in sorted_items if it.total_score <= 80]

    # 統計
    total = len(sorted_items)
    avg_score = sum(it.total_score for it in sorted_items) / total if total else 0
    sources: dict[str, int] = {}
    for it in sorted_items:
        src = it.item.source_name or it.item.source.value
        sources[src] = sources.get(src, 0) + 1
    top_source = max(sources, key=sources.get) if sources else "N/A"

    lines: list[str] = []

    # Header
    lines.append(f"---")
    lines.append(f"title: 每日精選摘要 — {date_str}")
    lines.append(f"date: {date_str}")
    lines.append(f"type: digest")
    lines.append(f"total_items: {total}")
    lines.append(f"avg_score: {avg_score:.1f}")
    lines.append(f"---")
    lines.append("")
    lines.append(f"# 每日精選摘要 — {date_str}")
    lines.append("")

    # Quick Stats
    lines.append("## Quick Stats")
    lines.append("")
    lines.append(f"| 指標 | 數值 |")
    lines.append(f"|------|------|")
    lines.append(f"| 評分素材總數 | {total} |")
    lines.append(f"| 平均分數 | {avg_score:.1f} |")
    lines.append(f"| Top Picks (>80) | {len(top_picks)} |")
    lines.append(f"| 主要來源 | {top_source} |")
    lines.append("")

    # Top Picks
    if top_picks:
        lines.append("## Top Picks")
        lines.append("")
        for i, it in enumerate(top_picks, 1):
            tags_str = ", ".join(it.item.tags[:5]) if it.item.tags else ""
            lines.append(f"### {i}. {it.item.title}")
            lines.append("")
            lines.append(f"- **來源**: {it.item.source_name or it.item.source.value}")
            if it.item.organization:
                lines.append(f"- **機構**: {it.item.organization}")
            if it.item.authors:
                lines.append(f"- **作者**: {', '.join(it.item.authors[:3])}")
            lines.append(f"- **分數**: {it.total_score:.0f} (規則: {it.rule_score:.0f}, LLM: {it.llm_score or 0:.0f})")
            if tags_str:
                lines.append(f"- **標籤**: {tags_str}")
            lines.append(f"- **連結**: [{it.item.title[:40]}]({it.item.url})")
            if it.llm_reason:
                lines.append(f"- **評語**: {it.llm_reason}")
            if it.item.abstract:
                abstract_short = it.item.abstract[:200]
                if len(it.item.abstract) > 200:
                    abstract_short += "..."
                lines.append(f"\n> {abstract_short}")
            lines.append("")
    else:
        lines.append("## Top Picks")
        lines.append("")
        lines.append("今日無分數超過 80 的 Top Pick。")
        lines.append("")

    # Worth Watching
    if worth_watching:
        lines.append("## Worth Watching")
        lines.append("")
        lines.append("| # | 標題 | 來源 | 分數 |")
        lines.append("|---|------|------|------|")
        for i, it in enumerate(worth_watching[:20], 1):
            title_short = it.item.title[:50]
            if len(it.item.title) > 50:
                title_short += "..."
            src = it.item.source_name or it.item.source.value
            lines.append(f"| {i} | [{title_short}]({it.item.url}) | {src} | {it.total_score:.0f} |")
        lines.append("")

    # Source breakdown
    lines.append("## 來源分布")
    lines.append("")
    lines.append("| 來源 | 數量 |")
    lines.append("|------|------|")
    for src, count in sorted(sources.items(), key=lambda x: x[1], reverse=True):
        lines.append(f"| {src} | {count} |")
    lines.append("")

    return "\n".join(lines)


def generate_and_save_digest(items: list[ScoredItem], target_date: date) -> Path:
    """生成並儲存每日摘要 Markdown。"""
    content = generate_digest(items, target_date)
    path = DIGESTS_DIR / f"{target_date.isoformat()}.md"
    path.write_text(content, encoding="utf-8")
    return path
