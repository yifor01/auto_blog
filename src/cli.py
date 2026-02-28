"""CLI entry point for auto_post_blog pipeline."""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from src.logger import get_logger, setup_logging
from src.models import ContentItem, ScoredItem
from src.scoring.rules import batch_rule_score
from src.scoring.scorer import batch_llm_score
from src.utils import (
    DIGESTS_DIR,
    NOTES_DIR,
    POSTS_DIR,
    PROMPTS_DIR,
    RAW_DIR,
    SCORED_DIR,
    HEALTH_DIR,
    FEEDBACK_DIR,
    console,
    get_seen_urls,
    load_config,
    save_json,
    load_json,
    today_str,
)

setup_logging()  # 從 AUTOPB_LOG_FORMAT env 自動偵測模式
_logger = get_logger("cli")

app = typer.Typer(
    name="autopb",
    help="Auto Post Blog — AI 新知自動收集 & 部落格素材產出系統",
)


def _get_collectors():
    """Lazy-initialize collectors（只在需要收集時才建立，避免啟動時不必要的 import）。"""
    from src.collectors.arxiv_collector import ArxivCollector
    from src.collectors.blog_collector import BlogCollector
    from src.collectors.chatpaper_collector import ChatPaperCollector
    from src.collectors.github_trending import GitHubTrendingCollector
    from src.collectors.hackernews_collector import HackerNewsCollector
    from src.collectors.hf_papers import HFPapersCollector
    from src.collectors.rss_collector import RSSCollector
    return [
        ArxivCollector(),
        ChatPaperCollector(),
        HFPapersCollector(),
        RSSCollector(),
        BlogCollector(),
        GitHubTrendingCollector(),
        HackerNewsCollector(),
    ]


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
# Resume / 斷點續跑機制
# ──────────────────────────────────────────────────────────

def _get_raw_path(d: date):
    return RAW_DIR / f"{d.isoformat()}.json"


def _get_scored_path(d: date):
    return SCORED_DIR / f"{d.isoformat()}.json"


def _has_posts(d: date) -> bool:
    """檢查該日期是否已有生成的 blog posts。"""
    prefix = d.isoformat()
    return any(f.name.startswith(prefix) for f in POSTS_DIR.glob("*.md"))


def _clear_outputs(d: date) -> None:
    """清除指定日期的所有輸出檔案（posts, notes, prompts）。"""
    prefix = d.isoformat()
    cleared = 0
    for dir_path in [POSTS_DIR, NOTES_DIR, PROMPTS_DIR]:
        for f in dir_path.glob(f"{prefix}*.md"):
            f.unlink()
            console.print(f"  🗑️  刪除 {f.name}")
            cleared += 1
    if cleared == 0:
        console.print("  （無已生成的輸出檔案）")


def _get_pipeline_state(d: date) -> str:
    """檢查 pipeline 對指定日期的完成狀態。

    Returns:
        "none"      — 尚未開始
        "collected" — 已收集 raw data
        "scored"    — 已完成篩選
        "done"      — 已生成 posts + notes
    """
    if _has_posts(d):
        return "done"
    if _get_scored_path(d).exists():
        return "scored"
    if _get_raw_path(d).exists():
        return "collected"
    return "none"


# ──────────────────────────────────────────────────────────
# Pipeline stages
# ──────────────────────────────────────────────────────────

def _collect(target_date: date | None = None) -> list[ContentItem]:
    """執行所有 collectors 並去重（含跨日去重）。支援斷點續跑。"""
    target_date = target_date or date.today()
    raw_path = _get_raw_path(target_date)

    if raw_path.exists():
        console.print(
            f"[cyan]♻️  已存在 {raw_path.name}, 跳過收集 (使用快取)[/cyan]"
        )
        raw_data = load_json(raw_path)
        return [ContentItem(**item) for item in raw_data]

    console.rule(f"[bold blue]📡 收集階段 — {target_date}[/bold blue]")

    import time
    all_items: list[ContentItem] = []
    health_data = {}

    for collector in _get_collectors():
        start_time = time.time()
        try:
            items = collector.collect(target_date)
            all_items.extend(items)
            health_data[collector.name] = {
                "status": "success",
                "count": len(items),
                "duration": round(time.time() - start_time, 2)
            }
        except Exception as e:
            _logger.error("Collector failed", extra={"collector": collector.name, "error": str(e)})
            console.print(f"[red]✗ {collector.name} failed: {e}[/red]")
            health_data[collector.name] = {
                "status": "error",
                "error": str(e),
                "duration": round(time.time() - start_time, 2)
            }
            
    # Save health data
    save_json(health_data, HEALTH_DIR / f"{target_date.isoformat()}.json")

    # 單日去重
    seen: set[str] = set()
    unique: list[ContentItem] = []
    for item in all_items:
        key = item.dedup_key()
        if key not in seen:
            seen.add(key)
            unique.append(item)

    console.print(
        f"\n[bold]📊 單日去重: {len(all_items)} total → {len(unique)} unique[/bold]"
    )

    # 跨日去重
    config = load_config()
    lookback_days = config.get("dedup", {}).get("lookback_days", 0)
    if lookback_days > 0:
        cross_day_seen = get_seen_urls(exclude_date=target_date, lookback_days=lookback_days)
        before = len(unique)
        unique = [item for item in unique if item.dedup_key() not in cross_day_seen]
        skipped = before - len(unique)
        if skipped > 0:
            console.print(
                f"[cyan]🔄 跨日去重 (回看 {lookback_days} 天): 排除 {skipped} 筆重複 → {len(unique)} unique[/cyan]"
            )

    _logger.info("Collection complete", extra={"unique_items": len(unique), "date": str(target_date)})
    console.print(f"[bold green]✅ 最終收集: {len(unique)} items[/bold green]")

    save_json([item.model_dump() for item in unique], raw_path)
    console.print(f"💾 Raw data saved: {raw_path.name}")

    return unique


