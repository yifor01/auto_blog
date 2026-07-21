"""Shared utilities: config loading, HTTP client, dedup, LLM calls."""

from __future__ import annotations

import itertools
import json
import os
from datetime import date, datetime
from pathlib import Path
from typing import Callable

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
LISTS_DIR = OUTPUT_DIR / "lists"

for d in [RAW_DIR, SCORED_DIR, FEEDBACK_DIR, HEALTH_DIR, POSTS_DIR, NOTES_DIR, PROMPTS_DIR, DIGESTS_DIR, BLOGS_DIR, LISTS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

load_dotenv(PROJECT_ROOT / ".env")


def load_config() -> dict:
    config_path = PROJECT_ROOT / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)


# ──────────────────────────────────────────────────────────
# 簡體中文 → 繁體中文（台灣正字）轉換
# ──────────────────────────────────────────────────────────

_opencc_converter = None
_opencc_unavailable = False


def to_traditional(text: str) -> str:
    """簡體中文 → 繁體中文（OpenCC s2twp：台灣正字 + 慣用詞轉換）。

    兩個用途：
      - 來源端（Layer A）：量子位 / ChatPaper 等中國 source 的簡體 title/abstract。
      - 生成端（Layer B）：免費 LLM 偶發吐出的簡體字（如 Agnes 的「应」）。

    特性：
      - 對純英文 / 已是繁中 / 空字串為冪等（OpenCC 只映射簡體字形，ASCII/URL/程式碼原樣通過）。
      - OpenCC 未安裝或轉換失敗時，lazy 記 warning 後原樣回傳，絕不中斷 pipeline。
    """
    global _opencc_converter, _opencc_unavailable
    if not text or _opencc_unavailable:
        return text
    if _opencc_converter is None:
        try:
            from opencc import OpenCC

            _opencc_converter = OpenCC("s2twp")
        except Exception as e:
            _opencc_unavailable = True
            _logger.warning(
                "OpenCC unavailable, skipping 簡→繁 conversion",
                extra={"error": str(e)[:160]},
            )
            return text
    try:
        return _opencc_converter.convert(text)
    except Exception as e:
        _logger.debug("to_traditional failed", extra={"error": str(e)[:160]})
        return text


# ──────────────────────────────────────────────────────────
# 多 provider 路由 + 各自多 key 輪替 + 多 model 降級
#
# 同一條 chain 可混用不同 provider 的 model：由 model id 推斷 provider
# （agnes-* → agnes，其餘 → openrouter），各 provider 有獨立的 base_url
# 與 key 池。Agnes（apihub.agnes-ai.com）作為 OpenRouter 免費 model 全掛時的
# 可用性保險，放在 generation chain 末端。
# ──────────────────────────────────────────────────────────

_AGNES_DEFAULT_BASE_URL = "https://apihub.agnes-ai.com/v1"


def _load_keys(prefix: str) -> list[str]:
    """讀取 PREFIX, PREFIX_2 .. PREFIX_9 的 API keys（缺的略過）。"""
    keys: list[str] = []
    for suffix in ["", "_2", "_3", "_4", "_5", "_6", "_7", "_8", "_9"]:
        k = os.getenv(f"{prefix}{suffix}", "")
        if k:
            keys.append(k)
    return keys


_PROVIDER_KEYS: dict[str, list[str]] = {
    "openrouter": _load_keys("OPENROUTER_API_KEY"),
    "agnes": _load_keys("AGNES_API_KEY"),
}

# Lazy 檢查：不在 import 時 raise，讓不需 LLM 的指令（clean / status / list）
# 即使沒設定 API key 也能正常執行；真正呼叫 LLM 時才在 get_next_api_key() raise。
# cycle 元素為 (序號, key) pair：序號 1-based，供 log 記 key#N（key 值絕不入 log）。
_PROVIDER_CYCLES: dict[str, "itertools.cycle | None"] = {
    p: (itertools.cycle(enumerate(ks, 1)) if ks else None) for p, ks in _PROVIDER_KEYS.items()
}
for _p, _ks in _PROVIDER_KEYS.items():
    if _ks:
        _logger.info("API keys loaded", extra={"provider": _p, "key_count": len(_ks)})

# 執行期可被 lazy retire / 緊急 discover 修改的 healthy model chains（None 代表尚未載入）
_scoring_chain: list[str] | None = None
_generation_chain: list[str] | None = None

