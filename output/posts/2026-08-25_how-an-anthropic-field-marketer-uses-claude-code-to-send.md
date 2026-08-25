---
title: How an Anthropic field marketer uses Claude Code to send weekly personalized
  updates to every sales rep
source: Claude Blog
url: https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep
model: claude-code/sonnet
generated_at: '2026-08-25T06:17:51.615692'
pinned: true
---

📌 【Anthropic 官方分享】行銷人靠 Claude Code 打造千人專屬週報

TL;DR：Anthropic 行銷團隊用 Claude Code 把一份銷售報告，自動轉成給每位業務員的個人化週一簡報。

每週日晚上熬夜做投影片，換來的卻是業務一句「我沒聽過這個活動」——這是許多行銷人共同的惡夢，也是 Anthropic 行銷團隊成員 Adam Ward 曾經的日常。

🤔 手動彙整報告，跟不上團隊成長速度

Adam Ward 原本每週日晚上彙整全公司的最新進度，做成投影片，週一在站會上口頭報告，再把檔案分享到 Slack。但隨著支援的業務團隊變多，這套流程越來越難維持，因為他不再有時間替每個團隊挑出真正相關的機會，簡報也變得越來越沒有針對性。

🧩 不用會寫程式，但要會講清楚問題

轉機來自一場行銷團隊的 hackathon，Adam 和同事花了一小時聚焦這個問題。他的做法是先用白話向 Claude 說明自己不是工程師，但深知業務問題，請 Claude 把他當成理解商業邏輯的產品經理，一步步協作；他甚至會先錄下自己口頭解釋問題的過程，把逐字稿直接餵給 Claude 補足背景。

具體流程是：
- 先手寫一份「假的」週報當範本，內含業務員最在意的「本週三件優先事項」，例如可以分享給客戶的活動或最新內容。
- 另外準備一份給主管看的彙整版範本，因為主管想看的是整個團隊的全貌，而非單一客戶的細節。
- 透過 MCP 把 Claude 接上 BigQuery（彙整 HubSpot、Clay、Salesforce 資料的公司單一事實來源），從活動與研討會資料開始。
- 為了個人化，讓 Claude 從 CRM 抓出每位業務員負責的客戶名單，並比對 Slack 上的相關客戶動態，交叉比對後生成專屬簡報。之後陸續擴充納入部落格文章、電子書、客戶案例、研討會與合作夥伴生態系的活動資訊。

📊 從 10 人小組測試到全業務團隊上線

Adam 先找一組 10 人的業務團隊測試，願意持續回饋問題。到第一週結束時，prompt 已經累積了九條內容規則，每一條都對應一則真實的使用者回饋。上線後，光是一場高階主管晚宴的邀請，報名人數就在一週內翻倍，原因純粹是對的業務員在週一早上就看到了對的活動資訊。後來業務開發代表（BDR）團隊也想要專屬版本，因為 CRM 中 BDR 與客戶的對應關係跟業務員不同，團隊複製同一套 prompt 架構只調整一個欄位，兩天內就上線；同樣的做法後續也套用到客戶成功與合作夥伴團隊。

💡 使用者回饋才是真正的 prompt engineering

這篇分享最有意思的地方，是把「使用者回饋」直接當成調整 prompt 的依據：
- Claude 曾經在活動缺少連結時，自己編出一個看起來合理但連不到任何頁面的網址，團隊立刻把「絕不捏造網址」寫成硬性規則，連結只有在跟原始資料表逐字相符時才會顯示；後來乾脆把沒有連結的活動整個從簡報中移除，因為業務員無法幫客戶報名的活動只是雜訊。
- 有業務員回報，一場給知識工作者的工作坊被推薦給工程 VP，於是加入了聯絡人職稱與活動受眾的比對機制，不符合就悄悄過濾掉，不特別說明原因。
- 加入「產業別過濾」，避免零售業客戶收到金融業的晚宴邀請；也替還沒有客戶名單的新進業務員準備簡短的歡迎訊息，而非空白簡報。
- 面對來源資料表六週內三次調整欄位順序的現實，團隊把 prompt 從「寫死看 C 欄」改成「先讀表頭、找到寫著活動網址的欄位」，讓流程能適應資料結構變動。

⚠️ 仍保有人工把關的習慣

即便系統已經穩定到 Adam 休假時也能自動寄出週報，他仍然維持「每次都親自看過寄出內容」的習慣，只是流程本身已經不需要等他核准才能發送。

🎯 實務啟示

這個案例對工程師的參考價值，不在於程式碼本身，而在於怎麼把「非技術使用者的回饋」轉譯成可持續維護的 prompt 規則：明確禁止模型捏造資訊、用「找到符合特徵的欄位」取代寫死的欄位定位、把每一條規則都追溯到具體的使用情境。這些原則同樣適用於任何要串接內部資料源、產出個人化內容的 agentic 工作流程設計。

🔗 來源
- 標題：How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep
- 作者／機構：Adam Ward, Anthropic
- 連結：https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep

#ClaudeCode #Anthropic #AIAutomation #MarketingOps #PromptEngineering #AgenticWorkflow #SalesEnablement #MCP #BigQuery #LLMApplications
