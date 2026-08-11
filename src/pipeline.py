"""Pipeline 業務邏輯（收集 → 篩選 → 生成）。

CLI (`src/cli.py`) 只負責參數解析，實際的 pipeline 編排、checkpoint 機制、
collectors lazy init、增量評分與跨日去重都集中在此模組。

公開介面：
    路徑 / 狀態 helper：
        get_raw_path / get_scored_path / has_posts / clear_outputs / get_pipeline_state
    Collectors：
        get_collectors / COLLECTOR_SOURCE_MAP
    階段函式（含 console 輸出，行為與原 CLI 完全一致）：
        collect_items / supplement_items / score_items / score_incremental / generate_posts
    高階編排（對應 CLI 指令）：
        run_pipeline / run_supplement / run_catchup / run_collect / run_score / run_generate
    報表：
        print_summary
"""

from __future__ import annotations

from datetime import date, timedelta

import typer
from rich.table import Table

from src.lists import LIST_SOURCES, build_lists, get_lists_path
from src.logger import get_logger
from src.models import ContentItem, ScoredItem, SourceType, item_from_raw, scored_from_raw
from src.pinned import select_pinned, to_pinned_scored
from src.scoring.rules import batch_rule_score
from src.scoring.scorer import batch_llm_score
from src.utils import (
    HEALTH_DIR,
    POSTS_DIR,
    PROMPTS_DIR,
    RAW_DIR,
    SCORED_DIR,
    console,
    get_seen_urls,
    load_config,
    load_json,
    save_json,
)

_logger = get_logger("pipeline")


# ──────────────────────────────────────────────────────────
# Collectors lazy init（新 collector 在這裡註冊）
# ──────────────────────────────────────────────────────────

def get_collectors():
    """Lazy-initialize collectors（只在需要收集時才建立，避免啟動時不必要的 import）。"""
    from src.collectors.arxiv_collector import ArxivCollector
    from src.collectors.blog_collector import BlogCollector
    from src.collectors.chatpaper_collector import ChatPaperCollector
    from src.collectors.cn_labs_collector import CNLabsCollector
    from src.collectors.github_trending import GitHubTrendingCollector
    from src.collectors.hackernews_collector import HackerNewsCollector
    from src.collectors.hf_papers import HFPapersCollector
    from src.collectors.newsapi_collector import NewsAPICollector
    from src.collectors.reddit_collector import RedditCollector
    from src.collectors.rss_collector import RSSCollector
    from src.collectors.semantic_scholar import SemanticScholarCollector
    return [
        # HF 在 arXiv 前：單日去重「先收集者留」，同論文優先保留帶 upvotes 的 HF 版
        HFPapersCollector(),
        ArxivCollector(),
        ChatPaperCollector(),
        RSSCollector(),
        BlogCollector(),
        CNLabsCollector(),
        GitHubTrendingCollector(),
        HackerNewsCollector(),
        RedditCollector(),
        NewsAPICollector(),
        SemanticScholarCollector(),
    ]


# Collector → SourceType 對應表（用於 supplement 偵測缺失 source）
COLLECTOR_SOURCE_MAP: dict[str, SourceType] = {
    "arxiv": SourceType.ARXIV,
    "chatpaper": SourceType.CHATPAPER,
    "hf_papers": SourceType.HF_PAPERS,
    "rss": SourceType.RSS,
    "blogs": SourceType.BLOG,
    "cn_labs": SourceType.CN_LABS,
    "github": SourceType.GITHUB,
    "hackernews": SourceType.HACKERNEWS,
    "reddit": SourceType.REDDIT,
    "newsapi": SourceType.NEWSAPI,
    "semantic_scholar": SourceType.SEMANTIC_SCHOLAR,
}


# ──────────────────────────────────────────────────────────
# Resume / 斷點續跑機制：路徑與狀態 helper
# ──────────────────────────────────────────────────────────

def get_raw_path(d: date):
    return RAW_DIR / f"{d.isoformat()}.json"


def get_scored_path(d: date):
    return SCORED_DIR / f"{d.isoformat()}.json"


def has_posts(d: date) -> bool:
    """檢查該日期是否已有生成的 blog posts。"""
    prefix = d.isoformat()
    return any(f.name.startswith(prefix) for f in POSTS_DIR.glob("*.md"))


