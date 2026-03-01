"""Tests for abstract quality gate in blog post generator."""
from unittest.mock import MagicMock, patch
import pytest
from datetime import date
from src.generators.blog_post import generate_and_save_posts
from src.models import ContentItem, ScoredItem, SourceType


def _make_scored_item(abstract: str) -> ScoredItem:
    item = ContentItem(
        source=SourceType.BLOG,
        source_name="Test Blog",
        title="Test Article",
        url="https://example.com/test",
        authors=["Author"],
        abstract=abstract,
        published_date=date.today(),
        tags=["test"],
    )
    return ScoredItem(item=item, rule_score=80.0, llm_score=70.0)


def test_short_abstract_skips_generation():
    """abstract < 100 字元應跳過生成，回傳空 list。"""
    item = _make_scored_item("Short abstract.")  # < 100 chars
    with patch("src.generators.blog_post.generate_blog_post") as mock_gen:
        result = generate_and_save_posts([item], target_date=date.today())
        mock_gen.assert_not_called()
    assert result == []


def test_sufficient_abstract_generates():
    """abstract >= 100 字元應正常生成。"""
    long_abstract = "B" * 150  # 150 chars, >= 100
    item = _make_scored_item(long_abstract)
    mock_content = MagicMock()
    mock_content.source_item = item
    mock_content.content = "Generated blog post"
    mock_content.prompt_used = "prompt"
    mock_content.model_used = "test-model"
    from datetime import datetime
    mock_content.generated_at = datetime.now()
    with patch("src.generators.blog_post.generate_blog_post", return_value=mock_content):
        with patch("src.generators.blog_post.save_blog_post", return_value="/fake/path.md") as mock_save:
            result = generate_and_save_posts([item], target_date=date.today())
            mock_save.assert_called_once()
    assert result == ["/fake/path.md"]
