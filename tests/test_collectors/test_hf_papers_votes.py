"""HF Papers 票數抽取、日期轉址防護、隔日補票。"""
from datetime import date
from unittest.mock import MagicMock, patch

from bs4 import BeautifulSoup

from src.collectors.hf_papers import _parse_upvotes, _resolved_page_date, fetch_upvotes

# HF 卡片實際結構：票數在 role="checkbox" 內的 .leading-none，沒有 button、沒有 upvote class
_CARD = """
<article>
  <h3><a href="/papers/2607.21553">SANA-Video 2.0</a></h3>
  <div role="checkbox" aria-checked="false">
    <svg></svg>
    <div class="leading-none">48</div>
  </div>
</article>
"""

# 舊版假設的結構（button + class 帶 upvote）——現在的頁面已經沒有這些
_LEGACY_CARD = """
<article>
  <h3><a href="/papers/2607.00001">Legacy Layout</a></h3>
  <button class="upvote-btn">12</button>
</article>
"""


def _article(html: str):
    return BeautifulSoup(html, "html.parser").select_one("article")


def test_parse_upvotes_reads_checkbox_block():
    assert _parse_upvotes(_article(_CARD)) == 48


def test_parse_upvotes_missing_element_returns_zero():
    """抓不到票數時回 0（並記 warning），不可拋例外中斷整批收集。"""
    assert _parse_upvotes(_article(_LEGACY_CARD)) == 0


def test_resolved_page_date_no_redirect():
    """沒轉址時（維持 ?date= 形式）視為就是目標日期。"""
    resp = MagicMock()
    resp.url = "https://huggingface.co/papers?date=2026-07-24"
    assert _resolved_page_date(resp, date(2026, 7, 24)) == date(2026, 7, 24)


def test_resolved_page_date_detects_redirect():
    """HF 週末會 302 到最近有資料的日期，須解析出真正的日期。"""
    resp = MagicMock()
    resp.url = "https://huggingface.co/papers/date/2026-07-24"
    assert _resolved_page_date(resp, date(2026, 7, 26)) == date(2026, 7, 24)


def _mock_client(url: str, html: str, status: int = 200):
    client = MagicMock()
    resp = MagicMock()
    resp.status_code = status
    resp.url = url
    resp.text = html
    client.get.return_value = resp
    return client


def test_fetch_upvotes_returns_mapping():
    client = _mock_client("https://huggingface.co/papers?date=2026-07-24", _CARD)
    with patch("src.collectors.hf_papers.get_http_client", return_value=client):
        votes = fetch_upvotes(date(2026, 7, 24))
    assert votes == {"https://huggingface.co/papers/2607.21553": 48}


def test_fetch_upvotes_rejects_redirected_date():
    """日期對不上就回空 dict——否則會把別天的票數蓋到今天的論文上。"""
    client = _mock_client("https://huggingface.co/papers/date/2026-07-24", _CARD)
    with patch("src.collectors.hf_papers.get_http_client", return_value=client):
        assert fetch_upvotes(date(2026, 7, 26)) == {}


def test_fetch_upvotes_non_200_returns_empty():
    client = _mock_client("https://huggingface.co/papers?date=2026-07-30", "", status=400)
    with patch("src.collectors.hf_papers.get_http_client", return_value=client):
        assert fetch_upvotes(date(2026, 7, 30)) == {}
