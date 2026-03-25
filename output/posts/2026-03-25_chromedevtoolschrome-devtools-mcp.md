---
title: "ChromeDevTools/chrome-devtools-mcp"
source: GitHub Trending
url: https://github.com/ChromeDevTools/chrome-devtools-mcp
score: 112
model: gpt-4o-free
generated_at: 2026-03-25T19:39:37.847370
---

📌 **ChromeDevTools 釋出 MCP 伺服器，讓 AI 編碼助理直接操控瀏覽器**  

你是否曾希望 AI 助手不只能寫程式，還能即時觀察網頁行為、偵測效能瓶頸或自動化重複的除錯步驟？Chrome 團隊最近在 GitHub Trending 上公開的 **chrome-devtools-mcp** 專案，正是要把 Model‑Context‑Protocol（MCP）與 Chrome DevTools 整合，讓 Gemini、Claude、Cursor、Copilot 等 coding agent 取得瀏覽器的完整偵測與自動化能力。  

🤔 **從程式產生到瀏覽器操作的自然延伸**  
隨著 AI 輔助編程工具成為日常，開發者的工作流程已經從「寫程式」擴展到「檢查程式在瀏覽器中的表現」。然而，傳統的做法仍需要人工切換到 DevTools 面板、手動錄製效能追蹤或逐行查看 console。這種斷裂不僅浪費時間，也增加了人為錯誤的機會。chrome-devtools-mcp 想要解決的正是這個痛點：讓 AI 能以程式化的方式呼叫 DevTools 的各項功能，使偵測與自動化成為編碼流程的一部分。  

🧪 **以 MCP 伺服器方式公開 DevTools 功能**  
該專案實作了一個 MCP 伺服器，透過標準的 Model‑Context‑Protocol 介面，將 Chrome DevTools 的核心能力包裝成可被 AI 客戶端呼叫的工具。實際上，它內部使用 Puppeteer 來驅動 Chrome 執行執行動作，並自動等待動作完成，以確保操作的可靠性。目前公開的功能包括：  - **效能追蹤**：記錄瀏覽器 trace，並擷取可操作的效能洞察（例如長任務、重繪瓶頸）。  
- **進階除錯**：擷取網路請求詳情、截圖、讀取 console 訊息，並提供 source‑map 對應的堆疊追蹤。  
- **可靠自動化**：透過 Puppeteer 執行點擊、輸入等瀏覽器操作，並自動等待結果返回。  

這些功能均透過 MCP 的「工具呼叫」方式呈現，讓 AI 助手可以在不離開編輯器的情況下，發出指令取得即時回饋。  💡 **AI 不再只是程式產生器，而是瀏覽器偵測夥伴**  透過這層抽象，AI 的角色從「根據提示產生程式碼」延伸至「觀察、分析與修改執行中的網頁」。例如，當 AI 產生一段新的 UI 元件時，它可以立即呼叫效能追蹤工具檢查是否引入了長任務；若偵測到異常，又可以自動截圖並將 console 錯誤回報給開發者。這種閉環互動有望減少人工除錯的迴圈，提升開發效率。  

⚠️ **資料暴露與瀏覽器支援的限制**  
專案文件明確指出，使用 chrome-devtools-mcp 會將瀏覽器實例的內容暴露給 MCP 客戶端，因此務必避免在處理敏感或個人資料時啟用該伺服器。此外，該工具官方僅支援 Google Chrome 與 Chrome for Testing；其他 Chromium 衍生瀏覽器或許能運作，但不保證行為一致，需自行斟酌風險。效能工具亦可能將 trace URL 傳送至 Google CrUX API 以取得真實使用者體驗資料，這也是需要注意的資料流向。  

🎯 **開發者可即將此工具納入工作流程**  - 將 chrome-devtools-mcp 作為本地 MCP 伺服器啟動，再在偏好的 coding agent 中設定對應的 MCP 客戶端。  - 透過 agent 的自然語言或程式介面呼叫「效能追蹤」、「除錯」或「自動化」工具，取得即時回饋。  
- 在團隊內建立標準化的偵測腳本，讓 AI 協助執行迴歸效能檢查或自動產生除錯報告。  

這樣的做法不需要深入了解 Puppeteer 或 DevOps 細節，開發者只要熟悉如何在自己的 AI 編碼助理中加入 MCP 服務，即可獲得瀏覽器層級的偵測與自動化能力。  

🔗 **專案連結**  
📦 chrome-devtools-mcp：https://github.com/ChromeDevTools/chrome-devtools-mcp  
（GitHub Trending 今日獲得 232 颗星，顯示社群對此類工具的關注度正在上升）  

你有試過讓 AI 助手直接除錯網頁嗎？歡迎在留言區分享你的使用經驗或想法 👇  

#AI #ChromeDevTools #MCP #開發工具 #除錯 #效能分析 #自動化 #GitHubTrending #Claude #Gemini #Cursor #Copilot
