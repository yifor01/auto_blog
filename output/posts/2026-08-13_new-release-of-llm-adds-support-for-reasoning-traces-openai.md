---
title: New release of LLM adds support for reasoning traces, OpenAI Responses, server-side
  tools, and smarter logging
source: Simon Willison
url: https://simonwillison.net/2026/Aug/4/new-release-of-llm/
model: claude-code/sonnet
generated_at: '2026-08-13T07:36:05.709968'
score: 80
---

📌 LLM 0.32：一個命令列小工具，正在長出 agent 的骨架

TL;DR：LLM CLI 新增 reasoning trace、伺服器端工具與 Git 式訊息記錄，形態越來越像 agent 框架。

一個原本只是「命令列丟一句 prompt、拿回一串字串」的小工具，如今能顯示模型的推理過程、呼叫供應商的伺服器端工具，還能像 Git 一樣做內容定址式的訊息記錄——Simon Willison 稱這是 LLM 專案自初版發布以來最重要的一次更新。

🤔 **為誰解決什麼問題**

LLM 是一個命令列與 Python 函式庫工具，讓使用者能混搭不同來源的模型與工具，以一行指令完成任務。隨著推理模型與代理式工作流普及，原本的設計開始出現落差：使用者看不到模型的推理過程、無法使用供應商提供的伺服器端工具、對話式 API 的訊息歷史會在每次記錄時重複寫入大量 JSON、也缺少一個能快速對任何 OpenAI 相容端點下 prompt 的工具。0.32 版針對這些缺口逐一補齊。

🧩 **這次更新做了什麼**

- **可視推理過程**：執行推理模型時，推理過程會顯示到標準錯誤（stderr），不會混進可以直接 pipe 給其他工具的標準輸出；加上 `-R`/`--hide-reasoning` 參數可關閉此行為。預設模型也改為較便宜但能力不錯的 GPT-5.6 Luna。
- **伺服器端工具**：OpenAI 提供程式碼執行環境與 WebSearch 作為伺服器端工具；`llm-anthropic` plugin 新增 WebSearch、WebFetch、CodeExecution 與 AnthropicMCP，可讓 Anthropic 在單一次請求／回應互動中，對外部 MCP 伺服器（例如作者自製的 datasette-mcp plugin）發出呼叫。
- **一次性端點工具**：新的 `llm openai endpoint` 指令能對任何 OpenAI 相容端點下一行式 prompt，且不會被記錄，適合對本機服務（例如透過 uvx 免安裝呼叫本機 LM Studio 上跑的 Gemma 4 12B）做一次性測試，還能混搭 `llm-tools-quickjs` 這類工具 plugin。
- **Python API 重新設計**：原本要求先建立對話物件、逐則傳送訊息，這其實是對「每次請求都攜帶完整歷史訊息」這個真實機制的一層抽象，在進階場景中反而礙事。新版加入 `model.prompt(messages=[])` 參數，可直接傳入完整訊息序列。
- **回應形狀升級**：過去每次 prompt 回傳的是字串序列，如今模型常混雜推理文字、輸出字串、工具呼叫甚至圖片附件，0.32 針對這種混合形狀提供了對應的處理方式。
- **內容定址訊息儲存**：仿照 Git 的設計，避免對話式 API 每輪都重複記錄相同的 JSON；`llm logs` 與 `llm logs --json` 也同步升級，能把這種新格式還原成易讀內容。
- **人工核可與續傳**：工具鏈呼叫現在可以暫停、等待人工核可，並從已儲存的訊息歷史繼續執行——這正是作者另一個專案 Datasette Agent 所需要的能力。

作者也基於這些底層變更，另外發布了 `llm-chat-completions-server` plugin，提供一個相容 OpenAI chat completions API 的伺服器實作，讓外部工具能透過 `llm openai endpoint` 直接對它下 prompt。

⚠️ **升級注意事項**

既有的 LLM plugin 應能繼續運作，但若 plugin 本身提供額外模型，就必須升級到 0.32 才能完整參與新的串流事件（streaming events）系統。

🎯 **實務啟示**

這次更新的多數底層改動，其實是被作者另一個專案 Datasette Agent 的需求所驅動的——工具鏈暫停等待人工核可、從儲存的訊息歷史續傳、混合型回應的處理，都是構建 agent 系統時會遇到的真實痛點。對正在用 LLM CLI 串接工具鏈或自建 agent 的工程師而言，這代表可以用同一套熟悉的命令列工具，逐步過渡到更接近 agent 框架的用法，值得檢視自己維護的 plugin 是否需要同步升級。

🔗 **來源**
- 標題：New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Aug/4/new-release-of-llm/

#LLMCLI #SimonWillison #OpenSource #AIAgents #OpenAIResponses #MCP #DeveloperTools #Python #CommandLineTools #ReasoningModels
