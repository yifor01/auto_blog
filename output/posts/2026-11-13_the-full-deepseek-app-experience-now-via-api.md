---
title: The full DeepSeek App experience, now via API
source: DeepSeek
url: https://api-docs.deepseek.com/news/news261113
model: claude-code/sonnet
generated_at: '2026-11-13T22:42:03.268466'
pinned: true
---

📌 DeepSeek 把 App 裡的搜尋、檔案、語音能力全開給 API

TL;DR：DeepSeek 將 App 內的搜尋、檔案解析、URL 讀取、安全檢查與語音能力開放給開發者直接呼叫。

想重建一個像樣的 AI 聊天應用，光是搜尋、讀檔、語音這些基礎功能就要花掉大半開發時間。DeepSeek 這次直接把自家 App 背後的這些能力整包開放給開發者。

🤔 **開發者不該一直重造基礎功能**

根據 DeepSeek 官方公告，DeepSeek App 背後的搜尋、檔案處理、連結讀取、安全防護與語音這幾項能力，現在都可以透過 DeepSeek API 直接取用。開發者可以用幾個參數啟用內建功能，或是呼叫 OCR、ASR、TTS 等獨立 API，藉此打造更豐富的對話體驗，甚至在自己的應用中重現完整的 DeepSeek App 體驗。

🧩 **deepseek-flash 一次打包五項能力**

公告指出，V4.1-Flash（deepseek-flash）現在在 Messages、Responses、Chat Completions 三套介面上都支援以下能力，工具呼叫與 context 組裝皆由伺服器端處理：

- 網路搜尋（Web Search）：在非 thinking 模式下搜尋網頁或圖片，並附上引用來源。
- 深度思考搜尋（Deep Thinking Search）：在多步推理過程中搜尋並閱讀頁面內容。
- 檔案輸入（File Input）：將 PDF、Office 檔案、圖片等解析進對話的 context 中。
- 連結讀取（URL Reading）：自動抓取使用者訊息中的連結內容，作為回答的依據。
- 安全檢查（Safety Checks）：篩查輸入與輸出內容，偵測到風險時回傳拒絕指示。

要啟用搜尋與連結讀取，分別對應 deepseek_web_search 與 deepseek_read_url 這兩個參數；公告特別註明，面向公眾的應用必須啟用安全檢查。除了這些內建功能，搜尋、網頁擷取、OCR、ASR、TTS 也都提供獨立 API，方便開發者整合進自訂的工作流程。

DeepSeek 同時開源了一個聊天 demo 前端（chat-demo），支援匯入 DeepSeek 的對話紀錄，可作為串接這些能力的參考實作。

⚠️ **責任與費用仍在開發者身上**

公告明確表示，開發者仍須自行負責內容審核、適用的 AI 模型註冊，以及 AI 生成內容的標示義務。此外，這些擴充能力除了標準的 token 費用外，還會額外收取工具使用費，公告中附有費用細項說明，但本篇素材未提供具體金額。

🎯 **實務啟示**

對正在打造聊天類應用的工程師來說，這次釋出的意義在於「不用重新發明輪子」:搜尋、讀檔、語音辨識與合成這些曾經要自己串接第三方服務才能拼出來的功能，現在可以直接用 DeepSeek 的 API 參數開關取用。在規劃產品功能時，可以把重心放在差異化的體驗設計上，而不是重複打造搜尋或 OCR 這類基礎能力；同時別忘了把額外的工具使用費算進成本評估,並確認自己的應用符合安全檢查與內容標示的要求。

🔗 **來源**
- 標題：The full DeepSeek App experience, now via API
- 作者／機構：DeepSeek
- 連結：https://api-docs.deepseek.com/news/news261113

#DeepSeek #LLMAPI #AIAgents #WebSearch #OCR #ASR #TTS #ChatbotDevelopment #OpenSourceAI #DeveloperTools