def _score(items: list[ContentItem], target_date: date | None = None) -> list[ScoredItem]:
    """Rule-based 預篩 + LLM 深度評分。支援斷點續跑。"""
    target_date = target_date or date.today()
    scored_path = _get_scored_path(target_date)

    if scored_path.exists():
        console.print(
            f"[cyan]♻️  已存在 {scored_path.name}, 跳過篩選 (使用快取)[/cyan]"
        )
        scored_data = load_json(scored_path)
        return [ScoredItem(**item) for item in scored_data]

    console.rule("[bold blue]🔍 篩選階段[/bold blue]")
    config = load_config()

    rule_passed = batch_rule_score(items, config)
    top_items = batch_llm_score(rule_passed, config)

    save_json([item.model_dump() for item in top_items], scored_path)

    return top_items


def _generate(top_items: list[ScoredItem], target_date: date | None = None) -> tuple[list[str], list[str]]:
    """生成 blog posts 和 notes。已生成則跳過。"""
    from src.generators.blog_post import generate_and_save_posts
    from src.generators.note import generate_and_save_notes

    target_date = target_date or date.today()

    if _has_posts(target_date):
        console.print(
            f"[cyan]♻️  {target_date} 已有生成結果, 跳過生成[/cyan]"
        )
        prefix = target_date.isoformat()
        existing = [str(f) for f in POSTS_DIR.glob(f"{prefix}*.md")]
        return existing, []

    console.rule("[bold blue]✍️ 生成階段[/bold blue]")

    post_paths = generate_and_save_posts(top_items, target_date)
    note_paths = generate_and_save_notes(top_items, target_date)

    return post_paths, note_paths


# ──────────────────────────────────────────────────────────
# CLI Commands
# ──────────────────────────────────────────────────────────

@app.command()
def run(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD), 預設今天"),
    dry_run: bool = typer.Option(False, "--dry-run", help="只收集和篩選，不生成內容"),
    top_k: int = typer.Option(None, "--top-k", "-k", help="覆蓋 config 中的 final_top_k"),
    force: bool = typer.Option(False, "--force", "-f", help="強制重新執行, 清除所有快取與生成結果"),
):
    """完整 pipeline: 收集 → 篩選 → 生成 (支援斷點續跑)"""
    d = _parse_date(target_date)
    state = _get_pipeline_state(d)
    console.rule(f"[bold magenta]🚀 Auto Post Blog — {d}[/bold magenta]")
    console.print(f"  📌 Pipeline 狀態: [bold]{state}[/bold]")

    # --force: 清除所有快取與輸出（含 posts/notes/prompts）
    if force:
        console.print("[yellow]🔄 --force: 清除所有快取與生成結果, 重新執行[/yellow]")
        for p in [_get_raw_path(d), _get_scored_path(d)]:
            if p.exists():
                p.unlink()
                console.print(f"  🗑️  刪除 {p.name}")
        _clear_outputs(d)

    if state == "done" and not force:
        console.print(f"[green]✅ {d} 已完成所有階段, 不需重跑 (用 --force 強制重跑)[/green]")
        return

    items = _collect(d)
    if not items:
        _logger.warning("No items collected", extra={"date": str(d)})
        console.print("[yellow]⚠ No items collected. Exiting.[/yellow]")
        return

    top_items = _score(items, d)
    if top_k:
        top_items = top_items[:top_k]

    if dry_run:
        console.print("\n[yellow]🏁 Dry run 完成 — 跳過內容生成[/yellow]")
        _print_summary(top_items)
        return

    if not top_items:
        _logger.warning("No items passed scoring", extra={"date": str(d)})
        console.print("[yellow]⚠ No items passed scoring. Exiting.[/yellow]")
        return

    post_paths, note_paths = _generate(top_items, d)

    console.rule("[bold green]📋 每日報告[/bold green]")
    console.print(f"  📡 收集: {len(items)} unique items")
    console.print(f"  🏆 Top-{len(top_items)} selected")
    console.print(f"  📝 Blog posts: {len(post_paths)}")
    console.print(f"  📓 Notes: {len(note_paths)}")
    for p in post_paths:
        console.print(f"    → {p}")


