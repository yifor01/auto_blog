"""In-memory config manager — 供 Settings 頁面讀寫 config.yaml 與 .env。"""
from __future__ import annotations

import copy
import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import dotenv_values, load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = PROJECT_ROOT / "config.yaml"
ENV_PATH = PROJECT_ROOT / ".env"

_config: dict = {}


def init_config() -> None:
    """App 啟動時呼叫一次，將 config.yaml 載入 memory。"""
    global _config
    load_dotenv(ENV_PATH)
    with open(CONFIG_PATH, encoding="utf-8") as f:
        _config = yaml.safe_load(f) or {}


def get_config() -> dict:
    """回傳 in-memory config 的 deep copy。"""
    return copy.deepcopy(_config)


def get_env_values() -> dict[str, str]:
    """讀取 .env 中的 API 相關設定。直接讀檔以避免 os.getenv 快取問題。"""
    vals = dotenv_values(ENV_PATH) if ENV_PATH.exists() else {}
    return {
        "api_key": vals.get("OPENROUTER_API_KEY", os.getenv("OPENROUTER_API_KEY", "")),
        "api_url": vals.get("OPENROUTER_API_URL", os.getenv("OPENROUTER_API_URL", "")),
        "newsapi_key": vals.get("NEWSAPI_KEY", os.getenv("NEWSAPI_KEY", "")),
    }


_ALLOWED_KEY_PREFIXES = ("llm.", "scoring.", "dedup.", "generation.", "collectors.")
_ALLOWED_EXACT_KEYS = {"retention_days"}


def update_and_save(config_updates: dict[str, Any], env_updates: dict[str, str]) -> None:
    """更新 in-memory config，並 flush 到 config.yaml + .env。Atomic：失敗時還原 snapshot。"""
    global _config
    snapshot = copy.deepcopy(_config)
    try:
        _apply_nested(config_updates)
        _write_config_yaml()
        if env_updates:
            _write_env(env_updates)
        load_dotenv(ENV_PATH, override=True)
    except Exception:
        _config = snapshot
        raise


def _apply_nested(updates: dict[str, Any]) -> None:
    """將 "a.b.c": value 格式的更新寫入 _config。只允許白名單 key。"""
    for dotted_key, value in updates.items():
        if dotted_key not in _ALLOWED_EXACT_KEYS and not any(
            dotted_key.startswith(prefix) for prefix in _ALLOWED_KEY_PREFIXES
        ):
            raise ValueError(
                f"不允許的 config key：'{dotted_key}'。"
                f"允許的前綴：{list(_ALLOWED_KEY_PREFIXES)}；允許的完整 key：{list(_ALLOWED_EXACT_KEYS)}"
            )
        keys = dotted_key.split(".")
        d = _config
        for k in keys[:-1]:
            d = d.setdefault(k, {})
        d[keys[-1]] = value


def _write_config_yaml() -> None:
    """將 _config 寫回 config.yaml（注意：注釋會被移除）。"""
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.dump(_config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def _write_env(updates: dict[str, str]) -> None:
    """逐行更新 .env：替換現有 KEY=VALUE，找不到則 append；注釋行原樣保留。"""
    if ENV_PATH.exists():
        lines = ENV_PATH.read_text(encoding="utf-8").splitlines()
    else:
        lines = []

    written: set[str] = set()
    new_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped and not stripped.startswith("#") and "=" in stripped:
            key = stripped.split("=", 1)[0].strip()
            if key in updates:
                new_lines.append(f"{key}={updates[key].replace(chr(10), '').replace(chr(13), '')}")
                written.add(key)
                continue
        new_lines.append(line)

    for key, val in updates.items():
        if key not in written:
            new_lines.append(f"{key}={val.replace(chr(10), '').replace(chr(13), '')}")

    ENV_PATH.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
