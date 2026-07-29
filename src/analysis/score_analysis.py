"""評分分佈分析：單日統計 + 多日趨勢 + 漂移偵測。

統計計算僅使用 Python 標準庫 `statistics`，不引入 numpy / pandas。
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from src.models import ScoredItem, scored_from_raw

# ──────────────────────────────────────────────────────────
# 常數
# ──────────────────────────────────────────────────────────

DIMENSIONS: list[str] = [
    "novelty",
    "impact",
    "trending",
    "practicality",
    "blog_worthiness",
]

DIM_LABELS: dict[str, str] = {
    "novelty": "新穎性",
    "impact": "影響力",
    "trending": "話題性",
    "practicality": "實用性",
    "blog_worthiness": "部落格適合度",
}

LOW_STDEV_THRESHOLD = 2.0   # stdev 低於此值標記警告（維度「擠在一起」）
OUTLIER_Z_THRESHOLD = 2.5   # z-score 高於此值視為離群值
DRIFT_THRESHOLD = 10.0      # 相鄰兩日 mean 差超過此值標記漂移警告


# ──────────────────────────────────────────────────────────
# 資料結構
# ──────────────────────────────────────────────────────────

@dataclass
class DimStats:
    name: str
    label: str
    mean: float
    stdev: float
    count: int


@dataclass
class DayAnalysis:
    target_date: date
    total_items: int
    rule_passed: int         # rule_score > 0
    llm_scored: int          # llm_score is not None

    # LLM 總分統計
    llm_mean: Optional[float]
    llm_min: Optional[float]
    llm_max: Optional[float]
    llm_stdev: Optional[float]
    llm_median: Optional[float]

    # 5 維度
    dim_stats: list[DimStats] = field(default_factory=list)

    # 來源分組：{source_name: (count, avg_total_score)}
    source_stats: dict[str, tuple[int, float]] = field(default_factory=dict)

    # 離群值：(item, z_score)
    outliers: list[tuple[ScoredItem, float]] = field(default_factory=list)

    # rule_score vs llm_score 的 Pearson 相關係數
    pearson: Optional[float] = None


# ──────────────────────────────────────────────────────────
# 核心統計計算
# ──────────────────────────────────────────────────────────

def _safe_stdev(values: list[float]) -> float:
    """n < 2 時回傳 0.0 而非 raise。"""
    if len(values) < 2:
        return 0.0
    return statistics.stdev(values)


def _pearson(xs: list[float], ys: list[float]) -> Optional[float]:
    """計算 Pearson 相關係數，樣本不足時回傳 None。"""
    n = len(xs)
    if n < 2:
        return None
    mx = statistics.mean(xs)
    my = statistics.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den_sq = sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)
    if den_sq <= 0:
        return None
    return num / math.sqrt(den_sq)


def compute_day_analysis(
    items: list[ScoredItem],
    target_date: date,
    outlier_z: float = OUTLIER_Z_THRESHOLD,
) -> DayAnalysis:
    """對一天的 ScoredItem 清單計算完整分析結果。"""
    total = len(items)
    rule_passed = sum(1 for it in items if it.rule_score > 0)
    llm_items = [it for it in items if it.llm_score is not None]
    llm_count = len(llm_items)

    # ── LLM 總分統計 ──
    llm_scores = [it.llm_score for it in llm_items]  # type: ignore[misc]
    if llm_scores:
        llm_mean = statistics.mean(llm_scores)
        llm_min = min(llm_scores)
        llm_max = max(llm_scores)
        llm_stdev = _safe_stdev(llm_scores)
        llm_median = statistics.median(llm_scores)
    else:
        llm_mean = llm_min = llm_max = llm_stdev = llm_median = None

    # ── 5 維度統計 ──
    dim_stats: list[DimStats] = []
    for dim in DIMENSIONS:
        vals = [getattr(it, dim) for it in llm_items if getattr(it, dim) is not None]
        if vals:
            dim_stats.append(
                DimStats(
                    name=dim,
                    label=DIM_LABELS[dim],
                    mean=statistics.mean(vals),
                    stdev=_safe_stdev(vals),
                    count=len(vals),
                )
            )

    # ── 來源分組 ──
    source_map: dict[str, list[float]] = {}
    for it in items:
        src = it.item.source.value
        total_score = it.total_score
        source_map.setdefault(src, []).append(total_score)
    source_stats = {
        src: (len(scores), statistics.mean(scores))
        for src, scores in source_map.items()
    }

    # ── 離群值（z-score 基於 llm_score） ──
    outliers: list[tuple[ScoredItem, float]] = []
    if llm_scores and llm_mean is not None and llm_stdev and llm_stdev > 0:
        for it in llm_items:
            z = (it.llm_score - llm_mean) / llm_stdev  # type: ignore[operator]
            if z > outlier_z:
                outliers.append((it, round(z, 2)))
        outliers.sort(key=lambda t: t[1], reverse=True)

    # ── Pearson：rule_score vs llm_score ──
    paired = [(it.rule_score, it.llm_score) for it in llm_items if it.llm_score is not None]
    pearson: Optional[float] = None
    if paired:
        rs, ls = zip(*paired)
        pearson = _pearson(list(rs), list(ls))

    return DayAnalysis(
        target_date=target_date,
        total_items=total,
        rule_passed=rule_passed,
        llm_scored=llm_count,
        llm_mean=llm_mean,
        llm_min=llm_min,
        llm_max=llm_max,
        llm_stdev=llm_stdev,
        llm_median=llm_median,
        dim_stats=dim_stats,
        source_stats=source_stats,
        outliers=outliers,
        pearson=pearson,
    )


# ──────────────────────────────────────────────────────────
# 資料載入
# ──────────────────────────────────────────────────────────

def load_day_items(scored_dir: Path, target_date: date) -> list[ScoredItem]:
    """從 scored JSON 載入指定日期的 ScoredItem 清單。無資料時回傳空清單。"""
    from src.utils import load_json  # 延遲 import 避免循環

    path = scored_dir / f"{target_date.isoformat()}.json"
    if not path.exists():
        return []
    raw = load_json(path)
    if not isinstance(raw, list):
        return []
    items = []
    for d in raw:
        try:
            # scored_from_raw：讀 scored 一律無損還原（analyze-scores 只看數字，
            # 但保持單一讀取路徑，才不會有人照這裡的寫法複製到會輸出文字的地方）
            items.append(scored_from_raw(d))
        except Exception:
            continue
    return items


# ──────────────────────────────────────────────────────────
# Rich 輸出 helpers
# ──────────────────────────────────────────────────────────

def _fmt_float(v: Optional[float], decimals: int = 1) -> str:
    if v is None:
        return "—"
    return f"{v:.{decimals}f}"


def print_single_day_report(
    analysis: DayAnalysis,
    console: Console,
) -> None:
    """將單日分析結果以 Rich 格式輸出到 console。"""
    d = analysis.target_date

    # ── 標頭 ──
    console.print(
        Panel(
            f"[bold cyan]{d}[/bold cyan] 評分分佈分析",
            expand=False,
        )
    )

    # ── 概覽表 ──
    overview = Table(show_header=False, box=None, padding=(0, 2))
    overview.add_column("key", style="bold", width=20)
    overview.add_column("val")
    overview.add_row("總項目數", str(analysis.total_items))
    overview.add_row("Rule 通過數", str(analysis.rule_passed))
    overview.add_row("LLM 評分數", str(analysis.llm_scored))
    console.print(overview)

    if analysis.llm_mean is None:
        console.print("[yellow]  無 LLM 評分資料[/yellow]")
        return

    # ── LLM 總分統計 ──
    console.print("\n[bold]LLM 總分統計[/bold]")
    score_tbl = Table(box=None, padding=(0, 2))
    score_tbl.add_column("指標", style="bold", width=12)
    score_tbl.add_column("數值", justify="right", width=10)
    score_tbl.add_row("Min", _fmt_float(analysis.llm_min))
    score_tbl.add_row("Max", _fmt_float(analysis.llm_max))
    score_tbl.add_row("Mean", _fmt_float(analysis.llm_mean))
    score_tbl.add_row("Stdev", _fmt_float(analysis.llm_stdev))
    score_tbl.add_row("中位數", _fmt_float(analysis.llm_median))
    console.print(score_tbl)

    # ── 5 維度 ──
    if analysis.dim_stats:
        console.print("\n[bold]5 維度均值 / 標準差[/bold]")
        dim_tbl = Table(box=None, padding=(0, 2))
        dim_tbl.add_column("維度", width=16)
        dim_tbl.add_column("Mean", justify="right", width=8)
        dim_tbl.add_column("Stdev", justify="right", width=8)
        dim_tbl.add_column("樣本", justify="right", width=6)
        dim_tbl.add_column("備註", width=20)
        for ds in analysis.dim_stats:
            note = ""
            if ds.stdev < LOW_STDEV_THRESHOLD:
                note = Text("⚠ 分佈過度集中", style="yellow")
            dim_tbl.add_row(
                ds.label,
                _fmt_float(ds.mean),
                _fmt_float(ds.stdev),
                str(ds.count),
                note,  # type: ignore[arg-type]
            )
        console.print(dim_tbl)

    # ── 來源分組 ──
    if analysis.source_stats:
        console.print("\n[bold]來源分組[/bold]")
        src_tbl = Table(box=None, padding=(0, 2))
        src_tbl.add_column("來源", width=16)
        src_tbl.add_column("項目數", justify="right", width=8)
        src_tbl.add_column("平均總分", justify="right", width=10)
        for src, (cnt, avg) in sorted(
            analysis.source_stats.items(), key=lambda kv: kv[1][1], reverse=True
        ):
            src_tbl.add_row(src, str(cnt), _fmt_float(avg))
        console.print(src_tbl)

    # ── 離群值 ──
    if analysis.outliers:
        console.print("\n[bold]離群值（z-score > {:.1f}）[/bold]".format(OUTLIER_Z_THRESHOLD))
        out_tbl = Table(box=None, padding=(0, 2))
        out_tbl.add_column("標題", max_width=60)
        out_tbl.add_column("LLM分", justify="right", width=8)
        out_tbl.add_column("z-score", justify="right", width=8)
        for it, z in analysis.outliers:
            title = it.item.title[:60]
            out_tbl.add_row(title, _fmt_float(it.llm_score), f"{z:.2f}")
        console.print(out_tbl)
    else:
        console.print("\n[dim]無離群值[/dim]")

    # ── Pearson ──
    if analysis.pearson is not None:
        console.print(
            f"\n[bold]Rule Score vs LLM Score Pearson 相關係數[/bold]: "
            f"[cyan]{analysis.pearson:.3f}[/cyan]"
        )


def print_multi_day_trend(
    analyses: list[DayAnalysis],
    console: Console,
) -> None:
    """輸出多日趨勢表，相鄰 mean 差 > DRIFT_THRESHOLD 時標記漂移警告。"""
    console.print(Panel("[bold cyan]多日評分趨勢[/bold cyan]", expand=False))

    trend_tbl = Table(box=None, padding=(0, 2))
    trend_tbl.add_column("日期", style="bold", width=12)
    trend_tbl.add_column("項目", justify="right", width=6)
    trend_tbl.add_column("LLM評分", justify="right", width=8)
    trend_tbl.add_column("Mean", justify="right", width=8)
    trend_tbl.add_column("Stdev", justify="right", width=8)
    trend_tbl.add_column("備註", width=24)

    prev_mean: Optional[float] = None
    for ana in analyses:
        drift_note = ""
        if prev_mean is not None and ana.llm_mean is not None:
            diff = abs(ana.llm_mean - prev_mean)
            if diff > DRIFT_THRESHOLD:
                drift_note = Text(
                    f"⚠ 分數漂移警告 Δ{diff:.1f}",
                    style="bold red",
                )
        trend_tbl.add_row(
            str(ana.target_date),
            str(ana.total_items),
            str(ana.llm_scored),
            _fmt_float(ana.llm_mean),
            _fmt_float(ana.llm_stdev),
            drift_note,  # type: ignore[arg-type]
        )
        if ana.llm_mean is not None:
            prev_mean = ana.llm_mean

    console.print(trend_tbl)
