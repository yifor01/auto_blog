---
title: LFM2.5-Encoders for Fast Long-Context Inference on CPU
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm2-5-encoders
model: tencent/hy3:free
generated_at: '2026-07-29T14:10:47.689587'
score: 97
---

📌 【HuggingFace 報導】LFM2.5-Encoders 登場：在 CPU 上實現長上下文的高效推論

TL;DR：LiquidAI 推出 LFM2.5-Encoders，讓 CPU 也能快速處理長文本的編碼任務。

當處理長文件時，傳統模型往往會讓推論延遲隨輸入長度劇增，這對需要全天候運作的生產環境（如 PII 偵測或意圖路由）來說是極大的成本挑戰。

🤔 **為什麼需要通用型 Encoder？**

雖然 LiquidAI 上個月才發布了專為多語言搜尋設計的 LFM2.5-Retrievers，但這次推出的 LFM2.5-Encoders 旨在服務更廣泛的場景。

透過預訓練的 masked-language objective（遮蔽語言目標），這些模型可以針對分類、Token 級別任務以及搜尋進行 fine-tuning（微調）。這類任務在實際生產環境中通常需要全天候執行，且大多運行於 CPU 設備上，且輸入內容往往非常長。

🧩 **從 Decoder 轉化為 Bidirectional Encoder**

LFM2.5-Encoders 繼承自 LFM2 架構，其設計核心在於成本隨輸入長度增長的速率非常緩慢。

開發團隊的技術路徑如下：
1. 使用 LFM2.5-230M 與 LFM2.5-350M 作為解碼器（Decoder）骨幹進行初始化。
2. 將原本的因果解碼器（Causal Decoder）轉化為雙向編碼器（Bidirectional Encoder）。

📊 **效能表現：在 CPU 上比 ModernBERT 快 3.7 倍**

這系列模型包含 LFM2.5-Encoder-230M 與 LFM2.5-Encoder-350M 兩種規模，其表現如下：

- **高質量與長上下文**：在 GLUE、SuperGLUE 及多語言任務上，表現能與更大規模的模型媲美或更佳；支援 8,192-token 的上下文長度。
- **CPU 推論優勢**：在處理長上下文時，速度約為 ModernBERT-base 的 3.7 倍。
- **延遲特性**：隨著輸入內容變長，延遲（Latency）的增長速度非常緩慢。

🎯 **實務啟示**

對於工程師而言，這類模型提供了一個低成本的解決方案，可以用現有的硬體（CPU）來建構以下應用：
- 意圖路由（Intent Routers）
- 策略檢查工具（Policy Linters）
- 個人隱私資訊偵測（PII Detectors）
- 文字分類器（Text Classifiers）

🔗 **來源**
- 標題：LFM2.5-Encoders for Fast Long-Context Inference on CPU
- 作者／機構：LiquidAI @ HuggingFace
- 連結：https://huggingface.co/blog/LiquidAI/lfm2-5-encoders

#AI #NLP #HuggingFace #LiquidAI #Encoder #CPUInference #LongContext #MachineLearning #DeepLearning #Efficiency
