"""ChatPaper API collector."""

from __future__ import annotations

from datetime import date

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import (
    date_to_chatpaper_ts,
    get_http_client,
    load_config,
)

_logger = get_logger("collectors.chatpaper")


class ChatPaperCollector(BaseCollector):
    name = "chatpaper"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["chatpaper"]
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        ts = date_to_chatpaper_ts(target_date)
        base_url = cfg["base_url"]
        page_size = cfg.get("page_size", 30)
        categories = cfg.get("categories", [{"id": 2, "name": "AI"}])

        all_items: list[ContentItem] = []
        seen_ids: set[str] = set()

        client = get_http_client()
        try:
            for cat in categories:
                cat_id = cat["id"]
                cat_name = cat["name"]
                try:
                    url = f"{base_url}?page=1&page_size={page_size}&category_id={cat_id}&language=english&date={ts}"
                    resp = client.get(url)
                    resp.raise_for_status()
                    data = resp.json()

                    for article in data.get("items", []):
                        source_id = article.get("source_id", "")
                        if source_id in seen_ids:
                            continue
                        seen_ids.add(source_id)

                        all_items.append(
                            ContentItem(
                                source=SourceType.CHATPAPER,
                                source_name=f"ChatPaper/{cat_name}",
                                title=article.get("title", ""),
                                url=article.get("article_url", ""),
                                authors=article.get("authors", []),
                                abstract=article.get("abstract", ""),
                                published_date=target_date,
                                tags=[
                                    c.get("tag", "")
                                    for c in article.get("category_list", [])
                                ],
                                organization=article.get("organization", ""),
                                raw_metadata={
                                    "arxiv_id": source_id,
                                    "pdf_url": article.get("pdf_url", ""),
                                    "chatpaper_id": article.get("id"),
                                    "source_type": article.get("source_type", ""),
                                },
                            )
                        )

                    _logger.info("ChatPaper category complete", extra={"category": cat_name, "count": len(data.get("items", []))})
                except Exception as e:
                    _logger.error("ChatPaper category error", extra={"category": cat_name, "error": str(e)})
        finally:
            client.close()

        _logger.info("ChatPaper collection complete", extra={"count": len(all_items)})
        return all_items
