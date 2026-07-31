"""Tests for HF Papers arXiv abstract enrichment and non-200 handling."""
import pytest
from unittest.mock import MagicMock, patch
from src.collectors.hf_papers import _extract_arxiv_id, _fetch_arxiv_abstract, _ENRICH_DELAY_SECONDS


def test_extract_arxiv_id_standard():
    """標準 HF paper URL 應正確解析出 arxiv_id。"""
    url = "https://huggingface.co/papers/2402.12345"
    assert _extract_arxiv_id(url) == "2402.12345"


def test_extract_arxiv_id_non_paper_url_returns_none():
    """非 paper URL 應回傳 None。"""
    assert _extract_arxiv_id("https://huggingface.co/models/bert") is None
    assert _extract_arxiv_id("https://huggingface.co/datasets") is None


def test_fetch_arxiv_abstract_success():
    """成功時應回傳解析後的摘要。"""
    arxiv_xml = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <summary>
      This is the abstract
      spanning multiple lines.
    </summary>
  </entry>
</feed>"""
    mock_client = MagicMock()
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = arxiv_xml
    mock_client.get.return_value = mock_resp

    result = _fetch_arxiv_abstract("2402.12345", mock_client)
    assert "This is the abstract" in result
    assert "\n" not in result  # 多餘換行已清理


def test_fetch_arxiv_abstract_http_error_returns_empty():
    """HTTP 非 200 回應應回傳空字串。"""
    mock_client = MagicMock()
    mock_resp = MagicMock()
    mock_resp.status_code = 404
    mock_client.get.return_value = mock_resp

    result = _fetch_arxiv_abstract("2402.99999", mock_client)
    assert result == ""


def test_fetch_arxiv_abstract_network_error_returns_empty():
    """網路錯誤（exception）應回傳空字串。"""
    mock_client = MagicMock()
    mock_client.get.side_effect = Exception("Connection error")

    result = _fetch_arxiv_abstract("2402.12345", mock_client)
    assert result == ""


# ── _ENRICH_DELAY_SECONDS 常數 ─────────────────────────────────────────────

def test_enrich_delay_constant_is_numeric_and_positive():
    """_ENRICH_DELAY_SECONDS should be a positive number (readable name for 0.5)."""
    assert isinstance(_ENRICH_DELAY_SECONDS, float)
    assert _ENRICH_DELAY_SECONDS > 0


# ── per-paper page non-200 handling ───────────────────────────────────────────

_MINIMAL_HF_HTML = """
<html><body>
<article>
  <h3><a href="/papers/2402.00001">Test Paper</a></h3>
  <button>42</button>
</article>
</body></html>
"""


@patch("src.collectors.hf_papers.time.sleep")
@patch("src.collectors.hf_papers.get_http_client")
def test_non200_paper_page_logs_warning(mock_get_client, mock_sleep, caplog):
    """Non-200 response when fetching a paper page emits a warning log."""
    import logging
    from src.collectors.hf_papers import HFPapersCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    # First call: the HF papers listing page (200)
    list_resp = MagicMock()
    list_resp.status_code = 200
    list_resp.text = _MINIMAL_HF_HTML

    # Second call: the individual paper page (503)
    paper_resp = MagicMock()
    paper_resp.status_code = 503

    mock_client.get.side_effect = [list_resp, paper_resp]

    collector = HFPapersCollector()
    with caplog.at_level(logging.WARNING, logger="collectors.hf_papers"):
        items = collector.collect()

    warning_texts = [r.message for r in caplog.records if r.levelno == logging.WARNING]
    assert any("503" in t or "Non-200" in t or "non-200" in t.lower() for t in warning_texts), \
        f"Expected a warning mentioning 503. Got: {warning_texts}"


@patch("src.collectors.hf_papers.time.sleep")
@patch("src.collectors.hf_papers.get_http_client")
def test_non200_paper_page_uses_title_fallback(mock_get_client, mock_sleep):
    """When paper page returns non-200, abstract falls back to the title-based string."""
    from src.collectors.hf_papers import HFPapersCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    list_resp = MagicMock()
    list_resp.status_code = 200
    list_resp.text = _MINIMAL_HF_HTML

    paper_resp = MagicMock()
    paper_resp.status_code = 404

    mock_client.get.side_effect = [list_resp, paper_resp]

    collector = HFPapersCollector()
    items = collector.collect()

    assert len(items) == 1
    # Abstract should be the title-based fallback, not empty
    assert items[0].abstract != ""
    assert "Test Paper" in items[0].abstract or "HuggingFace" in items[0].abstract


from src.collectors.hf_papers import looks_unspaced


class TestLooksUnspaced:
    def test_detects_stripped_whitespace(self):
        # 實測破損樣本：get_text(strip=True) 把節點間空白全吃掉
        broken = "LLMtrainingisshiftingfrommanualdesignandannotationtointeractiondrivenselfevolution" * 2
        assert looks_unspaced(broken) is True

    def test_normal_english_abstract_is_fine(self):
        ok = (
            "LLM training is shifting from manual design and annotation to "
            "interaction-driven self-evolution. However, existing methods face a dilemma."
        )
        assert looks_unspaced(ok) is False

    def test_flags_broken_text_containing_slashes(self):
        # 真實破損樣本有 59/192 含 "/"（and/or、Hand-Object），不得被排除
        broken = "Hand-ObjectInteraction(HOI)synthesisisacornerstoneforanimationproductionand/orembodiedAI." * 2
        assert looks_unspaced(broken) is True

    def test_chinese_abstract_not_flagged(self):
        # 中文幾乎沒有空白，必須靠 ASCII 比例擋掉
        zh = "本文提出一種新的大型語言模型訓練方法，透過技能自我對弈提升模型能力邊界。" * 4
        assert looks_unspaced(zh) is False

    def test_short_text_not_flagged(self):
        assert looks_unspaced("short") is False

    def test_empty_string_not_flagged(self):
        assert looks_unspaced("") is False


# ── 破損（黏字）abstract 觸發 arXiv fallback ──────────────────────────────────

_BROKEN_ABSTRACT = (
    "Softwareloggingisessentialformaintaininganddebuggingcomplexsystems,"
    "yetitremainsunclearhowAIcodingagentshandlethistask." * 2
)
_GOOD_ABSTRACT = (
    "Software logging is essential for maintaining and debugging complex "
    "systems, yet it remains unclear how AI coding agents handle this task. "
    "We present a benchmark to study this question in depth."
)

_ARXIV_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry><summary>Recovered arXiv abstract with proper spacing throughout.</summary></entry>
</feed>"""


