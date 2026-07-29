"""歷史資料修復：HF 摘要黏字重抓 + Layer A 清洗回補（entity / 媒體標記 / 簡→繁）
＋ `data/scored` 依 `data/raw` 對齊。

why 合併成一支：所有修復都要翻 data/raw、data/scored、output/lists、output/posts
同一批檔案，分成多支等於把每個檔案改多遍、產生多次巨量 diff。

why 這裡是清洗的唯一歸屬：讀取端（`models.item_from_raw()` /
`models.scored_from_raw()`）刻意**無損還原**存檔原值，不做二次清洗——否則每讀一次
就多套一層 s2twp 而漂移。分工是「讀取端無損，清洗歸資料層」，資料層就是本模組。

修復目標與判定依據見 docs/superpowers/specs/2026-07-28-raw-data-box-design.md
"""

from __future__ import annotations

import html
import json
import re
import time
from collections.abc import Callable
from datetime import date, timedelta
from functools import lru_cache
from pathlib import Path

from src.collectors.hf_papers import (
    _ENRICH_DELAY_SECONDS,
    _extract_arxiv_id,
    _fetch_arxiv_abstract,
    fetch_paper_abstract,
    looks_unspaced,
)
from src.logger import get_logger
from src.models import _LAYER_A_FIELDS, strip_media_tags
from src.utils import normalize_url_light, save_json, to_traditional_shape_only

_logger = get_logger(__name__)

_RAW_DIR = Path("data/raw")
_SCORED_DIR = Path("data/scored")
_LISTS_DIR = Path("output/lists")
_POSTS_DIR = Path("output/posts")

# output/lists 的條目沒有 tags 欄位，只有 title / abstract
_LIST_FIELDS = ("title", "abstract")

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


# ──────────────────────────────────────────────────────────
# 單一欄位的清洗：entity 解碼 → 剝媒體標記 → 簡→繁（只修字形）
#
# 順序刻意與 `ContentItem` 的 Layer A validator 一致（unescape → strip → 轉繁）：
# `&lt;img src=...&gt;` 要解碼後才認得出是標記，剝完再轉繁也少餵 OpenCC 一段標記。
# ──────────────────────────────────────────────────────────


@lru_cache(maxsize=None)
def _is_simplified_char(ch: str) -> bool:
    """單字元層級是否為簡體。

    「單字元」是關鍵：OpenCC 的詞組規則要有上下文才會觸發，餵單一字元等於只問
    「這個字本身是不是簡體」（`个` 是、`了` 不是）。OpenCC 不可用時
    `to_traditional_shape_only()` 原樣回傳 → 一律判定為非簡體 → `_to_traditional_safe()`
    整個退化成 no-op，這是刻意的安全降級。
    """
    return to_traditional_shape_only(ch) != ch


def _has_control_chars(text: str) -> bool:
    return any(ord(c) < 32 and c not in "\n\r\t" for c in text)


def _convert_once(text: str) -> str:
    """單輪簡→繁，含兩道守門（理由見 `_to_traditional_safe()`）。"""
    if _has_control_chars(text):
        return text
    if not any(_is_simplified_char(c) for c in text):
        return text
    return to_traditional_shape_only(text)


# 收斂上限。實測全庫 71765 個欄位最多 2 輪就穩定，留餘裕但不無限跑。
_MAX_CONVERT_ROUNDS = 5


