---
title: "web-infra-dev/midscene"
source: GitHub Trending
url: https://github.com/web-infra-dev/midscene
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-05-23T19:28:45.544716
---

📌 【web-infra-dev】Midscene.js：AI 驅動、視覺導向的跨平台 UI 自動化框架  

你是否曾經為了寫穩定的 UI 測試而花費大量時間調整選擇器（selector），只因頁面微微變動就導致腳本失效？當前的自動化工具大多依賴 DOM 結構或座標，一旦介面改版、主題切換或跨平台測試，維護成本就會急速上升。  

🤔 **視覺 + 語言讓自動化不再脆弱**  
Midscene.js 把「看」和「說」結合起來：使用自然語言描述你想達成的目標與步驟，框架內部的視覺模型會根據當前畫面定位元素，進而執行點擊、輸入或斷言。這種方式不依賴固定的選擇器，理論上能在介面變動時仍保持穩定。  

🧪 **多平台統一的 SDK 與模式**  
- **Web**：可直接與 Puppeteer、Playwright 整合，或使用 Bridge Mode 控制本機桌面瀏覽器。  
- **Android**：透過 JavaScript SDK + adb 控制本機安卓設備或模擬器。  
- **iOS**：透過 JavaScript SDK + WebDriverAgent 控制本機 iOS 設備與模擬器。  
- **任意介面**：只要能透過 JavaScript 呼叫，即可使用同一套 SDK 操作自訂介面。  

💡 **核心功能概覽**  
1. **Interaction API** – 點擊、輸入、滑動等 UI 操作。  
2. **Data Extraction API** – 從畫面或 DOM 抽取文字、屬性或結構化資料。  
3. **Utility API** – 包含 `aiAssert()`、`aiLocate()`、`aiWaitFor()` 等輔助函式，讓斷言與等待更具語意。  
4. **MCP（Midscene Cloud Platform）** – 提供 UI 預覽與補丁發布功能，進一步簡化跨裝置測試流程。  

🔍 **深入技術點**  
- 框架內部使用視覺模型來理解螢幕畫面，將自然語言指令映射到可操作的 UI 元素。  
- 透過 SDK 層，開發者只需撰寫 JavaScript 或 YAML 腳本，即可獲得跨平台一致的執行體驗。  
- 因為不依賴固定的選擇器，理論上能減少因 UI 改版導致的腳本失效率。  

⚠️ **目前已知的限制**  
- 專案仍處於早期階段，社區文件與範例數量有限。  
- 視覺模型的準確度與效能會受到畫面解析度、光照條件以及模型版本的影響。  
- 複雜的跨桌面應用（例如原生視訊會議軟體）尚未在說明中明確提及支援程度。  

🎯 **對開發者的實務建議**  
- 若你的團隊正面臨 UI 測試維護成本高的問題，可先在非關鍵路徑上嘗試使用 Midscene.js 的自然語言腳本，觀察其在介面微小變動時的穩定性。  
- 利用 `aiLocate()` 與 `aiWaitFor()` 等 utility 函式，將視覺定位與顯式等待結合，減少不必要的硬編碼等待時間。  
- 關注專案的 Issue 與 Discussions，參與早期社群貢獻，有助於填補文件與範例的空白。  

🔗 **資源連結**  
- 📦 GitHub：https://github.com/web-infra-dev/midscene  
- 🌐 官方網站：https://midscenejs.com/  

你是否已經在專案中嘗試過以自然語言驅動的 UI 自動化？歡迎在留言區分享你的經驗或疑問 👇  

#AI #UIAutomation #Midscene #WebAutomation #MobileTesting #OpenSource #DevTools #web-infra-dev
