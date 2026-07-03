"""Hacker News collector using the Algolia API."""

from __future__ import annotations

import re
import time
from datetime import date, datetime
from urllib.parse import urlparse
from zoneinfo import ZoneInfo

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import build_link_abstract, get_http_client, load_config

_logger = get_logger("collectors.hackernews")

API_BASE = "https://hn.algolia.com/api/v1/search"

_HN_429_INITIAL_DELAY = 2.0   # seconds; doubles each retry: 2 → 4 → 8
_HN_429_MAX_RETRIES = 3

# Algolia 已不支援以 points 作 numericFilters（2026-06 起回 400），
# 因此每頁抓大量結果後在 client-side 過濾 min_points
_HN_HITS_PER_PAGE = 100


def _hn_fetch_with_backoff(client, params: dict, query: str) -> dict | None:
    """Fetch HN Algolia search results with 429 exponential backoff.

    Returns parsed JSON dict on success, or None if all retries are exhausted
    or a non-429 error occurs (caller should log and skip).
    """
    delay = _HN_429_INITIAL_DELAY
    for attempt in range(_HN_429_MAX_RETRIES + 1):
        resp = client.get(API_BASE, params=params)
        if resp.status_code == 429:
            if attempt < _HN_429_MAX_RETRIES:
                _logger.warning(
                    "HackerNews 429 rate limited, retrying",
                    extra={"query": query, "wait_seconds": delay, "attempt": attempt + 1},
                )
                time.sleep(delay)
                delay *= 2
                continue
            _logger.warning(
                "HackerNews 429 max retries exceeded, skipping query",
                extra={"query": query},
            )
            return None
        resp.raise_for_status()
        return resp.json()
    return None  # unreachable; satisfies type checker


class HackerNewsCollector(BaseCollector):
    name = "hackernews"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config.get("collectors", {}).get("hackernews", {})
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        queries: list[str] = cfg.get("queries", ["AI", "LLM", "GPT"])
        min_points: int = cfg.get("min_points", 50)
        max_results: int = cfg.get("max_results", 30)

        # 計算目標日期的 Unix timestamp 範圍（以台灣時區 Asia/Taipei 為基準）
        start_dt = datetime(target_date.year, target_date.month, target_date.day, tzinfo=ZoneInfo("Asia/Taipei"))
        start_ts = int(start_dt.timestamp())
        end_ts = start_ts + 86400  # +1 day

        items: list[ContentItem] = []
        seen_ids: set[str] = set()
        client = get_http_client()

        try:
            for i, query in enumerate(queries):
                if i > 0:
                    time.sleep(0.2)

                try:
                    params = {
                        "query": query,
                        "tags": "story",
                        "numericFilters": f"created_at_i>{start_ts},created_at_i<{end_ts}",
                        "hitsPerPage": _HN_HITS_PER_PAGE,
                    }
                    data = _hn_fetch_with_backoff(client, params, query)
                    if data is None:
                        continue
                except Exception as e:
                    _logger.warning("HackerNews query error", extra={"query": query, "error": str(e)})
                    continue

                for hit in data.get("hits", []):
                    object_id = hit.get("objectID", "")
                    if object_id in seen_ids:
                        continue
                    seen_ids.add(object_id)

                    title = hit.get("title", "")
                    if not title:
                        continue

                    if (hit.get("points") or 0) < min_points:
                        continue

                    raw_url = hit.get("url", "")
                    hn_url = f"https://news.ycombinator.com/item?id={object_id}"
                    if raw_url and raw_url.startswith(("http://", "https://")):
                        url = raw_url
                    else:
                        url = hn_url
                    points = hit.get("points", 0)
                    num_comments = hit.get("num_comments", 0)
                    author = hit.get("author", "")
                    story_text_raw = hit.get("story_text") or ""
                    story_text = re.sub(r"<[^>]+>", " ", story_text_raw).strip()

                    if story_text:
                        abstract = story_text
                    elif raw_url:
                        engagement = f"{points} points, {num_comments} comments on Hacker News"
                        domain = urlparse(raw_url).netloc.replace("www.", "")
                        abstract = build_link_abstract(url, client, engagement, domain)
                    else:
                        abstract = f"news.ycombinator.com — {points} points, {num_comments} comments on Hacker News"

                    items.append(
                        ContentItem(
                            source=SourceType.HACKERNEWS,
                            source_name="Hacker News",
                            title=title,
                            url=url,
                            authors=[author] if author else [],
                            abstract=abstract,
                            published_date=target_date,
                            tags=["hackernews"],
                            raw_metadata={
                                "points": points,
                                "num_comments": num_comments,
                                "hn_url": hn_url,
                                "object_id": object_id,
                            },
                        )
                    )

                    if len(items) >= max_results:
                        break

                if len(items) >= max_results:
                    break
        except Exception as e:
            _logger.error("HackerNews collection error", extra={"error": str(e)})
        finally:
            client.close()

        _logger.info("HackerNews collection complete", extra={"count": len(items)})
        return items
