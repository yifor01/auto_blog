---
title: Elsewhere
source: Simon Willison
url: https://simonwillison.net/elsewhere/
model: claude-code/sonnet
generated_at: '2026-08-31T12:16:18.796388'
score: 23
---

📌 SDK 大改版連鎖反應：Simon Willison 週報看見的 LLM 工具鏈真實面貌

TL;DR：Anthropic 與 OpenAI 同步換底層 HTTP 函式庫，牽動整條 LLM 工具鏈跟著改版。

一個底層 HTTP 函式庫的替換，竟然讓下游一整批工具同時斷裂——這正是最近 LLM 生態圈的縮影。Simon Willison 在部落格彙整了近期一系列零散但彼此牽動的更新，從 SDK 遷移到本機模型測試，勾勒出目前 LLM 開發工具鏈的真實樣貌。

🤔 **httpx 換成 httpx2，牽動一串依賴鏈**

Anthropic 在其 anthropic v1.0.0 Python 函式庫中把底層從 httpx 換成了 httpx2，OpenAI 兩週前也在 v3.0.0 做了同樣的改動。這個變動直接讓 LLM 專案的全新安裝失效：LLM 原本仰賴 httpx，但只是透過 openai 的傳遞依賴（transitive dependency）間接安裝，OpenAI 函式庫一旦拿掉 httpx，LLM 就跟著壞掉。Simon 先用釘住版本 openai<3 的方式緊急修補，之後即將推出的 0.33 版才會正式改用 httpx2。為了讓 Anthropic 外掛跟上 anthropic>=1，他直接在 Claude Code 中提示 Fable 5：「讀取官方 migration guide，升級並讓測試全部通過」。

🧩 **LLM 生態系的連動更新**

llm-gemini 外掛也同步升級，新增對 Gemini 3.7 Flash、gemini-3.6-flash、gemini-3.5-flash-lite 的支援，以及 gemini-embedding-2 與 gemini-embedding-001 兩個 embedding 模型；配合 LLM 0.32，現在可以看到 reasoning traces，也能透過特定模式啟用 server-side tools。嵌入模型現在也採用與一般 LLM 模型相同的金鑰模式，讓使用者能建立「模型 + 預設參數」打包成模板的用法，這對於測試各家自行仿製 OpenAI Responses API 的服務特別實用。

💡 **agentic coding 的臨場應變：計畫 A 行不通就換計畫 B**

Bun 1.4 是自從 Rust 重寫以來的首個穩定版，新增 1,517 項 Node.js 測試、修了超過 2,900 個問題，並帶來 Bun.Image、Bun.WebView、Bun.markdown、Bun.cron()、Bun.Terminal、bun run --parallel 等一系列新功能。其中最吸引 Simon 注意的是 Bun.WebView，它透過 macOS WebKit 或本機 Chromium 的 CDP 協定，為 Bun 核心帶來第一級的瀏覽器自動化支援。受此啟發，他讓 Claude Code for web 建了一個雛形版網頁 API，可以載入網頁並對其執行 JavaScript，測試發現要跑起完整 Chrome 大約需要 192MB 到 256MB 的容器（以 cgroups 測量）。

另一個例子更能看出 agentic coding 工具的臨場反應能力：Simon 交給 Claude Code for web 中的 Fable 5 一項研究任務，要它評估 smolmachines.com 作為執行不受信任程式碼的沙箱可行性。Fable 5 很快發現 Claude Code for web 的環境本身無法執行 smol machines，於是改用 Plan B：安裝 smolvm，直接在 GitHub Actions runner 上對該分支跑測試。Simon 形容這是 Fable「鍥而不捨地主動應變」的又一個例子。此外他也用 GPT-5.6-Sol xhigh 打造了一個網頁 UI，用來測試在 LM Studio 上運行於 M5 MacBook Pro 與 NVIDIA DGX Spark 的 Qwen 3.8 27B，該 UI 相容於 OpenAI-Responses 格式的 chat endpoint，對 LM Studio（搭配 --cors）與 OpenRouter 都能正常運作，對話會保存在瀏覽器中並可匯出成 JSON，還會在串流輸出過程中即時漸進渲染生成中的 SVG 圖片。

📊 **其他值得一提的小修補**

sqlite-utils 4.2 曾出現一個因為 typing-extensions 未被正式列為依賴而導致的崩潰問題（該套件原本是靠其他開發依賴間接安裝），修復後他也建立了用 --no-default-groups 與 --isolated 執行的煙霧測試，確保即使沒有開發依賴，CLI 工具仍可正常運作；table.transform() 功能也在這次更新中補齊了更多邊界情況的支援，包括 check constraints、unique constraints 與欄位註解的保留。

🎯 **實務啟示**

當 Anthropic、OpenAI 這類上游 SDK 進行大版本升級時，值得預先盤點自己專案中透過傳遞依賴間接使用的底層函式庫，避免像 LLM 這次一樣被動遭殃；同時，agentic coding 工具在遇到環境限制時展現的「換一條路徑照樣把任務做完」的能力，也是評估這類工具實用性時值得關注的面向。

🔗 **來源**
- 標題：Elsewhere
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/elsewhere/

#LLMTooling #Anthropic #OpenAI #Bun #AgenticCoding #LocalLLM #DeveloperTools #ClaudeCode #Gemini #SQLite
