---
title: 'Meet WebBrain: An Open-Source, Local-First AI Browser Agent That Reads Pages
  and Automates Tasks in Chrome and Firefox'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/02/meet-webbrain-an-open-source-local-first-ai-browser-agent-that-reads-pages-and-automates-tasks-in-chrome-and-firefox/
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:56:52.087496'
---

📌 **WebBrain：支援本地模型、能直接操作瀏覽器的開源 AI Agent**

TL;DR：一款支援 Chrome 與 Firefox 的開源瀏覽器 Agent，可選擇本地模型執行以確保隱私，並透過 CDP 實現真實的網頁自動化。

大多數的瀏覽器 AI 外掛僅能讀取文字，但如果想要 AI 幫你點選按鈕、填寫表單，且不希望個資上傳到雲端，該怎麼做？

🧩 **本地優先的設計：資料不離開你的機器**

WebBrain 是一款由 Emre Sokullu 開發並以 MIT 授權釋出的開源專案。其核心特點在於「Local-First」，使用者可以將 Agent 連線至本地模型執行，讓所有網頁資料留在本地端；若需要更強的處理能力，則可選擇連線雲端 API。

該外掛直接執行在瀏覽器的側邊欄（Side Panel），且能直接利用使用者已登入的帳號 session 進行操作，無需重新登入。為了保護隱私，WebBrain 不會將資料儲存至外部，且不含任何遙測（telemetry）或帳號系統。

🧩 **「詢問」與「執行」兩種模式的技術差異**

WebBrain 將功能拆分為兩種模式，以平衡功能與安全性：

- **Ask mode（唯讀模式）**：僅能讀取頁面內容，無法修改頁面。其運作方式是透過一般的內容指令碼（content scripts）來讀取資訊。
- **Act mode（執行模式）**：可執行點選、輸入、捲動、跳轉及複雜的工作流。

值得注意的是 Act mode 的技術實作：在 Chrome 中，它透過 `chrome.debugger` API 呼叫 Chrome DevTools Protocol (CDP)，產生網站可信任的輸入事件，並能存取內容指令碼無法觸及的跨來源 iframe 與 shadow DOM。由於 Firefox 沒有對等的 CDP 機制，因此 Firefox 版的 Act mode 功能較弱。

💡 **為了可預測性與安全性的細節設計**

為了確保自動化操作的穩定性，WebBrain 固定了模型溫度（Temperature）設定，不允許隨意調整：
- **Act mode**：溫度 0.15（追求精準執行）
- **Ask mode**：溫度 0.3
- **視覺截圖描述**：溫度 0（追求絕對一致）

針對網頁端可能存在的「提示詞注入」（Prompt Injection）攻擊，WebBrain 採取了防禦性設計：Agent 預設從唯讀的 Ask mode 啟動，在執行任何具體操作前會先詢問使用者。

🎯 **實務啟示**

對於開發者而言，WebBrain 的實作路徑提供了一個關鍵參考：若要開發能被現代網站接受的自動化 Agent，單靠 content scripts 是不足的，利用 CDP (Chrome DevTools Protocol) 才能模擬出更真實的輸入事件並突破 shadow DOM 的限制。此外，將「讀取」與「執行」許可權分開，是處理 AI Agent 安全風險的有效實作模式。

🔗 **來源**
- 標題：Meet WebBrain: An Open-Source, Local-First AI Browser Agent That Reads Pages and Automates Tasks in Chrome and Firefox
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/07/02/meet-webbrain-an-open-source-local-first-ai-browser-agent-that-reads-pages-and-automates-tasks-in-chrome-and-firefox/

#AI #OpenSource #BrowserAgent #LocalLLM #Chrome #Firefox #CDP #Automation #Privacy #WebAutomation
