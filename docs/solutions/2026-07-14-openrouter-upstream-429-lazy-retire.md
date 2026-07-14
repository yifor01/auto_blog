# OpenRouter 上游 429 與正交 fallback（lazy retire 重構）

Date: 2026-07-14
來源：econ-news-daily 7/13 CI 事故盤點（commit 9a48890 同構修法），本專案實測確認後移植。

## 問題

1. 兩條 LLM chain 前兩順位全死：`openai/gpt-oss-120b:free` 已下架（404）、`google/gemma-4-31b-it:free` 被 Google AI Studio 上游池限流（429）。每次呼叫先撞完 404+429 才降到 nemotron，每 item 白燒 2+ 次請求。
2. scorer parse retry 重打整條 chain：最壞 3 parse × 3 model × 3 retry = 27 次請求/item；OpenRouter 免費日額度為**帳號級 50 次/天**（未儲值），兩個 item 就燒光。
3. 起頭 preflight probe 每天固定燒 5-7 次請求。

## Root Cause

OpenRouter `:free` model 的 429 有兩種，舊程式碼混為一談：

- **上游 provider 池限流**（body 帶 `error.metadata.provider_name`）：`:free` 由上游池（Venice/Novita/Google AI Studio/Nvidia/Darkbloom）供應、全體免費用戶共用。這是 provider 層級拒絕——**換 key 無效**（不是我方 quota）、**backoff 無效**（分鐘級限流），唯一有效動作是換掛在不同上游的 model。
- **我方帳號額度**（無 provider_name）：backoff 有意義；但額度綁帳號不綁 key，多 key 同帳號放大不了。

舊 chain 的 fallback 彼此又可能共用上游 → 「共用上游的 fallback 不是 fallback」。

## 解法

1. **429 分流**（`src/utils.py`）：`_upstream_provider()` 防禦式解析 body；上游 429 / 404 → 記入 process 級 `_RETIRED_MODELS`、零重試直接換 model（一個死 model 整個 run 只花 1 次確認）；我方 429 → 指數退避且每次 retry 換 key。附 `reset_model_health()`。
2. **Provider 正交 chain**（`config.yaml`）：scoring gpt-oss-20b(Darkbloom)→gemma-4-26b(Google)→nemotron(Nvidia)；generation hy3(Novita)→gemma-4-26b→nemotron→agnes。注意 `:free` 的上游不在 models API 裡，只有 429 body 看得到，對照表靠實打建。
3. **移除 preflight probe**：lazy retire 零成本達到同效果；chain 全滅時 `llm_chat` 內一次性緊急 auto-discover 自救（原保底能力不丟）。
4. **`llm_chat(validate=...)`**：model 吐爛 JSON 原地降級下一個 model、**不 retire**（三態：死/忙/活著但這次輸出爛）；scorer 最壞 27 → ~6 次請求。
5. **Log 補齊**：model / status_code / provider_name / `key#N`（key 值絕不入 log）。

額外坑（e2e 驗證新發現）：gpt-oss 系是 reasoning model，推理 token 也算進 `max_tokens`，偏小時 content 為空且**無 exception**（靜默失敗）；OpenRouter 把推理放 `message.reasoning`（非 DeepSeek 的 `reasoning_content`）。修法：scorer max_tokens 500→1200、`_extract_content` 增援該欄位。

## 可複用 Pattern

- **fallback 的維度必須與失敗的維度正交**：key 輪替只治 per-key 額度、model fallback 只治下架、換上游才治池限流——維度錯配的重試是笛卡爾積式白燒。
- **先分辨失敗類型再選對策**：對「不可恢復失敗」（404、上游限流）重試 = 白燒；lazy retire（首撞即整輪跳過）比 preflight（預防性全 probe）便宜且效果相同。
- **meta-router（openrouter/free）只配當最後保底**：解決可用性但犧牲品質選擇權與評分尺度一致性。

## 驗證

383→399 tests；真實 API e2e：scoring 首位直出有效 JSON 五維分、generation 由 hy3 回正常繁中。CI 驗證見 2026-07-15 daily-pipeline。
