---
title: "Hmbown/DeepSeek-TUI"
source: GitHub Trending
url: https://github.com/Hmbown/DeepSeek-TUI
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:51:49.331627
---

📌 **DeepSeek V4 終端原生 TUI 代理釋出**

在終端機裡跑 AI Agent 已經不稀奇，但能完整支援 1M Token 上下文、思考模式串流，還能調度子代理的工具，目前還不多見。GitHub Trending 上出現的這個開源專案，試圖把 DeepSeek V4 的完整能力直接帶進你的 CLI 工作流。

🤔 **DeepSeek V4 火力全開，終端機介面卻跟不上？**

大型語言模型的上下文長度不斷增加，DeepSeek V4 已經來到 1M Token 的規模。然而，許多現有的互動介面仍停留在簡單的問答模式，無法有效利用龐大的上下文進行複雜的專案級操作。這個專案試圖解決的問題是，如何讓開發者在熟悉的終端環境中，直接調度具備完整工具使用能力的 AI 代理。

🧪 **專為 DeepSeek V4 設計的鍵盤驅動工作流**

這是由 Hmbown 開發的 `deepseek-tui`，一個完全在終端機運作的編程代理。它不僅是一個對話框，而是一個具備完整 Agent Loop 的系統。它支援 `deepseek-v4-pro` 與 `deepseek-v4-flash`，並針對這兩個模型優化了工具呼叫與上下文壓縮機制。

 **三種模式切換：從只讀觀察到 YOLO 全自動**

這個工具最實用的設計在於它的三種互動模式，滿足不同場景的需求：

- **Plan 模式**：唯讀探索，適合讓 AI 分析現有程式碼庫。
- **Agent 模式**：互動式操作，執行檔案修改或指令前會先請求批准。
- **YOLO 模式**：全自動執行，適合信任度高的標準化任務。

此外，它支援透過 Shift+Tab 切換推理強度（off → high → max），並能即時串流顯示模型思考過程（Thinking-mode）。

💡 **平行 RLM 分解，讓 AI 自己管理子任務**

這個專案的技術亮點在於其「分解優先」的系統提示設計。它內建了 `rlm_query` 工具，能夠平行調度 1 到 16 個 `deepseek-v4-flash` 子代理進行分析或推理。

這代表模型在執行複雜任務前，會先學習撰寫檢查清單（checklist）、更新計畫（update_plan），甚至在必要時生成子代理來並行處理不同區塊的程式碼。這種設計有效地利用了 Flash 模型低成本的特性來進行大規模的上下文處理。

⚠️ **非官方實作，依賴 API 配額與網路環境**

雖然功能強大，但這是一個社群開源專案（Hmbown），並非 DeepSeek 官方出品。使用者需要自行準備 API Key，且工具涉及網頁搜尋與 Git 操作，需留意權限管理與執行環境的安全性。另外，雖然支援 1M Token 上下文，但在極端長的對話下，系統會進行自動智慧壓縮（Intelligent Compaction）。

🎯 **給 CLI 死忠們的生產力神器**

如果你習慣在終端機裡完成所有工作，且不滿足於單純的程式碼補全，這個工具提供了一個完整的 Agentic 解決方案。你可以透過 `npm i -g deepseek-tui` 快速安裝。對於需要頻繁切換上下文、處理大型專案，或是想要觀察模型思考過程的開發者來說，這是一個值得嘗試的本地化部署方案。

🔗 **專案連結**
📝 DeepSeek-TUI: A terminal-native coding agent for DeepSeek V4
👤 Hmbown
🔗 GitHub: https://github.com/Hmbown/DeepSeek-TUI

你習慣用哪種 AI 編程工具？是喜歡 IDE 整合還是終端機原生？歡迎留言討論 👇

#DeepSeek #AI #Terminal #TUI #CodingAgent #OpenSource #GitHub #程式開發
