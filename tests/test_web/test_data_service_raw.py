"""get_raw_by_url() 測試。"""

from __future__ import annotations

import json

import pytest


@pytest.fixture
def raw_day(tmp_path, monkeypatch):
    # why 用 monkeypatch.setattr 而非 chdir：RAW_DIR 是由 PROJECT_ROOT 推導的絕對路徑，
    # 換 cwd 不會改變它（chdir 會讓測試讀到專案真實的 data/raw）
    from src.web import data_service

    d = tmp_path / "data/raw"
    d.mkdir(parents=True)
    monkeypatch.setattr(data_service, "RAW_DIR", d)
    (d / "2026-07-27.json").write_text(
        json.dumps([
            {"source": "hf_papers", "source_name": "HuggingFace Daily Papers",
             "title": "Skill Self-Play", "url": "https://huggingface.co/papers/2607.1",
             "authors": ["A", "B"], "abstract": "An abstract.", "tags": ["LLM"],
             "organization": "HF", "published_date": "2026-07-27",
             # stars_today: 0 用來釘住「0 值不入列」；arxiv_id 用來釘住「非數值不入列」
             "raw_metadata": {"upvotes": 42, "stars_today": 0, "arxiv_id": "2607.1"}},
        ], ensure_ascii=False),
        encoding="utf-8",
    )
    return tmp_path


def test_finds_item_by_exact_url(raw_day):
    from src.web.data_service import get_raw_by_url

    got = get_raw_by_url("2026-07-27", "https://huggingface.co/papers/2607.1")
    assert got is not None
    assert got["title"] == "Skill Self-Play"
    assert got["abstract"] == "An abstract."
    assert got["authors"] == ["A", "B"]
    assert got["collected_date"] == "2026-07-27"


def test_matches_despite_trailing_slash_and_scheme(raw_day):
    from src.web.data_service import get_raw_by_url

    assert get_raw_by_url("2026-07-27", "http://huggingface.co/papers/2607.1/") is not None


def test_uses_light_normalization_not_the_dedup_one(raw_day):
    """釘住呼叫端用的是 normalize_url_light（與 enrich.ts 一致），而非去重用的 normalize_url。

    raw 裡存的是帶 `www.` 與特定 query 順序的 URL；去重版會把兩者都抹平因而命中，
    輕量版則維持與 Astro 端相同的嚴格比對。這裡不是在主張「不該命中比較好」，
    而是在把「兩個前端用同一套規則」這件事釘死——兩端規則分歧時 box 會靜默消失。
    """
    import json

    from src.web.data_service import get_raw_by_url

    d = raw_day / "data/raw"
    (d / "2026-07-26.json").write_text(
        json.dumps([
            {"source": "rss", "source_name": "Blog", "title": "T",
             "url": "https://www.example.com/a?b=2&a=1", "authors": [],
             "abstract": "x", "tags": [], "organization": "",
             "published_date": "2026-07-26", "raw_metadata": {}},
        ]),
        encoding="utf-8",
    )

    # 完全相同的字串（+ 尾斜線 / http:）→ 命中
    assert get_raw_by_url("2026-07-26", "http://www.example.com/a?b=2&a=1/") is not None
    # 只有去重版才會抹平的差異 → 不命中
    assert get_raw_by_url("2026-07-26", "https://example.com/a?b=2&a=1") is None
    assert get_raw_by_url("2026-07-26", "https://www.example.com/a?a=1&b=2") is None


def test_returns_none_when_url_absent(raw_day):
    from src.web.data_service import get_raw_by_url

    assert get_raw_by_url("2026-07-27", "https://example.com/nope") is None


def test_returns_none_when_no_raw_file(raw_day):
    from src.web.data_service import get_raw_by_url

    assert get_raw_by_url("2020-01-01", "https://huggingface.co/papers/2607.1") is None


def test_exposes_only_positive_signals(raw_day):
    from src.web.data_service import get_raw_by_url

    got = get_raw_by_url("2026-07-27", "https://huggingface.co/papers/2607.1")
    # arxiv_id 非數值不列入；stars_today 為 0 也不列入
    assert got["signals"] == [("👍 upvotes", 42)]
    assert all(label != "⭐ stars today" for label, _ in got["signals"])


# ──────────────────────────────────────────────────────────
# Route 層：post_view / note_view 共用 post_view.html
#
# why 要在這裡打真實 route：`{% if raw_item %}` 是唯一擋住 note 頁 500 的東西
# （note_view 不傳 raw_item，少了 guard 會 UndefinedError），
# 而 tests/test_web/ 原本沒有任何測試打過 /post/ 或 /note/。
# ──────────────────────────────────────────────────────────

_SIDEBAR_STATS = {
    "total_posts": 0, "total_notes": 0, "today_posts": 0,
    "today_notes": 0, "total_materials": 0, "bookmarks_count": 0,
}


@pytest.fixture
def client(monkeypatch):
    from unittest.mock import MagicMock
    from fastapi.testclient import TestClient

    import src.web.app as app_module

    mock_ds = MagicMock()
    mock_ds.get_sidebar_stats.return_value = _SIDEBAR_STATS
    mock_ds.get_feedback.return_value = None
    monkeypatch.setattr(app_module, "ds", mock_ds)
    return TestClient(app_module.app), mock_ds


