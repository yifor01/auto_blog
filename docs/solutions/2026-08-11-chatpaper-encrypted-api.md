# ChatPaper API 改吐加密 binary — 靜默斷線 78 天的排查與逆向

**日期**：2026-08-11
**相關 commit**：`ddf3a3a`
**同類前例**：`2026-07-31-silent-collector-failures.md`（newsapi / blog collector）

## 問題

ChatPaper collector 每天 4 個 category 全回 0 筆，pipeline 照常綠燈、無告警。最後一次有資料是 **2026-05-25（105 筆）**，發現時已斷 **78 天**。

## Root cause

API 在 2026-05-26 後改成加密回應：

```
HTTP/2 200
content-type: application/binary-json
x-binary-key: eLhWHiyYs2ShyvoNwKU9KJdw9RRDHkroHycxbH/74Z8=
（body 為亂碼）
```

HTTP 仍是 **200**、`raise_for_status()` 過關，只有 `resp.json()` 會炸——而那行包在 per-category 的 `try/except` 裡，只寫一行 log 就繼續跑下一個 category。**「HTTP 200 + 例外被吞」= 靜默歸零**，與 newsapi 那次的「HTTP 200 + `totalResults: 0`」是同一類失敗。

## 解法

**不要猜演算法。** 一開始對 48 bytes 密文枚舉 AES-CBC/ECB/GCM 與各種 IV 假設是浪費——前端 bundle 裡就有原始碼：

1. `curl -D` 看真實 response headers，拿到 `x-binary-key` 這個線索
2. 抓首頁列出的 Nuxt chunk（`cdn.pdppt.com/chatpaper/_nuxt/*.js`），`grep x-binary-key` → 命中 `Bygw52PF.js` 的 class `fu`

演算法（兩層共用同一個解密函式）：

```
x-binary-key --base64--> 用寫死的 master key(858d8c50f67f501dac332703000ae4ce) 解 --> session key 字串
response body --用 session key 解--> JSON
```

單層 = **AES-128-CBC**：

- key = 金鑰字串**前 16 字元**的 UTF-8 bytes，右補 `\x00` 到 16 的倍數
- iv = 金鑰字串**反轉後**前 16 字元，同樣補齊
- 解出的明文：**首 byte 是尾端 zero-padding 長度的 16 進位單字元**，去頭去尾後 `zlib.decompress`

實作見 `src/collectors/chatpaper_collector.py` 的 `parse_response()`。**沒有 `x-binary-key` header 就照舊當純 JSON**——前端自己就是這樣分支，API 改回明文不會壞。

## 可複用 pattern

1. **診斷順序**：`curl -D` 看真實 headers/body 前幾個 byte → 前端 bundle grep header 名字 → 才是讀自己的程式碼。從自己的程式碼讀起會一路合理化「大概是限流吧」。
2. **加密協定的權威來源是前端 bundle**，不是猜測或試誤。SPA 一定要在瀏覽器端解密，金鑰與演算法必然在 JS 裡。
3. **加密回應的測試要用真實抓下來的密文當 golden sample**。round-trip（自己加密再解開）會讓 key/iv 推導、padding 規則、壓縮格式全寫錯還是綠——那只驗證了「我的加密和我的解密一致」。
4. **collector 的 per-item/per-category `except` 是靜默失敗溫床**：只 log 不計數，連續 0 筆沒人看得見。這是第二次踩到，「連續 N 天 0 筆告警」已列入 status.md 的 Next Steps。

## 驗證

- 實跑 `ChatPaperCollector().collect(date(2026,8,10))` 打真實 API → **101 筆**（斷線前同級數），欄位映射全對
- 08-11 / 08-04 / 05-25 三天另測，皆解出完整 JSON，schema 與斷線前一致
- `pytest tests/` 1040 → **1043 passed**

## 未做

- 2026-05-26 ~ 08-10 共 78 天的缺漏**未回補**（待決定，會吃 LLM 評分額度）
