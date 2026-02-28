"""去重邏輯測試（單日 + 跨日）。"""

from __future__ import annotations

import json
import tempfile
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import patch

import pytest

from src.models import ContentItem, SourceType
from src.utils import get_seen_urls


# ──────────────────────────────────────────────────────────
# dedup_key 測試
# ──────────────────────────────────────────────────────────

class TestDedupKey:
    def test_arxiv_id_dedup_key(self):
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Paper",
            url="https://arxiv.org/abs/2601.00001",
            published_date=date(2026, 2, 26),
            raw_metadata={"arxiv_id": "2601.00001"},
        )
        assert item.dedup_key() == "arxiv:2601.00001"

    def test_chatpaper_same_arxiv_id_deduplicates(self):
        """ChatPaper 和 arXiv 的同一論文應被去重（相同 arxiv_id）。"""
        arxiv = ContentItem(
            source=SourceType.ARXIV,
            title="Paper A",
            url="https://arxiv.org/abs/2601.00001",
            published_date=date(2026, 2, 26),
            raw_metadata={"arxiv_id": "2601.00001"},
        )
        chatpaper = ContentItem(
            source=SourceType.CHATPAPER,
            title="Paper A (ChatPaper)",
            url="https://chatpaper.com/paper/2601.00001",
            published_date=date(2026, 2, 26),
            raw_metadata={"arxiv_id": "2601.00001"},
        )
        assert arxiv.dedup_key() == chatpaper.dedup_key()

    def test_different_urls_different_keys(self):
        a = ContentItem(
            source=SourceType.RSS,
            title="News 1",
            url="https://site.com/a",
            published_date=date(2026, 2, 26),
        )
        b = ContentItem(
            source=SourceType.RSS,
            title="News 2",
            url="https://site.com/b",
            published_date=date(2026, 2, 26),
        )
        assert a.dedup_key() != b.dedup_key()

    def test_single_day_dedup_logic(self):
        """單日去重：相同 key 的 items 只保留第一個。"""
        items = [
            ContentItem(
                source=SourceType.ARXIV,
                title="Paper",
                url=f"https://arxiv.org/abs/2601.00001",
                published_date=date(2026, 2, 26),
                raw_metadata={"arxiv_id": "2601.00001"},
            )
            for _ in range(3)  # 3 個相同的 items
        ]
        seen: set[str] = set()
        unique = []
        for item in items:
            key = item.dedup_key()
            if key not in seen:
                seen.add(key)
                unique.append(item)
        assert len(unique) == 1


# ──────────────────────────────────────────────────────────
# 跨日去重測試
# ──────────────────────────────────────────────────────────

class TestGetSeenUrls:
    def _make_raw_json(self, items_data: list[dict]) -> str:
        return json.dumps(items_data)

    def test_collects_urls_from_raw_files(self, tmp_path):
        """應從 RAW_DIR 中的 JSON 檔案收集 URL。"""
        raw_dir = tmp_path / "raw"
        raw_dir.mkdir()

        items = [
            {"url": "https://example.com/paper1", "raw_metadata": {}},
            {"url": "https://example.com/paper2", "raw_metadata": {"arxiv_id": "2601.00001"}},
        ]
        (raw_dir / "2026-02-25.json").write_text(json.dumps(items))

        with patch("src.utils.RAW_DIR", raw_dir):
            seen = get_seen_urls(exclude_date=date(2026, 2, 26), lookback_days=7)

        assert "https://example.com/paper1" in seen
        assert "https://example.com/paper2" in seen
        assert "arxiv:2601.00001" in seen

    def test_excludes_today_file(self, tmp_path):
        """exclude_date 對應的檔案不應被讀取。"""
        raw_dir = tmp_path / "raw"
        raw_dir.mkdir()

        today = date(2026, 2, 26)
        items_today = [{"url": "https://example.com/today", "raw_metadata": {}}]
        items_yesterday = [{"url": "https://example.com/yesterday", "raw_metadata": {}}]

        (raw_dir / f"{today.isoformat()}.json").write_text(json.dumps(items_today))
        (raw_dir / f"{(today - timedelta(days=1)).isoformat()}.json").write_text(
            json.dumps(items_yesterday)
        )

        with patch("src.utils.RAW_DIR", raw_dir):
            seen = get_seen_urls(exclude_date=today, lookback_days=7)

        assert "https://example.com/today" not in seen
        assert "https://example.com/yesterday" in seen

    def test_respects_lookback_days(self, tmp_path):
        """只回看 lookback_days 天，更舊的檔案不讀取。"""
        raw_dir = tmp_path / "raw"
        raw_dir.mkdir()

        today = date(2026, 2, 26)
        # 建立 3 天的資料
        for delta, url in [(1, "yesterday"), (3, "three_days_ago"), (10, "ten_days_ago")]:
            d = today - timedelta(days=delta)
            items = [{"url": f"https://example.com/{url}", "raw_metadata": {}}]
            (raw_dir / f"{d.isoformat()}.json").write_text(json.dumps(items))

        with patch("src.utils.RAW_DIR", raw_dir):
            seen = get_seen_urls(exclude_date=today, lookback_days=5)

        assert "https://example.com/yesterday" in seen
        assert "https://example.com/three_days_ago" in seen
        assert "https://example.com/ten_days_ago" not in seen  # 超出 lookback

    def test_handles_corrupt_json_gracefully(self, tmp_path):
        """損壞的 JSON 檔案不應導致崩潰。"""
        raw_dir = tmp_path / "raw"
        raw_dir.mkdir()

        (raw_dir / "2026-02-25.json").write_text("this is not json {{{")
        (raw_dir / "2026-02-24.json").write_text(
            json.dumps([{"url": "https://good.com", "raw_metadata": {}}])
        )

        with patch("src.utils.RAW_DIR", raw_dir):
            seen = get_seen_urls(exclude_date=date(2026, 2, 26), lookback_days=7)

        assert "https://good.com" in seen  # 正常檔案應被讀取

    def test_no_lookback_reads_all_files(self, tmp_path):
        """lookback_days=None 時讀取所有檔案（exclude_date 除外）。"""
        raw_dir = tmp_path / "raw"
        raw_dir.mkdir()

        today = date(2026, 2, 26)
        for delta, label in [(1, "d1"), (30, "d30"), (365, "d365")]:
            d = today - timedelta(days=delta)
            items = [{"url": f"https://example.com/{label}", "raw_metadata": {}}]
            (raw_dir / f"{d.isoformat()}.json").write_text(json.dumps(items))

        with patch("src.utils.RAW_DIR", raw_dir):
            seen = get_seen_urls(exclude_date=today, lookback_days=None)

        assert "https://example.com/d1" in seen
        assert "https://example.com/d30" in seen
        assert "https://example.com/d365" in seen
