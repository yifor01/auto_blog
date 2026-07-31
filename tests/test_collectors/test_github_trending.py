"""Tests for GitHubTrendingCollector defensive handling.

Covers:
- 429/403 on README fetch stops further README fetches for that language
- Already-collected repo items are still returned with description fallback
- Timeout exception in README fetch does not abort the outer repo loop
- Browser-like User-Agent is set on the client
"""

from __future__ import annotations

import pytest
from unittest.mock import MagicMock, patch
from datetime import date


# Minimal GitHub trending HTML with two AI-related repos
_TRENDING_HTML = """
<html><body>
<article class="Box-row">
  <h2><a href="/owner/llm-toolkit">owner/llm-toolkit</a></h2>
  <p class="color-fg-muted">A toolkit for LLM inference</p>
</article>
<article class="Box-row">
  <h2><a href="/owner/gpt-agent">owner/gpt-agent</a></h2>
  <p class="color-fg-muted">GPT-based agent framework</p>
</article>
</body></html>
"""

_README_HTML = """
<html><body>
<article class="markdown-body">Detailed README content here.</article>
</body></html>
"""


def _make_resp(status_code: int, text: str = "") -> MagicMock:
    resp = MagicMock()
    resp.status_code = status_code
    resp.text = text
    resp.raise_for_status = MagicMock()
    return resp


def _single_lang_config() -> dict:
    """Return a minimal config dict with a single language to isolate tests."""
    return {"collectors": {"github": {"enabled": True, "languages": ["python"]}}}


@patch("src.collectors.github_trending.load_config", return_value=_single_lang_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_429_stops_readme_fetches_for_language(mock_get_client, mock_sleep, mock_cfg):
    """On 429 from GitHub README page, no further README fetches are attempted."""
    from src.collectors.github_trending import GitHubTrendingCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    # Call sequence for single language (python):
    # 1. trending page (200)
    # 2. README for repo1 (429) → skip_readme_fetch = True
    # 3. README for repo2 → NOT called (skipped)
    mock_client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML),   # trending page
        _make_resp(429),                   # repo1 README → triggers stop
    ]

    collector = GitHubTrendingCollector()
    items = collector.collect()

    # Both repos should still be collected (description fallback)
    assert len(items) == 2
    # Only 2 client.get() calls: trending + first README (second README skipped)
    assert mock_client.get.call_count == 2


@patch("src.collectors.github_trending.load_config", return_value=_single_lang_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_403_stops_readme_fetches_for_language(mock_get_client, mock_sleep, mock_cfg):
    """On 403 from GitHub README page, no further README fetches are attempted."""
    from src.collectors.github_trending import GitHubTrendingCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    mock_client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML),
        _make_resp(403),
    ]

    collector = GitHubTrendingCollector()
    items = collector.collect()

    assert len(items) == 2
    assert mock_client.get.call_count == 2


@patch("src.collectors.github_trending.load_config", return_value=_single_lang_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_rate_limited_repos_use_description_fallback(mock_get_client, mock_sleep, mock_cfg):
    """Repos whose README fetch was skipped due to rate-limit use description as abstract."""
    from src.collectors.github_trending import GitHubTrendingCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    mock_client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML),
        _make_resp(429),
    ]

    collector = GitHubTrendingCollector()
    items = collector.collect()

    # Both items should have non-empty abstracts (description fallback)
    for item in items:
        assert item.abstract, f"Expected non-empty abstract for {item.title}"


@patch("src.collectors.github_trending.load_config", return_value=_single_lang_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_readme_timeout_does_not_abort_repo_loop(mock_get_client, mock_sleep, mock_cfg):
    """Timeout exception during README fetch is caught; remaining repos still processed."""
    import httpx
    from src.collectors.github_trending import GitHubTrendingCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    mock_client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML),      # trending page
        httpx.TimeoutException("timed out"),  # repo1 README → exception caught
        _make_resp(200, _README_HTML),        # repo2 README → succeeds
    ]

    collector = GitHubTrendingCollector()
    items = collector.collect()

    # Both repos collected; second one has README content
    assert len(items) == 2
    readme_items = [i for i in items if "Detailed README" in i.abstract]
    assert len(readme_items) == 1


@patch("src.collectors.github_trending.load_config", return_value=_single_lang_config())
@patch("src.collectors.github_trending.get_http_client")
def test_browser_user_agent_set_on_client(mock_get_client, mock_cfg):
    """The collector sets a browser-like User-Agent on the HTTP client."""
    from src.collectors.github_trending import GitHubTrendingCollector, _GITHUB_UA

    mock_client = MagicMock()
    mock_client.headers = {}
    mock_get_client.return_value = mock_client

    # Return empty trending page so collect() completes without further side-effects
    mock_client.get.return_value = _make_resp(200, "<html></html>")

    collector = GitHubTrendingCollector()
    collector.collect()

    assert "User-Agent" in mock_client.headers
    ua = mock_client.headers["User-Agent"]
    assert "Mozilla" in ua, f"Expected browser UA, got: {ua}"
    assert ua == _GITHUB_UA
