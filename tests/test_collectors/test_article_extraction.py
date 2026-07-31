"""文章正文提取：容器優先序、雜訊剝除、句界截斷。

背景（2026-07-31 root cause）：
`extract_full_text_from_html` 原本把整串 selector 丟給 `select_one`，而 CSS
`select_one` 依**文件順序**回傳第一個 match——外層容器必然排在內層之前，
所以 selector 列表「由精確到泛用」的意圖完全失效，每個站都選到最外層 `main`，
把 Topics / Most Popular 等推薦區一起吃進 abstract。

加上 `text[:max_chars]` 的硬切與寫死的 2000 上限，實測 18 個 RSS 來源
全部撞到上限且斷在句中（例：`…what you did is competitive, not`）。
"""


# 依 TechCrunch 實際 DOM 結構：main 為最外層，正文在 .entry-content，
# 推薦區（Topics / Most Popular）是 .entry-content 的 sibling、同在 main 之下。
TECHCRUNCH_LIKE_HTML = """
<html><body>
<main class="wp-block-group template-content">
  <div class="entry-content">
    <p>Andon Labs published a new installment of its Vending-Bench research, where
       frontier models run a simulated vending machine business for a simulated year.</p>
    <p>The models grew especially shady after the simulation placed them together on a
       busy tourist street, each given email access to the others under pseudonyms.</p>
    <p>Sol soon realized it could gain an edge by convincing its competitors to collude
       on a price floor, then immediately undercut them by a single cent.</p>
  </div>
  <div class="wp-block-tc23-post-relevant-terms">Topics AI Startups Exclusive</div>
  <section class="river river--homepage">
    <h2>Most Popular</h2>
    <p>SpaceX launches new V3 Starlink satellites but suffers another booster failure</p>
    <p>Prentis, new AI lab co-founded by Reid Hoffman, in talks to raise $100M</p>
  </section>
</main>
</body></html>
"""


def test_prefers_inner_content_container_over_outer_main():
    """正文容器比最外層 main 精確時應選正文容器，不把推薦區吃進來。"""
    from src.utils import extract_full_text_from_html

    result = extract_full_text_from_html(TECHCRUNCH_LIKE_HTML)

    assert "Vending-Bench research" in result
    assert "grew especially shady" in result
    assert "Most Popular" not in result
    assert "Starlink" not in result


def test_strips_related_posts_when_only_outer_container_exists():
    """只有泛用容器可選時，仍須剝除推薦 / 訂閱 / 分享等雜訊區塊。"""
    from src.utils import extract_full_text_from_html

    html = """
    <html><body>
    <main>
      <p>The actual article body explains how the benchmark was constructed in detail.</p>
      <div class="related-posts"><p>Related: another article you might like reading</p></div>
      <div class="newsletter-signup"><p>Subscribe to our daily newsletter for more</p></div>
      <div class="social-share"><p>Share this on X and LinkedIn right now</p></div>
    </main>
    </body></html>
    """
    result = extract_full_text_from_html(html)

    assert "actual article body" in result
    assert "Related:" not in result
    assert "Subscribe to our daily" not in result
    assert "Share this on X" not in result


_LONG_PARA = (
    "The Claude Partner Network brings Claude into the everyday work of demanding industries, "
    "the kinds of contexts where the model has to sustain long-running tasks without supervision. "
    "This paragraph exists to push the container past the minimum length threshold for selection. "
)


def test_strips_trailing_recommendation_section_with_hashed_class_names():
    """class 被雜湊（CSS modules / Next.js）時，靠尾段標題剝除推薦區。

    Anthropic 等站的推薦區 class 形如 `LinkGrid-module-scss-module__wTN57W__intro`，
    語意關鍵字比對完全無效。
    """
    from src.utils import extract_full_text_from_html

    html = f"""
    <html><body><article>
      <div class="Prose-module__aB3xz__root"><p>{_LONG_PARA * 2}</p></div>
      <section class="LandingPageSection-module-scss-module__ZSMdoa__root">
        <div class="SectionIntro-module__i9TRza__root"><h2>Related content</h2></div>
        <p>Investigating three real-world incidents in our cybersecurity evaluations</p>
      </section>
    </article></body></html>
    """
    result = extract_full_text_from_html(html)

    assert "Claude Partner Network" in result
    assert "Related content" not in result
    assert "cybersecurity evaluations" not in result


