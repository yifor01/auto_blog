"""Shared utilities: config loading, HTTP client, dedup, LLM calls."""

from __future__ import annotations

import itertools
import json
import os
from datetime import date, datetime
from pathlib import Path

import time

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
# OpenRouter 多 key 輪替 + 多 model 降級
# ──────────────────────────────────────────────────────────

_API_KEYS: list[str] = []
for _suffix in ["", "_2", "_3", "_4", "_5", "_6", "_7", "_8", "_9"]:
    _k = os.getenv(f"OPENROUTER_API_KEY{_suffix}", "")
    if _k:
        _API_KEYS.append(_k)

if not _API_KEYS:
    raise ValueError("No OpenRouter API keys configured (set OPENROUTER_API_KEY[_2..9])")

_key_cycle = itertools.cycle(_API_KEYS)
_logger.info("API keys loaded", extra={"provider": "openrouter", "key_count": len(_API_KEYS)})

# 執行期可被 preflight 修改的 healthy model chains（初始為 None 代表尚未載入）
_scoring_chain: list[str] | None = None
_generation_chain: list[str] | None = None


def _get_api_base_url() -> str:
    url = os.getenv("OPENROUTER_API_URL")
    if url:
        return url
    config = load_config()
    return config.get("llm", {}).get("api_url", "https://openrouter.ai/api/v1")


def get_next_api_key() -> str:
    """Round-robin 取得下一個 API key。"""
    return next(_key_cycle)


def get_llm_client() -> OpenAI:
    """建立帶有輪替 key 的 OpenAI-compatible client。每次呼叫使用下一個 key。"""
    return OpenAI(api_key=get_next_api_key(), base_url=_get_api_base_url())


def _extract_content(resp) -> str:
    msg = resp.choices[0].message
    if msg.content:
        return msg.content
    # DeepSeek R1 有時把回答放在 reasoning_content
    reasoning = getattr(msg, "reasoning_content", None)
    return reasoning or ""


def _try_model(
    client: OpenAI,
    model: str,
    messages: list[dict],
    max_tokens: int,
    temperature: float,
    max_retries: int,
) -> str | None:
    """單一 (client, model) 呼叫：429 retry，其他 error 或 empty 直接回 None。"""
    for attempt in range(max_retries + 1):
        try:
            resp = client.chat.completions.create(
                model=model, messages=messages,
                max_tokens=max_tokens, temperature=temperature,
            )
            content = _extract_content(resp)
            return content or None
        except Exception as e:
            err = str(e)
            if "429" in err and attempt < max_retries:
                wait = (attempt + 1) * 5
                _logger.warning("Rate limited, retrying", extra={"model": model, "wait_seconds": wait, "attempt": attempt + 1})
                time.sleep(wait)
                continue
            _logger.debug("Model call failed", extra={"model": model, "error": err[:200]})
            return None
    return None


def _load_default_chains() -> tuple[list[str], list[str]]:
    """從 config.yaml 讀取 scoring_models / generation_models。缺失時退回 legacy 單 model。"""
    cfg = load_config().get("llm", {})
    scoring = list(cfg.get("scoring_models") or [])
    generation = list(cfg.get("generation_models") or [])
    # legacy fallback：舊 config 只有 model / generation_model
    if not scoring and cfg.get("model"):
        scoring = [cfg["model"]]
        if cfg.get("fallback_model"):
            scoring.append(cfg["fallback_model"])
    if not generation and cfg.get("generation_model"):
        generation = [cfg["generation_model"]]
        if cfg.get("generation_fallback_model"):
            generation.append(cfg["generation_fallback_model"])
    return scoring, generation


def _get_chain(is_generation: bool) -> list[str]:
    global _scoring_chain, _generation_chain
    if _scoring_chain is None or _generation_chain is None:
        s, g = _load_default_chains()
        _scoring_chain = s
        _generation_chain = g
    return _generation_chain if is_generation else _scoring_chain


def _probe_model(model: str, timeout: float = 15.0) -> tuple[bool, str]:
    """對單一 model 送最小 probe call。回傳 (alive, err_msg)。"""
    client = get_llm_client()
    try:
        resp = client.with_options(timeout=timeout).chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "ping"}],
            max_tokens=5, temperature=0.0,
        )
        _ = _extract_content(resp)
        return True, ""
    except Exception as e:
        return False, str(e)[:200]


