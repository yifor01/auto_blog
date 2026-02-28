"""arXiv collector using the arxiv Python package."""

from __future__ import annotations

from datetime import date

import arxiv

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import load_config

_logger = get_logger("collectors.arxiv")


class ArxivCollector(BaseCollector):
    name = "arxiv"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["arxiv"]
        if not cfg.get("enabled", True):
            return []

        categories = cfg.get("categories", ["cs.AI", "cs.CL", "cs.LG", "cs.CV"])
        max_results = cfg.get("max_results", 50)

        cat_query = " OR ".join(f"cat:{c}" for c in categories)

        client = arxiv.Client()
        search = arxiv.Search(
            query=cat_query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
            sort_order=arxiv.SortOrder.Descending,
        )

        items: list[ContentItem] = []
        try:
            for result in client.results(search):
                pub_date = result.published.date()
                # arXiv 時間(UTC/EST)比台灣晚，通常今天的 paper 日期會是昨天或前天
                if target_date:
                    from datetime import timedelta
                    if pub_date < target_date - timedelta(days=2) or pub_date > target_date:
                        continue

                items.append(
                    ContentItem(
                        source=SourceType.ARXIV,
                        source_name="arXiv",
                        title=result.title,
                        url=result.entry_id,
                        authors=[a.name for a in result.authors],
                        abstract=result.summary,
                        published_date=pub_date,
                        tags=[str(c) for c in result.categories],
                        organization="",
                        raw_metadata={
                            "arxiv_id": result.entry_id.split("/")[-1],
                            "pdf_url": result.pdf_url,
                            "primary_category": str(result.primary_category),
                        },
                    )
                )
        except Exception as e:
            _logger.error("arXiv collection error", extra={"error": str(e)})

        _logger.info("arXiv collection complete", extra={"count": len(items)})
        return items