# 本次 run 已判死的 model：404（下架）或上游池限流（換 key/backoff 無效，唯換 model）。
# 換 model 才有效，故整輪跳過；下次 process 重啟或 reset_model_health() 才復活。
_RETIRED_MODELS: set[str] = set()

# 緊急 auto-discover 防重入 flag（chain 全空時才觸發一次，平常零成本）。
_emergency_discovered = False


def reset_model_health() -> None:
    """清空 retired set + 重設快取 chain + 緊急 discover flag。

    供測試隔離與長駐 process（如 web monitor 跨日 run）復活被 retire 的 model 用。
    """
    global _scoring_chain, _generation_chain, _emergency_discovered
    _RETIRED_MODELS.clear()
    _scoring_chain = None
    _generation_chain = None
    _emergency_discovered = False


def _provider_for_model(model: str | None) -> str:
    """由 model id 推斷 provider。agnes-* 走 Agnes，其餘預設 OpenRouter。"""
    if model and model.startswith("agnes"):
        return "agnes"
    return "openrouter"


def _get_api_base_url(provider: str = "openrouter") -> str:
    if provider == "agnes":
        return os.getenv("AGNES_API_URL") or _AGNES_DEFAULT_BASE_URL
    url = os.getenv("OPENROUTER_API_URL")
    if url:
        return url
    config = load_config()
    return config.get("llm", {}).get("api_url", "https://openrouter.ai/api/v1")


def _next_key_with_index(provider: str = "openrouter") -> tuple[str, int]:
    """Round-robin 取得指定 provider 的下一個 (key, 1-based 序號)。
    無 key 時才 raise（lazy，僅在真正呼叫該 provider 時）。"""
    cycle = _PROVIDER_CYCLES.get(provider)
    if cycle is None:
        env = "OPENROUTER_API_KEY" if provider == "openrouter" else "AGNES_API_KEY"
        raise ValueError(f"No API keys configured for provider '{provider}' (set {env}[_2..9])")
    idx, key = next(cycle)
    return key, idx


def get_next_api_key(provider: str = "openrouter") -> str:
    """Round-robin 取得指定 provider 的下一個 API key。
    無 key 時才 raise（lazy，僅在真正呼叫該 provider 時）。"""
    return _next_key_with_index(provider)[0]


def _client_with_key_index(model: str | None = None) -> tuple[OpenAI, int]:
    """建立輪替 key 的 client，同時回傳該 key 的 1-based 序號（供 log 記 key#N）。"""
    provider = _provider_for_model(model)
    key, idx = _next_key_with_index(provider)
    return OpenAI(api_key=key, base_url=_get_api_base_url(provider)), idx


def get_llm_client(model: str | None = None) -> OpenAI:
    """建立帶有輪替 key 的 OpenAI-compatible client。依 model 推斷 provider，
    選對應 base_url 並輪替該 provider 的 key。model=None 時預設 OpenRouter。"""
    return _client_with_key_index(model)[0]


def _extract_content(resp) -> str:
    msg = resp.choices[0].message
    if msg.content:
        return msg.content
    # reasoning model 在 max_tokens 被推理吃光時 content 為空：
    # DeepSeek R1 放 reasoning_content，OpenRouter（gpt-oss 等）放 reasoning
    reasoning = getattr(msg, "reasoning_content", None) or getattr(msg, "reasoning", None)
    return reasoning or ""


_BACKOFF_BASE_SECONDS = 5
_BACKOFF_CAP_SECONDS = 60


def _status_code_of(exc) -> int | None:
    """防禦式取 HTTP status code：先 openai SDK 的 .status_code，fallback 掃字串；都沒有回 None。"""
    code = getattr(exc, "status_code", None)
    if isinstance(code, int):
        return code
    import re
    m = re.search(r"\b([45]\d\d)\b", str(exc))
    return int(m.group(1)) if m else None


def _upstream_provider(exc) -> str | None:
    """從 openai SDK exception 解析上游 provider 名稱（上游池限流的判別依據）。

    OpenRouter body 約為 {"error": {"code": 429, "metadata": {"provider_name": "Venice",
    "raw": "... temporarily rate-limited upstream ..."}}}；SDK 有時把 error 內層直接當 body。
    任何形狀不符（無 body / 非 dict / 無 metadata / 無 provider_name）一律回 None，絕不 raise。
    """
    try:
        body = getattr(exc, "body", None)
        if not isinstance(body, dict):
            return None
        # SDK 有時把 error 內層直接當 body；有 error dict 就往內鑽，否則就地取
        inner = body.get("error")
        err = inner if isinstance(inner, dict) else body
        meta = err.get("metadata")
        if not isinstance(meta, dict):
            return None
        name = meta.get("provider_name")
        return name if isinstance(name, str) and name else None
    except Exception:
        return None


