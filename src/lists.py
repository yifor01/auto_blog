"""清單型來源（GitHub Trending / Papers）每日清單建構。

這五個來源 LLM 拿不到全文、評分不可靠，退出評分 pipeline，
改用天然訊號（stars_today / upvotes / citation_count）排序成每日清單，
輸出 output/lists/{date}.json 供 Astro 靜態站與 Web Monitor 共用。零 LLM。
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import LISTS_DIR, console, load_config, save_json, slugify

_logger = get_logger("lists")

LIST_SOURCES = {
    SourceType.GITHUB,
    SourceType.HF_PAPERS,
    SourceType.ARXIV,
    SourceType.CHATPAPER,
    SourceType.SEMANTIC_SCHOLAR,
}

PAPER_SOURCES = {SourceType.ARXIV, SourceType.CHATPAPER, SourceType.SEMANTIC_SCHOLAR}


def get_lists_path(d: date) -> Path:
    return LISTS_DIR / f"{d.isoformat()}.json"


def _int_meta(item: ContentItem, key: str) -> int:
    try:
        return int(item.raw_metadata.get(key) or 0)
    except (TypeError, ValueError):
        return 0


def _github_entry(it: ContentItem) -> dict:
    return {
        "title": it.title,
        "slug": slugify(it.title),
        "url": it.url,
        "abstract": it.abstract,
        "stars_today": _int_meta(it, "stars_today"),
        "language": it.raw_metadata.get("language", ""),
    }


def _hf_entry(it: ContentItem) -> dict:
    return {
        "title": it.title,
        "slug": slugify(it.title),
        "url": it.url,
        "abstract": it.abstract,
        "upvotes": _int_meta(it, "upvotes"),
        "arxiv_id": it.raw_metadata.get("arxiv_id", ""),
        "authors": it.authors,
    }


def _other_entry(it: ContentItem) -> dict:
    return {
        "title": it.title,
        "slug": slugify(it.title),
        "url": it.url,
        "abstract": it.abstract,
        "source": it.source.value,
        "source_name": it.source_name,
        "citation_count": _int_meta(it, "citation_count"),
        "published_date": it.published_date.isoformat(),
        "authors": it.authors,
    }


def build_day_lists(
    items: list[ContentItem], target_date: date, config: dict | None = None
) -> dict:
    """純函式：從當日 items 篩出清單來源，排序＋截斷成 lists dict（不做 IO）。"""
    config = config or load_config()
    lists_cfg = config.get("lists", {})
    github_top_k = lists_cfg.get("github_top_k", 10)
    hf_top_k = lists_cfg.get("hf_top_k", 10)
    others_limit = lists_cfg.get("other_papers_limit", 30)

    github = sorted(
        (it for it in items if it.source == SourceType.GITHUB),
        key=lambda it: _int_meta(it, "stars_today"),
        reverse=True,
    )[:github_top_k]
    hf = sorted(
        (it for it in items if it.source == SourceType.HF_PAPERS),
        key=lambda it: _int_meta(it, "upvotes"),
        reverse=True,
    )[:hf_top_k]
    others = sorted(
        (it for it in items if it.source in PAPER_SOURCES),
        key=lambda it: (_int_meta(it, "citation_count"), it.published_date.isoformat()),
        reverse=True,
    )[:others_limit]

    return {
        "date": target_date.isoformat(),
        "github": [_github_entry(it) for it in github],
        "papers": {
            "hf": [_hf_entry(it) for it in hf],
            "others": [_other_entry(it) for it in others],
        },
    }


def build_lists(
    items: list[ContentItem], target_date: date, force: bool = False
) -> dict | None:
    """建構並寫入 output/lists/{date}.json。已存在且非 force → 跳過（checkpoint）。"""
    path = get_lists_path(target_date)
    if path.exists() and not force:
        return None
    data = build_day_lists(items, target_date)
    save_json(data, path)
    _logger.info(
        "Lists saved",
        extra={
            "date": str(target_date),
            "github": len(data["github"]),
            "hf": len(data["papers"]["hf"]),
            "others": len(data["papers"]["others"]),
        },
    )
    console.print(
        f"📋 Lists saved: {path.name} "
        f"(github {len(data['github'])} / hf {len(data['papers']['hf'])} "
        f"/ others {len(data['papers']['others'])})"
    )
    return data
