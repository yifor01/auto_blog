"""測試 Semantic Scholar collector：解析、arxiv_id 映射、缺 abstract、429 退避、無 key 不帶 header。"""
from datetime import date
from unittest.mock import MagicMock, patch


def _make_paper(
    paper_id: str = "p1",
    title: str = "A Great LLM Paper",
    abstract: str | None = "We propose a new method for large language models.",
    url: str = "https://www.semanticscholar.org/paper/p1",
    publication_date: str | None = "2026-06-09",
    arxiv: str | None = None,
    citation_count: int = 7,
    venue: str = "NeurIPS",
    authors: list[dict] | None = None,
) -> dict:
    external_ids: dict = {"DOI": "10.x/y", "CorpusId": 123}
    if arxiv is not None:
        external_ids["ArXiv"] = arxiv
    return {
        "paperId": paper_id,
        "title": title,
        "abstract": abstract,
        "url": url,
        "publicationDate": publication_date,
        "externalIds": external_ids,
        "citationCount": citation_count,
        "venue": venue,
        "authors": authors if authors is not None else [{"name": "Jane Doe"}],
    }


def _make_response(status_code: int, data: list[dict] | None = None) -> MagicMock:
    resp = MagicMock()
    resp.status_code = status_code
    if data is not None:
        resp.json.return_value = {"total": len(data), "token": None, "data": data}
    return resp


@patch("src.collectors.semantic_scholar.get_http_client")
def test_basic_parse(mock_get_client):
    """成功解析：欄位正確映射到 ContentItem。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector
    from src.models import SourceType

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(200, [_make_paper()])

    items = SemanticScholarCollector().collect(date(2026, 6, 10))

    assert len(items) == 1
    it = items[0]
    assert it.source == SourceType.SEMANTIC_SCHOLAR
    assert it.source_name == "Semantic Scholar"
    assert it.title == "A Great LLM Paper"
    assert it.authors == ["Jane Doe"]
    assert it.published_date == date(2026, 6, 9)
    assert it.raw_metadata["citation_count"] == 7
    assert it.raw_metadata["venue"] == "NeurIPS"
    assert it.organization == ""


@patch("src.collectors.semantic_scholar.get_http_client")
def test_arxiv_id_mapping_strips_version(mock_get_client):
    """externalIds.ArXiv 映射到 raw_metadata['arxiv_id']，並去除版本號 → 走 arxiv 去重 key。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(200, [_make_paper(arxiv="2606.11190v1")])

    items = SemanticScholarCollector().collect(date(2026, 6, 10))

    assert items[0].raw_metadata["arxiv_id"] == "2606.11190"
    # 走 arxiv 去重 key
    assert items[0].dedup_key() == "arxiv:2606.11190"


@patch("src.collectors.semantic_scholar.get_http_client")
def test_no_arxiv_id_uses_url_dedup(mock_get_client):
    """無 ArXiv id 時 arxiv_id 為空，dedup 走 URL。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(200, [_make_paper(arxiv=None)])

    items = SemanticScholarCollector().collect(date(2026, 6, 10))

    assert items[0].raw_metadata["arxiv_id"] == ""
    assert not items[0].dedup_key().startswith("arxiv:")


@patch("src.collectors.semantic_scholar.get_http_client")
def test_missing_abstract_kept_with_fallback(mock_get_client):
    """缺 abstract 的論文保留，並以 title + venue 組 fallback（非空）。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(
        200, [_make_paper(abstract=None, title="Edge Paper", venue="ICML")]
    )

    items = SemanticScholarCollector().collect(date(2026, 6, 10))

    assert len(items) == 1
    assert items[0].abstract != ""
    assert "Edge Paper" in items[0].abstract
    assert "ICML" in items[0].abstract


@patch("src.collectors.semantic_scholar.get_http_client")
def test_empty_title_skipped(mock_get_client):
    """無標題的論文跳過。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(
        200, [_make_paper(title=""), _make_paper(paper_id="p2", title="Valid")]
    )

    items = SemanticScholarCollector().collect(date(2026, 6, 10))

    assert len(items) == 1
    assert items[0].title == "Valid"


@patch("src.collectors.semantic_scholar.get_http_client")
def test_limit_respected(mock_get_client):
    """結果數量受 limit 上限約束。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    papers = [_make_paper(paper_id=f"p{i}", title=f"Paper {i}") for i in range(50)]
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(200, papers)

    items = SemanticScholarCollector().collect(date(2026, 6, 10))

    # config 預設 limit=30
    assert len(items) == 30