def _try_model(
    model: str,
    messages: list[dict],
    max_tokens: int,
    temperature: float,
    max_retries: int,
    timeout: float = 60.0,
) -> str | None:
    """單一 model 呼叫（每次 attempt 內建新 client → 429 retry 時輪替 key）。

    429 分兩種（實測確認）：
    - 上游池限流（body 帶 provider_name）：換 key/backoff 均無效，唯一有效動作是換 model，
      故將 model 加入 _RETIRED_MODELS，零重試零 backoff 直接回 None。
    - 我方帳號額度（無 provider_name）：指數退避重試（5s→10s→20s，上限 60s），每次換 key。
    404（model 下架）：加入 _RETIRED_MODELS，回 None。
    timeout / 其他 error / empty content：視為該 model 本次失敗回 None，讓上層走 fallback 鏈。
    key 值絕不入 log，只記序號 key#N。
    """
    for attempt in range(max_retries + 1):
        client, key_idx = _client_with_key_index(model)
        try:
            resp = client.with_options(timeout=timeout).chat.completions.create(
                model=model, messages=messages,
                max_tokens=max_tokens, temperature=temperature,
            )
            content = _extract_content(resp)
            return content or None
        except Exception as e:
            err = str(e)
            status = _status_code_of(e)

            # 404：model 下架 → 本次 run retire，不重試
            if status == 404 or "404" in err:
                _RETIRED_MODELS.add(model)
                _logger.warning(
                    "Model not found, retired for this run",
                    extra={"model": model, "status_code": 404},
                )
                return None

            # 429
            if status == 429 or "429" in err:
                provider_name = _upstream_provider(e)
                if provider_name:
                    # 上游池限流：換 key/backoff 無效 → retire，零重試直接降級下一 model
                    _RETIRED_MODELS.add(model)
                    _logger.warning(
                        "Upstream provider rate-limited, retiring model for this run",
                        extra={"model": model, "status_code": status,
                               "provider_name": provider_name, "key": f"key#{key_idx}"},
                    )
                    return None
                # 我方帳號額度：指數退避重試，下次 attempt 會換新 key
                if attempt < max_retries:
                    wait = min(_BACKOFF_BASE_SECONDS * (2 ** attempt), _BACKOFF_CAP_SECONDS)
                    _logger.warning(
                        "Rate limited (account quota), retrying with next key",
                        extra={"model": model, "wait_seconds": wait,
                               "attempt": attempt + 1, "key": f"key#{key_idx}"},
                    )
                    time.sleep(wait)
                    continue
                _logger.warning(
                    "Rate limited, retries exhausted",
                    extra={"model": model, "status_code": status, "key": f"key#{key_idx}"},
                )
                return None

            # 其他 error（含 timeout）：視為該 model 本次失敗
            _logger.warning(
                "Model call failed",
                extra={"model": model, "status_code": status,
                       "error": err[:200], "key": f"key#{key_idx}"},
            )
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
    # 指令式 prompt 比 "ping" 更能穩定觸發輸出；空內容視為失效，
    # 避免雖在架但回空字串的 model 進 chain 後生成出空白文章（06-05 timeout 教訓）。
    # 健康 model 偶發回空，故對空回應 retry 一次以吸收抖動、避免誤殺。
    # 429 視為 alive（「忙」非「死」）：免費 model 起頭常碰每分鐘限流，
    # 但 runtime 有 4 key 輪替 + request_delay 間隔可吸收，不該整輪移出 chain。
    last_err = "empty content"
    for _attempt in range(2):
        try:
            # provider-aware：Agnes model 用 Agnes endpoint probe，否則 preflight 會
            # 拿 OpenRouter endpoint 去 probe Agnes 而誤判其死亡（fallback 保全關鍵）。
            resp = get_llm_client(model).with_options(timeout=timeout).chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Reply with the single word: OK"}],
                max_tokens=16, temperature=0.0,
            )
            if _extract_content(resp).strip():
                return True, ""
        except Exception as e:
            err = str(e)
            if "429" in err:
                return True, ""
            return False, err[:200]
    return False, last_err


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


_LAST_RESORT_MODEL = "openrouter/free"
"""OpenRouter 官方 meta-model，pricing 0，能力弱但穩定。chain 全空時的最後保底。"""