def discover_free_models(min_context: int = 32000, limit: int = 12) -> list[str]:
    """向 OpenRouter /models 查詢 pricing 全為 0 的 model，按 context 降序排序。
    用於 preflight 發現 configured chain 全死時的 auto-fallback 池。"""
    try:
        url = _get_api_base_url().rstrip("/") + "/models"
        key = get_next_api_key()
        r = httpx.get(url, headers={"Authorization": f"Bearer {key}"}, timeout=15)
        data = r.json().get("data", [])
    except Exception as e:
        _logger.warning("discover_free_models: API call failed", extra={"error": str(e)[:160]})
        return []

    free = []
    for m in data:
        pricing = m.get("pricing") or {}
        if pricing.get("prompt") == "0" and pricing.get("completion") == "0":
            ctx = m.get("context_length") or 0
            if ctx >= min_context:
                free.append((m["id"], ctx))
    free.sort(key=lambda x: -x[1])
    return [mid for mid, _ in free[:limit]]


def preflight_models(
    timeout: float = 15.0,
    auto_discover: bool = True,
    discover_probe_limit: int = 4,
) -> dict:
    """Pipeline 起頭 probe 所有配置的 model，失效者從 chain 移除。
    若任一 chain（scoring / generation）全空，且 `auto_discover=True`，
    會查 OpenRouter 免費池補上可用 model。

    回傳 {'scoring': [...], 'generation': [...], 'dead': [...], 'discovered': [...]}。
    """
    global _scoring_chain, _generation_chain
    scoring, generation = _load_default_chains()
    candidates = list(dict.fromkeys(scoring + generation))

    alive: set[str] = set()
    dead: list[tuple[str, str]] = []

    for m in candidates:
        ok, err = _probe_model(m, timeout)
        if ok:
            alive.add(m)
            _logger.info("Preflight OK", extra={"model": m})
        else:
            dead.append((m, err))
            _logger.warning("Preflight failed", extra={"model": m, "error": err[:160]})

    scoring_alive = [m for m in scoring if m in alive]
    generation_alive = [m for m in generation if m in alive]
    discovered: list[str] = []

    # Auto-discover：任一 chain 全空時去 OpenRouter 免費池找替補
    if auto_discover and (not scoring_alive or not generation_alive):
        _logger.info("Auto-discover: chain empty, querying free pool")
        pool = discover_free_models()
        # 排除已 probe 過的 candidates，避免重複 probe
        pool = [m for m in pool if m not in candidates][:discover_probe_limit]
        for m in pool:
            ok, err = _probe_model(m, timeout)
            if ok:
                discovered.append(m)
                _logger.info("Auto-discover: model alive", extra={"model": m})
            else:
                dead.append((m, err))
                _logger.debug("Auto-discover: model dead", extra={"model": m, "error": err[:160]})

        # 把探索到的附在對應 chain 末端（不覆蓋 configured 偏好）
        if not scoring_alive:
            scoring_alive = list(discovered)
        if not generation_alive:
            generation_alive = list(discovered)

    _scoring_chain = scoring_alive
    _generation_chain = generation_alive
    return {
        "scoring": list(_scoring_chain),
        "generation": list(_generation_chain),
        "dead": dead,
        "discovered": discovered,
    }


def llm_chat(
    messages: list[dict],
    model: str | None = None,
    max_tokens: int | None = None,
    temperature: float = 0.7,
    max_retries: int = 2,
    fallback_model: str | None = None,
    is_generation: bool = False,
) -> str:
    """走 OpenRouter 多 model chain。每個 model 嘗試一次，失敗降級。全部失敗回傳 ""。

    - `model` / `fallback_model`：caller 指定偏好；若不在 chain 中則前置插入。
    - `is_generation=True` 使用 generation chain，否則使用 scoring chain。
    """
    cfg = load_config()["llm"]
    max_tokens = max_tokens or cfg.get("max_tokens", 8192)

    chain = list(_get_chain(is_generation))
    # caller 偏好插在最前面（去重）
    for pref in (model, fallback_model):
        if pref and pref not in chain:
            chain.insert(0, pref)

    if not chain:
        _logger.error("llm_chat: empty model chain (preflight 可能全部失敗)")
        return ""

    for m in chain:
        client = get_llm_client()  # key 輪替
        result = _try_model(client, m, messages, max_tokens, temperature, max_retries)
        if result:
            return result
        _logger.warning("Model failed, trying next in chain", extra={"model": m})

    _logger.error("All LLM models failed", extra={"tried": chain})
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
