"""P1-1 回歸測試：RSS collector 透過共用 httpx client（有 timeout）抓 feed，
而非 feedparser.parse(url) 自帶無 timeout 的 urllib。"""
from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock, patch

_CFG = {
    "collectors": {
        "rss": {
            "enabled": True,
            "feeds": [{"name": "TestFeed", "url": "https://feed.example/rss"}],
        }
    }
}


@patch("src.collectors.rss_collector.load_config", return_value=_CFG)
@patch("src.collectors.rss_collector.feedparser")
@patch("src.collectors.rss_collector.get_http_client")
def test_rss_fetches_via_http_client_not_feedparser_url(mock_get_client, mock_feedparser, _cfg):
    from src.collectors.rss_collector import RSSCollector

    client = MagicMock()
    mock_get_client.return_value = client
    resp = MagicMock()
    resp.content = b"<rss></rss>"
    client.get.return_value = resp

    parsed = MagicMock()
    parsed.entries = []
    mock_feedparser.parse.return_value = parsed

    RSSCollector().collect(target_date=date(2026, 2, 26))

    # 用共用 client 抓 feed URL（帶 timeout）
    client.get.assert_called_once_with("https://feed.example/rss")
    # feedparser 收到的是 bytes，而不是 URL 字串（後者會走無 timeout 的 urllib）
    mock_feedparser.parse.assert_called_once_with(b"<rss></rss>")


@patch("src.collectors.rss_collector.load_config", return_value=_CFG)
@patch("src.collectors.rss_collector.feedparser")
@patch("src.collectors.rss_collector.get_http_client")
def test_rss_feed_fetch_error_does_not_crash(mock_get_client, mock_feedparser, _cfg):
    """單一 feed 抓取失敗時整體不應拋例外，回空清單並繼續。"""
    from src.collectors.rss_collector import RSSCollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.side_effect = Exception("timeout")

    items = RSSCollector().collect(target_date=date(2026, 2, 26))
    assert items == []
    mock_feedparser.parse.assert_not_called()
    client.close.assert_called_once()
