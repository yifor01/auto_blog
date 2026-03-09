"""資料讀取層 — 重用 src/utils 的路徑常數與 load_json。"""

from __future__ import annotations

import re
import time as _time
from datetime import date, timedelta
from pathlib import Path

from src.logger import get_logger
from src.models import ContentItem, ScoredItem
from src.utils import NOTES_DIR, POSTS_DIR, RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR, DIGESTS_DIR, DATA_DIR, load_json, save_json, slugify

_logger = get_logger("web.data_service")


def _get_raw_path(d: date) -> Path:
    return RAW_DIR / f"{d.isoformat()}.json"


def _get_scored_path(d: date) -> Path:
    return SCORED_DIR / f"{d.isoformat()}.json"


def _has_posts(d: date) -> bool:
    prefix = d.isoformat()
    return any(f.name.startswith(prefix) for f in POSTS_DIR.glob("*.md"))


def get_pipeline_state(d: date) -> str:
    """回傳 pipeline 狀態：none / collected / scored / done。"""
    if _has_posts(d):
        return "done"
    if _get_scored_path(d).exists():
        return "scored"
    if _get_raw_path(d).exists():
        return "collected"
    return "none"


def get_week_status(days: int = 7, running_dates: set[str] | None = None) -> list[dict]:
    """取得最近 N 天的 pipeline 狀態摘要。"""
    today = date.today()
    result = []
    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        state = get_pipeline_state(d)
        if running_dates and d.isoformat() in running_dates:
            state = "running"

        raw_count = 0
        raw_path = _get_raw_path(d)
        if raw_path.exists():
            data = load_json(raw_path)
            raw_count = len(data) if isinstance(data, list) else 0

        scored_count = 0
        scored_path = _get_scored_path(d)
        if scored_path.exists():
            data = load_json(scored_path)
            scored_count = len(data) if isinstance(data, list) else 0

        prefix = d.isoformat()
        posts = list(POSTS_DIR.glob(f"{prefix}*.md"))
        notes = list(NOTES_DIR.glob(f"{prefix}*.md"))

        result.append(
            {
                "date": d.isoformat(),
                "state": state,
                "raw_count": raw_count,
                "scored_count": scored_count,
                "posts_count": len(posts),
                "notes_count": len(notes),
            }
        )
    return result


def get_week_top_items(days: int = 7, top_k: int = 5) -> list[dict]:
    """取得近 N 天中 total_score 最高的 top_k 個項目（跨日聚合）。"""
    today = date.today()
    all_items = []
    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        scored_path = _get_scored_path(d)
        if not scored_path.exists():
            continue
        data = load_json(scored_path)
        if not isinstance(data, list):
            continue
        for raw in data:
            try:
                item = ScoredItem(**raw)
                all_items.append(
                    {
                        "date": d.isoformat(),
                        "title": item.item.title,
                        "source_name": item.item.source_name,
                        "total_score": item.rule_score + (item.llm_score or 0),
                        "llm_reason": item.llm_reason,
                        "url": item.item.url,
                        "tags": item.item.tags,
                        "authors": item.item.authors,
                        "abstract": item.item.abstract,
                    }
                )
            except Exception:
                _logger.debug("Skipping malformed scored item in weekly top", extra={"date": d.isoformat()})
                continue

    all_items.sort(key=lambda x: x["total_score"], reverse=True)
    return all_items[:top_k]


def _serialize_scored_item(idx: int, si: ScoredItem) -> dict:
    """將 ScoredItem 投影為 dict，供 get_day_items / get_all_day_items 共用。"""
    total = si.rule_score + (si.llm_score or 0)
    return {
        "index": idx,
        "title": si.item.title,
        "url": si.item.url,
        "source": si.item.source.value,
        "source_name": si.item.source_name,
        "organization": si.item.organization,
        "rule_score": si.rule_score,
        "llm_score": si.llm_score,
        "total_score": total,
        "llm_reason": si.llm_reason,
        "novelty": si.novelty,
        "impact": si.impact,
        "trending": si.trending,
        "practicality": si.practicality,
        "blog_worthiness": si.blog_worthiness,
        "tags": si.item.tags,
        "authors": si.item.authors,
        "abstract": si.item.abstract,
    }


def get_day_items(d: date) -> list[dict]:
    """取得指定日期的所有 ScoredItem，按 total_score 降序。"""
    scored_path = _get_scored_path(d)
    if not scored_path.exists():
        return []
    data = load_json(scored_path)
    if not isinstance(data, list):
        return []

    items = []
    for idx, raw in enumerate(data):
        try:
            item = ScoredItem(**raw)
            items.append(_serialize_scored_item(idx, item))
        except Exception:
            _logger.debug("Skipping malformed scored item", extra={"date": d.isoformat(), "index": idx})
            continue

    items.sort(key=lambda x: x["total_score"], reverse=True)
    return items


