"""測試 ChatPaper collector 的去重與欄位映射。"""
from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock, patch

_CFG = {
    "collectors": {
        "chatpaper": {
            "enabled": True,
            "base_url": "https://chatpaper.example/api",
            "page_size": 30,
            "categories": [{"id": 2, "name": "AI"}],
        }
    }
}


def _resp(items: list[dict]) -> MagicMock:
    r = MagicMock()
    r.status_code = 200
    r.headers = {}  # 無 x-binary-key → parse_response 走純 JSON 分支
    r.json.return_value = {"items": items}
    return r


def _article(source_id="2601.001", title="Paper A"):
    return {
        "source_id": source_id,
        "title": title,
        "article_url": f"https://arxiv.org/abs/{source_id}",
        "authors": ["Alice"],
        "abstract": "An abstract about agents.",
        "category_list": [{"tag": "cs.AI"}],
        "organization": "Google",
        "pdf_url": "https://arxiv.org/pdf/x",
        "id": 99,
        "source_type": "arxiv",
    }


@patch("src.collectors.chatpaper_collector.load_config", return_value=_CFG)
@patch("src.collectors.chatpaper_collector.get_http_client")
def test_chatpaper_maps_fields(mock_get_client, _cfg):
    from src.collectors.chatpaper_collector import ChatPaperCollector
    from src.models import SourceType

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.return_value = _resp([_article()])

    items = ChatPaperCollector().collect(target_date=date(2026, 2, 26))
    assert len(items) == 1
    it = items[0]
    assert it.source == SourceType.CHATPAPER
    assert it.source_name == "ChatPaper/AI"
    assert it.raw_metadata["arxiv_id"] == "2601.001"
    assert it.organization == "Google"


@patch("src.collectors.chatpaper_collector.load_config", return_value=_CFG)
@patch("src.collectors.chatpaper_collector.get_http_client")
def test_chatpaper_dedup_by_source_id(mock_get_client, _cfg):
    """同一 source_id 重複出現只保留一筆。"""
    from src.collectors.chatpaper_collector import ChatPaperCollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.return_value = _resp([_article(source_id="dup"), _article(source_id="dup", title="dup2")])

    items = ChatPaperCollector().collect(target_date=date(2026, 2, 26))
    assert len(items) == 1


@patch("src.collectors.chatpaper_collector.load_config", return_value=_CFG)
@patch("src.collectors.chatpaper_collector.get_http_client")
def test_chatpaper_category_error_does_not_crash(mock_get_client, _cfg):
    """單一 category 失敗時整體不應拋例外，回傳空清單。"""
    from src.collectors.chatpaper_collector import ChatPaperCollector

    client = MagicMock()
    mock_get_client.return_value = client
    client.get.side_effect = Exception("network down")

    items = ChatPaperCollector().collect(target_date=date(2026, 2, 26))
    assert items == []
    client.close.assert_called_once()