def clear_outputs(d: date) -> None:
    """清除指定日期的 prompts。Posts 保留（force 重跑只補生成新的，不刪舊文章）。"""
    prefix = d.isoformat()
    cleared = 0
    for dir_path in [PROMPTS_DIR]:
        for f in dir_path.glob(f"{prefix}*.md"):
            f.unlink()
            console.print(f"  🗑️  刪除 {f.name}")
            cleared += 1
    if cleared == 0:
        console.print("  （無需清除的輸出檔案）")


def get_pipeline_state(d: date) -> str:
    """檢查 pipeline 對指定日期的完成狀態。

    Returns:
        "none"      — 尚未開始
        "collected" — 已收集 raw data
        "scored"    — 已完成篩選
        "done"      — 已生成 posts + notes
    """
    if has_posts(d):
        return "done"
    if get_scored_path(d).exists():
        return "scored"
    if get_raw_path(d).exists():
        return "collected"
    return "none"


# ──────────────────────────────────────────────────────────
# Pipeline stages
# ──────────────────────────────────────────────────────────

def collect_items(target_date: date | None = None) -> list[ContentItem]:
    """執行所有 collectors 並去重（含跨日去重）。支援斷點續跑。"""
    target_date = target_date or date.today()
    raw_path = get_raw_path(target_date)

    if raw_path.exists():
        console.print(
            f"[cyan]♻️  已存在 {raw_path.name}, 跳過收集 (使用快取)[/cyan]"
        )
        raw_data = load_json(raw_path)
        # item_from_raw：checkpoint 續跑時不重複套用 Layer A 的 s2twp，否則
        # 這批 items 餵給 build_lists() 產出的 output/lists 會比 data/raw 多漂一格
        return [item_from_raw(item) for item in raw_data]

    console.rule(f"[bold blue]📡 收集階段 — {target_date}[/bold blue]")

    import time
    all_items: list[ContentItem] = []
    health_data = {}

    for collector in get_collectors():
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

    # 不 cache 空結果：所有 collector 同時失敗（網路/限流）多半是 transient，
    # 若寫成 [] 會被 checkpoint 當「已完成」永久卡住，只能 --force 解。空結果直接回傳、
    # 不留 cache，下次 run 會重試。
    if unique:
        save_json([item.model_dump() for item in unique], raw_path)
        console.print(f"💾 Raw data saved: {raw_path.name}")
    else:
        _logger.warning("收集結果為空，跳過寫入 cache（避免 transient 失敗被永久快取）")
        console.print("[yellow]⚠️  收集結果為空，不寫入 cache（下次 run 會重試）[/yellow]")

    return unique


