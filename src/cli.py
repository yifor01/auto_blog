"""CLI entry point for auto_post_blog pipeline.

只負責參數解析與呼叫 `src.pipeline` 中的編排函式。實際的 pipeline 業務邏輯
（收集 / 篩選 / 生成、checkpoint、增量評分、跨日去重、collectors 註冊）都在
`src/pipeline.py`。
"""

from __future__ import annotations

from datetime import date, timedelta
from pathlib import Path

import typer
from rich.markdown import Markdown
from rich.table import Table

from src.logger import get_logger, setup_logging
from src.models import ScoredItem, scored_from_raw
from src.pipeline import (
    get_pipeline_state,
    get_raw_path,
    get_scored_path,
    print_summary,
    run_catchup,
    run_collect,
    run_generate,
    run_pipeline,
    run_score,
)
from src.utils import (
    FEEDBACK_DIR,
    HEALTH_DIR,
    LISTS_DIR,
    NOTES_DIR,
    POSTS_DIR,
    PROMPTS_DIR,
    RAW_DIR,
    SCORED_DIR,
    console,
    load_config,
    load_json,
)

setup_logging()  # 從 AUTOPB_LOG_FORMAT env 自動偵測模式
_logger = get_logger("cli")

app = typer.Typer(
    name="autopb",
    help="Auto Post Blog — AI 新知自動收集 & 部落格素材產出系統",
)


# ──────────────────────────────────────────────────────────
# 日期驗證 helper
# ──────────────────────────────────────────────────────────

def _parse_date(date_str: str | None) -> date:
    """解析日期字串，提供友善錯誤訊息。"""
    if date_str is None:
        return date.today()
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        console.print(f"[red]✗ 日期格式錯誤：'{date_str}'，請使用 YYYY-MM-DD（例如 2026-02-26）[/red]")
        raise typer.Exit(1)


# ──────────────────────────────────────────────────────────
# CLI Commands
# ──────────────────────────────────────────────────────────

@app.command()
def run(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD), 預設今天"),
    dry_run: bool = typer.Option(False, "--dry-run", help="只收集和篩選，不生成內容"),
    top_k: int = typer.Option(None, "--top-k", "-k", help="覆蓋 config 中的 final_top_k"),
    force: bool = typer.Option(False, "--force", "-f", help="強制重新執行, 清除所有快取與生成結果"),
    supplement: bool = typer.Option(False, "--supplement", "-s", help="補收缺失 source 並增量評分"),
):
    """完整 pipeline: 收集 → 篩選 → 生成 (支援斷點續跑)"""
    d = _parse_date(target_date)
    run_pipeline(d, dry_run=dry_run, top_k=top_k, force=force, supplement=supplement)


@app.command()
def catchup(
    days: int = typer.Option(7, "--days", help="回補最近幾天"),
    dry_run: bool = typer.Option(False, "--dry-run", help="只收集和篩選"),
):
    """補跑缺失的日期 (開機後自動補跑)。"""
    run_catchup(days, dry_run)


@app.command()
def collect(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD)"),
    force: bool = typer.Option(False, "--force", "-f", help="強制重新收集"),
):
    """只收集資料 (已有快取則跳過)。"""
    d = _parse_date(target_date)
    run_collect(d, force=force)


@app.command()
def score(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD)"),
    force: bool = typer.Option(False, "--force", "-f", help="強制重新篩選"),
):
    """對已收集的資料進行篩選 (已有快取則跳過)。"""
    d = _parse_date(target_date)
    run_score(d, force=force)


@app.command()
def generate(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期"),
    top_k: int = typer.Option(None, "--top-k", "-k", help="生成數量，預設使用 config 的 final_top_k"),
):
    """對已篩選的 top items 生成內容。"""
    d = _parse_date(target_date)
    run_generate(d, top_k=top_k)


@app.command()
def summary(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期"),
):
    """查看今日評分摘要。"""
    d = _parse_date(target_date)
    scored_path = get_scored_path(d)
    if not scored_path.exists():
        console.print(f"[yellow]No scored data for {d}[/yellow]")
        return

    scored_data = load_json(scored_path)
    # scored_from_raw：讀 scored 一律無損還原，否則摘要表格顯示的標題會比
    # data/scored 多套一次 s2twp
    items = [scored_from_raw(item) for item in scored_data]
    print_summary(items)


