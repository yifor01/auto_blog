---
title: ChromeDevTools/chrome-devtools-mcp
source: GitHub Trending
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-06-16T21:11:47.308159'
---

📌 【ChromeDevTools 最新開源】讓 AI 代理人直接操控 Chrome DevTools，自動化除錯進入新階段

你是否曾希望 AI 能幫你檢查 Network Tab 為什麼報錯，或者直接分析 Page Speed 效能瓶頸，而不是得把截圖或 Log 貼給它？現在，Google ChromeDevTools 團隊將這個願望變成了現實。

透過最新的 `chrome-devtools-mcp` 專案，AI Coding Agent 不再只是「寫程式碼」，而是能像開發者一樣，直接「操控並檢查」一個運作中的 Chrome 瀏覽器。

🤔 **從「生成程式碼」到「掌控運行環境」的跨越**

目前的 AI 助手（如 Cursor, Claude, Copilot）強在邏輯生成，但在面對「運行時錯誤（Runtime Error）」時，通常依賴開發者手動餵資料。這種斷層導致 AI 缺乏對實際執行環境的感知。

這項專案的核心在於將 Chrome DevTools 封裝成一個 MCP (Model Context Protocol) 伺服器，讓 AI 代理人擁有一個標準化的介面來與瀏覽器互動，將「觀察 $\rightarrow$ 分析 $\rightarrow$ 修改」的循環完全自動化。

🧪 **基於 MCP 協定，將瀏覽器能力模組化**

該工具將 Chrome 的底層能力轉化為 AI 可調用的 Tool，其設計亮點在於：

- **標準化介面**：採用 MCP 協議，使其能快速整合進 Antigravity, Claude, Cursor 或 Copilot 等支援 MCP 的 AI 工具中。
- **Puppeteer 驅動**：底層使用 Puppeteer 實現可靠的自動化操作，並具備自動等待動作結果的機制，減少 AI 操作時常見的同步問題。
- **獨立運行能力**：除了 MCP 模式，專案同步提供 CLI 工具，讓不使用 MCP 框架的開發者也能直接利用其功能。

🚀 **AI 現在能幫你做這三件事**

- **深度除錯 (Advanced Debugging)**：AI 可以直接分析網路請求 (Network requests)、檢查主控台訊息 (Console messages)，且支援 source-mapped stack traces，讓 AI 能精準定位到原始碼的錯誤行數。
- **效能洞察 (Performance Insights)**：AI 能記錄追蹤紀錄 (Traces) 並提取可執行的效能優化建議，而非僅僅是猜測。
- **視覺化驗證**：AI 能主動截圖 (Take screenshots)，確認 UI 渲染是否符合預期。

⚠️ **權限極高，請小心處理敏感資訊**

由於 `chrome-devtools-mcp` 會將瀏覽器實例的所有內容暴露給 MCP 客戶端，這意味著 AI 代理人可以檢查、除錯甚至修改瀏覽器中的任何數據。

**重要提醒：** 請避免在 AI 操控的瀏覽器視窗中輸入敏感個資或私密資訊，以免被傳送至 AI 模型端。此外，該專案目前僅正式支援 Google Chrome 與 Chrome for Testing，其他 Chromium 瀏覽器的相容性並不保證。

🎯 **從「手動除錯」轉向「AI 驅動的自動化診斷」**

這項工具的實務價值在於將 AI 的能力從「靜態分析」提升到「動態診斷」。對於前端工程師或 QA 而言，未來的開發流程可能會變成：

1. AI 偵測到 Bug $\rightarrow$ 2. AI 自動開啟 Chrome $\rightarrow$ 3. AI 檢查 Network 與 Console $\rightarrow$ 4. AI 根據 Stack Trace 修改程式碼 $\rightarrow$ 5. AI 再次驗證 $\rightarrow$ 6. 完成。

這將大幅降低重複性的除錯成本，讓開發者專注於更高層次的架構設計。

🔗 **專案連結**
📦 專案名稱：chrome-devtools-mcp
👤 作者：ChromeDevTools
🔗 GitHub：https://github.com/ChromeDevTools/chrome-devtools-mcp

你會讓 AI 代理人接管你的瀏覽器除錯流程嗎？歡迎在下方分享你的看法 👇

#Chrome #DevTools #MCP #AI #LLM #Automation #WebDevelopment #Google #OpenSource