def supplement_items(target_date: date | None = None) -> tuple[list[ContentItem], bool]:
    """補收現有 raw data 中缺失的 source，回傳 (items, changed)。

    - raw 不存在 → fallback 到完整 collect_items()
    - 所有 source 皆在 → 回傳快取，changed=False
    - 有缺失 → 只跑缺失 collector → 合併去重 → 覆寫 raw
    """
    target_date = target_date or date.today()
    raw_path = get_raw_path(target_date)

    if not raw_path.exists():
        return collect_items(target_date), True

    raw_data = load_json(raw_path)
    # item_from_raw：重建既有項目時不重複套用 Layer A 的 s2twp（s2twp 對繁體不
    # 冪等，「這個文件的參數」→「這個檔案的參數」），否則這批 items 餵給
    # build_lists() 產出的 output/lists 會比 data/raw 多漂一格
    existing_items = [item_from_raw(item) for item in raw_data]
    # 寫回 raw 時用的 payload（與 existing_items 同索引）。既有項目一律沿用原始
    # dict，不能用 model_dump()：每次 --supplement 覆寫整份 raw，任何重建誤差
    # 都會被固化進存檔。
    payload: list[dict] = list(raw_data)
    present_sources = {item.source for item in existing_items}

    all_collectors = get_collectors()
    missing = [
        c for c in all_collectors
        if COLLECTOR_SOURCE_MAP.get(c.name) not in present_sources
    ]

    if not missing:
        console.print(f"[cyan]♻️  {raw_path.name} 已包含所有 source，無需補收[/cyan]")
        return existing_items, False

    missing_names = [c.name for c in missing]
    console.rule(f"[bold blue]🔄 補收缺失 source — {target_date}[/bold blue]")
    console.print(f"  缺失: [yellow]{', '.join(missing_names)}[/yellow]")

    import time
    new_items: list[ContentItem] = []
    for collector in missing:
        start_time = time.time()
        try:
            items = collector.collect(target_date)
            new_items.extend(items)
            console.print(
                f"  [green]✓ {collector.name}: {len(items)} items "
                f"({time.time() - start_time:.1f}s)[/green]"
            )
        except Exception as e:
            _logger.error("Supplement collector failed",
                         extra={"collector": collector.name, "error": str(e)})
            console.print(f"  [red]✗ {collector.name} failed: {e}[/red]")

    if not new_items:
        console.print("[cyan]  補收來源無新項目[/cyan]")
        return existing_items, False

    # 單日去重合併
    seen = {item.dedup_key() for item in existing_items}
    added = 0
    for item in new_items:
        key = item.dedup_key()
        if key not in seen:
            seen.add(key)
            existing_items.append(item)
            # 新收項目沒有對應的原始 dict，序列化是唯一來源（也是它第一次落地）
            payload.append(item.model_dump())
            added += 1

    # 跨日去重
    config = load_config()
    lookback_days = config.get("dedup", {}).get("lookback_days", 0)
    if lookback_days > 0 and added > 0:
        cross_day_seen = get_seen_urls(exclude_date=target_date, lookback_days=lookback_days)
        before = len(existing_items)
        # payload 與 existing_items 必須一起篩，否則兩邊索引錯位、寫回的內容會張冠李戴
        kept = [
            (raw, item)
            for raw, item in zip(payload, existing_items)
            if item.dedup_key() not in cross_day_seen
        ]
        payload = [raw for raw, _ in kept]
        existing_items = [item for _, item in kept]
        skipped = before - len(existing_items)
        if skipped > 0:
            console.print(
                f"  [cyan]🔄 跨日去重: 排除 {skipped} 筆 → {len(existing_items)}[/cyan]"
            )

    save_json(payload, raw_path)
    console.print(f"[bold green]✅ 補收完成: +{added} 新項目 (總計 {len(existing_items)})[/bold green]")

    return existing_items, added > 0


def score_incremental(
    all_items: list[ContentItem],
    target_date: date,
) -> list[ScoredItem]:
    """增量評分：只對新項目評分，與既有 scored 合併排名。"""
    scored_path = get_scored_path(target_date)

    if not scored_path.exists():
        # 無既有 scored → 走正常全量評分
        return score_items(all_items, target_date)

    scored_data = load_json(scored_path)
    # scored_from_raw：這裡是讀-改-寫，直接 ScoredItem(**item) 會讓每次
    # --supplement 都把 Layer A 的 s2twp 再套一輪並寫回，漂移就此永久固化
    # （Web Monitor 啟動時對當天自動走 --supplement，開一次 dashboard 就一次）
    existing_scored = [scored_from_raw(item) for item in scored_data]
    scored_urls = {si.item.dedup_key() for si in existing_scored}

    # 找出新增的 items
    new_items = [item for item in all_items if item.dedup_key() not in scored_urls]
    # 清單來源不評分（拿不到全文，評分不可靠；已由 lists stage 呈現）；
    # pinned 官方 blog 也繞過評分直接生成，故從評分 pool 剔除
    config = load_config()
    pinned_keys = {it.dedup_key() for it in select_pinned(all_items, target_date, config)}
    new_items = [
        it for it in new_items
        if it.source not in LIST_SOURCES and it.dedup_key() not in pinned_keys
    ]

    if not new_items:
        console.print(f"[cyan]♻️  無新項目需要評分[/cyan]")
        return existing_scored

    console.rule(f"[bold blue]🔍 增量評分 — {len(new_items)} 新項目[/bold blue]")

    # 只對新項目跑 rule + LLM scoring
    new_rule_passed = batch_rule_score(new_items, config)
    new_scored = batch_llm_score(new_rule_passed, config) if new_rule_passed else []

    # 合併排名。(寫回 payload, ScoredItem) 成對搬移：既有項目一律沿用原始 dict，
    # 不能用 model_dump()——重建誤差（Layer A 二次套用、欄位預設值變動）會被這次
    # 覆寫固化進 data/scored。新評分項目沒有原始 dict，序列化是唯一來源。
    pairs: list[tuple[dict, ScoredItem]] = [
        *zip(scored_data, existing_scored),
        *((si.model_dump(), si) for si in new_scored),
    ]
    pairs.sort(key=lambda p: p[1].total_score, reverse=True)
    final_top_k = config.get("scoring", {}).get("final_top_k", 30)
    pairs = pairs[:final_top_k]
    merged = [si for _, si in pairs]

    save_json([payload for payload, _ in pairs], scored_path)
    console.print(
        f"[bold green]✅ 增量評分完成: +{len(new_scored)} 新評分項目, "
        f"最終 top-{len(merged)}[/bold green]"
    )

    return merged


