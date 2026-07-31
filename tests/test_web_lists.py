"""Web data_service 的 lists 讀取測試。"""
from datetime import date

from src.web import data_service

D = date(2026, 7, 21)


def test_get_day_lists_missing_returns_none(tmp_path, monkeypatch):
    # why: 舊日期沒有 lists 檔時應回 None（tab bar 隱藏），不可炸頁面
    monkeypatch.setattr(data_service, "LISTS_DIR", tmp_path)
    assert data_service.get_day_lists(D) is None


def test_get_day_lists_reads_json(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "LISTS_DIR", tmp_path)
    (tmp_path / "2026-07-21.json").write_text(
        '{"date": "2026-07-21", "github": [], "papers": {"hf": [], "others": []}}'
    )
    data = data_service.get_day_lists(D)
    assert data["date"] == "2026-07-21"


def test_get_day_lists_corrupt_returns_none(tmp_path, monkeypatch):
    # why: JSON 損毀時 graceful 降級回 None，並記 warning
    monkeypatch.setattr(data_service, "LISTS_DIR", tmp_path)
    (tmp_path / "2026-07-21.json").write_text("{not valid json")
    assert data_service.get_day_lists(D) is None


def test_get_day_lists_non_dict_returns_none(tmp_path, monkeypatch):
    # why: 格式不符（如 list）也視為無效，回 None
    monkeypatch.setattr(data_service, "LISTS_DIR", tmp_path)
    (tmp_path / "2026-07-21.json").write_text("[1, 2, 3]")
    assert data_service.get_day_lists(D) is None
