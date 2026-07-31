"""tests/test_analysis.py — analyze-scores 分析模組的單元測試。"""

from __future__ import annotations

import json
import statistics
from datetime import date
from pathlib import Path
from typing import Optional

import pytest
from typer.testing import CliRunner

from src.models import ContentItem, ScoredItem, SourceType

# ──────────────────────────────────────────────────────────
# 測試輔助：快速建立 ScoredItem
# ──────────────────────────────────────────────────────────

def _make_item(
    title: str = "Test Item",
    source: SourceType = SourceType.RSS,
    rule_score: float = 30.0,
    llm_score: Optional[float] = 60.0,
    novelty: float = 12.0,
    impact: float = 12.0,
    trending: float = 12.0,
    practicality: float = 12.0,
    blog_worthiness: float = 12.0,
    pub_date: date = date(2026, 6, 6),
) -> ScoredItem:
    return ScoredItem(
        item=ContentItem(
            source=source,
            source_name=source.value,
            title=title,
            url=f"https://example.com/{title.replace(' ', '-').lower()}",
            published_date=pub_date,
        ),
        rule_score=rule_score,
        llm_score=llm_score,
        novelty=novelty,
        impact=impact,
        trending=trending,
        practicality=practicality,
        blog_worthiness=blog_worthiness,
    )


def _make_scored_json(items: list[ScoredItem]) -> list[dict]:
    return [it.model_dump(mode="json") for it in items]


# ──────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────

@pytest.fixture
def sample_items() -> list[ScoredItem]:
    """10 個分數各異的 ScoredItem，包含 2 個來源。"""
    scores = [20.0, 30.0, 40.0, 50.0, 60.0, 65.0, 70.0, 75.0, 80.0, 90.0]
    items = []
    for i, s in enumerate(scores):
        src = SourceType.RSS if i < 7 else SourceType.BLOG
        items.append(
            _make_item(
                title=f"Item {i}",
                source=src,
                rule_score=25.0 + i,
                llm_score=s,
                novelty=s / 5,
                impact=s / 5,
                trending=s / 5,
                practicality=s / 5,
                blog_worthiness=s / 5,
            )
        )
    return items


@pytest.fixture
def scored_dir(tmp_path: Path, sample_items: list[ScoredItem]) -> Path:
    """在 tmp_path 建立 scored/ 目錄，寫入 2026-06-06.json。"""
    d = tmp_path / "scored"
    d.mkdir()
    path = d / "2026-06-06.json"
    path.write_text(json.dumps(_make_scored_json(sample_items)), encoding="utf-8")
    return d


# ──────────────────────────────────────────────────────────
# compute_day_analysis — 統計正確性
# ──────────────────────────────────────────────────────────

class TestComputeDayAnalysis:
    def test_basic_counts(self, sample_items: list[ScoredItem]):
        from src.analysis.score_analysis import compute_day_analysis

        ana = compute_day_analysis(sample_items, date(2026, 6, 6))
        assert ana.total_items == 10
        assert ana.rule_passed == 10
        assert ana.llm_scored == 10

    def test_llm_stats_correct(self, sample_items: list[ScoredItem]):
        from src.analysis.score_analysis import compute_day_analysis

        ana = compute_day_analysis(sample_items, date(2026, 6, 6))
        scores = [20.0, 30.0, 40.0, 50.0, 60.0, 65.0, 70.0, 75.0, 80.0, 90.0]

        assert ana.llm_min == pytest.approx(20.0)
        assert ana.llm_max == pytest.approx(90.0)
        assert ana.llm_mean == pytest.approx(statistics.mean(scores), rel=1e-6)
        assert ana.llm_stdev == pytest.approx(statistics.stdev(scores), rel=1e-6)
        assert ana.llm_median == pytest.approx(statistics.median(scores), rel=1e-6)

    def test_dim_stats_populated(self, sample_items: list[ScoredItem]):
        from src.analysis.score_analysis import compute_day_analysis, DIMENSIONS

        ana = compute_day_analysis(sample_items, date(2026, 6, 6))
        assert len(ana.dim_stats) == len(DIMENSIONS)
        for ds in ana.dim_stats:
            assert ds.count == 10
            assert ds.mean > 0

    def test_source_stats_groups_correctly(self, sample_items: list[ScoredItem]):
        from src.analysis.score_analysis import compute_day_analysis

        ana = compute_day_analysis(sample_items, date(2026, 6, 6))
        # rss: items 0-6 (7 items), blog: items 7-9 (3 items)
        assert "rss" in ana.source_stats
        assert "blog" in ana.source_stats
        assert ana.source_stats["rss"][0] == 7
        assert ana.source_stats["blog"][0] == 3

    def test_pearson_in_range(self, sample_items: list[ScoredItem]):
        from src.analysis.score_analysis import compute_day_analysis

        ana = compute_day_analysis(sample_items, date(2026, 6, 6))
        assert ana.pearson is not None
        assert -1.0 <= ana.pearson <= 1.0

    def test_positive_correlation_with_aligned_scores(self):
        """rule_score 和 llm_score 正相關時，Pearson 應為正值。"""
        from src.analysis.score_analysis import compute_day_analysis

        items = [
            _make_item(f"I{i}", rule_score=float(i * 10), llm_score=float(i * 8))
            for i in range(1, 6)
        ]
        ana = compute_day_analysis(items, date(2026, 6, 6))
        assert ana.pearson is not None
        assert ana.pearson > 0.9

    def test_empty_items_returns_none_stats(self):
        from src.analysis.score_analysis import compute_day_analysis

        ana = compute_day_analysis([], date(2026, 6, 6))
        assert ana.total_items == 0
        assert ana.llm_mean is None
        assert ana.llm_min is None
        assert ana.pearson is None
        assert ana.outliers == []

    def test_single_item_no_stdev_crash(self):
        """只有 1 個 item 時，stdev 應為 0.0 不 raise。"""
        from src.analysis.score_analysis import compute_day_analysis

        items = [_make_item(llm_score=55.0)]
        ana = compute_day_analysis(items, date(2026, 6, 6))
        assert ana.llm_stdev == pytest.approx(0.0)
        assert ana.llm_mean == pytest.approx(55.0)
        # 單一樣本 Pearson 應為 None
        assert ana.pearson is None


