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

# ── 免費方案 ~24h 延遲補償（2026-07-31 修復）───────────────────────────
# 症狀：118 天的 data/raw 裡 116 天 newsapi 為 0 筆，且 log 無任何 error
#（API 回 HTTP 200 + status ok + totalResults 0，完全合法）。
# 根因：Developer(免費) 方案的文章有 ~24 小時延遲，而 collector 永遠查
# target_date=當天 → 結構性保證撈不到。實測 T-0=0 / T-1=15 / T-2=82 / T-3=85。
# 唯二有資料的 07-08、07-10 是 07-11 那次 catchup 補跑「過去日期」的產物。


@patch("src.collectors.newsapi_collector.load_config", return_value=_CFG)
@patch.dict("os.environ", {"NEWSAPI_KEY": "k"}, clear=True)
@patch("src.collectors.newsapi_collector.get_http_client")
def test_newsapi_queries_lagged_window_not_target_date(mock_get_client, _cfg):
    """免費方案當天無資料，查詢區間必須往回退 lag_days（預設 2）。"""
    from src.collectors.newsapi_collector import NewsAPICollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.return_value = _resp([])

    NewsAPICollector().collect(target_date=date(2026, 2, 26))

    params = client.get.call_args.kwargs["params"]
    assert params["from"] == "2026-02-24", (
        f"查詢起日仍是當天/未退回 lag_days，免費方案必定回 0 筆。實際 from={params['from']}"
    )
    assert params["to"] == "2026-02-25"


@patch("src.collectors.newsapi_collector.load_config", return_value=_CFG)
@patch.dict("os.environ", {"NEWSAPI_KEY": "k"}, clear=True)
@patch("src.collectors.newsapi_collector.get_http_client")
def test_newsapi_uses_real_published_at(mock_get_client, _cfg):
    """published_date 取 API 的 publishedAt，不可用收集日（否則舊聞會被標成當天）。"""
    from src.collectors.newsapi_collector import NewsAPICollector

    client = MagicMock()
    mock_get_client.return_value = client
    art = _article()
    art["publishedAt"] = "2026-02-24T08:30:00Z"
    client.get.return_value = _resp([art])

    items = NewsAPICollector().collect(target_date=date(2026, 2, 26))
    assert items[0].published_date == date(2026, 2, 24), (
        f"published_date 應為真實發布日 2026-02-24，實際 {items[0].published_date}"
    )


@patch("src.collectors.newsapi_collector.load_config", return_value=_CFG)
@patch.dict("os.environ", {"NEWSAPI_KEY": "k"}, clear=True)
@patch("src.collectors.newsapi_collector.get_http_client")
def test_newsapi_falls_back_to_lagged_date_when_published_at_unusable(mock_get_client, _cfg):
    """publishedAt 缺失或格式壞掉時退回查詢日，不得整筆丟棄或炸掉。"""
    from src.collectors.newsapi_collector import NewsAPICollector

    client = MagicMock()
    mock_get_client.return_value = client
    missing = _article(url="https://news.example/missing")
    missing["publishedAt"] = ""
    broken = _article(url="https://news.example/broken")
    broken["publishedAt"] = "not-a-date"
    client.get.return_value = _resp([missing, broken])

    items = NewsAPICollector().collect(target_date=date(2026, 2, 26))
    assert len(items) == 2
    assert all(i.published_date == date(2026, 2, 24) for i in items), (
        [i.published_date for i in items]
    )
