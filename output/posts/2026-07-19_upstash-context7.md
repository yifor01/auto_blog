---
title: upstash/context7
source: GitHub Trending
url: https://github.com/upstash/context7
score: 76
model: tencent/hy3:free
generated_at: '2026-07-19T08:06:47.700250'
---

📌 【upstash 開源】Context7：把最新程式庫檔案直接餵進 LLM 提示

TL;DR：Context7 從原始來源擷取版本特定的檔案與範例，解決 LLM 產生過時或幻覺 API 的問題。

你用的 LLM 是不是常給出一年前的程式碼範例，甚至呼叫根本不存在的 API？當套件版本迭代，模型訓練資料卻停留在舊時代，這種落差正是開發者的日常痛點。

🤔 **沒有 Context7，LLM 依賴過時或泛用資訊**

README 指出，若不使用 Context7，LLM 在處理你使用的程式庫時容易出現三類問題：
- 程式碼範例過時，基於一年以上的訓練資料
- 幻覺出根本不存在的 API
- 針對舊版套件給出泛用回答

🧩 **Context7 直接從來源拉取版本特定檔案**

Context7 的設計理念是從原始來源拉取最新的、版本特定的檔案與程式碼範例，並直接放進你的 prompt 中。README 展示的實際情境包括：建立 Next.js middleware 檢查 JWT 並導向登入頁、設定 Cloudflare Worker 快取 JSON API 回應五分鐘、查詢 Supabase 的 email/password 註冊 auth API——這些都透過 `use context7` 觸發，將最新範例與檔案送進 LLM 上下文，免去切換分頁與猜測 API。

它提供兩種運作模式：
- CLI + Skills：安裝 skill 引導 agent 用 `ctx7` CLI 指令抓取檔案，不需 MCP
- MCP：註冊 Context7 MCP server，讓 agent 原生呼叫檔案工具

🎯 **實務啟示**

對工程師來說，Context7 可用單一指令接入編碼 agent，降低「檔案幻覺」的維修成本。若你常踩到套件升級後 LLM 給舊語法的坑，可優先試 CLI 模式：`npx ctx7 setup`（需 Node.js 18+）會經 OAuth 認證、產生 API key 並安裝對應 skill，也能選 MCP 模式。

🔗 **來源**
- 標題：upstash/context7
- 作者／機構：upstash
- 連結：https://github.com/upstash/context7

#Context7 #upstash #LLM #Documentation #MCP #CLI #CodeGeneration #Hallucination #DeveloperTools #Nextjs