# ── header / key 行為 ────────────────────────────────────────────────────────

@patch.dict("os.environ", {"SEMANTIC_SCHOLAR_API_KEY": "secret-key"}, clear=False)
@patch("src.collectors.semantic_scholar.get_http_client")
def test_api_key_sent_in_header(mock_get_client):
    """有 key 時帶 x-api-key header。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(200, [_make_paper()])

    SemanticScholarCollector().collect(date(2026, 6, 10))

    _, kwargs = mock_client.get.call_args
    assert kwargs["headers"].get("x-api-key") == "secret-key"


@patch.dict("os.environ", {}, clear=True)
@patch("src.collectors.semantic_scholar.get_http_client")
def test_no_api_key_no_header(mock_get_client):
    """無 key 時不帶 x-api-key header（仍可呼叫）。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = _make_response(200, [_make_paper()])

    items = SemanticScholarCollector().collect(date(2026, 6, 10))

    _, kwargs = mock_client.get.call_args
    assert "x-api-key" not in kwargs["headers"]
    assert len(items) == 1


# ── 429 退避 ─────────────────────────────────────────────────────────────────

@patch("src.collectors.semantic_scholar.time.sleep")
def test_429_retries_then_succeeds(mock_sleep):
    """首次 429 後重試並在成功時回傳 data。"""
    from src.collectors.semantic_scholar import _s2_fetch_with_backoff

    resp_429 = MagicMock()
    resp_429.status_code = 429
    resp_ok = _make_response(200, [_make_paper()])

    mock_client = MagicMock()
    mock_client.get.side_effect = [resp_429, resp_ok]

    result = _s2_fetch_with_backoff(mock_client, {}, {}, "q")

    assert result is not None
    assert result["data"][0]["paperId"] == "p1"
    mock_sleep.assert_called_once_with(2.0)


@patch("src.collectors.semantic_scholar.time.sleep")
def test_429_all_retries_exhausted_returns_none(mock_sleep):
    """連續 429 耗盡重試後回傳 None。"""
    from src.collectors.semantic_scholar import _s2_fetch_with_backoff, _S2_429_MAX_RETRIES

    resp_429 = MagicMock()
    resp_429.status_code = 429
    mock_client = MagicMock()
    mock_client.get.return_value = resp_429

    result = _s2_fetch_with_backoff(mock_client, {}, {}, "q")

    assert result is None
    assert mock_client.get.call_count == _S2_429_MAX_RETRIES + 1


@patch("src.collectors.semantic_scholar.time.sleep")
def test_429_backoff_doubles(mock_sleep):
    """退避延遲遵循 2 → 4 → 8 模式。"""
    from src.collectors.semantic_scholar import _s2_fetch_with_backoff

    resp_429 = MagicMock()
    resp_429.status_code = 429
    resp_ok = _make_response(200, [])

    mock_client = MagicMock()
    mock_client.get.side_effect = [resp_429, resp_429, resp_ok]

    _s2_fetch_with_backoff(mock_client, {}, {}, "q")

    sleep_calls = [c.args[0] for c in mock_sleep.call_args_list]
    assert sleep_calls == [2.0, 4.0]


@patch("src.collectors.semantic_scholar.get_http_client")
def test_collect_handles_none_from_backoff(mock_get_client):
    """fetch 回傳 None（429 耗盡）時 collect 回傳空清單，不拋例外。"""
    from src.collectors.semantic_scholar import SemanticScholarCollector

    resp_429 = MagicMock()
    resp_429.status_code = 429
    mock_client = MagicMock()
    mock_get_client.return_value = mock_client
    mock_client.get.return_value = resp_429

    with patch("src.collectors.semantic_scholar.time.sleep"):
        items = SemanticScholarCollector().collect(date(2026, 6, 10))

    assert items == []
