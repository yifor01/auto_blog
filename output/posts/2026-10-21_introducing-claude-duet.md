---
title: Introducing Claude Duet
source: Claude Blog
url: https://claude.com/resources/articles/claude-duet
model: claude-code/sonnet
generated_at: '2026-10-21T20:50:49.003856'
score: 110
---

📌 Anthropic推出Claude Duet：主動幫你盯著待辦事項的agent

TL;DR：Claude Duet是Anthropic新推出的主動式agent應用，會主動彙報、背景工作、關鍵動作前才找你確認。

大多數AI助手還在等你開口下指令，Claude Duet想做的事情正好相反：它會先盯著你連接的帳號，主動決定什麼事該讓你知道，什麼事可以自己處理完再跟你報告。

🤔 多數AI助手等你開口，Claude Duet反過來主動盯著你

Anthropic把Claude Duet定位給每天要處理的決定比能追蹤的還多的專業人士與小企業主。它以Claude Opus 5.5為核心，目前以研究預覽的形式開放，提供獨立的iOS、Android App以及claude.ai網頁版，涵蓋在Pro與Max方案內，用量計入既有方案額度，目前須透過候補名單申請使用。

🧩 早報、背景執行、關鍵動作才找你核准

Claude Duet每天早上會針對所有已連接的App，整理出一份最重要事項的簡短早報；接下來一天則持續追蹤這些帳號，只有在真的需要你注意時才發訊息。Anthropic表示，持續不間斷地檢查會太快耗盡方案額度，因此目前的檢查頻率是每幾個小時一次，使用者也可以指定想收到哪些類型的通知與頻率。

它延續你在Claude帳號裡既有的記憶、skills與已連接的App，設定成本很低；差別在於互動方式變成一個持續的對話串，無論是一句簡單的回覆還是一個長達一週的專案，都從同一個地方開始。由於Claude Duet擁有自己的虛擬機與瀏覽器，執行任務不需要你的手機或電腦保持開機，任務完成或需要你確認時才會收到通知。

任務範圍從排會議這類行政工作，到建立涵蓋數十種工具的儀表板、財務或銷售預測、prototype與網頁應用開發都可以交辦。但真正關鍵的決定仍保留在人類手上：在發送訊息、付款、簽署文件或刪除任何東西之前，Claude Duet會先展示它即將執行的具體動作，等你核准才會真正執行；交易證券、帳戶間轉帳這類動作則是即使核准也完全不允許執行，使用者也可以隨時解除任何已連接的App授權。

🔒 安全機制全部沿用既有的agent信任框架

Claude Duet的安全機制並非從零打造，而是直接沿用Anthropic既有的多項基礎設施：整體遵循Anthropic的可信任agent框架，與Claude Code、Claude in Chrome共用同一套設計準則；憑證處理方式沿用Claude Managed Agents的設計，Claude Duet本身不會直接看到使用者的密碼或登入token；每個動作都要經過auto mode classifier審核，這與保護Claude和Claude Code不做出使用者未要求動作的安全機制相同；防範隱藏指令與prompt injection的能力，來自Anthropic的browser-use研究成果。Anthropic也針對Claude Duet進行了紅隊測試與外部機構的滲透測試，並已納入公開的bug bounty計畫。

此外，Claude Duet另外搭配一套新的專用classifier與安全系統提示詞，會檢查每一則訊息，防止敏感資訊外流：信用卡號、政府身分證件等最高敏感等級資訊一律拒絕分享；健康或個人財務等其他敏感資訊，則只有在使用者明確指示的情況下才會被放行。

🔌 透過6000+連接器串進Gmail、QuickBooks、Shopify

Claude Duet可以透過Claude Marketplace超過6,000個連接器與外掛，處理像是在Gmail、Slack找出未讀訊息並協助回覆、檢查QuickBooks或Stripe中未付款的發票並草擬提醒信、在Gusto中準備並執行含工時獎金的payroll、草擬職缺貼文並在使用者編輯核准後發布到LinkedIn、透過Docusign準備並送出待簽署的合約、根據HubSpot的聯絡與交易紀錄草擬後續追蹤信，以及在Canva、Shopify上製作行銷活動與管理商店等工作。它也能透過Stripe的數位錢包Link代為採購，過程中會先與使用者確認商品，並由Link請求核准支出後以虛擬卡付款，不會透露使用者的真實卡號；也支援透過Shopify的Shop Pay完成線上結帳。

💡 內部團隊與小企業主怎麼用它

Anthropic提到，負責Claude Code團隊的Boris Cherny會在散步時把待辦清單口述給Claude Duet；負責模型與產品行為設計團隊的Chelsea Larsson會在下班前把待辦事項交給它，當晚取得彙整報告；Claude Duet團隊負責人Karan Ahuja則用它安排使用者訪談、協作prototype，甚至直接出程式碼。

早期取得存取權的小企業主也分享了實際案例：房仲Jess Provencher提到，Claude Duet曾在沒被要求的情況下，主動發現行事曆上一場賞屋排錯了日期；在南佛羅裡達擁有約110名員工的Shahs of Kabob老闆Amin Ebrahimi，用它處理記帳、客服與行銷，逐店核對發票；品牌策略顧問Mya Dalton則提到，Claude Duet注意到她某通電話剛好排在航班起飛前，主動提議幫忙改期。

⚠️ 仍是研究預覽，判斷邏輯還在調整

目前Claude Duet仍是研究預覽階段，檢查頻率、何時該主動通知的判斷邏輯，Anthropic表示都還在持續測試與調整中，須透過候補名單才能取得存取權限。

🎯 憑證隔離與敏感資訊分級，是值得參考的安全架構範本

對經常需要串接多個SaaS工具、處理重複性行政工作的團隊來說，Claude Duet把背景執行加關鍵動作才找人核准的agent互動模式做成了產品化的預設行為，值得關注它在憑證隔離與敏感資訊分級放行上的具體設計，這對自建企業內部agent系統的工程團隊也是一份可以參考的安全架構清單。

🔗 來源
- 標題：Introducing Claude Duet
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/claude-duet

#ClaudeDuet #Anthropic #ClaudeOpus #AIAgent #AgenticAI #ProductivityTools #AIForBusiness #PromptInjection #AgentSafety #ClaudeCode
