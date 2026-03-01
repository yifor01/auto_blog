"""HuggingFace Daily Papers collector."""

from __future__ import annotations

import re
import time
import xml.etree.ElementTree as ET
from datetime import date
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import get_http_client, load_config

_logger = get_logger("collectors.hf_papers")

_ARXIV_API_URL = "https://export.arxiv.org/api/query"
_ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}
_ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")


def _extract_arxiv_id(paper_url: str) -> str | None:
    """從 HF paper URL 解析 arxiv ID。"""
    path = urlparse(paper_url).path.rstrip("/")
    parts = path.strip("/").split("/")
    if len(parts) == 2 and parts[0] == "papers":
        candidate = parts[1]
        if _ARXIV_ID_RE.match(candidate):
            return candidate
    return None


def _fetch_arxiv_abstract(arxiv_id: str, client) -> str:
    """從 arXiv API 取得論文摘要。失敗時回傳空字串。"""
    try:
        resp = client.get(_ARXIV_API_URL, params={"id_list": arxiv_id})
        if resp.status_code != 200:
            return ""
        root = ET.fromstring(resp.text)
        entry = root.find("atom:entry", _ARXIV_NS)
        if entry is None:
            return ""
        summary_el = entry.find("atom:summary", _ARXIV_NS)
        if summary_el is None or not summary_el.text:
            return ""
        return " ".join(summary_el.text.split())  # 清理多餘換行
    except Exception as e:
        _logger.debug("arXiv API fetch error", extra={"arxiv_id": arxiv_id, "error": str(e)})
        return ""


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
                except Exception as e:
                    _logger.debug(
                        "Failed to fetch HF paper abstract",
                        extra={"url": paper_url, "error": str(e)},
                    )
                
                # 如果還是抓不到，我們預設為標題
                if not abstract:
                    abstract = f"AI Paper from HuggingFace Daily Papers: {title}"

                # NEW: arXiv abstract enrichment
                arxiv_id = _extract_arxiv_id(paper_url)
                if len(abstract.strip()) < 100 and arxiv_id:
                    _logger.debug("Attempting arXiv enrichment", extra={"arxiv_id": arxiv_id})
                    arxiv_abstract = _fetch_arxiv_abstract(arxiv_id, client)
                    if arxiv_abstract:
                        abstract = arxiv_abstract
                        _logger.info("arXiv enrichment succeeded", extra={"arxiv_id": arxiv_id, "abstract_len": len(abstract)})
                    else:
                        _logger.warning("arXiv enrichment failed, keeping fallback", extra={"arxiv_id": arxiv_id})

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
                            "arxiv_id": arxiv_id or "",  # 新增
                        },
                    )
                )
        except Exception as e:
            _logger.error("HF Papers collection error", extra={"error": str(e), "date": str(target_date)})
        finally:
            client.close()

        _logger.info("HF Papers collection complete", extra={"count": len(items), "date": str(target_date)})
        return items
