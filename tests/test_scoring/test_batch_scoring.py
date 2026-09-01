"""批次評分測試（全 mock，不叫起 claude CLI）。

設計前提與批次生成相同：批次是**可選路徑**，config flag 關閉時既有逐筆路徑的行為必須
一字不差，且批次任何一筆出問題都要能退回逐筆——切回 OpenRouter 只需改一個 bool。
"""
from __future__ import annotations

import json
from datetime import date
from unittest.mock import patch

import pytest

from src.models import ContentItem, ScoredItem, SourceType
from src.scoring.scorer import (
    SCORE_BATCH_END_MARKER,
    batch_llm_score,
    build_score_batch_prompt,
    parse_score_batch_output,
    score_items_batch,
)


def _item(title: str = "Test Article", abstract_len: int = 150) -> ScoredItem:
    item = ContentItem(
        source=SourceType.BLOG,
        source_name="Test Blog",
        title=title,
        url=f"https://example.com/{title.replace(' ', '-')}",
        authors=["Author"],
        abstract="A" * abstract_len,
        published_date=date.today(),
        tags=["test"],
    )
    return ScoredItem(item=item, rule_score=80.0)


def _scores(n: int, reason: str = "理由") -> dict:
    return {
        "novelty": n, "impact": n, "trending": n,
        "practicality": n, "blog_worthiness": n, "reason": reason,
    }


def _batch_output(*score_dicts: dict) -> str:
    parts = [f"===SCORE {i}===\n{json.dumps(d, ensure_ascii=False)}"
             for i, d in enumerate(score_dicts, 1)]
    return "\n".join(parts) + f"\n{SCORE_BATCH_END_MARKER}\n"


def _cfg(**batch_scoring) -> dict:
    cfg = {
        "llm": {"request_delay_seconds": 0},
        "scoring": {"llm_top_k": 10, "final_top_k": 10},
    }
    if batch_scoring:
        cfg["llm"]["batch_scoring"] = batch_scoring
    return cfg


# ── 解析 ──────────────────────────────────────────────────────────────────

class TestParseScoreBatchOutput:
    def test_splits_all_entries(self):
        got = parse_score_batch_output(_batch_output(_scores(5), _scores(9)), expected=2)
        assert set(got) == {1, 2}
        assert got[1]["novelty"] == 5
        assert got[2]["impact"] == 9

    def test_end_marker_does_not_break_last_entry(self):
        got = parse_score_batch_output(_batch_output(_scores(7)), expected=1)
        assert got[1]["trending"] == 7

    def test_leading_noise_discarded(self):
        """模型偶爾在第一個分隔行前寫一句「好的，以下是評分」。"""
        noisy = "好的，以下是評分結果：\n\n" + _batch_output(_scores(4))
        assert parse_score_batch_output(noisy, expected=1)[1]["novelty"] == 4

    def test_json_in_code_block_still_parsed(self):
        out = f"===SCORE 1===\n```json\n{json.dumps(_scores(6))}\n```\n{SCORE_BATCH_END_MARKER}"
        assert parse_score_batch_output(out, expected=1)[1]["impact"] == 6

    def test_missing_entry_simply_absent(self):
        """少評一筆不是例外，是缺漏——回傳缺該 key，由上層 fallback。"""
        out = (f"===SCORE 1===\n{json.dumps(_scores(3))}\n"
               f"===SCORE 3===\n{json.dumps(_scores(8))}\n{SCORE_BATCH_END_MARKER}")
        assert set(parse_score_batch_output(out, expected=3)) == {1, 3}

    def test_out_of_range_index_ignored(self):
        """模型多評一筆不存在的素材，放行會讓對齊錯位，把 A 的分數寫到 B 身上。"""
        out = (f"===SCORE 1===\n{json.dumps(_scores(3))}\n"
               f"===SCORE 9===\n{json.dumps(_scores(8))}\n{SCORE_BATCH_END_MARKER}")
        assert set(parse_score_batch_output(out, expected=2)) == {1}

    def test_incomplete_dimensions_dropped(self):
        """5 維沒到齊的整筆視為缺漏：補成 0 分會讓那筆靜默沉底。"""
        partial = {"novelty": 10, "impact": 10, "reason": "只寫了兩維"}
        out = f"===SCORE 1===\n{json.dumps(partial)}\n{SCORE_BATCH_END_MARKER}"
        assert parse_score_batch_output(out, expected=1) == {}

    def test_non_numeric_dimension_dropped(self):
        bad = _scores(5) | {"impact": "很高"}
        out = f"===SCORE 1===\n{json.dumps(bad, ensure_ascii=False)}\n{SCORE_BATCH_END_MARKER}"
        assert parse_score_batch_output(out, expected=1) == {}

    def test_marker_must_own_its_line(self):
        """摘要正文可能引用 ===SCORE，只有獨佔一行的才算分隔。"""
        out = f"前文提到 ===SCORE 1=== 這個字串\n{SCORE_BATCH_END_MARKER}"
        assert parse_score_batch_output(out, expected=1) == {}

    @pytest.mark.parametrize("junk", ["", "完全不照格式的一段話", None])
    def test_unparseable_returns_empty(self, junk):
        assert parse_score_batch_output(junk or "", expected=3) == {}


