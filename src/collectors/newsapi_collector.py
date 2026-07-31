"""NewsAPI collector for mainstream tech news."""

from __future__ import annotations

import os
from datetime import date, datetime, timedelta

from src.collectors.base import BaseCollector
from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import get_http_client, load_config

_logger = get_logger("collectors.newsapi")

API_URL = "https://newsapi.org/v2/everything"

# NewsAPI 的 Developer（免費）方案對新文章有 ~24 小時延遲。查當天必定回
# HTTP 200 + status ok + totalResults 0——完全合法的空結果，raise_for_status
# 抓不到、log 也只會寫 count: 0。實測 T-0=0 / T-1=15 / T-2=82 / T-3=85，
# 所以預設退兩天取完整的一天。付費方案可在 config 設 lag_days: 0。
LAG_DAYS_DEFAULT = 2


def _parse_published_at(value: str) -> date | None:
    """解析 NewsAPI 的 ISO 8601 publishedAt（結尾 Z）。無法解析回 None。"""
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
    except ValueError:
        return None


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

        # 免費方案有 ~24h 延遲：往回退 lag_days 取「已沉澱完整」的那一天。
        # 每天各取一天、不重疊，重複的部分交給既有的 7 天跨日去重處理。
        lag_days: int = cfg.get("lag_days", LAG_DAYS_DEFAULT)
        query_date = target_date - timedelta(days=lag_days)
        date_from = query_date.isoformat()
        date_to = (query_date + timedelta(days=1)).isoformat()

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
                published_at = article.get("publishedAt", "")
                # 用真實發布日；缺失/格式壞掉才退回查詢日（不可用 target_date，
                # 那會把兩天前的舊聞標成當天，並影響 pinned 的 published_date 排序）
                pub_date = _parse_published_at(published_at) or query_date

                items.append(
                    ContentItem(
                        source=SourceType.NEWSAPI,
                        source_name=source_name,
                        title=title,
                        url=url,
                        authors=[author] if author else [],
                        abstract=abstract,
                        published_date=pub_date,
                        tags=["newsapi"],
                        raw_metadata={
                            "newsapi_source": source_name,
                            "published_at": published_at,
                        },
                    )
                )

        except Exception as e:
            _logger.error("NewsAPI collection error", extra={"error": str(e)})
        finally:
            client.close()

        _logger.info("NewsAPI collection complete", extra={"count": len(items)})
        return items
