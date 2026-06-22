---
title: 'SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document
  RAG'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.18381
score: 92
model: google/gemma-4-31b-it:free
generated_at: '2026-06-22T21:04:11.833457'
---

📌 SproutRAG：利用注意力引導與漸進式嵌入，突破長文本 RAG 檢索瓶頸

TL;DR：透過學習句子間的 attention 建立層次化結構，實現無需額外 LLM 呼叫的多粒度長文檢索。

面對長文本 RAG 時，工程師常面臨兩難：切分太細會失去上下文語義，切分太粗則會引入過多雜訊且浪費 Token。目前的常見做法是依賴 LLM 進行摘要或預先分層，但這會大幅增加運算成本與延遲。

🤔 **擺脫對 LLM 摘要的依賴**

SproutRAG 提出了一種層次化檢索增強生成框架，其核心目標是在不增加額外 LLM 呼叫或預先摘要的情況下，將句子級別的切片（sentence-level chunks）組織成具有語義連貫性的單位。

🧩 **以注意力機制建構層次化結構**

SproutRAG 的技術路徑在於將「層次化」的過程轉化為可學習的表示問題：

1. **學習句子間注意力**：利用 learned inter-sentence attention 來分析句子之間的關係。
2. **漸進式嵌入（Progressive Embeddings）**：透過這種注意力引導，將細粒度的句子逐步聚合為更高層級的語義單位。
3. **多粒度檢索**：這種結構允許系統在不同粒度（從單句到較大的語義單元）之間進行檢索，從而精準定位長文本中的關鍵資訊。

💡 **對 RAG 流程的效能最佳化**

相較於傳統的 RAG 流程，SproutRAG 的設計帶來了兩個關鍵改變：
- **降低成本**：因為組織層次結構是透過 Embedding 與 Attention 達成，而非呼叫 LLM 進行摘要，大幅降低了前處理的成本。
- **保持語義連貫**：透過學習句子間的關聯，檢索到的內容不再是破碎的片段，而是具有語義連貫性的單位。

🎯 **實務啟示**

對於處理大量長檔案（如法律合約、技術手冊）的工程師來說，SproutRAG 提供了一種新的思考方向：層次化索引不一定要靠「人工定義規則」或「LLM 摘要」，透過學習 Embedding 之間的注意力關係，可以在檢索階段就兼顧「精準度」與「上下文完整性」。

🔗 **來源**
- 標題：SproutRAG: Attention-Guided Tree Search with Progressive Embeddings for Long-Document RAG
- 連結：https://huggingface.co/papers/2606.18381

#RAG #LongDocument #Attention #Embedding #InformationRetrieval #NLP #LLM #HierarchicalRetrieval #SemanticSearch #SproutRAG
