"""Web Monitor 置頂文章顯示測試（spec §3.2）。

涵蓋 data_service.get_day_pinned_posts + Day Detail 頁面 📌 置頂文章 區塊渲染。
"""
from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock

from fastapi.testclient import TestClient

import src.web.app as app_module
from src.web import data_service
from src.web.app import app

D = date(2026, 7, 21)


def _write_post(dir_, slug, *, pinned=None, title="示例標題", raw=None):
    if raw is not None:
        (dir_ / f"{D.isoformat()}_{slug}.md").write_text(raw, encoding="utf-8")
        return
    fm = f"title: {title}\n"
    if pinned is not None:
        fm += f"pinned: {str(pinned).lower()}\n"
    (dir_ / f"{D.isoformat()}_{slug}.md").write_text(
        f"---\n{fm}---\n\n內文", encoding="utf-8"
    )


# ──────────────────────────────────────────────────────────
# get_day_pinned_posts 單元測試
# ──────────────────────────────────────────────────────────

def test_pinned_post_found(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "POSTS_DIR", tmp_path)
    _write_post(tmp_path, "openai-gpt6", pinned=True, title="OpenAI GPT-6")
    got = data_service.get_day_pinned_posts(D)
    assert len(got) == 1
    assert got[0]["title"] == "OpenAI GPT-6"
    assert got[0]["filename"] == "2026-07-21_openai-gpt6.md"
    assert got[0]["url"] == "/post/2026-07-21/openai-gpt6"


def test_non_pinned_ignored(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "POSTS_DIR", tmp_path)
    _write_post(tmp_path, "regular", pinned=False)
    _write_post(tmp_path, "no-key")  # 無 pinned key
    assert data_service.get_day_pinned_posts(D) == []


def test_malformed_frontmatter_skipped(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "POSTS_DIR", tmp_path)
    # 損毀 YAML（縮排錯誤造成 parse 失敗）→ 跳過不炸
    _write_post(tmp_path, "broken", raw="---\ntitle: x\n  bad: : :\n---\n內文")
    _write_post(tmp_path, "ok", pinned=True, title="正常")
    got = data_service.get_day_pinned_posts(D)
    assert [p["title"] for p in got] == ["正常"]


def test_no_files_returns_empty(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "POSTS_DIR", tmp_path)
    assert data_service.get_day_pinned_posts(D) == []


# ──────────────────────────────────────────────────────────
# Day Detail 頁面 smoke test（TestClient）
# ──────────────────────────────────────────────────────────

def _mock_ds(pinned_posts):
    ds = MagicMock()
    ds.get_day_stats.return_value = {
        "date": D.isoformat(), "raw_count": 0, "scored_count": 0,
        "posts_count": 0, "notes_count": 0,
        "score_dist": [], "score_dist_labels": [], "source_counts": {},
    }
    ds.get_all_day_items.return_value = []
    ds.list_day_contents.return_value = []
    ds.get_pipeline_state.return_value = "done"
    ds.get_bookmarked_indices.return_value = set()
    ds.get_day_lists.return_value = None
    ds.get_day_pinned_posts.return_value = pinned_posts
    ds.get_sidebar_stats.return_value = {
        "total_posts": 0, "total_notes": 0, "today_posts": 0,
        "today_notes": 0, "total_materials": 0, "bookmarks_count": 0,
    }
    return ds


def test_day_page_shows_pinned_block(monkeypatch):
    pinned = [{"title": "OpenAI GPT-6", "filename": "x.md",
               "url": "/post/2026-07-21/openai-gpt6"}]
    monkeypatch.setattr(app_module, "ds", _mock_ds(pinned))
    resp = TestClient(app).get(f"/day/{D.isoformat()}")
    assert resp.status_code == 200
    assert "📌 置頂文章" in resp.text
    assert "/post/2026-07-21/openai-gpt6" in resp.text
    assert "OpenAI GPT-6" in resp.text


def test_day_page_no_pinned_block_when_empty(monkeypatch):
    monkeypatch.setattr(app_module, "ds", _mock_ds([]))
    resp = TestClient(app).get(f"/day/{D.isoformat()}")
    assert resp.status_code == 200
    assert "📌 置頂文章" not in resp.text
