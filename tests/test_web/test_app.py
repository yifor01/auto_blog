"""Pipeline API 測試（PipelineRun in-memory state 重寫版）。"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

import src.web.app as app_module
from src.web.app import (
    app,
    PipelineRun,
    StageInfo,
    _finalize_run,
    _run_stage_pipeline,
)


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


@pytest.fixture(autouse=True)
def clean_runs(monkeypatch):
    """每次測試前清空 _runs，避免跨測試污染。"""
    monkeypatch.setattr(app_module, "_runs", {})


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
    monkeypatch.setattr(app_module, "_runs", {
        "2026-01-01": PipelineRun(status="running"),
    })
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
# 測試 5：stage-info 從 in-memory _runs 回傳（有完成的 PipelineRun）
# ──────────────────────────────────────────────────────────

def test_stage_info_from_memory(client, monkeypatch):
    """stage-info 應直接從 _runs 回傳完成的 pipeline 狀態"""
    run = PipelineRun(status="done", log_offset=0)
    run.stages["collect"] = StageInfo(status="done", elapsed=3.0, item_count=15)
    run.stages["score"] = StageInfo(status="done", elapsed=20.0, item_count=0)
    run.stages["generate"] = StageInfo(status="done", elapsed=10.0, item_count=3)
    monkeypatch.setattr(app_module, "_runs", {"2026-01-01": run})

    res = client.get("/api/logs/2026-01-01/stage-info")
    assert res.status_code == 200
    data = res.json()
    stages = {s["name"]: s for s in data["stages"]}
    assert stages["collect"]["item_count"] == 15
    assert stages["score"]["item_count"] == 0
    assert stages["generate"]["item_count"] == 3
    assert data["pipeline_status"] == "done"
    assert "log_offset" not in data  # done 時不回傳 log_offset


# ──────────────────────────────────────────────────────────
# 測試 6：stage-info fallback 到 data files（無 _runs entry）
# ──────────────────────────────────────────────────────────

def test_stage_info_fallback_to_data_files(client, mock_data_service, monkeypatch):
    """stage-info 無 _runs entry 時應 fallback 到 data file 推算"""
    monkeypatch.setattr(app_module, "_runs", {})
    mock_data_service.get_pipeline_state.return_value = "scored"

    res = client.get("/api/logs/2026-01-01/stage-info")
    assert res.status_code == 200
    data = res.json()
    stages = {s["name"]: s for s in data["stages"]}
    assert stages["collect"]["status"] == "done"
    assert stages["score"]["status"] == "done"
    assert stages["generate"]["status"] == "pending"
    assert data["pipeline_status"] == "scored"


# ──────────────────────────────────────────────────────────
# 測試 7：stage-info running 時回傳 log_offset
# ──────────────────────────────────────────────────────────

def test_stage_info_running_returns_log_offset(client, monkeypatch):
    """stage-info running 狀態應包含 log_offset"""
    run = PipelineRun(status="running", log_offset=1234)
    run.stages["collect"] = StageInfo(status="running")
    monkeypatch.setattr(app_module, "_runs", {"2026-01-01": run})

    res = client.get("/api/logs/2026-01-01/stage-info")
    assert res.status_code == 200
    data = res.json()
    assert data["pipeline_status"] == "running"
    assert data["log_offset"] == 1234


# ──────────────────────────────────────────────────────────
# 測試 8：day_detail 路由使用 list_day_contents
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
    assert "content-badge-blog" in res.text
    assert "Test Post" in res.text
    mock_data_service.list_posts.assert_not_called()
    mock_data_service.list_notes.assert_not_called()


# ──────────────────────────────────────────────────────────
# 測試 9：generate stage 重跑時刪除舊輸出檔案
# ──────────────────────────────────────────────────────────

def test_run_stage_generate_deletes_old_files(tmp_path: Path, monkeypatch):
    """_run_stage_pipeline 執行 generate stage 時，應刪除舊輸出。"""
    date_str = "2026-03-02"

    posts_dir = tmp_path / "posts"
    notes_dir = tmp_path / "notes"
    prompts_dir = tmp_path / "prompts"
    logs_dir = tmp_path / "logs"
    for d in (posts_dir, notes_dir, prompts_dir, logs_dir):
        d.mkdir(parents=True)

    old_post = posts_dir / f"{date_str}_old-post.md"
    old_note = notes_dir / f"{date_str}_old-note.md"
    old_prompt = prompts_dir / f"{date_str}_old-prompt.md"
    other_post = posts_dir / "2026-01-01_other-post.md"
    for f in (old_post, old_note, old_prompt, other_post):
        f.write_text("dummy content", encoding="utf-8")

    monkeypatch.setattr(app_module, "POSTS_DIR", posts_dir)
    monkeypatch.setattr(app_module, "NOTES_DIR", notes_dir)
    monkeypatch.setattr(app_module, "PROMPTS_DIR", prompts_dir)
    monkeypatch.setattr(app_module, "LOGS_DIR", logs_dir)

    # 設定 _runs 中的 PipelineRun（由 api_run_stage 預先建立）
    run = PipelineRun(status="running", log_offset=0)
    monkeypatch.setattr(app_module, "_runs", {date_str: run})

    mock_proc = MagicMock()
    mock_proc.wait.return_value = None
    mock_proc.returncode = 0
    mock_proc.poll.return_value = 0

    with patch("subprocess.Popen", return_value=mock_proc):
        thread = threading.Thread(target=_run_stage_pipeline, args=(date_str, "generate"))
        thread.start()
        thread.join(timeout=5)

    assert not old_post.exists(), "舊 post 檔案應被刪除"
    assert not old_note.exists(), "舊 note 檔案應被刪除"
    assert not old_prompt.exists(), "舊 prompt 檔案應被刪除"
    assert other_post.exists(), "其他日期的 post 檔案不應被刪除"

    # run 應被 finalize 為 done
    assert app_module._runs[date_str].status == "done"


# ──────────────────────────────────────────────────────────
# 測試 10：api_run_stage 成功時回傳 log_offset（無 log 檔）
# ──────────────────────────────────────────────────────────

def test_run_stage_returns_log_offset_zero_when_no_log(client, tmp_path, monkeypatch):
    """POST /api/run/{date}/stage/{stage} 無 log 檔時 log_offset 為 0"""
    monkeypatch.setattr(app_module, "LOGS_DIR", tmp_path)
    with patch("src.web.app._run_stage_pipeline"):
        res = client.post("/api/run/2026-01-01/stage/collect")
    assert res.status_code == 200
    data = res.json()
    assert "log_offset" in data
    assert data["log_offset"] == 0


# ──────────────────────────────────────────────────────────
# 測試 11：api_run_stage 成功時回傳 log_offset（有 log 檔）
# ──────────────────────────────────────────────────────────

def test_run_stage_returns_log_offset_when_log_exists(client, tmp_path, monkeypatch):
    """POST /api/run/{date}/stage/{stage} 有 log 檔時 log_offset 為 log 大小"""
    monkeypatch.setattr(app_module, "LOGS_DIR", tmp_path)
    log_file = tmp_path / "2026-01-01.log"
    log_file.write_text("existing content", encoding="utf-8")
    expected_offset = log_file.stat().st_size
    with patch("src.web.app._run_stage_pipeline"):
        res = client.post("/api/run/2026-01-01/stage/collect")
    assert res.status_code == 200
    data = res.json()
    assert data["log_offset"] == expected_offset


# ──────────────────────────────────────────────────────────
# 測試 12：負數 offset 應回傳 422
# ──────────────────────────────────────────────────────────

def test_logs_stream_rejects_negative_offset(client):
    """GET /api/logs/{date}/stream?from=-1 應回傳 422 驗證錯誤"""
    res = client.get("/api/logs/2026-01-01/stream?from=-1")
    assert res.status_code == 422


# ──────────────────────────────────────────────────────────
# 測試 13：triggerRun 409 不應觸發 SSE（回歸測試需要前端，這裡測 API）
# ──────────────────────────────────────────────────────────

def test_api_run_returns_409_with_detail(client, monkeypatch):
    """POST /api/run/{date} 在 pipeline 執行中應回 409 含 detail"""
    monkeypatch.setattr(app_module, "_runs", {
        "2026-01-01": PipelineRun(status="running"),
    })
    res = client.post("/api/run/2026-01-01")
    assert res.status_code == 409
    data = res.json()
    assert "detail" in data
    assert "已在執行中" in data["detail"]


# ──────────────────────────────────────────────────────────
# 測試 14：_finalize_run 正確解析 pipeline_stage JSON
# ──────────────────────────────────────────────────────────

def test_finalize_run_parses_log(tmp_path, monkeypatch, mock_data_service):
    """_finalize_run 應從 log 解析 stage elapsed 和 item_count"""
    log_path = tmp_path / "2026-01-01.log"
    log_lines = [
        "=== Pipeline started: 2026-01-01 (force=False) ===",
        json.dumps({"pipeline_stage": "collect", "stage_action": "start"}),
        json.dumps({"pipeline_stage": "collect", "stage_action": "end", "elapsed": 3.5, "item_count": 12}),
        json.dumps({"pipeline_stage": "score", "stage_action": "start"}),
        json.dumps({"pipeline_stage": "score", "stage_action": "end", "elapsed": 18.2, "item_count": 8}),
        "=== Pipeline finished: exit_code=0 ===",
    ]
    log_path.write_text("\n".join(log_lines), encoding="utf-8")

    run = PipelineRun(status="running", log_offset=0)
    _finalize_run(run, log_path, "2026-01-01", "done")

    assert run.status == "done"
    assert run.proc is None
    assert run.stages["collect"].status == "done"
    assert run.stages["collect"].elapsed == 3.5
    assert run.stages["collect"].item_count == 12
    assert run.stages["score"].status == "done"
    assert run.stages["score"].elapsed == 18.2
    assert run.stages["score"].item_count == 8
    assert run.stages["generate"].status == "pending"


# ──────────────────────────────────────────────────────────
# 測試 15：_finalize_run 呼叫 3 個 cache invalidation 函數
# ──────────────────────────────────────────────────────────

def test_finalize_run_invalidates_caches(tmp_path, monkeypatch, mock_data_service):
    """_finalize_run 應呼叫 3 個 cache invalidation 函數"""
    log_path = tmp_path / "2026-01-01.log"
    log_path.write_text("=== Pipeline finished: exit_code=0 ===\n", encoding="utf-8")

    run = PipelineRun(status="running", log_offset=0)
    _finalize_run(run, log_path, "2026-01-01", "done")

    mock_data_service.invalidate_scored_cache.assert_called_once_with("2026-01-01")
    mock_data_service.invalidate_sidebar_cache.assert_called_once()
    mock_data_service.invalidate_search_index.assert_called_once()


# ──────────────────────────────────────────────────────────
# 測試 16：_finalize_run 失敗時標記 running stages 為 failed
# ──────────────────────────────────────────────────────────

def test_finalize_run_marks_running_stages_on_failure(tmp_path, monkeypatch, mock_data_service):
    """_finalize_run 以 failed 狀態完成時，running stages 應被標為 failed"""
    log_path = tmp_path / "2026-01-01.log"
    log_path.write_text("", encoding="utf-8")

    run = PipelineRun(status="running", log_offset=0)
    run.stages["collect"] = StageInfo(status="done", elapsed=3.0, item_count=10)
    run.stages["score"] = StageInfo(status="running")  # 仍在 running
    _finalize_run(run, log_path, "2026-01-01", "failed")

    assert run.status == "failed"
    assert run.stages["collect"].status == "done"  # 已完成的不受影響
    assert run.stages["score"].status == "failed"  # running → failed
    assert run.stages["generate"].status == "pending"  # pending 不受影響


# ──────────────────────────────────────────────────────────
# 測試 17：api_run 建立 eager PipelineRun
# ──────────────────────────────────────────────────────────

def test_api_run_creates_eager_pipeline_run(client, monkeypatch):
    """POST /api/run/{date} 應在 _runs 中建立 PipelineRun（eager）"""
    with patch("src.web.app._run_pipeline"):
        res = client.post("/api/run/2026-01-01")
    assert res.status_code == 200
    assert "2026-01-01" in app_module._runs
    assert app_module._runs["2026-01-01"].status == "running"


# ──────────────────────────────────────────────────────────
# 測試 18：api_run_stage 重用已存在的 PipelineRun
# ──────────────────────────────────────────────────────────

def test_api_run_stage_reuses_existing_run(client, tmp_path, monkeypatch):
    """api_run_stage 應重用已完成的 PipelineRun，只重設目標 stage"""
    monkeypatch.setattr(app_module, "LOGS_DIR", tmp_path)
    existing_run = PipelineRun(status="done", log_offset=0)
    existing_run.stages["collect"] = StageInfo(status="done", elapsed=3.0, item_count=10)
    existing_run.stages["score"] = StageInfo(status="done", elapsed=20.0, item_count=5)
    existing_run.stages["generate"] = StageInfo(status="done", elapsed=10.0, item_count=3)
    monkeypatch.setattr(app_module, "_runs", {"2026-01-01": existing_run})

    with patch("src.web.app._run_stage_pipeline"):
        res = client.post("/api/run/2026-01-01/stage/collect")
    assert res.status_code == 200

    run = app_module._runs["2026-01-01"]
    assert run.status == "running"
    assert run.stages["collect"].status == "pending"  # 重設
    assert run.stages["score"].status == "done"  # 保留
    assert run.stages["generate"].status == "done"  # 保留
