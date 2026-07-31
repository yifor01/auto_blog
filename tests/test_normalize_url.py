"""normalize_url() 與其在 dedup_key / get_seen_urls 一致性的測試。"""

from __future__ import annotations

import json
from datetime import date
from unittest.mock import patch

from src.models import ContentItem, SourceType
from src.utils import get_seen_urls, normalize_url


class TestNormalizeUrl:
    def test_trailing_slash_removed(self):
        assert normalize_url("https://example.com/a/") == normalize_url(
            "https://example.com/a"
        )

    def test_http_and_https_equal(self):
        assert normalize_url("http://example.com/a") == normalize_url(
            "https://example.com/a"
        )

    def test_www_prefix_stripped(self):
        assert normalize_url("https://www.example.com/a") == normalize_url(
            "https://example.com/a"
        )

    def test_netloc_lowercased(self):
        assert normalize_url("https://Example.COM/a") == normalize_url(
            "https://example.com/a"
        )

    def test_utm_params_removed(self):
        assert normalize_url(
            "https://example.com/a?utm_source=x&utm_medium=y"
        ) == normalize_url("https://example.com/a")

    def test_tracking_params_removed(self):
        assert normalize_url(
            "https://example.com/a?fbclid=1&gclid=2&msclkid=3&ref=hn"
        ) == normalize_url("https://example.com/a")

    def test_query_order_normalized(self):
        assert normalize_url("https://example.com/a?b=2&a=1") == normalize_url(
            "https://example.com/a?a=1&b=2"
        )

    def test_real_query_preserved(self):
        assert normalize_url("https://example.com/a?id=42") == "https://example.com/a?id=42"

    def test_fragment_removed(self):
        assert normalize_url("https://example.com/a#section") == normalize_url(
            "https://example.com/a"
        )

    def test_empty_url(self):
        assert normalize_url("") == ""

    def test_combined(self):
        a = "http://WWW.Example.com/path/?utm_source=tw&b=2&a=1#frag"
        b = "https://example.com/path?a=1&b=2"
        assert normalize_url(a) == b


class TestDedupKeyNormalization:
    def _item(self, url: str) -> ContentItem:
        return ContentItem(
            source=SourceType.RSS,
            title="x",
            url=url,
            published_date=date(2026, 2, 26),
        )

    def test_url_variants_same_dedup_key(self):
        variants = [
            "https://site.com/post",
            "https://site.com/post/",
            "http://site.com/post",
            "https://www.site.com/post",
            "https://site.com/post?utm_source=fb",
        ]
        keys = {self._item(u).dedup_key() for u in variants}
        assert len(keys) == 1

    def test_arxiv_id_priority_unaffected(self):
        item = ContentItem(
            source=SourceType.ARXIV,
            title="p",
            url="https://arxiv.org/abs/2601.00001?utm_source=x",
            published_date=date(2026, 2, 26),
            raw_metadata={"arxiv_id": "2601.00001"},
        )
        assert item.dedup_key() == "arxiv:2601.00001"


class TestGetSeenUrlsConsistency:
    def test_seen_urls_normalized_match_dedup_key(self, tmp_path):
        """歷史 raw JSON 的 URL（帶 www / trailing slash / utm）正規化後，
        應與當天 ContentItem.dedup_key() 比對得到。"""
        raw_dir = tmp_path / "raw"
        raw_dir.mkdir()
        items = [{"url": "https://www.site.com/post/?utm_source=fb", "raw_metadata": {}}]
        (raw_dir / "2026-02-25.json").write_text(json.dumps(items))

        with patch("src.utils.RAW_DIR", raw_dir):
            seen = get_seen_urls(exclude_date=date(2026, 2, 26), lookback_days=7)

        today_item = ContentItem(
            source=SourceType.RSS,
            title="x",
            url="https://site.com/post",
            published_date=date(2026, 2, 26),
        )
        assert today_item.dedup_key() in seen


class TestArxivVersionNormalization:
    """arxiv_id 版本後綴正規化：跨來源（arxiv/hf_papers/semantic_scholar）去重。"""

    def _item(self, arxiv_id: str):
        from datetime import date

        from src.models import ContentItem, SourceType

        return ContentItem(
            source=SourceType.ARXIV,
            title="t",
            url="https://arxiv.org/abs/2606.11190",
            published_date=date(2026, 6, 10),
            raw_metadata={"arxiv_id": arxiv_id},
        )

    def test_version_suffix_stripped(self):
        assert self._item("2606.11190v1").dedup_key() == "arxiv:2606.11190"
        assert self._item("2606.11190v12").dedup_key() == "arxiv:2606.11190"

    def test_bare_id_unchanged(self):
        assert self._item("2606.11190").dedup_key() == "arxiv:2606.11190"

    def test_versioned_and_bare_collide(self):
        assert self._item("2606.11190v2").dedup_key() == self._item("2606.11190").dedup_key()