def _hf_paper_page(abstract_text: str) -> str:
    return f"<html><body><p>{abstract_text}</p></body></html>"


@patch("src.collectors.hf_papers.time.sleep")
@patch("src.collectors.hf_papers.get_http_client")
def test_unspaced_abstract_triggers_arxiv_fallback(mock_get_client, mock_sleep):
    """黏字破損的 abstract 很長，舊的 len<100 條件擋不住，必須靠 looks_unspaced 觸發補救。"""
    from src.collectors.hf_papers import HFPapersCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    list_resp = MagicMock(status_code=200, text=_MINIMAL_HF_HTML)
    paper_resp = MagicMock(status_code=200, text=_hf_paper_page(_BROKEN_ABSTRACT))
    arxiv_resp = MagicMock(status_code=200, text=_ARXIV_XML)
    mock_client.get.side_effect = [list_resp, paper_resp, arxiv_resp]

    items = HFPapersCollector().collect()

    assert len(items) == 1
    assert items[0].abstract == "Recovered arXiv abstract with proper spacing throughout."


@patch("src.collectors.hf_papers.time.sleep")
@patch("src.collectors.hf_papers.get_http_client")
def test_healthy_abstract_does_not_trigger_arxiv_fallback(mock_get_client, mock_sleep):
    """正常帶空白的長 abstract 不該多打一次 arXiv API。"""
    from src.collectors.hf_papers import HFPapersCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client

    list_resp = MagicMock(status_code=200, text=_MINIMAL_HF_HTML)
    paper_resp = MagicMock(status_code=200, text=_hf_paper_page(_GOOD_ABSTRACT))
    mock_client.get.side_effect = [list_resp, paper_resp]

    items = HFPapersCollector().collect()

    assert len(items) == 1
    assert items[0].abstract == _GOOD_ABSTRACT
    assert mock_client.get.call_count == 2  # 只打列表頁 + 論文頁，沒有第三次


# ── fetch_paper_abstract() 介面層單元測試 ─────────────────────────────────────
# 這是跨 task 公開介面（Task 3 以 repair_all(fetcher=...) 注入式呼叫），
# 「失敗一律回 ""、絕不 raise」是 load-bearing 契約：網路錯誤若外洩成 exception
# 會炸掉修復 CLI 的整個批次迴圈，必須有直接測試守著。

def test_fetch_paper_abstract_success():
    """200 且有長 <p> 時回傳正規化空白後的 abstract。"""
    from src.collectors.hf_papers import fetch_paper_abstract

    mock_client = MagicMock()
    mock_client.get.return_value = MagicMock(
        status_code=200, text=_hf_paper_page(_GOOD_ABSTRACT)
    )

    assert fetch_paper_abstract(mock_client, "https://huggingface.co/papers/2402.00001") == _GOOD_ABSTRACT


def test_fetch_paper_abstract_network_error_returns_empty():
    """網路錯誤（exception）必須被吞掉並回空字串，不得往外拋。"""
    from src.collectors.hf_papers import fetch_paper_abstract

    mock_client = MagicMock()
    mock_client.get.side_effect = Exception("Connection error")

    assert fetch_paper_abstract(mock_client, "https://huggingface.co/papers/2402.00001") == ""


def test_fetch_paper_abstract_malformed_response_returns_empty():
    """回應物件壞掉（.text 存取即拋錯）同樣不得外洩 exception。"""
    from src.collectors.hf_papers import fetch_paper_abstract

    mock_resp = MagicMock(status_code=200)
    type(mock_resp).text = property(lambda self: (_ for _ in ()).throw(ValueError("decode failed")))
    mock_client = MagicMock()
    mock_client.get.return_value = mock_resp

    assert fetch_paper_abstract(mock_client, "https://huggingface.co/papers/2402.00001") == ""


def test_fetch_paper_abstract_non_200_returns_empty():
    """非 200 回空字串。"""
    from src.collectors.hf_papers import fetch_paper_abstract

    mock_client = MagicMock()
    mock_client.get.return_value = MagicMock(status_code=503, text="")

    assert fetch_paper_abstract(mock_client, "https://huggingface.co/papers/2402.00001") == ""


def test_fetch_paper_abstract_no_long_paragraph_returns_empty():
    """頁面存在但沒有夠長的 <p>（全是導覽列短文字）時回空字串。"""
    from src.collectors.hf_papers import fetch_paper_abstract

    mock_client = MagicMock()
    mock_client.get.return_value = MagicMock(
        status_code=200, text="<html><body><p>Short</p><p>Also short</p></body></html>"
    )

    assert fetch_paper_abstract(mock_client, "https://huggingface.co/papers/2402.00001") == ""
