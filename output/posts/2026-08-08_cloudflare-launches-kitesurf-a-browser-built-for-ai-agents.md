---
title: Cloudflare launches Kitesurf, a browser built for AI agents
source: TechCrunch AI
url: https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/
model: tencent/hy3:free
generated_at: '2026-08-08T06:51:49.943077'
score: 84
---

📌 【Cloudflare 新品】推出 Kitesurf：專為 AI Agent 設計的雲端瀏覽器

TL;DR：Kitesurf 是運行於 Workers 上的雲端瀏覽器，讓 AI Agent 能高效執行網頁任務。

🎣 隨著 AI 從「回答問題的聊天機器人」演進為「能代執行任務的代理人 (Agents)」，瀏覽器正成為這場轉型中的關鍵基礎設施，因為 Agent 需要像人類一樣瀏覽網頁並操作網站。

🧩 **專為 Agent 優化，捨棄視覺元素與外掛**

與傳統為人類設計的瀏覽器不同，為 AI Agent 設計的瀏覽器不需要主題 (themes)、分頁 (tabs) 或瀏覽器擴充功能 (browser extensions)。Cloudflare 指出，AI 瀏覽器更核心的挑戰在於：
- 管理 Context window (上下文視窗)
- 效能與擴展性 (scalability)
- Token 成本控制
- 應對新型態威脅，例如 Prompt injection (提示詞注入) 攻擊

🛠️ **技術架構：基於 Workers 運作的模組化設計**

Kitesurf 是一個完全運行在 Cloudflare serverless 平臺 Workers 之上的雲端託管瀏覽器。其技術組成包含：
- 渲染引擎：採用 Blitz 的模組化渲染引擎
- CSS 解析器：使用 Firefox 的 Stylo
- JavaScript 引擎：使用 Rust 編寫的 Boa JS
- 靈感來源：受開源 Rust headless 引擎 Obscura 啟發，其概念驗證 (PoC) 是將 Obscura 移植到 Workers 上完成的。

📊 **效能優於 Chromium，能有效降低運算成本**

對於開發者而言，Kitesurf 的核心優勢在於降低成本與提升效率。Cloudflare 宣稱，在執行如截圖 (screenshots) 與 HTML 擷取 (HTML extraction) 等常見的 Agent 任務時，Kitesurf 的 CPU 與記憶體消耗顯著低於 Chromium。

目前 Kitesurf 處於 Beta 測試階段，開發者可以透過 Browser Run 免費使用，藉此以程式化方式控制並與 Cloudflare 網路上的 headless browser (無頭瀏覽器) 實例進行互動。

💡 **測試表現與相容性**

雖然產品尚屬早期階段，但 Kitesurf 已通過超過 215,000 項 Web Platform 測試，且每週都在增加測試項目。根據官方測試，它能正確渲染 TodoMVC (JavaScript 框架基準測試應用)、Wikipedia、Hacker News、Cloudflare Blog 以及 Cloudflare 控制台。

🎯 **實務啟示**

AI 應用程式的開發者現在不需要自行開發複雜的瀏覽器軟體，即可讓 Agent 具備導航網站、填寫表單等網頁操作能力，並能利用 Cloudflare 的基礎設施來降低 Agent 運算與 Token 的成本。

🔗 **來源**
- 標題：Cloudflare launches Kitesurf, a browser built for AI agents
- 作者／機構：Sarah Perez @ TechCrunch
- 連結：https://techcrunch.com/2026/08/07/cloudflare-launches-kitesurf-a-browser-built-for-ai-agents/

#Cloudflare #Kitesurf #AIAgents #WebBrowser #Serverless #Workers #Chromium #HeadlessBrowser #MachineLearning #AIInfrastructure
