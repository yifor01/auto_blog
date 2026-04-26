---
title: "RAG Without Vectors: How PageIndex Retrieves by Reasoning"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/25/rag-without-vectors-how-pageindex-retrieves-by-reasoning/
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-04-26T19:09:28.638978
---

📌 **無向量RAG：PageIndex以推理檢索**

多數RAG系統的檢索模組其實從根上就有設計缺陷。
傳統架構依賴向量相似度匹配，但對財報、法務文件、學術研報這類長專業文檔來說，
最相關的答案往往不在語義最相似的區塊裡，甚至需要跨章節多步推理才能找到。

🤔 **向量相似度是弱代理，無法滿足專業