def _to_traditional_safe(text: str) -> str:
    """簡→繁，但只在「這個欄位真的含簡體字」時才動手，且收斂到不動點。

    ## why 用 s2tw（shape only）而不是 Layer A 的 `to_traditional()`（s2twp）

    s2twp 帶台灣詞庫、對繁體**不冪等**（文件→檔案→…）。歷史 raw 混著兩種資料：
    2026-06-20 之前是未經 Layer A 的真簡體，之後是已經 Layer A 過的繁體。對全量
    套 s2twp，等於把後半段再轉一次——實測一輪 round-trip 就漂 731 個欄位 / 521 筆
    記錄（3.00%），正是前幾輪從讀取路徑移除的那個 bug。

    ## why 還要加「含簡體字」這道門

    s2tw 對**純繁體**輸入不是無害的：OpenCC 的詞組規則會誤觸發，實測
    `說明了一件事` → `說明瞭一件事`（明了→明瞭）、`裡面包括` → `裡麵包括`
    （面包→麵包）、`一目了然` 之外的 `了` 也會中招。這些字（了/面/里/干/托/杆）
    單獨看不是簡體，只有在詞組規則下才被改寫——所以「欄位裡至少要有一個
    **單字元層級**的簡體字」正好把「整段簡體的舊資料」與「已是繁體的新資料」分開。
    實測 data/raw：894 個欄位會被 s2tw 改動，這道門擋掉 76 個（其中 37 個是
    純繁體被詞組規則誤改），放行 804 個。

    殘餘風險（已實測、可接受）：3 個欄位是「幾乎全繁體但夾了 1 個簡體字」的
    量子位長摘要，過門後仍會吃到詞組規則（如 2026-07-29 的 `說明了`→`說明瞭`）。
    不進一步收緊是因為：放行的 804 個欄位裡有 90 個要靠詞組規則才轉得對
    （关系→關係、制作→製作），而 Layer A 對新資料本來就是全詞組轉換——
    收緊到「只換簡體字位置」會讓舊資料反而與新資料不一致。

    ## why 擋掉含控制字元的欄位

    少數 abstract 是被當成文字存進來的 PNG / JPEG 位元組。OpenCC 遇到 NUL 會
    **靜默截斷**——實測 1543 字的欄位轉完只剩 7 字。那些欄位本來就是壞資料，
    但靜默截斷是不可逆的破壞，一律不碰（data/raw 17 個、data/scored 1 個）。

    ## why 要收斂到不動點（而不是轉一次就收工）

    OpenCC 的詞組規則吃上下文，而第一輪把周邊字轉繁之後**上下文就變了**，於是
    第二輪還會再動一次：`互不干扰` →（1）`互不干擾` →（2）`互不幹擾`。實測全庫
    71765 個欄位有 16 個是這種兩輪才穩定的，涉及 21 個字元，全部是「一簡對多繁」
    的歧義字（干→幹 9、托→託 6、里→裡 2、了/出/占/卷 各 1）。

    轉一次就收工的話，這 16 個欄位會在**下一次跑 repair-content 時**再變一格——
    正是本專案一路在修的「每跑一次漂一格」。所以這裡直接收斂，把不動點寫進檔案，
    之後再跑幾次都不會再動。

    取捨（已實測、刻意接受）：收斂會讓那 21 個字裡約半數轉成較不通用的異體
    （`互不干擾` → `互不幹擾`）。另一個選項是「不穩定就整個欄位不轉」，但那會讓
    16 篇**整段簡體**的長摘要原封留著簡體——對使用者而言遠比個位數的異體字糟。
    超過 `_MAX_CONVERT_ROUNDS` 仍不收斂就整個欄位不動並記 warning（實測 0 筆）。
    """
    out = text
    for _ in range(_MAX_CONVERT_ROUNDS):
        nxt = _convert_once(out)
        if nxt == out:
            return out
        out = nxt
    _logger.warning("簡→繁轉換未收斂，該欄位保持原值", extra={"preview": text[:80]})
    return text


def _clean_value(value: str, stats: dict) -> str:
    """單一字串跑完三道清洗，並分類累計統計。"""
    unescaped = html.unescape(value)
    if unescaped != value:
        stats["entities_fixed"] += 1

    stripped = strip_media_tags(unescaped)
    if stripped != unescaped:
        stats["media_stripped"] += 1

    converted = _to_traditional_safe(stripped)
    if converted != stripped:
        stats["simplified_converted"] += 1

    return converted


def _clean_field(value, stats: dict):
    """回傳 (新值, 是否改動)。字串與字串陣列（tags）都處理，其餘型別原樣返回。"""
    if isinstance(value, str):
        new = _clean_value(value, stats)
        return new, new != value
    if isinstance(value, list):
        out, changed = [], False
        for v in value:
            nv, c = _clean_field(v, stats)
            out.append(nv)
            changed = changed or c
        return out, changed
    return value, False


def _clean_fields_in_place(container: dict, fields, stats: dict) -> bool:
    """就地清洗 dict 的指定欄位，回傳是否有改動。"""
    changed = False
    for field in fields:
        if field not in container:
            continue
        new_val, ch = _clean_field(container[field], stats)
        if ch:
            container[field] = new_val
            changed = True
    return changed


