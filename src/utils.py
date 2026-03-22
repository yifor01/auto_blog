"""Shared utilities: config loading, HTTP client, dedup, LLM calls."""

from __future__ import annotations

import itertools
import json
import os
from datetime import date, datetime
from pathlib import Path

import httpx
import yaml
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

console = Console()

from src.logger import get_logger as _get_logger  # noqa: E402
_logger = _get_logger("utils")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
SCORED_DIR = DATA_DIR / "scored"
FEEDBACK_DIR = DATA_DIR / "feedback"
HEALTH_DIR = DATA_DIR / "health"
OUTPUT_DIR = PROJECT_ROOT / "output"
POSTS_DIR = OUTPUT_DIR / "posts"
NOTES_DIR = OUTPUT_DIR / "notes"
PROMPTS_DIR = OUTPUT_DIR / "prompts"
DIGESTS_DIR = OUTPUT_DIR / "digests"
BLOGS_DIR = OUTPUT_DIR / "blogs"

for d in [RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR, POSTS_DIR, NOTES_DIR, PROMPTS_DIR, DIGESTS_DIR, BLOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

load_dotenv(PROJECT_ROOT / ".env")


def load_config() -> dict:
    config_path = PROJECT_ROOT / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


# ──────────────────────────────────────────────────────────
# Multi-key round-robin
# ──────────────────────────────────────────────────────────

_API_KEYS: list[str] = []
for _i in range(1, 10):  # 支援最多 9 組
    _k = os.getenv(f"AIHUBMIX_API_KEY_{_i}", "")
    if _k:
        _API_KEYS.append(_k)

# fallback 到舊的 OPENROUTER_API_KEY
if not _API_KEYS:
    _old_key = os.getenv("OPENROUTER_API_KEY", "")
    if _old_key:
        _API_KEYS.append(_old_key)

if not _API_KEYS:
    raise ValueError("No API keys configured (set AIHUBMIX_API_KEY_* or OPENROUTER_API_KEY)")

_key_cycle = itertools.cycle(_API_KEYS)
_logger.info("API keys loaded", extra={"key_count": len(_API_KEYS)})


def _get_api_base_url() -> str:
    """取得 API base URL：AIHUBMIX_API_URL > OPENROUTER_API_URL > config.yaml。"""
    url = os.getenv("AIHUBMIX_API_URL") or os.getenv("OPENROUTER_API_URL")
    if url:
        return url
    config = load_config()
    return config.get("llm", {}).get("api_url", "https://openrouter.ai/api/v1")


def get_next_api_key() -> str:
    """Round-robin 取得下一個 API key。"""
    return next(_key_cycle)


def get_llm_client() -> OpenAI:
    """建立帶有輪替 key 的 OpenAI-compatible client。每次呼叫使用下一個 key。"""
    api_key = get_next_api_key()
    return OpenAI(
        api_key=api_key,
        base_url=_get_api_base_url(),
    )


def _extract_content(resp) -> str:
    """從 LLM response 中提取文字內容。處理 DeepSeek R1 的 reasoning_content。"""
    msg = resp.choices[0].message
    # 正常 content
    if msg.content:
        return msg.content
    # DeepSeek R1 有時把回答放在 reasoning_content
    reasoning = getattr(msg, "reasoning_content", None)
    if reasoning:
        return reasoning
    return ""


def _try_model(client: OpenAI, model: str, messages: list[dict], max_tokens: int, temperature: float, max_retries: int) -> str | None:
    """嘗試用指定 client + model 呼叫 LLM，429 時 retry。成功回傳 content，全部失敗回傳 None。"""
    import time
    for attempt in range(max_retries + 1):
        try:
            resp = client.chat.completions.create(
                model=model, messages=messages,
                max_tokens=max_tokens, temperature=temperature,
            )
            content = _extract_content(resp)
            if content:
                return content
            return None  # empty → 讓外層嘗試下個選項
        except Exception as e:
            if "429" in str(e) and attempt < max_retries:
                wait = (attempt + 1) * 5
                _logger.warning("Rate limited, retrying", extra={"model": model, "wait_seconds": wait, "attempt": attempt + 1})
                time.sleep(wait)
                continue
            return None  # 非 429 或 retry 用盡 → 回傳 None
    return None


_OR_KEYS: list[str] = []
for _i in ["", "_2", "_3", "_4", "_5"]:
    _k = os.getenv(f"OPENROUTER_API_KEY{_i}", "")
    if _k:
        _OR_KEYS.append(_k)
_or_key_cycle = itertools.cycle(_OR_KEYS) if _OR_KEYS else None


def _get_openrouter_client() -> OpenAI | None:
    """建立 OpenRouter client（多 key 輪替）。"""
    if not _or_key_cycle:
        return None
    key = next(_or_key_cycle)
    config = load_config()
    or_cfg = config.get("llm", {}).get("openrouter_fallback", {})
    url = or_cfg.get("api_url") or os.getenv("OPENROUTER_API_URL") or "https://openrouter.ai/api/v1"
    return OpenAI(api_key=key, base_url=url)


def llm_chat(
    messages: list[dict],
    model: str | None = None,
    max_tokens: int | None = None,
    temperature: float = 0.7,
    max_retries: int = 2,
    fallback_model: str | None = None,
    is_generation: bool = False,
) -> str:
    """呼叫 LLM 並返回回應文字。三層 fallback：primary → fallback model → OpenRouter provider。"""
    config = load_config()
    llm_cfg = config["llm"]
    model = model or llm_cfg["model"]
    max_tokens = max_tokens or llm_cfg.get("max_tokens", 8192)
    fallback = fallback_model or llm_cfg.get("fallback_model")

    # Layer 1: Primary model（輪替 key）
    client = get_llm_client()
    result = _try_model(client, model, messages, max_tokens, temperature, max_retries)
    if result:
        return result

    # Layer 2: Fallback model（輪替 key）
    if fallback and fallback != model:
        _logger.warning("Primary failed, trying fallback model", extra={"model": model, "fallback": fallback})
        client = get_llm_client()
        result = _try_model(client, fallback, messages, max_tokens, temperature, max_retries)
        if result:
            return result

    # Layer 3: OpenRouter provider fallback
    or_cfg = llm_cfg.get("openrouter_fallback", {})
    or_client = _get_openrouter_client()
    if or_client and or_cfg:
        or_model = or_cfg.get("generation_model" if is_generation else "model", or_cfg.get("model", ""))
        if or_model:
            _logger.warning("Provider fallback to OpenRouter", extra={"model": or_model})
            result = _try_model(or_client, or_model, messages, max_tokens, temperature, max_retries)
            if result:
                return result
            _logger.error("OpenRouter fallback also failed", extra={"model": or_model})

    return ""


def get_http_client() -> httpx.Client:
    return httpx.Client(
        timeout=30,
        headers={"User-Agent": "AutoPostBlog/0.1"},
        follow_redirects=True,
    )


def today_str() -> str:
    return date.today().isoformat()


def date_to_chatpaper_ts(d: date) -> int:
    """將 date 轉換為 ChatPaper API 的 Unix timestamp（Asia/Taipei, UTC+8）。

    明確指定 Asia/Taipei 時區，避免在非 UTC+8 主機上產生錯誤時間範圍。
    例如: datetime(2026, 2, 20, tzinfo=Asia/Taipei) → 1771516800
    """
    from zoneinfo import ZoneInfo
    tz = ZoneInfo("Asia/Taipei")
    dt = datetime(d.year, d.month, d.day, 0, 0, 0, tzinfo=tz)
    return int(dt.timestamp())


def save_json(data: list | dict, path: Path) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)


