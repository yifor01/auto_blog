"""測試 config_manager 的讀寫功能。"""
from __future__ import annotations

import os
from pathlib import Path

import pytest
import yaml


@pytest.fixture(autouse=True)
def reset_config():
    """每個測試前後重設 _config，防止測試間汙染。"""
    import src.web.config_manager as cm
    cm._config = {}
    yield
    cm._config = {}


@pytest.fixture
def tmp_env(tmp_path):
    """建立 .env 測試檔。"""
    env_file = tmp_path / ".env"
    env_file.write_text(
        "OPENROUTER_API_KEY=sk-test-123\n"
        "OPENROUTER_API_URL=https://openrouter.ai/api/v1\n"
        "# 這是注釋\n",
        encoding="utf-8",
    )
    return env_file


@pytest.fixture
def tmp_config(tmp_path):
    """建立 config.yaml 測試檔。"""
    cfg = {
        "llm": {
            "model": "test-model",
            "fallback_model": "fallback-model",
            "max_tokens": 4096,
            "request_delay_seconds": 0.5,
        },
        "scoring": {
            "rule_threshold": 25,
            "llm_top_k": 30,
            "final_top_k": 10,
            "hf_upvote_bonus_threshold": 10,
            "github_stars_high": 100,
            "github_stars_medium": 50,
        },
        "dedup": {"lookback_days": 7},
        "retention_days": 90,
    }
    config_file = tmp_path / "config.yaml"
    with open(config_file, "w") as f:
        yaml.dump(cfg, f, allow_unicode=True)
    return config_file


def test_init_config_loads_yaml(tmp_config, tmp_env, monkeypatch):
    """init_config 應將 config.yaml 載入 _config。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "CONFIG_PATH", tmp_config)
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm.init_config()
    cfg = cm.get_config()
    assert cfg["llm"]["model"] == "test-model"
    assert cfg["scoring"]["rule_threshold"] == 25


def test_get_env_values(tmp_config, tmp_env, monkeypatch):
    """get_env_values 應讀取 .env 中的 API 設定。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "CONFIG_PATH", tmp_config)
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm.init_config()
    env = cm.get_env_values()
    assert env["api_key"] == "sk-test-123"
    assert "openrouter.ai" in env["api_url"]


def test_write_env_updates_existing_key(tmp_env, monkeypatch):
    """_write_env 應替換現有 KEY=VALUE 行，並保留注釋行。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm._write_env({"OPENROUTER_API_KEY": "sk-new-456"})
    content = tmp_env.read_text(encoding="utf-8")
    assert "sk-new-456" in content
    assert "sk-test-123" not in content
    assert "# 這是注釋" in content  # 注釋行保留


def test_write_env_appends_new_key(tmp_env, monkeypatch):
    """_write_env 當 key 不存在時應 append 到末尾。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm._write_env({"NEW_KEY": "new-value"})
    content = tmp_env.read_text(encoding="utf-8")
    assert "NEW_KEY=new-value" in content


def test_update_and_save_writes_config(tmp_config, tmp_env, monkeypatch):
    """update_and_save 應更新 memory 並寫回 config.yaml。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "CONFIG_PATH", tmp_config)
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm.init_config()
    cm.update_and_save({"scoring.rule_threshold": 30}, {})
    # memory 已更新
    assert cm.get_config()["scoring"]["rule_threshold"] == 30
    # 磁碟已更新
    with open(tmp_config) as f:
        disk = yaml.safe_load(f)
    assert disk["scoring"]["rule_threshold"] == 30


def test_update_and_save_writes_env(tmp_config, tmp_env, monkeypatch):
    """update_and_save 應更新 .env 中的 API key。"""
    import src.web.config_manager as cm
    monkeypatch.setattr(cm, "CONFIG_PATH", tmp_config)
    monkeypatch.setattr(cm, "ENV_PATH", tmp_env)
    cm.init_config()
    cm.update_and_save({}, {"OPENROUTER_API_KEY": "sk-updated"})
    content = tmp_env.read_text(encoding="utf-8")
    assert "sk-updated" in content