# ── Prompt 組裝 ────────────────────────────────────────────────────────────

class TestBuildScoreBatchPrompt:
    def test_contains_every_item_and_contract(self):
        items = [_item("甲文"), _item("乙文"), _item("丙文")]
        prompt = build_score_batch_prompt(items)
        for t in ("甲文", "乙文", "丙文"):
            assert t in prompt
        assert "### 素材 3" in prompt
        assert SCORE_BATCH_END_MARKER in prompt
        assert "0-20" in prompt  # 評分規範本體有帶進來

    def test_social_signals_included(self):
        it = _item("熱門文")
        it.item.raw_metadata = {"upvotes": 42}
        assert "HF upvotes: 42" in build_score_batch_prompt([it])


# ── 批次執行 ──────────────────────────────────────────────────────────────

class TestScoreItemsBatch:
    def test_applies_scores_in_input_order(self):
        items = [_item("甲文"), _item("乙文")]
        out = _batch_output(_scores(4, "甲的理由"), _scores(16, "乙的理由"))
        with patch("src.scoring.scorer.claude_code_generate", return_value=out):
            missing = score_items_batch(items, "sonnet", 900)
        assert missing == []
        assert items[0].novelty == 4 and items[0].llm_reason == "甲的理由"
        assert items[1].novelty == 16 and items[1].llm_reason == "乙的理由"

    def test_llm_score_is_recomputed_not_trusted(self):
        """自行加總，不信任 LLM 給的 total。"""
        items = [_item()]
        lying = _scores(10) | {"total": 999}
        out = f"===SCORE 1===\n{json.dumps(lying, ensure_ascii=False)}\n{SCORE_BATCH_END_MARKER}"
        with patch("src.scoring.scorer.claude_code_generate", return_value=out):
            score_items_batch(items, "sonnet", 900)
        assert items[0].llm_score == 50

    def test_gap_returns_only_that_item(self):
        items = [_item("甲文"), _item("乙文"), _item("丙文")]
        out = (f"===SCORE 1===\n{json.dumps(_scores(5))}\n"
               f"===SCORE 3===\n{json.dumps(_scores(15))}\n{SCORE_BATCH_END_MARKER}")
        with patch("src.scoring.scorer.claude_code_generate", return_value=out):
            missing = score_items_batch(items, "sonnet", 900)
        assert missing == [items[1]]
        assert items[0].novelty == 5 and items[2].novelty == 15

    def test_cli_failure_returns_all_as_missing(self):
        items = [_item("甲文"), _item("乙文")]
        with patch("src.scoring.scorer.claude_code_generate", return_value=""):
            missing = score_items_batch(items, "sonnet", 900)
        assert missing == items


# ── 路徑分流 ──────────────────────────────────────────────────────────────

