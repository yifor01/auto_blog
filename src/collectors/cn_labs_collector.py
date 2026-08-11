"""中國 AI 實驗室官方 blog collector（JSON API）。

這幾家的官網都是 CSR SPA，既沒有 RSS 也爬不到 HTML（blog collector 實測全 0 筆），
但前端各自打自己的 JSON API 取內容——本 collector 直接打那些 API。

實測 2026-08-11：Qwen 與 MiniMax 有乾淨的 JSON API；ByteDance Seed 前端只有埋點
請求、HTML 也不含資料，智譜（zhipuai.cn）的內容埋在 Next.js RSC flight payload 裡，
兩者都沒有可用端點，因此不納入。
"""

from __future__ import annotations

import re
from datetime import date, datetime, timezone
from urllib.parse import urljoin

import httpx

from src.collectors._helpers import infer_organization
from src.collectors.base import BaseCollector
from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import (
    ABSTRACT_MAX_CHARS_DEFAULT,
    extract_full_text_from_html,
    fetch_article_text,
    get_http_client,
    load_config,
)

_logger = get_logger("collectors.cn_labs")

# 中文站與英文站回的是同一批文章，只差語言；取 zh-CN 讓 Layer A 的 s2twp 轉成繁中。
_QWEN_API = "https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN"
_MINIMAX_API = "https://www.minimax.io/api/news?page=1&locale=en"

# API 一次回全部歷史文章（Qwen 34 篇跨 1.5 年），不過濾會每天把舊文重新灌進評分。
MAX_AGE_DAYS_DEFAULT = 7

# MiniMax 列表只給一句 summary，太短的補抓詳情頁全文。
_MINIMAX_SUMMARY_MIN_CHARS = 200

_PUBLISHED_META_RE = re.compile(
    r'article:published_time"\s+content="([^"]+)"'
)


def _parse_published_meta(html: str) -> date | None:
    """從文章頁 HTML 抽 `article:published_time`。抽不到回 None。

    Qwen 的 API 沒有日期欄位，日期只存在於 content 那一整頁 HTML 的 meta 裡。
    """
    m = _PUBLISHED_META_RE.search(html)
    if not m:
        return None
    try:
        return datetime.fromisoformat(m.group(1)).date()
    except ValueError:
        return None


def _collect_qwen(
    client: httpx.Client, target_date: date, cutoff: date, max_chars: int
) -> list[ContentItem]:
    resp = client.get(_QWEN_API)
    resp.raise_for_status()
    articles = resp.json().get("data", {}).get("articles", [])

    items: list[ContentItem] = []
    for article in articles:
        path = article.get("path", "")
        title = article.get("title", "")
        content = article.get("content", "")
        if not path or not title:
            continue

        published = _parse_published_meta(content)
        if published is None or published < cutoff:
            continue

        # content 裡的 canonical 指向 qwenlm.github.io，但那個站已停更，新文章
        # 一律 404（實測 qwen3.8 篇）——照抄 canonical 等於整批死連結。
        url = f"https://qwen.ai/blog?id={path}"
        items.append(
            ContentItem(
                source=SourceType.CN_LABS,
                source_name="Qwen",
                title=title,
                url=url,
                abstract=extract_full_text_from_html(content, max_chars),
                published_date=published,
                organization=infer_organization("Qwen", url),
                raw_metadata={"provider": "qwen", "path": path},
            )
        )
    return items


def _parse_minimax_date(value: object) -> date | None:
    """MiniMax 的 `publishDate` 同一欄位混用兩種型別，兩種都要吃。

    實測 2026-08-11 同一頁回應裡：新文章是毫秒 epoch 整數（1785756267890），
    2026-05 以前的舊文章是 ISO 8601 字串（"2026-05-24T16:00:00.000Z"）。
    只處理其中一種會在跑進舊文時整個 provider 拋例外。
    """
    if isinstance(value, (int, float)):
        return datetime.fromtimestamp(value / 1000, tz=timezone.utc).date()
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
        except ValueError:
            return None
    return None


def _collect_minimax(
    client: httpx.Client, target_date: date, cutoff: date, max_chars: int
) -> list[ContentItem]:
    resp = client.get(_MINIMAX_API)
    resp.raise_for_status()
    news = resp.json().get("data", [])

    items: list[ContentItem] = []
    for entry in news:
        slug = entry.get("slug", "")
        title = entry.get("title", "")
        if not slug or not title:
            continue

        published = _parse_minimax_date(entry.get("publishDate"))
        if published is None or published < cutoff:
            continue

        url = f"https://www.minimax.io/news/{slug}"
        abstract = entry.get("summary", "")
        if len(abstract) < _MINIMAX_SUMMARY_MIN_CHARS:
            abstract = fetch_article_text(url, client, max_chars) or abstract

        items.append(
            ContentItem(
                source=SourceType.CN_LABS,
                source_name="MiniMax",
                title=title,
                url=url,
                abstract=abstract,
                published_date=published,
                tags=entry.get("tags", []),
                organization=infer_organization("MiniMax", url),
                raw_metadata={"provider": "minimax", "slug": slug},
            )
        )
    return items


_DEEPSEEK_NEWS_INDEX = "https://api-docs.deepseek.com/news/"
_DEEPSEEK_SLUG_RE = re.compile(r"/news/(news\d+)")


def _parse_deepseek_slug_date(slug: str) -> date | None:
    """DeepSeek 的公告 slug 內嵌日期：`news260424` → 2026-04-24。

    2024 年的舊公告用 4 碼 `newsMMDD`（news0725 / news1226），年份不在 slug 裡也
    不在頁面上，無從還原——一律回 None 跳過。那些都遠早於任何 max_age_days 窗口，
    真正要解析的只有 6 碼 YYMMDD 這種新格式。
    """
    digits = slug[len("news"):]
    if len(digits) != 6:
        return None
    try:
        return datetime.strptime(digits, "%y%m%d").date()
    except ValueError:
        return None