def preflight_models(
    timeout: float = 15.0,
    auto_discover: bool = True,
    discover_probe_limit: int = 4,
) -> dict:
    """Pipeline 起頭 probe 所有配置的 model，失效者從 chain 移除。
    若任一 chain（scoring / generation）全空，且 `auto_discover=True`，
    依序嘗試補救：
      1. 查 OpenRouter 免費池（`discover_free_models`）找替補
      2. 若仍空，加上 `openrouter/free` meta-model 保底（慢但穩定）

    回傳 {'scoring': [...], 'generation': [...], 'dead': [...],
           'discovered': [...], 'last_resort': bool}。
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

    # Last resort：仍然空 → 試 openrouter/free meta-model（保底）
    last_resort = False
    if auto_discover and (not scoring_alive or not generation_alive):
        _logger.info("Last resort: probing openrouter/free meta-model")
        ok, err = _probe_model(_LAST_RESORT_MODEL, timeout)
        if ok:
            last_resort = True
            _logger.info("Last resort: openrouter/free alive")
            if not scoring_alive:
                scoring_alive = [_LAST_RESORT_MODEL]
            if not generation_alive:
                generation_alive = [_LAST_RESORT_MODEL]
        else:
            dead.append((_LAST_RESORT_MODEL, err))
            _logger.error("Last resort dead — pipeline 無可用 model", extra={"error": err[:160]})

    _scoring_chain = scoring_alive
    _generation_chain = generation_alive
    return {
        "scoring": list(_scoring_chain),
        "generation": list(_generation_chain),
        "dead": dead,
        "discovered": discovered,
        "last_resort": last_resort,
    }


def _emergency_discover(is_generation: bool) -> list[str]:
    """chain 全空（全部 retired 或 config 空）時的一次性自救。

    保留原 preflight 的「全滅時自救」能力，但平常零成本（只在 chain 空且尚未觸發過時跑）：
    查 OpenRouter 免費池、排除 retired、最多 probe 3 個，活的接到快取 chain 供本次及後續呼叫用。
    module 級 flag 確保整個 process 只觸發一次，避免每次 llm_chat 都白燒 discover/probe 請求。
    """
    global _emergency_discovered, _scoring_chain, _generation_chain
    if _emergency_discovered:
        return []
    _emergency_discovered = True
    _logger.warning("llm_chat: chain empty, 觸發緊急 auto-discover")

    pool = [m for m in discover_free_models() if m not in _RETIRED_MODELS]
    alive: list[str] = []
    for m in pool[:3]:
        ok, _err = _probe_model(m)
        if ok:
            alive.append(m)

    if alive:
        # 接到兩條快取 chain（此時原 chain 已空，不存在覆蓋偏好問題）
        _scoring_chain = list(dict.fromkeys((_scoring_chain or []) + alive))
        _generation_chain = list(dict.fromkeys((_generation_chain or []) + alive))
        _logger.info("緊急 auto-discover 成功", extra={"discovered": alive})
    return alive


def llm_chat(
    messages: list[dict],
    model: str | None = None,
    max_tokens: int | None = None,
    temperature: float = 0.7,
    max_retries: int = 2,
    fallback_model: str | None = None,
    is_generation: bool = False,
    timeout: float | None = None,
    validate: Callable[[str], bool] | None = None,
) -> str:
    """走多 model chain。每個 model 嘗試一次，失敗降級。全部失敗回傳 ""。

    - `model` / `fallback_model`：caller 指定偏好；若不在 chain 中則前置插入。
    - `is_generation=True` 使用 generation chain，否則使用 scoring chain。
    - `timeout`：單次 LLM 呼叫逾時秒數；None 時讀 config `llm.timeout_seconds`（預設 60）。
    - `validate`：model 回了內容但 validate(content) 為 False 時視為該 model 本次輸出爛，
      記 warning 並降級下一 model（**不** retire——model 活著只是這次輸出爛）。
    - 本次 run 已 retire 的 model（404 / 上游 429）自動從 chain 過濾。
    """
    cfg = load_config()["llm"]
    max_tokens = max_tokens or cfg.get("max_tokens", 8192)
    if timeout is None:
        timeout = cfg.get("timeout_seconds", 60)

    chain = list(_get_chain(is_generation))
    # caller 偏好插在最前面（去重）
    for pref in (model, fallback_model):
        if pref and pref not in chain:
            chain.insert(0, pref)

    # 過濾本次 run 已 retire 的 model（含 caller 前置插入的偏好）
    chain = [m for m in chain if m not in _RETIRED_MODELS]

    # 緊急補救：過濾後全空（全部 retired 或 config 空）→ 一次性 auto-discover
    if not chain:
        chain = _emergency_discover(is_generation)

    if not chain:
        _logger.error("llm_chat: empty model chain (全部 retired 或 config 空, auto-discover 亦無補救)")
        return ""

    for m in chain:
        result = _try_model(m, messages, max_tokens, temperature, max_retries, timeout)
        if result is None:
            _logger.warning("Model failed, trying next in chain", extra={"model": m})
            continue
        if validate is not None and not validate(result):
            _logger.warning("Response failed validation, falling through", extra={"model": m})
            continue
        return result

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
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        # corrupt / 寫到一半 / merge conflict 殘留的 JSON 不該炸掉該日期的所有後續 run。
        # 記 error 並當作「無資料」處理（caller 多半會重新收集/評分）。
        _logger.error("load_json failed, treating as empty", extra={"path": str(path), "error": str(e)})
        return []


_TRACKING_PARAM_KEYS = {"fbclid", "gclid", "msclkid", "ref"}


def normalize_url(url: str) -> str:
    """URL 正規化，用於跨來源 / 跨日去重比對。

    - scheme 統一 https（http/空 → https）
    - netloc 小寫並去掉 `www.` 前綴
    - path 去尾部 `/`
    - 移除追蹤參數（utm_*、fbclid、gclid、msclkid、ref）
    - 其餘 query 參數按 key 排序，確保順序不影響 key
    - 移除 fragment（#anchor 為前端錨點，不影響內容）

    無法解析（空字串等）時原樣回傳。
    """
    if not url:
        return url
    from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

    try:
        parts = urlsplit(url.strip())
    except ValueError:
        return url

    scheme = "https" if parts.scheme in ("", "http", "https") else parts.scheme
    netloc = parts.netloc.lower()
    if netloc.startswith("www."):
        netloc = netloc[4:]
    path = parts.path.rstrip("/")

    kept = [
        (k, v)
        for k, v in parse_qsl(parts.query, keep_blank_values=True)
        if not k.lower().startswith("utm_") and k.lower() not in _TRACKING_PARAM_KEYS
    ]
    kept.sort(key=lambda kv: kv[0])
    query = urlencode(kept)

    return urlunsplit((scheme, netloc, path, query, ""))


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
                        # 與 ContentItem.dedup_key() 一致：兩側都經 normalize_url，
                        # 否則歷史 raw JSON 的舊 URL key 會比不到當天正規化後的 key。
                        seen.add(normalize_url(url))
                    arxiv_id = item.get("raw_metadata", {}).get("arxiv_id", "")
                    if arxiv_id:
                        seen.add(f"arxiv:{arxiv_id}")
        except Exception:
            continue
    return seen


def slugify(text: str, max_len: int = 60) -> str:
    """將標題轉為檔名安全的 slug。

    - 所有非單字字元（`/`、`.`、空白、標點等）一律轉成分隔符 `-`，
      避免 `memvid/memvid` 被直接刪成 `memvidmemvid` 這種黏字 bug。
    - 連續 `-` 折疊成單一，並 strip 頭尾。
    - 截斷 `max_len` 後若切在單字中間，退回最後一個完整單字，
      避免 `...world-modeli` 這種殘字。
    - 全特殊字元 / 空輸入回傳 fallback `untitled`。
    - 保留 unicode 單字字元（如中文），維持既有行為。
    """
    import re

    s = text.lower()
    # 非單字字元（含 / . 空白 標點）→ 分隔符；保留 \w（含 unicode 中文與底線）
    s = re.sub(r"[^\w]+", "-", s, flags=re.UNICODE)
    # \w 含底線，依慣例底線視為分隔符
    s = s.replace("_", "-")
    # 折疊連續 dash + 去頭尾
    s = re.sub(r"-{2,}", "-", s).strip("-")

    if not s:
        return "untitled"
    if len(s) <= max_len:
        return s

    truncated = s[:max_len]
    # 若切點仍在單字中間（下一字元非分隔符且當前結尾非分隔符），退回最後一個完整單字
    if s[max_len] != "-" and not truncated.endswith("-") and "-" in truncated:
        truncated = truncated.rsplit("-", 1)[0]
    return truncated.strip("-") or "untitled"


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
