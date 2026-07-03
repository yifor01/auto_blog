---
title: 'Multi-Resolution Flow Matching: Training-Free Diffusion Acceleration via Staged
  Sampling'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.01642
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:51:40.228750'
---

📌 不需要重新訓練，MrFlow 讓文字生成影像速度提升 25 倍

TL;DR：透過低解析度生成結合畫素空間超解析度與雜訊注入，實現無需訓練的 Diffusion 加速。

在追求生成品質與推論速度的拉鋸戰中，大多數的加速方案往往需要對模型進行蒸餾 (Distillation) 或重新訓練，這對工程師來說意味著高昂的運算成本與調優時間。

🤔 **如何在不修改模型的前提下，極速提升生成速度？**

MrFlow 提出了一種名為「多解析度流匹配 (Multi-Resolution Flow Matching)」的策略。其核心邏輯不再是單純地減少取樣步數，而是將生成過程拆解為不同階段的取樣，以降低運算量。

🧩 **低解析度生成與畫素空間超解析度的結合**

MrFlow 的加速流程採取以下步驟：
1. 先在低解析度 (Low-resolution) 狀態下進行初步生成。
2. 結合畫素空間的超解析度 (Pixel-space super-resolution) 技術將影像放大。
3. 引入雜訊注入 (Noise injection) 機制，在後續階段修正細節並提升影像品質。

這種分階段取樣 (Staged Sampling) 的設計，讓模型能快速確定影像的大致結構，再將有限的運算資源集中在細節修復上。

📊 **最高 25 倍的推論加速**

根據作者宣稱，MrFlow 能夠在不對模型進行任何訓練 (Training-free) 且無需修改執行時間 (Runtime modifications) 的情況下，實現最高 25 倍的生成速度提升。這意味著開發者可以直接將此方法應用於現有的 Diffusion 模型，而不需要重新跑一遍訓練流程。

🎯 **實務啟示**

對於需要部署生成式 AI 服務的工程師來說，MrFlow 提供了一個極具吸引力的方向：加速不一定要透過模型壓縮或蒸餾。透過設計「低解析度 $\to$ 超解析度 $\to$ 雜訊修正」的取樣管線，可以在維持品質的前提下大幅降低推論延遲，且部署成本幾乎為零。

🔗 **來源**
- 標題：Multi-Resolution Flow Matching: Training-Free Diffusion Acceleration via Staged Sampling
- 連結：https://huggingface.co/papers/2607.01642

#Diffusion #FlowMatching #TextToImage #InferenceAcceleration #TrainingFree #SuperResolution #ComputerVision #GenerativeAI #Sampling #MrFlow
