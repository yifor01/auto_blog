---
title: How to Give Your AI Agent Memory
source: KDnuggets
url: https://www.kdnuggets.com/how-to-give-your-ai-agent-memory
model: claude-code/sonnet
generated_at: '2026-11-06T22:29:18.876393'
score: 80
---

📌 幫 AI Agent 裝上長期記憶：用 Mem0 打破「每次對話都重來」

TL;DR：用 Mem0 與 MCP 讓 AI agent 跨 session 記住使用者偏好與決策。

你是不是常常要跟 AI 助理重複同一句「我比較習慣用 Python 搭配 uv」？多數 agent 對話一結束，這些資訊就消失了，下一次又要從頭說明。

🤔 問題：Agent 為什麼記不住

大部分 agent 推理、呼叫工具、完成任務都沒問題，但 session 結束後知識就歸零。文章把記憶分成兩種：短期記憶，指本次對話的訊息與暫時狀態；長期記憶，指偏好、決策、目標、過去經驗等能跨 session 保留的資訊。關鍵在「檢索」：不是把所有歷史對話塞進 prompt，而是讓 agent 搜尋記憶庫，只取出跟當前問題相關的片段，維持 context 精簡，同時還能表現出「記得你」的效果。

🧩 架構：search → reason → save 的迴圈

先用 `pip install openai-agents mem0ai` 安裝依賴，設定 `OPENAI_API_KEY` 與 `MEM0_API_KEY`。建立 `MemoryClient` 與一個 `USER_ID`，每位使用者獨立的 ID 能讓記憶彼此隔離。接著定義兩個 function tool：`search_memory` 呼叫 `memory.search` 做語意搜尋（Mem0 用語意比對，查詢字詞不用完全一致），回傳最相關的 5 筆記憶；`save_memory` 呼叫 `memory.add` 把值得保留的資訊寫入 Mem0，由 Mem0 自行判斷哪些內容該變成長期記憶，而不是整段對話都存下來。

Agent 的 instructions 明確規定行為：每次回答前都要先呼叫 `search_memory`，即使是一般問題；找到相關記憶時要自然地在回答開頭提及；遇到值得保留的偏好、目標、事實要呼叫 `save_memory` 並用一句話確認；略過問候語、暫時資訊與重複內容。最後用 `Runner.run_sync` 包成一個 `chat()` 函式即可互動。

📊 實測效果

先輸入「記得我偏好 Python 並用 uv 管理專案」，agent 會回覆確認已記住這個偏好。換個新問題「我的下一個 Python 專案該怎麼設定？」，agent 能自動在回答中帶出先前存的偏好，並給出 `uv init`、`uv add` 等指令建議。因為資料存在 Mem0 端，即使重啟 Python 應用程式，記憶依然能被檢索到。

🧩 接上 OpenCode：用 MCP 共享同一套記憶

Mem0 提供官方 hosted MCP server，內建 `add_memory`、`search_memories`、`get_memories`、`update_memory`、`delete_memory` 等工具。用 `npx mcp-add --name mem0-mcp --type http --url "https://mcp.mem0.ai/mcp" --clients "opencode"` 就能把同一套記憶接到 OpenCode，不用自己重寫 Python 工具。重啟 OpenCode 後，在一個 session 告訴它偏好，開新 session 問相關問題，OpenCode 就能透過 MCP 工具取回之前存的偏好；可用 `opencode mcp list` 確認連線狀態。

💡 深入分析

這套做法的核心，其實是在既有的 Mem0 托管記憶服務外面包一層 function tool，讓 agent 懂得何時查、何時寫。這類「檢索式記憶 wrapper」目前已是不少 agent 框架（包括 ChatGPT 的記憶功能）採用的共通模式，技術上沒有太多新東西，但勝在串接速度快，能直接套用到既有的 agent 專案上。

🎯 實務啟示

如果手上已有 agent 專案，不需要自己設計向量資料庫或檢索邏輯，直接接 Mem0 的 API 或 MCP server 就能快速補上跨 session 記憶。用 instructions 控制「什麼該存、什麼該略過」，往往比技術實作本身更關鍵，能避免記憶庫被問候語或重複資訊塞滿。而且同一套記憶可以同時供應用程式與 coding agent 使用，適合拿來做跨工具共用的使用者偏好庫。

🔗 來源
- 標題：How to Give Your AI Agent Memory
- 作者／機構：Abid Ali Awan, KDnuggets
- 連結：https://www.kdnuggets.com/how-to-give-your-ai-agent-memory

#AIAgent #LLM #Mem0 #OpenAIAgentsSDK #MCP #AgentMemory #RAG #OpenCode #MachineLearning #DeveloperTools
