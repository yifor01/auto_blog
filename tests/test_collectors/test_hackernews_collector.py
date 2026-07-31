"""測試 HackerNews collector 的 abstract 建立邏輯與 429 退避行為。"""
from unittest.mock import MagicMock, call, patch


def _make_mock_response(hits: list[dict]) -> MagicMock:
    """建立 mock HTTP response，包含 hits 清單。"""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"hits": hits}
    return mock_response


def _make_hit(
    object_id: str = "12345",
    title: str = "Test Article",
    url: str | None = "https://reuters.com/article/test",
    story_text: str | None = None,
    points: int = 141,
    num_comments: int = 44,
    author: str = "testuser",
) -> dict:
    """建立 HN API hit 字典。"""
    return {
        "objectID": object_id,
        "title": title,
        "url": url,
        "story_text": story_text,
        "points": points,
        "num_comments": num_comments,
        "author": author,
    }


@patch("src.collectors.hackernews_collector.get_http_client")
def test_link_post_abstract_contains_domain(mock_get_client):
    """link post 無 story_text 時，abstract 應包含外部 URL 的 domain。"""
    from src.collectors.hackernews_collector import HackerNewsCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_mock_response([
        _make_hit(url="https://reuters.com/article/test", story_text=None)
    ])

    collector = HackerNewsCollector()
    items = collector.collect()

    assert len(items) == 1
    assert "reuters.com" in items[0].abstract


@patch("src.collectors.hackernews_collector.get_http_client")
def test_link_post_abstract_contains_engagement(mock_get_client):
    """link post 無 story_text 時，abstract 應包含 points 與 comments 數量。"""
    from src.collectors.hackernews_collector import HackerNewsCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_mock_response([
        _make_hit(url="https://reuters.com/article/test", story_text=None, points=141, num_comments=44)
    ])

    collector = HackerNewsCollector()
    items = collector.collect()

    assert len(items) == 1
    assert "141 points" in items[0].abstract
    assert "44 comments" in items[0].abstract


@patch("src.collectors.hackernews_collector.get_http_client")
def test_self_post_uses_story_text(mock_get_client):
    """self post 有 story_text 時，abstract 應使用清理後的原始文字。"""
    from src.collectors.hackernews_collector import HackerNewsCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_mock_response([
        _make_hit(
            url=None,
            story_text="<p>Hello world</p>",
            points=50,
            num_comments=10,
        )
    ])

    collector = HackerNewsCollector()
    items = collector.collect()

    assert len(items) == 1
    assert items[0].abstract == "Hello world"


@patch("src.collectors.hackernews_collector.get_http_client")
def test_link_post_no_url_fallback(mock_get_client):
    """link post 無外部 URL 時，abstract 應 fallback 到 news.ycombinator.com。"""
    from src.collectors.hackernews_collector import HackerNewsCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_mock_response([
        _make_hit(url=None, story_text=None, points=80, num_comments=20)
    ])

    collector = HackerNewsCollector()
    items = collector.collect()

    assert len(items) == 1
    assert items[0].abstract != ""
    assert "news.ycombinator.com" in items[0].abstract


# ── client-side points 過濾（Algolia 已不支援 points numericFilter）──────────


@patch("src.collectors.hackernews_collector.get_http_client")
def test_low_points_hits_filtered_client_side(mock_get_client):
    """低於 min_points 的 hits 應在 client-side 被過濾掉（含 points 缺失者）。"""
    from src.collectors.hackernews_collector import HackerNewsCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    low = _make_hit(object_id="1", title="Low points", points=3)
    high = _make_hit(object_id="2", title="High points", points=120)
    no_points = _make_hit(object_id="3", title="No points")
    no_points.pop("points")
    mock_client.get.return_value = _make_mock_response([low, high, no_points])

    collector = HackerNewsCollector()
    items = collector.collect()

    assert [i.title for i in items] == ["High points"]


@patch("src.collectors.hackernews_collector.get_http_client")
def test_numeric_filters_exclude_points(mock_get_client):
    """API 請求的 numericFilters 只能含時間範圍，不得再帶 points（Algolia 會回 400）。"""
    from src.collectors.hackernews_collector import HackerNewsCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_mock_response([])

    collector = HackerNewsCollector()
    collector.collect()

    for c in mock_client.get.call_args_list:
        filters = c.kwargs["params"]["numericFilters"]
        assert "points" not in filters
        assert "created_at_i>" in filters and "created_at_i<" in filters


