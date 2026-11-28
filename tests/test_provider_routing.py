"""多 provider 路由測試：Agnes 與 OpenRouter 依 model id 分流。"""

from __future__ import annotations

import pytest

import src.utils as u


class TestProviderInference:
    @pytest.mark.parametrize(
        "model,expected",
        [
            ("agnes-2.0-flash", "agnes"),
            ("agnes-image-2.1-flash", "agnes"),
            ("google/gemma-4-31b-it:free", "openrouter"),
            ("openai/gpt-oss-120b:free", "openrouter"),
            ("openrouter/free", "openrouter"),
            (None, "openrouter"),
            ("", "openrouter"),
        ],
    )
    def test_provider_for_model(self, model, expected):
        assert u._provider_for_model(model) == expected


class TestBaseUrl:
    def test_agnes_default_base_url(self, monkeypatch):
        monkeypatch.delenv("AGNES_API_URL", raising=False)
        assert u._get_api_base_url("agnes") == u._AGNES_DEFAULT_BASE_URL

    def test_agnes_base_url_env_override(self, monkeypatch):
        monkeypatch.setenv("AGNES_API_URL", "https://custom.example/v1")
        assert u._get_api_base_url("agnes") == "https://custom.example/v1"

    def test_openrouter_base_url_default(self, monkeypatch):
        monkeypatch.delenv("OPENROUTER_API_URL", raising=False)
        assert "openrouter.ai" in u._get_api_base_url("openrouter")


class TestKeyRotationIsolation:
    def test_missing_provider_keys_raises_with_helpful_msg(self, monkeypatch):
        # agnes 無 key 時，呼叫 agnes provider 才 raise（lazy），且訊息指向正確 env
        monkeypatch.setitem(u._PROVIDER_CYCLES, "agnes", None)
        with pytest.raises(ValueError, match="AGNES_API_KEY"):
            u.get_next_api_key("agnes")

    def test_openrouter_and_agnes_keys_are_separate_pools(self):
        # 兩個 provider 各自獨立 key 池，不共用
        assert "openrouter" in u._PROVIDER_KEYS
        assert "agnes" in u._PROVIDER_KEYS


class TestOpenAIProvider:
    @pytest.mark.parametrize(
        "model,expected",
        [
            ("gpt-6.1-terra", "openai"),
            ("gpt-6.2-sol", "openai"),
            # OpenRouter 上的 OpenAI 模型帶 vendor 前綴，仍走 OpenRouter
            ("openai/gpt-oss-120b:free", "openrouter"),
        ],
    )
    def test_gpt_models_route_to_openai(self, model, expected):
        assert u._provider_for_model(model) == expected

    def test_openai_base_url_default(self, monkeypatch):
        monkeypatch.delenv("OPENAI_API_URL", raising=False)
        assert u._get_api_base_url("openai") == "https://api.openai.com/v1"

    def test_missing_openai_key_raises_with_helpful_msg(self, monkeypatch):
        monkeypatch.setitem(u._PROVIDER_CYCLES, "openai", None)
        with pytest.raises(ValueError, match="OPENAI_API_KEY"):
            u.get_next_api_key("openai")

    def _capture_create_kwargs(self, monkeypatch, model):
        captured = {}

        class FakeCompletions:
            def create(self, **kw):
                captured.update(kw)
                msg = type("M", (), {"content": "ok"})()
                return type("R", (), {"choices": [type("C", (), {"message": msg})()]})()

        class FakeClient:
            chat = type("Chat", (), {"completions": FakeCompletions()})()

            def with_options(self, **_):
                return self

        monkeypatch.setattr(u, "_client_with_key_index", lambda m: (FakeClient(), 1))
        assert u._try_model(model, [{"role": "user", "content": "hi"}], 1200, 0.3, 0) == "ok"
        return captured

    def test_openai_uses_max_completion_tokens_and_default_temperature(self, monkeypatch):
        # gpt-6.x 拒收 max_tokens 與非預設 temperature（2026-11-28 實打 API 確認）
        kw = self._capture_create_kwargs(monkeypatch, "gpt-6.1-terra")
        assert kw["max_completion_tokens"] == 1200
        assert "max_tokens" not in kw
        assert "temperature" not in kw

    def test_openrouter_keeps_max_tokens_and_temperature(self, monkeypatch):
        kw = self._capture_create_kwargs(monkeypatch, "openrouter/free")
        assert kw["max_tokens"] == 1200
        assert kw["temperature"] == 0.3
