"""CLI 指令整合測試。"""

from __future__ import annotations

import json
import tempfile
from datetime import date, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from typer.testing import CliRunner

from src.cli import app, _parse_date, _read_frontmatter


runner = CliRunner()


# ──────────────────────────────────────────────────────────
# _parse_date helper 測試
# ──────────────────────────────────────────────────────────

class TestParseDate:
    def test_valid_date(self):
        assert _parse_date("2026-02-26") == date(2026, 2, 26)

    def test_none_returns_today(self):
        assert _parse_date(None) == date.today()

    def test_invalid_date_exits(self):
        import click
        with pytest.raises((SystemExit, click.exceptions.Exit)):
            _parse_date("not-a-date")

    def test_invalid_format_exits(self):
        import click
        with pytest.raises((SystemExit, click.exceptions.Exit)):
            _parse_date("26/02/2026")


# ──────────────────────────────────────────────────────────
# status 指令
# ──────────────────────────────────────────────────────────

class TestStatusCommand:
    def test_status_runs_without_error(self):
        result = runner.invoke(app, ["status"])
        assert result.exit_code == 0
        assert "Pipeline Status" in result.output

    def test_status_custom_days(self):
        result = runner.invoke(app, ["status", "--days", "3"])
        assert result.exit_code == 0


# ──────────────────────────────────────────────────────────
# list 指令
# ──────────────────────────────────────────────────────────

class TestListCommand:
    def test_list_runs_without_error(self):
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0

    def test_list_type_filter_post(self):
        result = runner.invoke(app, ["list", "--type", "post"])
        assert result.exit_code == 0

    def test_list_type_filter_note(self):
        result = runner.invoke(app, ["list", "--type", "note"])
        assert result.exit_code == 0

    def test_list_days_option(self):
        result = runner.invoke(app, ["list", "--days", "3"])
        assert result.exit_code == 0


# ──────────────────────────────────────────────────────────
# show 指令
# ──────────────────────────────────────────────────────────

class TestShowCommand:
    def test_show_nonexistent_file_exits(self, tmp_path):
        result = runner.invoke(app, ["show", str(tmp_path / "nonexistent.md")])
        assert result.exit_code != 0
        assert "找不到檔案" in result.output

    def test_show_file_with_frontmatter(self, tmp_path):
        md_file = tmp_path / "test.md"
        md_file.write_text(
            "---\ntitle: \"Test Article\"\nsource: arXiv\n---\n\n# Title\n\nContent here.",
            encoding="utf-8",
        )
        result = runner.invoke(app, ["show", str(md_file)])
        assert result.exit_code == 0

    def test_show_file_without_frontmatter(self, tmp_path):
        md_file = tmp_path / "simple.md"
        md_file.write_text("# Simple\n\nJust content.", encoding="utf-8")
        result = runner.invoke(app, ["show", str(md_file)])
        assert result.exit_code == 0


# ──────────────────────────────────────────────────────────
# clean 指令
# ──────────────────────────────────────────────────────────

class TestCleanCommand:
    def test_clean_requires_before_or_keep_days(self):
        result = runner.invoke(app, ["clean"])
        assert result.exit_code != 0
        assert "請指定" in result.output

    def test_clean_dry_run_shows_files(self, tmp_path):
        """dry-run 模式應列出檔案但不刪除。"""
        from src.utils import POSTS_DIR
        # 建立一個很久以前的 post 檔案
        old_date = date(2020, 1, 1)
        old_file = POSTS_DIR / f"{old_date.isoformat()}_test.md"
        try:
            old_file.write_text("---\ntitle: Old\n---\n\nOld content.", encoding="utf-8")
            result = runner.invoke(
                app,
                ["clean", "--before", "2021-01-01", "--dry-run"],
                input="y\n",
            )
            assert result.exit_code == 0
            assert old_file.exists()  # dry-run 不應刪除
        finally:
            if old_file.exists():
                old_file.unlink()

    def test_clean_invalid_date_exits(self):
        result = runner.invoke(app, ["clean", "--before", "not-a-date"])
        assert result.exit_code != 0


# ──────────────────────────────────────────────────────────
# --force 行為測試（B1）
# ──────────────────────────────────────────────────────────

