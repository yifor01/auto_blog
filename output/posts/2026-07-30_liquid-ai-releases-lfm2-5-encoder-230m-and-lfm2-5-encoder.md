---
title: 'Liquid AI Releases LFM2.5-Encoder-230M and LFM2.5-Encoder-350M: Bidirectional
  Encoders That Stay Fast at 8K Context on CPU'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/29/liquid-ai-releases-lfm2-5-encoder-230m-and-lfm2-5-encoder-350m-bidirectional-encoders-that-stay-fast-at-8k-context-on-cpu/
model: tencent/hy3:free
generated_at: '2026-07-30T08:21:19.629877'
score: 86
---

📌 【Liquid AI 新發佈】LFM2.5 雙向編碼器：在 CPU 上處理 8K 長文本依然高效

TL;DR：Liquid AI 推出兩款輕量級雙向編碼器，透過 LFM2 混合架構，讓 CPU 在 8K 上下文下仍具備高效率。

🤔 **解決持續運行的分類與過濾任務**

在現代 AI 流程中，編碼器 (Encoder) 經常位於分類器、意圖路由 (intent routers)、安全過濾器 (safety filters) 與 PII（個人識別資訊）檢測器的底層。這些任務通常需要持續不斷地運行，且為了節省成本，大多在沒有 GPU 的環境下於 CPU 上執行。隨著輸入長度增加，如何在維持效能的同時處理更長的文本，成為關鍵挑戰。

🧩 **基於 LFM2 混合架構的設計理念**

Liquid AI 推出的 LFM2.5-Encoder-230M 與 LFM2.5-Encoder-350M 並非從零開始訓練，而是從 LFM2.5 的解碼器 (decoder) 骨幹模型進行轉換。其核心架構設計包含：

- **混合架構**：將門控短卷積塊 (gated short-convolution blocks) 與分組查詢注意力 (grouped-query attention) 交錯排列。
- **長文本優勢**：由於 LFM2 架構的成本隨輸入長度增加的成長速度較慢，因此在處理長文本時具備優勢。
- **模型規格**：兩款模型均擁有 1024 的隱藏層維度 (hidden size)、65,536 的詞彙表大小 (vocabulary)，並支援 15 種語言。

📊 **以較小規模實現高精準度排名**

Liquid AI 針對 17 項任務（涵蓋 GLUE、SuperGLUE 及多語言分類）對 14 個模型進行評估，所有模型皆經過針對任務的完全微調 (fine-tuned)。

**LFM2.5-Encoder-350M 表現：**
- 17 項任務平均分數為 81.02 (±1.00)，在評估中排名第四。
- 領先的型號（XLM-R XL、ModernBERT-large、XLM-R large）規模均比它大。
- 值得注意的是，排名第一的模型規模幾乎是它的 10 倍。

**LFM2.5-Encoder-230M 表現：**
- 17 項任務平均分數為 79.29 (±1.02)，排名第六。
- 表現優於 ModernBERT-base (78.19) 以及所有 EuroBERT 模型（包括 EuroBERT-610M 與 EuroBERT-2.1B）。
- 效能亦超越了 Liquid AI 自身的檢索型模型（ColBERT 與 Embedding 系列）。

🎯 **實務啟示**

對於需要在 CPU 環境下進行高頻率、長文本處理（如安全過濾或意圖識別）的工程師來說，這類具備高效長文本處理能力且規模較小的雙向編碼器，提供了一個在低硬體成本下維持高精準度的選擇。

🔗 **來源**
- 標題：Liquid AI Releases LFM2.5-Encoder-230M and LFM2.5-Encoder-350M: Bidirectional Encoders That Stay Fast at 8K Context on CPU
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/29/liquid-ai-releases-lfm2-5-encoder-230m-and-lfm2-5-encoder-350m-bidirectional-encoders-that-stay-fast-at-8k-context-on-cpu/

#LiquidAI #Encoder #MachineLearning #NLP #LFM2 #CPUInference #BidirectionalModel #Transformer #DeepLearning #OpenSource
