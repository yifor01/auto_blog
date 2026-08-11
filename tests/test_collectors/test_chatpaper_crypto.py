"""ChatPaper 加密回應（`application/binary-json`）的解密。

golden sample 是 2026-08-11 從真實 API 抓的一頁（`page_size=1`, `category_id=91`,
`date=1786291200`）原始密文，**不是自己加密再解開的 round-trip**——目的就是釘住
「伺服器實際吐出來的格式」，演算法（AES key/iv 推導、首 byte padding、zlib）任一環
寫錯都會紅。金鑰是 header 原文，非機密（每個瀏覽器訪客都拿得到同一把）。
"""
from __future__ import annotations

import base64
import json
from unittest.mock import MagicMock

from src.collectors.chatpaper_collector import parse_response

_GOLDEN_KEY = "eLhWHiyYs2ShyvoNwKU9KJdw9RRDHkroHycxbH/74Z8="
_GOLDEN_BODY = (
    "VYVHcP7Du2XzfSvulE7A4u2NquIa+saw+BZ4NfAyqV16zJ7XfIk7RPkxJgcWE1b53akbgZcz1ZPkadDOZXYYDLGD"
    "+6JFyxYSqKLC2Pcer0k0xQm2hRbjh1CC+G9jSHCvEJf961ea/DTbjjNaygRjOA5YP370EGd1jU0XPFLMCr1ujOVO"
    "LBB4SY2l2kHhpZJZTsUEfhw9E3EN3vUMSeRqCu5IMhK5quGiU/ogZGUc7QWzra0kpfGOKyFJj8tZH+3VFcyYh5tn"
    "JAOCOkm3q9cFyrH3LoRfAAMTjlNrLvKznMfeN5UR7N8SJmZN3TaoToXB5TTSApTueOXSjAbp2Na/Nl4YtBFzY5m7"
    "ESzW5uGfHB8pkyLzQJkPXEJ9cgjilYf1i70RXh4RPVNp6yHuQOjFUXT8sgI1//WtxTJQcaoE9IsmJP7Mz+H/4qtn"
    "h67udUaFMVkwsZdIZtIjo11I1cWjkjzGgx0vo7PoZaA4cTbPvIO0pllHjn42P6wpJXW8iRT9xkDuTIu9/eNyKyAX"
    "MrUcHZJFbsIL7+751mk+KEc8c3G0VqdmvxnaVzWZAIdyC00y2GNQD5OsWNntT90Jdy6TAWUt0xhYI8hpu8VP4Kx2"
    "Z7NAhtAh9pghenVo7HobXc/pAu2z+ZXMebi3ev1N7NCcc2eBk7OlU9bb6NzACiOvKjlqGjAWbM95BTKIbWzWOyrc"
    "5dyNzWiKqZex7xMH2BASRUJZMo+lJJizkShxDzJLCLVuDZXeM0mNgm92RtPDQNIaYngyO96sQ6dPaPZW+5HL4NQD"
    "TRNYzQJqOxDjLadjkMozRPwpeEQhUBo1z3L+xsMMogV/iN7d7Apt5sSUAI+k+6xwYuon8KqrupEPmeg07PGnxy5J"
    "9FBrzYEiZ0TjCwfBJ41ZsB3UKmsWaZLUffwWffhgmoB5EY/XeebSbSyq+gO/DqdorFRJHnjrh6tAP5S1JNFhqI96"
    "f4ca+i6J6N15YUsdh+nY4NX4yz68bXu96rmw1+B6Xyz+wczFjWw+tTT3tiIZGCGtOeZ9g6QYC9JgUTiMFiG0A074"
    "O+RTDCZGeAf1IzNXSgE7XOAKuU3mJfOPu2rppPzk9Y3qK/D0/muMWtbhKAvNloMN0dOJQzYk5PkFYw+My5jOYSr6"
    "y4kp0a08MJWq8/AAcOfF1NZ2LyuAPivgAgydLqxD9d2kz3ChXdmAv5BTqnF1Uces+wJdxoNlauMvJTd/6yC26UTQ"
    "cfjBHEaYR78SykMHKe4GaPRhTT1m5hbcrURWnn5ClRW3JAwQmmlxl2wPuRB67vphs0jXk5yUZrC8LP3iPqx7G+wD"
    "OPuQ2uqEfs2O8BzJuHjQvHtVy44E4qDU1Q5XumK94z1h5qOTY+bKcVMO6yNeURBWw1RPi7pQPGcCScKnI4NgFjEJ"
    "Wi3j/hck81joaSPyi3Rim8LHB4muMSziT8fDVI1IdOz6tO88Jex1f+ZurpBppTuA9iFVC3lmK+ayGFzzag+M3ET2"
    "xLl4sUxjOgTBYgcmUhqF8WD4YxPVkBXtDv7WDgCAE29GB2Ts6v0kEI9CfXSoSmLm1VakV7tyUzBH30iA2nsNQDfL"
    "hiO+o5x1XEHVFuwO"
)


def _encrypted_resp() -> MagicMock:
    r = MagicMock()
    r.headers = {"x-binary-key": _GOLDEN_KEY}
    r.content = base64.b64decode(_GOLDEN_BODY)
    return r


def test_parse_response_decrypts_binary_json():
    data = parse_response(_encrypted_resp())
    assert data["total"] == 16
    assert len(data["items"]) == 1
    item = data["items"][0]
    assert item["source_id"] == "2608.07152"
    assert item["title"] == "Exact Adaptive Hybrid Retrieval Without Fixed Top-L Cutoffs"
    assert item["abstract"].startswith("Modern retrieval-augmented generation")


def test_parse_response_falls_back_to_plain_json():
    """API 若改回明文（無 `x-binary-key`）就照舊走 resp.json()。"""
    r = MagicMock()
    r.headers = {}
    r.json.return_value = {"items": [{"title": "plain"}]}

    assert parse_response(r) == {"items": [{"title": "plain"}]}
    r.json.assert_called_once()


def test_encrypted_payload_is_not_plain_json():
    """密文本身不是 JSON——確認 golden sample 真的是加密的，測試沒有空轉。"""
    try:
        json.loads(base64.b64decode(_GOLDEN_BODY))
    except (ValueError, UnicodeDecodeError):
        return
    raise AssertionError("golden sample 應該是密文")
