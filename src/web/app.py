"""FastAPI 監控網頁應用程式。"""

from __future__ import annotations

import json
import os
import subprocess
import sys
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
from src.utils import NOTES_DIR, POSTS_DIR, PROMPTS_DIR
from src.web import data_service as ds
from src.web import config_manager as cm

_logger = get_logger("web.app")

app = FastAPI(title="Auto Post Blog Monitor", docs_url=None, redoc_url=None)


@app.on_event("startup")
async def startup_event():
    cm.init_config()


_proc_lock = threading.Lock()
RUNNING_TASKS: set[str] = set()
RUNNING_PROCS: dict[str, subprocess.Popen] = {}

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
    week_status = ds.get_week_status(7, running_dates=RUNNING_TASKS)
    top_items = ds.get_week_top_items(7, top_k=10)
    charts = ds.get_dashboard_charts(30)
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "week_status": week_status,
            "top_items": top_items,
            "today": date.today().isoformat(),
            "charts": charts,
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
    items = ds.get_day_items(d)
    contents = ds.list_day_contents(date_str)

    # Build title → content mapping for inline badges in scored items table
    content_map = {}
    for c in contents:
        key = (c.get("title") or "").strip().lower()
        if key:
            content_map[key] = {
                "has_post": c.get("has_post", False),
                "has_note": c.get("has_note", False),
                "post_slug": c.get("post_slug"),
                "note_slug": c.get("note_slug"),
            }

    state = ds.get_pipeline_state(d)
    if RUNNING_TASKS and date_str in RUNNING_TASKS:
        state = "running"

    return templates.TemplateResponse(
        "day_detail.html",
        {
            "request": request,
            "date_str": date_str,
            "stats": stats,
            "items": items,
            "content_map": content_map,
            "state": state,
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
    return templates.TemplateResponse(
        "material_library.html",
        {
            "request": request,
            "materials": materials,
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

    return templates.TemplateResponse(
        "material_detail.html",
        {
            "request": request,
            "date_str": date_str,
            "item": detail,
            "back_url": "/materials",
            "back_label": "素材庫",
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
):
    env_updates: dict[str, str] = {}
    if api_key.strip():
        env_updates["OPENROUTER_API_KEY"] = api_key.strip()
    if api_url.strip():
        env_updates["OPENROUTER_API_URL"] = api_url.strip()

    # 解析 hackernews queries（逗號分隔 → list）
    hn_queries = [q.strip() for q in hackernews_queries.split(",") if q.strip()]
    if not hn_queries:
        hn_queries = ["AI", "LLM", "GPT"]

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
    return JSONResponse({"message": "已收藏"})


@app.delete("/api/bookmark/{date_str}/{index}")
async def api_bookmark_remove(date_str: str, index: int):
    """取消收藏。"""
    ds.remove_bookmark(date_str, index)
    return JSONResponse({"message": "已取消收藏"})


@app.patch("/api/bookmark/{date_str}/{index}/status")
async def api_bookmark_status(request: Request, date_str: str, index: int):
    """更新書籤狀態。"""
    body = await request.json()
    status = body.get("status", "")
    if status not in ("bookmarked", "writing", "written", "published"):
        raise HTTPException(status_code=400, detail="無效的狀態")
    ds.update_bookmark_status(date_str, index, status)
    return JSONResponse({"message": "已更新"})


@app.get("/api/bookmark/{date_str}/{index}/check")
async def api_bookmark_check(date_str: str, index: int):
    """檢查是否已收藏。"""
    return JSONResponse({"bookmarked": ds.is_bookmarked(date_str, index)})


@app.get("/api/bookmarks")
async def api_bookmarks(status: str = ""):
    """列出所有書籤。"""
    items = ds.list_bookmarked_items(status)
    return JSONResponse(content={"items": items})


@app.get("/queue", response_class=HTMLResponse)
async def writing_queue(request: Request):
    """待寫清單（Kanban 視圖）。"""
    bookmarks = ds.get_all_bookmarks()

    # 按狀態分組
    columns = {
        "bookmarked": [],
        "writing": [],
        "written": [],
        "published": [],
    }
    for key, val in bookmarks.items():
        status = val.get("status", "bookmarked")
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
            entry["source_name"] = detail.get("source_name", "")
            entry["total_score"] = detail.get("total_score", 0)
            entry["tags"] = detail.get("tags", [])
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
    return JSONResponse(content={"week": ds.get_week_status(7, running_dates=RUNNING_TASKS)})


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
    """解析 log 檔，回傳 pipeline 各階段狀態摘要。"""
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    log_path = LOGS_DIR / f"{date_str}.log"
    stages_order = ["collect", "score", "generate"]
    stages = {n: {"name": n, "status": "pending", "elapsed": None, "item_count": None} for n in stages_order}

    # Step 1：用資料檔推算基礎狀態（最可靠的 fallback）
    data_state = ds.get_pipeline_state(d)
    if data_state in ("collected", "scored", "done"):
        stages["collect"]["status"] = "done"
    if data_state in ("scored", "done"):
        stages["score"]["status"] = "done"
    if data_state == "done":
        stages["generate"]["status"] = "done"

    pipeline_status = data_state if data_state != "none" else "idle"

    # Step 2：若正在執行中，標記 pipeline_status = running
    if date_str in RUNNING_TASKS:
        pipeline_status = "running"

    # Step 3：解析 log 取得精確 elapsed 與即時 stage 狀態（覆蓋 Step 1）
    if log_path.exists():
        content = log_path.read_text(encoding="utf-8", errors="replace")
        has_stage_markers = False

        for line in content.splitlines():
            if "=== Pipeline started" in line:
                # 新一輪執行：重置 stage 狀態（log 是每次覆寫的）
                stages = {n: {"name": n, "status": "pending", "elapsed": None, "item_count": None} for n in stages_order}
                if date_str not in RUNNING_TASKS:
                    pipeline_status = "running"
                continue
            if "Pipeline cancelled by user" in line:
                pipeline_status = "cancelled"
                # 將仍為 running 的 stage 標為 cancelled
                for n in stages_order:
                    if stages[n]["status"] == "running":
                        stages[n]["status"] = "cancelled"
                continue
            for s in ["collect", "score", "generate"]:
                if f"Stage {s} cancelled by user" in line:
                    if stages[s]["status"] == "running":
                        stages[s]["status"] = "cancelled"
            if "=== Pipeline finished" in line:
                if date_str not in RUNNING_TASKS:
                    pipeline_status = "done" if "exit_code=0" in line else "failed"
                    # 若 pipeline 結束但有 stage 仍為 running → 標為 failed
                    for s in stages.values():
                        if s["status"] == "running":
                            s["status"] = "failed"
                continue
            try:
                parsed = json.loads(line)
                if "pipeline_stage" in parsed:
                    has_stage_markers = True
                    name = parsed["pipeline_stage"]
                    action = parsed["stage_action"]
                    if action == "start":
                        stages[name]["status"] = "running"
                    elif action == "end":
                        stages[name]["status"] = "done"
                        stages[name]["elapsed"] = parsed.get("elapsed")
                        if "item_count" in parsed:
                            stages[name]["item_count"] = parsed["item_count"]
            except Exception:
                _logger.debug("SSE log parse error", exc_info=True)

        # 若 log 沒有 stage markers（舊格式），回退到 data_state 推算結果
        if not has_stage_markers:
            if data_state in ("collected", "scored", "done"):
                stages["collect"]["status"] = "done"
            if data_state in ("scored", "done"):
                stages["score"]["status"] = "done"
            if data_state == "done":
                stages["generate"]["status"] = "done"

    return JSONResponse({"stages": [stages[n] for n in stages_order], "pipeline_status": pipeline_status})


@app.get("/api/logs/{date_str}/stream")
async def api_logs_stream(date_str: str, from_: int = Query(0, alias="from")):
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
            if log_path.exists():
                try:
                    content = log_path.read_text(encoding="utf-8", errors="replace")
                    if len(content) > offset:
                        new_text = content[offset:]
                        offset_new = len(content)
                        for line in new_text.splitlines():
                            if not line.strip():
                                continue
                            display = line
                            try:
                                parsed = json.loads(line)
                                if "pipeline_stage" in parsed:
                                    name = parsed["pipeline_stage"]
                                    action = parsed["stage_action"]
                                    current_stage = name if action == "start" else None
                                    stage_payload: dict = {
                                        "name": name,
                                        "action": action,
                                        "elapsed": parsed.get("elapsed"),
                                    }
                                    if action == "end" and "item_count" in parsed:
                                        stage_payload["item_count"] = parsed["item_count"]
                                    yield f"event: stage\ndata: {json.dumps(stage_payload)}\n\n"
                                    continue  # 不輸出為普通 log 行
                                if "msg" in parsed:
                                    level = parsed.get("level", "INFO")
                                    msg = _fmt_log_msg(parsed)
                                    ts_str = parsed.get("ts", "")
                                    ts_display = ts_str[11:19] if len(ts_str) >= 19 else ""
                                    prefix = f"[{ts_display}] " if ts_display else ""
                                    display = f"{prefix}[{level}] {msg}"
                            except Exception:
                                _logger.debug("SSE log parse error", exc_info=True)
                            # 偵測 pipeline 取消
                            if "Pipeline cancelled by user" in display or any(
                                f"Stage {s} cancelled by user" in display for s in VALID_STAGES
                            ):
                                yield f"event: cancelled\ndata: {{}}\n\n"
                                return
                            # 若偵測到 pipeline 結束行，立即送 done event
                            if "=== Pipeline finished" in line:
                                yield f"data: pipeline|{display}\n\n"
                                yield "event: done\ndata: done\n\n"
                                return
                            # 偵測單一 stage 重跑結束行
                            for _sname in VALID_STAGES:
                                if f"=== Stage {_sname} finished" in line:
                                    yield f"data: pipeline|{display}\n\n"
                                    yield "event: done\ndata: done\n\n"
                                    return
                            prefix = current_stage or "pipeline"
                            yield f"data: {prefix}|{display}\n\n"
                        offset = offset_new
                        consecutive_idle = 0
                    else:
                        consecutive_idle += 1
                except Exception as e:
                    yield f"data: pipeline|[讀取 log 失敗: {e}]\n\n"
            else:
                consecutive_idle += 1
                if consecutive_idle == 1:
                    yield f"data: pipeline|[等待 pipeline 啟動...]\n\n"

            # 若 pipeline 結束且 30 秒無新輸出，斷開連線
            if consecutive_idle >= 30 and log_path.exists():
                content = log_path.read_text(encoding="utf-8", errors="replace")
                new_content = content[offset:]  # 只看未讀過的部分
                if "Pipeline cancelled by user" in new_content or any(f"Stage {s} cancelled" in new_content for s in VALID_STAGES):
                    yield f"event: cancelled\ndata: {{}}\n\n"
                    return
                if "=== Pipeline finished" in new_content or any(f"=== Stage {s} finished" in new_content for s in VALID_STAGES):
                    yield "data: [Pipeline 已結束]\n\n"
                    yield "event: done\ndata: done\n\n"
                    return

            await asyncio.sleep(1)

        yield "data: [串流逾時，請直接查看 /api/logs/{date_str}]\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",  # 停用 nginx 緩衝
        },
    )


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
        "running_pipelines": list(RUNNING_TASKS),
        "last_completed_date": last_done,
        "logs_dir": str(LOGS_DIR),
    })


def _run_pipeline(date_str: str, force: bool) -> None:
    """在背景執行 pipeline，並將 stdout/stderr 寫入 logs/{date_str}.log。"""
    with _proc_lock:
        if date_str in RUNNING_TASKS:
            return  # 防止同一日期重複執行
        RUNNING_TASKS.add(date_str)

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
            with _proc_lock:
                RUNNING_PROCS[date_str] = proc
            proc.wait()
            exit_code = proc.returncode
            if exit_code in (-15, -9):  # SIGTERM / SIGKILL
                log_file.write(f"\n=== Pipeline cancelled by user: exit_code={exit_code} ===\n")
            else:
                log_file.write(f"\n=== Pipeline finished: exit_code={exit_code} ===\n")
    except Exception as e:
        _logger.error("Pipeline failed to start", extra={"date": date_str, "error": str(e)})
        try:
            log_path.write_text(f"Pipeline failed to start: {e}\n", encoding="utf-8")
        except OSError:
            pass
    finally:
        with _proc_lock:
            RUNNING_TASKS.discard(date_str)
            RUNNING_PROCS.pop(date_str, None)


def _run_stage_pipeline(date_str: str, stage_name: str) -> None:
    """在背景執行單一 pipeline stage，並將 stdout/stderr 附加至 logs/{date_str}.log。"""
    with _proc_lock:
        if date_str in RUNNING_TASKS:
            return
        RUNNING_TASKS.add(date_str)
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
            with _proc_lock:
                RUNNING_PROCS[date_str] = proc
            proc.wait()
            exit_code = proc.returncode
            if exit_code in (-15, -9):
                log_file.write(f"\n=== Stage {stage_name} cancelled by user: exit_code={exit_code} ===\n")
            else:
                log_file.write(f"\n=== Stage {stage_name} finished: exit_code={exit_code} ===\n")
    except Exception as e:
        _logger.error("Stage pipeline failed", extra={"date": date_str, "stage": stage_name, "error": str(e)})
        try:
            with open(log_path, "a", encoding="utf-8") as lf:
                lf.write(f"\n=== Stage {stage_name} finished: exit_code=1 ===\n")
        except OSError:
            pass
    finally:
        with _proc_lock:
            RUNNING_TASKS.discard(date_str)
            RUNNING_PROCS.pop(date_str, None)


@app.post("/api/run/{date_str}")
async def api_run(date_str: str, background_tasks: BackgroundTasks):
    """在背景執行指定日期的 pipeline。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    with _proc_lock:
        if date_str in RUNNING_TASKS:
            raise HTTPException(status_code=409, detail=f"Pipeline 已在執行中（{date_str}）")
    background_tasks.add_task(_run_pipeline, date_str, False)
    return JSONResponse({"message": f"Pipeline 已啟動（{date_str}），可透過 /api/logs/{date_str} 查看進度", "date": date_str})


@app.post("/api/run/{date_str}/force")
async def api_run_force(date_str: str, background_tasks: BackgroundTasks):
    """強制重跑指定日期的 pipeline（清除 checkpoint）。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    with _proc_lock:
        if date_str in RUNNING_TASKS:
            raise HTTPException(status_code=409, detail=f"Pipeline 已在執行中（{date_str}）")
    background_tasks.add_task(_run_pipeline, date_str, True)
    return JSONResponse({"message": f"強制重跑已啟動（{date_str}），可透過 /api/logs/{date_str} 查看進度", "date": date_str})


@app.post("/api/run/{date_str}/stop")
async def api_run_stop(date_str: str):
    """中止正在執行的 pipeline。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    with _proc_lock:
        proc = RUNNING_PROCS.get(date_str)

    if proc is None:
        raise HTTPException(status_code=404, detail="找不到執行中的 pipeline")

    if proc.poll() is not None:
        # 已結束但尚未從 dict 清除
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
    with _proc_lock:
        if date_str in RUNNING_TASKS:
            raise HTTPException(status_code=409, detail=f"Pipeline 已在執行中（{date_str}）")
    log_path = LOGS_DIR / f"{date_str}.log"
    log_offset = log_path.stat().st_size if log_path.exists() else 0
    background_tasks.add_task(_run_stage_pipeline, date_str, stage_name)
    return JSONResponse({"status": "started", "date": date_str, "stage": stage_name, "log_offset": log_offset})


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
    if not log_path.exists():
        return {"stage": stage_name, "entries": [], "item_count": None}

    item_count = None
    in_stage = False
    all_entries: list[dict] = []
    temp_entries: list[dict] = []

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
    return {"stage": stage_name, "entries": all_entries, "item_count": item_count}


@app.post("/api/feedback/{date_str}/{slug}/{rating}")
async def api_feedback(date_str: str, slug: str, rating: str):
    """儲存文章品質回饋。"""
    if rating not in ["good", "normal", "bad"]:
        raise HTTPException(status_code=400, detail="無效的評分")
    ds.save_feedback(date_str, slug, rating)
    return JSONResponse({"message": "感謝回饋"})
