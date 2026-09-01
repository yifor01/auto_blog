"""Model health 檢查測試（全 mock，不連外）。

判準本身是「實打 OpenRouter」，所以這裡測的是**分類邏輯**：什麼樣的回應算可用、
什麼算該換掉、什麼是「今天忙」不該換。
"""
from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

from src.model_health import (
    STATUS_BAD_OUTPUT,
    STATUS_BUSY,
    STATUS_ERROR,
    STATUS_GONE,
    STATUS_OK,
    ProbeResult,
    check_scoring_chain,
    probe_scoring_model,
    render_report,
)

VALID = json.dumps({
    "novelty": 12, "impact": 10, "trending": 8,
    "practicality": 15, "blog_worthiness": 13, "reason": "理由",
})


def _client(*contents: str | Exception):
    """回傳一個 mock get_llm_client，依序吐出每次呼叫的結果。"""
    seq = list(contents)

    def create(**_kw):
        item = seq.pop(0) if seq else seq_last
        if isinstance(item, Exception):
            raise item
        resp = MagicMock()
        resp.choices = [MagicMock()]
        resp.choices[0].message.content = item
        return resp

    seq_last = contents[-1] if contents else ""
    client = MagicMock()
    client.with_options.return_value.chat.completions.create.side_effect = create
    return MagicMock(return_value=client)


class TestProbeClassification:
    def test_valid_json_is_ok(self):
        with patch("src.model_health.get_llm_client", _client(VALID)):
            assert probe_scoring_model("m").status == STATUS_OK

    def test_json_in_code_block_is_ok(self):
        with patch("src.model_health.get_llm_client", _client(f"```json\n{VALID}\n```")):
            assert probe_scoring_model("m").status == STATUS_OK

    def test_404_is_gone(self):
        with patch("src.model_health.get_llm_client", _client(Exception("Error code: 404 - unavailable"))):
            r = probe_scoring_model("m")
        assert r.status == STATUS_GONE

    def test_429_is_busy_not_broken(self):
        """限流是「今天忙」，不是該換掉的理由——換 model 治不了上游池滿載。"""
        err = Exception("Error code: 429 - Provider returned error, provider_name: Google AI Studio")
        with patch("src.model_health.get_llm_client", _client(err)):
            r = probe_scoring_model("m")
        assert r.status == STATUS_BUSY
        assert "上游池限流" in r.detail

    def test_empty_content_is_bad_output(self):
        with patch("src.model_health.get_llm_client", _client("", "")):
            r = probe_scoring_model("m")
        assert r.status == STATUS_BAD_OUTPUT
        assert "空字串" in r.detail

    def test_reasoning_leak_is_bad_output(self):
        """_probe_model 的 "Reply with OK" 抓不到這種，所以才要用真實評分 prompt。"""
        leak = "Here's a thinking process:\n\n1. Analyze the user request..."
        with patch("src.model_health.get_llm_client", _client(leak, leak)):
            r = probe_scoring_model("m")
        assert r.status == STATUS_BAD_OUTPUT

    def test_missing_dimension_is_bad_output(self):
        partial = json.dumps({"novelty": 10, "impact": 10, "reason": "只有兩維"})
        with patch("src.model_health.get_llm_client", _client(partial, partial)):
            r = probe_scoring_model("m")
        assert r.status == STATUS_BAD_OUTPUT
        assert "缺維度" in r.detail

    def test_other_exception_is_error(self):
        with patch("src.model_health.get_llm_client", _client(Exception("connection reset"))):
            assert probe_scoring_model("m").status == STATUS_ERROR


class TestProbeRetry:
    def test_second_attempt_can_rescue(self):
        """openrouter/free 每次呼叫隨機換 model，單次 probe 等於擲骰子。"""
        with patch("src.model_health.get_llm_client", _client("", VALID)):
            assert probe_scoring_model("openrouter/free").status == STATUS_OK

    def test_gone_does_not_retry(self):
        exc = Exception("Error code: 404")
        client = _client(exc, VALID)
        with patch("src.model_health.get_llm_client", client):
            assert probe_scoring_model("m").status == STATUS_GONE

    def test_busy_does_not_retry(self):
        exc = Exception("Error code: 429")
        with patch("src.model_health.get_llm_client", _client(exc, VALID)):
            assert probe_scoring_model("m").status == STATUS_BUSY

    def test_attempts_configurable(self):
        with patch("src.model_health.get_llm_client", _client("", "", VALID)):
            assert probe_scoring_model("m", attempts=3).status == STATUS_OK


class TestCheckScoringChain:
    CFG = {"llm": {"scoring_models": ["a", "b"]}}

    def test_healthy_chain_probes_no_candidates(self):
        """chain 健康時不去探索免費池——那會白燒每日額度。"""
        with patch("src.model_health.probe_scoring_model",
                   side_effect=lambda m, *a, **k: ProbeResult(m, STATUS_OK)), \
             patch("src.model_health.discover_free_models") as disc:
            out = check_scoring_chain(self.CFG)
        disc.assert_not_called()
        assert out["broken"] == []
        assert [r.model for r in out["configured"]] == ["a", "b"]

    def test_busy_alone_does_not_trigger_discovery(self):
        with patch("src.model_health.probe_scoring_model",
                   side_effect=lambda m, *a, **k: ProbeResult(m, STATUS_BUSY)), \
             patch("src.model_health.discover_free_models") as disc:
            out = check_scoring_chain(self.CFG)
        disc.assert_not_called()
        assert out["broken"] == []

    def test_broken_chain_probes_candidates_excluding_configured(self):
        def fake_probe(m, *a, **k):
            return ProbeResult(m, STATUS_GONE if m == "a" else STATUS_OK)

        with patch("src.model_health.probe_scoring_model", side_effect=fake_probe), \
             patch("src.model_health.discover_free_models", return_value=["a", "c", "d"]):
            out = check_scoring_chain(self.CFG)
        assert [r.model for r in out["broken"]] == ["a"]
        assert [r.model for r in out["candidates"]] == ["c", "d"]  # 已在 chain 的 a 不重複 probe


class TestRenderReport:
    def test_healthy_report_says_nothing_to_change(self):
        out = {"configured": [ProbeResult("a", STATUS_OK, elapsed=1.0)], "candidates": [], "broken": []}
        md = render_report(out)
        assert "沒有需要更換的項目" in md
        assert "`a`" in md

    def test_broken_report_lists_replacements(self):
        out = {
            "configured": [ProbeResult("a", STATUS_GONE, "404")],
            "candidates": [ProbeResult("c", STATUS_OK, elapsed=2.0),
                           ProbeResult("d", STATUS_BAD_OUTPUT, "回空字串")],
            "broken": [ProbeResult("a", STATUS_GONE, "404")],
        }
        md = render_report(out)
        assert "需要更換：1 個" in md
        assert "`c`" in md
        assert "`d`" not in md  # 不可用的候選不該被推薦
        assert "不同上游 provider" in md

    def test_no_usable_candidate_mentions_last_resort(self):
        out = {
            "configured": [ProbeResult("a", STATUS_GONE, "404")],
            "candidates": [ProbeResult("c", STATUS_BAD_OUTPUT, "回空字串")],
            "broken": [ProbeResult("a", STATUS_GONE, "404")],
        }
        assert "openrouter/free" in render_report(out)
