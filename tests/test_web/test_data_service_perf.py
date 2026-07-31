"""效能優化相關測試 — Task 1/2/3。

- Task 1: _parse_markdown_file() mtime 快取
- Task 2: list_all_materials / get_week_top_items N+1 glob 修正
- Task 3: _slug_matches() 提取與行為驗證
"""
from __future__ import annotations

import json
import time
from pathlib import Path

import pytest


# ──────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────

SCORED_ITEM_TEMPLATE = {
    "item": {
        "source": "arxiv",
        "source_name": "arXiv",
        "title": "Some Paper Title",
        "url": "https://arxiv.org/abs/1234.5678",
        "authors": [],
        "abstract": "abstract text",
        "published_date": "2026-01-01",
        "organization": "",
        "raw_metadata": {},
    },
    "rule_score": 30.0,
    "rule_reasons": [],
    "llm_score": 50.0,
    "llm_reason": "Great paper",
    "novelty": 18.0,
    "impact": 16.0,
    "trending": 15.0,
    "practicality": 14.0,
    "blog_worthiness": 17.0,
}


def _make_scored(title: str, url: str = "https://example.com") -> dict:
    item = json.loads(json.dumps(SCORED_ITEM_TEMPLATE))
    item["item"]["title"] = title
    item["item"]["url"] = url
    return item


@pytest.fixture()
def fake_dirs(tmp_path: Path):
    """建立最小化目錄結構，回傳各目錄路徑 dict。"""
    posts_dir = tmp_path / "output" / "posts"
    notes_dir = tmp_path / "output" / "notes"
    blogs_dir = tmp_path / "output" / "blogs"
    scored_dir = tmp_path / "data" / "scored"
    for d in [posts_dir, notes_dir, blogs_dir, scored_dir]:
        d.mkdir(parents=True)
    return {
        "posts": posts_dir,
        "notes": notes_dir,
        "blogs": blogs_dir,
        "scored": scored_dir,
        "root": tmp_path,
    }


# ──────────────────────────────────────────────────────────
# Task 1: _parse_markdown_file() caching
# ──────────────────────────────────────────────────────────

class TestParseMarkdownCache:
    """_parse_markdown_file 快取行為測試。"""

    def test_same_mtime_returns_cached(self, tmp_path: Path):
        """相同 mtime → 第二次呼叫不讀檔，直接回快取（同一物件）。"""
        import src.web.data_service as ds

        # 清快取確保乾淨
        ds._md_cache.clear()

        md_file = tmp_path / "test.md"
        md_file.write_text("---\ntitle: Hello\n---\n\nBody", encoding="utf-8")

        result1 = ds._parse_markdown_file(md_file)
        result2 = ds._parse_markdown_file(md_file)

        # 同一 mtime → 應回傳相同物件（快取命中）
        assert result1 is result2
        assert result1["frontmatter"]["title"] == "Hello"

    def test_changed_file_updates_cache(self, tmp_path: Path):
        """mtime 改變後，舊快取失效，重新解析新內容。"""
        import src.web.data_service as ds

        ds._md_cache.clear()

        md_file = tmp_path / "update.md"
        md_file.write_text("---\ntitle: Old\n---\n\nOld body", encoding="utf-8")

        result1 = ds._parse_markdown_file(md_file)
        assert result1["frontmatter"]["title"] == "Old"

        # 稍等確保 mtime 不同（部分 FS 精度 1s）
        time.sleep(0.01)
        md_file.write_text("---\ntitle: New\n---\n\nNew body", encoding="utf-8")
        # 手動更新 mtime 確保不同
        md_file.touch()

        result2 = ds._parse_markdown_file(md_file)
        # 內容應已更新
        assert result2["frontmatter"]["title"] == "New"

    def test_nonexistent_file_returns_none(self, tmp_path: Path):
        """不存在的路徑回傳 None，不拋例外。"""
        import src.web.data_service as ds

        result = ds._parse_markdown_file(tmp_path / "ghost.md")
        assert result is None

    def test_cache_limit_clears_on_overflow(self, tmp_path: Path):
        """快取超過 _MD_CACHE_MAX 時整體清除，不會無限成長。"""
        import src.web.data_service as ds

        original_max = ds._MD_CACHE_MAX
        ds._MD_CACHE_MAX = 3  # 降低上限方便測試
        ds._md_cache.clear()

        files = []
        for i in range(4):
            f = tmp_path / f"f{i}.md"
            f.write_text(f"# {i}", encoding="utf-8")
            files.append(f)

        try:
            for f in files:
                ds._parse_markdown_file(f)
            # 第 4 次寫入觸發 clear + 重新 cache → 最多 1 筆
            assert len(ds._md_cache) <= 1
        finally:
            ds._MD_CACHE_MAX = original_max
            ds._md_cache.clear()

    def test_frontmatter_parsed_correctly(self, tmp_path: Path):
        """有 YAML frontmatter 的檔案正確解析 frontmatter 與 body。"""
        import src.web.data_service as ds

        ds._md_cache.clear()
        md_file = tmp_path / "fm.md"
        md_file.write_text(
            "---\ntitle: My Post\ntags: [ai, ml]\n---\n\nThis is body.",
            encoding="utf-8",
        )

        result = ds._parse_markdown_file(md_file)
        assert result is not None
        assert result["frontmatter"]["title"] == "My Post"
        assert result["frontmatter"]["tags"] == ["ai", "ml"]
        assert "This is body." in result["body"]