@app.command(name="list")
def list_posts(
    days: int = typer.Option(7, "--days", "-n", help="顯示最近幾天"),
    post_type: str = typer.Option("all", "--type", "-t", help="類型: all | post | note"),
):
    """列出已生成的部落格文章與筆記。"""
    today = date.today()

    table = Table(title="📚 已生成的內容")
    table.add_column("日期", style="bold", width=12)
    table.add_column("類型", width=7)
    table.add_column("標題", max_width=55)
    table.add_column("分數", width=8)
    table.add_column("來源", width=18)

    count = 0
    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        prefix = d.isoformat()

        entries: list[tuple[str, Path]] = []
        if post_type in ("all", "post"):
            entries += [("📝 post", f) for f in sorted(POSTS_DIR.glob(f"{prefix}*.md"))]
        if post_type in ("all", "note"):
            entries += [("📓 note", f) for f in sorted(NOTES_DIR.glob(f"{prefix}*.md"))]

        for type_label, f in entries:
            frontmatter = _read_frontmatter(f)
            title = frontmatter.get("title", f.stem[11:].replace("-", " "))[:55]
            score = frontmatter.get("score", "—")
            source = frontmatter.get("source", "—")
            table.add_row(str(d), type_label, title, str(score), str(source))
            count += 1

    if count == 0:
        console.print(f"[yellow]最近 {days} 天內無已生成的內容[/yellow]")
    else:
        console.print(table)
        console.print(f"[dim]共 {count} 篇[/dim]")


@app.command()
def show(
    filepath: str = typer.Argument(..., help="文章路徑（output/posts/... 或 output/notes/...）"),
):
    """在終端機中渲染顯示指定文章。"""
    path = Path(filepath)
    if not path.exists():
        console.print(f"[red]✗ 找不到檔案: {filepath}[/red]")
        raise typer.Exit(1)

    content = path.read_text(encoding="utf-8")
    # 移除 YAML frontmatter 後渲染
    if content.startswith("---"):
        end = content.find("\n---\n", 3)
        if end != -1:
            content = content[end + 5:]

    console.rule(f"[bold]{path.name}[/bold]")
    console.print(Markdown(content))


@app.command()
def clean(
    before: str = typer.Option(None, "--before", help="刪除此日期之前的資料 (YYYY-MM-DD)"),
    keep_days: int = typer.Option(None, "--keep-days", help="只保留最近 N 天，刪除更舊的"),
    auto: bool = typer.Option(False, "--auto", help="自動讀取 config 的 retention_days 清理"),
    dry_run: bool = typer.Option(False, "--dry-run", help="只列出不實際刪除"),
):
    """清理歷史資料與輸出檔案。"""
    if auto:
        config = load_config()
        keep_days = config.get("retention_days", 90)

    if before is None and keep_days is None:
        console.print("[red]✗ 請指定 --before 或 --keep-days 或 --auto[/red]")
        raise typer.Exit(1)

    cutoff: date
    if keep_days is not None:
        cutoff = date.today() - timedelta(days=keep_days)
    else:
        cutoff = _parse_date(before)

    console.print(f"[yellow]將清理 {cutoff} 之前的資料...[/yellow]")

    to_delete: list[Path] = []
    for dir_path in [RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR, LISTS_DIR, POSTS_DIR, NOTES_DIR, PROMPTS_DIR]:
        for f in dir_path.glob("*.json" if dir_path in (RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR, LISTS_DIR) else "*.md"):
            try:
                file_date = date.fromisoformat(f.stem[:10])
                if file_date < cutoff:
                    to_delete.append(f)
            except ValueError:
                continue

    if not to_delete:
        console.print("[green]無需清理的檔案[/green]")
        return

    console.print(f"  找到 {len(to_delete)} 個檔案：")
    for f in sorted(to_delete)[:20]:
        console.print(f"  [dim]  {f.relative_to(f.parent.parent.parent)}[/dim]")
    if len(to_delete) > 20:
        console.print(f"  [dim]  ... 以及 {len(to_delete) - 20} 個更多[/dim]")

    if dry_run:
        console.print("[yellow]Dry run — 未實際刪除[/yellow]")
        return

    if not auto and not typer.confirm(f"\n確認刪除 {len(to_delete)} 個檔案？"):
        console.print("取消。")
        return

    for f in to_delete:
        f.unlink()
    console.print(f"[green]✅ 已刪除 {len(to_delete)} 個檔案[/green]")


