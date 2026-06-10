"""Shared helper utilities for collectors."""

from __future__ import annotations

from datetime import date
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Organization inference helpers
# ---------------------------------------------------------------------------

# Feed name / blog source name → organization.
# Keys must be lower-cased; values must match the institution names in
# config.yaml `scoring.top_institutions` so that rules.py gets word-boundary
# hits on the `organization` field.
_NAME_TO_ORG: dict[str, str] = {
    # RSS feeds (matches config.yaml rss.feeds[].name, lowercased)
    "openai blog": "OpenAI",
    "google ai blog": "Google",
    "google research": "Google",
    "huggingface blog": "HuggingFace",
    "anthropic engineering": "Anthropic",
    "anthropic research": "Anthropic",
    # Blog sources (matches config.yaml blogs.sources[].name, lowercased)
    "lilian weng (openai)": "OpenAI",
}

# URL netloc (www-stripped, lowercased) → organization.
# Only include domains whose ownership is unambiguous.
_DOMAIN_TO_ORG: dict[str, str] = {
    "openai.com": "OpenAI",
    "anthropic.com": "Anthropic",
    "blog.google": "Google",
    "research.google": "Google",
    "blog.research.google": "Google",
    "ai.google": "Google",
    "deepmind.google": "Google DeepMind",
    "deepmind.com": "Google DeepMind",
    "huggingface.co": "HuggingFace",
    "ai.meta.com": "Meta AI",
    "research.fb.com": "Meta AI",
    "microsoft.com": "Microsoft",
    "research.microsoft.com": "Microsoft Research",
    "nvidia.com": "NVIDIA",
    "deepseek.com": "DeepSeek",
    "mistral.ai": "Mistral",
    "cohere.com": "Cohere",
    "allenai.org": "AI2",
    "xai.com": "xAI",
}


def infer_organization(feed_name: str, url: str) -> str:
    """Infer organization name from a feed/blog name and its URL.

    Strategy:
    1. Case-insensitive exact match on the feed/blog name.
    2. Domain match on the URL netloc (www-prefix stripped).

    Returns an empty string when the organization cannot be reliably
    determined — callers must NOT fill in guesses from author names here;
    that path still lives in rules.py as a lower-confidence fallback.
    """
    # 1. Name match (most reliable: config explicitly names the source)
    name_key = feed_name.strip().lower()
    org = _NAME_TO_ORG.get(name_key, "")
    if org:
        return org

    # 2. Domain match
    try:
        netloc = urlparse(url).netloc.lower()
        if netloc.startswith("www."):
            netloc = netloc[4:]
    except Exception:
        return ""

    return _DOMAIN_TO_ORG.get(netloc, "")


# ---------------------------------------------------------------------------
# Date helpers
# ---------------------------------------------------------------------------


def parse_entry_date(entry) -> date | None:
    """Parse the publication date from a feedparser entry.

    Tries published, updated, and created fields in that order,
    using both the raw string value and the pre-parsed tuple.
    Returns None if no date can be parsed.
    """
    for field in ("published", "updated", "created"):
        val = entry.get(field)
        if val:
            try:
                return parsedate_to_datetime(val).date()
            except Exception:
                pass
        parsed = entry.get(f"{field}_parsed")
        if parsed:
            try:
                return date(*parsed[:3])
            except Exception:
                pass
    return None
