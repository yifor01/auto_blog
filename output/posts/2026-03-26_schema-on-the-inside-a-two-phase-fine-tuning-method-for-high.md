---
title: "Schema on the Inside: A Two-Phase Fine-Tuning Method for High-Efficiency Text-to-SQL at Scale"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.24023
score: 109
model: gpt-4o-free
generated_at: 2026-03-26T19:42:55.931629
---

📌 【Sporta Technologies 最新研究】用 8B 模型大幅提升 Text-to-SQL 效率，輕鬆省下 99% Token 成本！

你是否也在為 Text-to-SQL 應用中的高成本與延遲問題頭痛？當長達 17,000 Token 的 Schema 重到無法負擔，印度最大夢幻體育平台 Dream11 的團隊提出了一個大膽的解法——讓模型「記住」整個資料庫結構，徹底擺脫長提示詞的限制！

🎣 **17k Token 提示詞？現在只需要不到 100！**

在 Text-to-SQL 應用中，開發者通常需要將龐大的資料庫 Schema 作為提示詞傳入大型語言模型。這不僅導致每次 API 調用的成本居高不下，還因延遲過高而無法大規模部署。

Sporta Technologies 的研究團隊找到了解決方案：通過兩階段的特殊微調方法，讓一個 80 億參數的模型能「內化」整個資料庫結構，完全不需要長提示詞。結果是：

- Token 輸入量減少 **99%**（從 17,000 減到不到 100）
- 不再依賴昂貴的外部 API，改用高效的本地推論

🤔 **Text-to-SQL 的大規模部署挑戰**

這項研究針對的是 CriQ，一個專為印度夢幻體育平台 Dream11 開發的應用程式，旨在回答用戶對板球數據的提問。Dream11 擁有超過 2.5 億用戶，這意味著任何解決方案都需要能夠應對大規模的查詢負載，同時保證高精度和低延遲。

🧪 **兩階段微調：內化 Schema 的關鍵技術**

研究團隊設計了一種兩階段的監督式微調方法，具體細節如下：

1. **第一階段**：讓模型學會資料庫 Schema 的結構，理解表與欄位的關係。
2. **第二階段**：在特定應用場景下進一步微調，提升模型對自然語言查詢的理解力。

這種方法不僅讓模型能夠充分「記住」資料庫的結構，還能在不依賴外部 API 的情況下，執行高效的本地推論。

🎯 **結果：更快、更準、更省錢**

研究結果顯示，這套系統不僅在成本與效能上表現出色，還在準確度上全面超越基準模型：

- **執行成功率**：98.4%（優於 Gemini Flash 2.0 的 95.6%）
- **語義準確率**：92.5%（優於 Gemini Flash 2.0 的 89.4%）

這些數據證明，內化資料庫 Schema 的方法不僅是可行的，還能顯著提升 Text-to-SQL 的效能。

⚠️ **研究限制：僅針對單一應用場景**

雖然這項研究在 CriQ 應用中取得了極高的效能，但研究範圍限於板球數據查詢，對其他類型資料庫的通用性仍需進一步驗證。

🎯 **實務啟示：擺脫長提示詞，專注本地化模型**

對於希望部署 Text-to-SQL 系統的工程師來說，這篇研究提供了關鍵啟示：

- 長提示詞成本高昂且不具可擴展性，讓模型內化 Schema 是更優的選擇。
- 自主部署的專用模型可以顯著降低成本，同時提升效能。
- 使用微調方法針對特定應用場景進行優化，能有效提升準確率。

🔗 **論文連結**
📝 Schema on the Inside: A Two-Phase Fine-Tuning Method for High-Efficiency Text-to-SQL at Scale  
👤 Chinmay Soni, Shivam Chourasia, Gaurav Kumar, Hitesh Kapoor @ Sporta Technologies Private Limited  
🔗 論文全文：https://arxiv.org/abs/2603.24023

你對這種內化 Schema 的方法有什麼看法？是否考慮在你的專案中採用類似的技術？歡迎留言討論！👇

#AI #TextToSQL #人工智慧 #資料庫 #模型微調 #Dream11 #LLM #技術效率
