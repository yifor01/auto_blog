"""測試 arXiv collector 的日期過濾與欄位映射。"""
from __future__ import annotations

from datetime import date, datetime, timezone
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

_CFG = {"collectors": {"arxiv": {"enabled": True, "categories": ["cs.AI"], "max_results": 50}}}


def _make_result(
    title: str = "A Reasoning Agent",
    entry_id: str = "http://arxiv.org/abs/2601.00123v1",
    published: datetime | None = None,
    summary: str = "We propose a novel framework. " * 10,
):
    return SimpleNamespace(
        title=title,
        entry_id=entry_id,
        published=published or datetime(2026, 2, 26, tzinfo=timezone.utc),
        authors=[SimpleNamespace(name="Alice"), SimpleNamespace(name="Bob")],
        summary=summary,
        categories=["cs.AI", "cs.LG"],
        primary_category="cs.AI",
        pdf_url="http://arxiv.org/pdf/2601.00123v1",
    )


def _patch_client(results: list):
    mock_client = MagicMock()
    mock_client.results.return_value = iter(results)
    return mock_client


@patch("src.collectors.arxiv_collector.load_config", return_value=_CFG)
@patch("src.collectors.arxiv_collector.arxiv")
def test_arxiv_maps_fields(mock_arxiv, _cfg):
    from src.collectors.arxiv_collector import ArxivCollector
    from src.models import SourceType

    mock_arxiv.Client.return_value = _patch_client([_make_result()])
    items = ArxivCollector().collect(target_date=date(2026, 2, 26))

    assert len(items) == 1
    it = items[0]
    assert it.source == SourceType.ARXIV
    assert it.title == "A Reasoning Agent"
    assert it.authors == ["Alice", "Bob"]
    # arxiv_id 取 entry_id 最後一段
    assert it.raw_metadata["arxiv_id"] == "2601.00123v1"
    assert "cs.AI" in it.tags


@patch("src.collectors.arxiv_collector.load_config", return_value=_CFG)
@patch("src.collectors.arxiv_collector.arxiv")
def test_arxiv_date_filter_excludes_too_old(mock_arxiv, _cfg):
    """published 早於 target_date - 2 天的應被排除。"""
    from src.collectors.arxiv_collector import ArxivCollector

    too_old = _make_result(published=datetime(2026, 2, 20, tzinfo=timezone.utc))
    in_range = _make_result(published=datetime(2026, 2, 25, tzinfo=timezone.utc))
    mock_arxiv.Client.return_value = _patch_client([too_old, in_range])

    items = ArxivCollector().collect(target_date=date(2026, 2, 26))
    assert len(items) == 1
    assert items[0].published_date == date(2026, 2, 25)


@patch("src.collectors.arxiv_collector.load_config",
       return_value={"collectors": {"arxiv": {"enabled": False}}})
@patch("src.collectors.arxiv_collector.arxiv")
def test_arxiv_disabled_returns_empty(mock_arxiv, _cfg):
    from src.collectors.arxiv_collector import ArxivCollector

    assert ArxivCollector().collect() == []
    mock_arxiv.Client.assert_not_called()
