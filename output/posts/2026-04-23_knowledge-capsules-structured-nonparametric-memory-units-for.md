---
title: "Knowledge Capsules: Structured Nonparametric Memory Units for LLMs"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.20487
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:39:05.630811
---

📌 【浙大系團隊】知識膠囊，解決 RAG 穩定性痛點

RAG 技術雖然解決了 LLM 的知識更新問題，但在處理長上下文或多跳推理時，塞進去的文本往往會在注意力機制中「打架」，導致結果不穩定。有沒有可能讓外部知識不再只是「上下文」，而是直接參與模型思考？

🤔 **RAG 的痛點：知識在注意力機制中競爭**

現行的檢索增強生成（RAG）技術，本質上是將外部知識以文本形式堆疊在輸入端。這種做法只是單純的上下文擴充，當文件變長或需要多步推理時，這些外部 Token 會與模型內部的原始 Token 競爭注意力資源，導致知識的影響力間接且脆弱。

🧪 **知識膠囊：結構化的非參數記憶單元**

來自浙江 Angel Medical AI 等機構的研究團隊提出了 Knowledge Capsules（知識膠囊）。這是一種結構化的非參數記憶單元，用於表示規範化的關聯知識。關鍵在於，這些膠囊可以直接從文檔語料庫構建，且不需要訓練基座模型。

 **KVI 框架：直接注入 KV 快取**

這篇論文的核心創新在於 External Key Value Injection (KVI) 框架。不同於 RAG 注入文本，KVI 將知識膠囊編譯成與注意力機制兼容的 Key-Value 表示，讓外部知識直接參與模型的注意力計算。這將知識整合從「上下文層級的擴充」轉變為「記憶層級的互動」。

💡 **全面超越 RAG 與 GraphRAG**

在多個 QA 基準測試中，Knowledge Capsules 展現了顯著的優勢：
- 在長上下文與多跳推理場景下，準確度與穩定性均優於 RAG。
- 效能甚至超越了 GraphRAG。
- 實現了這一切，卻完全不需要更新模型參數。

💡 **從參數記憶到動態記憶的轉變**

LLM 將知識編碼在參數權重中，更新成本極高。Knowledge Capsules 提供了一種新的思路：將知識模組化、結構化，並以非參數的形式存在。這不僅解決了更新難題，更透過直接介入注意力計算，避免了資訊在長文本傳遞中的衰減。

⚠️ **技術門檻與適用場景**

雖然無需微調模型，但構建高質量的「知識膠囊」需要對文檔語料進行結構化處理。此外，目前的評測主要集中在 QA 任務上，對於更複雜的開放式生成任務，其效果仍有待觀察。

🎯 **工程師的新武器**

對於需要頻繁更新知識庫或處理複雜邏輯推理的應用場景，KVI 框架提供了一個極具潛力的替代方案。它讓模型在不改變權重的情況下，獲得更穩定的外部知識獲取能力。

🔗 **論文連結**
📝 Knowledge Capsules: Structured Nonparametric Memory Units for LLMs
👤 Bin Ju, Shenfeng Weng, Danying Zhou, Kunkai Su, Rongkai Xu
🏢 Zhejiang Angel Medical AI Technology Co., Ltd.; Miti AI Technology Co., Ltd.; 等
🔗 論文：https://arxiv.org/abs/2604.20487

你覺得這種「直接注入 KV」的方式，會是下一代 RAG 的標準嗎？歡迎留言討論 👇

#LLM #RAG #KnowledgeGraph #AIResearch #NLP #MachineLearning #知識工程
