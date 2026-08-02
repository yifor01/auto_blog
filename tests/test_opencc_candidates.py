"""簡→繁修正表候選累積（方案 A）測試。

四條是計畫明列的必要防線：覆蓋判定用**完整字串**（防子字串 bug）、版本不符**拒跑**、
已裁決 pattern 被濾掉、跨文章計數正確。其餘是它們的邊界。

全部離線：歧義組表與 raw 檔都用 fixture 注入，不讀真實 `data/`、不寫真實 `output/`。
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from src.cli import app
from src.opencc_candidates import (
    OpenCCVersionMismatch,
    _installed_opencc_version,
    build_ambiguity_groups,
    covered_positions,
    load_ambiguity_groups,
    load_decisions,
    minority_map,
    render_report,
    save_ambiguity_groups,
    scan,
)

runner = CliRunner()


# `发 → 發/髮` 是計畫舉的範例組，也是語料裡真的出過錯的組（被髮明出來）。
FAKE_GROUPS = {
    "opencc_version": _installed_opencc_version(),
    "groups": {
        "发": {"default": "發", "chars": ["发", "發", "髮"]},
        "里": {"default": "裡", "chars": ["裏", "裡", "里"]},
    },
}


def write_raw(raw_dir: Path, day: str, items: list[dict]) -> None:
    raw_dir.mkdir(parents=True, exist_ok=True)
    (raw_dir / f"{day}.json").write_text(
        json.dumps(items, ensure_ascii=False), encoding="utf-8"
    )


def run_scan(raw_dir: Path, **kwargs):
    kwargs.setdefault("groups_doc", FAKE_GROUPS)
    kwargs.setdefault("decisions", {})
    kwargs.setdefault("keys", ())
    return scan(days=None, raw_dir=raw_dir, **kwargs)


# ──────────────────────────────────────────────────────────
# 歧義組表：來源是 OpenCC 自己的字典
# ──────────────────────────────────────────────────────────

class TestBuildAmbiguityGroups:
    """建表跑全 CJK 兩個區塊（27,584 字），約 10 秒——刻意只跑一次並共用。"""

    @pytest.fixture(scope="class")
    def doc(self):
        return build_ambiguity_groups()

    def test_stamps_installed_version(self, doc):
        assert doc["opencc_version"] == _installed_opencc_version()

    def test_covers_far_more_than_corpus_derived_table(self, doc):
        # 計畫的實測基線：2802 組。用語料觀察到的字只建得出 39 組，這個數量差
        # （72 倍）正是「不能用語料建表」的理由，掉下來就代表建表邏輯壞了。
        assert len(doc["groups"]) > 2000

    def test_classic_group_has_expected_default_and_branches(self, doc):
        group = doc["groups"]["发"]
        assert group["default"] == "發"
        assert set(group["chars"]) >= {"發", "髮"}

    def test_every_group_default_is_inside_its_own_group(self, doc):
        # 預設分支不在組內時無法定義「少數分支」（實測 2 組：腭/齶、鮎/鲇），
        # 必須整組排除而不是硬取一個分支。
        assert all(g["default"] in g["chars"] for g in doc["groups"].values())

    def test_single_branch_groups_are_excluded(self, doc):
        assert all(len(g["chars"]) >= 2 for g in doc["groups"].values())


class TestMinorityMap:
    def test_default_branch_is_not_a_candidate(self):
        mapping = minority_map(FAKE_GROUPS)
        assert "發" not in mapping
        assert mapping["髮"] == ("发", "發")

    def test_simplified_char_itself_counts_as_minority(self):
        # `发` 出現在 Layer A 的產物裡代表轉換根本沒生效，該被看見。
        assert minority_map(FAKE_GROUPS)["发"] == ("发", "發")


# ──────────────────────────────────────────────────────────
# 版本守門：不符必須**拒跑**，不是警告
# ──────────────────────────────────────────────────────────

class TestVersionGuard:
    def test_mismatched_version_refuses_to_run(self, tmp_path):
        path = save_ambiguity_groups(
            {"opencc_version": "0.0.0-not-installed", "groups": {}},
            path=tmp_path / "groups.json",
        )
        with pytest.raises(OpenCCVersionMismatch):
            load_ambiguity_groups(path)

    def test_matching_version_loads(self, tmp_path):
        path = save_ambiguity_groups(FAKE_GROUPS, path=tmp_path / "groups.json")
        assert load_ambiguity_groups(path)["groups"]["发"]["default"] == "發"

    def test_shipped_table_matches_installed_opencc(self):
        # repo 裡那份表是 1.3.1 建的；CI 每天重裝依賴，版本一漂這條就紅。
        # 沒有這條的話，漂移的表現是「掃描拒跑」——只有真的去跑的人才會發現。
        from src.opencc_candidates import GROUPS_PATH

        doc = load_ambiguity_groups(GROUPS_PATH)
        assert len(doc["groups"]) > 2000

    def test_missing_table_points_at_rebuild_command(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="rebuild-groups"):
            load_ambiguity_groups(tmp_path / "nope.json")


# ──────────────────────────────────────────────────────────
# 覆蓋判定：完整字串，不是單字元子字串
# ──────────────────────────────────────────────────────────

class TestCoveredPositions:
    def test_covers_the_whole_key_span(self):
        assert covered_positions("前綴髮型後綴", ("髮型",)) == {2, 3}

    def test_covers_every_occurrence(self):
        assert covered_positions("髮型與髮型", ("髮型",)) == {0, 1, 3, 4}

    def test_key_elsewhere_does_not_cover_other_occurrences(self):
        # 這條就是「單字元子字串 bug」的形狀：`髮` 同時出現在 key 命中處與別處，
        # 用 `ch in key` 判定會把兩個都當成已覆蓋，整個掃描靜默回報 0 筆。
        positions = covered_positions("被髮明出來，理髮型", ("髮型",))
        assert positions == {7, 8}
        assert 1 not in positions

    def test_no_keys_covers_nothing(self):
        assert covered_positions("被髮明", ()) == set()


class TestScanRespectsCoverage:
    def test_covered_occurrence_is_not_a_candidate(self, tmp_path):
        write_raw(tmp_path, "2026-08-01", [{"url": "u1", "title": "理髮型沙龍"}])
        result = run_scan(tmp_path, keys=("髮型",))
        assert result.candidates == []

    def test_uncovered_occurrence_in_the_same_field_still_surfaces(self, tmp_path):
        write_raw(tmp_path, "2026-08-01", [{"url": "u1", "title": "被髮明出來的理髮型"}])
        result = run_scan(tmp_path, keys=("髮型",))
        assert [c.pattern for c in result.candidates] == ["髮→發"]
        assert result.candidates[0].count == 1


# ──────────────────────────────────────────────────────────
# 裁決帳本
# ──────────────────────────────────────────────────────────

class TestDecisions:
    def test_decided_pattern_is_suppressed_not_reported(self, tmp_path):
        write_raw(tmp_path, "2026-08-01", [{"url": "u1", "title": "被髮明出來"}])
        result = run_scan(tmp_path, decisions={"髮→發": {"verdict": "rejected"}})
        assert result.candidates == []
        assert result.suppressed == {"髮→發": 1}

    def test_last_record_wins_and_blank_lines_ignored(self, tmp_path):
        path = tmp_path / "decisions.jsonl"
        path.write_text(
            '{"pattern":"髮→發","verdict":"rejected"}\n'
            "\n"
            '{"pattern":"髮→發","verdict":"accepted"}\n',
            encoding="utf-8",
        )
        assert load_decisions(path)["髮→發"]["verdict"] == "accepted"

    def test_absent_ledger_is_empty(self, tmp_path):
        assert load_decisions(tmp_path / "nope.jsonl") == {}

    def test_comment_lines_are_skipped(self, tmp_path):
        # 帳本是人手寫的，檔頭帶欄位說明；註解若沒被跳過會直接 JSONDecodeError。
        path = tmp_path / "decisions.jsonl"
        path.write_text(
            "# 欄位：pattern / verdict / counterexample …\n"
            '{"pattern":"髮→發","verdict":"rejected"}\n',
            encoding="utf-8",
        )
        assert list(load_decisions(path)) == ["髮→發"]

    def test_shipped_ledger_parses(self):
        # repo 裡那份含 6 行註解的實檔——格式壞掉會讓每週審查整個掃描炸掉。
        from src.opencc_candidates import DECISIONS_PATH

        assert load_decisions(DECISIONS_PATH) == {}


# ──────────────────────────────────────────────────────────
# 聚合：跨文章 / 跨天計數與排序
# ──────────────────────────────────────────────────────────

class TestAggregation:
    def test_repeats_in_one_article_count_as_one_article(self, tmp_path):
        write_raw(
            tmp_path,
            "2026-08-01",
            [{"url": "u1", "title": "被髮明", "abstract": "又被髮明，再被髮明"}],
        )
        candidate = run_scan(tmp_path).candidates[0]
        assert candidate.count == 3
        assert candidate.article_count == 1
        assert candidate.day_count == 1

    def test_counts_articles_and_days_across_files(self, tmp_path):
        write_raw(tmp_path, "2026-08-01", [{"url": "u1", "title": "被髮明"}])
        write_raw(
            tmp_path,
            "2026-08-02",
            [{"url": "u2", "title": "髮生了"}, {"url": "u3", "title": "髮布會"}],
        )
        candidate = run_scan(tmp_path).candidates[0]
        assert (candidate.count, candidate.article_count, candidate.day_count) == (3, 3, 2)

    def test_ranked_by_article_count_not_total_count(self, tmp_path):
        # `裏` 總次數多但全在一篇；`髮` 次數少卻跨兩篇 —— 後者該排前面。
        write_raw(
            tmp_path,
            "2026-08-01",
            [
                {"url": "u1", "title": "裏面裏面裏面裏面"},
                {"url": "u2", "title": "被髮明"},
                {"url": "u3", "title": "髮生了"},
            ],
        )
        result = run_scan(tmp_path)
        assert [c.pattern for c in result.candidates] == ["髮→發", "裏→裡"]
        assert result.candidates[1].count > result.candidates[0].count

    def test_scans_title_abstract_and_tags(self, tmp_path):
        write_raw(
            tmp_path,
            "2026-08-01",
            [{"url": "u1", "title": "被髮明", "abstract": "髮生了", "tags": ["髮布"]}],
        )
        assert run_scan(tmp_path).candidates[0].count == 3

    def test_items_without_url_are_still_distinct_articles(self, tmp_path):
        write_raw(tmp_path, "2026-08-01", [{"title": "被髮明"}, {"title": "髮生了"}])
        assert run_scan(tmp_path).candidates[0].article_count == 2

    def test_context_snippets_are_capped(self, tmp_path):
        write_raw(
            tmp_path,
            "2026-08-01",
            [{"url": f"u{i}", "title": "被髮明"} for i in range(9)],
        )
        candidate = run_scan(tmp_path).candidates[0]
        assert candidate.count == 9
        assert len(candidate.contexts) == 5

    def test_unreadable_file_is_skipped_not_fatal(self, tmp_path):
        (tmp_path).mkdir(parents=True, exist_ok=True)
        (tmp_path / "2026-08-01.json").write_text("{not json", encoding="utf-8")
        write_raw(tmp_path, "2026-08-02", [{"url": "u1", "title": "被髮明"}])
        assert run_scan(tmp_path).candidates[0].count == 1


class TestDayWindow:
    def test_days_window_excludes_older_files(self, tmp_path):
        from datetime import date, timedelta

        today = date.today()
        write_raw(tmp_path, today.isoformat(), [{"url": "u1", "title": "被髮明"}])
        write_raw(
            tmp_path,
            (today - timedelta(days=30)).isoformat(),
            [{"url": "u2", "title": "髮生了"}],
        )
        result = scan(days=7, raw_dir=tmp_path, groups_doc=FAKE_GROUPS, decisions={}, keys=())
        assert result.days_scanned == 1
        assert result.candidates[0].count == 1


# ──────────────────────────────────────────────────────────
# 報告
# ──────────────────────────────────────────────────────────

class TestRenderReport:
    def test_report_carries_context_and_counterexample_field(self, tmp_path):
        write_raw(tmp_path, "2026-08-01", [{"url": "u1", "source": "rss", "title": "被髮明出來"}])
        text = render_report(run_scan(tmp_path))
        assert "`髮`" in text
        assert "被髮明出來" in text
        assert "反例檢查（審查者必填）" in text
        assert "[2026-08-01 rss]" in text

    def test_suppressed_patterns_stay_visible(self, tmp_path):
        # `rejected` 會永久壓住一個 pattern；當初判錯的話，這一段是唯一的回頭路。
        write_raw(tmp_path, "2026-08-01", [{"url": "u1", "title": "被髮明"}])
        decisions = {"髮→發": {"verdict": "rejected", "date": "2026-08-02"}}
        text = render_report(run_scan(tmp_path, decisions=decisions), decisions)
        assert "已裁決（本次略過）" in text
        assert "rejected（2026-08-02）" in text


# ──────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────

class TestCli:
    def test_reports_and_writes_to_the_given_dir(self, tmp_path, monkeypatch):
        import src.opencc_candidates as mod

        write_raw(tmp_path / "raw", "2026-08-01", [{"url": "u1", "title": "被髮明"}])
        monkeypatch.setattr(mod, "RAW_DIR", tmp_path / "raw")
        monkeypatch.setattr(mod, "REPORT_DIR", tmp_path / "report")
        monkeypatch.setattr(mod, "GROUPS_PATH", tmp_path / "groups.json")
        monkeypatch.setattr(mod, "DECISIONS_PATH", tmp_path / "decisions.jsonl")
        save_ambiguity_groups(FAKE_GROUPS, path=tmp_path / "groups.json")

        result = runner.invoke(app, ["opencc-candidates", "--all"])
        assert result.exit_code == 0, result.output
        assert "候選≠錯字" in result.output
        assert (tmp_path / "report").exists()

    def test_missing_groups_table_exits_nonzero(self, tmp_path, monkeypatch):
        import src.opencc_candidates as mod

        monkeypatch.setattr(mod, "RAW_DIR", tmp_path / "raw")
        monkeypatch.setattr(mod, "GROUPS_PATH", tmp_path / "absent.json")
        result = runner.invoke(app, ["opencc-candidates"])
        assert result.exit_code == 1
        assert "rebuild-groups" in result.output
