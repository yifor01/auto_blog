---
title: 'Liquid AI Introduces LFM2.5-Embedding-350M and LFM2.5-ColBERT-350M: Dense
  Bi-Encoder and Late-Interaction Models for Fast Multilingual Search Across 11 Languages'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/19/liquid-ai-introduces-lfm2-5-embedding-350m-and-lfm2-5-colbert-350m-dense-bi-encoder-and-late-interaction-models-for-fast-multilingual-search-across-11-languages/
score: 79
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:43:03.914379'
---

📌 【Liquid AI】推出 LFM2.5 檢索模型：350M 參數支援 11 國語言高效搜尋

TL;DR：Liquid AI 發布兩款 350M 參數的雙向編碼模型，提供單向量與多向量兩種選擇，優化多國語言檢索效能。

在 RAG（檢索增強生成）管線中，如何在「檢索速度」與「精準度」之間取得平衡？Liquid AI 最新推出的兩款模型 LFM2.5-Embedding-350M 與 LFM2.5-ColBERT-350M，試圖透過輕量化的 350M 參數規模，為 11 種語言的跨語言搜尋提供低成本且高效的解決方案。

🧩 **從 Causal Decoder 轉向雙向編碼的架構調整**

這兩款模型皆基於 3 月發布的 LFM2.5-350M-Base 基礎模型開發。為了將原本適合「由左至右生成」的因果解碼器（Causal Decoder）轉化為適合「檢索」的雙向編碼器（Bidirectional Encoder），Liquid AI 採取了以下技術修改：

- **Attention Mask 替換**：將原有的 Causal Attention Mask 替換為雙向遮罩，使每個 token 能同時關注左側與右側的上下文。
- **卷積層非因果化**：將 LFM2 的短卷積（short convolutions）改為非因果模式，讓局部資訊在每個 token 周圍對稱地混合，而非僅從過去資訊獲取。

這種設計在保留 LFM2 骨幹效率的同時，使其能更自然地處理檢索任務。

🤔 **單向量 vs 多向量：根據需求選擇索引方案**

雖然兩者共享相同的骨幹架構，但在文本表示方式上完全不同，工程師可依據儲存成本與精準度需求選擇：

- **LFM2.5-Embedding-350M (Dense Bi-Encoder)**
  - **機制**：將整個文件壓縮為單一向量。
  - **優勢**：搜尋速度最快，索引空間最小且成本最低。
- **LFM2.5-ColBERT-350M (Late-Interaction Model)**
  - **機制**：將每個 token 分別轉換為向量，實現字對字的匹配。
  - **優勢**：更高的精準度與更強的泛化能力。
  - **限制**：索引體積較大，查詢長度上限為 32 個 token。
  - **額外功能**：可在不建立索引的情況下，直接對第一階段檢索的結果進行重排序（Rerank）。

📊 **適用場景與部署特性**

由於模型規模僅 350M，記憶體占用極低，幾乎可以在任何環境運行。這兩款模型特別針對「短上下文搜尋」進行優化，最適合的應用場景包括：
- 產品目錄（Product Catalogs）
- FAQ 知識庫
- 客服支援文件（Support Docs）

Liquid AI 將其定位為既有 RAG 管線的「直接替換方案」（drop-in replacement），旨在簡化多國語言搜尋的部署流程。

🎯 **實務啟示**

對於開發者而言，這組模型的價值在於提供了明確的權衡選擇：若專案優先考量成本與延遲，應選擇 Embedding 版本；若對檢索精準度有極高要求且能承受較大的儲存開銷，則 ColBERT 版本是更好的選擇。此外，ColBERT 版本的重排序功能可讓工程師在不大幅更改架構的前提下，快速提升 RAG 的首階段檢索品質。

🔗 **來源**
- 標題：Liquid AI Introduces LFM2.5-Embedding-350M and LFM2.5-ColBERT-350M: Dense Bi-Encoder and Late-Interaction Models for Fast Multilingual Search Across 11 Languages
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/06/19/liquid-ai-introduces-lfm2-5-embedding-350m-and-lfm2-5-colbert-350m-dense-bi-encoder-and-late-interaction-models-for-fast-multilingual-search-across-11-languages/

#LiquidAI #RAG #Embedding #ColBERT #MultilingualSearch #InformationRetrieval #NLP #OpenSource #MachineLearning #BiEncoder