# ──────────────────────────────────────────────────────────
# 離群值偵測
# ──────────────────────────────────────────────────────────

class TestOutlierDetection:
    def test_outlier_detected_above_threshold(self):
        """分數遠高於其他的 item 應被偵測為離群值。"""
        from src.analysis.score_analysis import compute_day_analysis

        base_items = [_make_item(f"Base {i}", llm_score=50.0) for i in range(9)]
        outlier = _make_item("Outlier", llm_score=100.0)
        items = base_items + [outlier]

        ana = compute_day_analysis(items, date(2026, 6, 6), outlier_z=2.0)
        outlier_titles = [it.item.title for it, _ in ana.outliers]
        assert "Outlier" in outlier_titles

    def test_no_outliers_when_uniform(self):
        """分數均一時應無離群值。"""
        from src.analysis.score_analysis import compute_day_analysis

        items = [_make_item(f"I{i}", llm_score=60.0) for i in range(10)]
        ana = compute_day_analysis(items, date(2026, 6, 6))
        assert ana.outliers == []

    def test_outlier_z_score_positive(self, sample_items: list[ScoredItem]):
        from src.analysis.score_analysis import compute_day_analysis

        # 強制偵測一個離群值（降低門檻）
        ana = compute_day_analysis(sample_items, date(2026, 6, 6), outlier_z=1.0)
        for _item, z in ana.outliers:
            assert z > 1.0


# ──────────────────────────────────────────────────────────
# 漂移警告（多日趨勢）
# ──────────────────────────────────────────────────────────

class TestDriftDetection:
    def _build_analyses_with_drift(self):
        from src.analysis.score_analysis import compute_day_analysis

        # day1 mean ≈ 60，day2 mean ≈ 30 → 差 30 > DRIFT_THRESHOLD(10)
        day1_items = [_make_item(f"D1-{i}", llm_score=60.0) for i in range(5)]
        day2_items = [_make_item(f"D2-{i}", llm_score=30.0) for i in range(5)]
        a1 = compute_day_analysis(day1_items, date(2026, 6, 5))
        a2 = compute_day_analysis(day2_items, date(2026, 6, 6))
        return [a1, a2]

    def test_drift_captured_in_output(self, capsys):
        """漂移發生時，print_multi_day_trend 輸出應包含警告文字。"""
        from io import StringIO
        from rich.console import Console as RichConsole
        from src.analysis.score_analysis import print_multi_day_trend

        analyses = self._build_analyses_with_drift()
        buf = StringIO()
        c = RichConsole(file=buf, highlight=False, markup=False)
        print_multi_day_trend(analyses, c)
        output = buf.getvalue()
        assert "漂移" in output or "Δ" in output

    def test_no_drift_when_stable(self):
        from io import StringIO
        from rich.console import Console as RichConsole
        from src.analysis.score_analysis import compute_day_analysis, print_multi_day_trend

        day1_items = [_make_item(f"D1-{i}", llm_score=60.0) for i in range(5)]
        day2_items = [_make_item(f"D2-{i}", llm_score=62.0) for i in range(5)]
        a1 = compute_day_analysis(day1_items, date(2026, 6, 5))
        a2 = compute_day_analysis(day2_items, date(2026, 6, 6))

        buf = StringIO()
        c = RichConsole(file=buf, highlight=False, markup=False)
        print_multi_day_trend([a1, a2], c)
        output = buf.getvalue()
        # 穩定時不應出現漂移警告
        assert "漂移" not in output


# ──────────────────────────────────────────────────────────
# load_day_items
# ──────────────────────────────────────────────────────────

