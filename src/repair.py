"""歷史資料修復：HF 摘要黏字重抓 + 跨來源 HTML entity 解碼。

why 合併成一支：兩種修復都要翻 data/raw、output/lists、output/posts 同一批
檔案，分兩支等於把每個檔案改兩遍、產生兩次巨量 diff。

修復目標與判定依據見 docs/superpowers/specs/2026-07-28-raw-data-box-design.md
"""

from __future__ import annotations

import html
import json
import re
from collections.abc import Callable
from datetime import date, timedelta
from pathlib import Path

from src.collectors.hf_papers import fetch_paper_abstract, looks_unspaced
from src.logger import get_logger
from src.utils import save_json

_logger = get_logger(__name__)

_RAW_DIR = Path("data/raw")
_LISTS_DIR = Path("output/lists")
_POSTS_DIR = Path("output/posts")

_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
# 只吃 frontmatter 的 title 行；body 不動（可能含程式碼區塊裡字面意義的 &amp;）
_TITLE_LINE_RE = re.compile(r'^title:[ \t]*(.*)$', re.MULTILINE)


def _norm_url(url: str) -> str:
    """輕量 URL 正規化，與 web/src/enrich.ts 的 normalizeUrl 行為一致。

    why 不用 utils.normalize_url：那支為去重設計，會排序 query、去 www.，
    比對兩端來源相同（皆為 ContentItem.url 原值）時只會徒增不一致風險。
    """
    if not url:
        return ""
    return url.strip().rstrip("/").replace("http:", "https:", 1)


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


def repair_all(
    days: int | None = None,
    dry_run: bool = False,
    fetcher: Callable[[str], str] | None = None,
) -> dict:
    """修復歷史資料。fetcher 為注入點（測試必須注入，避免真實 HTTP）。"""
    stats = {"hf_refetched": 0, "hf_failed": 0, "entities_fixed": 0, "files_written": 0}
    fetched: dict[str, str] = {}  # normUrl -> 修好的 abstract，供 lists 同步

    if fetcher is None:
        from src.utils import get_http_client

        client = get_http_client()
        fetcher = lambda url: fetch_paper_abstract(client, url)  # noqa: E731

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
            if it.get("source") == "hf_papers" and looks_unspaced(it.get("abstract") or ""):
                new_abs = fetcher(it.get("url", ""))
                if new_abs and not looks_unspaced(new_abs):
                    it["abstract"] = new_abs
                    fetched[_norm_url(it.get("url", ""))] = new_abs
                    stats["hf_refetched"] += 1
                    changed = True
                else:
                    stats["hf_failed"] += 1
                    _logger.warning("HF abstract refetch failed", extra={"url": it.get("url")})
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
                repaired = fetched.get(_norm_url(e.get("url", "")))
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
