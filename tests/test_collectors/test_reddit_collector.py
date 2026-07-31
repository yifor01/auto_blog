"""測試 Reddit collector 的 CI 跳過、upvote 門檻、日期過濾與欄位映射。"""
from __future__ import annotations

from datetime import date, datetime
from unittest.mock import MagicMock, patch

from zoneinfo import ZoneInfo

_TZ = ZoneInfo("Asia/Taipei")
_TARGET = date(2026, 2, 26)
# target_date 當天台灣時間中午的 epoch（落在 collector 的 [start, end) 窗口內）
_IN_WINDOW_TS = datetime(2026, 2, 26, 12, 0, tzinfo=_TZ).timestamp()
_OUT_WINDOW_TS = datetime(2026, 2, 25, 12, 0, tzinfo=_TZ).timestamp()

_CFG = {
    "collectors": {
        "reddit": {
            "enabled": True,
            "subreddits": ["LocalLLaMA"],
            "min_upvotes": 50,
            "max_results": 30,
            "time_filter": "day",
        }
    }
}


def _resp(posts: list[dict]) -> MagicMock:
    r = MagicMock()
    r.status_code = 200
    r.json.return_value = {"data": {"children": [{"data": p} for p in posts]}}
    return r


def _post(post_id="abc", title="Cool LLM", score=120, created_utc=_IN_WINDOW_TS,
          is_self=True, selftext="Some self text", permalink="/r/LocalLLaMA/comments/abc/"):
    return {
        "id": post_id,
        "title": title,
        "score": score,
        "created_utc": created_utc,
        "is_self": is_self,
        "selftext": selftext,
        "permalink": permalink,
        "url": f"https://www.reddit.com{permalink}",
        "num_comments": 12,
        "author": "redditor",
        "domain": "self.LocalLLaMA",
    }


@patch.dict("os.environ", {"GITHUB_ACTIONS": "true"}, clear=True)
@patch("src.collectors.reddit_collector.load_config", return_value=_CFG)
def test_reddit_skips_on_github_actions(_cfg):
    from src.collectors.reddit_collector import RedditCollector

    with patch("src.collectors.reddit_collector.get_http_client") as mock_client:
        assert RedditCollector().collect(target_date=_TARGET) == []
        mock_client.assert_not_called()


@patch.dict("os.environ", {}, clear=True)
@patch("src.collectors.reddit_collector.load_config", return_value=_CFG)
@patch("src.collectors.reddit_collector.get_http_client")
def test_reddit_filters_low_score_and_out_of_window(mock_get_client, _cfg):
    from src.collectors.reddit_collector import RedditCollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.return_value = _resp([
        _post(post_id="low", score=10),                       # 低於 min_upvotes
        _post(post_id="old", created_utc=_OUT_WINDOW_TS),     # 不在當日窗口
        _post(post_id="good", score=200),                     # 通過
    ])

    items = RedditCollector().collect(target_date=_TARGET)
    assert len(items) == 1
    assert items[0].raw_metadata["post_id"] == "good"


@patch.dict("os.environ", {}, clear=True)
@patch("src.collectors.reddit_collector.load_config", return_value=_CFG)
@patch("src.collectors.reddit_collector.get_http_client")
def test_reddit_self_post_uses_selftext(mock_get_client, _cfg):
    from src.collectors.reddit_collector import RedditCollector
    from src.models import SourceType

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.return_value = _resp([_post(is_self=True, selftext="Hello reddit body")])

    items = RedditCollector().collect(target_date=_TARGET)
    assert len(items) == 1
    it = items[0]
    assert it.source == SourceType.REDDIT
    assert it.abstract == "Hello reddit body"
    assert it.source_name == "r/LocalLLaMA"
