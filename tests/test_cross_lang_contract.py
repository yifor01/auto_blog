"""跨語言契約測試（Python 側）。

why 這支存在：`src/web/data_service.py`（Web Monitor）與 `web/src/`（Astro 靜態站）
是「原始資料 box」的兩份平行實作。樣式層刻意不共用，但 URL 正規化與訊號標籤
這兩項**契約**必須逐字一致——對不上的症狀是 box 查不到資料而**整個靜默不渲染**，
沒有 log、沒有 exception。

why 讀共用 fixture 而不是在這裡寫期望值：期望值寫兩份等於把重複搬進測試，
兩邊各自漂移一樣抓不到。期望值只存在 `web/src/__fixtures__/cross-lang-contract.json`，
TS 側 `web/src/cross-lang-contract.test.ts` 讀同一個檔案。
任一端改實作而沒同步 fixture，兩邊會一起紅。
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from src.utils import normalize_url_light
from src.web.data_service import _RAW_SIGNAL_LABELS

FIXTURE_PATH = (
    Path(__file__).resolve().parents[1] / "web" / "src" / "__fixtures__" / "cross-lang-contract.json"
)


def _load_fixture() -> dict:
    # 缺檔一律硬失敗，不 skip：fixture 不見了等於這條防線整個消失。
    assert FIXTURE_PATH.is_file(), f"共用 fixture 不存在：{FIXTURE_PATH}"
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


FIXTURE = _load_fixture()
SHARED = FIXTURE["normalizeUrl"]["shared"]
DIVERGENT = FIXTURE["normalizeUrl"]["divergent"]
SIGNAL_ENTRIES = FIXTURE["signalLabels"]["entries"]


def test_fixture_has_content():
    """避免 fixture 被清空造成「零斷言全綠」。"""
    assert len(SHARED) > 5
    assert len(DIVERGENT) > 0
    assert len(SIGNAL_ENTRIES) > 0


@pytest.mark.parametrize("case", SHARED, ids=[c["note"] for c in SHARED])
def test_normalize_url_light_matches_shared_contract(case):
    """兩端行為相同的案例：TS 側對同一批輸入斷言同一批輸出。"""
    assert normalize_url_light(case["input"]) == case["expected"]


@pytest.mark.parametrize("case", DIVERGENT, ids=[c["input"] for c in DIVERGENT])
def test_normalize_url_light_known_divergence(case):
    """已知分歧刻意不修，所以這裡釘的是「Python 端目前的行為」。

    哪天有人把兩端統一（例如 Python 改成錨定的取代），這一筆會 FAIL
    並把人帶回 fixture 與 `normalize_url_light()` 的 docstring 去同步 TS 端。
    """
    assert normalize_url_light(case["input"]) == case["python"]
    # 順帶釘住「分歧確實存在」，避免有人把 fixture 的 ts/python 值改成一樣就當作解決了
    assert case["ts"] != case["python"]


def test_raw_signal_labels_match_fixture():
    """key、標籤文字（含 emoji）與順序都要與 fixture 完全相同。

    整份比對而非逐筆：少一筆、多一筆、順序調換都要被抓到。
    """
    expected = [(e["key"], e["label"]) for e in SIGNAL_ENTRIES]
    assert list(_RAW_SIGNAL_LABELS) == expected
