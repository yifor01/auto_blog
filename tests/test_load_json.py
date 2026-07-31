"""測試 load_json 對 corrupt / 缺檔的防禦行為（P1-4）。"""
from __future__ import annotations

import json

from src.utils import load_json, save_json


def test_load_json_missing_file_returns_empty(tmp_path):
    assert load_json(tmp_path / "nope.json") == []


def test_load_json_valid_roundtrip(tmp_path):
    p = tmp_path / "ok.json"
    save_json({"a": 1, "b": ["x"]}, p)
    assert load_json(p) == {"a": 1, "b": ["x"]}


def test_load_json_corrupt_returns_empty_not_raise(tmp_path):
    """corrupt / merge-conflict 殘留的 JSON 不該炸掉整天的 run，回 []。"""
    p = tmp_path / "corrupt.json"
    p.write_text('{"a": 1, broken <<<<<<< HEAD', encoding="utf-8")
    assert load_json(p) == []


def test_load_json_empty_file_returns_empty(tmp_path):
    p = tmp_path / "empty.json"
    p.write_text("", encoding="utf-8")
    assert load_json(p) == []
