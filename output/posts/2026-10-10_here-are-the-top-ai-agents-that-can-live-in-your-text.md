---
title: Here are the top AI agents that can live in your text messages
source: TechCrunch AI
url: https://techcrunch.com/2026/10/10/all-the-ai-agents-that-can-live-in-your-text-messages/
model: claude-code/sonnet
generated_at: '2026-10-10T20:54:29.689397'
score: 51
---

📌 簡訊就能用的AI代理人：盤點10款直接住進你手機訊息匣的助理

TL;DR：免下載新App，愈來愈多AI代理人直接用iMessage、RCS或WhatsApp傳訊息就能用。

想像一下，你不用再多裝一個App，只要像平常傳訊息給朋友一樣，把事情交代給手機裡的對話框，AI就會記住上下文、串接你原本就在用的服務，然後把事情辦好。這正是目前一批新創公司在搶的賽道，而且其中一家的估值已經衝到100億美元。

🤔 **為什麼大家都想住進你的訊息匣**

比起叫使用者學一套全新介面，「用簡訊操作AI代理人」的優勢很直接：零學習成本、零安裝門檻。這批產品的共同邏輯是：連結使用者既有的信箱、日曆、WhatsApp等服務，自動從雜亂資訊中找出「需要被處理的事」，再透過文字或語音完成預約、提醒、研究、購物等任務。

🧩 **通用型助理：從Instinct到Martin**

- **Instinct**：目前最受矚目的一款，先在9月以10億美元募資把估值推到100億美元。它可透過文字或語音操作，串接Email、日曆、Google Workspace，官方稱使用者已用它規劃旅行、買菜、訂票、取消訂閱。近期更開始為使用者提供專屬Email位址，讓代理人能代為註冊帳號、聯繫商家，但這也引發隱私與安全上的疑慮，目前仍為私測階段。
- **Martin**：走全能助理路線，可透過SMS、電話、WhatsApp、Email、Slack及自家iOS App操作，能代為發訊息、打電話，並提供每日摘要，訂閱價格較高，從每月21美元起。
- **Comma**：強調把任務「做到完」而非只是回應，會自我檢查工作、判斷任務是否完成，並在需要人為決策時才交回使用者審核。可透過Signal、Telegram、WeChat遠端操作，免費且開源。
- **Folk**：透過iMessage、WhatsApp、Telegram操作,運行在自家私有雲端電腦上，能執行程式碼與多步驟任務，免費版之外有每月8.33美元的Pro方案可無限背景任務。
- **Iris**：由Hermes Agent驅動，專注於iMessage內的任務委派，會保留過去互動的上下文並主動回報進度。

🧩 **垂直場景型：家庭與旅遊**

- **Fambot**：定位為家庭「幕僚長」，整合學校通知、運動行程、餐食規劃與日曆，每晚自動發送明日摘要。目前串接Gmail、Google Calendar、Outlook、WhatsApp，Beta期間免費，公司已募得350萬美元前種子輪。
- **Ohai**：同樣主打家庭場景，可透過文字、轉寄Email或語音請求來建立排程與提醒，提供免費方案，付費方案依家庭人數從每月9.99美元起。
- **Ollie**：訴求是把分散在學校訊息、日曆、群組聊天中的資訊整合起來，其最大差異化是已取得SOC 2合規認證，付費方案從每月25美元（150則訊息）到100美元（1000則訊息）不等。
- **Miso**：專注旅遊場景，透過iMessage結合AI行程規劃與真人旅遊團隊支援，可代為安排航班並考量忠誠點數與個人偏好。

📊 **價格與平臺一覽**

| 產品 | 主要管道 | 定位 | 價格 |
|---|---|---|---|
| Instinct | 文字/語音 | 通用助理 | 私測中 |
| Martin | SMS/電話/WhatsApp等 | 通用助理 | 月付21美元起 |
| Comma | Signal/Telegram/WeChat | 工作+生活任務 | 免費、開源 |
| Folk | iMessage/WhatsApp/Telegram | 通用助理 | 免費/月付8.33美元 |
| Fambot | App+SMS | 家庭管理 | Beta免費 |
| Ohai | 文字/語音/Email轉寄 | 家庭管理 | 月付9.99美元起 |
| Ollie | 文字 | 家庭管理 | 月付25美元起 |
| Miso | iMessage | 旅遊規劃 | 未提供 |

💡 **深入分析：便利與風險是一體兩面**

這些產品共同的賣點，是把「代理人」做成使用者原本就會用的通訊介面，降低採用門檻。但正如Instinct讓代理人擁有專屬Email帳號、能自行註冊服務這件事所顯示的，代理人自主性愈高，隱私與安全的治理問題也愈迫切——這也是為什麼Ollie特別把SOC 2合規當作差異化賣點來強調。

⚠️ **目前仍是百花齊放、良莠不齊的階段**

多數產品仍在beta階段，功能邊界、資料存取範圍、安全規範也不盡相同，使用者在串接個人信箱、日曆前仍需評估各家的資料處理方式。

🎯 **實務啟示**

對工程師而言，這個賽道示範了一個明確的產品方向：把代理人的「介面」做到使用者零摩擦（既有的簡訊/通訊App），而把複雜度留在後端的工具串接與記憶管理上。若要評估或打造類似產品，資料存取權限設計與可稽核性，會是比模型能力更早要解決的工程問題。

🔗 **來源**
- 標題：Here are the top AI agents that can live in your text messages
- 作者／機構：Lauren Forristal, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/10/all-the-ai-agents-that-can-live-in-your-text-messages/

#AIAgent #PersonalAssistant #iMessage #ConversationalAI #Startup #ProductivityTools #AIAutomation #TechNews #ConsumerAI #AgenticAI
