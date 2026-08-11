"""測試中國 AI 實驗室 collector 的欄位映射、日期過濾與失敗降級。"""
from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock, patch

_CFG = {
    "collectors": {
        "cn_labs": {"enabled": True, "sources": ["qwen", "minimax"], "max_age_days": 7},
        "abstract_max_chars": 8000,
    }
}

# Qwen API 不回日期欄位，日期只存在於 content 那一整頁 HTML 的 meta 裡。
_QWEN_PAGE = """<!doctype html><html><head>
<meta property="article:published_time" content="{ts}T04:59:26+08:00">
<link rel=canonical href=https://qwenlm.github.io/zh/blog/{path} /></head>
<body><div class="post-content"><p>{body}</p></div></body></html>"""


def _qwen_resp(articles: list[dict]) -> MagicMock:
    r = MagicMock()
    r.status_code = 200
    r.json.return_value = {"success": True, "data": {"articles": articles}}
    return r


def _qwen_article(title="Qwen3.8-Max 發表", path="qwen3.8", ts="2026-08-03", body="模型正文" * 20):
    return {
        "id": "abc",
        "type": "qwen_ai",
        "title": title,
        "content": _QWEN_PAGE.format(ts=ts, path=path, body=body),
        "path": path,
        "language": "zh-CN",
        "extra": "{}",
    }


def _minimax_resp(items: list[dict]) -> MagicMock:
    r = MagicMock()
    r.status_code = 200
    r.json.return_value = {"data": items, "hasMore": False, "page": 1, "total": len(items)}
    return r


def _minimax_item(title="MiniMax H3 Is Now Open Source", slug="minimax-h3-open-source",
                  published_ms=1785756267890, summary="Today we open-source MiniMax H3."):
    return {
        "newsId": "6a707bcec5d96038cccce2f6",
        "title": title,
        "content": "",
        "summary": summary,
        "tags": ["MiniMax H3", "Video Generation"],
        "publishDate": published_ms,
        "slug": slug,
    }


def _client_returning(qwen: MagicMock | Exception, minimax: MagicMock | Exception) -> MagicMock:
    """依 URL 分流回應，讓兩個 provider 能各自被測。"""
    client = MagicMock()

    def _get(url, *a, **kw):
        resp = qwen if "qwen.ai" in url else minimax
        if isinstance(resp, Exception):
            raise resp
        return resp

    client.get.side_effect = _get
    return client


@patch("src.collectors.cn_labs_collector.load_config", return_value=_CFG)
def test_disabled_returns_empty(_cfg):
    from src.collectors.cn_labs_collector import CNLabsCollector

    with patch("src.collectors.cn_labs_collector.load_config",
               return_value={"collectors": {"cn_labs": {"enabled": False}}}):
        with patch("src.collectors.cn_labs_collector.get_http_client") as mock_client:
            assert CNLabsCollector().collect(target_date=date(2026, 8, 4)) == []
            mock_client.assert_not_called()


_DEEPSEEK_CFG = {
    "collectors": {"cn_labs": {"enabled": True, "sources": ["deepseek"], "max_age_days": 7},
                   "abstract_max_chars": 8000}
}

_DEEPSEEK_INDEX = """<html><body><nav>
<a href="/news/news260805">DeepSeek V4 Preview Release</a>
<a href="/news/news250115">舊公告</a>
<a href="/news/news1226">2024 年的四碼舊格式</a>
</nav></body></html>"""

_DEEPSEEK_PAGE = """<html><body><article><h1>DeepSeek V4 Preview Release</h1>
<div class="post-content"><p>{}</p></div></article></body></html>"""


def _deepseek_client() -> MagicMock:
    client = MagicMock()
    pages: list[str] = []

    def _get(url, *a, **kw):
        r = MagicMock()
        r.status_code = 200
        if url.rstrip("/").endswith("/news"):
            r.text = _DEEPSEEK_INDEX
        else:
            pages.append(url)
            r.text = _DEEPSEEK_PAGE.format("公告正文" * 30)
        return r

    client.get.side_effect = _get
    client.fetched_pages = pages
    return client


