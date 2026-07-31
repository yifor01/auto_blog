"""llm_chat / _try_model 穩健性測試（lazy retire + 上游 429 偵測 + key 輪替，全 mock）。"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

import src.utils as utils
from src.utils import _try_model, _upstream_provider, llm_chat, reset_model_health


@pytest.fixture(autouse=True)
def _reset_health():
    """每個測試前後清空 retired set / 快取 chain / 緊急 discover flag，避免污染。"""
    reset_model_health()
    yield
    reset_model_health()


def _make_resp(content: str):
    resp = MagicMock()
    resp.choices[0].message.content = content
    return resp


def _make_client(side_effect):
    """建立 mock client：client.with_options(timeout=...).chat.completions.create(...)。

    回傳 (client, captured)，captured["timeout"] 記錄最後一次傳入的 timeout。
    """
    client = MagicMock()
    captured: dict = {}
    inner = MagicMock()
    inner.chat.completions.create.side_effect = side_effect

    def with_options(**kwargs):
        captured["timeout"] = kwargs.get("timeout")
        return inner

    client.with_options.side_effect = with_options
    return client, captured


def _patch_client(client, key_idx: int = 1):
    """把 _try_model 內部的 client 建構 patch 成固定 (client, key_idx)。"""
    return patch("src.utils._client_with_key_index", return_value=(client, key_idx))


class _Fake404(Exception):
    def __init__(self):
        super().__init__("Error code: 404 - model not found")
        self.status_code = 404


class _FakeUpstream429(Exception):
    """上游池限流：body 帶 provider_name。"""

    def __init__(self):
        super().__init__("429 Provider returned error")
        self.status_code = 429
        self.body = {
            "error": {
                "code": 429,
                "message": "Provider returned error",
                "metadata": {"provider_name": "Venice", "raw": "temporarily rate-limited upstream"},
            }
        }


def _exc_with_body(body):
    e = Exception("boom")
    e.body = body
    return e


class TestUpstreamProvider:
    def test_standard_shape(self):
        e = _exc_with_body({"error": {"code": 429, "metadata": {"provider_name": "Venice"}}})
        assert _upstream_provider(e) == "Venice"

    def test_inner_error_shape(self):
        # SDK 有時把 error 內層直接當 body
        e = _exc_with_body({"code": 429, "metadata": {"provider_name": "Chutes"}})
        assert _upstream_provider(e) == "Chutes"

    def test_shape_without_metadata_returns_none(self):
        e = _exc_with_body({"error": {"code": 429}})
        assert _upstream_provider(e) is None

    def test_non_dict_body_returns_none(self):
        assert _upstream_provider(_exc_with_body("oops")) is None

    def test_no_body_returns_none(self):
        assert _upstream_provider(Exception("plain")) is None

    def test_empty_provider_name_returns_none(self):
        e = _exc_with_body({"error": {"metadata": {"provider_name": ""}}})
        assert _upstream_provider(e) is None


class TestTryModelBackoff:
    def test_429_exponential_backoff_waits(self):
        """我方額度 429 重試採指數退避：5 → 10。"""
        side = [Exception("429 rate limit"), Exception("429 rate limit"), _make_resp("ok")]
        client, _ = _make_client(side)
        with _patch_client(client), patch("src.utils.time.sleep") as mock_sleep:
            result = _try_model("m", [], 100, 0.5, max_retries=2)
        assert result == "ok"
        waits = [c.args[0] for c in mock_sleep.call_args_list]
        assert waits == [5, 10]

    def test_429_backoff_caps_at_60(self):
        """指數退避上限 60 秒：5,10,20,40,60。"""
        side = [Exception("429")] * 6
        client, _ = _make_client(side)
        with _patch_client(client), patch("src.utils.time.sleep") as mock_sleep:
            result = _try_model("m", [], 100, 0.5, max_retries=5)
        assert result is None
        waits = [c.args[0] for c in mock_sleep.call_args_list]
        assert waits == [5, 10, 20, 40, 60]

    def test_429_retry_rotates_key(self):
        """我方額度 429 重試時每次 attempt 換一把新 key（序號輪替）。"""
        side = [Exception("429"), Exception("429"), _make_resp("ok")]
        client, _ = _make_client(side)
        seen_idx: list[int] = []
        idx_iter = iter([1, 2, 3])

        def fake_client(model):
            i = next(idx_iter)
            seen_idx.append(i)
            return client, i

        with patch("src.utils._client_with_key_index", side_effect=fake_client), \
             patch("src.utils.time.sleep"):
            result = _try_model("m", [], 100, 0.5, max_retries=2)
        assert result == "ok"
        assert seen_idx == [1, 2, 3]  # 每次 attempt 都重取 key


class TestTryModelRetire:
    def test_upstream_429_retires_and_no_sleep(self):
        """上游池限流 → 加入 _RETIRED_MODELS、零 sleep、直接回 None。"""
        client, _ = _make_client([_FakeUpstream429()])
        with _patch_client(client), patch("src.utils.time.sleep") as mock_sleep:
            result = _try_model("up-model", [], 100, 0.5, max_retries=2)
        assert result is None
        assert "up-model" in utils._RETIRED_MODELS
        mock_sleep.assert_not_called()

    def test_404_retires_model(self):
        """404 下架 → retire。"""
        client, _ = _make_client([_Fake404()])
        with _patch_client(client), patch("src.utils.time.sleep") as mock_sleep:
            result = _try_model("dead-model", [], 100, 0.5, max_retries=2)
        assert result is None
        assert "dead-model" in utils._RETIRED_MODELS
        mock_sleep.assert_not_called()


class TestTryModelTimeout:
    def test_timeout_passed_to_client(self):
        client, captured = _make_client([_make_resp("ok")])
        with _patch_client(client):
            _try_model("m", [], 100, 0.5, max_retries=0, timeout=42.0)
        assert captured["timeout"] == 42.0

    def test_timeout_exception_treated_as_failure(self):
        """timeout 例外（非 429）視為該 model 失敗回 None，不重試、不 retire。"""
        side = [TimeoutError("request timed out")]
        client, _ = _make_client(side)
        with _patch_client(client), patch("src.utils.time.sleep") as mock_sleep:
            result = _try_model("m", [], 100, 0.5, max_retries=2)
        assert result is None
        assert "m" not in utils._RETIRED_MODELS
        mock_sleep.assert_not_called()


class TestLlmChatChain:
    def test_continues_to_next_model_on_failure(self):
        """第一個 model 失敗，應繼續走 fallback 鏈拿到第二個結果。"""
        with patch("src.utils._get_chain", return_value=["m1", "m2"]), \
             patch("src.utils._try_model", side_effect=[None, "second"]):
            result = llm_chat([{"role": "user", "content": "hi"}])
        assert result == "second"

    def test_all_fail_returns_empty(self):
        with patch("src.utils._get_chain", return_value=["m1", "m2"]), \
             patch("src.utils._try_model", return_value=None):
            result = llm_chat([{"role": "user", "content": "hi"}])
        assert result == ""

    def test_default_timeout_from_config(self):
        """timeout=None 時應讀 config llm.timeout_seconds（讀不到用 60）並傳給 _try_model。"""
        captured: dict = {}

        def fake_try(model, messages, max_tokens, temperature, max_retries, timeout):
            captured["timeout"] = timeout
            return "x"

        fake_cfg = {"llm": {"timeout_seconds": 77}}
        with patch("src.utils._get_chain", return_value=["m1"]), \
             patch("src.utils.load_config", return_value=fake_cfg), \
             patch("src.utils._try_model", side_effect=fake_try):
            llm_chat([{"role": "user", "content": "hi"}])
        assert captured["timeout"] == 77

    def test_skips_retired_model(self):
        """chain 中已 retired 的 model 應被過濾，不會嘗試。"""
        utils._RETIRED_MODELS.add("m1")
        called: list[str] = []

        def fake_try(model, *a):
            called.append(model)
            return "ok" if model == "m2" else None

        with patch("src.utils._get_chain", return_value=["m1", "m2"]), \
             patch("src.utils._try_model", side_effect=fake_try):
            result = llm_chat([{"role": "user", "content": "hi"}])
        assert result == "ok"
        assert called == ["m2"]

    def test_reset_model_health_clears_state(self):
        utils._RETIRED_MODELS.add("x")
        utils._scoring_chain = ["a"]
        utils._generation_chain = ["b"]
        utils._emergency_discovered = True
        reset_model_health()
        assert utils._RETIRED_MODELS == set()
        assert utils._scoring_chain is None
        assert utils._generation_chain is None
        assert utils._emergency_discovered is False


class TestLlmChatValidate:
    def test_validate_falls_through_without_retiring(self):
        """第一個 model 輸出爛 → 降級第二個 model 成功；不 retire 第一個 model。"""
        with patch("src.utils._get_chain", return_value=["m1", "m2"]), \
             patch("src.utils._try_model", side_effect=["bad", "good"]):
            result = llm_chat(
                [{"role": "user", "content": "hi"}],
                validate=lambda t: t == "good",
            )
        assert result == "good"
        assert "m1" not in utils._RETIRED_MODELS


class TestLlmChatEmergencyDiscover:
    def test_emergency_discover_triggers_once(self):
        """chain 全空 → 觸發一次 auto-discover；第二次呼叫不再 discover。"""
        with patch("src.utils._get_chain", return_value=[]), \
             patch("src.utils.discover_free_models", return_value=["d1"]) as mock_disc, \
             patch("src.utils._probe_model", return_value=(True, "")), \
             patch("src.utils._try_model", return_value="ok"):
            r1 = llm_chat([{"role": "user", "content": "hi"}])
            llm_chat([{"role": "user", "content": "hi"}])
        assert r1 == "ok"
        assert mock_disc.call_count == 1

    def test_emergency_discover_all_dead_returns_empty(self):
        """discover 到的 model 都 probe 失敗 → 回 ""。"""
        with patch("src.utils._get_chain", return_value=[]), \
             patch("src.utils.discover_free_models", return_value=["d1", "d2"]), \
             patch("src.utils._probe_model", return_value=(False, "dead")), \
             patch("src.utils._try_model", return_value="ok"):
            result = llm_chat([{"role": "user", "content": "hi"}])
        assert result == ""
