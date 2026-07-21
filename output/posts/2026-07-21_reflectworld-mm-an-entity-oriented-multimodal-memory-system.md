---
title: 'ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended
  Video Streams'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.09759
score: 97
model: tencent/hy3:free
generated_at: '2026-07-21T08:29:47.519322'
---

📌 【新論文】ReflectWorld-MM：以實體為核心，讓 AI 助手能持續觀察並理解世界

TL;DR：ReflectWorld-MM 透過實體導向記憶架構，在六項長影片與終身學習基準測試中取得最佳表現。

當 AI 助手開始「持續觀察」世界時，它們該如何處理源源不絕的視覺資訊？目前的系統大多將記憶儲存在模型上下文（Context）或扁平的特徵庫（Feature Store）中，並以「影格（Frames）」為單位進行組織。然而，真實世界的影片流（Video Streams）本質上是由「實體（Entities）」構成的，這種以影格為中心的記憶方式限制了 AI 對重複出現之物件的追蹤能力。

🧩 **以實體為核心的層次化記憶架構**

為了克服現有系統無法有效追蹤「誰」或「什麼」在時間長河中重複出現的限制，ReflectWorld-MM 提出了以實體為導向的多模態記憶系統，其架構包含三個核心部分：

1.  **感知前端（Perception Front-end）**：將音視覺流（Audio-visual stream）轉換為經過實體解析的觀察結果（Entity-resolved observations），並儲存在受限的短期記憶中。
2.  **層次化長期記憶（Hierarchical Long-term Memory）**：借鑒人類記憶理論設計，結合了三個維度：
    *   多尺度情節記憶（Multi-scale episodic memory）。
    *   不斷演進的以實體為中心的語義記憶（Evolving entity-centric semantic memory）。
    *   程式性記憶（Procedural memory）。
3.  **完整實作方案（Complete Realization）**：專為實際操作設計，能夠接收任意串流並與現有的助手（Assistants）進行整合。

📊 **橫掃六項基準測試，取得最佳準確度**

在針對長影片（Long-video）與終身學習（Lifelong memory）設計的六項基準測試中，ReflectWorld-MM 在所有測試專案中均達成了最高準確度，表現優於強大的記憶代理人（Memory agents）以及現有的前沿模型（Frontier model）。

🎯 **實務啟示**

對於開發長時程多模態代理人的工程師而言，ReflectWorld-MM 提供了一個關鍵的設計範式：將記憶從「影格層級」提升到「實體層級」，這對於需要處理連續不斷、且包含重複出現物件的複雜環境（如機器人視覺或長影片分析）具有重要的參考價值。

🔗 **來源**
- 標題：ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams
- 連結：huggingface.co/papers/2607.09759

#AI #Multimodal #ComputerVision #MemorySystem #LongTermMemory #VideoUnderstanding #MachineLearning #ArtificialIntelligence #EntityCentric #Research
