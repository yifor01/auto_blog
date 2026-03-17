"""FastAPI 監控網頁應用程式。"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any, Optional

import asyncio
import threading
import time as _time

from fastapi import BackgroundTasks, FastAPI, Form, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from src.logger import get_logger
from src.utils import NOTES_DIR, POSTS_DIR, PROMPTS_DIR, RAW_DIR, SCORED_DIR, load_json
from src.web import data_service as ds
from src.web import config_manager as cm

_logger = get_logger("web.app")

app = FastAPI(title="Auto Post Blog Monitor", docs_url=None, redoc_url=None)


@app.on_event("startup")
async def startup_event():
    cm.init_config()
    # 自動觸發當天 pipeline（背景執行）
    today = date.today().isoformat()
    with _lock:
        existing = _runs.get(today)
        if existing and existing.status == "running":
            return  # 已在執行中，跳過
        _runs[today] = PipelineRun(status="running", log_offset=0)
    threading.Thread(target=_run_pipeline, args=(today, False), daemon=True).start()
    _logger.info("Auto-triggered pipeline on startup", extra={"date": today})


@dataclass
class StageInfo:
    status: str = "pending"     # pending | running | done | failed | cancelled
    elapsed: float | None = None
    item_count: int | None = None


@dataclass
class PipelineRun:
    status: str = "running"     # running | done | failed | cancelled
    proc: subprocess.Popen | None = None
    log_offset: int = 0
    stages: dict[str, StageInfo] = field(default_factory=lambda: {
        "collect": StageInfo(),
        "score": StageInfo(),
        "generate": StageInfo(),
    })


_lock = threading.Lock()
_runs: dict[str, PipelineRun] = {}


def _is_running(date_str: str) -> bool:
    with _lock:
        run = _runs.get(date_str)
        return run is not None and run.status == "running"


def _get_running_dates() -> set[str]:
    with _lock:
        return {d for d, r in _runs.items() if r.status == "running"}


def _finalize_run(run: PipelineRun, log_path: Path, date_str: str, final_status: str) -> None:
    """proc.wait() 後呼叫一次——解析 log、invalidate caches、設定最終狀態。"""
    # ① 解析 log 填充 stage 狀態（只讀本次 run 的 log）
    try:
        content = log_path.read_text(encoding="utf-8", errors="replace")
        for line in content[run.log_offset:].splitlines():
            try:
                parsed = json.loads(line)
                if "pipeline_stage" in parsed:
                    name = parsed["pipeline_stage"]
                    action = parsed["stage_action"]
                    if name in run.stages:
                        if action == "start":
                            run.stages[name].status = "running"
                        elif action == "end":
                            run.stages[name].status = "done"
                            run.stages[name].elapsed = parsed.get("elapsed")
                            run.stages[name].item_count = parsed.get("item_count")
            except (json.JSONDecodeError, KeyError):
                pass
    except OSError:
        pass
    # ② Invalidate caches（在設 status 之前！確保 reload 時 cache 已清空）
    ds.invalidate_scored_cache(date_str)
    ds.invalidate_sidebar_cache()
    ds.invalidate_search_index()
    # ③ 設定最終狀態
    with _lock:
        run.status = final_status
        if final_status in ("cancelled", "failed"):
            for s in run.stages.values():
                if s.status == "running":
                    s.status = final_status
        # ④ 若 pipeline 成功但所有 stage 仍 pending → checkpoint 跳過，全部標記 done
        if final_status == "done":
            all_pending = all(s.status == "pending" for s in run.stages.values())
            if all_pending:
                for s in run.stages.values():
                    s.status = "done"
        run.proc = None

# B5: 改用 pathlib 建構路徑，避免 str.replace 脆弱性
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

# B6: log 存放目錄
LOGS_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

VALID_STAGES = {"collect", "score", "generate"}


def _fmt_log_msg(parsed: dict[str, Any]) -> str:
    """將 JSON log entry 轉為人類可讀字串，包含 source 名稱與計數。"""
    msg = parsed.get("msg", "")
    # 前綴：source 名稱（blog/feed/category/language/repo 取第一個）
    for key in ("blog", "feed", "category", "language", "repo"):
        val = parsed.get(key)
        if val:
            msg = f"[{val}] {msg}"
            break
    # 後綴：計數
    count = parsed.get("count") if parsed.get("count") is not None else parsed.get("total_count")
    if count is not None:
        msg = f"{msg} ({count} 筆)"
    # 後綴：錯誤訊息（截斷至 100 字元）
    err = parsed.get("error")
    if err:
        err_str = str(err)
        err_short = err_str[:100] + ("..." if len(err_str) > 100 else "")
        msg = f"{msg}: {err_short}"
    return msg


@app.get("/", response_class=RedirectResponse)
async def index():
    return RedirectResponse(url="/dashboard")


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    week_status = ds.get_week_status(7, running_dates=_get_running_dates())
    top_items = ds.get_week_top_items(7, top_k=10)
    charts = ds.get_dashboard_charts(30)
    recent_blogs = ds.list_all_blogs()[:5]
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "week_status": week_status,
            "top_items": top_items,
            "today": date.today().isoformat(),
            "today_str": date.today().isoformat(),
            "charts": charts,
            "recent_blogs": recent_blogs,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/day/{date_str}", response_class=HTMLResponse)
async def day_detail(request: Request, date_str: str):
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤，請使用 YYYY-MM-DD")

    stats = ds.get_day_stats(d)
    items = ds.get_all_day_items(d)
    contents = ds.list_day_contents(date_str)

    # Build title → content mapping for inline badges in scored items table
    content_map = {}
    for c in contents:
        key = (c.get("title") or "").strip().lower()
        if key:
            content_map[key] = {
                "has_post": c.get("has_post", False),
                "has_note": c.get("has_note", False),
                "has_blog": c.get("has_blog", False),
                "post_slug": c.get("post_slug"),
                "note_slug": c.get("note_slug"),
                "blog_slug": c.get("blog_slug"),
            }

    state = ds.get_pipeline_state(d)
    if _is_running(date_str):
        state = "running"

    bookmarked_indices = ds.get_bookmarked_indices(date_str)

    return templates.TemplateResponse(
        "day_detail.html",
        {
            "request": request,
            "date_str": date_str,
            "stats": stats,
            "items": items,
            "content_map": content_map,
            "state": state,
            "bookmarked_indices": bookmarked_indices,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/raw/{date_str}", response_class=HTMLResponse)
async def raw_detail(request: Request, date_str: str):
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤，請使用 YYYY-MM-DD")

    items = ds.get_day_raw_items(d)

    return templates.TemplateResponse(
        "raw_detail.html",
        {
            "request": request,
            "date_str": date_str,
            "items": items,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/item/{date_str}/{index}", response_class=HTMLResponse)
async def item_detail(request: Request, date_str: str, index: int):
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    detail = ds.get_material_detail(date_str, index)
    if detail is None:
        raise HTTPException(status_code=404, detail="找不到該項目")

    return templates.TemplateResponse(
        "material_detail.html",
        {
            "request": request,
            "date_str": date_str,
            "item": detail,
            "back_url": f"/day/{date_str}",
            "back_label": date_str,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/post/{date_str}/{slug}", response_class=HTMLResponse)
async def post_view(request: Request, date_str: str, slug: str):
    post = ds.get_post(date_str, slug)
    if post is None:
        raise HTTPException(status_code=404, detail="找不到該部落格文")

    from markdown_it import MarkdownIt

    md = MarkdownIt()
    content_html = md.render(post["body"])
    feedback = ds.get_feedback(date_str, slug)

    return templates.TemplateResponse(
        "post_view.html",
        {
            "request": request,
            "date_str": date_str,
            "slug": slug,
            "frontmatter": post["frontmatter"],
            "content_html": content_html,
            "content_type": "部落格文",
            "feedback": feedback,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/note/{date_str}/{slug}", response_class=HTMLResponse)
async def note_view(request: Request, date_str: str, slug: str):
    note = ds.get_note(date_str, slug)
    if note is None:
        raise HTTPException(status_code=404, detail="找不到該 AI 筆記")

    from markdown_it import MarkdownIt

    md = MarkdownIt()
    content_html = md.render(note["body"])
    feedback = ds.get_feedback(date_str, slug)

    return templates.TemplateResponse(
        "post_view.html",
        {
            "request": request,
            "date_str": date_str,
            "slug": slug,
            "frontmatter": note["frontmatter"],
            "content_html": content_html,
            "content_type": "AI 筆記",
            "feedback": feedback,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/materials", response_class=HTMLResponse)
async def material_library(request: Request):
    materials = ds.list_all_materials()
    # 已收藏的 key 集合（用於 card 上顯示星號）
    bm = ds.get_all_bookmarks()
    bookmarked_keys = set(bm.keys())
    return templates.TemplateResponse(
        "material_library.html",
        {
            "request": request,
            "materials": materials,
            "bookmarked_keys": bookmarked_keys,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/material/{date_str}/{index}", response_class=HTMLResponse)
async def material_detail(request: Request, date_str: str, index: int):
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    detail = ds.get_material_detail(date_str, index)
    if detail is None:
        raise HTTPException(status_code=404, detail="找不到該素材")

    # Context-aware breadcrumb
    from_param = request.query_params.get("from", "")
    if from_param == "queue":
        back_url = "/queue"
        back_label = "待寫清單"
    elif from_param == "day":
        back_url = f"/day/{date_str}"
        back_label = date_str
    else:
        back_url = "/materials"
        back_label = "素材庫"

    return templates.TemplateResponse(
        "material_detail.html",
        {
            "request": request,
            "date_str": date_str,
            "item": detail,
            "back_url": back_url,
            "back_label": back_label,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/posts", response_class=RedirectResponse)
async def posts_redirect():
    return RedirectResponse(url="/materials", status_code=301)


@app.get("/notes", response_class=RedirectResponse)
async def notes_redirect():
    return RedirectResponse(url="/materials", status_code=301)


@app.get("/topics", response_class=HTMLResponse)
async def topics_view(request: Request, days: int = 30):
    result = ds.cluster_topics(days)
    topics = result["topics"]
    timeline = result["timeline"]

    # 產生最近 14 天日期列表給 sparkline
    from datetime import timedelta
    today = date.today()
    spark_dates = [(today - timedelta(days=i)).isoformat() for i in range(13, -1, -1)]

    return templates.TemplateResponse(
        "topics.html",
        {
            "request": request,
            "topics": topics,
            "timeline": timeline,
            "days": days,
            "spark_dates": spark_dates,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/digest", response_class=HTMLResponse)
async def digest_list(request: Request):
    digests = ds.list_recent_digests(90)
    return templates.TemplateResponse(
        "digest.html",
        {
            "request": request,
            "digests": digests,
            "digest": None,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/digest/{date_str}", response_class=HTMLResponse)
async def digest_view(request: Request, date_str: str):
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    digest = ds.get_digest(date_str)
    if digest is None:
        raise HTTPException(status_code=404, detail="找不到該日期的摘要")

    from markdown_it import MarkdownIt
    md = MarkdownIt()
    digest_html = md.render(digest["body"])

    return templates.TemplateResponse(
        "digest.html",
        {
            "request": request,
            "date_str": date_str,
            "digest": digest,
            "digest_html": digest_html,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/blogs", response_class=HTMLResponse)
async def blogs_list(request: Request):
    blogs = ds.list_all_blogs()
    return templates.TemplateResponse(
        "blogs.html",
        {"request": request, "blogs": blogs,
         "sidebar_stats": ds.get_sidebar_stats()},
    )


@app.get("/blog/{date_str}/{slug}", response_class=HTMLResponse)
async def blog_view(request: Request, date_str: str, slug: str):
    blog = ds.get_blog(date_str, slug)
    if blog is None:
        raise HTTPException(status_code=404, detail="找不到該 Blog 文章")
    from markdown_it import MarkdownIt
    md = MarkdownIt()
    content_html = md.render(blog["body"])
    content_fb = blog.get("body_fb", "")

    # 比對 scored JSON 找對應 material index
    material_index = None
    fm = blog["frontmatter"]
    paper_title = (fm.get("paper_title") or fm.get("title") or "").strip()
    if paper_title:
        from src.utils import slugify as _slugify
        target_slug = _slugify(paper_title)
        try:
            d = date.fromisoformat(date_str)
            items = ds.get_day_items(d)
            for item in items:
                item_slug = _slugify(item.get("title", ""))
                if item_slug and (target_slug in item_slug or item_slug in target_slug):
                    material_index = item["index"]
                    break
        except Exception:
            pass

    return templates.TemplateResponse(
        "blog_view.html",
        {"request": request, "date_str": date_str, "slug": slug,
         "frontmatter": blog["frontmatter"], "content_html": content_html,
         "content_fb": content_fb,
         "material_index": material_index,
         "sidebar_stats": ds.get_sidebar_stats()},
    )


@app.get("/docs", response_class=HTMLResponse)
async def docs_page(request: Request):
    """專案文件瀏覽頁面。"""
    from markdown_it import MarkdownIt

    md = MarkdownIt().enable("table")
    project_root = Path(__file__).resolve().parent.parent.parent

    doc_files = [
        ("README.md", project_root / "README.md"),
        ("CLAUDE.md", project_root / "CLAUDE.md"),
        ("TODO.md", project_root / "TODO.md"),
        ("review.md", project_root / "review.md"),
    ]
    docs = []
    for name, path in doc_files:
        if path.exists():
            raw = path.read_text(encoding="utf-8", errors="replace")
            docs.append({"name": name, "html": md.render(raw)})
        else:
            docs.append({"name": name, "html": f"<p style='color:var(--t4)'>{name} 不存在</p>"})

    return templates.TemplateResponse(
        "docs.html",
        {
            "request": request,
            "docs": docs,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/settings", response_class=HTMLResponse)
async def settings_page(request: Request, saved: str = ""):
    cfg = cm.get_config()
    env = cm.get_env_values()
    return templates.TemplateResponse(
        "settings.html",
        {
            "request": request,
            "cfg": cfg,
            "env": env,
            "saved": saved == "1",
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.post("/settings")
async def settings_save(
    request: Request,
    api_key: str = Form(""),
    api_url: str = Form(""),
    llm_model: str = Form(""),
    fallback_model: str = Form(""),
    max_tokens: int = Form(8192, ge=256, le=131072),
    request_delay: float = Form(0.5, ge=0.0, le=60.0),
    rule_threshold: int = Form(25, ge=0, le=500),
    llm_top_k: int = Form(30, ge=1, le=1000),
    final_top_k: int = Form(10, ge=1, le=500),
    hf_upvote_threshold: int = Form(10, ge=0, le=100000),
    github_stars_high: int = Form(100, ge=1, le=100000),
    github_stars_medium: int = Form(50, ge=1, le=100000),
    dedup_lookback: int = Form(7, ge=0, le=365),
    retention_days: int = Form(90, ge=7, le=3650),
    # Collector toggles（checkbox 未勾選時不送出，需用 Optional[str]）
    arxiv_enabled: Optional[str] = Form(None),
    arxiv_max_results: int = Form(50, ge=1, le=200),
    hf_papers_enabled: Optional[str] = Form(None),
    chatpaper_enabled: Optional[str] = Form(None),
    chatpaper_page_size: int = Form(30, ge=1, le=100),
    rss_enabled: Optional[str] = Form(None),
    blogs_enabled: Optional[str] = Form(None),
    github_enabled: Optional[str] = Form(None),
    hackernews_enabled: Optional[str] = Form(None),
    hackernews_queries: str = Form(""),
    hackernews_min_points: int = Form(50, ge=0, le=1000),
    hackernews_max_results: int = Form(30, ge=1, le=200),
    reddit_enabled: Optional[str] = Form(None),
    reddit_subreddits: str = Form(""),
    reddit_min_upvotes: int = Form(50, ge=0, le=10000),
    reddit_max_results: int = Form(30, ge=1, le=200),
    newsapi_enabled: Optional[str] = Form(None),
    newsapi_key: str = Form(""),
    newsapi_query: str = Form(""),
    newsapi_max_results: int = Form(20, ge=1, le=100),
    # Source weights
    sw_arxiv: int = Form(0, ge=0, le=50),
    sw_chatpaper: int = Form(5, ge=0, le=50),
    sw_hf_papers: int = Form(0, ge=0, le=50),
    sw_rss: int = Form(15, ge=0, le=50),
    sw_blog: int = Form(15, ge=0, le=50),
    sw_github: int = Form(0, ge=0, le=50),
    sw_hackernews: int = Form(0, ge=0, le=50),
    sw_reddit: int = Form(0, ge=0, le=50),
    sw_newsapi: int = Form(15, ge=0, le=50),
):
    env_updates: dict[str, str] = {}
    if api_key.strip():
        env_updates["OPENROUTER_API_KEY"] = api_key.strip()
    if api_url.strip():
        env_updates["OPENROUTER_API_URL"] = api_url.strip()
    if newsapi_key.strip():
        env_updates["NEWSAPI_KEY"] = newsapi_key.strip()

    # 解析 hackernews queries（逗號分隔 → list）
    hn_queries = [q.strip() for q in hackernews_queries.split(",") if q.strip()]
    if not hn_queries:
        hn_queries = ["AI", "LLM", "GPT"]

    # 解析 reddit subreddits（逗號分隔 → list）
    reddit_subs = [s.strip() for s in reddit_subreddits.split(",") if s.strip()]
    if not reddit_subs:
        reddit_subs = ["LocalLLaMA", "MachineLearning"]

    config_updates: dict = {
        "llm.model": llm_model.strip() or cm.get_config().get("llm", {}).get("model", ""),
        "llm.fallback_model": fallback_model.strip(),
        "llm.max_tokens": max_tokens,
        "llm.request_delay_seconds": request_delay,
        "scoring.rule_threshold": rule_threshold,
        "scoring.llm_top_k": llm_top_k,
        "scoring.final_top_k": final_top_k,
        "scoring.hf_upvote_bonus_threshold": hf_upvote_threshold,
        "scoring.github_stars_high": github_stars_high,
        "scoring.github_stars_medium": github_stars_medium,
        "dedup.lookback_days": dedup_lookback,
        "retention_days": retention_days,
        # Collectors
        "collectors.arxiv.enabled": arxiv_enabled is not None,
        "collectors.arxiv.max_results": arxiv_max_results,
        "collectors.hf_papers.enabled": hf_papers_enabled is not None,
        "collectors.chatpaper.enabled": chatpaper_enabled is not None,
        "collectors.chatpaper.page_size": chatpaper_page_size,
        "collectors.rss.enabled": rss_enabled is not None,
        "collectors.blogs.enabled": blogs_enabled is not None,
        "collectors.github.enabled": github_enabled is not None,
        "collectors.hackernews.enabled": hackernews_enabled is not None,
        "collectors.hackernews.queries": hn_queries,
        "collectors.hackernews.min_points": hackernews_min_points,
        "collectors.hackernews.max_results": hackernews_max_results,
        "collectors.reddit.enabled": reddit_enabled is not None,
        "collectors.reddit.subreddits": reddit_subs,
        "collectors.reddit.min_upvotes": reddit_min_upvotes,
        "collectors.reddit.max_results": reddit_max_results,
        "collectors.newsapi.enabled": newsapi_enabled is not None,
        "collectors.newsapi.query": newsapi_query.strip() or "generative AI OR LLM OR large language model",
        "collectors.newsapi.max_results": newsapi_max_results,
        # Source weights
        "scoring.source_weights.arxiv": sw_arxiv,
        "scoring.source_weights.chatpaper": sw_chatpaper,
        "scoring.source_weights.hf_papers": sw_hf_papers,
        "scoring.source_weights.rss": sw_rss,
        "scoring.source_weights.blog": sw_blog,
        "scoring.source_weights.github": sw_github,
        "scoring.source_weights.hackernews": sw_hackernews,
        "scoring.source_weights.reddit": sw_reddit,
        "scoring.source_weights.newsapi": sw_newsapi,
    }
    try:
        cm.update_and_save(config_updates, env_updates)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="設定儲存失敗，請稍後重試")
    return RedirectResponse(url="/settings?saved=1", status_code=303)


@app.get("/api/search")
async def api_search(
    q: str = "",
    source: str = "",
    min_score: float = 0,
    max_score: float = 999,
    date_from: str = "",
    date_to: str = "",
    page: int = 1,
    limit: int = 20,
):
    """搜尋素材 API。"""
    result = ds.search_items(
        q=q, source=source, min_score=min_score, max_score=max_score,
        date_from=date_from, date_to=date_to, page=page, limit=limit,
    )
    return JSONResponse(content=result)


@app.post("/api/bookmark/{date_str}/{index}")
async def api_bookmark_add(date_str: str, index: int):
    """收藏素材。"""
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    detail = ds.get_item_detail(d, index)
    title = detail["title"] if detail else ""
    ds.set_bookmark(date_str, index, title=title)
    ds.invalidate_sidebar_cache()
    stats = ds.get_sidebar_stats()
    return JSONResponse({"message": "已收藏", "bookmarks_count": stats["bookmarks_count"]})


@app.delete("/api/bookmark/{date_str}/{index}")
async def api_bookmark_remove(date_str: str, index: int):
    """取消收藏。"""
    ds.remove_bookmark(date_str, index)
    ds.invalidate_sidebar_cache()
    stats = ds.get_sidebar_stats()
    return JSONResponse({"message": "已取消收藏", "bookmarks_count": stats["bookmarks_count"]})


@app.patch("/api/bookmark/{date_str}/{index}/status")
async def api_bookmark_status(request: Request, date_str: str, index: int):
    """更新書籤狀態。"""
    body = await request.json()
    status = body.get("status", "")
    if status not in ("bookmarked", "written", "published"):
        raise HTTPException(status_code=400, detail="無效的狀態")
    ds.update_bookmark_status(date_str, index, status)
    ds.invalidate_sidebar_cache()
    stats = ds.get_sidebar_stats()
    return JSONResponse({"message": "已更新", "bookmarks_count": stats["bookmarks_count"]})


@app.get("/api/bookmark/{date_str}/{index}/check")
async def api_bookmark_check(date_str: str, index: int):
    """檢查是否已收藏。"""
    return JSONResponse({"bookmarked": ds.is_bookmarked(date_str, index)})


@app.get("/api/bookmarks")
async def api_bookmarks(status: str = ""):
    """列出所有書籤。"""
    items = ds.list_bookmarked_items(status)
    return JSONResponse(content={"items": items})




@app.post("/api/promote-to-blog/{date_str}/{index}")
async def api_promote_to_blog(date_str: str, index: int):
    """將 Blog Draft 推送為正式 Blog 文章。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    try:
        result = ds.promote_to_blog(date_str, index)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

    return JSONResponse(content=result)


