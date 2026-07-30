---
title: LFM2.5-Encoders for Fast Long-Context Inference on CPU
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm2-5-encoders
model: tencent/hy3:free
generated_at: '2026-07-29T08:29:38.537838'
score: 98
---

📌 【HuggingFace 報導】LFM2.5-Encoders 登場：讓長上下文在 CPU 上也能高效運作

TL;DR：LiquidAI 推出 LFM2.5-Encoders，在 CPU 上處理長文本的效能比 ModernBERT-base 快 3.7 倍。

🤔 **突破長文本推理的硬體限制**

在處理大規模文件任務時，開發者往往受限於昂貴的 GPU 資源。LiquidAI 透過 LFM2.5-Encoders 解決了這個痛點，讓開發者能在現有的硬體（甚至是 CPU）上，順暢地執行大規模的文本處理工作。

🧩 **基於 LFM2 架構的通用編碼器**

LFM2.5-Encoders 是從 LFM2 解碼器骨幹（Backbones）演變而來，透過將原本的因果解碼器（Causal Decoder）轉化為雙向編碼器（Bidirectional Encoder）而成。

這款模型具備以下特性：
- **兩款尺寸**：分別為 LFM2.5-Encoder-230M 與 LFM2.5-Encoder-350M。
- **長上下文支援**：具備 8,192 token 的上下文長度，且延遲（Latency）隨輸入長度增加的成長速度非常緩慢。
- **通用性強**：採用遮蔽語言模型（Masked-language objective）進行預訓練，因此不僅能用於搜尋，還能微調（Fine-tune）來執行分類、Token 層級任務或搜尋任務。

📊 **效能與精準度表現**

- **超越傳統模型**：在 GLUE、SuperGLUE 及多語言任務上的表現，足以媲美甚至超越體積更大的編碼器。
- **CPU 推理優勢**：在處理長上下文時，效能約為 ModernBERT-base 的 3.7 倍。

🎯 **實務啟示**

對於需要全天候運行且成本敏感的 NLP 應用，LFM2.5-Encoders 提供了一個極具成本效益的選擇，特別適合用於開發以下功能：
- 意圖路由（Intent Routers）
- 策略檢查工具（Policy Linters）
- 個人敏感資料偵測（PII Detectors）
- 文本分類器（Text Classifiers）

🔗 **來源**
- 標題：LFM2.5-Encoders for Fast Long-Context Inference on CPU
- 作者／機構：LiquidAI @ HuggingFace
- 連結：https://huggingface.co/blog/LiquidAI/lfm2-5-encoders

#AI #MachineLearning #NLP #HuggingFace #LiquidAI #Encoder #CPUInference #LongContext #ModernBERT #DeepLearning
