---
title: Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction
source: BAIR
url: http://bair.berkeley.edu/blog/2026/07/26/abbel/
model: tencent/hy3:free
generated_at: '2026-07-27T09:07:16.458354'
score: 105
---

📌 【BAIR 研究】解決 Context 壓縮困境：ABBEL 框架讓 LLM 能透過「信念狀態」進行長程互動

TL;DR：ABBEL 透過自然語言「信念狀態」取代完整對話歷史，解決傳統摘要壓縮導致的效能落差。

🎣 隨著任務複雜度提升，LLM 必須在數百甚至數千個步驟中與人類協作。然而，當對話歷史不斷堆疊，將整個互動歷程全部塞入 Context（上下文）是不切實際的。

🤔 **摘要壓縮（Compaction）的效能瓶頸**

目前主流的解決方案是「內容壓縮」（Context Compaction），即將歷史紀錄進行摘要。雖然這能縮減長度，但卻帶來嚴重的副作用：
- 即使在基準測試中表現差異看似不大，實務上的模型伺服器（如 Cursor）仍建議使用者在任務中盡量避免使用摘要功能。
- 在 Combination Lock（一種類似 Wordle 的遊戲）的實驗中，即便經過強化學習（RL）微調，使用摘要的模型效能始終無法追上使用「完整對話歷史」的模型。

🧩 **ABBEL：將資訊轉化為「信念狀態」**

為了克服摘要導致的資訊流失，研究者提出了 ABBEL 框架。其核心設計理念如下：
- **取代歷史紀錄**：不再僅是生成一段摘要，而是將「信念狀態」（Belief States）作為 Agent 的工作上下文（Working Context）來取代完整的互動歷史。
- **資訊監督**：透過「信念分級」（Belief Grading）機制，對每個信念狀態的內容進行監督，確保摘要的資訊品質。
- **自然語言表述**：將摘要內容以自然語言形式的信念狀態進行隔離與管理，使資訊更具解釋性且精簡。

🎯 **實務啟示**

對於需要處理長程任務（Long-Horizon Interaction）的 AI 應用（如協作程式碼生成）而言，單純的「內容壓縮」可能不足以維持高精度的任務執行。開發者應關注如何將資訊轉化為結構化且受監督的「信念狀態」，以在縮減 Context 長度的同時，保留關鍵的任務邏輯。

🔗 **來源**
- 標題：Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction
- 連結：http://bair.berkeley.edu/blog/2026/07/26/abbel/

#AI #LLM #MachineLearning #LongHorizonInteraction #BeliefStates #ABBEL #ContextWindow #ArtificialIntelligence #NLP #AIResearch