class TestLoadDayItems:
    def test_loads_existing_file(self, scored_dir: Path):
        from src.analysis.score_analysis import load_day_items

        items = load_day_items(scored_dir, date(2026, 6, 6))
        assert len(items) == 10
        assert all(isinstance(it, ScoredItem) for it in items)

    def test_missing_date_returns_empty(self, scored_dir: Path):
        from src.analysis.score_analysis import load_day_items

        items = load_day_items(scored_dir, date(2026, 1, 1))
        assert items == []

    def test_malformed_entry_skipped(self, tmp_path: Path):
        from src.analysis.score_analysis import load_day_items

        d = tmp_path / "scored"
        d.mkdir()
        valid = _make_scored_json([_make_item("Valid")])
        # 混入無法解析的 entry
        mixed = valid + [{"bad": "data"}]
        path = d / "2026-06-06.json"
        path.write_text(json.dumps(mixed), encoding="utf-8")

        items = load_day_items(d, date(2026, 6, 6))
        assert len(items) == 1
        assert items[0].item.title == "Valid"

    def test_reads_scored_losslessly(self, tmp_path: Path):
        """釘住 load_day_items 走 scored_from_raw：讀 data/scored 不得重複套用 Layer A。

        analyze-scores 目前只看數字，漂移不影響它的輸出——但這是唯一一處
        「讀 scored 卻不顯示文字」的呼叫點，最容易被當成無所謂而退回
        ScoredItem(**d)，接著被人照抄到會輸出文字的地方。
        單一讀取路徑要靠測試釘住，不能靠慣例。
        """
        from src.analysis.score_analysis import load_day_items
        from src.utils import to_traditional

        drifting = "這個文件的參數設定"
        assert to_traditional(drifting) != drifting, "測試前提失效：這串已經冪等了"

        d = tmp_path / "scored"
        d.mkdir()
        rec = _make_scored_json([_make_item("placeholder")])
        rec[0]["item"]["title"] = drifting
        rec[0]["item"]["abstract"] = drifting * 3
        rec[0]["item"]["tags"] = [drifting]
        (d / "2026-06-06.json").write_text(json.dumps(rec, ensure_ascii=False), encoding="utf-8")

        items = load_day_items(d, date(2026, 6, 6))
        assert items[0].item.title == drifting
        assert items[0].item.abstract == drifting * 3
        assert items[0].item.tags == [drifting]


# ──────────────────────────────────────────────────────────
# CLI 整合測試
# ──────────────────────────────────────────────────────────

class TestAnalyzeScoresCLI:
    def test_no_data_exits_cleanly(self, tmp_path: Path, monkeypatch):
        """無資料時應以 exit code 0 結束並顯示友善訊息。"""
        import src.analysis.score_analysis as sa
        monkeypatch.setattr(sa, "load_day_items", lambda _dir, _date: [])

        # monkeypatch SCORED_DIR 至 tmp 目錄，並 patch load_day_items
        from src.cli import app
        runner = CliRunner()
        result = runner.invoke(app, ["analyze-scores", "--date", "2099-01-01"])
        assert result.exit_code == 0
        assert "無" in result.output or "no" in result.output.lower()

    def test_single_day_report_contains_stats(self, scored_dir: Path, monkeypatch):
        """有資料時應輸出包含 Mean 與來源資訊的報告。"""
        import src.analysis.score_analysis as sa
        from src.analysis.score_analysis import load_day_items

        # Monkeypatch load_day_items 使用 tmp scored_dir
        orig_load = load_day_items

        def patched_load(sdir, d):
            return orig_load(scored_dir, d)

        monkeypatch.setattr(sa, "load_day_items", patched_load)

        from src.cli import app
        runner = CliRunner()
        result = runner.invoke(app, ["analyze-scores", "--date", "2026-06-06"])
        assert result.exit_code == 0
        assert "Mean" in result.output or "mean" in result.output.lower()

    def test_days_flag_shows_trend(self, scored_dir: Path, monkeypatch, tmp_path: Path):
        """--days 2 時應輸出多日趨勢表。"""
        import src.analysis.score_analysis as sa
        from src.analysis.score_analysis import load_day_items

        # 補一天資料
        second_day = scored_dir / "2026-06-05.json"
        items_day2 = [_make_item(f"D2-{i}", llm_score=float(40 + i * 5)) for i in range(5)]
        second_day.write_text(json.dumps(_make_scored_json(items_day2)), encoding="utf-8")

        orig_load = load_day_items

        def patched_load(sdir, d):
            return orig_load(scored_dir, d)

        monkeypatch.setattr(sa, "load_day_items", patched_load)

        from src.cli import app
        runner = CliRunner()
        result = runner.invoke(app, ["analyze-scores", "--date", "2026-06-06", "--days", "2"])
        assert result.exit_code == 0
        assert "趨勢" in result.output or "2026-06-05" in result.output