def test_trailing_strip_does_not_swallow_the_body_container():
    """推薦區深埋在正文容器內時，只能剝該區塊，不得連正文容器一起剝掉。

    The Verge 實例：h2 "Most Popular" 距容器 8 層，若無腦上溯到容器的直接子節點，
    會剝掉整個 entry-body-container（8131 字元正文只剩 506）。
    """
    from src.utils import extract_full_text_from_html

    html = f"""
    <html><body><article>
      <div class="entry-body-container">
        <div class="body-copy"><p>{_LONG_PARA * 4}</p></div>
        <div class="footer-widgets"><div><div><section><h2>Most popular</h2>
          <p>Some unrelated trending headline nobody asked for</p>
        </section></div></div></div>
      </div>
    </article></body></html>
    """
    result = extract_full_text_from_html(html)

    assert "Claude Partner Network" in result
    assert len(result) > 800, f"正文被連帶剝除（len={len(result)}）"
    assert "unrelated trending headline" not in result


def test_keeps_recommendation_like_heading_in_article_body():
    """同樣的標題出現在正文中段時不得被誤殺（只剝尾段）。"""
    from src.utils import extract_full_text_from_html

    html = f"""
    <html><body><article>
      <div><h2>Most popular</h2>
      <p>This section is part of the article body and discusses which models were most popular.</p>
      <p>{_LONG_PARA * 3}</p></div>
    </article></body></html>
    """
    result = extract_full_text_from_html(html)

    assert "part of the article body" in result


def test_truncate_at_boundary_returns_text_unchanged_when_within_limit():
    """未超過上限時原樣返回。"""
    from src.utils import truncate_at_boundary

    text = "Short enough. No truncation needed."
    assert truncate_at_boundary(text, 100) == text


def test_truncate_at_boundary_cuts_at_sentence_end():
    """超過上限時退回最後一個完整句子，不斷在句中。"""
    from src.utils import truncate_at_boundary

    text = "First sentence is here. Second sentence follows. Third sentence trails off"
    result = truncate_at_boundary(text, 60)

    assert result.endswith(".")
    assert "Second sentence follows." in result
    assert "Third sentence" not in result


def test_truncate_at_boundary_handles_cjk_punctuation():
    """中文句號同樣視為句界。"""
    from src.utils import truncate_at_boundary

    text = "第一句話在這裡。第二句話接著出現。第三句話被截斷"
    result = truncate_at_boundary(text, 20)

    assert result.endswith("。")
    assert "第三句話" not in result


def test_truncate_at_boundary_falls_back_to_word_boundary():
    """沒有句界可退時退到詞界，仍不得切在單字中間。"""
    from src.utils import truncate_at_boundary

    text = "alpha bravo charlie delta echo foxtrot golf hotel india juliett kilo lima"
    result = truncate_at_boundary(text, 40)

    assert not result.endswith(" ")
    # 切點必須落在原文的詞界上
    assert text.startswith(result)
    assert text[len(result)] == " "


def test_truncate_at_boundary_does_not_discard_most_of_the_window():
    """句界離切點太遠時不得回退過頭（避免只剩開頭一句）。"""
    from src.utils import truncate_at_boundary

    # 只有開頭有一個句號，其餘 200 字元無標點
    text = "Tiny lead. " + "x" * 200
    result = truncate_at_boundary(text, 150)

    assert len(result) > 100, f"回退過頭，只剩 {len(result)} 字元"


def test_default_max_chars_no_longer_caps_articles_at_2000():
    """預設上限須容納一般新聞全文（原 2000 會腰斬近七成內容）。"""
    from src.utils import extract_full_text_from_html

    body = "".join(f"<p>Paragraph number {i} with a fair amount of filler text here.</p>" for i in range(120))
    html = f'<html><body><main><div class="entry-content">{body}</div></main></body></html>'

    result = extract_full_text_from_html(html)

    assert len(result) > 2000, f"仍被 2000 上限截斷（len={len(result)}）"


