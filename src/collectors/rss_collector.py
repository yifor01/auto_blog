"""RSS feed collector for AI news and blogs."""

from __future__ import annotations

from datetime import date, datetime
from email.utils import parsedate_to_datetime

import feedparser

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import (
    extract_full_text_from_html,
    fetch_article_text,
    get_http_client,
    load_config,
)

_logger = get_logger("collectors.rss")


class RSSCollector(BaseCollector):
    name = "rss"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["rss"]
        if not cfg.get("enabled", True):
            return []

        feeds = cfg.get("feeds", [])
        target_date = target_date or date.today()
        items: list[ContentItem] = []

        client = get_http_client()
        try:
            for feed_cfg in feeds:
                feed_name = feed_cfg["name"]
                feed_url = feed_cfg["url"]
                try:
                    parsed = feedparser.parse(feed_url)
                    count = 0
                    for entry in parsed.entries:
                        # 解析發布日期
                        pub_date = self._parse_date(entry)
                        if pub_date is None:
                            _logger.debug(
                                "Skipping entry: cannot parse date",
                                extra={"feed": feed_name, "title": entry.get("title", "")[:80]},
                            )
                            continue
                        # 只取今天的，但給 1 天的容差
                        if abs((pub_date - target_date).days) > 1:
                            continue

                        article_url = entry.get("link", "")
                        abstract = self._extract_abstract(entry, article_url, client)

                        items.append(
                            ContentItem(
                                source=SourceType.RSS,
                                source_name=feed_name,
                                title=entry.get("title", ""),
                                url=article_url,
                                authors=[
                                    a.get("name", "") for a in entry.get("authors", [])
                                ]
                                if hasattr(entry, "authors")
                                else [],
                                abstract=abstract,
                                published_date=pub_date,
                                tags=self._extract_tags(entry),
                                raw_metadata={
                                    "feed_name": feed_name,
                                    "feed_url": feed_url,
                                },
                            )
                        )
                        count += 1

                    _logger.info("RSS feed complete", extra={"feed": feed_name, "count": count})
                except Exception as e:
                    _logger.error("RSS feed error", extra={"feed": feed_name, "error": str(e)})
        finally:
            client.close()

        _logger.info("RSS collection complete", extra={"total_count": len(items)})
        return items

    @staticmethod
    def _extract_abstract(
        entry,
        article_url: str,
        client,
        min_len: int = 1000,
        max_len: int = 2000,
    ) -> str:
        """三段 priority 提取 abstract：content:encoded > summary > HTTP fetch。"""
        raw_html = ""
        # Priority 1: content:encoded / Atom content
        if hasattr(entry, "content") and entry.content:
            raw_html = entry.content[0].get("value", "")
        # Priority 2: summary / description
        if not raw_html:
            raw_html = getattr(entry, "summary", "") or getattr(entry, "description", "")

        abstract = extract_full_text_from_html(raw_html, max_len) if raw_html else ""

        # Priority 3: 短摘要補抓
        if len(abstract) < min_len and article_url:
            fetched = fetch_article_text(article_url, client, max_len)
            if len(fetched) > len(abstract):
                abstract = fetched

        return abstract

    @staticmethod
    def _parse_date(entry) -> date | None:
        """嘗試從 RSS entry 解析日期。"""
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

    @staticmethod
    def _extract_tags(entry) -> list[str]:
        tags = []
        for tag in entry.get("tags", []):
            term = tag.get("term", "")
            if term:
                tags.append(term)
        return tags
