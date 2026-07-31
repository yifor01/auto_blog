"""Tests for BlogCollector RSS path probe optimization.

Covers:
- First successful path returns immediately (no further probing)
- Timeout/DNS connection errors abort the remaining paths
- Non-200 responses log a debug message and continue
- Generic exceptions continue to the next path
"""

from __future__ import annotations

import httpx
import pytest
from unittest.mock import MagicMock, call, patch
from datetime import date


def _make_200_xml_resp(content: str = "<rss><channel></channel></rss>") -> MagicMock:
    resp = MagicMock()
    resp.status_code = 200
    resp.headers = {"content-type": "application/rss+xml"}
    resp.text = content
    return resp


def _make_non200_resp(status_code: int = 404) -> MagicMock:
    resp = MagicMock()
    resp.status_code = status_code
    resp.headers = {}
    resp.text = ""
    return resp


@patch("src.collectors.blog_collector.get_http_client")
def test_first_success_stops_probing(mock_get_client):
    """After the first successful RSS path, no further paths are probed."""
    from src.collectors.blog_collector import BlogCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    rss_content = "<rss><channel></channel></rss>"
    mock_client.get.return_value = _make_200_xml_resp(rss_content)

    collector = BlogCollector()
    # feedparser.parse must return non-empty entries for the code to return early.
    # We also mock _parse_feed_entries so it short-circuits cleanly.
    with patch("feedparser.parse") as mock_feedparser, \
         patch.object(BlogCollector, "_parse_feed_entries", return_value=[]):
        mock_feedparser.return_value = MagicMock(entries=[MagicMock()])  # non-empty → stop probing
        collector._scrape_blog(mock_client, "TestBlog", "http://example.com", date.today())

    # Only one get() call: the first path (/feed) succeeded and returned early
    assert mock_client.get.call_count == 1, (
        f"Expected 1 RSS probe call, got {mock_client.get.call_count}: "
        f"{mock_client.get.call_args_list}"
    )


@patch("src.collectors.blog_collector.get_http_client")
def test_timeout_aborts_remaining_paths(mock_get_client):
    """A TimeoutException on one path aborts all subsequent RSS path probes."""
    from src.collectors.blog_collector import BlogCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    # First path: 404 (continue), second path: TimeoutException (break)
    mock_client.get.side_effect = [
        _make_non200_resp(404),          # /feed → continue
        httpx.TimeoutException("timed out"),  # /rss → break
    ]

    collector = BlogCollector()
    with patch.object(collector, "_scrape_html", return_value=[]) as mock_html:
        collector._scrape_blog(mock_client, "Blog", "http://example.com", date.today())

    # Only 2 get() calls: /feed (404) + /rss (timeout) → remaining 4 paths skipped
    rss_probes = [c for c in mock_client.get.call_args_list]
    assert len(rss_probes) == 2, f"Expected 2 probe calls, got {len(rss_probes)}"
    # Should still fall back to HTML scraping
    mock_html.assert_called_once()


@patch("src.collectors.blog_collector.get_http_client")
def test_connect_error_aborts_remaining_paths(mock_get_client):
    """A ConnectError (DNS failure) aborts all remaining RSS path probes."""
    from src.collectors.blog_collector import BlogCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    mock_client.get.side_effect = httpx.ConnectError("Name resolution failed")

    collector = BlogCollector()
    with patch.object(collector, "_scrape_html", return_value=[]):
        collector._scrape_blog(mock_client, "Blog", "http://broken.example.com", date.today())

    # Only 1 probe call: ConnectError on first path aborts immediately
    assert mock_client.get.call_count == 1


@patch("src.collectors.blog_collector.get_http_client")
def test_non200_logs_debug_and_continues(mock_get_client, caplog):
    """Non-200 HTTP status on a path logs debug and continues to the next path."""
    import logging
    from src.collectors.blog_collector import BlogCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    # All paths return 404 → all tried, then HTML fallback
    mock_client.get.return_value = _make_non200_resp(404)

    collector = BlogCollector()
    with patch.object(collector, "_scrape_html", return_value=[]):
        # Use root-level DEBUG capture; logger name includes "autopb." prefix
        with caplog.at_level(logging.DEBUG):
            collector._scrape_blog(mock_client, "Blog", "http://example.com", date.today())

    # All 6 paths were probed (none succeeded)
    assert mock_client.get.call_count == 6
    debug_msgs = [r.message for r in caplog.records if r.levelno == logging.DEBUG]
    assert any("non-success" in m.lower() or "404" in m or "status" in m.lower() for m in debug_msgs), \
        f"Expected a debug message about non-success status. Got: {debug_msgs}"


@patch("src.collectors.blog_collector.get_http_client")
def test_generic_exception_continues_to_next_path(mock_get_client):
    """An unexpected exception on one path continues probing the remaining paths."""
    from src.collectors.blog_collector import BlogCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    # First path: generic error → continue; rest: 404
    mock_client.get.side_effect = [
        Exception("unexpected error"),
        _make_non200_resp(404),
        _make_non200_resp(404),
        _make_non200_resp(404),
        _make_non200_resp(404),
        _make_non200_resp(404),
    ]

    collector = BlogCollector()
    with patch.object(collector, "_scrape_html", return_value=[]):
        collector._scrape_blog(mock_client, "Blog", "http://example.com", date.today())

    # All 6 paths attempted despite the first one erroring
    assert mock_client.get.call_count == 6
