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
