"""歷史資料修復：HF 摘要黏字重抓 + 跨來源 HTML entity 解碼。

why 合併成一支：兩種修復都要翻 data/raw、output/lists、output/posts 同一批
檔案，分兩支等於把每個檔案改兩遍、產生兩次巨量 diff。

修復目標與判定依據見 docs/superpowers/specs/2026-07-28-raw-data-box-design.md
"""

from __future__ import annotations

import html
import json
import re
import time
from collections.abc import Callable
from datetime import date, timedelta
from pathlib import Path

from src.collectors.hf_papers import (
    _ENRICH_DELAY_SECONDS,
    _extract_arxiv_id,
    _fetch_arxiv_abstract,
    fetch_paper_abstract,
    looks_unspaced,
)
from src.logger import get_logger
from src.utils import normalize_url_light, save_json

_logger = get_logger(__name__)

_RAW_DIR = Path("data/raw")
_LISTS_DIR = Path("output/lists")
_POSTS_DIR = Path("output/posts")

_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
# 只吃 frontmatter 的 title 行；body 不動（可能含程式碼區塊裡字面意義的 &amp;）
_TITLE_LINE_RE = re.compile(r'^title:[ \t]*(.*)$', re.MULTILINE)


def _within_days(path: Path, days: int | None) -> bool:
    if days is None:
        return True
    m = _DATE_RE.match(path.stem)
    if not m:
        return False
    return date.fromisoformat(m.group(1)) >= date.today() - timedelta(days=days)


def _unescape_field(value):
    """回傳 (新值, 修正筆數)。字串與字串陣列都處理。"""
    if isinstance(value, str):
        new = html.unescape(value)
        return new, int(new != value)
    if isinstance(value, list):
        out, n = [], 0
        for v in value:
            nv, c = _unescape_field(v)
            out.append(nv)
            n += c
        return out, n
    return value, 0


def _build_default_fetchers() -> tuple[Callable[[str], str], Callable[[str], str]]:
    """建立生產用的真實 HTTP fetcher（每次請求前先節流）。

    why 每次請求前 sleep：本模組會在迴圈裡連續打 HF 論文頁（全期約 192 次），
    沿用 collectors/hf_papers.py 的 collect() 對同一端點的既有節流慣例，
    刻意 import `_ENRICH_DELAY_SECONDS` 而非另立常數——兩處調的是同一個端點，
    分成兩個常數只會日後各自漂移。

    why sleep 放在 fetcher 內而非呼叫迴圈：注入 stub 的測試因此完全不會 sleep，
    節流只發生在真的要連網的路徑上。
    """
    from src.utils import get_http_client

    client = get_http_client()

    def _fetch_hf(url: str) -> str:
        time.sleep(_ENRICH_DELAY_SECONDS)
        return fetch_paper_abstract(client, url)

    def _fetch_arxiv(arxiv_id: str) -> str:
        time.sleep(_ENRICH_DELAY_SECONDS)
        return _fetch_arxiv_abstract(arxiv_id, client)

    return _fetch_hf, _fetch_arxiv


def _repair_hf_abstract(
    url: str,
    fetcher: Callable[[str], str],
    arxiv_fetcher: Callable[[str], str],
) -> str:
    """重抓單筆 HF 摘要，修不好回 ""。

    三段式（依設計 spec §6）：重抓論文頁 → 失敗或結果仍判定為破損則走 arXiv
    fallback → 兩者皆失敗才回空字串，由呼叫端保留原值。

    why 一定要有 arXiv 這層：192 筆破損項全部抽得出 arxiv_id（覆蓋率 192/192），
    而它正是 HF 端被限流時唯一的救生索——少了它，一旦 HF 開始擋就整批修不動。
    """
    new_abs = fetcher(url)
    if new_abs and not looks_unspaced(new_abs):
        return new_abs

    arxiv_id = _extract_arxiv_id(url)
    if not arxiv_id:
        return ""
    alt = arxiv_fetcher(arxiv_id)
    if alt and not looks_unspaced(alt):
        _logger.info("HF abstract repaired via arXiv fallback", extra={"arxiv_id": arxiv_id})
        return alt
    return ""


