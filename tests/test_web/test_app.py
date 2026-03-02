"""Per-stage pipeline API 測試。"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

import src.web.app as app_module
from src.web.app import app, _run_stage_pipeline


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
    mock_ds.get_sidebar_stats.return_value = {
        "total_posts": 0, "total_notes": 0, "today_posts": 0,
        "today_notes": 0, "total_materials": 0, "bookmarks_count": 0,
    }
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


# ──────────────────────────────────────────────────────────
# 測試 6：day_detail 路由使用 list_day_contents
# ──────────────────────────────────────────────────────────

def test_day_detail_uses_contents(client, mock_data_service):
    """GET /day/{date} 傳遞 content_map 到模板，評分列表顯示 Blog/Note badge"""
    mock_data_service.get_day_stats.return_value = {
        "date": "2026-01-01",
        "raw_count": 10,
        "scored_count": 5,
        "posts_count": 2,
        "notes_count": 2,
        "score_dist": [0, 0, 2, 2, 1],
        "score_dist_labels": ["0-20", "20-40", "40-60", "60-80", "80+"],
        "source_counts": {"arXiv": 3, "HN": 2},
    }
    mock_data_service.get_day_items.return_value = [
        {"title": "Test Post", "url": "https://example.com", "source": "arXiv",
         "source_name": "arXiv", "total_score": 80, "rule_score": 30,
         "llm_score": 50, "tags": [], "authors": [], "index": 0},
    ]
    mock_data_service.list_day_contents.return_value = [
        {"title": "Test Post", "slug": "test-post", "has_post": True,
         "has_note": True, "post_slug": "test-post", "note_slug": "test-post",
         "rule_score": 30, "llm_score": 50, "tags": [], "reading_time_min": 3,
         "source_name": "arXiv"},
    ]
    res = client.get("/day/2026-01-01")
    assert res.status_code == 200
    # 產出 badge 在評分列表中顯示
    assert "content-badge-blog" in res.text
    assert "Test Post" in res.text
    # 確認不再使用 list_posts / list_notes
    mock_data_service.list_posts.assert_not_called()
    mock_data_service.list_notes.assert_not_called()


# ──────────────────────────────────────────────────────────
# 測試 7：generate stage 重跑時刪除舊輸出檔案
# ──────────────────────────────────────────────────────────

def test_run_stage_generate_deletes_old_files(tmp_path: Path, monkeypatch):
    """_run_stage_pipeline 執行 generate stage 時，應刪除 POSTS_DIR/NOTES_DIR/PROMPTS_DIR 中符合 {date}*.md 的舊檔案。"""
    date_str = "2026-03-02"

    # 建立三個模擬輸出目錄
    posts_dir = tmp_path / "posts"
    notes_dir = tmp_path / "notes"
    prompts_dir = tmp_path / "prompts"
    logs_dir = tmp_path / "logs"
    for d in (posts_dir, notes_dir, prompts_dir, logs_dir):
        d.mkdir(parents=True)

    # 在每個目錄中建立符合 {date}*.md 的舊檔案（應被刪除）
    old_post = posts_dir / f"{date_str}_old-post.md"
    old_note = notes_dir / f"{date_str}_old-note.md"
    old_prompt = prompts_dir / f"{date_str}_old-prompt.md"
    # 另外放一個不符合日期的檔案（不應被刪除）
    other_post = posts_dir / "2026-01-01_other-post.md"
    for f in (old_post, old_note, old_prompt, other_post):
        f.write_text("dummy content", encoding="utf-8")

    # 替換 app 模組的目錄常數
    monkeypatch.setattr(app_module, "POSTS_DIR", posts_dir)
    monkeypatch.setattr(app_module, "NOTES_DIR", notes_dir)
    monkeypatch.setattr(app_module, "PROMPTS_DIR", prompts_dir)
    monkeypatch.setattr(app_module, "LOGS_DIR", logs_dir)

    # 確保 RUNNING_TASKS 初始為空（避免跨測試污染）
    monkeypatch.setattr(app_module, "RUNNING_TASKS", set())
    monkeypatch.setattr(app_module, "RUNNING_PROCS", {})

    # mock subprocess.Popen，模擬 CLI 立即成功退出（returncode=0）
    mock_proc = MagicMock()
    mock_proc.wait.return_value = None
    mock_proc.returncode = 0
    mock_proc.poll.return_value = 0

    # 在背景執行緒中呼叫，與正式使用方式一致；等待完成後再斷言
    with patch("subprocess.Popen", return_value=mock_proc):
        thread = threading.Thread(target=_run_stage_pipeline, args=(date_str, "generate"))
        thread.start()
        thread.join(timeout=5)

    # 符合 {date}*.md 的舊檔案應已被刪除
    assert not old_post.exists(), "舊 post 檔案應被刪除"
    assert not old_note.exists(), "舊 note 檔案應被刪除"
    assert not old_prompt.exists(), "舊 prompt 檔案應被刪除"

    # 不符合日期的檔案不應被刪除
    assert other_post.exists(), "其他日期的 post 檔案不應被刪除"

    # RUNNING_TASKS 在 finally 中應被清空
    assert date_str not in app_module.RUNNING_TASKS