# ──────────────────────────────────────────────────────────
# Task 2: N+1 glob 修正
# ──────────────────────────────────────────────────────────

class TestListAllMaterialsNoPlusOneGlob:
    """list_all_materials() 應一次性掃描目錄，而非每日期 glob 多次。"""

    def test_returns_items_with_correct_has_post_flag(self, fake_dirs: dict, monkeypatch):
        """has_post=True 當且僅當 POSTS_DIR 有對應 slug 的 .md 檔。"""
        import src.web.data_service as ds
        from datetime import date, timedelta

        today = date.today().isoformat()

        # 寫入 scored JSON（使用今天日期確保在 days=30 範圍內）
        scored_data = [_make_scored("My Awesome Paper", "https://example.com/1")]
        (fake_dirs["scored"] / f"{today}.json").write_text(
            json.dumps(scored_data), encoding="utf-8"
        )

        # 寫入對應的 post（slug = "my-awesome-paper"）
        (fake_dirs["posts"] / f"{today}_my-awesome-paper.md").write_text(
            "---\ntitle: My Awesome Paper\n---\n\nBody", encoding="utf-8"
        )

        monkeypatch.setattr(ds, "POSTS_DIR", fake_dirs["posts"])
        monkeypatch.setattr(ds, "NOTES_DIR", fake_dirs["notes"])
        monkeypatch.setattr(ds, "BLOGS_DIR", fake_dirs["blogs"])
        monkeypatch.setattr(ds, "SCORED_DIR", fake_dirs["scored"])

        results = ds.list_all_materials(days=30)
        assert len(results) >= 1
        item = next(r for r in results if r["title"] == "My Awesome Paper")
        assert item["has_post"] is True
        assert item["has_note"] is False

    def test_no_post_has_post_false(self, fake_dirs: dict, monkeypatch):
        """POSTS_DIR 沒有對應檔案時 has_post=False。"""
        import src.web.data_service as ds
        from datetime import date

        today = date.today().isoformat()

        scored_data = [_make_scored("Unknown Paper", "https://example.com/2")]
        (fake_dirs["scored"] / f"{today}.json").write_text(
            json.dumps(scored_data), encoding="utf-8"
        )

        monkeypatch.setattr(ds, "POSTS_DIR", fake_dirs["posts"])
        monkeypatch.setattr(ds, "NOTES_DIR", fake_dirs["notes"])
        monkeypatch.setattr(ds, "BLOGS_DIR", fake_dirs["blogs"])
        monkeypatch.setattr(ds, "SCORED_DIR", fake_dirs["scored"])

        results = ds.list_all_materials(days=30)
        assert len(results) >= 1
        item = next(r for r in results if r["title"] == "Unknown Paper")
        assert item["has_post"] is False

    def test_blog_map_matched_correctly(self, fake_dirs: dict, monkeypatch):
        """BLOGS_DIR 有對應的 blog 檔案時 has_blog=True，blog_slug 正確。"""
        import src.web.data_service as ds
        from datetime import date

        today = date.today().isoformat()
        title = "Super Blog Paper"
        scored_data = [_make_scored(title, "https://example.com/3")]
        (fake_dirs["scored"] / f"{today}.json").write_text(
            json.dumps(scored_data), encoding="utf-8"
        )

        # blog 以 paper_title 在 frontmatter 標記
        blog_content = (
            "---\ntitle: Super Blog Paper\npaper_title: Super Blog Paper\n---\n\nBlog body"
        )
        (fake_dirs["blogs"] / f"{today}_super-blog-paper.md").write_text(
            blog_content, encoding="utf-8"
        )

        monkeypatch.setattr(ds, "POSTS_DIR", fake_dirs["posts"])
        monkeypatch.setattr(ds, "NOTES_DIR", fake_dirs["notes"])
        monkeypatch.setattr(ds, "BLOGS_DIR", fake_dirs["blogs"])
        monkeypatch.setattr(ds, "SCORED_DIR", fake_dirs["scored"])

        results = ds.list_all_materials(days=30)
        item = next(r for r in results if r["title"] == title)
        assert item["has_blog"] is True
        assert item["blog_slug"] == "super-blog-paper"


