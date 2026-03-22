"""測試 RSS abstract 三段 priority 提取邏輯。"""
from unittest.mock import MagicMock, patch


def _make_entry(content_val=None, summary=None, description=None, link="http://example.com"):
    entry = MagicMock()
    if content_val is not None:
        entry.content = [{"value": content_val}]
    else:
        entry.content = []
    entry.summary = summary or ""
    entry.description = description or ""
    entry.link = link
    return entry


def test_priority1_content_encoded():
    """content:encoded 優先於 summary。"""
    from src.collectors.rss_collector import RSSCollector

    entry = _make_entry(
        content_val="<p>" + "word " * 100 + "</p>",
        summary="short summary",
    )
    client = MagicMock()
    result = RSSCollector._extract_abstract(entry, "", client)
    assert len(result) > 50
    assert "short summary" not in result  # content 優先


def test_priority2_summary_fallback():
    """無 content:encoded 時使用 summary。"""
    from src.collectors.rss_collector import RSSCollector

    entry = _make_entry(summary="<p>" + "word " * 60 + "</p>")
    client = MagicMock()
    result = RSSCollector._extract_abstract(entry, "", client, min_len=200)
    assert len(result) > 0


def test_priority3_fetch_when_short(monkeypatch):
    """abstract < min_len 時補抓文章 URL。"""
    from src.collectors.rss_collector import RSSCollector

    entry = _make_entry(summary="too short")

    mock_client = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = "<p>" + "word " * 100 + "</p>"
    mock_client.get.return_value = mock_response

    result = RSSCollector._extract_abstract(entry, "http://example.com", mock_client, min_len=1000)
    mock_client.get.assert_called_once_with("http://example.com", timeout=12)
    assert len(result) > len("too short")


def test_no_fetch_when_long_enough():
    """abstract >= min_len 時不觸發補抓。"""
    from src.collectors.rss_collector import RSSCollector

    long_content = "<p>" + "word " * 250 + "</p>"  # 250 * 5 = 1250 chars > 1000
    entry = _make_entry(content_val=long_content)
    client = MagicMock()
    result = RSSCollector._extract_abstract(entry, "http://example.com", client, min_len=1000)
    client.get.assert_not_called()
    assert len(result) > 0


def test_extract_full_text_from_html_prefers_semantic_container():
    """extract_full_text_from_html 優先選取語意容器標籤。"""
    from src.utils import extract_full_text_from_html

    html = """
    <html><body>
    <nav>Navigation noise</nav>
    <article>Main article content here with enough words to be useful.</article>
    </body></html>
    """
    result = extract_full_text_from_html(html)
    assert "Main article content" in result
    assert "Navigation noise" not in result


def test_fetch_article_text_returns_empty_on_error():
    """fetch_article_text 失敗時靜默返回空字串。"""
    from src.utils import fetch_article_text

    client = MagicMock()
    client.get.side_effect = Exception("connection error")
    result = fetch_article_text("http://example.com", client)
    assert result == ""


def test_fetch_article_text_returns_empty_on_non_200():
    """fetch_article_text 非 200 狀態碼時返回空字串。"""
    from src.utils import fetch_article_text

    client = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 404
    client.get.return_value = mock_response
    result = fetch_article_text("http://example.com", client)
    assert result == ""