def test_explicit_max_chars_is_respected():
    """呼叫端傳入的上限仍然有效。"""
    from src.utils import extract_full_text_from_html

    body = "".join(f"<p>Sentence {i} padding text goes here.</p>" for i in range(200))
    html = f'<html><body><main><div class="entry-content">{body}</div></main></body></html>'

    result = extract_full_text_from_html(html, 500)

    assert len(result) <= 500


# --- collector 端：上限須可由 config 調整，預設不再是寫死的 2000 ---

from datetime import date  # noqa: E402
from unittest.mock import MagicMock, patch  # noqa: E402

_LONG_BODY = "".join(f"<p>Paragraph {i} carries a fair amount of filler text here.</p>" for i in range(120))
_LONG_ARTICLE_HTML = f'<html><body><main><div class="entry-content">{_LONG_BODY}</div></main></body></html>'


def _rss_config(abstract_max_chars=None):
    cfg = {
        "collectors": {
            "rss": {
                "enabled": True,
                "feeds": [{"name": "TechCrunch AI", "url": "https://techcrunch.com/feed/"}],
            }
        }
    }
    if abstract_max_chars is not None:
        cfg["collectors"]["abstract_max_chars"] = abstract_max_chars
    return cfg


def _feed_entry():
    entry = MagicMock()
    entry.get = lambda k, d="": {
        "title": "Claude Opus 5 became downright ruthless",
        "link": "https://techcrunch.com/2026/07/29/vending-machine/",
        "published": "Wed, 29 Jul 2026 12:00:00 +0000",
        "authors": [],
        "tags": [],
    }.get(k, d)
    entry.content = [{"value": _LONG_ARTICLE_HTML}]
    entry.summary = ""
    entry.description = ""
    return entry


def test_rss_extract_abstract_not_capped_at_2000_by_default():
    """RSS abstract 預設不再被 2000 腰斬。"""
    from src.collectors.rss_collector import RSSCollector

    result = RSSCollector._extract_abstract(_feed_entry(), "", MagicMock())

    assert len(result) > 2000, f"仍被 2000 截斷（len={len(result)}）"


@patch("src.collectors.rss_collector.get_http_client")
@patch("src.collectors.rss_collector.feedparser.parse")
@patch("src.collectors.rss_collector.load_config")
def test_rss_collector_honors_config_abstract_max_chars(mock_cfg, mock_feedparser, mock_get_client):
    """collectors.abstract_max_chars 可調整 abstract 上限。"""
    from src.collectors.rss_collector import RSSCollector

    mock_cfg.return_value = _rss_config(abstract_max_chars=600)
    mock_feedparser.return_value = MagicMock(entries=[_feed_entry()])
    mock_get_client.return_value = MagicMock()

    items = RSSCollector().collect(target_date=date(2026, 7, 29))

    assert len(items) == 1
    assert len(items[0].abstract) <= 600


def test_blog_collector_honors_max_chars_argument():
    """blog collector 走同一個上限參數（原本同樣寫死 2000）。"""
    from src.collectors.blog_collector import BlogCollector

    items = BlogCollector()._parse_feed_entries(
        [_feed_entry()],
        "Anthropic News",
        "https://www.anthropic.com/rss.xml",
        date(2026, 7, 29),
        MagicMock(),
        max_chars=600,
    )

    assert len(items) == 1
    assert len(items[0].abstract) <= 600


def test_build_link_abstract_not_capped_at_1500_by_default():
    """HN / Reddit 的 link post 走同一套上限，不再各自寫死 1500。"""
    from src.utils import build_link_abstract

    client = MagicMock()
    resp = MagicMock()
    resp.status_code, resp.text = 200, _LONG_ARTICLE_HTML
    client.get.return_value = resp

    result = build_link_abstract("https://example.com/post", client, "120 points", "example.com")

    assert len(result) > 1500, f"仍被 1500 截斷（len={len(result)}）"
    assert "120 points" in result


