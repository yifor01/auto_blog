"""測試 NewsAPI collector 的 key 缺失跳過、[Removed] 過濾與欄位映射。"""
from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock, patch

_CFG = {"collectors": {"newsapi": {"enabled": True, "max_results": 20}}}


def _resp(articles: list[dict]) -> MagicMock:
    r = MagicMock()
    r.status_code = 200
    r.json.return_value = {"articles": articles}
    return r


def _article(title="OpenAI ships GPT", url="https://news.example/a", description="A description"):
    return {
        "title": title,
        "url": url,
        "description": description,
        "content": "full content",
        "source": {"name": "TechNews"},
        "author": "Reporter",
        "publishedAt": "2026-02-26T10:00:00Z",
    }


@patch("src.collectors.newsapi_collector.load_config", return_value=_CFG)
@patch.dict("os.environ", {}, clear=True)
def test_newsapi_no_key_skips(_cfg):
    """無 NEWSAPI_KEY 時跳過、回傳空清單，不打 API。"""
    from src.collectors.newsapi_collector import NewsAPICollector

    with patch("src.collectors.newsapi_collector.get_http_client") as mock_client:
        assert NewsAPICollector().collect(target_date=date(2026, 2, 26)) == []
        mock_client.assert_not_called()


@patch("src.collectors.newsapi_collector.load_config", return_value=_CFG)
@patch.dict("os.environ", {"NEWSAPI_KEY": "k"}, clear=True)
@patch("src.collectors.newsapi_collector.get_http_client")
def test_newsapi_filters_removed_and_no_url(mock_get_client, _cfg):
    from src.collectors.newsapi_collector import NewsAPICollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.return_value = _resp([
        _article(title="[Removed]"),
        _article(title="No URL", url=""),
        _article(title="Good one", url="https://news.example/good"),
    ])

    items = NewsAPICollector().collect(target_date=date(2026, 2, 26))
    assert len(items) == 1
    assert items[0].title == "Good one"


@patch("src.collectors.newsapi_collector.load_config", return_value=_CFG)
@patch.dict("os.environ", {"NEWSAPI_KEY": "k"}, clear=True)
@patch("src.collectors.newsapi_collector.get_http_client")
def test_newsapi_maps_fields(mock_get_client, _cfg):
    from src.collectors.newsapi_collector import NewsAPICollector
    from src.models import SourceType

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.return_value = _resp([_article()])

    items = NewsAPICollector().collect(target_date=date(2026, 2, 26))
    assert len(items) == 1
    it = items[0]
    assert it.source == SourceType.NEWSAPI
    assert it.source_name == "TechNews"
    assert it.authors == ["Reporter"]
    assert it.abstract == "A description"
