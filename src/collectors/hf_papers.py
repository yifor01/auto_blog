"""HuggingFace Daily Papers collector."""

from __future__ import annotations

import time
from datetime import date

from bs4 import BeautifulSoup

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import get_http_client, load_config

_logger = get_logger("collectors.hf_papers")


class HFPapersCollector(BaseCollector):
    name = "hf_papers"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["hf_papers"]
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        url = f"https://huggingface.co/papers?date={target_date.isoformat()}"

        items: list[ContentItem] = []
        client = get_http_client()
        try:
            resp = client.get(url)
            if resp.status_code in (400, 403):
                _logger.warning("HF Papers error status", extra={"status_code": resp.status_code, "date": str(target_date)})
                client.close()
                return items
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")

            # HF Papers 頁面的論文卡片
            for article in soup.select("article"):
                title_el = article.select_one("h3 a")
                if not title_el:
                    continue

                title = title_el.get_text(strip=True)
                href = title_el.get("href", "")
                paper_url = f"https://huggingface.co{href}" if href.startswith("/") else href

                # 嘗試取得 upvote 數
                upvote_el = article.select_one("[class*='upvote'], button")
                upvotes = 0
                if upvote_el:
                    text = upvote_el.get_text(strip=True)
                    try:
                        upvotes = int("".join(c for c in text if c.isdigit()) or "0")
                    except ValueError:
                        pass

                # 修改為去論文單獨頁面抓取 abstract
                abstract = ""
                try:
                    p_resp = client.get(paper_url)
                    if p_resp.status_code == 200:
                        p_soup = BeautifulSoup(p_resp.text, "html.parser")
                        ps = p_soup.select("p")
                        for p in ps:
                            text = p.get_text(strip=True)
                            if len(text) > 100:  # 通常 abstract 都比較長
                                abstract = text
                                break
                except Exception:
                    pass
                
                # 如果還是抓不到，我們預設為標題
                if not abstract:
                    abstract = f"AI Paper from HuggingFace Daily Papers: {title}"
                
                # Sleep briefly to be nice to the server
                time.sleep(0.5)

                items.append(
                    ContentItem(
                        source=SourceType.HF_PAPERS,
                        source_name="HuggingFace Daily Papers",
                        title=title,
                        url=paper_url,
                        authors=[],
                        abstract=abstract,
                        published_date=target_date,
                        tags=["hf_daily"],
                        raw_metadata={
                            "upvotes": upvotes,
                            "hf_url": paper_url,
                        },
                    )
                )
        except Exception as e:
            _logger.error("HF Papers collection error", extra={"error": str(e), "date": str(target_date)})
        finally:
            client.close()

        _logger.info("HF Papers collection complete", extra={"count": len(items), "date": str(target_date)})
        return items
