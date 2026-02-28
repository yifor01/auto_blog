"""Per-stage pipeline API 測試。"""

from __future__ import annotations

import json
from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

import src.web.app as app_module
from src.web.app import app


# ──────────────────────────────────────────────────────────
# Fixtures
# ──────────────────────────────────────────────────────────

@pytest.fixture(autouse=True)
def mock_data_service(monkeypatch):
    """Mock data_service 函式，避免讀取真實檔案系統。"""
    mock_ds = MagicMock()
    mock_ds.get_week_status.return_value = []
    mock_ds.get_week_top_items.return_value = []
    mock_ds.get_dashboard_charts.return_value = {}
    mock_ds.get_sidebar_stats.return_value = {}
    mock_ds.get_pipeline_state.return_value = "none"
    monkeypatch.setattr(app_module, "ds", mock_ds)
    return mock_ds


@pytest.fixture(autouse=True)
def mock_config_manager(monkeypatch):
    """Mock config_manager 函式，避免讀取真實 config 檔。"""
    mock_cm = MagicMock()
    mock_cm.get_config.return_value = {}
    mock_cm.get_env_values.return_value = {}
    mock_cm.init_config.return_value = None
    monkeypatch.setattr(app_module, "cm", mock_cm)
    return mock_cm


@pytest.fixture
def client():
    """建立 FastAPI TestClient。"""
    with TestClient(app, raise_server_exceptions=True) as c:
        yield c


# ──────────────────────────────────────────────────────────
# 測試 1：invalid stage 回 400
# ──────────────────────────────────────────────────────────

def test_run_stage_invalid(client):
    """POST /api/run/{date}/stage/{invalid} 回 400"""
    res = client.post("/api/run/2026-01-01/stage/invalid_stage")
    assert res.status_code == 400


# ──────────────────────────────────────────────────────────
# 測試 2：pipeline 已在執行時回 409
# ──────────────────────────────────────────────────────────

def test_run_stage_409_when_running(client, monkeypatch):
    """POST /api/run/{date}/stage/{stage} 當 pipeline 在執行中時回 409"""
    monkeypatch.setattr(app_module, "RUNNING_TASKS", {"2026-01-01"})
    res = client.post("/api/run/2026-01-01/stage/collect")
    assert res.status_code == 409


# ──────────────────────────────────────────────────────────
# 測試 3：log 不存在時回空 entries
# ──────────────────────────────────────────────────────────

def test_stage_log_no_file(client, tmp_path, monkeypatch):
    """GET /api/logs/{date}/stage/{stage} 當 log 不存在時回空 entries"""
    monkeypatch.setattr(app_module, "LOGS_DIR", tmp_path)
    res = client.get("/api/logs/2099-01-01/stage/collect")
    assert res.status_code == 200
    data = res.json()
    assert data["entries"] == []
    assert data["item_count"] is None


# ──────────────────────────────────────────────────────────
# 測試 4：解析 log 的 entries 格式
# ──────────────────────────────────────────────────────────

def test_stage_log_parses_entries(client, tmp_path, monkeypatch):
    """GET /api/logs/{date}/stage/{stage} 解析 JSON log entries"""
    monkeypatch.setattr(app_module, "LOGS_DIR", tmp_path)

    log_lines = [
        json.dumps({"pipeline_stage": "collect", "stage_action": "start", "ts": "2026-01-01T10:00:00"}),
        json.dumps({"ts": "2026-01-01T10:00:01.123", "level": "INFO", "msg": "Collecting items", "pipeline_stage": "other"}),
        json.dumps({"pipeline_stage": "collect", "stage_action": "end", "elapsed": 5.0, "item_count": 10}),
    ]
    log_file = tmp_path / "2026-01-01.log"
    log_file.write_text("\n".join(log_lines), encoding="utf-8")

    res = client.get("/api/logs/2026-01-01/stage/collect")
    assert res.status_code == 200
    data = res.json()
    assert len(data["entries"]) == 1
    assert data["entries"][0]["msg"] == "Collecting items"
    assert data["item_count"] == 10


# ──────────────────────────────────────────────────────────
# 測試 5：stage-info 回傳 item_count
# ──────────────────────────────────────────────────────────

def test_stage_info_item_count(client, tmp_path, monkeypatch):
    """GET /api/logs/{date}/stage-info 回傳正確的 item_count"""
    monkeypatch.setattr(app_module, "LOGS_DIR", tmp_path)

    log_lines = [
        json.dumps({"pipeline_stage": "collect", "stage_action": "start"}),
        json.dumps({"pipeline_stage": "collect", "stage_action": "end", "elapsed": 3.0, "item_count": 15}),
        json.dumps({"pipeline_stage": "score", "stage_action": "start"}),
        json.dumps({"pipeline_stage": "score", "stage_action": "end", "elapsed": 20.0, "item_count": 0}),
    ]
    log_file = tmp_path / "2026-01-01.log"
    log_file.write_text("\n".join(log_lines), encoding="utf-8")

    res = client.get("/api/logs/2026-01-01/stage-info")
    assert res.status_code == 200
    data = res.json()
    stages = {s["name"]: s for s in data["stages"]}
    assert stages["collect"]["item_count"] == 15
    assert stages["score"]["item_count"] == 0
