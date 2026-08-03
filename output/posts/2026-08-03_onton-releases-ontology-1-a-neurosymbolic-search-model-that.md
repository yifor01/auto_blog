---
title: 'Onton Releases Ontology 1: A Neurosymbolic Search Model That is 2.7x More
  Accurate than the World’s Best E-commerce Search Engines'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/02/onton-releases-ontology-1-a-neurosymbolic-search-model/
model: tencent/hy3:free
generated_at: '2026-08-03T09:08:43.614170'
score: 92
---

📌 【Onton 新技術】超越 Google 與 Amazon：神經符號模型 Ontology 1 重新定義電商搜尋

TL;DR：Onton 推出 Ontology 1 神經符號模型，在複雜搜尋任務中表現優於 Google Shopping 與 Amazon。

面對日益複雜的對話式與多模態產品搜尋需求，傳統電商搜尋正遭遇瓶頸。當使用者搜尋「適合寵物的沙發」時，傳統系統往往只能依賴賣家標籤，但如果賣家沒寫，搜尋結果就會大打折扣。

🤔 **打破傳統標籤限制：從屬性推理而非單純比對**

目前的電商介面大多依賴類別與屬性（如尺寸、價格、品牌），但缺乏對「功能性需求」的理解。Onton 提出的 Ontology 1 採取了不同的路徑：

- **不盲信賣家標籤**：當搜尋「寵物友善」時，模型不會僅看標籤，而是從更具客觀性的屬性（如纖維材質、織法、結構）進行推理。
- **建立可檢視的世界模型**：模型並非僅將模式吸收進權重中，而是建立一個明確且可檢視的世界模型。
- **持續自我學習**：當模型發現「寵物友善」是一個知識缺口時，它會透過「易清潔性」、「耐用性」與「聚酯纖維材質」來推導答案，並將此邏輯應用於後續類似的查詢中。

📊 **實驗結果：在複雜查詢中大幅領先主流引擎**

研究團隊透過 Subtext-Decor-90 基準測試，使用三個獨立的 LLM 裁判（Claude Opus 4.8、Gemini 3.1 Pro 與 GPT-5.5）對 90 個查詢進行評分。

**平均 Precision@10 (P@10) 表現對照：**

| 搜尋引擎 | 平均 P@10 | 註解 |
| :--- | :--- | :--- |
| **Onton (Ontology 1)** | **0.630** | 僅索引約 1% 的目錄 |
| Google Shopping | 0.543 | |
| Amazon | 0.469 | |

*註：排除空值後的結果顯示，Onton 的 P@10 為 0.665，優於 Google (0.549) 與 Amazon (0.459)。*

雖然在某些特定功能性查詢（如「不會吵醒伴侶的燈」）上，Amazon 憑藉龐大的目錄廣度仍佔有優勢，但 Onton 認為其自我學習迴圈將逐步縮小此差距。

🧩 **技術架構：高效能的知識圖譜 Ograph**

Ontology 1 的知識圖譜運行於自研的圖資料庫 Ograph 上。根據 Onton 提供的數據，其效能表現驚人：

- **CPU 版本**：單核吞吐量約為 SuiteSparse:GraphBLAS 的 100 倍。
- **GPU 版本**：比 CPU 版本快 43 倍，在優化實作下，效能甚至能達到 CPU 版的 1000 倍。

⚠️ **目前僅限合作夥伴使用**

雖然技術表現強勁，但 Ontology 1 目前並非開源專案。它沒有公開的 API、定價方案或可下載的模型權重。目前 Onton 採用的模式是針對「建構代理型網路 (Agentic Web) 的團隊」進行個別案例的合作開發。

🎯 **實務啟示**

對於正在開發 AI Agent 或複雜搜尋功能的工程師來說，Ontology 1 展示了「神經符號 (Neurosymbolic)」結合「自我學習迴圈」的潛力。當模型不再只是模仿模式，而是學會透過底層屬性來「推理」缺失的標籤時，搜尋的精準度將會有質的飛躍。

🔗 **來源**
- 標題：Onton Releases Ontology 1: A Neurosymbolic Search Model That is 2.7x More Accurate than the World’s Best E-commerce Search Engines
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/02/onton-releases-ontology-1-a-neurosymbolic-search-model/

#AI #MachineLearning #Neurosymbolic #SearchEngine #Ecommerce #Onton #Ontology1 #KnowledgeGraph #LLM #AIResearch
