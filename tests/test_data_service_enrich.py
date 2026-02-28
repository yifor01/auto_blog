"""測試 data_service 的 scored 跨查與 feedback 聚合功能。"""
from __future__ import annotations

import json
from pathlib import Path

import pytest


@pytest.fixture
def tmp_project(tmp_path):
    """建立最小化的 output/posts、data/scored、data/feedback 目錄結構。"""
    posts_dir = tmp_path / "output" / "posts"
    notes_dir = tmp_path / "output" / "notes"
    scored_dir = tmp_path / "data" / "scored"
    feedback_dir = tmp_path / "data" / "feedback"
    for d in [posts_dir, notes_dir, scored_dir, feedback_dir]:
        d.mkdir(parents=True)

    # 一篇 post
    post = posts_dir / "2026-02-27_test-paper.md"
    post.write_text(
        "---\ntitle: \"Test Paper\"\nsource: arXiv\nurl: https://example.com\n"
        "score: 95\nmodel: test\ngenerated_at: 2026-02-27T10:00:00\n---\n\n"
        "Body text here for word count. " * 50,
        encoding="utf-8",
    )

    # 對應的 scored JSON
    scored = [
        {
            "item": {
                "source": "arxiv",
                "source_name": "arXiv",
                "title": "Test Paper",
                "url": "https://example.com",
                "authors": [],
                "abstract": "",
                "published_date": "2026-02-27",
                "organization": "",
                "raw_metadata": {},
            },
            "rule_score": 45.0,
            "rule_reasons": [],
            "llm_score": 50.0,
            "llm_reason": "Good paper",
            "novelty": 18.0,
            "impact": 16.0,
            "trending": 15.0,
            "practicality": 14.0,
            "blog_worthiness": 17.0,
        }
    ]
    (scored_dir / "2026-02-27.json").write_text(
        json.dumps(scored), encoding="utf-8"
    )

    # feedback
    (feedback_dir / "2026-02-27.json").write_text(
        json.dumps({"test-paper": "good"}), encoding="utf-8"
    )

    return {
        "root": tmp_path,
        "posts_dir": posts_dir,
        "notes_dir": notes_dir,
        "scored_dir": scored_dir,
        "feedback_dir": feedback_dir,
    }


def test_load_scored_for_date_returns_title_keyed_dict(tmp_project, monkeypatch):
    """_load_scored_for_date 應回傳以 title 為 key 的 dict。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    result = ds._load_scored_for_date("2026-02-27")

    assert "Test Paper" in result
    assert result["Test Paper"]["novelty"] == 18.0
    assert result["Test Paper"]["impact"] == 16.0
    assert result["Test Paper"]["llm_score"] == 50.0


def test_load_scored_for_date_missing_returns_empty(tmp_project, monkeypatch):
    """日期不存在時回傳空 dict，不拋例外。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    result = ds._load_scored_for_date("2099-01-01")
    assert result == {}


def test_enrich_with_scored_fills_5d(tmp_project, monkeypatch):
    """_enrich_with_scored 應填入 5D 分數。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    item = {"date_str": "2026-02-27", "title": "Test Paper", "slug": "test-paper"}
    enriched = ds._enrich_with_scored(item)

    assert enriched["novelty"] == 18.0
    assert enriched["trending"] == 15.0
    assert enriched["llm_score"] == 50.0
    assert enriched["source_name"] == "arXiv"


def test_enrich_with_scored_no_match_returns_unchanged(tmp_project, monkeypatch):
    """找不到對應項目時，原 item 不受影響。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    item = {"date_str": "2026-02-27", "title": "Non-existent Paper", "slug": "none"}
    enriched = ds._enrich_with_scored(item)

    assert enriched.get("novelty") is None
    assert enriched["title"] == "Non-existent Paper"


def test_get_all_feedback_returns_flat_map(tmp_project, monkeypatch):
    """get_all_feedback 應回傳 {date_slug: rating} 格式。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "FEEDBACK_DIR", tmp_project["feedback_dir"])

    result = ds.get_all_feedback()

    assert result["2026-02-27_test-paper"] == "good"


def test_list_all_posts_includes_feedback_and_5d(tmp_project, monkeypatch):
    """list_all_posts 回傳項目應含 feedback 與 5D 分數。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "POSTS_DIR", tmp_project["posts_dir"])
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "FEEDBACK_DIR", tmp_project["feedback_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    posts = ds.list_all_posts()

    assert len(posts) == 1
    p = posts[0]
    assert p["feedback"] == "good"
    assert p["novelty"] == 18.0
    assert p["fm_score"] == 95.0
    assert p["source_fm"] == "arXiv"
