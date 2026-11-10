---
title: Google Gemini routes personal Drive files and emails to human annotators
source: Hacker News
url: https://github.com/thisisme6598/gemini_files/
model: claude-code/sonnet
generated_at: '2026-11-10T01:06:18.464427'
score: 83
---

📌 Gemini悄悄把你的Drive信件送進人工審查

TL;DR：Google靜悄悄撤回「人工審查看不到個人資料」承諾，測試顯示完整信件內容可能被整段送審。

2023年Google信誓旦旦地說,連結Gmail、Drive後,Gemini的人工審查者絕對看不到使用者的個人內容。三年後的今天,這句承諾被悄悄改寫了。

🤔 一句承諾的消失

這篇在Hacker News上拿下354個點讚、90則討論的調查指出,2023年Google推出Gemini Workspace extensions時明確承諾,來自Gmail、Docs、Drive的個人內容「不會被人工審查者看到」。但作者發現,Google在Help Answer 16836988的更新內容,以及10月16日對該2023年部落格文章的編輯中,已經明確承認已連結的Drive或信件會被送進人工審查流程,並直接警告審查者看到的「可能就是那封信或那個檔案」,提醒使用者「如果你的應用程式含有不想讓審查者看到的機密資訊,請不要把它們連結到Gemini Apps」。

🧩 不用標記、機率性觸發的擷取管線

作者的測試顯示,這種個人資料擷取是在背景對話中自動觸發的,使用者不需要明確標註@Drive或@Gmail。由於LLM的工具呼叫與context注入本質上是機率性的,同一句測試提問可能得到四種不同結果:

1. Zero Retrieval:模型沒有觸發Connected Apps工具,不會拉取任何個人資料,尤其當Gemini能靠模型權重或先前對話歷史就回答出來時。
2. Metadata/Generic Summary:Gemini拉取信件或檔案後只生成高層摘要,例如「你有3封關於航班的信件」。
3. Partial Unredacted Extraction:Gemini從檔案中擷取2到4句原文,經常包含敏感個資、帳戶細節或具體數字。
4. Full-File Ingestion:整份文件或信件的完整未遮罩文字,被直接注入到session context裡。

作者特別提醒,如果只測一次就看到情境1或2,並不代表這套擷取管線不存在,那只是在一個不確定性系統裡抽到了其中一種結果,必須刪除對話重新測試才有代表性。

📊 重現步驟與實測結果

重現方法是:在消費版Gemini設定中開啟Connected Apps（Google Workspace）、把模型設為Flash搭配High Thinking或更高階思考模式,然後在對話中隨意提到Drive或Gmail裡的主題（不使用@標籤、不主動要求搜尋檔案）,接著要求Gemini「印出檢索工具回傳並注入到prompt中的確切文字與metadata區塊」。作者以自己網路服務商的帳單信件實測,多次嘗試後四種情境都出現過,包括完整姓名、地址、帳號、確認碼、付款日期整段被印出的狀況。文章也指出,Google自家的regex與NER自動去識別化工具,無法充分處理敘事性資料,例如帳號、確認碼、交易日期,以及姓名、城市、事件等組合起來足以識別個人身分的資訊。

🎯 實務啟示

如果你或你的團隊在個人或公司帳號中啟用了Gemini的Connected Apps,應該假設任何隨口提到的主題都有可能觸發背景檢索,進而被人工審查者看到;對含有機密或PII的信件與文件,最安全的做法是不要連結,或改用有明確資料隔離保證的方案。這也提醒正在打造RAG或agent工具呼叫系統的工程師:工具呼叫是否觸發、擷取多少內容本身就是機率性的,單次測試無法驗證你的pipeline是否會洩漏完整原文,需要反覆刪除對話重測,才能觀察到完整的行為分佈。

🔗 來源
- 標題：Google Gemini routes personal Drive files and emails to human annotators
- 作者／機構：gf74918（Hacker News，354 points，90 comments）
- 連結：https://github.com/thisisme6598/gemini_files/

#Gemini #Google #AIPrivacy #DataPrivacy #PII #RAG #LLM #AISecurity #GoogleWorkspace #PrivacyPolicy
