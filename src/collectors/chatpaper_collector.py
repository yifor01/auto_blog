"""ChatPaper API collector."""

from __future__ import annotations

import base64
import json
import zlib
from datetime import date
from typing import Any

from Crypto.Cipher import AES

from src.collectors.base import BaseCollector
from src.models import ContentItem, SourceType
from src.logger import get_logger
from src.utils import (
    date_to_chatpaper_ts,
    get_http_client,
    load_config,
)

_logger = get_logger("collectors.chatpaper")

# ChatPaper 在 2026-05-26 之後把 API 回應改成加密 binary（`content-type:
# application/binary-json`），`resp.json()` 直接炸並被 collector 的 except 吞掉 →
# 靜默 0 筆 78 天。以下演算法逆向自前端 bundle（`_nuxt/Bygw52PF.js` 的 class `fu`）：
#   1. `x-binary-key` header → base64 decode → 用寫死的 master key 解 → session key 字串
#   2. response body → 用 session key 解
# 兩層用同一個解密函式。**沒有 header 就照舊當純 JSON 讀**（前端也是這樣分支），
# 所以 API 哪天改回明文不會壞。
_MASTER_KEY = "858d8c50f67f501dac332703000ae4ce"


def _aes_key(s: str) -> bytes:
    """金鑰字串 → AES key bytes：取 UTF-8 bytes，右補 `\\x00` 到 16 的倍數。"""
    b = s.encode("utf-8")
    return b.ljust(-(-len(b) // 16) * 16, b"\x00")


def _decrypt(key: str, payload: bytes) -> bytes:
    """AES-128-CBC 解密 + 去 padding + zlib 解壓。

    key 與 iv 都由同一個字串推導：key 取前 16 字元，iv 取「字串反轉後」的前 16 字元。
    明文的第一個 byte 是 padding 長度的 16 進位單字元（尾端補了幾個 `\\x00`）。
    """
    cipher = AES.new(_aes_key(key[:16]), AES.MODE_CBC, _aes_key(key[::-1][:16]))
    plain = cipher.decrypt(payload)
    pad = int(chr(plain[0]), 16)
    return zlib.decompress(plain[1 : len(plain) - pad])


def parse_response(resp: Any) -> dict:
    """讀取 API 回應：有 `x-binary-key` 就解密，否則當純 JSON。"""
    header_key = resp.headers.get("x-binary-key")
    if not header_key:
        return resp.json()
    session_key = _decrypt(_MASTER_KEY, base64.b64decode(header_key)).decode("utf-8")
    return json.loads(_decrypt(session_key, resp.content))


class ChatPaperCollector(BaseCollector):
    name = "chatpaper"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config["collectors"]["chatpaper"]
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        ts = date_to_chatpaper_ts(target_date)
        base_url = cfg["base_url"]
        page_size = cfg.get("page_size", 30)
        categories = cfg.get("categories", [{"id": 2, "name": "AI"}])

        all_items: list[ContentItem] = []
        seen_ids: set[str] = set()

        client = get_http_client()
        try:
            for cat in categories:
                cat_id = cat["id"]
                cat_name = cat["name"]
                try:
                    url = f"{base_url}?page=1&page_size={page_size}&category_id={cat_id}&language=english&date={ts}"
                    resp = client.get(url)
                    resp.raise_for_status()
                    data = parse_response(resp)

                    for article in data.get("items", []):
                        source_id = article.get("source_id", "")
                        if source_id in seen_ids:
                            continue
                        seen_ids.add(source_id)

                        all_items.append(
                            ContentItem(
                                source=SourceType.CHATPAPER,
                                source_name=f"ChatPaper/{cat_name}",
                                title=article.get("title", ""),
                                url=article.get("article_url", ""),
                                authors=article.get("authors", []),
                                abstract=article.get("abstract", ""),
                                published_date=target_date,
                                tags=[
                                    c.get("tag", "")
                                    for c in article.get("category_list", [])
                                ],
                                organization=article.get("organization", ""),
                                raw_metadata={
                                    "arxiv_id": source_id,
                                    "pdf_url": article.get("pdf_url", ""),
                                    "chatpaper_id": article.get("id"),
                                    "source_type": article.get("source_type", ""),
                                },
                            )
                        )

                    _logger.info("ChatPaper category complete", extra={"category": cat_name, "count": len(data.get("items", []))})
                except Exception as e:
                    _logger.error("ChatPaper category error", extra={"category": cat_name, "error": str(e)})
        finally:
            client.close()

        _logger.info("ChatPaper collection complete", extra={"count": len(all_items)})
        return all_items
