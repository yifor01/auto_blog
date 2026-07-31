"""Blog scraper for individual AI blogs."""

from __future__ import annotations

import httpx
from datetime import date
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from src.collectors._helpers import infer_organization, parse_entry_date
from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import (
    ABSTRACT_MAX_CHARS_DEFAULT,
    extract_full_text_from_html,
    fetch_article_text,
    get_http_client,
    load_config,
)

_logger = get_logger("collectors.blogs")

_INVALID_TITLE_KEYWORDS = frozenset([
    "rss feed", "subscribe via email", "subscribe", "newsletter",
    "mailing list", "sign up", "signup", "notification",
    "atom feed", "sitemap", "follow us",
])

_FEED_URL_LAST_SEGMENTS = frozenset(["feed", "rss", "atom"])
_FEED_URL_EXTENSIONS = (".xml", ".rss", ".atom")


def _rss_candidates(index_url: str, rss_paths: list[str]) -> list[str]:
    """產生 RSS 探測網址：每條路徑先試「相對索引頁」再試「相對網站根」。

    索引頁本身帶路徑時（如 https://huyenchip.com/blog/），feed 常在網站根
    （https://huyenchip.com/feed）而非索引頁下。只拼索引頁會 6 條全 404，
    退回 HTML 抓取後連文章網址也拼錯，最終每篇只剩 "Title: {title}"。

    索引頁在網站根時兩種拼法相同，去重後探測次數與網址完全不變。
    """
    candidates: list[str] = []
    for path in rss_paths:
        for url in (index_url.rstrip("/") + path, urljoin(index_url, path)):
            if url not in candidates:
                candidates.append(url)
    return candidates


