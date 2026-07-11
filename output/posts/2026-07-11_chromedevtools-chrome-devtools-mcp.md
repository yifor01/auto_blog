---
title: ChromeDevTools/chrome-devtools-mcp
source: GitHub Trending
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
score: 113
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T09:26:05.006320'
---

📌 **ChromeDevTools 推出 MCP Server，讓 AI 直接控制瀏覽器**

TL;DR：ChromeDevTools 官方發布 MCP 伺服器，讓 AI 程式設計代理能直接操控 Chrome 進行除錯與效能分析。

🎣 你習慣用 AI 寫前端，卻發現它無法真正「看見」網頁在瀏覽器裡的實際運作狀態？現在，Chrome 開發工具團隊把這種隔閡打破了。

🧩 **MCP 協議與 DevTools 的深度整合**

這是一個開源專案 `chrome-devtools-mcp`，由 ChromeDevTools 團隊維護。它的核心目標是作為一個 Model-Context-Protocol (MCP) 伺服器，讓你的 AI 程式設計助手（如 Cursor、Copilot 或 Claude）能夠直接控制並檢查一個正在執行的 Chrome 瀏覽器例項。

透過這個橋接層，AI 不再只是靜態地閱讀程式碼，而是獲得了 Chrome DevTools 的全部能力。這意味著 AI 可以執行可靠的自動化操作、進行深度的除錯，以及分析網頁效能。專案也提供了 CLI 工具，讓使用者在不使用 MCP 的情況下也能直接操作。

📊 **三大核心功能**

根據 README 的描述，這個工具主要提供以下幾類能力：

*   **效能洞察**：利用 Chrome DevTools 記錄追蹤 (traces)，並提取可操作的效能改進建議。
*   **進階瀏覽器除錯**：能夠分析網路請求、擷取螢幕畫面，以及檢查瀏覽器主控臺的訊息（包含經過 Source Map 轉換的堆疊追蹤），這對於定位前端錯誤極具價值。
*   **可靠自動化**：底層使用 Puppeteer 來自動化 Chrome 中的動作，並且能夠自動等待操作結果完成，確保指令碼執行的穩定性。

⚠️ **安全與相容性限制**

在使用前，必須注意幾項重要的限制與警告：

1.  **資料外洩風險**：`chrome-devtools-mcp` 會讓 MCP 客戶端存取瀏覽器例項的內容。這意味著 AI 可以檢視、除錯甚至修改瀏覽器中的任何資料。**強烈建議不要在此瀏覽器中登入任何敏感帳戶或處理個人資訊。**
2.  **瀏覽器支援範圍**：官方僅支援 **Google Chrome** 和 **Chrome for Testing**。雖然其他基於 Chromium 的瀏覽器可能運作，但不保證相容性，可能會遇到預期外的行為。
3.  **版本承諾**：團隊致力於為最新的 Extended Stable Chrome 版本提供修復與支援。

🎯 **實務啟示：從「寫程式」到「調校程式」**

對工程師而言，這標誌著 AI 輔助開發的一個轉變。過去 AI 主要依賴程式碼上下文進行生成，容易產生「理論上正確但實際上無法執行」的程式碼。

透過接入 MCP 與 DevTools，AI 現在具備了「觀察者」的視角。它可以即時看到 DOM 的狀態、網路請求的回應以及主控臺的錯誤。這對於自動修復前端 Bug、最佳化渲染效能，以及測試複雜的使用者互動流程，提供了前所未有的可靠性。不過，在將其納入 CI/CD 或日常開發流程前，務必建立隔離的瀏覽器環境以確保資安。

🔗 **來源**
- 標題：Chrome DevTools for agents
- 作者／機構：ChromeDevTools
- 連結：https://github.com/ChromeDevTools/chrome-devtools-mcp

#AI #MCP #ChromeDevTools #WebDevelopment #Puppeteer #Debugging #Automation #Frontend #OpenSource #BrowserTesting
