---
title: "Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.09891
score: 117
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-11T18:27:05.263099
---

📌 **TREC 2025 RAG Track：從 150 隊參賽者看 RAG 系統的現狀與挑戰**

隨著 ChatGPT、Claude 等大模型席捲全球，「RAG（Retrieval Augmented Generation）」成為 AI 應用開發的核心技術。但你知道嗎？即使是頂尖團隊，在真實長文本查詢上，RAG 系統的表現仍然有極大落差。

🤔 **為什麼長敘述查詢是 RAG 的下一個挑戰？**

TREC 2025 RAG Track 是資訊檢索領域最權威的年度評測賽事，今年吸引超過 150 隊參賽。與去年的初版不同，今年引入了「長、多句子的敘述式查詢」，更貼近人們在處理複雜研究或決策問題時的真實搜尋行為。

🧪 **從 MS MARCO V2.1 到多層次評測框架**

今年評測使用 MS MARCO V2.1 語料庫（1.8B 文字），並採用四層評測標準：

- **相關性評估**：檢查回傳的文檔是否真的與查詢相關
- **回應完整性**：評估生成答案是否涵蓋了查詢的所有面向
- **引用驗證**：確認模型是否正確引用來源文檔
- **一致性分析**：檢查答案內部是否自相矛盾

這套評測框架旨在解決 RAG 系統最頭痛的問題：事實錯誤（hallucination）和不可解釋性。

💡 **長敘述查詢的隱藏難題**

研究發現，當查詢從簡短轉為長敘述（例如從「AI 對醫療的影響」變成「請分析 AI 在醫療領域的應用現狀、挑戰與未來發展，並討論其對醫療從業者職業倫理的影響」），RAG 系統的表現會明顯下降。

主要挑戰包括：

- **語義模糊**：長查詢往往包含多重意圖，難以精準定位關鍵需求
- **上下文丟失**：在多段文檔間切換時，模型容易遺忘初始查詢的細節
- **引用鏈路斷裂**：長答案中，模型可能難以追蹤每個事實的原始出處

⚠️ **評測揭示的現實差距**

從初步結果來看，即使是表現優異的系統，在長敘述查詢上的相關性得分也比簡短查詢低 15-20%。更嚴重的是，高達 30% 的答案存在某種程度的事實錯誤或不當引用。

🎯 **對開發者的啟示**

如果你正在開發 RAG 應用，這項研究告訴我們：

- 簡短查詢的 RAG 系統已經相當成熟，但長文本處理仍是短板
- 僅提升檢索準確度是不夠的，生成模組的推理能力同樣關鍵
- 透明度和可解釋性將成為 RAG 系統的核心競爭力

🔗 **論文連結**
📝 Overview of the TREC 2025 Retrieval Augmented Generation (RAG) Track
👤 Shivani Upadhyay, Nandan Thakur, Ronak Pradeep, Nick Craswell, Daniel Campos
🏫 University of Waterloo; Microsoft; Zipf AI; National Institute of Standards and Technology
🔗 論文：arxiv.org/abs/2603.09891

你開發的 RAG 系統在處理長文本查詢時表現如何？歡迎分享你的經驗 👇

#RAG #TREC #資訊檢索 #AI應用 #大語言模型 #事實驗證 #資訊檢索 #TREC2025
