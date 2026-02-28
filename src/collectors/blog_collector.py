"""Blog scraper for individual AI blogs."""

from __future__ import annotations

from datetime import date

from bs4 import BeautifulSoup

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import extract_full_text_from_html, fetch_article_text, get_http_client, load_config

_logger = get_logger("collectors.blogs")


class BlogCollector(BaseCollector):
    name = "blogs"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["blogs"]
        if not cfg.get("enabled", True):
            return []

        sources = cfg.get("sources", [])
        target_date = target_date or date.today()
        items: list[ContentItem] = []

        client = get_http_client()
        try:
            for blog in sources:
                blog_name = blog["name"]
                blog_url = blog["url"]
                try:
                    collected = self._scrape_blog(client, blog_name, blog_url, target_date)
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
    ) -> list[ContentItem]:
        """通用部落格爬蟲：嘗試找 RSS feed，否則 scrape HTML."""
        # 先嘗試常見 RSS 路徑
        rss_paths = ["/feed", "/rss", "/atom.xml", "/feed.xml", "/rss.xml", "/index.xml"]
        for rss_path in rss_paths:
            rss_url = url.rstrip("/") + rss_path
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
                            parsed.entries, name, url, target_date, client
                        )
            except Exception:
                continue

        # Fallback: scrape HTML 找最新文章連結
        return self._scrape_html(client, name, url, target_date)

    def _parse_feed_entries(
        self,
        entries: list,
        name: str,
        base_url: str,
        target_date: date,
        client,
    ) -> list[ContentItem]:
        items: list[ContentItem] = []
        for entry in entries[:10]:  # 最多看 10 篇
            pub_date = self._parse_entry_date(entry) or target_date
            # 只取最近 7 天的（blog 更新慢）
            delta = abs((pub_date - target_date).days)
            if delta > 7:
                continue

            raw_html = ""
            # Priority 1: content:encoded / Atom content
            if hasattr(entry, "content") and entry.content:
                raw_html = entry.content[0].get("value", "")
            # Priority 2: summary / description
            if not raw_html:
                raw_html = getattr(entry, "summary", "")
            abstract = extract_full_text_from_html(raw_html, 2000) if raw_html else ""

            # Priority 3: 短摘要補抓
            article_url = entry.get("link", "")
            if len(abstract) < 200 and article_url:
                fetched = fetch_article_text(article_url, client, 2000)
                if len(fetched) > len(abstract):
                    abstract = fetched

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

                if href.startswith("/"):
                    href = url.rstrip("/") + href

                # 為了避免每個部落格發送 10 次 request，這裡不主動 fetch content。
                # 但為了評分機制，我們將它標記為「待抓取」或提示此為 HTML 抓取。
                # 因為使用者反映 blog 來源缺少摘要，我們嘗試發起請求抓取正文前幾段，最多 10 篇應該還好。
                content_abstract = ""
                try:
                    p_resp = client.get(href)
                    if p_resp.status_code == 200:
                        p_soup = BeautifulSoup(p_resp.text, "html.parser")
                        # 找尋常見的正文標籤
                        article_body = p_soup.select_one("article, .post-content, .entry-content, main")
                        if article_body:
                            ps = article_body.select("p")
                            content_abstract = " ".join([p.get_text(strip=True) for p in ps[:3]])
                        else:
                            content_abstract = " ".join([p.get_text(strip=True) for p in p_soup.select("p")[:3]])
                except Exception:
                    pass

                items.append(
                    ContentItem(
                        source=SourceType.BLOG,
                        source_name=name,
                        title=title,
                        url=href,
                        authors=[name],
                        abstract=content_abstract[:1000] if content_abstract else f"Title: {title}",
                        published_date=target_date,
                        tags=["blog"],
                        raw_metadata={"blog_name": name, "blog_url": url},
                    )
                )
            return items
        except Exception:
            return []

    @staticmethod
    def _parse_entry_date(entry) -> date | None:
        from email.utils import parsedate_to_datetime

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