@patch("src.collectors.cn_labs_collector.load_config", return_value=_DEEPSEEK_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_deepseek_parses_slug_date_and_skips_old(mock_get_client, _cfg):
    """slug 內嵌日期（news260805 = 2026-08-05）；過期的不該再花一次 HTTP 抓內文。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    client = _deepseek_client()
    mock_get_client.return_value = client
    items = CNLabsCollector().collect(target_date=date(2026, 8, 11))

    assert len(items) == 1
    assert items[0].url == "https://api-docs.deepseek.com/news/news260805"
    assert items[0].published_date == date(2026, 8, 5)
    assert items[0].organization == "DeepSeek"
    assert items[0].source_name == "DeepSeek"
    # 舊公告與四碼格式都只在索引頁被日期擋掉，不進第二次請求
    assert client.fetched_pages == ["https://api-docs.deepseek.com/news/news260805"]


def test_deepseek_four_digit_slug_has_no_recoverable_year():
    """2024 年的 newsMMDD 沒有年份可還原，必須回 None 而不是猜今年。"""
    from src.collectors.cn_labs_collector import _parse_deepseek_slug_date

    assert _parse_deepseek_slug_date("news260424") == date(2026, 4, 24)
    assert _parse_deepseek_slug_date("news1226") is None
    assert _parse_deepseek_slug_date("news999999") is None


@patch("src.collectors.cn_labs_collector.load_config", return_value=_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_qwen_field_mapping(mock_get_client, _cfg):
    """Qwen：日期取自 meta、URL 必須組 qwen.ai/blog?id=，organization 推得出 Alibaba。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    mock_get_client.return_value = _client_returning(
        _qwen_resp([_qwen_article()]), _minimax_resp([])
    )
    items = CNLabsCollector().collect(target_date=date(2026, 8, 4))

    assert len(items) == 1
    item = items[0]
    assert item.source.value == "cn_labs"
    assert item.source_name == "Qwen"
    # canonical 指向的 qwenlm.github.io 對新文章是 404（該站已停更），
    # 照抄 canonical 會讓每一篇都是死連結。
    assert item.url == "https://qwen.ai/blog?id=qwen3.8"
    assert item.published_date == date(2026, 8, 3)
    assert item.organization == "Alibaba"
    assert "模型正文" in item.abstract


@patch("src.collectors.cn_labs_collector.load_config", return_value=_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_minimax_field_mapping(mock_get_client, _cfg):
    """MiniMax：publishDate 是毫秒 epoch，summary 太短時補抓詳情頁全文。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    mock_get_client.return_value = _client_returning(
        _qwen_resp([]), _minimax_resp([_minimax_item()])
    )
    with patch("src.collectors.cn_labs_collector.fetch_article_text", return_value="完整正文" * 30):
        items = CNLabsCollector().collect(target_date=date(2026, 8, 4))

    assert len(items) == 1
    item = items[0]
    assert item.source_name == "MiniMax"
    assert item.url == "https://www.minimax.io/news/minimax-h3-open-source"
    assert item.published_date == date(2026, 8, 3)  # 1785756267890ms = 2026-08-03 UTC
    assert item.organization == "MiniMax"
    assert "完整正文" in item.abstract
    assert "MiniMax H3" in item.tags


@patch("src.collectors.cn_labs_collector.load_config", return_value=_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_minimax_accepts_both_publish_date_types(mock_get_client, _cfg):
    """實測同一頁回應裡新文是 ms epoch int、舊文是 ISO 字串，只吃一種會整個 provider 拋錯。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    mock_get_client.return_value = _client_returning(
        _qwen_resp([]),
        _minimax_resp([
            _minimax_item(title="int 版", slug="a", published_ms=1785756267890),
            _minimax_item(title="ISO 版", slug="b", published_ms="2026-08-05T16:00:00.000Z"),
            _minimax_item(title="壞日期", slug="c", published_ms="not-a-date"),
        ]),
    )
    # 兩篇分別是 2026-08-03 與 2026-08-05，取 08-06 讓 7 天窗口同時涵蓋
    with patch("src.collectors.cn_labs_collector.fetch_article_text", return_value="正文" * 50):
        items = CNLabsCollector().collect(target_date=date(2026, 8, 6))

    assert [i.title for i in items] == ["int 版", "ISO 版"]


@patch("src.collectors.cn_labs_collector.load_config", return_value=_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_filters_articles_older_than_max_age(mock_get_client, _cfg):
    """兩家 API 都回「全部歷史文章」（Qwen 一次 34 篇跨 1.5 年），不過濾會每天灌舊文。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    mock_get_client.return_value = _client_returning(
        _qwen_resp([
            _qwen_article(title="新文", path="new", ts="2026-08-03"),
            _qwen_article(title="舊文", path="old", ts="2025-03-24"),
        ]),
        _minimax_resp([
            _minimax_item(title="舊聞", slug="old-news", published_ms=1740000000000),
        ]),
    )
    items = CNLabsCollector().collect(target_date=date(2026, 8, 4))

    assert [i.title for i in items] == ["新文"]


@patch("src.collectors.cn_labs_collector.load_config", return_value=_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_one_provider_failure_does_not_kill_the_other(mock_get_client, _cfg):
    """單一 provider 掛掉不得拖垮整個 collector。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    mock_get_client.return_value = _client_returning(
        RuntimeError("qwen down"), _minimax_resp([_minimax_item()])
    )
    with patch("src.collectors.cn_labs_collector.fetch_article_text", return_value="正文" * 50):
        items = CNLabsCollector().collect(target_date=date(2026, 8, 4))

    assert [i.source_name for i in items] == ["MiniMax"]


@patch("src.collectors.cn_labs_collector.load_config", return_value=_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_article_without_parsable_date_is_skipped(mock_get_client, _cfg):
    """抽不到日期就不收——寧可漏，也不要用今天的日期把舊文假裝成新文。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    broken = _qwen_article()
    broken["content"] = "<html><body><p>沒有 meta 的頁面</p></body></html>"
    mock_get_client.return_value = _client_returning(_qwen_resp([broken]), _minimax_resp([]))

    assert CNLabsCollector().collect(target_date=date(2026, 8, 4)) == []


_KIMI_CFG = {
    "collectors": {"cn_labs": {"enabled": True, "sources": ["kimi"], "max_age_days": 7},
                   "abstract_max_chars": 8000}
}

# 真實結構：連結是覆蓋整張卡片的 absolute <a>，與 .card-body 是兄弟。
# 第二張卡片刻意連到站外（2024 年的舊論文就是這樣），不得被配到第一張的 /blog/ 連結。
_KIMI_INDEX_HTML = """<html><body><div class="grid">
  <div class="card">
    <a href="/blog/kimi-k4" aria-label="Kimi K4" class="absolute inset-0"></a>
    <div class="card-body"><h4 class="card-title">Kimi K4</h4><p class="card-date">2026/08/06</p></div>
  </div>
  <div class="card">
    <a href="/blog/old-post" aria-label="舊文" class="absolute inset-0"></a>
    <div class="card-body"><h4 class="card-title">舊文</h4><p class="card-date">2025/01/20</p></div>
  </div>
  <div class="card">
    <a href="https://arxiv.org/abs/2407.00079" class="absolute inset-0"></a>
    <div class="card-body"><h4 class="card-title">Mooncake</h4><p class="card-date">2024/06/26</p></div>
  </div>
</div></body></html>"""


@patch("src.collectors.cn_labs_collector.load_config", return_value=_KIMI_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_kimi_pairs_card_with_its_own_link(mock_get_client, _cfg):
    from src.collectors.cn_labs_collector import CNLabsCollector

    client = MagicMock()
    resp = MagicMock()
    resp.status_code = 200
    resp.text = _KIMI_INDEX_HTML
    client.get.return_value = resp
    mock_get_client.return_value = client

    with patch("src.collectors.cn_labs_collector.fetch_article_text", return_value="正文" * 60):
        items = CNLabsCollector().collect(target_date=date(2026, 8, 11))

    # 站外卡片沒有 /blog/ 連結 → 整張跳過，不得借用隔壁卡片的連結
    assert [i.title for i in items] == ["Kimi K4"]
    assert items[0].url == "https://www.kimi.com/blog/kimi-k4"
    assert items[0].published_date == date(2026, 8, 6)
    assert items[0].organization == "Moonshot AI"


@patch("src.collectors.cn_labs_collector.load_config", return_value=_KIMI_CFG)
@patch("src.collectors.cn_labs_collector.get_http_client")
def test_kimi_ignores_dates_inside_article_pages(mock_get_client, _cfg):
    """文章頁裡的日期字串全是圖片 CDN 的上傳日，日期只能取自索引頁卡片。"""
    from src.collectors.cn_labs_collector import CNLabsCollector

    client = MagicMock()
    resp = MagicMock()
    resp.status_code = 200
    resp.text = _KIMI_INDEX_HTML
    client.get.return_value = resp
    mock_get_client.return_value = client

    with patch("src.collectors.cn_labs_collector.fetch_article_text",
               return_value="圖片路徑 2026-07-17 只是上傳日" * 20):
        items = CNLabsCollector().collect(target_date=date(2026, 8, 11))

    assert items[0].published_date == date(2026, 8, 6)