def test_note_view_renders_without_raw_box(client):
    """note_view 不傳 raw_item：頁面須正常回 200 且不含 box（不是 500）。"""
    tc, mock_ds = client
    mock_ds.get_note.return_value = {
        "frontmatter": {"title": "某篇筆記"}, "body": "# 內文", "filename": "n.md",
    }

    resp = tc.get("/note/2026-07-27/some-note")

    assert resp.status_code == 200
    assert "<details" not in resp.text
    assert "來源原標題" not in resp.text


def test_post_view_renders_raw_box(client):
    """post_view 有 raw_item：box 須渲染且帶入欄位值。"""
    tc, mock_ds = client
    mock_ds.get_post.return_value = {
        "frontmatter": {"title": "某篇文章", "url": "https://example.com/a"},
        "body": "# 內文", "filename": "p.md",
    }
    mock_ds.get_raw_by_url.return_value = {
        "title": "Source Title", "abstract": "Source abstract.",
        "authors": ["A"], "organization": "HF", "tags": ["LLM"],
        "source_name": "HuggingFace Daily Papers", "url": "https://example.com/a",
        "collected_date": "2026-07-27", "signals": [("👍 upvotes", 42)],
    }

    resp = tc.get("/post/2026-07-27/some-post")

    assert resp.status_code == 200
    assert "<details" in resp.text
    assert "Source Title" in resp.text
    assert "👍 upvotes 42" in resp.text
    mock_ds.get_raw_by_url.assert_called_once_with("2026-07-27", "https://example.com/a")


def test_post_view_without_raw_match_renders_no_box(client):
    """查無當日 raw（get_raw_by_url 回 None）：頁面正常，box 不渲染。"""
    tc, mock_ds = client
    mock_ds.get_post.return_value = {
        "frontmatter": {"title": "某篇文章", "url": "https://example.com/missing"},
        "body": "# 內文", "filename": "p.md",
    }
    mock_ds.get_raw_by_url.return_value = None

    resp = tc.get("/post/2026-07-27/some-post")

    assert resp.status_code == 200
    assert "<details" not in resp.text


# ──────────────────────────────────────────────────────────
# Web Monitor 讀 data/raw 的兩個呼叫點：顯示文字必須等於磁碟上的原文
#
# 同一頁的「原始資料 box」（get_raw_by_url）直接讀 dict，這兩支若多套一次
# Layer A 的 s2twp，並列時同一段文字會顯示不一致——無 log、無 exception。
# ──────────────────────────────────────────────────────────

DRIFTING = "這個文件的參數設定"  # s2twp 再套一次 → 這個檔案的參數設定
DRIFTING_TAG = "高性價比"


@pytest.fixture
def drifting_day(tmp_path, monkeypatch):
    """raw 裡放已是 Layer A 成品、但 s2twp 對它不冪等的文字；刻意不建 scored。"""
    from src.web import data_service

    raw_dir = tmp_path / "data/raw"
    scored_dir = tmp_path / "data/scored"
    raw_dir.mkdir(parents=True)
    scored_dir.mkdir(parents=True)
    monkeypatch.setattr(data_service, "RAW_DIR", raw_dir)
    monkeypatch.setattr(data_service, "SCORED_DIR", scored_dir)
    (raw_dir / "2026-07-27.json").write_text(
        json.dumps([
            {"source": "github", "source_name": "GitHub Trending",
             "title": DRIFTING, "url": "https://github.com/org/repo",
             "authors": [], "abstract": DRIFTING * 3, "tags": [DRIFTING_TAG],
             "organization": "", "published_date": "2026-07-27",
             "raw_metadata": {"stars_today": 10}},
        ], ensure_ascii=False),
        encoding="utf-8",
    )
    return tmp_path


def test_premise_these_strings_really_drift():
    from src.utils import to_traditional

    assert to_traditional(DRIFTING) != DRIFTING
    assert to_traditional(DRIFTING_TAG) != DRIFTING_TAG


def test_get_day_raw_items_text_matches_disk(drifting_day):
    from datetime import date

    from src.web.data_service import get_day_raw_items

    got = get_day_raw_items(date(2026, 7, 27))
    assert len(got) == 1
    assert got[0]["title"] == DRIFTING
    assert got[0]["abstract"] == DRIFTING * 3
    assert got[0]["tags"] == [DRIFTING_TAG]


def test_get_all_day_items_text_matches_disk(drifting_day):
    """未評分項目走 raw 分支（故 fixture 刻意不建 scored 檔）。"""
    from datetime import date

    from src.web.data_service import get_all_day_items

    got = get_all_day_items(date(2026, 7, 27))
    assert len(got) == 1
    assert got[0]["scored"] is False
    assert got[0]["title"] == DRIFTING


def test_monitor_and_raw_box_agree(drifting_day):
    """兩個前端讀同一批 raw：素材庫列表與「原始資料 box」的文字必須逐字相同。"""
    from datetime import date

    from src.web.data_service import get_day_raw_items, get_raw_by_url

    listed = get_day_raw_items(date(2026, 7, 27))[0]
    box = get_raw_by_url("2026-07-27", "https://github.com/org/repo")
    assert box is not None
    assert listed["title"] == box["title"]
    assert listed["abstract"] == box["abstract"]
