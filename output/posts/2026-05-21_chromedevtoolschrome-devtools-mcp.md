---
title: "ChromeDevTools/chrome-devtools-mcp"
source: GitHub Trending
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:34:23.999334
---

📌 Chrome DevTools 為 AI 打開的入口  

你的 AI 編程助手是否能直接操控瀏覽器除錯？一個新開源專案讓這成為可能。  

🤔 為什麼需要讓 AI 直接操作 DevTools  
隨著 Antigravity、Claude、Cursor、Copilot 等 AI 輔助編程工具成為開發者的日常，人們希望這些助手不僅能產生程式碼，還能在真實瀏覽器環境中進行除錯、效能分析與自動化測試。然而，傳統的 AI 工具只能透過文字或 API 與網頁互動，難以獲得瀏覽器內部的完整狀態。這正是 chrome-devtools-mcp 試圖解決的問題：讓 AI 能像開發者一樣，直接存取 Chrome DevTools 的全部功能。  

🧪 專案如何實現 MCP 伺服器與 Puppeteer 自動化  
chrome-devtools-mcp 以 Model-Context-Protocol (MCP) 伺服器的形式運行，提供一組標準介面讓 AI 客戶端呼叫。透過這個介面，AI 可以：  
- 使用 Chrome DevTools 記錄追蹤並擷取可操作的效能洞察。  
- 分析網路請求、擷取螢幕截圖、讀取帶有 source‑map 堆疊追蹤的控制台訊息。  
- 藉由內建的 Puppeteer 自動化層，在 Chrome 中執行操作並自動等待操作結果。  
專案同時提供一個命令列介面 (CLI)，讓開發者在不使用 MCP 的情況下也能直接呼叫相同的功能。  

🔑 核心功能：效能追蹤、深度除錯、可靠自動化  
根據專案說明，chrome-devtools-mcp 的主要能力包括：  
1. **效能洞察**：透過 DevTools 的追蹤功能產生效能資料，並將其轉換為 AI 可理解的建議。  
2. **進階瀏覽器除錯**：檢查網路請求、擷取畫面、讀取控制台訊息，並提供原始碼對應的堆疊追蹤。  
3. **可靠自動化**：利用 Puppeteer 在 Chrome 中執行點擊、輸入等操作，並自動等待操作完成，減少因時序問題導致的失敗。  
這些功能讓 AI 助手不僅能產生程式碼，還能在真實瀏覽器環境中驗證、優化與除錯。  

💡 使用注意與安全聲明  
專案特別提醒，由於 MCP 伺服器會將瀏覽器實例的內容暴露給連接的 AI 客戶端，使用者應避免分享不願透露給 AI 的敏感或個人資料。此外，chrome-devtools-mcp 官方僅支援 Google Chrome 與 Chrome for Testing；其他以 Chromium 為基礎的瀏覽器雖可能運作，但行為不受保證，使用時需自行斟酌風險。  

⚠️ 限制：僅支援特定 Chrome 版本，其他瀏覽器行為不保證  
- 功能依賴於 Chrome DevTools，因此只在官方支援的 Extended Stable Chrome 版本上保證穩定。  
- 對於其他 Chromium 衍生瀏覽器，專案未進行正式測試，可能出現預期以外的行為。  
- CLI 與 MCP 兩種使用方式均需自行安裝相依套件（如 Node、Puppeteer），安裝過程未在說明中詳細說明。  

🎯 對 AI 輔助開發工作流的潛在影響  
透過讓 AI 能直接呼叫 DevTools 的除錯與效能工具，開發團隊可能會看到以下變化：  
- AI 不僅能產生程式碼，還能在產出後立即執行效能分析，提供更具體的最佳化建議。  
- 在除錯階段，AI 能自行擷取控制台訊息與網路請求，減少開發者在瀏覽器切換與手動查詢的時間。  
- 自動化測試腳本可以透過同一介面由 AI 生成、執行與驗證，提升端到端測試的連貫性。  
這些可能性使得 chrome-devtools-mcp 成為構建更智慧、閉環 AI 編程環境的一塊重要基礎設施。  

🔗 Repo 連結  
📂 chrome-devtools-mcp  
🔗 https://github.com/ChromeDevTools/chrome-devtools-mcp  

你有試過讓 AI 直接操作瀏覽器除錯嗎？歡迎在留言區分享你的經驗或想法 👇  

#ChromeDevTools #MCP #AI開發 #瀏覽器除錯 #開源工具 #Claude #Cursor #Copilot #Antigravity #GitHubTrending