def get_all_day_items(d: date) -> list[dict]:
    """取得指定日期所有收集文章（raw + scored 合併）。
    已評分文章顯示完整分數，未評分文章 scored=False。
    排序：已評分 by total_score desc，未評分附後（by title）。
    """
    raw_path = _get_raw_path(d)
    scored_path = _get_scored_path(d)

    # 建立 URL → scored info mapping（保留原始 index 給 bookmark/detail 用）
    scored_by_url: dict[str, dict] = {}
    if scored_path.exists():
        scored_data = load_json(scored_path)
        if isinstance(scored_data, list):
            for idx, raw_scored in enumerate(scored_data):
                try:
                    si = ScoredItem(**raw_scored)
                    scored_by_url[si.item.url] = _serialize_scored_item(idx, si)
                except Exception:
                    _logger.debug("Skipping malformed scored item", extra={"date": d.isoformat(), "index": idx})
                    continue

    # 若 raw 不存在，fallback 到 scored only（相容舊資料）
    if not raw_path.exists():
        return get_day_items(d)

    raw_data = load_json(raw_path)
    if not isinstance(raw_data, list):
        return get_day_items(d)

    items: list[dict] = []
    for raw_dict in raw_data:
        try:
            ci = ContentItem(**raw_dict)
            si = scored_by_url.get(ci.url, {})
            scored = bool(si)
            if scored:
                entry = {**si, "scored": True}
            else:
                entry = {
                    "index": None,
                    "title": ci.title,
                    "url": ci.url,
                    "source": ci.source.value,
                    "source_name": ci.source_name,
                    "organization": ci.organization,
                    "rule_score": None,
                    "llm_score": None,
                    "total_score": 0,
                    "llm_reason": None,
                    "novelty": None,
                    "impact": None,
                    "trending": None,
                    "practicality": None,
                    "blog_worthiness": None,
                    "tags": ci.tags,
                    "authors": ci.authors,
                    "abstract": ci.abstract,
                    "scored": False,
                }
            items.append(entry)
        except Exception:
            _logger.debug("Skipping malformed raw item", extra={"date": d.isoformat()})
            continue

    # 排序：已評分 by total_score desc，未評分 by title
    items.sort(key=lambda x: (not x["scored"], -x["total_score"]))
    return items


def get_day_raw_items(d: date) -> list[dict]:
    """取得指定日期所有原始收集的資料 (還未經過評分)"""
    raw_path = _get_raw_path(d)
    if not raw_path.exists():
        return []
    data = load_json(raw_path)
    if not isinstance(data, list):
        return []

    items = []
    for idx, raw in enumerate(data):
        try:
            it = ContentItem(**raw)
            items.append({
                "index": idx,
                "title": it.title,
                "url": it.url,
                "source": it.source.value,
                "source_name": it.source_name,
                "authors": it.authors,
                "published_date": it.published_date.isoformat(),
                "abstract": it.abstract,
                "tags": it.tags,
            })
        except Exception:
            continue
    return items