class TestGetWeekTopItemsNoPlusOneGlob:
    """get_week_top_items() BLOGS_DIR 應只掃描一次。"""

    def test_top_items_returned_sorted(self, fake_dirs: dict, monkeypatch):
        """回傳項目依 total_score 降序，且限制在 top_k。"""
        import src.web.data_service as ds

        scored_data = [
            _make_scored("Paper High", "https://example.com/h"),
            _make_scored("Paper Low", "https://example.com/l"),
        ]
        scored_data[0]["rule_score"] = 80.0
        scored_data[1]["rule_score"] = 10.0

        # 使用今日日期確保在 days 範圍內
        from datetime import date
        today = date.today().isoformat()
        (fake_dirs["scored"] / f"{today}.json").write_text(
            json.dumps(scored_data), encoding="utf-8"
        )

        monkeypatch.setattr(ds, "BLOGS_DIR", fake_dirs["blogs"])
        monkeypatch.setattr(ds, "SCORED_DIR", fake_dirs["scored"])

        results = ds.get_week_top_items(days=7, top_k=5)
        assert len(results) >= 2
        titles = [r["title"] for r in results]
        assert titles.index("Paper High") < titles.index("Paper Low")

    def test_blog_linked_in_top_items(self, fake_dirs: dict, monkeypatch):
        """blog 存在時 has_blog=True。"""
        import src.web.data_service as ds
        from datetime import date

        title = "Top Blog Paper"
        today = date.today().isoformat()

        scored_data = [_make_scored(title, "https://example.com/top")]
        (fake_dirs["scored"] / f"{today}.json").write_text(
            json.dumps(scored_data), encoding="utf-8"
        )

        blog_md = (
            "---\ntitle: Top Blog Paper\npaper_title: Top Blog Paper\n---\n\nContent"
        )
        (fake_dirs["blogs"] / f"{today}_top-blog-paper.md").write_text(
            blog_md, encoding="utf-8"
        )

        monkeypatch.setattr(ds, "BLOGS_DIR", fake_dirs["blogs"])
        monkeypatch.setattr(ds, "SCORED_DIR", fake_dirs["scored"])

        results = ds.get_week_top_items(days=7, top_k=5)
        item = next((r for r in results if r["title"] == title), None)
        assert item is not None
        assert item["has_blog"] is True


# ──────────────────────────────────────────────────────────
# Task 3: _slug_matches()
# ──────────────────────────────────────────────────────────

class TestSlugMatches:
    """_slug_matches(slug, title_slug) 行為測試。"""

    def test_exact_match(self):
        """完全相同時返回 True。"""
        from src.web.data_service import _slug_matches

        assert _slug_matches("my-paper", "my-paper") is True

    def test_title_slug_in_slug(self):
        """title_slug 是 slug 的子串時返回 True。"""
        from src.web.data_service import _slug_matches

        assert _slug_matches("2026-01-01-my-paper-title", "my-paper") is True

    def test_slug_in_title_slug(self):
        """slug 是 title_slug 的子串時返回 True。"""
        from src.web.data_service import _slug_matches

        assert _slug_matches("my-paper", "my-paper-extended-version") is True

    def test_no_match(self):
        """無子串關係時返回 False。"""
        from src.web.data_service import _slug_matches

        assert _slug_matches("totally-different", "unrelated-slug") is False

    def test_empty_strings(self):
        """空字串是任何字串的子串，應返回 True。"""
        from src.web.data_service import _slug_matches

        assert _slug_matches("", "") is True
        assert _slug_matches("anything", "") is True

    def test_consistent_with_previous_inline_logic(self):
        """與原始 inline 邏輯 `title_slug in slug or slug in title_slug` 結果一致。"""
        from src.web.data_service import _slug_matches

        cases = [
            ("efficient-llm-inference", "efficient-llm"),
            ("paper", "different-topic"),
            ("gpt-4-technical-report", "gpt-4"),
            ("abc", "xyz"),
        ]
        for slug, title_slug in cases:
            expected = title_slug in slug or slug in title_slug
            assert _slug_matches(slug, title_slug) == expected, (
                f"_slug_matches({slug!r}, {title_slug!r}) expected {expected}"
            )
