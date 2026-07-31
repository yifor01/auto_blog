"""src/lists.py 清單建構測試。"""
from datetime import date

import pytest

from src.lists import LIST_SOURCES, build_day_lists, build_lists, get_lists_path
from src.models import ContentItem, SourceType

D = date(2026, 7, 21)


def _item(source, title, **meta):
    return ContentItem(
        source=source,
        source_name=source.value,
        title=title,
        url=f"https://example.com/{title.replace('/', '-')}",
        abstract="some abstract " * 5,
        published_date=D,
        raw_metadata=meta,
    )


CFG = {"lists": {"github_top_k": 2, "hf_top_k": 2, "other_papers_limit": 3}}


def test_list_sources_membership():
    assert LIST_SOURCES == {
        SourceType.GITHUB, SourceType.HF_PAPERS, SourceType.ARXIV,
        SourceType.CHATPAPER, SourceType.SEMANTIC_SCHOLAR,
    }


def test_github_sorted_by_stars_and_truncated():
    items = [
        _item(SourceType.GITHUB, "a/low", stars_today=5),
        _item(SourceType.GITHUB, "b/high", stars_today=500),
        _item(SourceType.GITHUB, "c/mid", stars_today=50),
    ]
    result = build_day_lists(items, D, CFG)
    assert [e["title"] for e in result["github"]] == ["b/high", "c/mid"]
    assert result["github"][0]["stars_today"] == 500
    assert result["github"][0]["slug"]  # slug 供詳情頁路由


def test_hf_sorted_by_upvotes():
    items = [
        _item(SourceType.HF_PAPERS, "paper low", upvotes=1, arxiv_id="2607.00001"),
        _item(SourceType.HF_PAPERS, "paper high", upvotes=99, arxiv_id="2607.00002"),
    ]
    result = build_day_lists(items, D, CFG)
    assert [e["title"] for e in result["papers"]["hf"]] == ["paper high", "paper low"]


def test_others_merged_sorted_truncated():
    items = [
        _item(SourceType.ARXIV, "arxiv paper", arxiv_id="2607.10001"),
        _item(SourceType.CHATPAPER, "chatpaper paper", arxiv_id="2607.10002"),
        _item(SourceType.SEMANTIC_SCHOLAR, "ss cited", arxiv_id="2607.10003", citation_count=42),
        _item(SourceType.SEMANTIC_SCHOLAR, "ss extra", arxiv_id="2607.10004", citation_count=7),
    ]
    result = build_day_lists(items, D, CFG)
    others = result["papers"]["others"]
    assert len(others) == 3  # other_papers_limit=3 截斷
    assert others[0]["title"] == "ss cited"  # citation_count 最高排最前


def test_missing_metadata_defaults_to_zero():
    items = [_item(SourceType.GITHUB, "a/nometa")]
    result = build_day_lists(items, D, CFG)
    assert result["github"][0]["stars_today"] == 0


def test_non_list_sources_excluded():
    items = [_item(SourceType.RSS, "some news")]
    result = build_day_lists(items, D, CFG)
    assert result["github"] == []
    assert result["papers"]["hf"] == []
    assert result["papers"]["others"] == []


def test_build_lists_checkpoint(tmp_path, monkeypatch):
    import src.lists as lists_mod
    monkeypatch.setattr(lists_mod, "LISTS_DIR", tmp_path)
    items = [_item(SourceType.GITHUB, "a/repo", stars_today=10)]
    first = build_lists(items, D)
    assert first is not None
    assert (tmp_path / "2026-07-21.json").exists()
    # 已存在 → 跳過
    assert build_lists(items, D) is None
    # force → 重建
    assert build_lists(items, D, force=True) is not None