@app.command()
def status(
    days: int = typer.Option(7, "--days", help="顯示最近幾天"),
):
    """查看最近幾天的 pipeline 執行狀態。"""
    table = Table(title="📅 Pipeline Status")
    table.add_column("Date", style="bold", width=12)
    table.add_column("State", width=12)
    table.add_column("Items", width=8)
    table.add_column("Top-K", width=8)
    table.add_column("Posts", width=8)

    today = date.today()
    for i in range(days, -1, -1):
        d = today - timedelta(days=i)
        state = get_pipeline_state(d)

        items_count = ""
        raw_path = get_raw_path(d)
        if raw_path.exists():
            raw_data = load_json(raw_path)
            items_count = str(len(raw_data)) if isinstance(raw_data, list) else ""

        scored_count = ""
        scored_path = get_scored_path(d)
        if scored_path.exists():
            scored_data = load_json(scored_path)
            scored_count = str(len(scored_data)) if isinstance(scored_data, list) else ""

        prefix = d.isoformat()
        posts_count = str(len(list(POSTS_DIR.glob(f"{prefix}*.md"))))

        state_style = {
            "done": "[green]done[/green]",
            "scored": "[yellow]scored[/yellow]",
            "collected": "[cyan]collected[/cyan]",
            "none": "[dim]none[/dim]",
        }

        table.add_row(
            str(d),
            state_style.get(state, state),
            items_count,
            scored_count,
            posts_count if int(posts_count) > 0 else "",
        )

    console.print(table)


@app.command()
def digest(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD)"),
):
    """生成每日精選摘要（模板式，不需 LLM）。"""
    from src.generators.digest import generate_and_save_digest

    d = _parse_date(target_date)
    scored_path = get_scored_path(d)
    if not scored_path.exists():
        console.print(f"[red]✗ No scored data for {d}. Run 'score' first.[/red]")
        raise typer.Exit(1)

    scored_data = load_json(scored_path)
    # scored_from_raw：digest 是寫檔輸出，重建誤差會直接固化進 output/digests
    items = [scored_from_raw(item) for item in scored_data]

    path = generate_and_save_digest(items, d)
    console.print(f"[bold green]✅ 每日摘要已生成: {path}[/bold green]")


@app.command(name="backfill-votes")
def backfill_votes(
    target_date: str = typer.Option(None, "--date", "-d", help="基準日期 (YYYY-MM-DD), 預設今天"),
    days: int = typer.Option(1, "--days", "-n", help="回補基準日之前 N 天（預設只補前一天）"),
):
    """回補 HF 論文票數並重排當日清單（論文剛發布時票數還沒累積）。"""
    from src.backfill import backfill_recent

    d = _parse_date(target_date)
    results = backfill_recent(d, days=days)
    changed = sum(r["changed"] for r in results)
    if changed == 0:
        console.print("[yellow]沒有票數需要更新（無 raw 資料 / 日期對不上 / 票數未變）[/yellow]")
    else:
        console.print(f"[bold green]✅ 共更新 {changed} 篇論文票數[/bold green]")


