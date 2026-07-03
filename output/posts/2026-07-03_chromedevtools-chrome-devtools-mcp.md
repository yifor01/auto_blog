---
title: ChromeDevTools/chrome-devtools-mcp
source: GitHub Trending
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
score: 105
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:50:04.721103'
---

📌 【ChromeDevTools】讓 AI Agent 直接控制 Chrome 瀏覽器，實現自動化除錯與效能分析

TL;DR：透過 MCP 協定讓 AI 助手（如 Claude, Cursor）能操作 Chrome DevTools 進行除錯與效能分析。

開發者在利用 AI 寫 Code 時，最痛苦的往往是「AI 看不到執行結果」——它能寫出完美的程式碼，但無法知道為什麼在瀏覽器中跑不起來。如果 AI 能像工程師一樣開啟 DevTools 檢視 Console 或 Network 標籤頁，開發流程將會完全改變。

🧩 **將 Chrome DevTools 轉化為 AI 的「眼睛」與「手」**

`chrome-devtools-mcp` 是一個基於 Model-Context-Protocol (MCP) 的伺服器，旨在讓 AI Coding Agent（例如 Claude、Cursor、Copilot 或 Antigravity）能夠直接控制並檢查執行中的 Chrome 瀏覽器。

透過這個介面，AI 助手不再僅僅是生成程式碼，而是能直接呼叫 Chrome DevTools 的能力來進行可靠的自動化操作、深度除錯與效能分析。

🚀 **三大核心功能：從自動化到深度分析**

- **深度瀏覽器除錯**：AI 可以分析網路請求（Network requests）、截圖，以及檢查瀏覽器主控臺（Console）訊息，且支援透過 source-mapped stack traces 追蹤錯誤來源。
- **可靠的自動化操作**：底層使用 Puppeteer 來驅動 Chrome 執行動作，並能自動等待動作結果，確保自動化流程的穩定性。
- **效能洞察**：利用 Chrome DevTools 記錄追蹤紀錄（Traces），並從中提取可執行的效能最佳化建議。

⚠️ **使用限制與安全提醒**

- **隱私風險**：由於此工具會將瀏覽器例項的內容暴露給 MCP 客戶端，AI 將能檢查、除錯並修改瀏覽器或 DevTools 中的任何資料，請避免在操作時輸入敏感或個人資訊。
- **瀏覽器相容性**：官方僅正式支援 Google Chrome 與 Chrome for Testing。雖然其他 Chromium 核心的瀏覽器可能可行，但官方不保證其行為一致。
- **版本維護**：開發團隊承諾針對最新版本的 Extended Stable Chrome 提供修正與支援。

🎯 **實務啟示**

對於 AI 工程師而言，這意味著「除錯迴圈」的縮短。未來你不需要手動複製 Console 的錯誤訊息給 AI，而是可以直接要求 AI：「檢查目前的網路請求為什麼報錯，並根據 Console 的 stack trace 修復它」。這種從「生成程式碼」到「觀察 $\rightarrow$ 診斷 $\rightarrow$ 修復」的閉環，將大幅提升 AI 輔助開發的可靠度。

🔗 **來源**
- 標題：chrome-devtools-mcp
- 作者／機構：ChromeDevTools
- 連結：https://github.com/ChromeDevTools/chrome-devtools-mcp

#ChromeDevTools #MCP #AI #Puppeteer #Automation #Debugging #Browser #LLM #CodingAgent #WebDevelopment
