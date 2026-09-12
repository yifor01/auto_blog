---
title: 'Litelm: LiteLLM Without the Bloat'
source: Hacker News
url: https://github.com/kennethwolters/litelm
model: claude-code/sonnet
generated_at: '2026-09-12T19:34:52.879947'
score: 70
---

📌 litelm：把 LiteLLM 瘦身到 2,900 行程式碼

TL;DR：litelm 只保留 LiteLLM 的路由與格式轉換核心，用 2,900 行、2 個依賴取代 10 萬行的完整套件。

如果你只是想呼叫不同家的 LLM API、順便處理一下訊息格式轉換，卻要為此安裝一個內建代理伺服器、快取層與成本追蹤的十萬行套件，這聽起來是不是有點本末倒置？

🤔 **要解決的問題：LiteLLM 太重了**

litelm 的開發者指出，LiteLLM 的路由（routing）與格式轉換（translation）這個核心功能，被埋在超過 10 萬行程式碼之下，裡面包含 proxy 伺服器、快取層、成本追蹤等大多數使用者根本用不到的功能。litelm 的做法是把「呼叫路徑」單獨抽出來，也就是 model routing、訊息格式轉換、streaming、tool use、embeddings，其餘一律不做：沒有 Router class、沒有 proxy、沒有快取。

🧩 **設計理念：API 完全比照 LiteLLM，換套件只需要改 import**

litelm 的核心賣點是 API 與 LiteLLM 幾乎一致，函式名稱、參數、回傳型別都相同，如果現在用的是 litellm，理論上只要把 import 裡的 `litellm` 換成 `litelm` 就能切換。每個函式也都提供 async 版本，例如 `acompletion`、`aembedding`、`aresponses`、`atext_completion`。

安裝方式依需求分層：

```
pip install litelm              # openai + httpx
pip install litelm[anthropic]   # + anthropic SDK
pip install litelm[bedrock]     # + boto3
pip install litelm[all]         # everything
```

基本用法：

```python
import litelm

response = litelm.completion(
    "openai/gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)

# Streaming
for chunk in litelm.completion(
    "groq/llama-3.1-70b-versatile",
    messages=[...],
    stream=True
):
    print(chunk.choices[0].delta.content or "", end="")
```

路由語法採 `provider/model-name`，README 列出 19 個支援的 provider，包括 OpenAI、Anthropic、Groq、Mistral、xAI、OpenRouter、Azure、Bedrock、Cloudflare、Together、Fireworks、DeepSeek、Perplexity、DeepInfra、Gemini、Cohere，以及 Ollama、vLLM、LM Studio 這類本地或 OpenAI 相容端點，只要傳入 `api_base` 就能連。錯誤處理則統一映射成 litelm 自己的例外階層，例如 `ContextWindowExceededError`、`RateLimitError`、`AuthenticationError`，方便寫重試或降級邏輯。

📊 **功能取捨一覽**

| 功能 | litellm | litelm |
|---|---|---|
| Model routing | ✓ | ✓ |
| 訊息格式轉換 | ✓ | ✓ |
| Streaming | ✓ | ✓ |
| Tool use | ✓ | ✓ |
| Embeddings | ✓ | ✓ |
| OpenAI Responses API | ✓ | ✓ |
| Router（負載平衡、fallback）| ✓ | ✗ |
| Proxy 伺服器 | ✓ | ✗ |
| 快取／預算／成本追蹤 | ✓ | ✗ |
| Token 計數 | ✓ | ✗ |
| 圖像生成、音訊、OCR、fine-tuning | ✓ | ✗ |
| Agents、guardrails、scheduler | ✓ | ✗ |

README 特別註明開發透明度：程式碼主要由 Claude Code（搭配 Claude Opus 4.6/4.7）協助撰寫，2026 年 5 月 14 日之後的程式碼則透過 Pi 搭配 GPT-5.5 完成，相容性宣稱是依據測試與維護者審查，而非以 AI 撰寫作為保證。維護者也附上針對上游 LiteLLM 特定 commit 範圍（649eb2d 到 9a715df2）的審計說明：檢視了 360 個核心路徑 commit，本地範圍測試 262 個通過、55 個跳過，45 個 provider 即時測試與 10 個 DSPy smoke test 皆通過，但聲明僅涵蓋 litelm 自己宣稱的 routing/formatting/DSPy 範圍，不代表與 LiteLLM 完全相容。

⚠️ **限制**

專案目前狀態為 Alpha，README 列出的功能取捨相當明確，凡是需要 Router 負載平衡、內建 proxy、成本追蹤或圖像／音訊等多模態能力的場景，litelm 都主動排除在外，需要這些功能的使用者仍得留在 LiteLLM。

🎯 **實務啟示**

如果你的專案只需要「呼叫多家 LLM、統一格式、順便處理 streaming 與 tool calling」，不需要 LiteLLM 的 proxy 與治理功能，litelm 提供了一個依賴更少、程式碼量小很多的替代方案，遷移成本理論上也低，因為 API 是刻意對齊的；但目前仍是 Alpha 階段，導入正式環境前建議先跑過自己會用到的路徑測試。

🔗 **來源**
- 標題：Litelm: LiteLLM Without the Bloat
- 作者／機構：kennethwolters, Hacker News
- 連結：https://github.com/kennethwolters/litelm

#LiteLLM #LLMRouting #OpenSource #Python #APIWrapper #DeveloperTools #LLMOps #SoftwareEngineering #AIInfrastructure #GitHub
