"""Tests for organization inference across collectors.

Covers:
- infer_organization() name-based and domain-based matching
- RSSCollector sets organization for known feeds
- BlogCollector sets organization for known blog sources
- GitHubTrendingCollector sets organization for known org owners
- Unknown / personal sources produce empty organization
"""

from __future__ import annotations

import pytest
from unittest.mock import MagicMock, patch
from datetime import date


# ---------------------------------------------------------------------------
# infer_organization() unit tests
# ---------------------------------------------------------------------------


class TestInferOrganization:
    def test_openai_blog_by_name(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("OpenAI Blog", "https://openai.com/blog/rss.xml") == "OpenAI"

    def test_google_ai_blog_by_name(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Google AI Blog", "https://blog.google/technology/ai/rss/") == "Google"

    def test_google_research_by_name(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Google Research", "https://blog.research.google/feeds/posts/default") == "Google"

    def test_anthropic_engineering_by_name(self):
        from src.collectors._helpers import infer_organization

        # Anthropic feeds come from raw.githubusercontent.com; domain won't match.
        result = infer_organization(
            "Anthropic Engineering",
            "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml",
        )
        assert result == "Anthropic"

    def test_anthropic_research_by_name(self):
        from src.collectors._helpers import infer_organization

        result = infer_organization(
            "Anthropic Research",
            "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_research.xml",
        )
        assert result == "Anthropic"

    def test_claude_blog_by_name(self):
        from src.collectors._helpers import infer_organization

        # claude.com/blog 走 raw.githubusercontent 鏡像，domain 對不上；
        # 推不出 Anthropic 就不會命中 pinned，等於整條 feed 白加。
        result = infer_organization(
            "Claude Blog",
            "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_claude.xml",
        )
        assert result == "Anthropic"

    def test_anthropic_news_by_name(self):
        from src.collectors._helpers import infer_organization

        result = infer_organization(
            "Anthropic News",
            "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_news.xml",
        )
        assert result == "Anthropic"

    def test_huggingface_blog_by_name(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("HuggingFace Blog", "https://huggingface.co/blog/feed.xml") == "HuggingFace"

    def test_name_match_is_case_insensitive(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("openai blog", "https://openai.com/blog/rss.xml") == "OpenAI"
        assert infer_organization("OPENAI BLOG", "https://openai.com/blog/rss.xml") == "OpenAI"

    def test_openai_by_domain(self):
        from src.collectors._helpers import infer_organization

        # Unknown feed name, but domain is known
        assert infer_organization("Some Unknown Feed", "https://openai.com/some/feed") == "OpenAI"

    def test_huggingface_by_domain(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Unknown Blog", "https://huggingface.co/blog/feed.xml") == "HuggingFace"

    def test_anthropic_com_by_domain(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Unknown", "https://anthropic.com/research/feed") == "Anthropic"

    def test_deepmind_google_by_domain(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Unknown", "https://deepmind.google/discover/blog/rss") == "Google DeepMind"

    def test_www_prefix_stripped(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Unknown", "https://www.deepseek.com/feed") == "DeepSeek"

    def test_unknown_name_and_domain_returns_empty(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("TechCrunch AI", "https://techcrunch.com/category/ai/feed/") == ""

    def test_personal_blog_url_returns_empty(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Simon Willison", "https://simonwillison.net/") == ""

    def test_lilian_weng_blog_by_name(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Lilian Weng (OpenAI)", "https://lilianweng.github.io/") == "OpenAI"

    def test_empty_feed_name_and_url_returns_empty(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("", "") == ""

    def test_invalid_url_returns_empty(self):
        from src.collectors._helpers import infer_organization

        assert infer_organization("Unknown Feed", "not-a-valid-url") == ""


# ---------------------------------------------------------------------------
# RSSCollector organization filling
# ---------------------------------------------------------------------------

_MINIMAL_RSS_FEED_XML = """<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <title>Test Feed</title>
    <item>
      <title>Test Article</title>
      <link>https://openai.com/blog/test</link>
      <pubDate>Mon, 09 Jun 2026 12:00:00 +0000</pubDate>
      <description>Short text about the article.</description>
    </item>
  </channel>
</rss>"""


def _rss_config(feed_name: str, feed_url: str) -> dict:
    return {
        "collectors": {
            "rss": {
                "enabled": True,
                "feeds": [{"name": feed_name, "url": feed_url}],
            }
        }
    }


@patch("src.collectors.rss_collector.fetch_article_text", return_value="")
@patch("src.collectors.rss_collector.get_http_client")
@patch("src.collectors.rss_collector.feedparser.parse")
@patch("src.collectors.rss_collector.load_config")
def test_rss_collector_sets_organization_for_openai_feed(
    mock_cfg, mock_feedparser, mock_get_client, mock_fetch
):
    from src.collectors.rss_collector import RSSCollector

    mock_cfg.return_value = _rss_config("OpenAI Blog", "https://openai.com/blog/rss.xml")

    entry = MagicMock()
    entry.get = lambda k, d="": {
        "title": "GPT-5 Released",
        "link": "https://openai.com/blog/gpt5",
        "published": "Mon, 09 Jun 2026 12:00:00 +0000",
        "authors": [],
        "tags": [],
    }.get(k, d)
    entry.content = []
    entry.summary = "A" * 200
    entry.description = ""

    mock_feedparser.return_value = MagicMock(entries=[entry])
    mock_get_client.return_value.__enter__ = MagicMock()
    client_mock = MagicMock()
    mock_get_client.return_value = client_mock

    items = RSSCollector().collect(target_date=date(2026, 6, 9))
    assert len(items) == 1
    assert items[0].organization == "OpenAI"


@patch("src.collectors.rss_collector.fetch_article_text", return_value="")
@patch("src.collectors.rss_collector.get_http_client")
@patch("src.collectors.rss_collector.feedparser.parse")
@patch("src.collectors.rss_collector.load_config")
def test_rss_collector_sets_organization_for_anthropic_engineering(
    mock_cfg, mock_feedparser, mock_get_client, mock_fetch
):
    from src.collectors.rss_collector import RSSCollector

    mock_cfg.return_value = _rss_config(
        "Anthropic Engineering",
        "https://raw.githubusercontent.com/Olshansk/rss-feeds/main/feeds/feed_anthropic_engineering.xml",
    )

    entry = MagicMock()
    entry.get = lambda k, d="": {
        "title": "Claude 4 Internals",
        "link": "https://anthropic.com/engineering/claude4",
        "published": "Mon, 09 Jun 2026 12:00:00 +0000",
        "authors": [],
        "tags": [],
    }.get(k, d)
    entry.content = []
    entry.summary = "B" * 200
    entry.description = ""

    mock_feedparser.return_value = MagicMock(entries=[entry])
    mock_get_client.return_value = MagicMock()

    items = RSSCollector().collect(target_date=date(2026, 6, 9))
    assert len(items) == 1
    assert items[0].organization == "Anthropic"


@patch("src.collectors.rss_collector.fetch_article_text", return_value="")
@patch("src.collectors.rss_collector.get_http_client")
@patch("src.collectors.rss_collector.feedparser.parse")
@patch("src.collectors.rss_collector.load_config")
def test_rss_collector_empty_organization_for_unknown_feed(
    mock_cfg, mock_feedparser, mock_get_client, mock_fetch
):
    from src.collectors.rss_collector import RSSCollector

    mock_cfg.return_value = _rss_config("TechCrunch AI", "https://techcrunch.com/category/ai/feed/")

    entry = MagicMock()
    entry.get = lambda k, d="": {
        "title": "AI News Article",
        "link": "https://techcrunch.com/ai/article",
        "published": "Mon, 09 Jun 2026 12:00:00 +0000",
        "authors": [],
        "tags": [],
    }.get(k, d)
    entry.content = []
    entry.summary = "C" * 200
    entry.description = ""

    mock_feedparser.return_value = MagicMock(entries=[entry])
    mock_get_client.return_value = MagicMock()

    items = RSSCollector().collect(target_date=date(2026, 6, 9))
    assert len(items) == 1
    assert items[0].organization == ""


# ---------------------------------------------------------------------------
# BlogCollector organization filling
# ---------------------------------------------------------------------------

_BLOG_CONFIG_LILIAN = {
    "collectors": {
        "blogs": {
            "enabled": True,
            "sources": [
                {"name": "Lilian Weng (OpenAI)", "url": "https://lilianweng.github.io/"},
            ],
        }
    }
}

_BLOG_CONFIG_PERSONAL = {
    "collectors": {
        "blogs": {
            "enabled": True,
            "sources": [
                {"name": "Simon Willison", "url": "https://simonwillison.net/"},
            ],
        }
    }
}

_BLOG_FEED_XML = """<?xml version="1.0"?>
<rss version="2.0">
  <channel>
    <title>Test Blog</title>
    <item>
      <title>Scaling Laws Revisited</title>
      <link>https://lilianweng.github.io/posts/scaling-laws</link>
      <pubDate>Mon, 09 Jun 2026 12:00:00 +0000</pubDate>
      <description>{abstract}</description>
    </item>
  </channel>
</rss>"""


def _make_http_resp(status_code: int = 200, text: str = "") -> MagicMock:
    resp = MagicMock()
    resp.status_code = status_code
    resp.text = text
    resp.headers = {"content-type": "application/xml"}
    resp.raise_for_status = MagicMock()
    return resp


def _make_feedparser_result(title: str, link: str, pub_date: str, abstract: str) -> MagicMock:
    """Build a minimal feedparser parse() return value."""
    entry = MagicMock()
    entry.get = lambda k, d="": {
        "title": title,
        "link": link,
        "published": pub_date,
    }.get(k, d)
    entry.content = []
    entry.summary = abstract
    parsed_mock = MagicMock()
    parsed_mock.entries = [entry]
    return parsed_mock


@patch("src.collectors.blog_collector.fetch_article_text", return_value="")
@patch("feedparser.parse")
@patch("src.collectors.blog_collector.get_http_client")
@patch("src.collectors.blog_collector.load_config", return_value=_BLOG_CONFIG_LILIAN)
def test_blog_collector_sets_organization_for_lilian_weng(
    mock_cfg, mock_get_client, mock_feedparser_parse, mock_fetch
):
    from src.collectors.blog_collector import BlogCollector

    abstract_text = "D" * 1200
    client_mock = MagicMock()
    # RSS probe: return XML-like response so the collector tries feedparser
    client_mock.get.return_value = _make_http_resp(
        200, "<?xml version='1.0'?><rss></rss>"
    )
    mock_get_client.return_value = client_mock

    mock_feedparser_parse.return_value = _make_feedparser_result(
        title="Scaling Laws Revisited",
        link="https://lilianweng.github.io/posts/scaling-laws",
        pub_date="Mon, 09 Jun 2026 12:00:00 +0000",
        abstract=abstract_text,
    )

    items = BlogCollector().collect(target_date=date(2026, 6, 9))
    assert len(items) >= 1
    assert all(item.organization == "OpenAI" for item in items)


@patch("src.collectors.blog_collector.fetch_article_text", return_value="")
@patch("feedparser.parse")
@patch("src.collectors.blog_collector.get_http_client")
@patch("src.collectors.blog_collector.load_config", return_value=_BLOG_CONFIG_PERSONAL)
def test_blog_collector_empty_organization_for_personal_blog(
    mock_cfg, mock_get_client, mock_feedparser_parse, mock_fetch
):
    from src.collectors.blog_collector import BlogCollector

    abstract_text = "E" * 1200
    client_mock = MagicMock()
    client_mock.get.return_value = _make_http_resp(
        200, "<?xml version='1.0'?><rss></rss>"
    )
    mock_get_client.return_value = client_mock

    mock_feedparser_parse.return_value = _make_feedparser_result(
        title="A Thought on AI",
        link="https://simonwillison.net/2026/Jun/9/thought",
        pub_date="Mon, 09 Jun 2026 12:00:00 +0000",
        abstract=abstract_text,
    )

    items = BlogCollector().collect(target_date=date(2026, 6, 9))
    assert len(items) >= 1
    assert all(item.organization == "" for item in items)


# ---------------------------------------------------------------------------
# GitHubTrendingCollector organization filling
# ---------------------------------------------------------------------------

_TRENDING_HTML_ORG = """
<html><body>
<article class="Box-row">
  <h2><a href="/openai/whisper">openai/whisper</a></h2>
  <p class="color-fg-muted">Robust Speech Recognition via large-scale weak supervision LLM</p>
</article>
<article class="Box-row">
  <h2><a href="/google-deepmind/graphcast">google-deepmind/graphcast</a></h2>
  <p class="color-fg-muted">Deep learning for weather forecasting AI model</p>
</article>
<article class="Box-row">
  <h2><a href="/personal-user/my-llm-project">personal-user/my-llm-project</a></h2>
  <p class="color-fg-muted">My personal LLM agent project</p>
</article>
</body></html>
"""


def _github_config() -> dict:
    return {"collectors": {"github": {"enabled": True, "languages": ["python"]}}}


@patch("src.collectors.github_trending.load_config", return_value=_github_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_github_trending_sets_org_for_openai(mock_get_client, mock_sleep, mock_cfg):
    from src.collectors.github_trending import GitHubTrendingCollector

    client = MagicMock()
    mock_get_client.return_value = client
    # All calls return 429 to skip README; trending page is 200
    client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML_ORG),  # trending page
        _make_resp(429),                       # openai/whisper README → skip
        # further README fetches are skipped due to skip_readme_fetch=True
    ]

    items = GitHubTrendingCollector().collect()
    openai_items = [i for i in items if "openai/whisper" in i.title]
    assert len(openai_items) == 1
    assert openai_items[0].organization == "OpenAI"


@patch("src.collectors.github_trending.load_config", return_value=_github_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_github_trending_sets_org_for_google_deepmind(mock_get_client, mock_sleep, mock_cfg):
    from src.collectors.github_trending import GitHubTrendingCollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML_ORG),
        _make_resp(429),
    ]

    items = GitHubTrendingCollector().collect()
    dm_items = [i for i in items if "google-deepmind/graphcast" in i.title]
    assert len(dm_items) == 1
    assert dm_items[0].organization == "Google DeepMind"


@patch("src.collectors.github_trending.load_config", return_value=_github_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_github_trending_empty_org_for_personal_owner(mock_get_client, mock_sleep, mock_cfg):
    from src.collectors.github_trending import GitHubTrendingCollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML_ORG),
        _make_resp(429),
    ]

    items = GitHubTrendingCollector().collect()
    personal_items = [i for i in items if "personal-user" in i.title]
    assert len(personal_items) == 1
    assert personal_items[0].organization == ""


@patch("src.collectors.github_trending.load_config", return_value=_github_config())
@patch("src.collectors.github_trending.time.sleep")
@patch("src.collectors.github_trending.get_http_client")
def test_github_trending_owner_stored_in_authors(mock_get_client, mock_sleep, mock_cfg):
    """repo owner should be stored in authors list for rules.py fallback matching."""
    from src.collectors.github_trending import GitHubTrendingCollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.side_effect = [
        _make_resp(200, _TRENDING_HTML_ORG),
        _make_resp(429),
    ]

    items = GitHubTrendingCollector().collect()
    openai_items = [i for i in items if "openai/whisper" in i.title]
    assert len(openai_items) == 1
    # owner is preserved in authors so rules.py author-fallback also works
    assert "openai" in openai_items[0].authors


# ---------------------------------------------------------------------------
# _GITHUB_OWNER_TO_ORG completeness spot-checks
# ---------------------------------------------------------------------------


def test_github_owner_map_contains_expected_orgs():
    from src.collectors.github_trending import _GITHUB_OWNER_TO_ORG

    expected = {
        "openai": "OpenAI",
        "anthropics": "Anthropic",
        "google": "Google",
        "google-deepmind": "Google DeepMind",
        "meta-llama": "Meta AI",
        "facebookresearch": "Meta AI",
        "microsoft": "Microsoft",
        "huggingface": "HuggingFace",
        "nvidia": "NVIDIA",
        "deepseek-ai": "DeepSeek",
        "qwenlm": "Alibaba",
        "mistralai": "Mistral",
        "allenai": "AI2",
    }
    for owner, expected_org in expected.items():
        assert _GITHUB_OWNER_TO_ORG.get(owner) == expected_org, (
            f"Expected {owner!r} → {expected_org!r}, "
            f"got {_GITHUB_OWNER_TO_ORG.get(owner)!r}"
        )


def _make_resp(status_code: int, text: str = "") -> MagicMock:
    """Local helper reusing the same pattern as test_github_trending.py."""
    resp = MagicMock()
    resp.status_code = status_code
    resp.text = text
    resp.raise_for_status = MagicMock()
    return resp
