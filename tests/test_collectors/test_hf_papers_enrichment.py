"""Tests for HF Papers arXiv abstract enrichment."""
import pytest
from unittest.mock import MagicMock, patch
from src.collectors.hf_papers import _extract_arxiv_id, _fetch_arxiv_abstract


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