def score_items(items: list[ContentItem], target_date: date | None = None) -> list[ScoredItem]:
    """Rule-based 預篩 + LLM 深度評分。支援斷點續跑。"""
    target_date = target_date or date.today()
    scored_path = get_scored_path(target_date)

    if scored_path.exists():
        console.print(
            f"[cyan]♻️  已存在 {scored_path.name}, 跳過篩選 (使用快取)[/cyan]"
        )
        scored_data = load_json(scored_path)
        # scored_from_raw：checkpoint 續跑時不重複套用 Layer A 的 s2twp，否則
        # 這批 ScoredItem 產出的 posts / digest 會比 data/scored 多漂一格
        return [scored_from_raw(item) for item in scored_data]

    console.rule("[bold blue]🔍 篩選階段[/bold blue]")
    config = load_config()

    # 清單來源不評分；pinned 官方 blog 繞過評分直接生成（generate 階段處理）
    pinned_keys = {it.dedup_key() for it in select_pinned(items, target_date, config)}
    before = len(items)
    items = [
        it for it in items
        if it.source not in LIST_SOURCES and it.dedup_key() not in pinned_keys
    ]
    if before != len(items):
        console.print(f"[dim]📋 清單/置頂來源不評分: {before} → {len(items)} items[/dim]")

    rule_passed = batch_rule_score(items, config)
    top_items = batch_llm_score(rule_passed, config)

    # 不 cache 空結果：空評分多半是 LLM 全數 429/失敗的 transient 狀況，
    # 寫成 [] 會被 checkpoint 永久卡住。空結果不留 cache，下次 run 會重試。
    if top_items:
        save_json([item.model_dump() for item in top_items], scored_path)
    else:
        _logger.warning("評分結果為空，跳過寫入 cache（避免 transient 失敗被永久快取）")
        console.print("[yellow]⚠️  評分結果為空，不寫入 cache（下次 run 會重試）[/yellow]")

    return top_items


def generate_posts(top_items: list[ScoredItem], target_date: date | None = None) -> list[str]:
    """生成 blog posts：先置頂官方 blog（免評分），再生成評分 top-K。"""
    from src.generators.blog_post import generate_and_save_posts

    target_date = target_date or date.today()

    console.rule("[bold blue]✍️ 生成階段[/bold blue]")

    pinned_paths = _generate_pinned_posts(target_date)
    paths = generate_and_save_posts(top_items, target_date)
    return pinned_paths + paths


def _generate_pinned_posts(target_date: date) -> list[str]:
    """頂尖 AI 公司官方 blog 免評分直接生成（逐篇 checkpoint：已有同名 post 跳過）。"""
    from src.generators.blog_post import generate_and_save_posts
    from src.utils import slugify

    raw_path = get_raw_path(target_date)
    if not raw_path.exists():
        return []

    config = load_config()
    # item_from_raw：讀 raw 一律無損還原，否則 pinned post 的 slug 與內文
    # 會比 data/raw 多套一次 s2twp
    items = [item_from_raw(r) for r in load_json(raw_path)]
    todo = []
    for it in select_pinned(items, target_date, config):
        post_path = POSTS_DIR / f"{target_date.isoformat()}_{slugify(it.title)}.md"
        if post_path.exists():
            continue
        todo.append(to_pinned_scored(it))

    if not todo:
        return []

    console.print(f"[bold]📌 置頂生成: {len(todo)} 篇頂尖 AI 公司官方發布[/bold]")
    paths = generate_and_save_posts(todo, target_date, pinned=True)
    if len(paths) < len(todo):
        _logger.warning(
            "部分置頂文章生成失敗",
            extra={"expected": len(todo), "generated": len(paths)},
        )
    return paths


# ──────────────────────────────────────────────────────────
# 報表 helper
# ──────────────────────────────────────────────────────────

def print_summary(items: list[ScoredItem]) -> None:
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