# ──────────────────────────────────────────────────────────
# HF 摘要重抓
# ──────────────────────────────────────────────────────────


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


# ──────────────────────────────────────────────────────────
# 各層檔案的修復
# ──────────────────────────────────────────────────────────


def _load_json_list(path: Path, label: str):
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        _logger.warning(f"Skipping unreadable {label} file", extra={"path": str(path)})
        return None
    return data if isinstance(data, list) else None


def _repair_raw_file(
    path: Path,
    stats: dict,
    dry_run: bool,
    fetcher: Callable[[str], str] | None,
    arxiv_fetcher: Callable[[str], str],
    fetched: dict[str, str],
) -> list | None:
    """修 `data/raw/{date}.json`，回傳清洗後的 items（供同日 scored 對齊）。

    回傳的是**記憶體中已清洗**的 items，即使 dry_run 沒寫檔也一樣——scored 的
    候選數因此在 dry-run 下也反映「raw 修乾淨之後」的狀態，不會把髒 raw 當基準。
    """
    items = _load_json_list(path, "raw")
    if items is None:
        return None

    changed = False
    for it in items:
        if not isinstance(it, dict):
            continue
        # 1) HF 黏字重抓
        #    source 限定是硬約束：looks_unspaced() 對其他來源不保證正確，
        #    全來源掃描會誤判 hackernews 26 筆 / reddit 8 筆（整串 URL 的留言）。
        #    那些若被拿去 fetch_paper_abstract，等於把 gist 頁 / 圖片 URL 的
        #    任意 <p> 寫進真實 abstract —— 是寫壞資料，不是修不完。
        refetched = False
        if it.get("source") == "hf_papers" and looks_unspaced(it.get("abstract") or ""):
            if dry_run:
                stats["hf_candidates"] += 1
            else:
                new_abs = _repair_hf_abstract(it.get("url", ""), fetcher, arxiv_fetcher)
                if new_abs:
                    it["abstract"] = new_abs
                    stats["hf_refetched"] += 1
                    changed = refetched = True
                else:
                    stats["hf_failed"] += 1
                    _logger.warning(
                        "HF abstract refetch failed (page + arXiv)",
                        extra={"url": it.get("url")},
                    )
        # 2) Layer A 清洗（entity / 媒體標記 / 簡→繁）
        if _clean_fields_in_place(it, _LAYER_A_FIELDS, stats):
            changed = True
        # 重抓值同樣先清洗完才進對照表——output/lists 要拿到與 raw 逐字相同的成品
        if refetched:
            fetched[normalize_url_light(it.get("url", ""))] = it["abstract"]

    if changed and not dry_run:
        save_json(items, path)
        stats["files_written"] += 1
    return items


def _repair_scored_file(
    path: Path, raw_items: list | None, stats: dict, dry_run: bool
) -> None:
    """把 `data/scored/{date}.json` 的 Layer A 欄位對齊同日 `data/raw`。

    why 需要這一步：`data/scored` 的 item 是 collect 當下的副本，從未被 repair 掃過。
    實測全庫 2712 筆與 raw 的一致率 97.46%（69 筆不一致：17 筆未解碼 entity、
    52 筆 abstract 空白被吃掉），而讀取端改成無損還原之後，這些落差就直接變成
    使用者可見的回歸（同一頁的「原始資料 box」讀 raw、列表讀 scored，兩處對不上）。

    配對用 `normalize_url_light()`：兩端拿的是同一個 `ContentItem.url` 原值，只需要
    吸收 scheme / 尾斜線這類無害差異。實測配對率 100%（2712/2712，0 缺 raw 檔、
    0 對不上 URL）。

    **評分欄位一律不動**——只覆寫 `_LAYER_A_FIELDS`。配對不到的記錄（實測 0 筆）
    仍會跑一次清洗，不會因為缺 raw 就整筆放生。
    """
    recs = _load_json_list(path, "scored")
    if recs is None:
        return

    raw_map: dict[str, dict] = {}
    for it in raw_items or []:
        if isinstance(it, dict):
            raw_map[normalize_url_light(it.get("url", ""))] = it

    changed = False
    for rec in recs:
        if not isinstance(rec, dict):
            continue
        item = rec.get("item")
        if not isinstance(item, dict):
            continue

        source = raw_map.get(normalize_url_light(item.get("url", "")))
        if source is not None:
            for field in _LAYER_A_FIELDS:
                if field not in source or item.get(field) == source[field]:
                    continue
                value = source[field]
                # list 要複製再塞：直接指派會讓 raw 與 scored 共用同一個 list 物件
                item[field] = list(value) if isinstance(value, list) else value
                stats["scored_backfilled"] += 1
                changed = True

        if _clean_fields_in_place(item, _LAYER_A_FIELDS, stats):
            changed = True

    if changed and not dry_run:
        save_json(recs, path)
        stats["files_written"] += 1