def test_blog_scrape_html_uses_shared_extraction():
    """無 RSS 的部落格走 HTML fallback 時，須用共用提取邏輯。

    原本 `_scrape_html` 自帶第三份複製：同樣的 select_one 祖先優先 bug、
    只取前 3 個 <p>、再 `[:1000]` 硬切。
    """
    from src.collectors.blog_collector import BlogCollector

    index_html = '<html><body><article><a href="/posts/vending">Claude Opus 5 became ruthless</a></article></body></html>'

    client = MagicMock()
    index_resp, article_resp = MagicMock(), MagicMock()
    index_resp.status_code, index_resp.text = 200, index_html
    article_resp.status_code, article_resp.text = 200, _LONG_ARTICLE_HTML
    client.get.side_effect = [index_resp, article_resp]

    items = BlogCollector()._scrape_html(client, "Some Blog", "https://blog.example.com", date(2026, 7, 29))

    assert len(items) == 1
    assert len(items[0].abstract) > 1000, f"仍被 1000 硬切（len={len(items[0].abstract)}）"


def test_github_readme_not_capped_at_1500():
    """GitHub README 原本 `readme_text[:1500]` 硬切，實測 91.6% 撞頂。"""
    from src.collectors.github_trending import GitHubTrendingCollector

    readme = "".join(f"<p>Section {i} of the readme explains one more configuration flag.</p>" for i in range(80))
    trending_html = """
    <html><body><article class="Box-row">
      <h2><a href="/acme/llm-agent">acme/llm-agent</a></h2>
      <p class="color-fg-muted">An LLM agent framework</p>
    </article></body></html>
    """
    repo_html = f'<html><body><article class="markdown-body">{readme}</article></body></html>'

    trending_resp, repo_resp = MagicMock(), MagicMock()
    trending_resp.status_code, trending_resp.text = 200, trending_html
    repo_resp.status_code, repo_resp.text = 200, repo_html
    client = MagicMock()
    client.get.side_effect = [trending_resp, repo_resp]

    cfg = {"collectors": {"github": {"enabled": True, "languages": ["python"]}}}
    with patch("src.collectors.github_trending.load_config", return_value=cfg), patch(
        "src.collectors.github_trending.get_http_client", return_value=client
    ), patch("src.collectors.github_trending.time.sleep"):
        items = GitHubTrendingCollector().collect(target_date=date(2026, 7, 29))

    assert len(items) == 1
    assert len(items[0].abstract) > 1500, f"仍被 1500 硬切（len={len(items[0].abstract)}）"


def test_reddit_selftext_not_capped_at_500():
    """Reddit self post 原本 `selftext[:500]` 硬切，實測 36.6% 撞頂。"""
    from src.collectors.reddit_collector import RedditCollector

    from datetime import datetime
    from zoneinfo import ZoneInfo

    selftext = "This paragraph explains one more detail about the setup. " * 40
    # created_utc 必須落在 target_date 的台灣時區當日，否則會被日期過濾掉
    created = datetime(2026, 7, 29, 10, tzinfo=ZoneInfo("Asia/Taipei")).timestamp()
    payload = {
        "data": {
            "children": [
                {
                    "data": {
                        "title": "How I run local models on a laptop",
                        "url": "https://reddit.com/r/LocalLLaMA/x",
                        "permalink": "/r/LocalLLaMA/x",
                        "is_self": True,
                        "selftext": selftext,
                        "score": 500,
                        "num_comments": 42,
                        "created_utc": created,
                        "author": "someone",
                    }
                }
            ]
        }
    }
    resp = MagicMock()
    resp.status_code, resp.json = 200, lambda: payload
    client = MagicMock()
    client.get.return_value = resp

    cfg = {"collectors": {"reddit": {"enabled": True, "subreddits": ["LocalLLaMA"], "min_upvotes": 10}}}
    with patch("src.collectors.reddit_collector.load_config", return_value=cfg), patch(
        "src.collectors.reddit_collector.get_http_client", return_value=client
    ), patch("src.collectors.reddit_collector.os.getenv", return_value=None):
        items = RedditCollector().collect(target_date=date(2026, 7, 29))

    assert len(items) >= 1
    assert len(items[0].abstract) > 500, f"仍被 500 硬切（len={len(items[0].abstract)}）"


def test_blog_collector_not_capped_at_2000_by_default():
    """未指定上限時不再被 2000 腰斬。"""
    from src.collectors.blog_collector import BlogCollector

    items = BlogCollector()._parse_feed_entries(
        [_feed_entry()],
        "Anthropic News",
        "https://www.anthropic.com/rss.xml",
        date(2026, 7, 29),
        MagicMock(),
    )

    assert len(items) == 1
    assert len(items[0].abstract) > 2000
