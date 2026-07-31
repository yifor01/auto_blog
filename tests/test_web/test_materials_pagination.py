"""素材庫分頁功能測試。

涵蓋：
- 分頁切片正確性
- 超出範圍頁碼處理（page > total_pages → clamp 到最後一頁）
- 篩選 + 分頁組合（篩選在切片前）
- page_size 上限（le=200 防呆）
- 各篩選參數獨立作用
"""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
from fastapi.testclient import TestClient

import src.web.app as app_module
from src.web.app import app


# ──────────────────────────────────────────────────────────
# Helpers / fixtures
# ──────────────────────────────────────────────────────────

def _make_material(
    idx: int,
    *,
    date_str: str = "2026-06-10",
    title: str | None = None,
    source_name: str = "arXiv",
    total_score: float = 50.0,
    has_post: bool = False,
    has_note: bool = False,
    has_blog: bool = False,
    tags: list[str] | None = None,
) -> dict:
    return {
        "date_str": date_str,
        "index": idx,
        "title": title or f"Paper Title {idx}",
        "url": f"https://example.com/{idx}",
        "source": "arxiv",
        "source_name": source_name,
        "organization": None,
        "authors": [],
        "abstract": f"Abstract for paper {idx}",
        "tags": tags or [],
        "rule_score": 30.0,
        "llm_score": 20.0,
        "total_score": total_score,
        "novelty": None,
        "impact": None,
        "trending": None,
        "practicality": None,
        "blog_worthiness": None,
        "llm_reason": None,
        "has_post": has_post,
        "has_note": has_note,
        "has_blog": has_blog,
        "post_slug": None,
        "note_slug": None,
        "blog_slug": None,
    }


def _make_materials(n: int, **kwargs) -> list[dict]:
    return [_make_material(i, **kwargs) for i in range(n)]


@pytest.fixture(autouse=True)
def mock_config_manager(monkeypatch):
    mock_cm = MagicMock()
    mock_cm.get_config.return_value = {}
    mock_cm.get_env_values.return_value = {}
    mock_cm.init_config.return_value = None
    monkeypatch.setattr(app_module, "cm", mock_cm)
    return mock_cm


@pytest.fixture(autouse=True)
def clean_runs(monkeypatch):
    monkeypatch.setattr(app_module, "_runs", {})


@pytest.fixture()
def mock_ds(monkeypatch):
    """回傳一個已 patch 好的 mock data_service。"""
    m = MagicMock()
    m.get_sidebar_stats.return_value = {
        "total_posts": 0, "total_notes": 0, "today_posts": 0,
        "today_notes": 0, "total_materials": 0, "bookmarks_count": 0,
    }
    m.get_all_bookmarks.return_value = {}
    monkeypatch.setattr(app_module, "ds", m)
    return m


@pytest.fixture()
def client():
    with TestClient(app, raise_server_exceptions=True) as c:
        yield c


# ──────────────────────────────────────────────────────────
# 1. 基本分頁切片正確性
# ──────────────────────────────────────────────────────────

def test_pagination_first_page(client, mock_ds):
    """第 1 頁應回傳前 page_size 筆，共 100 筆資料。"""
    mock_ds.list_all_materials.return_value = _make_materials(100)

    res = client.get("/materials?page=1&page_size=10")
    assert res.status_code == 200
    # 頁面應顯示第 1/10 頁
    assert "1/10" in res.text
    # 回傳 10 筆（每張卡片都有 mat-card class）
    assert res.text.count('class="mat-card"') == 10


def test_pagination_second_page(client, mock_ds):
    """第 2 頁應回傳第 11–20 筆（index 10–19）。"""
    materials = _make_materials(100)
    mock_ds.list_all_materials.return_value = materials

    res = client.get("/materials?page=2&page_size=10")
    assert res.status_code == 200
    assert "2/10" in res.text
    # Paper Title 10–19 出現在頁面上
    assert "Paper Title 10" in res.text
    assert "Paper Title 19" in res.text
    # Paper Title 0–9 不出現（已在第 1 頁）
    assert "Paper Title 0<" not in res.text


def test_pagination_last_page_partial(client, mock_ds):
    """最後一頁筆數可能 < page_size（105 筆，每頁 10，第 11 頁應有 5 筆）。"""
    mock_ds.list_all_materials.return_value = _make_materials(105)

    res = client.get("/materials?page=11&page_size=10")
    assert res.status_code == 200
    assert "11/11" in res.text
    assert res.text.count('class="mat-card"') == 5


def test_pagination_total_shown(client, mock_ds):
    """頁面應顯示篩選後的總筆數。"""
    mock_ds.list_all_materials.return_value = _make_materials(75)

    res = client.get("/materials?page=1&page_size=20")
    assert res.status_code == 200
    assert "75" in res.text  # 總筆數


# ──────────────────────────────────────────────────────────
# 2. 超出範圍頁碼處理
# ──────────────────────────────────────────────────────────

def test_page_beyond_total_clamped(client, mock_ds):
    """page > total_pages 時應 clamp 到最後一頁，回傳 200。"""
    mock_ds.list_all_materials.return_value = _make_materials(30)

    res = client.get("/materials?page=999&page_size=10")
    assert res.status_code == 200
    # 30 筆 / 10 每頁 = 3 頁，應顯示第 3 頁
    assert "3/3" in res.text


def test_page_zero_clamped_to_one(client, mock_ds):
    """page=0 應被 Query(ge=1) 拒絕（422）。"""
    mock_ds.list_all_materials.return_value = _make_materials(10)

    res = client.get("/materials?page=0&page_size=10")
    assert res.status_code == 422