@app.get("/queue", response_class=HTMLResponse)
async def writing_queue(request: Request):
    """待寫清單（Kanban 視圖）。"""
    bookmarks = ds.get_all_bookmarks()

    # 按狀態分組（writing 已移除，自動歸入 bookmarked）
    columns = {
        "bookmarked": [],
        "written": [],
        "published": [],
    }
    for key, val in bookmarks.items():
        status = val.get("status", "bookmarked")
        if status == "writing":
            status = "bookmarked"
        if status not in columns:
            status = "bookmarked"

        # 載入完整 item 資訊
        d_str = val.get("date_str", "")
        idx = val.get("index", 0)
        try:
            d = date.fromisoformat(d_str)
            detail = ds.get_item_detail(d, idx)
        except Exception:
            detail = None

        entry = {**val, "key": key}
        if detail:
            entry["title"] = detail["title"]
            entry["url"] = detail.get("url", "")
            entry["source_name"] = detail.get("source_name", "")
            entry["total_score"] = detail.get("total_score", 0)
            entry["tags"] = detail.get("tags", [])
            entry["abstract"] = detail.get("abstract", "")
            entry["llm_reason"] = detail.get("llm_reason", "")

            # 檢查是否有 Blog Draft
            from src.utils import slugify as _slugify
            _title_slug = _slugify(detail["title"])
            entry["has_post"] = any(
                _title_slug in f.stem[len(d_str) + 1:] or f.stem[len(d_str) + 1:] in _title_slug
                for f in POSTS_DIR.glob(f"{d_str}*.md")
            )

            # 為 published 項目查找 blog_slug
            if status == "published":
                from src.utils import BLOGS_DIR, slugify
                title_slug = slugify(detail["title"])
                for bf in BLOGS_DIR.glob(f"{d_str}*.md"):
                    bslug = bf.stem[len(d_str) + 1:]
                    bparsed = ds._parse_markdown_file(bf)
                    if bparsed:
                        bfm = bparsed["frontmatter"]
                        bpt = slugify((bfm.get("paper_title") or bfm.get("title") or ""))
                        if bpt and (title_slug in bpt or bpt in title_slug):
                            entry["blog_slug"] = bslug
                            break
        columns[status].append(entry)

    return templates.TemplateResponse(
        "writing_queue.html",
        {
            "request": request,
            "columns": columns,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/api/status")
async def api_status():
    """JSON 格式的 7 天狀態（除錯用）。"""
    return JSONResponse(content={"week": ds.get_week_status(7, running_dates=_get_running_dates())})


@app.get("/api/logs/{date_str}", response_class=PlainTextResponse)
async def api_logs(date_str: str):
    """回傳指定日期的 pipeline 執行日誌（完整內容）。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    log_path = LOGS_DIR / f"{date_str}.log"
    if not log_path.exists():
        return PlainTextResponse(f"[尚無日誌] {date_str}.log 不存在", status_code=200)
    return PlainTextResponse(log_path.read_text(encoding="utf-8", errors="replace"))


@app.get("/api/logs/{date_str}/stage-info")
async def api_logs_stage_info(date_str: str):
    """回傳 pipeline 各階段狀態摘要。優先從 in-memory _runs 讀取，無則 fallback 到 data 檔案。"""
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    stages_order = ["collect", "score", "generate"]

    run = _runs.get(date_str)
    if run:
        stages = [{"name": n, "status": run.stages[n].status,
                   "elapsed": run.stages[n].elapsed,
                   "item_count": run.stages[n].item_count} for n in stages_order]
        result: dict[str, Any] = {"stages": stages, "pipeline_status": run.status}
        if run.status == "running":
            result["log_offset"] = run.log_offset
        return JSONResponse(result)

    # Fallback：無 in-memory state → 從 data 檔案推算
    data_state = ds.get_pipeline_state(d)
    stages_list = []
    for n in stages_order:
        status = "pending"
        if data_state in ("collected", "scored", "done") and n == "collect":
            status = "done"
        if data_state in ("scored", "done") and n == "score":
            status = "done"
        if data_state == "done" and n == "generate":
            status = "done"
        stages_list.append({"name": n, "status": status, "elapsed": None, "item_count": None})
    pipeline_status = data_state if data_state != "none" else "idle"
    return JSONResponse({"stages": stages_list, "pipeline_status": pipeline_status})


@app.get("/api/logs/{date_str}/stream")
async def api_logs_stream(date_str: str, from_: int = Query(0, alias="from", ge=0)):
    """SSE 串流：即時推送 pipeline 執行日誌（每 1 秒 poll log 檔新增行）。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    log_path = LOGS_DIR / f"{date_str}.log"

    async def event_generator():
        offset = from_
        consecutive_idle = 0
        current_stage = None
        # 最多串流 10 分鐘（600 次 × 1s）
        for _ in range(600):
            # 檢查 run 狀態
            run = _runs.get(date_str)
            if run and run.status in ("done", "failed"):
                # Drain 殘餘 log 再結束
                if log_path.exists():
                    try:
                        content = log_path.read_text(encoding="utf-8", errors="replace")
                        if len(content) > offset:
                            for line in content[offset:].splitlines():
                                stripped = line.strip()
                                if not stripped:
                                    continue
                                display = _format_sse_line(stripped, current_stage)
                                if display is None:
                                    continue
                                stage_name, text = display
                                yield f"data: {stage_name}|{text}\n\n"
                    except OSError:
                        pass
                yield "event: done\ndata: done\n\n"
                return
            if run and run.status == "cancelled":
                yield "event: cancelled\ndata: {}\n\n"
                return

            # 讀 log 檔新內容
            if log_path.exists():
                try:
                    content = log_path.read_text(encoding="utf-8", errors="replace")
                    if len(content) > offset:
                        new_text = content[offset:]
                        offset = len(content)
                        for line in new_text.splitlines():
                            stripped = line.strip()
                            if not stripped:
                                continue
                            # 嘗試解析 JSON log 行
                            if stripped.startswith("{"):
                                try:
                                    parsed = json.loads(stripped)
                                    if "pipeline_stage" in parsed:
                                        name = parsed["pipeline_stage"]
                                        action = parsed["stage_action"]
                                        current_stage = name if action == "start" else current_stage
                                        stage_payload: dict = {
                                            "name": name,
                                            "action": action,
                                            "elapsed": parsed.get("elapsed"),
                                        }
                                        if action == "end" and "item_count" in parsed:
                                            stage_payload["item_count"] = parsed["item_count"]
                                        # 即時更新 run.stages（SSE 讀到的 stage event）
                                        if run and name in run.stages:
                                            if action == "start":
                                                run.stages[name].status = "running"
                                            elif action == "end":
                                                run.stages[name].status = "done"
                                                run.stages[name].elapsed = parsed.get("elapsed")
                                                run.stages[name].item_count = parsed.get("item_count")
                                        yield f"event: stage\ndata: {json.dumps(stage_payload)}\n\n"
                                        continue
                                    if "msg" in parsed:
                                        display_text = _format_log_display(parsed)
                                        prefix_stage = current_stage or "pipeline"
                                        yield f"data: {prefix_stage}|{display_text}\n\n"
                                        continue
                                except json.JSONDecodeError:
                                    pass  # malformed JSON, fall through to plain text
                            # 非 JSON 行（marker 行、Rich CLI 輸出等）
                            prefix_stage = current_stage or "pipeline"
                            yield f"data: {prefix_stage}|{stripped}\n\n"
                        consecutive_idle = 0
                    else:
                        consecutive_idle += 1
                except Exception as e:
                    yield f"data: pipeline|[讀取 log 失敗: {e}]\n\n"
            else:
                consecutive_idle += 1
                if consecutive_idle == 1:
                    yield "data: pipeline|[等待 pipeline 啟動...]\n\n"

            # 若無 run 且 idle 10 秒 → emit done
            if not run and consecutive_idle >= 10:
                yield "event: done\ndata: done\n\n"
                return

            await asyncio.sleep(1)

        yield f"data: pipeline|[串流逾時，請直接查看 /api/logs/{date_str}]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


def _format_log_display(parsed: dict[str, Any]) -> str:
    """將 JSON log entry 格式化為 [HH:MM:SS] [LEVEL] msg 顯示文字。"""
    level = parsed.get("level", "INFO")
    msg = _fmt_log_msg(parsed)
    ts_str = parsed.get("ts", "")
    ts_display = ts_str[11:19] if len(ts_str) >= 19 else ""
    prefix = f"[{ts_display}] " if ts_display else ""
    return f"{prefix}[{level}] {msg}"


def _format_sse_line(stripped: str, current_stage: str | None) -> tuple[str, str] | None:
    """將一行 log 轉為 (stage_name, display_text) tuple，或 None 跳過。"""
    if stripped.startswith("{"):
        try:
            parsed = json.loads(stripped)
            if "pipeline_stage" in parsed:
                return None  # stage events 由呼叫端處理
            if "msg" in parsed:
                return (current_stage or "pipeline", _format_log_display(parsed))
        except json.JSONDecodeError:
            pass
    return (current_stage or "pipeline", stripped)


@app.get("/api/health")
async def api_health():
    """健康檢查端點，回傳 server 狀態與最近執行摘要。"""
    today_str = date.today().isoformat()

    # 最近一次成功完成的日期
    last_done: str | None = None
    from src.web.data_service import get_pipeline_state
    from datetime import timedelta
    for i in range(30):
        d = date.today() - timedelta(days=i)
        if get_pipeline_state(d) == "done":
            last_done = d.isoformat()
            break

    return JSONResponse({
        "status": "ok",
        "today": today_str,
        "running_pipelines": list(_get_running_dates()),
        "last_completed_date": last_done,
        "logs_dir": str(LOGS_DIR),
    })


def _run_pipeline(date_str: str, force: bool) -> None:
    """在背景執行 pipeline，並將 stdout/stderr 寫入 logs/{date_str}.log。"""
    with _lock:
        run = _runs.get(date_str)
        if not run or run.status != "running":
            return  # 不應發生，但防禦性檢查
    log_path = LOGS_DIR / f"{date_str}.log"
    try:
        cmd = [sys.executable, "-m", "src.cli", "run", "--date", date_str]
        if force:
            cmd.append("--force")
        with open(log_path, "w", encoding="utf-8") as log_file:
            log_file.write(f"=== Pipeline started: {date_str} (force={force}) ===\n")
            log_file.flush()
            env = {**os.environ, "AUTOPB_LOG_FORMAT": "json"}
            proc = subprocess.Popen(
                cmd,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                env=env,
            )
            with _lock:
                run.proc = proc
            proc.wait()
            exit_code = proc.returncode
            if exit_code in (-15, -9):  # SIGTERM / SIGKILL
                log_file.write(f"\n=== Pipeline cancelled by user: exit_code={exit_code} ===\n")
                final_status = "cancelled"
            else:
                log_file.write(f"\n=== Pipeline finished: exit_code={exit_code} ===\n")
                final_status = "done" if exit_code == 0 else "failed"
        _finalize_run(run, log_path, date_str, final_status)
    except Exception as e:
        _logger.error("Pipeline failed to start", extra={"date": date_str, "error": str(e)})
        try:
            log_path.write_text(f"Pipeline failed to start: {e}\n", encoding="utf-8")
        except OSError:
            pass
        with _lock:
            run.status = "failed"
            run.proc = None


def _run_stage_pipeline(date_str: str, stage_name: str) -> None:
    """在背景執行單一 pipeline stage，並將 stdout/stderr 附加至 logs/{date_str}.log。"""
    with _lock:
        run = _runs.get(date_str)
        if not run or run.status != "running":
            return
    log_path = LOGS_DIR / f"{date_str}.log"
    try:
        if stage_name in ("collect", "score"):
            cmd = [sys.executable, "-m", "src.cli", stage_name, "--force", "--date", date_str]
        elif stage_name == "generate":
            # generate 子命令不支援 --force，由 web layer 預先刪除舊輸出
            for pattern_dir, glob_pattern in [
                (POSTS_DIR, f"{date_str}*.md"),
                (NOTES_DIR, f"{date_str}*.md"),
                (PROMPTS_DIR, f"{date_str}*.md"),
            ]:
                for old_file in pattern_dir.glob(glob_pattern):
                    try:
                        old_file.unlink()
                        _logger.debug("Deleted old output file", extra={"file": str(old_file)})
                    except OSError as del_err:
                        _logger.warning("Failed to delete output file", extra={"file": str(old_file), "error": str(del_err)})
            cmd = [sys.executable, "-m", "src.cli", "generate", "--date", date_str]
        else:
            raise ValueError(f"Unhandled stage in _run_stage_pipeline: {stage_name}")
        with open(log_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"\n=== Stage {stage_name} re-run: {date_str} ===\n")
            log_file.flush()
            env = {**os.environ, "AUTOPB_LOG_FORMAT": "json"}
            proc = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT,
                                    text=True, encoding="utf-8", env=env)
            with _lock:
                run.proc = proc
            proc.wait()
            exit_code = proc.returncode
            if exit_code in (-15, -9):
                log_file.write(f"\n=== Stage {stage_name} cancelled by user: exit_code={exit_code} ===\n")
                final_status = "cancelled"
            else:
                log_file.write(f"\n=== Stage {stage_name} finished: exit_code={exit_code} ===\n")
                final_status = "done" if exit_code == 0 else "failed"
        _finalize_run(run, log_path, date_str, final_status)
    except Exception as e:
        _logger.error("Stage pipeline failed", extra={"date": date_str, "stage": stage_name, "error": str(e)})
        try:
            with open(log_path, "a", encoding="utf-8") as lf:
                lf.write(f"\n=== Stage {stage_name} finished: exit_code=1 ===\n")
        except OSError:
            pass
        with _lock:
            run.status = "failed"
            run.proc = None


@app.post("/api/run/{date_str}")
async def api_run(date_str: str, background_tasks: BackgroundTasks):
    """在背景執行指定日期的 pipeline。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    with _lock:
        existing = _runs.get(date_str)
        if existing and existing.status == "running":
            raise HTTPException(status_code=409, detail=f"Pipeline 已在執行中（{date_str}）")
        _runs[date_str] = PipelineRun(status="running", log_offset=0)
    background_tasks.add_task(_run_pipeline, date_str, False)
    return JSONResponse({"message": f"Pipeline 已啟動（{date_str}），可透過 /api/logs/{date_str} 查看進度", "date": date_str})


@app.post("/api/run/{date_str}/force")
async def api_run_force(date_str: str, background_tasks: BackgroundTasks):
    """強制重跑指定日期的 pipeline（清除 checkpoint）。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    with _lock:
        existing = _runs.get(date_str)
        if existing and existing.status == "running":
            raise HTTPException(status_code=409, detail=f"Pipeline 已在執行中（{date_str}）")
        _runs[date_str] = PipelineRun(status="running", log_offset=0)
    background_tasks.add_task(_run_pipeline, date_str, True)
    return JSONResponse({"message": f"強制重跑已啟動（{date_str}），可透過 /api/logs/{date_str} 查看進度", "date": date_str})


@app.post("/api/run/{date_str}/stop")
async def api_run_stop(date_str: str):
    """中止正在執行的 pipeline。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    with _lock:
        run = _runs.get(date_str)
        proc = run.proc if run else None

    if proc is None:
        raise HTTPException(status_code=404, detail="找不到執行中的 pipeline")

    if proc.poll() is not None:
        return JSONResponse({"message": f"Pipeline 已結束（{date_str}）", "date": date_str})

    proc.terminate()
    try:
        loop = asyncio.get_event_loop()
        await asyncio.wait_for(
            loop.run_in_executor(None, proc.wait),
            timeout=3.0,
        )
    except asyncio.TimeoutError:
        proc.kill()

    return JSONResponse({"message": f"Pipeline 已中止（{date_str}）", "date": date_str})


@app.post("/api/run/{date_str}/stage/{stage_name}")
async def api_run_stage(date_str: str, stage_name: str, background_tasks: BackgroundTasks):
    """觸發指定日期的單一 pipeline stage（背景執行）。"""
    if stage_name not in VALID_STAGES:
        raise HTTPException(status_code=400, detail=f"Invalid stage: {stage_name}")
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    log_path = LOGS_DIR / f"{date_str}.log"
    log_offset = log_path.stat().st_size if log_path.exists() else 0
    with _lock:
        existing = _runs.get(date_str)
        if existing and existing.status == "running":
            raise HTTPException(status_code=409, detail=f"Pipeline 已在執行中（{date_str}）")
        if existing:
            # 重用：保留其他 stage 狀態，只重設目標 stage
            existing.status = "running"
            existing.stages[stage_name] = StageInfo(status="pending")
            existing.log_offset = log_offset
        else:
            _runs[date_str] = PipelineRun(status="running", log_offset=log_offset)
    background_tasks.add_task(_run_stage_pipeline, date_str, stage_name)
    return JSONResponse({"status": "started", "date": date_str, "stage": stage_name, "log_offset": log_offset})


def _build_checkpoint_summary(d: date, stage_name: str) -> list[dict] | None:
    """從 data 檔案產生 checkpoint 摘要條目（無 log 時 fallback）。"""
    from datetime import datetime as _dt

    entries: list[dict] = []

    def _mtime_str(p: Path) -> str:
        try:
            mt = p.stat().st_mtime
            return _dt.fromtimestamp(mt).strftime("%H:%M:%S")
        except OSError:
            return "--:--:--"

    prefix = d.isoformat()
    raw_path = RAW_DIR / f"{prefix}.json"
    scored_path = SCORED_DIR / f"{prefix}.json"

    if stage_name == "collect":
        if not raw_path.exists():
            return None
        data = load_json(raw_path)
        count = len(data) if isinstance(data, list) else 0
        ts = _mtime_str(raw_path)
        entries.append({"ts": ts, "level": "INFO", "msg": f"checkpoint 跳過：raw 資料已存在（{count} 篇）"})
        entries.append({"ts": ts, "level": "INFO", "msg": f"檔案：{raw_path.name}"})

    elif stage_name == "score":
        if not scored_path.exists():
            return None
        data = load_json(scored_path)
        count = len(data) if isinstance(data, list) else 0
        ts = _mtime_str(scored_path)
        entries.append({"ts": ts, "level": "INFO", "msg": f"checkpoint 跳過：scored 資料已存在（{count} 篇）"})
        # 摘要：分數範圍
        if isinstance(data, list) and data:
            scores = [it.get("total_score", 0) for it in data if isinstance(it, dict)]
            if scores:
                entries.append({"ts": ts, "level": "INFO", "msg": f"分數範圍：{min(scores):.0f} ~ {max(scores):.0f}，平均 {sum(scores)/len(scores):.1f}"})

    elif stage_name == "generate":
        posts = list(POSTS_DIR.glob(f"{prefix}*.md"))
        notes = list(NOTES_DIR.glob(f"{prefix}*.md"))
        if not posts and not notes:
            return None
        # 取最晚的 mtime
        all_files = posts + notes
        latest = max(all_files, key=lambda f: f.stat().st_mtime)
        ts = _mtime_str(latest)
        entries.append({"ts": ts, "level": "INFO", "msg": f"checkpoint 跳過：產出已存在（{len(posts)} 篇 blog, {len(notes)} 篇 note）"})
        for p in sorted(posts):
            entries.append({"ts": ts, "level": "INFO", "msg": f"  Blog: {p.name}"})
        for n in sorted(notes):
            entries.append({"ts": ts, "level": "INFO", "msg": f"  Note: {n.name}"})

    return entries if entries else None


@app.get("/api/logs/{date_str}/stage/{stage_name}")
async def api_stage_log(date_str: str, stage_name: str):
    """回傳指定 stage 最後一次執行的 log 條目。"""
    if stage_name not in VALID_STAGES:
        raise HTTPException(status_code=400, detail=f"Invalid stage: {stage_name}")
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    log_path = LOGS_DIR / f"{date_str}.log"

    # 先嘗試從 log 檔解析 stage 條目
    item_count = None
    in_stage = False
    all_entries: list[dict] = []
    temp_entries: list[dict] = []

    if log_path.exists():
        for line in log_path.read_text(encoding="utf-8").splitlines():
            try:
                obj = json.loads(line)
                if obj.get("pipeline_stage") == stage_name:
                    if obj.get("stage_action") == "start":
                        temp_entries = []
                        in_stage = True
                    elif obj.get("stage_action") == "end":
                        in_stage = False
                        item_count = obj.get("item_count")
                        all_entries = list(temp_entries)
                elif in_stage:
                    ts_full = obj.get("ts", "")
                    ts = ts_full[11:19] if len(ts_full) >= 19 else ts_full
                    temp_entries.append({
                        "ts": ts,
                        "level": obj.get("level", "INFO"),
                        "msg": _fmt_log_msg(obj),
                    })
            except (json.JSONDecodeError, ValueError):
                pass

    if in_stage:
        return {"stage": stage_name, "entries": temp_entries, "item_count": None, "in_progress": True}
    if all_entries:
        return {"stage": stage_name, "entries": all_entries, "item_count": item_count}

    # Fallback：無 log 但資料檔存在 → 產生 checkpoint 摘要
    d = date.fromisoformat(date_str)
    summary = _build_checkpoint_summary(d, stage_name)
    if summary:
        return {"stage": stage_name, "entries": summary, "item_count": None, "checkpoint": True}
    return {"stage": stage_name, "entries": [], "item_count": None}


@app.post("/api/feedback/{date_str}/{slug}/{rating}")
async def api_feedback(date_str: str, slug: str, rating: str):
    """儲存文章品質回饋。"""
    if rating not in ["good", "normal", "bad"]:
        raise HTTPException(status_code=400, detail="無效的評分")
    ds.save_feedback(date_str, slug, rating)
    return JSONResponse({"message": "感謝回饋"})