class TestModeDispatch:
    MOCK_SEQ = json.dumps(_scores(11))

    def test_flag_absent_uses_sequential(self):
        items = [_item("甲文")]
        with patch("src.scoring.scorer.claude_code_generate") as cli, \
             patch("src.scoring.scorer.llm_chat", return_value=self.MOCK_SEQ) as chat, \
             patch("src.scoring.scorer.time.sleep"):
            batch_llm_score(items, _cfg())
        cli.assert_not_called()
        assert chat.called
        assert items[0].novelty == 11

    def test_flag_on_uses_batch_and_skips_openrouter(self):
        items = [_item("甲文"), _item("乙文")]
        out = _batch_output(_scores(6), _scores(18))
        with patch("src.scoring.scorer.claude_code_generate", return_value=out) as cli, \
             patch("src.scoring.scorer.llm_chat") as chat, \
             patch("src.scoring.scorer.time.sleep"):
            result = batch_llm_score(items, _cfg(enabled=True, model="sonnet", batch_size=20))
        assert cli.call_count == 1
        chat.assert_not_called()
        assert [r.novelty for r in result] == [18, 6]  # 依總分降序

    def test_splits_into_batches_of_configured_size(self):
        items = [_item(f"文{i}") for i in range(5)]
        with patch("src.scoring.scorer.claude_code_generate",
                   return_value=_batch_output(*[_scores(9)] * 2)) as cli, \
             patch("src.scoring.scorer.llm_chat", return_value=self.MOCK_SEQ), \
             patch("src.scoring.scorer.time.sleep"):
            batch_llm_score(items, _cfg(enabled=True, batch_size=2))
        assert cli.call_count == 3  # 2 + 2 + 1

    def test_batch_gap_falls_back_per_item_not_per_batch(self):
        """缺漏的那一筆走 OpenRouter，已評好的不重評。"""
        items = [_item("甲文"), _item("乙文")]
        out = f"===SCORE 1===\n{json.dumps(_scores(7))}\n{SCORE_BATCH_END_MARKER}"
        with patch("src.scoring.scorer.claude_code_generate", return_value=out), \
             patch("src.scoring.scorer.llm_chat", return_value=self.MOCK_SEQ) as chat, \
             patch("src.scoring.scorer.time.sleep"):
            batch_llm_score(items, _cfg(enabled=True, batch_size=20))
        assert chat.call_count == 1
        assert items[0].novelty == 7   # 批次拿到的
        assert items[1].novelty == 11  # 逐篇補的

    def test_cli_dead_falls_back_entirely(self):
        """沒裝 claude / OAuth 過期時 claude_code_generate 回 ""，整批退回逐筆。"""
        items = [_item("甲文"), _item("乙文")]
        with patch("src.scoring.scorer.claude_code_generate", return_value=""), \
             patch("src.scoring.scorer.llm_chat", return_value=self.MOCK_SEQ) as chat, \
             patch("src.scoring.scorer.time.sleep"):
            batch_llm_score(items, _cfg(enabled=True, batch_size=20))
        assert chat.call_count == 2
        assert all(i.novelty == 11 for i in items)

    def test_short_abstract_excluded_before_batching(self):
        """摘要太短的不送 LLM，兩條路徑一致，且不佔批次名額。"""
        short = _item("短文", abstract_len=10)
        normal = _item("正常文")
        with patch("src.scoring.scorer.claude_code_generate",
                   return_value=_batch_output(_scores(13))) as cli, \
             patch("src.scoring.scorer.llm_chat") as chat, \
             patch("src.scoring.scorer.time.sleep"):
            batch_llm_score([short, normal], _cfg(enabled=True, batch_size=20))
        assert cli.call_count == 1
        chat.assert_not_called()
        assert normal.novelty == 13
        assert short.llm_score is None  # 完全沒被碰過

    def test_respects_final_top_k(self):
        items = [_item(f"文{i}") for i in range(4)]
        cfg = _cfg(enabled=True, batch_size=20)
        cfg["scoring"]["final_top_k"] = 2
        with patch("src.scoring.scorer.claude_code_generate",
                   return_value=_batch_output(*[_scores(n) for n in (3, 19, 7, 11)])), \
             patch("src.scoring.scorer.time.sleep"):
            result = batch_llm_score(items, cfg)
        assert [r.novelty for r in result] == [19, 11]