class BlogCollector(BaseCollector):
    name = "blogs"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["blogs"]
        if not cfg.get("enabled", True):
            return []

        sources = cfg.get("sources", [])
        max_chars = config["collectors"].get("abstract_max_chars", ABSTRACT_MAX_CHARS_DEFAULT)
        target_date = target_date or date.today()
        items: list[ContentItem] = []

        client = get_http_client()
        try:
            for blog in sources:
                blog_name = blog["name"]
                blog_url = blog["url"]
                try:
                    collected = self._scrape_blog(client, blog_name, blog_url, target_date, max_chars)
                    items.extend(collected)
                    _logger.info("Blog collected", extra={"blog": blog_name, "count": len(collected)})
                except Exception as e:
                    _logger.error("Blog error", extra={"blog": blog_name, "error": str(e)})
        finally:
            client.close()

        _logger.info("Blogs collection complete", extra={"total_count": len(items)})
        return items

    def _scrape_blog(
        self,
        client,
        name: str,
        url: str,
        target_date: date,
        max_chars: int = ABSTRACT_MAX_CHARS_DEFAULT,
    ) -> list[ContentItem]:
        """通用部落格爬蟲：嘗試找 RSS feed，否則 scrape HTML."""
        # 先嘗試常見 RSS 路徑；第一個成功就停，連線層錯誤立即放棄剩餘路徑
        rss_paths = ["/feed", "/rss", "/atom.xml", "/feed.xml", "/rss.xml", "/index.xml"]
        for rss_url in _rss_candidates(url, rss_paths):
            try:
                resp = client.get(rss_url)
                if resp.status_code == 200 and (
                    "xml" in resp.headers.get("content-type", "")
                    or "<?xml" in resp.text[:200]
                    or "<rss" in resp.text[:500]
                    or "<feed" in resp.text[:500]
                ):
                    import feedparser

                    parsed = feedparser.parse(resp.text)
                    if parsed.entries:
                        return self._parse_feed_entries(
                            parsed.entries, name, url, target_date, client, max_chars
                        )
                else:
                    _logger.debug(
                        "RSS path probe: non-success status",
                        extra={"rss_url": rss_url, "status_code": resp.status_code},
                    )
            except (httpx.TimeoutException, httpx.ConnectError) as e:
                # 連線層錯誤（timeout / DNS）：同一 host 其他路徑也連不上，直接放棄
                _logger.debug(
                    "RSS path probe: connection-level error, aborting remaining paths",
                    extra={"rss_url": rss_url, "error": str(e)},
                )
                break
            except Exception as e:
                _logger.debug(
                    "RSS path probe: unexpected error",
                    extra={"rss_url": rss_url, "error": str(e)},
                )
                continue

        # Fallback: scrape HTML 找最新文章連結
        return self._scrape_html(client, name, url, target_date, max_chars)

    def _parse_feed_entries(
        self,
        entries: list,
        name: str,
        base_url: str,
        target_date: date,
        client,
        max_chars: int = ABSTRACT_MAX_CHARS_DEFAULT,
    ) -> list[ContentItem]:
        items: list[ContentItem] = []
        for entry in entries[:10]:  # 最多看 10 篇
            pub_date = parse_entry_date(entry)
            if pub_date is None:
                _logger.debug(
                    "Skipping blog entry: cannot parse date",
                    extra={"blog": name, "title": entry.get("title", "")[:80]},
                )
                continue
            # 只取最近 7 天的（blog 更新慢）
            if abs((pub_date - target_date).days) > 7:
                continue

            raw_html = ""
            # Priority 1: content:encoded / Atom content
            if hasattr(entry, "content") and entry.content:
                raw_html = entry.content[0].get("value", "")
            # Priority 2: summary / description
            if not raw_html:
                raw_html = getattr(entry, "summary", "")
            abstract = extract_full_text_from_html(raw_html, max_chars) if raw_html else ""

            # Priority 3: 短摘要補抓
            article_url = entry.get("link", "")
            if len(abstract) < 1000 and article_url:
                fetched = fetch_article_text(article_url, client, max_chars)
                if len(fetched) > len(abstract):
                    abstract = fetched

            if not self._is_valid_blog_entry(
                title=entry.get("title", ""),
                url=article_url,
                abstract=abstract,
            ):
                _logger.debug("Skipping invalid blog entry", extra={"title": entry.get("title", "")[:80]})
                continue

            items.append(
                ContentItem(
                    source=SourceType.BLOG,
                    source_name=name,
                    title=entry.get("title", ""),
                    url=article_url,
                    authors=[name],
                    abstract=abstract,
                    published_date=pub_date,
                    tags=["blog"],
                    organization=infer_organization(name, base_url),
                    raw_metadata={"blog_name": name, "blog_url": base_url},
                )
            )
        return items

    def _scrape_html(
        self,
        client,
        name: str,
        url: str,
        target_date: date,
        max_chars: int = ABSTRACT_MAX_CHARS_DEFAULT,
    ) -> list[ContentItem]:
        """Fallback HTML scraping for blogs without RSS."""
        try:
            resp = client.get(url)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")

            items: list[ContentItem] = []
            # 找所有文章連結
            for a_tag in soup.select("article a, .post a, h2 a, h3 a")[:10]:
                title = a_tag.get_text(strip=True)
                href = a_tag.get("href", "")
                if not title or len(title) < 5:
                    continue

                # urljoin 正確處理三種形式：絕對網址原樣、根相對接 origin、
                # 相對路徑接索引頁。手寫 rstrip + href 會把根相對的 /2025/x.html
                # 接到索引頁路徑上（https://huyenchip.com/blog/2025/x.html → 404）
                href = urljoin(url, href)

                # 為了避免每個部落格發送 10 次 request，這裡不主動 fetch content。
                # 但為了評分機制，我們將它標記為「待抓取」或提示此為 HTML 抓取。
                # 因為使用者反映 blog 來源缺少摘要，我們嘗試發起請求抓取正文前幾段，最多 10 篇應該還好。
                content_abstract = ""
                try:
                    p_resp = client.get(href)
                    if p_resp.status_code == 200:
                        # 走共用提取：容器優先序 + 雜訊剝除 + 句界截斷，
                        # 不再自行 select_one（會踩祖先優先的坑）或只取前 3 段
                        content_abstract = extract_full_text_from_html(p_resp.text, max_chars)
                except Exception:
                    pass

                final_abstract = content_abstract or f"Title: {title}"
                if not self._is_valid_blog_entry(title=title, url=href, abstract=final_abstract):
                    _logger.debug("Skipping invalid HTML scraped entry", extra={"title": title[:80]})
                    continue

                items.append(
                    ContentItem(
                        source=SourceType.BLOG,
                        source_name=name,
                        title=title,
                        url=href,
                        authors=[name],
                        abstract=final_abstract,
                        published_date=target_date,
                        tags=["blog"],
                        organization=infer_organization(name, url),
                        raw_metadata={"blog_name": name, "blog_url": url},
                    )
                )
            return items
        except Exception:
            return []

    @staticmethod
    def _is_valid_blog_entry(title: str, url: str, abstract: str) -> bool:
        """過濾導航頁/訂閱連結，只保留真正的文章。"""
        if not title or len(title.strip()) < 5:
            return False
        title_lower = title.lower()
        if any(kw in title_lower for kw in _INVALID_TITLE_KEYWORDS):
            return False
        if not url:
            return False
        path = urlparse(url).path.rstrip("/")
        last_seg = path.split("/")[-1].lower() if path else ""
        if last_seg in _FEED_URL_LAST_SEGMENTS or path.lower().endswith(_FEED_URL_EXTENSIONS):
            return False
        if not abstract.strip():
            return False
        return True