def _repair_lists_file(
    path: Path, fetched: dict[str, str], stats: dict, dry_run: bool
) -> None:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return
    if not isinstance(doc, dict):
        return

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
            if _clean_fields_in_place(e, _LIST_FIELDS, stats):
                changed = True

    if changed and not dry_run:
        save_json(doc, path)
        stats["files_written"] += 1


def _repair_post_file(path: Path, stats: dict, dry_run: bool) -> None:
    """只改 frontmatter 的 `title:` 行。

    body 一律不動：那是 LLM 生成內容，裡面的 `&amp;` 可能是字面意義、`<script>`
    可能在程式碼區塊裡。檔名也不動——slug 是 Astro 頁面 id，改名會斷連結與
    localStorage 已讀記錄。
    """
    text = path.read_text(encoding="utf-8")
    m = _TITLE_LINE_RE.search(text)
    if not m:
        return
    new_title, changed = _clean_field(m.group(1), stats)
    if not changed or dry_run:
        return
    path.write_text(text[: m.start(1)] + new_title + text[m.end(1) :], encoding="utf-8")
    stats["files_written"] += 1


def repair_all(
    days: int | None = None,
    dry_run: bool = False,
    fetcher: Callable[[str], str] | None = None,
    arxiv_fetcher: Callable[[str], str] | None = None,
) -> dict:
    """修復歷史資料（raw / scored / lists / posts 四處）。

    fetcher(url) / arxiv_fetcher(arxiv_id) 為注入點，測試必須注入以避免真實 HTTP。

    why 注入 fetcher 就不再建立任何真實 client：只要呼叫端注入了 fetcher（＝測試
    路徑），未注入的 arxiv_fetcher 會退化成永遠回 "" 的 no-op，而不是偷偷建一個
    真的 arXiv client。測試因此不可能意外連網。生產路徑（兩者皆 None）才建真的。

    dry_run 完全不連網：只清點待修候選數，不重抓也不寫檔。

    why raw 與 scored 同日成對處理（而非各掃各的）：scored 的對齊來源必須是
    **修乾淨之後**的 raw，否則等於把髒資料原封抄過去。成對處理同時把記憶體
    上限壓在單日（data/raw 全量 33MB，整批載入沒必要）。
    """
    stats = {
        "hf_candidates": 0,
        "hf_refetched": 0,
        "hf_failed": 0,
        "entities_fixed": 0,
        "media_stripped": 0,
        "simplified_converted": 0,
        "scored_backfilled": 0,
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

    # ── data/raw + data/scored（同日成對）───────────────────
    stems: set[str] = set()
    for directory in (_RAW_DIR, _SCORED_DIR):
        if directory.exists():
            stems |= {p.stem for p in directory.glob("*.json") if _within_days(p, days)}
    for stem in sorted(stems):
        raw_items = _repair_raw_file(
            _RAW_DIR / f"{stem}.json", stats, dry_run, fetcher, arxiv_fetcher, fetched
        )
        _repair_scored_file(_SCORED_DIR / f"{stem}.json", raw_items, stats, dry_run)

    # ── output/lists ──────────────────────────────────────
    for path in sorted(_LISTS_DIR.glob("*.json")) if _LISTS_DIR.exists() else []:
        if _within_days(path, days):
            _repair_lists_file(path, fetched, stats, dry_run)

    # ── output/posts（只動 frontmatter title 行）─────────────
    for path in sorted(_POSTS_DIR.glob("*.md")) if _POSTS_DIR.exists() else []:
        if _within_days(path, days):
            _repair_post_file(path, stats, dry_run)

    return stats
