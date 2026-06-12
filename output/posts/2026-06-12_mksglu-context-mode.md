---
title: mksglu/context-mode
source: GitHub Trending
url: https://github.com/mksglu/context-mode
score: 99
model: google/gemma-4-31b-it:free
generated_at: '2026-06-12T20:38:51.078206'
---

📌 **【GitHub Trending】解決 MCP 記憶崩潰：Context Mode 讓上下文空間減少 98%**

當你使用 MCP (Model Context Protocol) 工具讓 AI 代理人（Agent）讀取 GitHub Issue 或 Playwright 截圖時，你是否發現對話只要持續 30 分鐘，上下文空間就快被塞滿了？

最糟糕的是，當 Agent 為了騰出空間而進行「對話壓縮」時，它往往會遺忘正在編輯的文件、執行中的任務，甚至是你最後的要求。

🤔 **工具調用正在「燒掉」你的上下文空間**

目前大多數 MCP 工具的運作方式是將原始數據（Raw Data）直接傾倒進上下文視窗。例如：
- 一次 Playwright 快照：56 KB
- 20 個 GitHub Issues：59 KB
- 一筆存取日誌：45 KB

這種模式導致上下文被大量冗餘數據佔據。當空間不足時，Agent 的壓縮機制會導致關鍵狀態遺失，且模型還會浪費輸出 Token 在客套話與冗長解釋上，從輸入與輸出兩端同時消耗資源。

🧪 **以 SQLite + FTS5 重新定義上下文管理**

`context-mode` 提出了一套全新的 MCP 伺服器設計，將「數據儲存」與「對話視窗」分離，核心設計包含以下三個維度：

**1. 數據沙盒化 (Context Saving)**
不再將原始數據直接丟入視窗，而是透過沙盒工具攔截。實測結果顯示，原本 315 KB 的數據量可縮減至 5.4 KB，減少了 98% 的空間佔用。

**2. 基於事件索引的會話連續性 (Session Continuity)**
所有文件編輯、Git 操作、任務進度與錯誤訊息都被記錄在 SQLite 中。當對話被壓縮時，`context-mode` 不會將所有數據重新塞回視窗，而是利用 FTS5 (Full-Text Search) 索引事件，並透過 BM25 搜尋算法僅檢索最相關的片段。這讓模型能精準接續之前的進度，而不會因為壓縮而失憶。

**3. 從「讀取數據」轉向「編寫分析程式」 (Think in Code)**
這是一個核心的思維轉變：讓 LLM 透過「編寫程式」來分析，而非透過「讀取數據」來計算。
- 傳統做法：讀取 50 個文件到上下文 $\rightarrow$ 讓 LLM 計算函數數量 $\rightarrow$ 消耗大量 Token。
- Context Mode 做法：LLM 寫一段腳本 $\rightarrow$ 執行腳本 $\rightarrow$ 僅將 `console.log()` 的結果回傳。
一個腳本即可取代十次工具調用，節省近 100 倍的上下文空間。

💡 **從「數據搬運」進化為「索引檢索」**

這項工具的洞察在於：LLM 不需要「擁有」所有數據，而只需要「能找到」正確的數據。透過將狀態管理外包給 SQLite 並引入檢索機制，將 LLM 從繁重的數據搬運工作中解放，讓它專注於高階的邏輯推理與程式編寫。

⚠️ **依賴本地資料庫，對即時性有特定需求**

由於該方案依賴 SQLite 與 FTS5 進行索引與檢索，其效能取決於檢索算法的精準度。此外，若不使用 `--continue` 指令，先前會話的數據會立即刪除，這意味著它採取的是一種「極簡且乾淨」的會話管理策略。

🎯 **開發 LLM Agent 的工程師可以嘗試的優化路徑**

如果你正在建構基於 MCP 的 Agent 系統，可以參考以下實作方向：
- **減少 Raw Data 注入**：將大塊數據存入外部儲存，僅回傳摘要或索引。
- **引入檢索機制**：使用 BM25 或向量檢索來替代全量回傳。
- **推動「Code-as-Analysis」**：引導模型編寫小工具來處理數據，而非直接讀取數據。

🔗 **專案連結**
📝 context-mode
👤 mksglu
🔗 GitHub: https://github.com/mksglu/context-mode

你目前在開發 AI Agent 時，最頭痛的是 Token 消耗還是模型失憶？歡迎在評論區分享你的解決方案 👇

#AI #LLM #MCP #GitHubTrending #SQLite #ContextWindow #AgenticWorkflow #軟體工程
