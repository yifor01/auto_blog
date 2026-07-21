---
title: Accelerating Text-to-Video Generation with Calibrated Sparse Attention
source: Apple ML
url: https://machinelearning.apple.com/research/calibrated-sparse-attention
model: tencent/hy3:free
generated_at: '2026-07-22T00:42:35.041119'
score: 108
---

這是一篇研究論文。

📌 【Apple ML 研究】CalibAtt：透過校準稀疏注意力，加速文字轉影片生成

TL;DR：CalibAtt 是一種無需重新訓練的方法，透過識別並跳過無效的注意力連線，實現最高 1.58 倍的影片生成加速。

🎣 隨著擴散模型（Diffusion Models）讓高品質影片生成成為現實，開發者卻面臨著沉重的運算負擔。影片生成過程中的 Transformer 架構，正受困於龐大的時空注意力（Spatiotemporal Attention）運算壓力。

🤔 **注意力機制中存在大量無效連線**

研究發現，在各種不同的輸入內容中，很大一部分的 token 對 token（標記對標記）連線產生的分數極低，幾乎可以忽略不計。更重要的是，這些「無效連線」的模式在不同的查詢（Queries）之間往往具有重複性，且在區域性 token 區塊（Local token blocks）之間的連線也呈現類似特性。

🧩 **CalibAtt：無需訓練的稀疏注意力架構**

基於上述觀察，研究團隊提出了 CalibAtt，這是一種「無需訓練」（Training-free）的加速方法，其核心流程如下：

1. **離線校準階段 (Offline Calibration Pass)**：識別並找出在不同輸入之間保持穩定的「區塊級稀疏性」與「重複模式」。
2. **編譯最佳化**：將這些模式編譯成針對每一層、每個注意力頭（Head）以及每個擴散時間步（Diffusion Timestep）最佳化的注意力運算指令。
3. **推論階段 (Inference Time)**：針對選定的、與輸入相關的連線進行密集（Dense）運算，並以硬體友善（Hardware-efficient）的方式跳過未被選中的連線。

📊 **在多種模型上實現最高 1.58 倍加速**

透過對多種模型進行廣泛實驗，CalibAtt 在保持影片生成品質與文本-影片對齊（Text-video alignment）能力的同時，展現了優異的效能：

- **測試模型**：包含 Wan 2.1 14B、Mochi 1 以及多種少步數蒸餾模型（Few-step distilled models）。
- **加速表現**：在不同解析度下，實現了最高達 1.58 倍的端到端（End-to-end）加速。
- **競爭力**：效能優於現有的其他無需訓練的加速方法。

🎯 **實務啟示**

對於需要大規模部署影片生成模型的工程師而言，CalibAtt 提供了一種「即插即用」的最佳化思路。由於它不需要重新訓練模型，工程師可以在不犧牲生成品質的前提下，透過校準階段直接提升推論效率，降低硬體成本並縮短生成等待時間。

🔗 **來源**
- 標題：Accelerating Text-to-Video Generation with Calibrated Sparse Attention
- 作者／機構：Shai Yehezkel, Shahar Yadin, Noam Elata, Yaron Ostrovsky-Berman, Bahjat Kawar @ Apple (Work done while at Tel Aviv University)
- 連結：https://machinelearning.apple.com/research/calibrated-sparse-attention

#AI #ComputerVision #VideoGeneration #DiffusionModels #Transformer #SparseAttention #MachineLearning #AppleML #CalibAtt #AIInference
