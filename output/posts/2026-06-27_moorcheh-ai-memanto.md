---
title: moorcheh-ai/memanto
source: GitHub Trending
url: https://github.com/moorcheh-ai/memanto
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-06-27T19:33:54.219061'
---

📌 **不再依賴向量資料庫：Memanto 為 AI Agent 提供主動式本地記憶層**

TL;DR：Memanto 是一個開源記憶代理，透過 remember、recall、answer 三大操作，為多款 AI Agent 提供跨對話的持久化記憶。

大多數 AI Agent 的記憶工具僅是「被動基礎設施」：Agent 必須主動查詢、解析結果，再決定下一步。這種模式導致 Agent 在追求長期目標時容易產生混亂或遺忘。

🧩 **從被動儲存轉向「主動記憶代理」**

Memanto 的設計理念並非單純的儲存空間，而是一個能夠「記憶、回想並回答」的記憶代理（Memory Agent）。其核心特點在於：

- **針對 Agent 痛點設計**：根據 AI Agent 自述的記憶缺口，實作了三項核心操作：`remember`（記憶）、`recall`（回想）與 `answer`（回答）。
- **跨對話持久化**：讓 Agent 在不同 session 之間能保有上下文，避免重複溝通或資訊流失。
- **資訊理論搜尋引擎**：基於首個資訊理論（information-theoretic）搜尋引擎構建，旨在提供高效的檢索效能與零寫入延遲（zero ingestion latency）。

⚙️ **支援多款工具且部署靈活**

Memanto 可作為 Claude Code、Cursor、Codex 等 14 種以上 AI Agent 的記憶擴充，且提供兩種部署選項：

- **完全本地化 (Fully Local)**：無需帳號與 API Key，透過 Docker 與 Ollama 執行，所有資料完全留在使用者機器上。
- **免費雲端 (Free Cloud)**：透過 Moorcheh API Key 快速啟動，約 60 秒即可完成設定。

🛠️ **快速上手流程**

安裝過程簡單，支援 macOS、Linux 與 Windows：

1. 執行 `pip install memanto`
2. 執行 `memanto` 指令
3. 選擇「On-Prem」進入 Docker + Ollama 設定（本地化）或選擇「Cloud」並貼上 API Key（雲端）。

🎯 **實務啟示**

對於開發 AI Agent 的工程師來說，Memanto 嘗試將記憶層從「被動的資料庫查詢」提升為「主動的記憶代理」。最關鍵的價值在於其「無需向量資料庫 (no vector database)」與「無後端維護」的宣稱，降低了實現長期記憶的工程複雜度，讓開發者能更專注於 Agent 的任務邏輯，而非底層記憶體的管理。

🔗 **來源**
- 標題：moorcheh-ai/memanto
- 作者／機構：moorcheh-ai
- 連結：https://github.com/moorcheh-ai/memanto

#AI #AIAgents #OpenSource #LocalLLM #MemoryAgent #ClaudeCode #Cursor #InformationTheory #PersistentMemory #Moorcheh
