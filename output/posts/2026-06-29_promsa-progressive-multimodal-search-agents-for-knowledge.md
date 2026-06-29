---
title: ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question
  Answering
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.27974
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:27:59.264077'
---

📌 ProMSA：透過漸進式多模態搜尋代理，解決知識型視覺問答挑戰

TL;DR：ProMSA 透過自適應選擇搜尋策略與序列層級強化學習，提升知識型 VQA 的回答精準度。

在處理知識型視覺問答（Knowledge-Based Visual Question Answering, KB-VQA）時，模型不僅需要理解影像，還必須在海量外部知識中精準定位答案。單一的搜尋策略往往難以應對不同複雜度的問題，如何讓 AI 能像人類一樣「根據情況調整搜尋方式」成為核心挑戰。

🤔 **KB-VQA 的搜尋策略僵化問題**

傳統的視覺問答系統在獲取外部知識時，通常採取固定的檢索流程。然而，不同型別的問題對搜尋的需求不同，若能根據問題的特質自適應地選擇搜尋策略，將能更有效地過濾雜訊並找到關鍵資訊。

🧩 **ProMSA 的漸進式搜尋與強化學習機制**

為了克服上述問題，ProMSA 提出了一套漸進式多模態搜尋代理（Progressive Multimodal Search Agents）架構，其核心設計包含：

- **自適應策略選擇**：代理能根據目前的狀態，動態選擇最適合的搜尋策略，而非執行單一的固定流程。
- **序列層級強化學習 (Sequence-level RL)**：利用強化學習對整個搜尋序列進行最佳化，讓模型學習如何透過一系列的步驟（Step-by-Step）最終達成正確的回答。

🎯 **實務啟示**

對於開發 VQA 系統的工程師而言，ProMSA 的設計理念顯示出「動態檢索」比「靜態檢索」更具潛力。在實作 RAG（檢索增強生成）系統時，嘗試將「搜尋路徑」視為一個可最佳化的序列，並引入強化學習來調整檢索策略，可能是提升複雜問答效能的有效方向。

🔗 **來源**
- 標題：ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question Answering
- 連結：https://huggingface.co/papers/2606.27974

#VQA #Multimodal #ReinforcementLearning #KnowledgeBasedVQA #SearchAgents #AI #MachineLearning #ComputerVision #InformationRetrieval #ProMSA
