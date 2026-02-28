"""LLM scorer 測試（mock llm_chat，驗證 JSON 解析與 practicality 儲存）。"""

from __future__ import annotations

import json
from unittest.mock import patch

import pytest

from src.scoring.scorer import _parse_score_json, batch_llm_score, llm_score_item


class TestParseScoreJson:
    """_parse_score_json 的各種 edge case 測試。"""

    VALID_SCORES = {
        "novelty": 17, "impact": 16, "trending": 15,
        "practicality": 14, "blog_worthiness": 13,
        "total": 75, "reason": "Good paper",
    }

    def test_parse_clean_json(self):
        result = _parse_score_json(json.dumps(self.VALID_SCORES))
        assert result["total"] == 75
        assert result["practicality"] == 14

    def test_parse_json_in_code_block(self):
        text = f"```json\n{json.dumps(self.VALID_SCORES)}\n```"
        result = _parse_score_json(text)
        assert result is not None
        assert result["novelty"] == 17

    def test_parse_json_in_plain_code_block(self):
        text = f"```\n{json.dumps(self.VALID_SCORES)}\n```"
        result = _parse_score_json(text)
        assert result is not None
        assert result["impact"] == 16

    def test_parse_json_with_surrounding_text(self):
        text = f"Here is my evaluation:\n{json.dumps(self.VALID_SCORES)}\nHope that helps!"
        result = _parse_score_json(text)
        assert result is not None
        assert result["total"] == 75

    def test_returns_none_for_garbage(self):
        result = _parse_score_json("This is completely invalid JSON with no structure")
        assert result is None

    def test_returns_none_for_empty_string(self):
        result = _parse_score_json("")
        assert result is None

    def test_handles_trailing_comma_in_code_block(self):
        """LLM 有時會產生結尾帶逗號的 JSON（不合法），應 gracefully 失敗。"""
        text = '```json\n{"total": 75, "reason": "ok",}\n```'
        # 允許 None（解析失敗）或成功解析（如果實作有容錯）
        result = _parse_score_json(text)
        # 不應拋出例外
        assert result is None or isinstance(result, dict)


class TestLlmScoreItem:
    """llm_score_item 驗證 practicality 正確儲存。"""

    MOCK_RESPONSE = json.dumps({
        "novelty": 17, "impact": 16, "trending": 15,
        "practicality": 14, "blog_worthiness": 13,
        "total": 75, "reason": "Excellent agent framework",
    })

    def test_all_5d_scores_stored(self, scored_item):
        """B3: 5 個維度分數（含 practicality）全部正確儲存。"""
        with patch("src.scoring.scorer.llm_chat", return_value=self.MOCK_RESPONSE):
            result = llm_score_item(scored_item)

        assert result.llm_score == 75
        assert result.novelty == 17
        assert result.impact == 16
        assert result.trending == 15
        assert result.practicality == 14
        assert result.blog_worthiness == 13
        assert result.llm_reason == "Excellent agent framework"

    def test_handles_llm_failure_gracefully(self, scored_item):
        """LLM 呼叫失敗時，item 保持原始狀態不崩潰。"""
        with patch("src.scoring.scorer.llm_chat", side_effect=Exception("Network error")):
            result = llm_score_item(scored_item)
        # 不應拋出例外，item 保持不變
        assert result is not None

    def test_handles_malformed_json_response(self, scored_item):
        """LLM 返回無法解析的回應，不應崩潰。"""
        with patch("src.scoring.scorer.llm_chat", return_value="Sorry, I cannot score this."):
            result = llm_score_item(scored_item)
        assert result is not None


class TestBatchLlmScore:
    MOCK_RESPONSE = json.dumps({
        "novelty": 15, "impact": 15, "trending": 15,
        "practicality": 15, "blog_worthiness": 15,
        "total": 75, "reason": "Good",
    })

    def test_respects_llm_top_k(self, scored_item, sample_config):
        """只對 llm_top_k 個 items 評分。"""
        sample_config["scoring"]["llm_top_k"] = 2
        items = [scored_item] * 5

        call_count = 0
        def mock_llm(**kwargs):
            nonlocal call_count
            call_count += 1
            return self.MOCK_RESPONSE

        with patch("src.scoring.scorer.llm_chat", side_effect=mock_llm):
            with patch("src.scoring.scorer.time.sleep"):
                batch_llm_score(items, sample_config)

        assert call_count == 2

    def test_returns_sorted_by_total_score(self, scored_item, sample_config):
        """結果應按 total_score 降序排列。"""
        responses = [
            json.dumps({"novelty": i, "impact": i, "trending": i,
                       "practicality": i, "blog_worthiness": i,
                       "total": i * 5, "reason": f"score {i}"})
            for i in [10, 5, 15, 8, 12]
        ]
        items = [scored_item] * 5
        sample_config["scoring"]["llm_top_k"] = 5
        sample_config["scoring"]["final_top_k"] = 5

        resp_iter = iter(responses)
        with patch("src.scoring.scorer.llm_chat", side_effect=lambda **kw: next(resp_iter)):
            with patch("src.scoring.scorer.time.sleep"):
                result = batch_llm_score(items, sample_config)

        scores = [r.total_score for r in result]
        assert scores == sorted(scores, reverse=True)

    def test_respects_final_top_k(self, scored_item, sample_config):
        """最終結果數量不超過 final_top_k。"""
        sample_config["scoring"]["llm_top_k"] = 5
        sample_config["scoring"]["final_top_k"] = 2
        items = [scored_item] * 5

        with patch("src.scoring.scorer.llm_chat", return_value=self.MOCK_RESPONSE):
            with patch("src.scoring.scorer.time.sleep"):
                result = batch_llm_score(items, sample_config)

        assert len(result) <= 2
