"""normalize_url_light() 與去重用 normalize_url() 的分界測試。

**跨語言契約（與 `web/src/enrich.ts` 的 `normalizeUrl` 逐條對照，含已知分歧）
已移到 `tests/test_cross_lang_contract.py`**：期望值統一放在共用 fixture
`web/src/__fixtures__/cross-lang-contract.json`，TS 側讀同一份。
期望值只留一份，才不會出現「Python 測試綠、TS 測試也綠、兩端行為卻不同」——
原本這裡與 TS 端各寫一份期望值，正是那個漏洞。

本檔剩下的職責是另一件事：釘住 `normalize_url_light()` 與 `normalize_url()`
**不是重複實作**。兩者用途不同（同源對照 vs 跨來源去重），
有人圖精簡把它們合併掉時，這裡會 FAIL。
"""

from __future__ import annotations

import pytest

from src.utils import normalize_url, normalize_url_light


class TestDistinctFromNormalizeUrl:
    """釘住「兩支不是重複實作」——有人合併掉就會 FAIL。

    把 normalize_url_light 換成 normalize_url，以下每一筆都會 FAIL。
    """

    @pytest.mark.parametrize(
        "raw",
        [
            "https://www.example.com/a",           # normalize_url 會拿掉 www.
            "https://Example.COM/a",               # normalize_url 會轉小寫
            "https://example.com/a?b=2&a=1",       # normalize_url 會排序 query
            "https://example.com/a?utm_source=x",  # normalize_url 會移除追蹤參數
            "https://example.com/a#sec",           # normalize_url 會移除 fragment
        ],
    )
    def test_light_preserves_what_dedup_version_strips(self, raw):
        assert normalize_url_light(raw) == raw
        assert normalize_url(raw) != raw