@app.command(name="repair-content")
def repair_content(
    days: int = typer.Option(None, "--days", "-n", help="只修最近 N 天（預設全期）"),
    dry_run: bool = typer.Option(
        False, "--dry-run", help="只清點待修規模，不重抓、不連網、不寫檔"
    ),
):
    """修復歷史資料：HF 摘要黏字重抓 + entity 解碼 + 媒體標記剝除 + 簡→繁 + scored 對齊 raw。"""
    from src.repair import repair_all

    stats = repair_all(days=days, dry_run=dry_run)
    color = "yellow" if dry_run else "green"
    if dry_run:
        console.print(f"HF 待修候選 [yellow]{stats['hf_candidates']}[/yellow] 筆")
    else:
        console.print(
            f"HF 重抓成功 [green]{stats['hf_refetched']}[/green] / "
            f"失敗 [yellow]{stats['hf_failed']}[/yellow]"
        )
    # 四個數字的單位一律是「欄位數」（tags 逐個元素算一個），不是「出現次數」——
    # 一個 title 裡有 3 個 entity 只計 1。文案與 `repair_all()` 的統計語意必須一致。
    # 「簡→繁」還包含**沒有任何簡體被轉換**的欄位：`to_traditional_shape_only()`
    # 每次都會順帶套 `utils._TERM_FIXES`（引數→參數 等），實測落地欄位裡有 27 個
    # 純 OpenCC 差異為 0、完全是被 term fixes 改的。詳見
    # `repair._to_traditional_safe()` 的「附帶效果」段。
    console.print(
        f"entity 解碼 [{color}]{stats['entities_fixed']}[/{color}] 欄，"
        f"媒體標記剝除 [{color}]{stats['media_stripped']}[/{color}] 欄，"
        f"簡→繁（含 term fixes）[{color}]{stats['simplified_converted']}[/{color}] 欄，"
        f"scored 對齊 raw [{color}]{stats['scored_backfilled']}[/{color}] 欄"
    )
    if dry_run:
        console.print("[yellow]--dry-run：未連網、未重抓、未寫入任何檔案[/yellow]")
    else:
        console.print(f"寫入 [bold]{stats['files_written']}[/bold] 個檔案")


@app.command(name="analyze-scores")
def analyze_scores(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD), 預設今天"),
    days: int = typer.Option(1, "--days", "-n", help="分析最近 N 天（N>1 輸出趨勢表）"),
):
    """分析評分分佈：統計 / 維度 / 來源 / 離群值 / 漂移偵測。"""
    from src.analysis.score_analysis import (
        compute_day_analysis,
        load_day_items,
        print_multi_day_trend,
        print_single_day_report,
    )
    from datetime import timedelta

    end_date = _parse_date(target_date)
    dates = [end_date - timedelta(days=i) for i in range(days - 1, -1, -1)]

    analyses = []
    for d in dates:
        items = load_day_items(SCORED_DIR, d)
        if not items:
            console.print(f"[yellow]  {d}: 無評分資料，跳過[/yellow]")
            continue
        analyses.append(compute_day_analysis(items, d))

    if not analyses:
        console.print("[yellow]指定範圍內無任何評分資料。[/yellow]")
        raise typer.Exit(0)

    if len(analyses) == 1:
        print_single_day_report(analyses[0], console)
    else:
        print_multi_day_trend(analyses, console)
        console.print()
        for ana in analyses:
            print_single_day_report(ana, console)
            console.print()


@app.command()
def web(
    host: str = typer.Option("127.0.0.1", "--host", help="監聽 host"),
    port: int = typer.Option(8555, "--port", "-p", help="監聽 port"),
    reload: bool = typer.Option(False, "--reload", help="開發模式（自動重載）"),
):
    """啟動內容品質監控網頁。"""
    try:
        import uvicorn
    except ImportError:
        console.print("[red]請先安裝 web 依賴: pip install 'auto-post-blog[web]'[/red]")
        raise typer.Exit(1)
    console.print(f"[bold green]🌐 監控網頁啟動中 → http://{host}:{port}[/bold green]")
    uvicorn.run("src.web.app:app", host=host, port=port, reload=reload)


# ──────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────

def _read_frontmatter(path: Path) -> dict:
    """從 Markdown 檔案讀取 YAML frontmatter 欄位（簡易解析）。"""
    try:
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return {}
        end = content.find("\n---\n", 3)
        if end == -1:
            return {}
        fm_text = content[3:end].strip()
        result: dict = {}
        for line in fm_text.splitlines():
            if ":" in line:
                key, _, val = line.partition(":")
                result[key.strip()] = val.strip().strip('"')
        return result
    except Exception:
        return {}


if __name__ == "__main__":
    app()