# ── 429 退避測試 ─────────────────────────────────────────────────────────────

def _make_response(status_code: int, hits: list[dict] | None = None) -> MagicMock:
    resp = MagicMock()
    resp.status_code = status_code
    if hits is not None:
        resp.json.return_value = {"hits": hits}
    else:
        resp.raise_for_status.side_effect = Exception(f"HTTP {status_code}")
    return resp


@patch("src.collectors.hackernews_collector.time.sleep")
def test_hn_429_retries_then_succeeds(mock_sleep):
    """On first 429, _hn_fetch_with_backoff retries and returns data on success."""
    from src.collectors.hackernews_collector import _hn_fetch_with_backoff

    resp_429 = MagicMock()
    resp_429.status_code = 429

    resp_ok = MagicMock()
    resp_ok.status_code = 200
    resp_ok.json.return_value = {"hits": [{"objectID": "1", "title": "Test"}]}

    mock_client = MagicMock()
    mock_client.get.side_effect = [resp_429, resp_ok]

    result = _hn_fetch_with_backoff(mock_client, {}, "AI")

    assert result is not None
    assert result["hits"][0]["objectID"] == "1"
    # sleep was called once (after first 429)
    mock_sleep.assert_called_once_with(2.0)


@patch("src.collectors.hackernews_collector.time.sleep")
def test_hn_429_all_retries_exhausted_returns_none(mock_sleep):
    """After _HN_429_MAX_RETRIES consecutive 429s, returns None and logs warning."""
    from src.collectors.hackernews_collector import _hn_fetch_with_backoff, _HN_429_MAX_RETRIES

    resp_429 = MagicMock()
    resp_429.status_code = 429

    mock_client = MagicMock()
    # Return 429 for every attempt (MAX_RETRIES + 1 calls total)
    mock_client.get.return_value = resp_429

    result = _hn_fetch_with_backoff(mock_client, {}, "LLM")

    assert result is None
    assert mock_client.get.call_count == _HN_429_MAX_RETRIES + 1


@patch("src.collectors.hackernews_collector.time.sleep")
def test_hn_429_backoff_delay_doubles(mock_sleep):
    """Backoff delays follow the 2→4→8 pattern."""
    from src.collectors.hackernews_collector import _hn_fetch_with_backoff

    resp_429 = MagicMock()
    resp_429.status_code = 429

    resp_ok = MagicMock()
    resp_ok.status_code = 200
    resp_ok.json.return_value = {"hits": []}

    mock_client = MagicMock()
    # Two 429s, then success
    mock_client.get.side_effect = [resp_429, resp_429, resp_ok]

    _hn_fetch_with_backoff(mock_client, {}, "GPT")

    sleep_calls = [c.args[0] for c in mock_sleep.call_args_list]
    assert sleep_calls == [2.0, 4.0]


@patch("src.collectors.hackernews_collector.get_http_client")
@patch("src.collectors.hackernews_collector.time.sleep")
def test_hn_collect_skips_query_on_persistent_429(mock_sleep, mock_get_client):
    """collect() skips a query that keeps returning 429 and continues with the next one."""
    from src.collectors.hackernews_collector import HackerNewsCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    resp_429 = MagicMock()
    resp_429.status_code = 429

    resp_ok = MagicMock()
    resp_ok.status_code = 200
    resp_ok.json.return_value = {"hits": [_make_hit(title="Good article")]}

    # First query: always 429; second query: succeeds
    call_count = {"n": 0}

    def side_effect(*args, **kwargs):
        call_count["n"] += 1
        # Calls 1-4 are for the first query (initial + 3 retries = 4 calls)
        if call_count["n"] <= 4:
            return resp_429
        return resp_ok

    mock_client.get.side_effect = side_effect

    collector = HackerNewsCollector()
    items = collector.collect()

    # Second query succeeded, so we should have one item
    assert len(items) == 1
    assert items[0].title == "Good article"
