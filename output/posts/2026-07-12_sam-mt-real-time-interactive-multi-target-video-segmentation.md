---
title: 'SAM-MT: Real-Time Interactive Multi-Target Video Segmentation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.08688
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-12T08:05:17.833476'
---

📌 SAM-MT：打破目標數量限制，實現即時多目標影片分割

TL;DR：基於 SAM 2 改進，透過解耦注意力機制讓多目標分割速度不再隨目標數增加而下降。

在影片目標分割（VOS）領域，追蹤單一目標早已相當成熟，但一旦要同時分割多個目標，傳統做法通常是為每個目標重複執行一次處理流程。這導致了一個嚴重的工程痛點：目標越多，FPS 越低，延遲隨之無限增加。

🤔 **多目標分割的延遲困境**

目前的 VOS 方法在處理多目標時，往往採取「複製單目標流程」的策略。這種線性增加的計算成本，使得即時處理（Real-time）在多目標場景下幾乎不可能實現。

🧩 **SAM-MT 的核心設計：解耦與並行處理**

為了將 SAM 2 轉化為可即時運作的多目標互動框架，SAM-MT 引入了以下技術設計：

- **查詢表示法**：使用明確的查詢（Explicit Queries）來代表不同的獨立目標，並同時搭配一個共享表示法（Shared Representation）來捕捉全域上下文。
- **解耦遮罩注意力（Decoupled Masked Attention）**：透過此機制確保各個目標的身份獨立，防止不同目標之間產生幹擾。
- **稀疏記憶體（Sparse Memory）**：用於維持時間演進（Temporal Evolution）的穩定性。
- **專屬處理策略**：針對遮擋處理（Occlusion Handling）與重疊防止（Overlap Prevention）設計了專門的策略。

📊 **效能突破：延遲與目標數量脫鉤**

SAM-MT 最顯著的貢獻在於成功將處理延遲與目標數量解耦。即便在追蹤 10 個目標的情況下，其速度仍能維持在 36 FPS 以上，達到與單目標基準線（Baseline）相當的即時水準，同時保留了 SAM 2 強大的影片分割效能。

🎯 **實務啟示**

對於需要開發多目標追蹤系統的工程師來說，SAM-MT 提供了一種有效的最佳化方向：不再採取簡單的重複迭代，而是透過「共享上下文 + 解耦目標查詢」的架構，在維持精準度的前提下，將計算複雜度從目標數的線性增長轉化為常數級別的開銷。

🔗 **來源**
- 標題：SAM-MT: Real-Time Interactive Multi-Target Video Segmentation
- 連結：https://huggingface.co/papers/2607.08688

#SAM2 #SAMMT #VideoObjectSegmentation #ComputerVision #RealTime #MultiTargetSegmentation #DeepLearning #AI #VideoProcessing #MaskedAttention