def repair_all(
    days: int | None = None,
    dry_run: bool = False,
    fetcher: Callable[[str], str] | None = None,
    arxiv_fetcher: Callable[[str], str] | None = None,
) -> dict:
    """修復歷史資料。

    fetcher(url) / arxiv_fetcher(arxiv_id) 為注入點，測試必須注入以避免真實 HTTP。

    why 注入 fetcher 就不再建立任何真實 client：只要呼叫端注入了 fetcher（＝測試
    路徑），未注入的 arxiv_fetcher 會退化成永遠回 "" 的 no-op，而不是偷偷建一個
    真的 arXiv client。測試因此不可能意外連網。生產路徑（兩者皆 None）才建真的。

    dry_run 完全不連網：只清點待修候選數（hf_candidates），不重抓也不寫檔。
    """
    stats = {
        "hf_candidates": 0,
        "hf_refetched": 0,
        "hf_failed": 0,
        "entities_fixed": 0,
        "files_written": 0,
    }
    fetched: dict[str, str] = {}  # normUrl -> 修好的 abstract，供 lists 同步

    if dry_run:
        # dry-run 的用途是確認規模，不需要真的抓；官方流程是「先 dry-run 再實跑」，
        # 若這裡也連網，光是預覽就把總請求數翻倍。
        fetcher = arxiv_fetcher = None
    elif fetcher is None:
        fetcher, default_arxiv = _build_default_fetchers()
        if arxiv_fetcher is None:
            arxiv_fetcher = default_arxiv
    if arxiv_fetcher is None:
        arxiv_fetcher = lambda _arxiv_id: ""  # noqa: E731

    # ── data/raw ──────────────────────────────────────────
    for path in sorted(_RAW_DIR.glob("*.json")) if _RAW_DIR.exists() else []:
        if not _within_days(path, days):
            continue
        try:
            items = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            _logger.warning("Skipping unreadable raw file", extra={"path": str(path)})
            continue
        if not isinstance(items, list):
            continue

        changed = False
        for it in items:
            if not isinstance(it, dict):
                continue
            # 1) HF 黏字重抓
            #    source 限定是硬約束：looks_unspaced() 對其他來源不保證正確，
            #    全來源掃描會誤判 hackernews 26 筆 / reddit 8 筆（整串 URL 的留言）。
            #    那些若被拿去 fetch_paper_abstract，等於把 gist 頁 / 圖片 URL 的
            #    任意 <p> 寫進真實 abstract —— 是寫壞資料，不是修不完。
            if it.get("source") == "hf_papers" and looks_unspaced(it.get("abstract") or ""):
                if dry_run:
                    stats["hf_candidates"] += 1
                else:
                    new_abs = _repair_hf_abstract(it.get("url", ""), fetcher, arxiv_fetcher)
                    if new_abs:
                        it["abstract"] = new_abs
                        fetched[normalize_url_light(it.get("url", ""))] = new_abs
                        stats["hf_refetched"] += 1
                        changed = True
                    else:
                        stats["hf_failed"] += 1
                        _logger.warning(
                            "HF abstract refetch failed (page + arXiv)",
                            extra={"url": it.get("url")},
                        )
            # 2) entity 解碼
            for field in ("title", "abstract", "tags"):
                if field not in it:
                    continue
                new_val, n = _unescape_field(it[field])
                if n:
                    it[field] = new_val
                    stats["entities_fixed"] += n
                    changed = True

        if changed and not dry_run:
            save_json(items, path)
            stats["files_written"] += 1

    # ── output/lists ──────────────────────────────────────
    for path in sorted(_LISTS_DIR.glob("*.json")) if _LISTS_DIR.exists() else []:
        if not _within_days(path, days):
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue

        changed = False
        buckets = [doc.get("github") or []]
        papers = doc.get("papers") or {}
        buckets += [papers.get("hf") or [], papers.get("others") or []]
        for entries in buckets:
            for e in entries:
                if not isinstance(e, dict):
                    continue
                repaired = fetched.get(normalize_url_light(e.get("url", "")))
                if repaired and e.get("abstract") != repaired:
                    e["abstract"] = repaired
                    changed = True
                for field in ("title", "abstract"):
                    if field not in e:
                        continue
                    new_val, n = _unescape_field(e[field])
                    if n:
                        e[field] = new_val
                        stats["entities_fixed"] += n
                        changed = True

        if changed and not dry_run:
            save_json(doc, path)
            stats["files_written"] += 1

    # ── output/posts（只動 frontmatter title 行）─────────────
    for path in sorted(_POSTS_DIR.glob("*.md")) if _POSTS_DIR.exists() else []:
        if not _within_days(path, days):
            continue
        text = path.read_text(encoding="utf-8")
        m = _TITLE_LINE_RE.search(text)
        if not m:
            continue
        new_title, n = _unescape_field(m.group(1))
        if not n:
            continue
        stats["entities_fixed"] += n
        if not dry_run:
            path.write_text(
                text[: m.start(1)] + new_title + text[m.end(1) :], encoding="utf-8"
            )
            stats["files_written"] += 1

    return stats
