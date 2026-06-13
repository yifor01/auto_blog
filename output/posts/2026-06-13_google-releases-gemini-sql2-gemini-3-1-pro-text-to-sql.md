---
title: 'Google Releases Gemini-SQL2: Gemini 3.1 Pro Text-to-SQL Scores 80.04% on BIRD
  Single-Model Leaderboard'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/12/google-releases-gemini-sql2-gemini-3-1-pro-text-to-sql-scores-80-04-on-bird-single-model-leaderboard/
score: 80
model: google/gemma-4-31b-it:free
generated_at: '2026-06-13T19:38:57.746528'
---

📌 【Google 最新研究】Gemini-SQL2 拿下 BIRD 榜單：讓自然語言轉 SQL 的「執行準確率」突破 80%

當我們在對話視窗輸入「請幫我分析上季營收最低的產品線」時，AI 生成的 SQL 語法看起來很正確，但實際執行時卻報錯，或回傳了錯誤的數據？這就是 Text-to-SQL 領域中最令人頭痛的「執行準確率 (Execution Accuracy)」問題。

🤔 **SQL 語法「看起來對」並不等於「跑得對」**

在 Text-to-SQL 的開發中，許多模型能生成符合語法的 SQL，但在面對複雜的商業邏輯、髒數據（Dirty Values）或需要外部知識對齊時，往往會失效。Google Research 團隊意識到，數據的細微差異與複雜的業務情境，使得從自然語言生成精準 SQL 成為極具挑戰的任務。

為了突破這個瓶頸，Google 推出了基於 Gemini 3.1 Pro 的新能力：Gemini-SQL2。

🧪 **在 BIRD 基準測試中挑戰極限**

為了驗證能力，Google 使用了業界標準的 BIRD (BIg Bench for LaRge-scale Database Grounded Text-to-SQL Evaluation) 進行測試。這個基準測試比早期的 Spider 更嚴苛，其特點包括：
- **規模龐大**：包含 95 個資料庫、37 個專業領域，總計 12,751 組問題-SQL 對。
- **真實環境**：資料庫包含真實世界的髒數據，且要求模型必須具備外部知識對齊能力。
- **嚴格指標**：衡量的是「執行準確率 (EX)」，也就是生成的 SQL 必須能成功執行，且回傳結果與標準答案完全一致。

🧪 **單一模型表現突破 80.04%**

Gemini-SQL2 在 BIRD 的「單一模型軌道 (Single Model Track)」取得了 80.04% 的執行準確率，超越了先前由 Google 紀錄的最高分。

值得注意的是，這個「單一模型軌道」限制了預處理、檢索 (Retrieval) 或 Agent 框架的輔助，這意味著這次的提升是來自於 Gemini 3.1 Pro 核心的 Text-to-SQL 理解能力提升，而非依賴外部框架的堆疊。

💡 **從「生成語法」進化到「執行就對」**

這次更新的核心洞察在於：Gemini-SQL2 產出的是 Google 所定義的「執行就緒 (Execution-ready)」查詢。這代表模型在理解自然語言與資料庫 Schema 之間的映射關係上有了顯著進步，能更精準地處理複雜的商業上下文，減少開發者在後端進行手動修正的成本。

⚠️ **這是一項能力更新，而非獨立模型發布**

需要釐清的是，Gemini-SQL2 並非一個全新的獨立基礎模型 (Foundation Model)，而是一種基於 Gemini 3.1 Pro 的特定能力增強。目前 Google 尚未正式確認哪些產品將優先導入此項能力，但根據其對「提升 Google 數據服務自然語言能力」的描述，預計將整合至 BigQuery Studio、AlloyDB AI 或 Cloud SQL Studio 等現有產品中。

🎯 **對資料工程師的實務啟示：減少 Prompt 調整的心力**

對於正在構建 NL-to-SQL 管線的工程師來說，這次的進步意味著：
- **降低對複雜 Agent 框架的依賴**：如果單一模型的執行準確率提升，我們可能不需要設計過於複雜的檢索與自我修正 (Self-correction) 迴路。
- **提升端到端體驗**：對於非技術用戶，從「輸入問題」到「獲得正確數據」的路徑更短，減少了因 SQL 報錯而導致的用戶挫折感。

🔗 **相關資訊**
📝 Gemini-SQL2: Gemini 3.1 Pro Text-to-SQL Scores 80.04% on BIRD Single-Model Leaderboard
👤 Asif Razzaq (MarkTechPost)
🔗 詳情：https://www.marktechpost.com/2026/06/12/google-releases-gemini-sql2-gemini-3-1-pro-text-to-sql-scores-80-04-on-bird-single-model-leaderboard/

你目前在實作 Text-to-SQL 時，最常遇到的問題是語法錯誤還是邏輯錯誤？歡迎在評論區分享你的經驗 👇

#Google #Gemini #TextToSQL #BigQuery #DataEngineering #LLM #BIRDBenchmark #AI