def _deepseek_body_text(html: str, max_chars: int) -> str:
    """取 docusaurus 的正文容器再抽文字。

    直接把整頁丟給 extract_full_text_from_html 會選到外層 `<article>`，開頭黏上
    右側目錄的 "On this page" 與整串小標——每篇都一樣，正好蓋掉 LLM 最看重的前幾句。
    """
    from bs4 import BeautifulSoup

    body = BeautifulSoup(html, "html.parser").select_one(".theme-doc-markdown")
    return extract_full_text_from_html(str(body) if body else html, max_chars)


def _collect_deepseek(
    client: httpx.Client, target_date: date, cutoff: date, max_chars: int
) -> list[ContentItem]:
    """DeepSeek 官方公告（API 文件站的 news 區）。

    索引頁只列最新一篇，側欄的完整清單要 JS 才展開——但這裡本來就只要新文章，
    所以吃索引頁列出的那幾篇就夠。日期先從 slug 解出來過濾，過濾掉的不必抓內文。
    """
    resp = client.get(_DEEPSEEK_NEWS_INDEX)
    resp.raise_for_status()

    items: list[ContentItem] = []
    for slug in dict.fromkeys(_DEEPSEEK_SLUG_RE.findall(resp.text)):
        published = _parse_deepseek_slug_date(slug)
        if published is None or published < cutoff:
            continue

        url = f"https://api-docs.deepseek.com/news/{slug}"
        page = client.get(url)
        if page.status_code != 200:
            continue

        title_match = re.search(r"<h1[^>]*>([^<]{3,120})</h1>", page.text)
        if not title_match:
            continue

        items.append(
            ContentItem(
                source=SourceType.CN_LABS,
                source_name="DeepSeek",
                title=title_match.group(1).strip(),
                url=url,
                abstract=_deepseek_body_text(page.text, max_chars),
                published_date=published,
                organization=infer_organization("DeepSeek", url),
                raw_metadata={"provider": "deepseek", "slug": slug},
            )
        )
    return items


_KIMI_INDEX = "https://www.kimi.com/blog/"

def _collect_kimi(
    client: httpx.Client, target_date: date, cutoff: date, max_chars: int
) -> list[ContentItem]:
    """Moonshot AI（Kimi）技術 blog。

    日期只在索引頁的卡片上（`2026/07/16`），文章頁沒有任何發布日期——頁面裡看起來
    像日期的字串全是圖片 CDN 路徑的上傳日（`kimi-file.moonshot.cn/.../2026-07-17/`），
    拿去當發布日會系統性偏移。所以日期一律取自索引頁卡片。
    """
    from bs4 import BeautifulSoup

    resp = client.get(_KIMI_INDEX)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    items: list[ContentItem] = []
    seen: set[str] = set()
    for card in soup.select(".card-body"):
        title_el = card.select_one(".card-title")
        date_el = card.select_one(".card-date")
        if not (title_el and date_el):
            continue

        # 卡片結構是 div > [a.absolute（整片覆蓋的連結）, div.card-body]，連結與標題是
        # 兄弟而非父子，所以從 card-body 的**父層**取 a。只看一層是刻意的：再往上
        # 就會跨到別張卡片，把 2024 年那些連到 arXiv 的舊卡片配上隔壁的 /blog/ 連結。
        parent = card.parent
        link = parent.find("a", href=lambda h: h and h.startswith("/blog/")) if parent else None
        if not link or link["href"] in seen:
            continue
        href = link["href"]
        seen.add(href)

        try:
            published = datetime.strptime(date_el.get_text(strip=True), "%Y/%m/%d").date()
        except ValueError:
            continue
        if published < cutoff:
            continue

        url = urljoin(_KIMI_INDEX, href)
        items.append(
            ContentItem(
                source=SourceType.CN_LABS,
                source_name="Kimi",
                title=title_el.get_text(strip=True),
                url=url,
                abstract=fetch_article_text(url, client, max_chars),
                published_date=published,
                organization=infer_organization("Kimi", url),
                raw_metadata={"provider": "kimi", "path": href},
            )
        )
    return items


_PROVIDERS = {
    "qwen": _collect_qwen,
    "minimax": _collect_minimax,
    "deepseek": _collect_deepseek,
    "kimi": _collect_kimi,
}


class CNLabsCollector(BaseCollector):
    name = "cn_labs"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config.get("collectors", {}).get("cn_labs", {})
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        max_chars = config.get("collectors", {}).get(
            "abstract_max_chars", ABSTRACT_MAX_CHARS_DEFAULT
        )
        max_age_days = cfg.get("max_age_days", MAX_AGE_DAYS_DEFAULT)
        cutoff = date.fromordinal(target_date.toordinal() - max_age_days)
        sources = cfg.get("sources", list(_PROVIDERS))

        items: list[ContentItem] = []
        client = get_http_client()
        try:
            for provider in sources:
                fetch = _PROVIDERS.get(provider)
                if fetch is None:
                    _logger.warning("Unknown cn_labs provider", extra={"provider": provider})
                    continue
                try:
                    collected = fetch(client, target_date, cutoff, max_chars)
                    items.extend(collected)
                    _logger.info(
                        "CN lab collected",
                        extra={"provider": provider, "count": len(collected)},
                    )
                except Exception as e:
                    _logger.error(
                        "CN lab error", extra={"provider": provider, "error": str(e)}
                    )
        finally:
            client.close()

        _logger.info("CN labs collection complete", extra={"total_count": len(items)})
        return items