def load_json(path: Path) -> list | dict:
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_seen_urls(exclude_date: date | None = None, lookback_days: int | None = None) -> set[str]:
    """載入已收集過的 URL/arxiv_id 集合，用於跨日去重。

    Args:
        exclude_date: 排除此日期的資料（通常是今天，避免把自己排除）
        lookback_days: 只回看最近 N 天（None 表示全部）
    """
    from datetime import timedelta
    seen: set[str] = set()

    cutoff: date | None = None
    if lookback_days is not None and exclude_date is not None:
        cutoff = exclude_date - timedelta(days=lookback_days)

    for f in RAW_DIR.glob("*.json"):
        # 跳過今天的檔案
        if exclude_date and f.stem == exclude_date.isoformat():
            continue
        # 只回看 lookback_days 天
        if cutoff:
            try:
                file_date = date.fromisoformat(f.stem)
                if file_date < cutoff:
                    continue
            except ValueError:
                continue
        try:
            items = load_json(f)
            if isinstance(items, list):
                for item in items:
                    url = item.get("url", "")
                    if url:
                        seen.add(url)
                    arxiv_id = item.get("raw_metadata", {}).get("arxiv_id", "")
                    if arxiv_id:
                        seen.add(f"arxiv:{arxiv_id}")
        except Exception:
            continue
    return seen