@app.command()
def catchup(
    days: int = typer.Option(7, "--days", help="回補最近幾天"),
    dry_run: bool = typer.Option(False, "--dry-run", help="只收集和篩選"),
):
    """補跑缺失的日期 (開機後自動補跑)。"""
    today = date.today()
    console.rule("[bold magenta]🔄 Catch-up 補跑模式[/bold magenta]")

    missed: list[date] = []
    for i in range(days, 0, -1):
        d = today - timedelta(days=i)
        state = _get_pipeline_state(d)
        if state != "done":
            missed.append(d)
            console.print(f"  📅 {d} — 狀態: {state}")

    if not missed:
        console.print(f"[green]✅ 最近 {days} 天都已完成, 不需補跑[/green]")
        return

    console.print(f"\n[cyan]需補跑 {len(missed)} 天: {', '.join(str(d) for d in missed)}[/cyan]\n")

    for d in missed:
        console.rule(f"[bold blue]補跑 {d}[/bold blue]")
        try:
            items = _collect(d)
            if not items:
                continue
            top_items = _score(items, d)
            if dry_run or not top_items:
                continue
            _generate(top_items, d)
        except Exception as e:
            _logger.error("Catchup failed", extra={"date": str(d), "error": str(e)})
            console.print(f"[red]✗ {d} 補跑失敗: {e}[/red]")


@app.command()
def collect(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD)"),
    force: bool = typer.Option(False, "--force", "-f", help="強制重新收集"),
):
    """只收集資料 (已有快取則跳過)。"""
    d = _parse_date(target_date)
    if force and _get_raw_path(d).exists():
        _get_raw_path(d).unlink()
    _collect(d)


@app.command()
def score(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期 (YYYY-MM-DD)"),
    force: bool = typer.Option(False, "--force", "-f", help="強制重新篩選"),
):
    """對已收集的資料進行篩選 (已有快取則跳過)。"""
    d = _parse_date(target_date)
    raw_path = _get_raw_path(d)
    if not raw_path.exists():
        console.print(f"[red]✗ No raw data for {d}. Run 'collect' first.[/red]")
        raise typer.Exit(1)

    if force and _get_scored_path(d).exists():
        _get_scored_path(d).unlink()

    raw_data = load_json(raw_path)
    items = [ContentItem(**item) for item in raw_data]
    _score(items, d)


@app.command()
def generate(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期"),
    top_k: int = typer.Option(None, "--top-k", "-k", help="生成數量，預設使用 config 的 final_top_k"),
):
    """對已篩選的 top items 生成內容。"""
    d = _parse_date(target_date)
    scored_path = _get_scored_path(d)
    if not scored_path.exists():
        console.print(f"[red]✗ No scored data for {d}. Run 'score' first.[/red]")
        raise typer.Exit(1)

    scored_data = load_json(scored_path)
    limit = top_k or len(scored_data)
    top_items = [ScoredItem(**item) for item in scored_data[:limit]]
    _generate(top_items, d)


@app.command()
def summary(
    target_date: str = typer.Option(None, "--date", "-d", help="目標日期"),
):
    """查看今日評分摘要。"""
    d = _parse_date(target_date)
    scored_path = _get_scored_path(d)
    if not scored_path.exists():
        console.print(f"[yellow]No scored data for {d}[/yellow]")
        return

    scored_data = load_json(scored_path)
    items = [ScoredItem(**item) for item in scored_data]
    _print_summary(items)


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
    for dir_path in [RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR, POSTS_DIR, NOTES_DIR, PROMPTS_DIR]:
        for f in dir_path.glob("*.json" if dir_path in (RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR) else "*.md"):
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
        state = _get_pipeline_state(d)

        items_count = ""
        raw_path = _get_raw_path(d)
        if raw_path.exists():
            raw_data = load_json(raw_path)
            items_count = str(len(raw_data)) if isinstance(raw_data, list) else ""

        scored_count = ""
        scored_path = _get_scored_path(d)
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
    scored_path = _get_scored_path(d)
    if not scored_path.exists():
        console.print(f"[red]✗ No scored data for {d}. Run 'score' first.[/red]")
        raise typer.Exit(1)

    scored_data = load_json(scored_path)
    items = [ScoredItem(**item) for item in scored_data]

    path = generate_and_save_digest(items, d)
    console.print(f"[bold green]✅ 每日摘要已生成: {path}[/bold green]")


@app.command()
def web(
    host: str = typer.Option("127.0.0.1", "--host", help="監聽 host"),
    port: int = typer.Option(8080, "--port", "-p", help="監聽 port"),
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

def _print_summary(items: list[ScoredItem]) -> None:
    table = Table(title="🏆 Top Items")
    table.add_column("#", style="dim", width=3)
    table.add_column("Score", style="bold", width=8)
    table.add_column("Source", width=15)
    table.add_column("Title", max_width=50)
    table.add_column("Reason", max_width=40)

    for i, item in enumerate(items, 1):
        table.add_row(
            str(i),
            f"{item.total_score:.0f}",
            item.item.source_name,
            item.item.title[:50],
            (item.llm_reason or ", ".join(item.rule_reasons))[:40],
        )

    console.print(table)


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
