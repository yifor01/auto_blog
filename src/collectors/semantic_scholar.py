"""Semantic Scholar Graph API collector.

使用 Semantic Scholar Academic Graph API 的 bulk search endpoint 收集近 N 天
發表的 AI/ML 論文。API 文件：https://api.semanticscholar.org/api-docs/

設計重點：
- API key 由環境變數 ``SEMANTIC_SCHOLAR_API_KEY`` 提供；**沒有 key 仍可呼叫**
  （S2 無 key 也能用，只是 rate limit 較嚴），此時不帶 ``x-api-key`` header。
- externalIds 內含 ArXiv id 時放入 ``raw_metadata["arxiv_id"]``，讓條目走
  arxiv 去重 key（與 arxiv / hf_papers collector 的相同論文去重）。
- 429 限流採指數退避重試（2 → 4 → 8 秒）。
"""

from __future__ import annotations

import os
import re
import time
from datetime import date, datetime, timedelta

from src.collectors.base import BaseCollector
from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import get_http_client, load_config

_logger = get_logger("collectors.semantic_scholar")

API_URL = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"

# 至少包含這些 fields（task 要求）
DEFAULT_FIELDS = "title,abstract,url,publicationDate,authors,externalIds,citationCount,venue"

_S2_429_INITIAL_DELAY = 2.0   # seconds; doubles each retry: 2 → 4 → 8
_S2_429_MAX_RETRIES = 3

# arxiv id 去版本號正規化（與 hf_papers collector 一致用 bare canonical id）
_ARXIV_VERSION_RE = re.compile(r"v\d+$")


def _normalize_arxiv_id(raw: str) -> str:
    """正規化 ArXiv id：去除尾端版本號（e.g. 2606.11190v1 → 2606.11190）。"""
    return _ARXIV_VERSION_RE.sub("", (raw or "").strip())


def _s2_fetch_with_backoff(
    client, params: dict, headers: dict, query: str
) -> dict | None:
    """呼叫 S2 bulk search，遇 429 指數退避重試。

    成功回傳 parsed JSON dict；重試耗盡或非 429 錯誤回傳 None（caller 應 log 並跳過）。
    """
    delay = _S2_429_INITIAL_DELAY
    for attempt in range(_S2_429_MAX_RETRIES + 1):
        resp = client.get(API_URL, params=params, headers=headers)
        if resp.status_code == 429:
            if attempt < _S2_429_MAX_RETRIES:
                _logger.warning(
                    "SemanticScholar 429 rate limited, retrying",
                    extra={"query": query, "wait_seconds": delay, "attempt": attempt + 1},
                )
                time.sleep(delay)
                delay *= 2
                continue
            _logger.warning(
                "SemanticScholar 429 max retries exceeded, skipping",
                extra={"query": query},
            )
            return None
        resp.raise_for_status()
        return resp.json()
    return None  # unreachable; satisfies type checker


class SemanticScholarCollector(BaseCollector):
    name = "semantic_scholar"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config.get("collectors", {}).get("semantic_scholar", {})
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        queries: list[str] = cfg.get("queries", ["large language model", "LLM"])
        days_back: int = cfg.get("days_back", 3)
        limit: int = cfg.get("limit", 30)
        fields: str = cfg.get("fields", DEFAULT_FIELDS)
        fields_of_study: list[str] = cfg.get("fields_of_study", ["Computer Science"])

        # bulk search 支援 boolean query：用 | 串接關鍵字（OR），各自加括號
        query_str = " | ".join(f"({q})" for q in queries)

        # publicationDateOrYear 日期範圍：YYYY-MM-DD:YYYY-MM-DD
        start = (target_date - timedelta(days=max(days_back, 0))).isoformat()
        end = target_date.isoformat()

        # API key：有則帶 x-api-key header，無則不帶（仍可呼叫，限流較嚴）
        api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "").strip()
        headers: dict[str, str] = {}
        if api_key:
            headers["x-api-key"] = api_key
        else:
            _logger.info("SEMANTIC_SCHOLAR_API_KEY not set, calling unauthenticated (stricter rate limit)")

        params = {
            "query": query_str,
            "fields": fields,
            "publicationDateOrYear": f"{start}:{end}",
            "sort": "publicationDate:desc",
        }
        if fields_of_study:
            params["fieldsOfStudy"] = ",".join(fields_of_study)

        items: list[ContentItem] = []
        seen_ids: set[str] = set()
        client = get_http_client()

        try:
            data = _s2_fetch_with_backoff(client, params, headers, query_str)
            if data is None:
                return items

            for paper in data.get("data", []) or []:
                paper_id = paper.get("paperId") or ""
                if paper_id in seen_ids:
                    continue
                seen_ids.add(paper_id)

                title = (paper.get("title") or "").strip()
                if not title:
                    continue

                external_ids = paper.get("externalIds") or {}
                arxiv_id = _normalize_arxiv_id(external_ids.get("ArXiv", ""))

                # URL：優先 S2 url，否則用 arxiv abs 頁，最後用 S2 paper 頁
                url = paper.get("url") or ""
                if not url and arxiv_id:
                    url = f"https://arxiv.org/abs/{arxiv_id}"
                if not url and paper_id:
                    url = f"https://www.semanticscholar.org/paper/{paper_id}"
                if not url:
                    continue

                abstract = (paper.get("abstract") or "").strip()
                if not abstract:
                    # 缺 abstract：保留條目，用標題 + venue 組 fallback（rule scoring 會視為低品質）
                    venue = (paper.get("venue") or "").strip()
                    abstract = f"{title}." + (f" {venue}" if venue else "")

                authors = [
                    a.get("name", "")
                    for a in (paper.get("authors") or [])
                    if a.get("name")
                ]

                # published_date：用論文真實發表日，無法解析則 fallback 到 target_date
                pub_date = target_date
                raw_pub = paper.get("publicationDate")
                if raw_pub:
                    try:
                        pub_date = datetime.strptime(raw_pub, "%Y-%m-%d").date()
                    except (ValueError, TypeError):
                        pub_date = target_date

                items.append(
                    ContentItem(
                        source=SourceType.SEMANTIC_SCHOLAR,
                        source_name="Semantic Scholar",
                        title=title,
                        url=url,
                        authors=authors,
                        abstract=abstract,
                        published_date=pub_date,
                        tags=["semantic_scholar"],
                        organization="",
                        raw_metadata={
                            "arxiv_id": arxiv_id,  # 走 arxiv 去重 key
                            "paper_id": paper_id,
                            "citation_count": paper.get("citationCount", 0),
                            "venue": paper.get("venue") or "",
                            "publication_date": raw_pub or "",
                        },
                    )
                )

                if len(items) >= limit:
                    break

        except Exception as e:
            _logger.error("SemanticScholar collection error", extra={"error": str(e)})
        finally:
            client.close()

        _logger.info("SemanticScholar collection complete", extra={"count": len(items)})
        return items