def slugify(text: str, max_len: int = 60) -> str:
    """將標題轉為檔名安全的 slug."""
    import re

    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text.strip())
    return text[:max_len].rstrip("-").lower()


def extract_full_text_from_html(html: str, max_chars: int = 2000) -> str:
    """從 HTML 提取純文字，優先選取語意容器標籤，fallback 到 <p> 聚合。"""
    import re

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")

    # 移除干擾元素
    for tag in soup.select("script, style, nav, footer, header, aside, .sidebar, .comments, .nav, .menu"):
        tag.decompose()

    # 嘗試語意容器（擴充 selector）
    body = soup.select_one(
        "article, .post-content, .entry-content, main, .content, "
        "[role='main'], .article-body, .c-entry-content, .post-body, "
        ".blog-post, .hentry, .h-entry, .e-content, #content, #main"
    )
    if body:
        text = body.get_text(separator=" ", strip=True)
        text = re.sub(r"\s{2,}", " ", text)
        if len(text) >= 200:
            return text[:max_chars]

    # Fallback: 聚合所有 <p> 標籤（排除過短段落）
    paragraphs = soup.find_all("p")
    p_texts = []
    for p in paragraphs:
        t = p.get_text(separator=" ", strip=True)
        if len(t) >= 30:  # 跳過極短段落（廣告、版權等）
            p_texts.append(t)
    if p_texts:
        text = " ".join(p_texts)
        text = re.sub(r"\s{2,}", " ", text)
        if len(text) >= 100:
            return text[:max_chars]

    # 最終 fallback: 整頁文字
    text = soup.get_text(separator=" ", strip=True)
    return re.sub(r"\s{2,}", " ", text)[:max_chars]


def fetch_article_text(url: str, client: httpx.Client, max_chars: int = 2000) -> str:
    """GET 文章 URL，返回純文字。失敗時返回空字串並記錄 debug log。"""
    try:
        resp = client.get(url, timeout=12)
        if resp.status_code != 200:
            _logger.debug("fetch_article_text non-200", extra={"url": url, "status_code": resp.status_code})
            return ""
        text = extract_full_text_from_html(resp.text, max_chars)
        if not text:
            _logger.debug("fetch_article_text empty extraction", extra={"url": url, "html_len": len(resp.text)})
        return text
    except Exception as e:
        _logger.debug("fetch_article_text request failed", extra={"url": url, "error": str(e)})
    return ""


def build_link_abstract(
    url: str, client: httpx.Client, engagement: str, fallback_domain: str, max_chars: int = 1500
) -> str:
    """Link post 共用 helper：嘗試抓取外部文章內容，失敗時 fallback 到 domain + engagement。"""
    fetched = fetch_article_text(url, client, max_chars)
    if fetched:
        return f"{fetched}\n\n({engagement})"
    return f"{fallback_domain} — {engagement}"