def get_day_stats(d: date) -> dict:
    """取得指定日期的統計摘要（含分數分佈與來源佔比）。"""
    raw_path = _get_raw_path(d)
    scored_path = _get_scored_path(d)

    raw_count = 0
    if raw_path.exists():
        data = load_json(raw_path)
        raw_count = len(data) if isinstance(data, list) else 0

    items = get_day_items(d)
    scored_count = len(items)

    prefix = d.isoformat()
    posts_count = len(list(POSTS_DIR.glob(f"{prefix}*.md")))
    notes_count = len(list(NOTES_DIR.glob(f"{prefix}*.md")))

    # 分數分佈（動態區間，根據實際資料範圍）
    source_counts: dict[str, int] = {}
    scores = []
    for it in items:
        scores.append(it["total_score"])
        src = it["source_name"] or it["source"]
        source_counts[src] = source_counts.get(src, 0) + 1

    if scores:
        lo = int(min(scores) // 10) * 10
        hi = int(max(scores) // 10 + 1) * 10
        # 確保至少 5 個區間，最多 8 個
        step = max(10, (hi - lo + 4) // 5 // 5 * 5) if hi - lo > 50 else 10
        bins = list(range(lo, hi + step, step))
        if len(bins) > 9:
            step = max(10, (hi - lo + 4) // 6 // 5 * 5 or 10)
            bins = list(range(lo, hi + step, step))
        score_dist_labels = [f"{bins[i]}-{bins[i+1]}" for i in range(len(bins) - 1)]
        score_dist = [0] * (len(bins) - 1)
        for s in scores:
            idx = min(int((s - lo) // step), len(score_dist) - 1)
            score_dist[idx] += 1
    else:
        score_dist_labels = []
        score_dist = []

    return {
        "date": d.isoformat(),
        "raw_count": raw_count,
        "scored_count": scored_count,
        "posts_count": posts_count,
        "notes_count": notes_count,
        "score_dist": score_dist,
        "score_dist_labels": score_dist_labels,
        "source_counts": source_counts,
    }


def get_item_detail(d: date, index: int) -> dict | None:
    """取得指定日期第 index 筆（原始順序）的詳細資料。"""
    scored_path = _get_scored_path(d)
    if not scored_path.exists():
        return None
    data = load_json(scored_path)
    if not isinstance(data, list) or index >= len(data):
        return None

    try:
        item = ScoredItem(**data[index])
    except Exception:
        return None

    return {
        "index": index,
        "date": d.isoformat(),
        "title": item.item.title,
        "url": item.item.url,
        "source": item.item.source.value,
        "source_name": item.item.source_name,
        "organization": item.item.organization,
        "authors": item.item.authors,
        "abstract": item.item.abstract,
        "published_date": item.item.published_date.isoformat(),
        "tags": item.item.tags,
        "rule_score": item.rule_score,
        "rule_reasons": item.rule_reasons,
        "llm_score": item.llm_score,
        "llm_reason": item.llm_reason,
        "novelty": item.novelty,
        "impact": item.impact,
        "trending": item.trending,
        "practicality": item.practicality,
        "blog_worthiness": item.blog_worthiness,
        "total_score": item.rule_score + (item.llm_score or 0),
    }


def _extract_content_meta(path: Path) -> dict:
    """從 markdown frontmatter + body 提取展示用 metadata。"""
    import re

    parsed = _parse_markdown_file(path)
    if not parsed:
        return {}
    fm = parsed["frontmatter"]
    body = parsed["body"]
    word_count = len(body.replace("\n", " ").split())
    reading_time_min = max(1, round(word_count / 200))
    clean = re.sub(r"[#*`>\[\]]+", "", body).strip()
    excerpt = clean[:120].rsplit(" ", 1)[0] + "…" if len(clean) > 120 else clean
    tags = fm.get("tags") or fm.get("標籤") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    score_raw = fm.get("score")
    try:
        fm_score = float(score_raw) if score_raw is not None else None
    except (TypeError, ValueError):
        fm_score = None
    source_fm = fm.get("source") or ""
    return {
        "title": fm.get("title") or fm.get("標題") or "",
        "tags": tags,
        "excerpt": excerpt,
        "word_count": word_count,
        "reading_time_min": reading_time_min,
        "fm_score": fm_score,
        "source_fm": source_fm,
    }


# Module-level scored cache（per process，不跨重啟）
_scored_cache: dict[str, dict[str, dict]] = {}


def _load_scored_for_date(date_str: str) -> dict[str, dict]:
    """讀取指定日期的 scored JSON，以 title 為 key（module-level cache）。"""
    if date_str in _scored_cache:
        return _scored_cache[date_str]
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        _scored_cache[date_str] = {}
        return {}
    path = _get_scored_path(d)
    if not path.exists():
        _scored_cache[date_str] = {}
        return {}
    data = load_json(path)
    result: dict[str, dict] = {}
    if isinstance(data, list):
        for raw in data:
            try:
                item = ScoredItem(**raw)
                result[item.item.title] = {
                    "novelty": item.novelty,
                    "impact": item.impact,
                    "trending": item.trending,
                    "practicality": item.practicality,
                    "blog_worthiness": item.blog_worthiness,
                    "rule_score": item.rule_score,
                    "llm_score": item.llm_score,
                    "source_name": item.item.source_name,
                    "llm_reason": item.llm_reason,
                }
            except Exception:
                continue
    _scored_cache[date_str] = result
    return result


_EMPTY_5D: dict = {
    "novelty": None,
    "impact": None,
    "trending": None,
    "practicality": None,
    "blog_worthiness": None,
    "rule_score": None,
    "llm_score": None,
    "llm_reason": None,
}


def _enrich_with_scored(item: dict) -> dict:
    """根據 date_str + title 跨查 scored JSON，填入 5D 分數等欄位。"""
    date_str = item.get("date_str", "")
    title = item.get("title", "")
    if not date_str or not title:
        return {**item, **_EMPTY_5D, "source_name": item.get("source_fm", "")}
    scored_map = _load_scored_for_date(date_str)
    scored = scored_map.get(title)
    if not scored:
        return {**item, **_EMPTY_5D, "source_name": item.get("source_fm", "")}
    return {**item, **scored}


def get_all_feedback() -> dict[str, str]:
    """回傳所有 feedback，格式：{date_str_slug: rating}。"""
    result: dict[str, str] = {}
    for path in FEEDBACK_DIR.glob("*.json"):
        date_str = path.stem
        data = load_json(path)
        if isinstance(data, dict):
            for slug, rating in data.items():
                result[f"{date_str}_{slug}"] = rating
    return result


_sidebar_cache: dict | None = None
_sidebar_cache_ts: float = 0.0
_SIDEBAR_TTL = 60  # 60 秒


def invalidate_scored_cache(date_str: str) -> None:
    """清除指定日期的 scored cache entry。Pipeline 完成後由 _finalize_run 呼叫。"""
    _scored_cache.pop(date_str, None)


def invalidate_sidebar_cache() -> None:
    """強制下次 sidebar stats 重新計算。"""
    global _sidebar_cache, _sidebar_cache_ts
    _sidebar_cache = None
    _sidebar_cache_ts = 0.0


def invalidate_search_index() -> None:
    """強制下次搜尋重建索引。"""
    global _search_built_at
    _search_built_at = 0


def get_sidebar_stats() -> dict:
    """取得 Sidebar 快速統計（只做 glob 計數，不讀取內容）。"""
    global _sidebar_cache, _sidebar_cache_ts
    if _sidebar_cache is not None and (_time.time() - _sidebar_cache_ts) < _SIDEBAR_TTL:
        return _sidebar_cache

    today_str = date.today().isoformat()
    total_posts = len(list(POSTS_DIR.glob("*.md")))
    total_notes = len(list(NOTES_DIR.glob("*.md")))
    today_posts = len(list(POSTS_DIR.glob(f"{today_str}*.md")))
    today_notes = len(list(NOTES_DIR.glob(f"{today_str}*.md")))

    # 素材總數 = scored JSON 中的 item 數
    total_materials = 0
    for f in SCORED_DIR.glob("*.json"):
        data = load_json(f)
        if isinstance(data, list):
            total_materials += len(data)

    # 書籤數
    bookmarks_count = 0
    bookmarks_path = DATA_DIR / "bookmarks.json"
    if bookmarks_path.exists():
        bm_data = load_json(bookmarks_path)
        if isinstance(bm_data, dict):
            bookmarks_count = sum(
                1 for v in bm_data.values()
                if v.get("status") not in ("written", "published")
            )

    result = {
        "total_posts": total_posts,
        "total_notes": total_notes,
        "today_posts": today_posts,
        "today_notes": today_notes,
        "total_materials": total_materials,
        "bookmarks_count": bookmarks_count,
    }
    _sidebar_cache = result
    _sidebar_cache_ts = _time.time()
    return result


def _parse_markdown_file(path: Path) -> dict | None:
    """解析帶 YAML frontmatter 的 markdown 檔案。"""
    import yaml

    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return None

    # 解析 frontmatter
    frontmatter: dict = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
            except Exception:
                frontmatter = {}
            body = parts[2].strip()

    return {"frontmatter": frontmatter, "body": body, "filename": path.name}


def get_post(date_str: str, slug: str) -> dict | None:
    """取得指定部落格文。"""
    filename = f"{date_str}_{slug}.md"
    path = POSTS_DIR / filename
    if not path.exists():
        # 嘗試模糊比對
        matches = list(POSTS_DIR.glob(f"{date_str}*{slug}*.md"))
        if not matches:
            return None
        path = matches[0]
    return _parse_markdown_file(path)


def get_note(date_str: str, slug: str) -> dict | None:
    """取得指定 AI 筆記。"""
    filename = f"{date_str}_{slug}.md"
    path = NOTES_DIR / filename
    if not path.exists():
        matches = list(NOTES_DIR.glob(f"{date_str}*{slug}*.md"))
        if not matches:
            return None
        path = matches[0]
    return _parse_markdown_file(path)


def list_posts(date_str: str) -> list[dict]:
    """列出指定日期的所有 posts。"""
    result = []
    feedback_map = get_all_feedback()
    for f in sorted(POSTS_DIR.glob(f"{date_str}*.md")):
        slug = f.stem[len(date_str) + 1 :] if f.stem.startswith(date_str) else f.stem
        meta = _extract_content_meta(f)
        item = {"slug": slug, "filename": f.name, "date_str": date_str, **meta}
        item = _enrich_with_scored(item)
        item["feedback"] = feedback_map.get(f"{date_str}_{slug}")
        result.append(item)
    return result


def list_notes(date_str: str) -> list[dict]:
    """列出指定日期的所有 notes。"""
    result = []
    feedback_map = get_all_feedback()
    for f in sorted(NOTES_DIR.glob(f"{date_str}*.md")):
        slug = f.stem[len(date_str) + 1 :] if f.stem.startswith(date_str) else f.stem
        meta = _extract_content_meta(f)
        item = {"slug": slug, "filename": f.name, "date_str": date_str, **meta}
        item = _enrich_with_scored(item)
        item["feedback"] = feedback_map.get(f"{date_str}_{slug}")
        result.append(item)
    return result


def list_day_contents(date_str: str) -> list[dict]:
    """合併指定日期的 posts + notes，同標題合併為一筆，按 total_score 降序。"""
    posts = list_posts(date_str)
    notes = list_notes(date_str)

    # 以 title 為 key 合併
    merged: dict[str, dict] = {}
    for p in posts:
        title = p.get("title") or p.get("slug", "")
        key = title.strip().lower()
        merged[key] = {
            **p,
            "has_post": True,
            "has_note": False,
            "post_slug": p.get("slug"),
            "note_slug": None,
        }

    for n in notes:
        title = n.get("title") or n.get("slug", "")
        key = title.strip().lower()
        if key in merged:
            merged[key]["has_note"] = True
            merged[key]["note_slug"] = n.get("slug")
        else:
            merged[key] = {
                **n,
                "has_post": False,
                "has_note": True,
                "post_slug": None,
                "note_slug": n.get("slug"),
            }

    result = list(merged.values())
    # 用 rule_score + llm_score 排序（取自 _enrich_with_scored 填入的欄位）
    result.sort(
        key=lambda x: (x.get("rule_score") or 0) + (x.get("llm_score") or 0),
        reverse=True,
    )
    return result


def list_all_posts() -> list[dict]:
    """列出所有日期的 posts，依日期由新到舊排序。"""
    result = []
    feedback_map = get_all_feedback()
    for f in POSTS_DIR.glob("*.md"):
        parts = f.stem.split("_", 1)
        if len(parts) >= 1:
            date_str = parts[0]
            if len(date_str) == 10 and date_str.count("-") == 2:
                slug = parts[1] if len(parts) > 1 else f.stem
                meta = _extract_content_meta(f)
                item = {"date_str": date_str, "slug": slug, "filename": f.name, **meta}
                item = _enrich_with_scored(item)
                item["feedback"] = feedback_map.get(f"{date_str}_{slug}")
                result.append(item)
    return sorted(result, key=lambda x: (x["date_str"], x["slug"]), reverse=True)


def list_all_notes() -> list[dict]:
    """列出所有日期的 notes，依日期由新到舊排序。"""
    result = []
    feedback_map = get_all_feedback()
    for f in NOTES_DIR.glob("*.md"):
        parts = f.stem.split("_", 1)
        if len(parts) >= 1:
            date_str = parts[0]
            if len(date_str) == 10 and date_str.count("-") == 2:
                slug = parts[1] if len(parts) > 1 else f.stem
                meta = _extract_content_meta(f)
                item = {"date_str": date_str, "slug": slug, "filename": f.name, **meta}
                item = _enrich_with_scored(item)
                item["feedback"] = feedback_map.get(f"{date_str}_{slug}")
                result.append(item)
    return sorted(result, key=lambda x: (x["date_str"], x["slug"]), reverse=True)
def list_all_materials(days: int = 90) -> list[dict]:
    """掃描所有 scored JSON，對每個 item 檢查是否有對應的 post/note 檔案。

    回傳含 has_post、has_note、post_slug、note_slug 的統一素材列表。
    """
    today = date.today()
    result: list[dict] = []

    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        scored_path = _get_scored_path(d)
        if not scored_path.exists():
            continue
        data = load_json(scored_path)
        if not isinstance(data, list):
            continue

        date_str = d.isoformat()
        # 預先載入該日期的 post/note slug 集合
        post_slugs = {f.stem[len(date_str) + 1:] for f in POSTS_DIR.glob(f"{date_str}*.md")}
        note_slugs = {f.stem[len(date_str) + 1:] for f in NOTES_DIR.glob(f"{date_str}*.md")}

        for idx, raw in enumerate(data):
            try:
                item = ScoredItem(**raw)
            except Exception:
                continue

            title_slug = slugify(item.item.title)
            # 嘗試匹配 slug（post/note 的 slug 可能是 title 的 slugified 版本）
            has_post = any(title_slug in s or s in title_slug for s in post_slugs) if post_slugs else False
            has_note = any(title_slug in s or s in title_slug for s in note_slugs) if note_slugs else False
            matched_post_slug = next((s for s in post_slugs if title_slug in s or s in title_slug), None)
            matched_note_slug = next((s for s in note_slugs if title_slug in s or s in title_slug), None)

            total = item.rule_score + (item.llm_score or 0)
            result.append({
                "date_str": date_str,
                "index": idx,
                "title": item.item.title,
                "url": item.item.url,
                "source": item.item.source.value,
                "source_name": item.item.source_name,
                "organization": item.item.organization,
                "authors": item.item.authors,
                "abstract": item.item.abstract,
                "tags": item.item.tags,
                "rule_score": item.rule_score,
                "llm_score": item.llm_score,
                "total_score": total,
                "novelty": item.novelty,
                "impact": item.impact,
                "trending": item.trending,
                "practicality": item.practicality,
                "blog_worthiness": item.blog_worthiness,
                "llm_reason": item.llm_reason,
                "has_post": has_post,
                "has_note": has_note,
                "post_slug": matched_post_slug,
                "note_slug": matched_note_slug,
            })

    result.sort(key=lambda x: (x["date_str"], x["total_score"]), reverse=True)
    return result


def get_material_detail(date_str: str, index: int) -> dict | None:
    """回傳完整 scored item + 解析過的 post/note 內容（若存在）。"""
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        return None

    detail = get_item_detail(d, index)
    if detail is None:
        return None

    title_slug = slugify(detail["title"])

    # 尋找對應的 post
    post_content = None
    post_slug = None
    for f in POSTS_DIR.glob(f"{date_str}*.md"):
        slug = f.stem[len(date_str) + 1:]
        if title_slug in slug or slug in title_slug:
            parsed = _parse_markdown_file(f)
            if parsed:
                from markdown_it import MarkdownIt
                md = MarkdownIt()
                post_content = md.render(parsed["body"])
                post_slug = slug
            break

    # 尋找對應的 note
    note_content = None
    note_slug = None
    for f in NOTES_DIR.glob(f"{date_str}*.md"):
        slug = f.stem[len(date_str) + 1:]
        if title_slug in slug or slug in title_slug:
            parsed = _parse_markdown_file(f)
            if parsed:
                from markdown_it import MarkdownIt
                md = MarkdownIt()
                note_content = md.render(parsed["body"])
                note_slug = slug
            break

    detail["post_content"] = post_content
    detail["note_content"] = note_content
    detail["post_slug"] = post_slug
    detail["note_slug"] = note_slug
    detail["has_post"] = post_content is not None
    detail["has_note"] = note_content is not None

    return detail


def save_feedback(date_str: str, slug: str, rating: str) -> None:
    path = FEEDBACK_DIR / f"{date_str}.json"
    data = load_json(path)
    if not isinstance(data, dict):
        data = {}
    data[slug] = rating
    save_json(data, path)


def get_feedback(date_str: str, slug: str) -> str | None:
    path = FEEDBACK_DIR / f"{date_str}.json"
    if not path.exists():
        return None
    data = load_json(path)
    if not isinstance(data, dict):
        return None
    return data.get(slug)


def get_digest(date_str: str) -> dict | None:
    """取得指定日期的摘要。"""
    path = DIGESTS_DIR / f"{date_str}.md"
    if not path.exists():
        return None
    return _parse_markdown_file(path)


def list_recent_digests(days: int = 30) -> list[dict]:
    """列出最近 N 天的摘要。"""
    today = date.today()
    result: list[dict] = []
    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        path = DIGESTS_DIR / f"{d.isoformat()}.md"
        if path.exists():
            parsed = _parse_markdown_file(path)
            if parsed:
                fm = parsed["frontmatter"]
                result.append({
                    "date_str": d.isoformat(),
                    "total_items": fm.get("total_items", 0),
                    "avg_score": fm.get("avg_score", 0),
                })
    return sorted(result, key=lambda x: x["date_str"], reverse=True)


def get_dashboard_charts(days: int = 30) -> dict:
    """取得 Dashboard 所需的統計資料：分數趨勢、來源佔比、Collector 健康度"""
    today = date.today()
    
    trend_labels = []
    trend_scores = []
    source_counts = {}
    health_summary = {}

    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        
        # 1. Score Trend & Source Counts
        scored_path = _get_scored_path(d)
        if scored_path.exists():
            data = load_json(scored_path)
            if isinstance(data, list) and len(data) > 0:
                daily_total = 0
                for raw in data:
                    try:
                        item = ScoredItem(**raw)
                        total = item.rule_score + (item.llm_score or 0)
                        daily_total += total
                        src = item.item.source_name or item.item.source.value
                        source_counts[src] = source_counts.get(src, 0) + 1
                    except Exception:
                        pass
                avg_score = daily_total / len(data)
                trend_labels.append(d.isoformat()[5:])
                trend_scores.append(round(avg_score, 1))
        
        # 2. Collector Health (aggregate past 7 days)
        if i < 7:
            health_path = HEALTH_DIR / f"{d.isoformat()}.json"
            if health_path.exists():
                h_data = load_json(health_path)
                if isinstance(h_data, dict):
                    for collector, stats in h_data.items():
                        if collector not in health_summary:
                            health_summary[collector] = {"success": 0, "error": 0, "total_duration": 0.0, "runs": 0}
                        if stats.get("status") == "success":
                            health_summary[collector]["success"] += 1
                        else:
                            health_summary[collector]["error"] += 1
                        health_summary[collector]["total_duration"] += stats.get("duration", 0)
                        health_summary[collector]["runs"] += 1

    health_panel = []
    for collector, st in health_summary.items():
        avg_time = round(st["total_duration"] / st["runs"], 1) if st["runs"] > 0 else 0
        health_panel.append({
            "name": collector,
            "success": st["success"],
            "error": st["error"],
            "avg_time": avg_time
        })
        
    return {
        "trend_labels": trend_labels,
        "trend_scores": trend_scores,
        "source_labels": list(source_counts.keys()),
        "source_data": list(source_counts.values()),
        "health_panel": health_panel
    }


# ──────────────────────────────────────────────────────────
# Search Engine（記憶體內倒排索引）
# ──────────────────────────────────────────────────────────

_search_index: list[dict] = []
_search_built_at: float = 0
_SEARCH_TTL = 300  # 5 分鐘


def _tokenize(text: str) -> list[str]:
    """簡易分詞：英文 lowercase + 中文字元拆分。"""
    text = text.lower()
    tokens = re.findall(r"[a-z0-9]+|[\u4e00-\u9fff]", text)
    return tokens


def build_search_index() -> None:
    """掃描所有 scored JSON 建立搜尋索引。"""
    global _search_index, _search_built_at
    items: list[dict] = []
    for f in sorted(SCORED_DIR.glob("*.json")):
        date_str = f.stem
        data = load_json(f)
        if not isinstance(data, list):
            continue
        for idx, raw in enumerate(data):
            try:
                item = ScoredItem(**raw)
            except Exception:
                continue
            total = item.rule_score + (item.llm_score or 0)
            searchable = " ".join([
                item.item.title,
                item.item.abstract or "",
                " ".join(item.item.tags or []),
                item.item.source_name or "",
                item.item.organization or "",
                " ".join(item.item.authors or []),
            ])
            items.append({
                "date_str": date_str,
                "index": idx,
                "title": item.item.title,
                "url": item.item.url,
                "source": item.item.source.value,
                "source_name": item.item.source_name,
                "total_score": total,
                "tags": item.item.tags,
                "abstract": item.item.abstract,
                "organization": item.item.organization,
                "_tokens": set(_tokenize(searchable)),
            })
    _search_index = items
    _search_built_at = _time.time()


def search_items(
    q: str = "",
    source: str = "",
    min_score: float = 0,
    max_score: float = 999,
    date_from: str = "",
    date_to: str = "",
    page: int = 1,
    limit: int = 20,
) -> dict:
    """查詢素材。回傳 {items, total, page, pages}。"""
    global _search_index, _search_built_at
    if not _search_index or (_time.time() - _search_built_at > _SEARCH_TTL):
        build_search_index()

    results = _search_index

    # 文字搜尋
    if q.strip():
        query_tokens = set(_tokenize(q))
        results = [
            it for it in results
            if query_tokens.issubset(it["_tokens"])
        ]

    # 來源篩選
    if source:
        source_lower = source.lower()
        results = [it for it in results if source_lower in (it.get("source_name") or "").lower()]

    # 分數篩選
    results = [it for it in results if min_score <= it["total_score"] <= max_score]

    # 日期篩選
    if date_from:
        results = [it for it in results if it["date_str"] >= date_from]
    if date_to:
        results = [it for it in results if it["date_str"] <= date_to]

    # 排序
    results.sort(key=lambda x: x["total_score"], reverse=True)

    total = len(results)
    pages = max(1, (total + limit - 1) // limit)
    start = (page - 1) * limit
    page_items = results[start:start + limit]

    # 移除 _tokens（不序列化）
    clean = [{k: v for k, v in it.items() if k != "_tokens"} for it in page_items]

    return {"items": clean, "total": total, "page": page, "pages": pages}


# ──────────────────────────────────────────────────────────
# Bookmark / 書籤系統
# ──────────────────────────────────────────────────────────

_BOOKMARKS_PATH = DATA_DIR / "bookmarks.json"


def _load_bookmarks() -> dict:
    if _BOOKMARKS_PATH.exists():
        data = load_json(_BOOKMARKS_PATH)
        return data if isinstance(data, dict) else {}
    return {}


def _save_bookmarks(data: dict) -> None:
    save_json(data, _BOOKMARKS_PATH)


def get_all_bookmarks() -> dict:
    return _load_bookmarks()


def get_bookmarked_indices(date_str: str) -> set[int]:
    """回傳指定日期所有已收藏的 index 集合。"""
    bm = _load_bookmarks()
    result: set[int] = set()
    prefix = f"{date_str}_"
    for key in bm:
        if key.startswith(prefix):
            try:
                result.add(int(key[len(prefix):]))
            except ValueError:
                continue
    return result


def set_bookmark(date_str: str, index: int, title: str = "", notes: str = "") -> None:
    """收藏一筆素材。"""
    from datetime import datetime
    bm = _load_bookmarks()
    key = f"{date_str}_{index}"
    bm[key] = {
        "status": "bookmarked",
        "starred_at": datetime.now().isoformat(),
        "notes": notes,
        "title": title,
        "date_str": date_str,
        "index": index,
    }
    _save_bookmarks(bm)


def remove_bookmark(date_str: str, index: int) -> None:
    bm = _load_bookmarks()
    key = f"{date_str}_{index}"
    bm.pop(key, None)
    _save_bookmarks(bm)


def update_bookmark_status(date_str: str, index: int, status: str) -> None:
    bm = _load_bookmarks()
    key = f"{date_str}_{index}"
    if key in bm:
        bm[key]["status"] = status
        _save_bookmarks(bm)


def is_bookmarked(date_str: str, index: int) -> bool:
    bm = _load_bookmarks()
    return f"{date_str}_{index}" in bm


def list_bookmarked_items(status: str = "") -> list[dict]:
    """列出書籤項目，可依狀態篩選。"""
    bm = _load_bookmarks()
    result: list[dict] = []
    for key, val in bm.items():
        if status and val.get("status") != status:
            continue
        # 嘗試載入完整 item 資訊
        d_str = val.get("date_str", "")
        idx = val.get("index", 0)
        try:
            d = date.fromisoformat(d_str)
            detail = get_item_detail(d, idx)
        except Exception:
            detail = None

        entry = {**val, "key": key}
        if detail:
            entry["title"] = detail["title"]
            entry["source_name"] = detail.get("source_name", "")
            entry["total_score"] = detail.get("total_score", 0)
            entry["tags"] = detail.get("tags", [])
            entry["url"] = detail.get("url", "")
        result.append(entry)

    return sorted(
        result,
        key=lambda x: (x.get("date_str", ""), x.get("total_score", 0)),
        reverse=True,
    )


# ──────────────────────────────────────────────────────────
# Topic Clustering（主題聚合）
# ──────────────────────────────────────────────────────────

def cluster_topics(days: int = 30) -> dict:
    """依 config 中的 topic_clusters 進行 keyword word-boundary 匹配。

    回傳:
        topics: {topic_name: [items...]}
        timeline: {topic_name: {date_str: count}}
    """
    from src.utils import load_config

    config = load_config()
    clusters = config.get("topic_clusters", {})
    if not clusters:
        return {"topics": {}, "timeline": {}}

    # 編譯 regex
    compiled: dict[str, list[re.Pattern]] = {}
    for topic, keywords in clusters.items():
        compiled[topic] = [
            re.compile(r"(?i)\b" + re.escape(kw) + r"\b" if all(c.isascii() for c in kw)
                       else re.escape(kw), re.IGNORECASE)
            for kw in keywords
        ]

    today = date.today()
    topics: dict[str, list[dict]] = {t: [] for t in clusters}
    timeline: dict[str, dict[str, int]] = {t: {} for t in clusters}

    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        scored_path = _get_scored_path(d)
        if not scored_path.exists():
            continue
        data = load_json(scored_path)
        if not isinstance(data, list):
            continue
        date_str = d.isoformat()

        for idx, raw in enumerate(data):
            try:
                item = ScoredItem(**raw)
            except Exception:
                continue
            searchable = " ".join([
                item.item.title,
                item.item.abstract or "",
                " ".join(item.item.tags or []),
            ])
            total = item.rule_score + (item.llm_score or 0)

            for topic, patterns in compiled.items():
                if any(p.search(searchable) for p in patterns):
                    topics[topic].append({
                        "date_str": date_str,
                        "index": idx,
                        "title": item.item.title,
                        "source_name": item.item.source_name,
                        "total_score": total,
                        "url": item.item.url,
                        "tags": item.item.tags,
                    })
                    timeline[topic][date_str] = timeline[topic].get(date_str, 0) + 1

    # 按 total_score 降序
    for topic in topics:
        topics[topic].sort(key=lambda x: x["total_score"], reverse=True)

    return {"topics": topics, "timeline": timeline}