class TestForceFlag:
    def test_force_clears_outputs(self, tmp_path):
        """--force 應清除 posts/notes/prompts 中該日期的檔案。"""
        from src.utils import NOTES_DIR, POSTS_DIR, PROMPTS_DIR, RAW_DIR, SCORED_DIR

        test_date = date(2020, 6, 15)
        prefix = test_date.isoformat()

        # 建立假的輸出檔案
        post_file = POSTS_DIR / f"{prefix}_test.md"
        note_file = NOTES_DIR / f"{prefix}_test.md"
        prompt_file = PROMPTS_DIR / f"{prefix}_test_prompt.md"
        raw_file = RAW_DIR / f"{prefix}.json"
        scored_file = SCORED_DIR / f"{prefix}.json"

        for f in [post_file, note_file, prompt_file]:
            f.write_text("test", encoding="utf-8")
        raw_file.write_text("[]")
        scored_file.write_text("[]")

        try:
            # mock collect_items 以避免真實執行
            with patch("src.pipeline.collect_items", return_value=[]):
                result = runner.invoke(
                    app,
                    ["run", "--date", str(test_date), "--force"],
                )

            # posts 應保留（force 不刪舊文章，只補生成新的）
            assert post_file.exists(), "post 應保留"
            # prompts 應被清除
            assert not prompt_file.exists(), "prompt 應被清除"
        finally:
            for f in [post_file, note_file, prompt_file, raw_file, scored_file]:
                if f.exists():
                    f.unlink()


# ──────────────────────────────────────────────────────────
# _read_frontmatter helper
# ──────────────────────────────────────────────────────────

class TestReadFrontmatter:
    def test_reads_yaml_frontmatter(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text(
            '---\ntitle: "Test Title"\nsource: arXiv\nscore: 125\n---\n\nContent.',
            encoding="utf-8",
        )
        fm = _read_frontmatter(f)
        assert fm["title"] == "Test Title"
        assert fm["source"] == "arXiv"
        assert fm["score"] == "125"

    def test_returns_empty_dict_without_frontmatter(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("# Just a title\n\nContent.", encoding="utf-8")
        assert _read_frontmatter(f) == {}

    def test_returns_empty_dict_for_missing_file(self, tmp_path):
        f = tmp_path / "nonexistent.md"
        assert _read_frontmatter(f) == {}


# ──────────────────────────────────────────────────────────
# 讀 data/scored 的 CLI 呼叫點：一律無損還原
#
# scored_from_raw() 的單元測試在 tests/test_models.py::TestScoredFromRaw；
# 這裡守的是「summary / digest 兩個指令真的走了它」。退回 ScoredItem(**rec)
# 不會拋錯也不會有 log，只有針對呼叫端的測試抓得到。
# ──────────────────────────────────────────────────────────

_DRIFTING = "這個文件的參數設定"  # s2twp 再套一次 → 這個檔案的參數設定


def _drifting_scored_json() -> list[dict]:
    return [{
        "item": {
            "source": "rss",
            "source_name": "TechCrunch AI",
            "title": _DRIFTING,
            "url": "https://example.com/a",
            "authors": [],
            "abstract": _DRIFTING * 3,
            "published_date": "2026-01-01",
            "tags": [_DRIFTING],
            "organization": "",
            "raw_metadata": {},
        },
        "rule_score": 30.0,
        "rule_reasons": [],
        "llm_score": 60.0,
        "llm_reason": "ok",
        "novelty": 12.0, "impact": 12.0, "trending": 12.0,
        "practicality": 12.0, "blog_worthiness": 12.0,
    }]


class TestCliScoredReadsAreLossless:
    def test_premise_string_really_drifts(self):
        from src.utils import to_traditional

        assert to_traditional(_DRIFTING) != _DRIFTING, "測試前提失效：這串已經冪等了"

    def _write(self, tmp_path) -> Path:
        p = tmp_path / "2026-01-01.json"
        p.write_text(json.dumps(_drifting_scored_json(), ensure_ascii=False), encoding="utf-8")
        return p

    def test_summary_command(self, tmp_path):
        """summary 表格顯示的標題來自 ScoredItem，不得漂。"""
        path = self._write(tmp_path)
        captured = {}
        with patch("src.cli.get_scored_path", return_value=path), \
             patch("src.cli.print_summary", lambda items: captured.setdefault("items", items)):
            result = runner.invoke(app, ["summary", "--date", "2026-01-01"])
        assert result.exit_code == 0
        assert captured["items"][0].item.title == _DRIFTING
        assert captured["items"][0].item.tags == [_DRIFTING]

    def test_digest_command(self, tmp_path):
        """digest 是寫檔輸出，漂移會直接固化進 output/digests。"""
        path = self._write(tmp_path)
        captured = {}

        def _fake_digest(items, d):
            captured["items"] = items
            return tmp_path / "digest.md"

        with patch("src.cli.get_scored_path", return_value=path), \
             patch("src.generators.digest.generate_and_save_digest", _fake_digest):
            result = runner.invoke(app, ["digest", "--date", "2026-01-01"])
        assert result.exit_code == 0, result.output
        assert captured["items"][0].item.title == _DRIFTING
        assert captured["items"][0].item.abstract == _DRIFTING * 3
        assert captured["items"][0].item.tags == [_DRIFTING]