def test_empty_results_page_one(client, mock_ds):
    """無資料時應顯示空狀態，total=0，total_pages=1（避免除以零）。"""
    mock_ds.list_all_materials.return_value = []

    res = client.get("/materials?page=1&page_size=50")
    assert res.status_code == 200
    assert "0 筆" in res.text


# ──────────────────────────────────────────────────────────
# 3. 篩選 + 分頁組合（篩選在切片前）
# ──────────────────────────────────────────────────────────

def test_filter_and_pagination(client, mock_ds):
    """篩選 source=HN 後應只剩 30 筆，分頁 total 應反映篩選後數量。"""
    arxiv_items = _make_materials(70, source_name="arXiv")
    hn_items = [_make_material(i + 70, source_name="Hacker News") for i in range(30)]
    mock_ds.list_all_materials.return_value = arxiv_items + hn_items

    res = client.get("/materials?source=hacker+news&page=1&page_size=10")
    assert res.status_code == 200
    # 篩選後 30 筆，每頁 10，共 3 頁
    assert "30" in res.text
    assert "3" in res.text  # 3 頁
    assert res.text.count('class="mat-card"') == 10


def test_filter_min_score_and_pagination(client, mock_ds):
    """min_score=80 篩選後應只剩高分項目，total 反映篩選後數量。"""
    low = _make_materials(40, total_score=50.0)
    high = [_make_material(i + 40, total_score=90.0) for i in range(20)]
    mock_ds.list_all_materials.return_value = low + high

    res = client.get("/materials?min_score=80&page=1&page_size=10")
    assert res.status_code == 200
    assert res.text.count('class="mat-card"') == 10
    # 總筆數應為 20
    assert "20" in res.text


def test_filter_tag_and_pagination(client, mock_ds):
    """tag=LLM 篩選後 total 應反映含 LLM tag 的筆數。"""
    with_tag = [_make_material(i, tags=["LLM", "Agent"]) for i in range(15)]
    without_tag = _make_materials(50)
    mock_ds.list_all_materials.return_value = with_tag + without_tag

    res = client.get("/materials?tag=LLM&page=1&page_size=10")
    assert res.status_code == 200
    assert res.text.count('class="mat-card"') == 10
    # 篩選後 15 筆，共 2 頁
    assert "15" in res.text


def test_filter_content_type_post(client, mock_ds):
    """content_type=post 篩選後只回傳 has_post=True 的項目。"""
    with_post = [_make_material(i, has_post=True) for i in range(8)]
    without_post = _make_materials(20)
    mock_ds.list_all_materials.return_value = with_post + without_post

    res = client.get("/materials?content_type=post&page=1&page_size=50")
    assert res.status_code == 200
    assert res.text.count('class="mat-card"') == 8
    assert "8" in res.text


def test_filter_and_pagination_page2(client, mock_ds):
    """篩選後第 2 頁應顯示正確的切片（篩選後 index 10-19）。"""
    hn_items = [_make_material(i, source_name="Hacker News",
                               title=f"HN Title {i}") for i in range(25)]
    other_items = _make_materials(50, source_name="arXiv")
    mock_ds.list_all_materials.return_value = hn_items + other_items

    res = client.get("/materials?source=hacker+news&page=2&page_size=10")
    assert res.status_code == 200
    # 篩選後 25 筆，第 2 頁 index 10-19
    assert res.text.count('class="mat-card"') == 10
    # 第 2 頁顯示的應是 HN Title 10–19
    assert "HN Title 10" in res.text


# ──────────────────────────────────────────────────────────
# 4. page_size 上限防呆
# ──────────────────────────────────────────────────────────

def test_page_size_max_200(client, mock_ds):
    """page_size > 200 應被 Query(le=200) 拒絕（422）。"""
    mock_ds.list_all_materials.return_value = _make_materials(10)

    res = client.get("/materials?page=1&page_size=201")
    assert res.status_code == 422


def test_page_size_exactly_200(client, mock_ds):
    """page_size=200 應被允許（上限邊界）。"""
    mock_ds.list_all_materials.return_value = _make_materials(10)

    res = client.get("/materials?page=1&page_size=200")
    assert res.status_code == 200


def test_page_size_zero_rejected(client, mock_ds):
    """page_size=0 應被 Query(ge=1) 拒絕（422）。"""
    mock_ds.list_all_materials.return_value = _make_materials(10)

    res = client.get("/materials?page=1&page_size=0")
    assert res.status_code == 422


# ──────────────────────────────────────────────────────────
# 5. 分頁連結保留 query string
# ──────────────────────────────────────────────────────────

def test_pagination_links_preserve_filters(client, mock_ds):
    """下一頁連結應保留篩選參數（source、min_score 等），且 page=2 出現在分頁列。"""
    # 不用 q 篩選（難保證 mock 資料包含特定字串），改用 source + min_score 組合
    # 60 筆均為 arXiv、score=50（>= 30），全部通過篩選 → 共 6 頁
    mock_ds.list_all_materials.return_value = _make_materials(60, source_name="arXiv")

    res = client.get("/materials?source=arxiv&min_score=30&page=1&page_size=10")
    assert res.status_code == 200
    # 下一頁連結應包含篩選參數
    assert "source=arxiv" in res.text
    assert "page=2" in res.text


def test_default_params(client, mock_ds):
    """預設參數（page=1, page_size=50）應正常回傳。"""
    mock_ds.list_all_materials.return_value = _make_materials(10)

    res = client.get("/materials")
    assert res.status_code == 200
    assert res.text.count('class="mat-card"') == 10
