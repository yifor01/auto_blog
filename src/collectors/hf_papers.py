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

# HF 沒有當日論文時（週末 / 假日）不會回 404，而是 302 到最近一個有資料的日期，
# 轉址後路徑長這樣：/papers/date/2026-07-24
_HF_DATE_PATH_RE = re.compile(r"/papers/date/(\d{4}-\d{2}-\d{2})")

# Delay between per-paper HF page fetches to be respectful to the server
_ENRICH_DELAY_SECONDS = 0.5


def _hf_list_url(target_date: date) -> str:
    return f"https://huggingface.co/papers?date={target_date.isoformat()}"


def _resolved_page_date(resp, target_date: date) -> date | None:
    """回傳頁面實際呈現的日期。無轉址（仍是 ?date= 形式）視為就是 target_date。"""
    m = _HF_DATE_PATH_RE.search(str(resp.url))
    if not m:
        return target_date
    try:
        return date.fromisoformat(m.group(1))
    except ValueError:
        return None


def _parse_upvotes(article) -> int:
    """從論文卡片取得 upvote 數。

    HF 現在把票數放在 role="checkbox" 的投票方塊裡（內含一個 svg 三角形 +
    <div class="leading-none">數字</div>），卡片內既沒有 class 帶 'upvote' 的元素、
    也沒有任何 <button>，舊 selector 一律 match 不到 → upvotes 全部靜默變 0。
    """
    el = article.select_one('[role="checkbox"] .leading-none') or article.select_one('[role="checkbox"]')
    if not el:
        _logger.warning("HF upvote element not found")
        return 0
    text = " ".join(el.get_text().split())
    digits = "".join(c for c in text if c.isdigit())
    if not digits:
        _logger.warning("HF upvote element found but no digits", extra={"text": text[:50]})
        return 0
    return int(digits)


def fetch_upvotes(target_date: date) -> dict[str, int]:
    """輕量抓取某日各論文的最新票數（paper_url → upvotes），只打列表頁一次。

    供隔日補票用：論文剛發布時票數還沒累積，隔天回頭抓才是有意義的排序訊號。
    日期對不上（HF 轉址到別天）或抓取失敗時回傳空 dict，呼叫端不做任何更新。
    """
    client = get_http_client()
    votes: dict[str, int] = {}
    try:
        resp = client.get(_hf_list_url(target_date))
        if resp.status_code != 200:
            _logger.warning(
                "HF upvote refetch non-200",
                extra={"status_code": resp.status_code, "date": str(target_date)},
            )
            return votes
        actual = _resolved_page_date(resp, target_date)
        if actual != target_date:
            _logger.warning(
                "HF upvote refetch date mismatch, skipping",
                extra={"date": str(target_date), "actual": str(actual), "final_url": str(resp.url)},
            )
            return votes
        soup = BeautifulSoup(resp.text, "html.parser")
        for article in soup.select("article"):
            title_el = article.select_one("h3 a")
            if not title_el:
                continue
            href = title_el.get("href", "")
            paper_url = f"https://huggingface.co{href}" if href.startswith("/") else href
            votes[paper_url] = _parse_upvotes(article)
    except Exception as e:
        _logger.error("HF upvote refetch error", extra={"error": str(e), "date": str(target_date)})
    finally:
        client.close()

    _logger.info("HF upvote refetch complete", extra={"count": len(votes), "date": str(target_date)})
    return votes


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
        url = _hf_list_url(target_date)

        items: list[ContentItem] = []
        client = get_http_client()
        try:
            resp = client.get(url)
            if resp.status_code in (400, 403):
                _logger.warning("HF Papers error status", extra={"status_code": resp.status_code, "date": str(target_date)})
                client.close()
                return items
            resp.raise_for_status()

            # HF 當日無論文時會 302 到最近有資料的日期並回 200，直接收就會把
            # 別天的論文標成今天（實測 07-25、07-26 都拿到 07-24 的 22 篇）
            actual_date = _resolved_page_date(resp, target_date)
            if actual_date != target_date:
                _logger.warning(
                    "HF Papers redirected to another date, skipping",
                    extra={"date": str(target_date), "actual": str(actual_date), "final_url": str(resp.url)},
                )
                client.close()
                return items

            soup = BeautifulSoup(resp.text, "html.parser")

            # HF Papers 頁面的論文卡片
            for article in soup.select("article"):
                title_el = article.select_one("h3 a")
                if not title_el:
                    continue

                title = title_el.get_text(strip=True)
                href = title_el.get("href", "")
                paper_url = f"https://huggingface.co{href}" if href.startswith("/") else href

                # 當日票數通常還沒累積，隔日由 backfill_hf_upvotes() 回補
                upvotes = _parse_upvotes(article)

                # 修改為去論文單獨頁面抓取 abstract
                abstract = ""
                try:
                    p_resp = client.get(paper_url)
                    if p_resp.status_code == 200:
                        p_soup = BeautifulSoup(p_resp.text, "html.parser")
                        ps = p_soup.select("p")
                        for p in ps:
                            # HF 論文頁的 abstract 被拆成逐字元 text node，get_text(strip=True)
                            # 會把節點間空白全部吃掉（整段變成一個無空白長字串），
                            # get_text(" ") 則會變成每字元間插空白 —— 只能先取原文再正規化空白
                            text = " ".join(p.get_text().split())
                            if len(text) > 100:  # 通常 abstract 都比較長
                                abstract = text
                                break
                    else:
                        _logger.warning(
                            "Non-200 fetching HF paper page, skipping enrichment",
                            extra={"url": paper_url, "status_code": p_resp.status_code},
                        )
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
                time.sleep(_ENRICH_DELAY_SECONDS)

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
