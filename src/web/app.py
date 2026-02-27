"""FastAPI 監控網頁應用程式。"""

from __future__ import annotations

import subprocess
import sys
from datetime import date
from pathlib import Path

import asyncio
import time as _time

from fastapi import BackgroundTasks, FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from src.web import data_service as ds
from src.web import config_manager as cm

app = FastAPI(title="Auto Post Blog Monitor", docs_url=None, redoc_url=None)
cm.init_config()
RUNNING_TASKS: set[str] = set()

# B5: 改用 pathlib 建構路徑，避免 str.replace 脆弱性
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

# B6: log 存放目錄
LOGS_DIR = Path(__file__).resolve().parent.parent.parent / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)


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
    posts = ds.list_posts(date_str)
    notes = ds.list_notes(date_str)

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
            "posts": posts,
            "notes": notes,
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
        d = date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    detail = ds.get_item_detail(d, index)
    if detail is None:
        raise HTTPException(status_code=404, detail="找不到該項目")

    return templates.TemplateResponse(
        "item_detail.html",
        {
            "request": request,
            "date_str": date_str,
            "item": detail,
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


@app.get("/posts", response_class=HTMLResponse)
async def posts_list(request: Request):
    posts = ds.list_all_posts()
    return templates.TemplateResponse(
        "posts_list.html",
        {
            "request": request,
            "posts": posts,
            "sidebar_stats": ds.get_sidebar_stats(),
        },
    )


@app.get("/notes", response_class=HTMLResponse)
async def notes_list(request: Request):
    notes = ds.list_all_notes()
    return templates.TemplateResponse(
        "notes_list.html",
        {
            "request": request,
            "notes": notes,
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
    max_tokens: int = Form(8192),
    request_delay: float = Form(0.5),
    rule_threshold: int = Form(25),
    llm_top_k: int = Form(30),
    final_top_k: int = Form(10),
    hf_upvote_threshold: int = Form(10),
    github_stars_high: int = Form(100),
    github_stars_medium: int = Form(50),
    dedup_lookback: int = Form(7),
    retention_days: int = Form(90),
):
    env_updates: dict[str, str] = {}
    if api_key.strip():
        env_updates["OPENROUTER_API_KEY"] = api_key.strip()
    if api_url.strip():
        env_updates["OPENROUTER_API_URL"] = api_url.strip()

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
    }
    cm.update_and_save(config_updates, env_updates)
    return RedirectResponse(url="/settings?saved=1", status_code=303)


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


@app.get("/api/logs/{date_str}/stream")
async def api_logs_stream(date_str: str):
    """SSE 串流：即時推送 pipeline 執行日誌（每 1 秒 poll log 檔新增行）。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")

    log_path = LOGS_DIR / f"{date_str}.log"

    async def event_generator():
        offset = 0
        consecutive_idle = 0
        # 最多串流 10 分鐘（600 次 × 1s）
        for _ in range(600):
            if log_path.exists():
                try:
                    content = log_path.read_text(encoding="utf-8", errors="replace")
                    if len(content) > offset:
                        new_text = content[offset:]
                        offset_new = len(content)
                        for line in new_text.splitlines():
                            yield f"data: {line}\n\n"
                        offset = offset_new
                        consecutive_idle = 0
                    else:
                        consecutive_idle += 1
                except Exception as e:
                    yield f"data: [讀取 log 失敗: {e}]\n\n"
            else:
                consecutive_idle += 1
                if consecutive_idle == 1:
                    yield f"data: [等待 pipeline 啟動...]\n\n"

            # 若 pipeline 結束且 30 秒無新輸出，斷開連線
            if consecutive_idle >= 30 and log_path.exists():
                content = log_path.read_text(encoding="utf-8", errors="replace")
                if "=== Pipeline finished" in content:
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
    RUNNING_TASKS.add(date_str)
    log_path = LOGS_DIR / f"{date_str}.log"
    try:
        cmd = [sys.executable, "-m", "src.cli", "run", "--date", date_str]
        if force:
            cmd.append("--force")
        # B6: 改用 Popen 寫 log，不再 capture_output 吞掉所有輸出
        with open(log_path, "w", encoding="utf-8") as log_file:
            log_file.write(f"=== Pipeline started: {date_str} (force={force}) ===\n")
            log_file.flush()
            proc = subprocess.Popen(
                cmd,
                stdout=log_file,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
            )
            proc.wait()
            exit_code = proc.returncode
            log_file.write(f"\n=== Pipeline finished: exit_code={exit_code} ===\n")
    except Exception as e:
        log_path.write_text(f"Pipeline failed to start: {e}\n", encoding="utf-8")
    finally:
        RUNNING_TASKS.discard(date_str)


@app.post("/api/run/{date_str}")
async def api_run(date_str: str, background_tasks: BackgroundTasks):
    """在背景執行指定日期的 pipeline。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    background_tasks.add_task(_run_pipeline, date_str, False)
    return JSONResponse({"message": f"Pipeline 已啟動（{date_str}），可透過 /api/logs/{date_str} 查看進度", "date": date_str})


@app.post("/api/run/{date_str}/force")
async def api_run_force(date_str: str, background_tasks: BackgroundTasks):
    """強制重跑指定日期的 pipeline（清除 checkpoint）。"""
    try:
        date.fromisoformat(date_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="日期格式錯誤")
    background_tasks.add_task(_run_pipeline, date_str, True)
    return JSONResponse({"message": f"強制重跑已啟動（{date_str}），可透過 /api/logs/{date_str} 查看進度", "date": date_str})


@app.post("/api/feedback/{date_str}/{slug}/{rating}")
async def api_feedback(date_str: str, slug: str, rating: str):
    """儲存文章品質回饋。"""
    if rating not in ["good", "normal", "bad"]:
        raise HTTPException(status_code=400, detail="無效的評分")
    ds.save_feedback(date_str, slug, rating)
    return JSONResponse({"message": "感謝回饋"})
