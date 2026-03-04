"""NewsAPI collector for mainstream tech news."""

from __future__ import annotations

import os
from datetime import date, timedelta

from src.collectors.base import BaseCollector
from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import get_http_client, load_config

_logger = get_logger("collectors.newsapi")

API_URL = "https://newsapi.org/v2/everything"


class NewsAPICollector(BaseCollector):
    name = "newsapi"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config.get("collectors", {}).get("newsapi", {})
        if not cfg.get("enabled", True):
            return []

        api_key = os.getenv("NEWSAPI_KEY", "")
        if not api_key:
            _logger.warning("NEWSAPI_KEY not set, skipping NewsAPI collector")
            return []

        target_date = target_date or date.today()
        query: str = cfg.get("query", "generative AI OR LLM OR large language model")
        language: str = cfg.get("language", "en")
        max_results: int = cfg.get("max_results", 20)
        sort_by: str = cfg.get("sort_by", "relevancy")

        # 嚴格日期範圍：只取 target_date 當天
        date_from = target_date.isoformat()
        date_to = (target_date + timedelta(days=1)).isoformat()

        items: list[ContentItem] = []
        client = get_http_client()

        try:
            resp = client.get(
                API_URL,
                params={
                    "q": query,
                    "from": date_from,
                    "to": date_to,
                    "language": language,
                    "sortBy": sort_by,
                    "pageSize": min(max_results, 100),
                    "apiKey": api_key,
                },
            )
            resp.raise_for_status()
            data = resp.json()

            for article in data.get("articles", [])[:max_results]:
                title = article.get("title") or ""
                # 過濾 [Removed] 標題
                if not title or title.strip() == "[Removed]":
                    continue

                url = article.get("url") or ""
                if not url:
                    continue

                description = article.get("description") or ""
                content_text = article.get("content") or ""
                abstract = description or content_text[:500]

                source_name = article.get("source", {}).get("name", "NewsAPI")
                author = article.get("author") or ""

                items.append(
                    ContentItem(
                        source=SourceType.NEWSAPI,
                        source_name=source_name,
                        title=title,
                        url=url,
                        authors=[author] if author else [],
                        abstract=abstract,
                        published_date=target_date,
                        tags=["newsapi"],
                        raw_metadata={
                            "newsapi_source": source_name,
                            "published_at": article.get("publishedAt", ""),
                        },
                    )
                )

        except Exception as e:
            _logger.error("NewsAPI collection error", extra={"error": str(e)})
        finally:
            client.close()

        _logger.info("NewsAPI collection complete", extra={"count": len(items)})
        return items