# ──────────────────────────────────────────────────────────
# 高階編排（對應 CLI 指令）
# ──────────────────────────────────────────────────────────

def run_supplement(d: date, dry_run: bool = False, top_k: int | None = None) -> None:
    """Supplement 模式：補收 → 增量評分 → 生成。"""
    import time as _time

    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "collect", "stage_action": "start"})
    items, changed = supplement_items(d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "collect", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(items),
    })

    if not items:
        console.print("[yellow]⚠ No items. Exiting.[/yellow]")
        return

    build_lists(items, d, force=changed)  # 補收有新項目時重建清單

    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "score", "stage_action": "start"})
    if changed:
        top_items = score_incremental(items, d)
    else:
        top_items = score_items(items, d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "score", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(top_items),
    })

    if top_k:
        top_items = top_items[:top_k]

    if dry_run:
        console.print("\n[yellow]🏁 Dry run 完成 — 跳過內容生成[/yellow]")
        print_summary(top_items)
        return

    # 置頂官方 blog 免評分，不受評分結果或 changed/has_posts gate block（spec §5）：
    # 即使 top_items 為空（429 風暴/門檻日）也要生成最重要的置頂內容。
    # 逐篇 checkpoint，下方 generate_posts 若再呼叫會全數跳過，無副作用。
    _generate_pinned_posts(d)

    if not top_items:
        console.print("[yellow]⚠ No items passed scoring. Exiting.[/yellow]")
        return

    # 有新評分項目或尚未生成 posts → 生成
    if changed or not has_posts(d):
        _t0 = _time.time()
        _logger.info("Stage started", extra={"pipeline_stage": "generate", "stage_action": "start"})
        post_paths = generate_posts(top_items, d)
        _logger.info("Stage ended", extra={
            "pipeline_stage": "generate", "stage_action": "end",
            "elapsed": round(_time.time() - _t0, 1),
            "item_count": len(post_paths),
        })
    else:
        console.print(f"[green]✅ {d} 無新項目且已有 posts, 跳過生成[/green]")


def run_pipeline(
    d: date,
    dry_run: bool = False,
    top_k: int | None = None,
    force: bool = False,
    supplement: bool = False,
) -> None:
    """完整 pipeline: 收集 → 篩選 → 生成 (支援斷點續跑)。"""
    state = get_pipeline_state(d)
    console.rule(f"[bold magenta]🚀 Auto Post Blog — {d}[/bold magenta]")
    console.print(f"  📌 Pipeline 狀態: [bold]{state}[/bold]")

    # LLM 健康度改採 lazy retire：不再起頭 probe 全部 model（白燒 5-7 次請求），
    # 改為呼叫時遇 404 / 上游 429 即將該 model 加入本次 run 的 retired set 跳過；
    # chain 全空時 llm_chat 內部一次性 auto-discover 自救。
    console.print("  🩺 LLM 健康度採 lazy retire（404 / 上游 429 即本次 run 跳過該 model）")

    # --force: 清除所有快取與輸出（含 posts/notes/prompts）
    if force:
        console.print("[yellow]🔄 --force: 清除所有快取與生成結果, 重新執行[/yellow]")
        for p in [get_raw_path(d), get_scored_path(d), get_lists_path(d)]:
            if p.exists():
                p.unlink()
                console.print(f"  🗑️  刪除 {p.name}")
        clear_outputs(d)

    # --supplement: 補收缺失 source + 增量評分
    if supplement and not force:
        return run_supplement(d, dry_run, top_k)

    if state == "done" and not force:
        console.print(f"[green]✅ {d} 已完成所有階段, 不需重跑 (用 --force 強制重跑)[/green]")
        return

    import time as _time

    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "collect", "stage_action": "start"})
    items = collect_items(d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "collect", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(items),
    })
    if not items:
        _logger.warning("No items collected", extra={"date": str(d)})
        console.print("[yellow]⚠ No items collected. Exiting.[/yellow]")
        return

    # 清單型來源（Trending/Papers）每日清單（零 LLM）——collect 後即產出
    build_lists(items, d)

    # 前一天的論文票數此時才沉澱下來，回頭補一次並重排（單次 HTTP，失敗不影響本次 run）
    try:
        from src.backfill import backfill_recent

        backfill_recent(d, days=1)
    except Exception as e:
        _logger.warning("Upvote backfill failed", extra={"date": str(d), "error": str(e)})

    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "score", "stage_action": "start"})
    top_items = score_items(items, d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "score", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(top_items),
    })
    if top_k:
        top_items = top_items[:top_k]

    if dry_run:
        console.print("\n[yellow]🏁 Dry run 完成 — 跳過內容生成[/yellow]")
        print_summary(top_items)
        return

    # 置頂官方 blog 免評分，不受評分結果 block（spec §5）：即使 top_items 為空也要生成。
    # 逐篇 checkpoint，下方 generate_posts 若再呼叫會全數跳過，無副作用。
    _generate_pinned_posts(d)

    if not top_items:
        _logger.warning("No items passed scoring", extra={"date": str(d)})
        console.print("[yellow]⚠ No items passed scoring. Exiting.[/yellow]")
        return

    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "generate", "stage_action": "start"})
    post_paths = generate_posts(top_items, d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "generate", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(post_paths),
    })

    console.rule("[bold green]📋 每日報告[/bold green]")
    console.print(f"  📡 收集: {len(items)} unique items")
    console.print(f"  🏆 Top-{len(top_items)} selected")
    console.print(f"  📝 Blog posts: {len(post_paths)}")
    for p in post_paths:
        console.print(f"    → {p}")


