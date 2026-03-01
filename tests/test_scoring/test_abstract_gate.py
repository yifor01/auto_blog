"""Tests for abstract quality gate in LLM scorer."""
from unittest.mock import MagicMock, patch
import pytest
from src.scoring.scorer import batch_llm_score
from src.models import ContentItem, ScoredItem, SourceType
from datetime import date


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
    return ScoredItem(item=item, rule_score=30.0)


def test_empty_abstract_skips_llm_scoring():
    """abstract="" 的 item 應該跳過 LLM 評分。"""
    item = _make_scored_item("")
    with patch("src.scoring.scorer.llm_score_item") as mock_llm:
        result = batch_llm_score([item], config={"scoring": {"llm_top_k": 5, "final_top_k": 5}, "llm": {"request_delay_seconds": 0}})
        mock_llm.assert_not_called()
    assert len(result) == 1


def test_short_abstract_skips_llm_scoring():
    """abstract < 50 字元的 item 應該跳過 LLM 評分。"""
    item = _make_scored_item("Too short abstract.")  # < 50 chars
    with patch("src.scoring.scorer.llm_score_item") as mock_llm:
        result = batch_llm_score([item], config={"scoring": {"llm_top_k": 5, "final_top_k": 5}, "llm": {"request_delay_seconds": 0}})
        mock_llm.assert_not_called()
    assert len(result) == 1


def test_sufficient_abstract_calls_llm():
    """abstract >= 50 字元的 item 應該正常呼叫 LLM 評分。"""
    long_abstract = "A" * 100  # 100 chars, >= 50
    item = _make_scored_item(long_abstract)
    mock_scored = MagicMock()
    mock_scored.total_score = 80.0
    with patch("src.scoring.scorer.llm_score_item", return_value=mock_scored) as mock_llm:
        result = batch_llm_score([item], config={"scoring": {"llm_top_k": 5, "final_top_k": 5}, "llm": {"request_delay_seconds": 0}})
        mock_llm.assert_called_once()
