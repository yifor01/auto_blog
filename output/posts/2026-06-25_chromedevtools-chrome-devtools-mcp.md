---
title: ChromeDevTools/chrome-devtools-mcp
source: GitHub Trending
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:24:23.543607'
---

📌 【ChromeDevTools】讓 AI Agent 直接控制 Chrome：chrome-devtools-mcp 正式開源

TL;DR：透過 MCP 協定讓 AI 編碼助手能控制 Chrome 瀏覽器，實現自動化除錯與效能分析。

當 AI 編碼助手（如 Cursor 或 Claude）幫你寫完前端程式碼後，你通常仍需手動開啟瀏覽器、檢查 Console 或分析 Network 才能確認結果。如果 AI 能直接「看到」並「操作」瀏覽器，這個迴圈將被徹底改變。

🧩 **將 Chrome DevTools 轉化為 AI 的感知器官**

`chrome-devtools-mcp` 是一個 Model-Context-Protocol (MCP) 伺服器，它讓 AI 編碼代理（Coding Agent）能直接控制並檢查執行中的 Chrome 瀏覽器。這意味著 AI 不再只是生成程式碼，而是能透過 DevTools 的能力進行可靠的自動化操作、深度除錯以及效能分析。

🛠️ **核心功能與實作方式**

該專案提供 AI 助手以下三項關鍵能力：

- **效能洞察 (Performance Insights)**：利用 Chrome DevTools 記錄 traces，並從中提取可執行的效能最佳化建議。
- **進階瀏覽器除錯 (Advanced Debugging)**：AI 可以分析網路請求 (Network requests)、截圖，以及檢查瀏覽器主控臺 (Console) 訊息（包含經過 source-mapped 的堆疊追蹤）。
- **可靠的自動化操作 (Reliable Automation)**：底層使用 Puppeteer 驅動 Chrome 自動化操作，並會自動等待操作結果，確保執行穩定性。

💡 **彈性的部署選項與支援範圍**

除了作為 MCP 伺服器與 AI 助手整合外，該專案也提供 CLI 工具，讓使用者在沒有 MCP 環境的情況下依然可以使用。

在支援度方面，作者明確指出該專案正式支援 Google Chrome 與 Chrome for Testing。雖然其他基於 Chromium 的瀏覽器可能可以運作，但並不保證穩定性且可能出現非預期行為。

⚠️ **安全性與使用限制**

由於 `chrome-devtools-mcp` 會將瀏覽器例項的內容完全暴露給 MCP 客戶端，這意味著 AI 助手可以檢查、除錯並修改瀏覽器中的任何資料。因此，使用者應避免在操作過程中處理不希望與 AI 共享的敏感或個人資訊。

🎯 **實務啟示**

對於前端工程師而言，這將 AI 的能力從「寫程式碼」延伸到了「驗證與調優」。未來開發流程可能演變為：AI 撰寫程式碼 $\rightarrow$ AI 自動開啟 Chrome 驗證 $\rightarrow$ AI 發現 Console 報錯 $\rightarrow$ AI 自行修正程式碼，大幅減少在編輯器與瀏覽器之間切換的時間成本。

🔗 **來源**
- 標題：ChromeDevTools/chrome-devtools-mcp
- 作者／機構：ChromeDevTools
- 連結：https://github.com/ChromeDevTools/chrome-devtools-mcp

#ChromeDevTools #MCP #AI #Frontend #Automation #Puppeteer #Debugging #Chrome #WebDevelopment #LLM
