"""Pydantic model 驗證測試。"""

from __future__ import annotations

from datetime import date, datetime

import pytest

from src.models import ContentItem, GeneratedContent, ScoredItem, SourceType


class TestContentItem:
    def test_dedup_key_prefers_arxiv_id(self):
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Test",
            url="https://arxiv.org/abs/2601.00001",
            published_date=date(2026, 2, 26),
            raw_metadata={"arxiv_id": "2601.00001"},
        )
        assert item.dedup_key() == "arxiv:2601.00001"

    def test_dedup_key_falls_back_to_url(self):
        item = ContentItem(
            source=SourceType.RSS,
            title="News",
            url="https://example.com/article",
            published_date=date(2026, 2, 26),
        )
        assert item.dedup_key() == "https://example.com/article"

    def test_dedup_key_github_uses_url(self):
        item = ContentItem(
            source=SourceType.GITHUB,
            title="repo",
            url="https://github.com/user/repo",
            published_date=date(2026, 2, 26),
        )
        assert item.dedup_key() == "https://github.com/user/repo"

    def test_default_fields(self):
        item = ContentItem(
            source=SourceType.BLOG,
            title="Blog Post",
            url="https://blog.com/post",
            published_date=date(2026, 2, 26),
        )
        assert item.authors == []
        assert item.abstract == ""
        assert item.organization == ""
        assert item.tags == []
        assert item.raw_metadata == {}


class TestScoredItem:
    def test_total_score_with_llm(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0, llm_score=75.0)
        assert item.total_score == 105.0

    def test_total_score_without_llm(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0)
        assert item.llm_score is None
        assert item.total_score == 30.0

    def test_practicality_field_exists(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0, practicality=14.0)
        assert item.practicality == 14.0

    def test_trending_field(self, arxiv_item):
        item = ScoredItem(item=arxiv_item, rule_score=30.0, trending=15.0)
        assert item.trending == 15.0

    def test_backward_compat_relevance_maps_to_trending(self, arxiv_item):
        """B3 向後相容：舊 JSON 的 relevance 欄位應對應到 trending。"""
        data = {
            "item": arxiv_item.model_dump(),
            "rule_score": 30.0,
            "relevance": 15.0,   # 舊欄位名
        }
        item = ScoredItem(**data)
        assert item.trending == 15.0

    def test_new_format_both_fields(self, arxiv_item):
        """新格式 trending 與 practicality 都能正常儲存。"""
        item = ScoredItem(
            item=arxiv_item,
            rule_score=30.0,
            llm_score=80.0,
            trending=18.0,
            practicality=16.0,
            novelty=17.0,
            impact=15.0,
            blog_worthiness=14.0,
        )
        assert item.trending == 18.0
        assert item.practicality == 16.0
        assert item.total_score == 110.0

    def test_zero_rule_score_floor(self, arxiv_item):
        """rule_score 可以是 0，total_score 不應為負。"""
        item = ScoredItem(item=arxiv_item, rule_score=0.0)
        assert item.total_score == 0.0
