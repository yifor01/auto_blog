---
title: Claude in Chrome is generally available
source: Claude Blog
url: https://claude.com/blog/claude-in-chrome-generally-available
model: claude-code/sonnet
generated_at: '2026-08-27T17:18:44.249963'
score: 107
---

📌 Claude in Chrome 全面開放，可自主完成瀏覽器操作

TL;DR：Claude in Chrome 正式 GA，能自主執行網頁操作，並靠安全分類器逐一驗證動作合法性。

如果你的工作流程裡有一堆沒有 API、只能靠人手動點擊的內部系統呢？Anthropic 這次把答案交給了瀏覽器本身：Claude in Chrome 現在對所有付費 Claude 方案全面開放，而且不再需要每個動作都經過人工核准。

🤔 **為什麼要讓 Claude 進瀏覽器**

許多日常使用的工具已經能直接連接 Claude，但內部儀表板、老舊系統、供應商入口網站等，往往沒有這樣的整合管道。Claude in Chrome 讓 Claude 直接使用你既有的登入狀態，讀取當前頁面、輸入文字、點擊連結、在頁面間導覽、填寫表單，等於補上了這一塊「無法整合」的缺口。這項功能去年以 pilot 形式首次推出，這次的 GA 是在強化 prompt injection 防禦後做出的決定。

🧩 **兩層防線：內容掃描 + 動作驗證**

Prompt injection 攻擊的風險是：惡意指令可能藏在網頁、郵件或表單欄位裡，使用者看不到，但可能讓代理人做出使用者從未要求的事，例如把郵件轉寄給攻擊者。Anthropic 描述了兩層防線。第一層是探針（probe），會在工具結果（也就是 Claude 讀到的頁面或郵件內容）進入模型之前先行掃描，一旦偵測到疑似攻擊，Claude 會被提醒對該內容保持懷疑，必要時會先向使用者確認。這組探針最早部署在 Claude Opus 4.5 上，後續持續擴大涵蓋的攻擊類型。第二層是動作驗證：在 Claude 執行像是切換網站、輸入文字這類動作之前，一個分類器會比對這個動作是否符合使用者原本的請求，不符合就會被擋下。這套自動核准機制，用的是和 Claude Code 中 auto mode 相同的方式，使用者仍可在設定中關閉，改回逐步人工核准。

📊 **從 17.6% 到 0%，但仍有例外**

Anthropic 公布了幾組評測數據。在較早、以 Cowork harness 進行的初步評測中，即使不開啟探針與分類器，Claude Fable 5、Opus 5、Sonnet 5 都沒有被任何攻擊突破。而在使用專業紅隊提供的更強攻擊的最新評測中，觸及模型的攻擊在沒有額外防護時，對 Opus 4.5 的成功率為 17.6%，對 Opus 5 為 3.8%；即使加上 2025 年 11 月時最強的防護，Opus 4.5 搭配探針仍有 16.7% 的攻擊成功率。但從 Opus 4.8 之後的每一個模型，只要同時搭配探針與安全分類器，Sonnet 5、Opus 5、Mythos 5 都沒有被任何攻擊突破，Fable 5 的攻擊成功率則是 0.3%。Anthropic 表示已人工確認所有成功突破的案例都屬於低嚴重度情境，並持續進行修補。

⚠️ **仍是移動中的目標**

Anthropic 也坦言，這套防禦只針對目前已知的攻擊手法有效，攻擊方式仍在持續演化，需要每一代模型都投入更多自動化攻擊發現與紅隊測試。此外，Claude in Chrome 目前僅支援 Chrome，不支援其他 Chromium 瀏覽器或行動裝置；若要處理本機檔案或串接其他應用程式，仍需要搭配桌面版 App 使用。

🎯 **實務啟示**

對於需要在內部系統、供應商後臺等「無 API」環境中自動化重複性瀏覽器操作的工程團隊，這次 GA 加上自動核准機制，代表可以開始評估把更多低風險、規則明確的瀏覽器任務交給 Claude 處理；企業方案下也可以透過 Organization Settings 把使用範圍限制在核準的網域內，作為導入前的風險控管手段。

🔗 **來源**
- 標題：Claude in Chrome is generally available
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/claude-in-chrome-generally-available

#Claude #ClaudeInChrome #Anthropic #PromptInjection #BrowserAutomation #AIAgent #AISafety #ClaudeCowork #LLMSecurity #Automation
