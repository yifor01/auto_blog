---
title: The Claude in Chrome side panel is now Claude Cowork
source: Claude Blog
url: https://claude.com/blog/cowork-chrome-side-panel
model: claude-code/sonnet
generated_at: '2026-08-13T07:25:58.803300'
pinned: true
---

📌 【Anthropic 官方發布】Claude in Chrome 側邊欄升級為 Cowork，任務可跨裝置無縫接續

TL;DR：Chrome 側邊欄裡的 Claude 現在直接對接 Claude Cowork，瀏覽器裡開始的任務能接續到桌面、網頁與行動裝置完成。

想像你在瀏覽器裡開了一堆分頁，正請 Claude 幫忙從各家廠商後臺抓發票金額整理成預算表，做到一半得先出門。過去這個工作階段（session）只存在瀏覽器分頁裡，關掉就等於重來。Anthropic 在 8 月 12 日的部落格文章宣布，這個斷點被打通了。

🤔 **側邊欄過去是孤立的**

Claude in Chrome 是一款瀏覽器擴充功能，讓 Claude 能看到你正在瀏覽的頁面，並代替你點擊連結、輸入文字、切換頁面、填寫表單，使用的是你既有的登入狀態。但根據文章說明，過去側邊欄裡的對話跟桌面版、網頁版、行動版的 Claude apps 是分開的兩套系統，context 和對話紀錄不會互通。

🧩 **同一個 Cowork session，跨平臺接續**

現在側邊欄執行的就是與桌面、網頁、行動版相同的 Claude Cowork session，用於需要多步驟、較長時間的工作。因為 session 是綁在帳號而非單一裝置上，你可以在瀏覽器裡開始一項任務，之後在任何地方接續。文章舉的例子是：你請 Claude in Chrome 幫忙從多個廠商入口網站蒐集發票金額與日期、建立成預算表，之後可以切到桌面版繼續加入電腦裡的檔案，或匯入上個月的預算比對差異。此外，你平常在其他 Claude apps 使用的 skills 與 connectors，在瀏覽器裡同樣可以運作。

⚠️ **Prompt injection 仍是核心風險**

Claude in Chrome 與所有能在瀏覽器裡行動的 AI agent 一樣，最主要的風險是 prompt injection：惡意內容可能被藏在網頁、郵件或文件裡，這些指令對使用者不可見，卻可能誘導 Claude 執行非預期的動作。Anthropic 表示，自從先前的 pilot 以來，他們新增了一道針對 Claude 自身行動的檢查機制：開啟「automatically approve」後，Claude 可以連續執行任務而不必每一步都停下來要求許可，但在送出表單、傳送訊息、下載檔案等具實質後果的動作前，會有獨立的檢查機制比對這個動作是否符合使用者原始的請求，不符合就會被擋下。至於購買或分享個人資料等不可逆或有成本的動作，Claude 仍會先詢問。文章也坦言，這些措施能顯著降低風險，但無法完全消除，官方建議先從你信任的網站開始使用。

🎯 **對工程師的實務啟示**

這項功能特別適合處理那些沒有直接串接 Claude 的系統，例如內部儀表板、老舊系統、廠商後臺，讓 Claude 透過瀏覽器介面去操作。目前新版側邊欄已對 Max 與 Team 方案開放，Pro 方案將於未來幾週陸續推出；Enterprise 方案預設關閉，需由管理員開啟並限制在核準的網域內使用。要注意的是，處理電腦本機檔案或串接其他應用程式仍需使用桌面版，且 Claude in Chrome 目前不支援其他 Chromium 瀏覽器或行動裝置。

🔗 **來源**
- 標題：The Claude in Chrome side panel is now Claude Cowork
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/cowork-chrome-side-panel

#Anthropic #ClaudeAI #ClaudeCowork #ClaudeInChrome #AIAgent #BrowserAutomation #PromptInjection #ProductivityTools #AIAssistant #EnterpriseAI
