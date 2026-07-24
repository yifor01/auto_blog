---
title: Agentic retrieval for Amazon Bedrock Managed Knowledge Base
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agentic-retrieval-for-amazon-bedrock-managed-knowledge-base/
model: tencent/hy3:free
generated_at: '2026-07-24T08:13:46.698015'
score: 98
---

這是一篇針對 AWS 技術部落格內容的轉寫，內容型別屬於「產業新聞／部落格報導」。

---

📌 【AWS 技術解析】面對複雜多重查詢，Agentic Retrieval 如何解決傳統 RAG 的檢索困境？

TL;DR：透過 Agentic Retrieval，Amazon Bedrock 能處理多意圖、對比型等複雜查詢，突破單次檢索的限制。

🎣 **傳統單次檢索（Single-shot Retrieval）在複雜問題面前往往會失靈**

當使用者提出的問題不再是簡單的關鍵字搜尋，而是包含多個部分、需要進行比較或探索性質的複雜問題時，傳統的檢索機制就會遇到瓶頸。例如，當使用者問「請比較 2020 與 2023 年的策略有何不同？」或是「各產品線中最大的三個風險是什麼？」時，這類問題在 Embedding（嵌入）空間中並沒有單一的代表點，傳統的 top-k 檢索往往會回傳一個包含多種衝突子意圖的「平均值」，導致結果缺乏精準度。

🧩 **Agentic Retrieval 的設計理念：從「一次檢索」轉向「規劃與迭代」**

為了應對這類問題，Amazon Bedrock 引入了 Agentic Retrieval 技術。其核心設計理念如下：

- **規劃與迭代**：不同於傳統 Retrieve API 僅執行單次查詢，Agentic Retrieval 會針對問題進行規劃，並針對檢索過程進行多次迭代。
- **整合回應**：它可以在同一個呼叫（Call）中完成檢索規劃並直接生成回應，無需開發者手動拆解問題。

📊 **實測對比：為什麼「最重要訊息」可能檢索到無關內容？**

作者透過一個實際案例展示了標準 Retrieve API 與 Agentic Retrieval 的差異。假設知識庫中包含了 Amazon 25 年的股東信：

- **情境一：直接查詢**
  - 查詢： 「檔案中最重要的訊息是什麼？」
  - 傳統 Retrieve API 結果： 雖然依據 Hybrid Score（混合評分）回傳了五個片段，但 top 1 結果雖然分數高，價值卻極低（僅提到 Amazon 的 Logo 配色方案），其餘片段分別涵蓋招募、開發者與差異化等主題。
  - 失敗原因： 「最重要」這個詞過於模糊，評分機制無法判斷什麼才是真正的「重要」。

- **情境二：複雜多意圖查詢**
  - 查詢： 「比較 Amazon 在 2020 與 2023 年對於招募、長期投資與客戶至上（Customer Obsession）的論述，重點有何轉移？」
  - 挑戰： 單次檢索必須在一個查詢向量（Query Vector）中，同時滿足三個意圖與兩個時間維度。
  - 傳統檢索結果： 通常會導致回傳的片段與問題關聯鬆散，無法精確對應所有維度。

💡 **技術實作：AgenticRetrieveStream API**

針對需要處理複雜邏輯的開發者，AWS 提供了 `AgenticRetrieveStream` API，其重點在於：
- **請求建構**：支援更具結構化的查詢方式。
- **Trace 解析**：開發者可以解析檢索過程的軌跡（Trace），瞭解 AI 是如何拆解問題並進行迭代檢索的。

🎯 **實務啟示：何時該選擇 Agentic Retrieval？**

開發者在選擇 API 時應依據查詢複雜度決定：
- **使用標準 Retrieve API**：當問題目標單一、意圖明確時。
- **使用 Agentic Retrieval**：當使用者問題涉及「比較」、「多重條件」或「探索性主題」時，以提升檢索的精準度與回應的深度。

🔗 **來源**
- 標題：Agentic retrieval for Amazon Bedrock Managed Knowledge Base
- 作者／機構：Omar Elkharbotly @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/agentic-retrieval-for-amazon-bedrock-managed-knowledge-base/

#AWS #AmazonBedrock #RAG #AgenticRetrieval #LLM #MachineLearning #AI #KnowledgeBase #GenerativeAI #CloudComputing
