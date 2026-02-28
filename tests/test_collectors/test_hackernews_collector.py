"""測試 HackerNews collector 的 abstract 建立邏輯。"""
from unittest.mock import MagicMock, patch


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
