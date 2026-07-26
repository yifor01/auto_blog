"""Shared helper utilities for collectors."""

from __future__ import annotations

import re
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
    # claude.com / anthropic.com 走 raw.githubusercontent 鏡像 feed，
    # domain 比對必然落空，只能靠 name 命中 —— 推不出 organization
    # 就不會進 pinned（見 src/pinned.py），整條 feed 等於白加。
    "claude blog": "Anthropic",
    "anthropic news": "Anthropic",
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
# Title helpers
# ---------------------------------------------------------------------------

# Anthropic 系鏡像 feed 由 Selenium 掃頁面產生，會把版面上的日期戳與分類標籤
# 一併吸進 <title>，例如 "Jul 24, 2026Frontier Red TeamProject Pilot: ..."。
# 不能用 \b 當邊界 —— 日期正是黏在字母上（"2026Frontier"、"ResearchJun"），
# 兩端都不存在 word boundary。改以月份縮寫錨定。
_FEED_DATE_RE = re.compile(
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s*\d{4}(?!\d)"
)

# 分類與標題之間沒有空格，接合處必為「小寫字母緊接大寫字母」。
# 限定 3–29 字元且只含英文字母與空格，避免誤切 PyTorch / vLLM 這類 CamelCase 產品名。
_CATEGORY_PREFIX_RE = re.compile(r"^[A-Z][A-Za-z ]{2,28}?(?<=[a-z])(?=[A-Z])")


def clean_feed_title(title: str) -> str:
    """移除 feed 標題中被吸進來的日期戳與分類前綴。

    僅在偵測到日期戳時才嘗試切除分類前綴 —— 沒有日期戳的標題一律原樣返回，
    因為 lowercase→uppercase 的接合在正常標題中也可能出現（CamelCase 產品名）。
    切不出可信的分類前綴時只移除日期、保留其餘。
    """
    if not title:
        return ""
    cleaned = title.strip()
    if not cleaned:
        return ""

    stripped, hits = _FEED_DATE_RE.subn("", cleaned)
    if not hits:
        return cleaned

    stripped = stripped.strip()
    match = _CATEGORY_PREFIX_RE.match(stripped)
    if match:
        stripped = stripped[match.end():]
    return stripped.strip()


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