def run_catchup(days: int = 7, dry_run: bool = False) -> None:
    """補跑缺失的日期 (開機後自動補跑)。"""
    today = date.today()
    console.rule("[bold magenta]🔄 Catch-up 補跑模式[/bold magenta]")

    missed: list[date] = []
    for i in range(days, 0, -1):
        d = today - timedelta(days=i)
        state = get_pipeline_state(d)
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
            items = collect_items(d)
            if not items:
                continue
            build_lists(items, d)
            top_items = score_items(items, d)
            if dry_run:
                continue
            # 置頂官方 blog 免評分，即使無評分項目也要生成（spec §5）
            _generate_pinned_posts(d)
            if not top_items:
                continue
            generate_posts(top_items, d)
        except Exception as e:
            _logger.error("Catchup failed", extra={"date": str(d), "error": str(e)})
            console.print(f"[red]✗ {d} 補跑失敗: {e}[/red]")


def run_collect(d: date, force: bool = False) -> list[ContentItem]:
    """只收集資料 (已有快取則跳過)。"""
    import time as _time

    if force and get_raw_path(d).exists():
        get_raw_path(d).unlink()
    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "collect", "stage_action": "start"})
    items = collect_items(d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "collect", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(items),
    })
    if items:
        build_lists(items, d, force=force)
    return items


def run_score(d: date, force: bool = False) -> list[ScoredItem]:
    """對已收集的資料進行篩選 (已有快取則跳過)。"""
    import time as _time

    raw_path = get_raw_path(d)
    if not raw_path.exists():
        console.print(f"[red]✗ No raw data for {d}. Run 'collect' first.[/red]")
        raise typer.Exit(1)

    if force and get_scored_path(d).exists():
        get_scored_path(d).unlink()

    raw_data = load_json(raw_path)
    # item_from_raw：讀 raw 一律無損還原，否則寫出的 data/scored 會比
    # data/raw 多套一次 s2twp
    items = [item_from_raw(item) for item in raw_data]
    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "score", "stage_action": "start"})
    scored = score_items(items, d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "score", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(scored),
    })
    return scored


def run_generate(d: date, top_k: int | None = None) -> list[str]:
    """對已篩選的 top items 生成內容。"""
    import time as _time

    scored_path = get_scored_path(d)
    if not scored_path.exists():
        console.print(f"[red]✗ No scored data for {d}. Run 'score' first.[/red]")
        raise typer.Exit(1)

    scored_data = load_json(scored_path)
    limit = top_k or len(scored_data)
    # scored_from_raw：讀 scored 一律無損還原，否則貼文標題 / slug / 內文會比
    # data/scored 多套一次 s2twp
    top_items = [scored_from_raw(item) for item in scored_data[:limit]]
    _t0 = _time.time()
    _logger.info("Stage started", extra={"pipeline_stage": "generate", "stage_action": "start"})
    post_paths = generate_posts(top_items, d)
    _logger.info("Stage ended", extra={
        "pipeline_stage": "generate", "stage_action": "end",
        "elapsed": round(_time.time() - _t0, 1),
        "item_count": len(post_paths),
    })
    return post_paths
