---
title: 'Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image
  Generation'
source: arXiv
url: http://arxiv.org/abs/2607.11886v1
score: 92
model: tencent/hy3:free
generated_at: '2026-07-14T08:00:40.980216'
---

📌 【arXiv 研究】不用訓練！將多模態大模型直接轉化為影像生成 RL 的報酬模型

TL;DR：SpectraReward 透過「提示詞還原度」實現 Zero-shot 報酬機制，無需額外訓練即可提升影像生成效能。

在影像生成領域的強化學習（Reinforcement Learning, RL）中，如何定義一個精準且強大的「報酬模型（Reward Model）」一直是難題。傳統做法往往需要收集大量偏好資料並對模型進行微調，但這不僅耗時，還可能引入偏好偏差。

🤔 **不用偏好標籤，直接利用 MLLM 的對齊能力**

研究者提出了一個名為 SpectraReward 的訓練免除（training-free）報酬函式。與以往要求多模態大模型（MLLM）直接判斷影像好壞，或回答一系列分解後的驗證問題不同，SpectraReward 的核心邏輯是：

1. **核心機制**：衡量從生成的影像中，能多大程度地「還原」原始提示詞（Prompt）。
2. **技術實作**：透過單次、以影像為條件（image-conditioned）且 teacher-forced 的前向傳播（forward pass），計算「影像條件下的提示詞對數概機率（image-conditioned prompt log-likelihood）」。
3. **優勢**：直接複用 MLLM 預訓練時已具備的「圖文對齊」能力，不需要任何偏好標籤（preference labels）或報酬模型的微調（fine-tuning）。

🧩 **Self-SpectraReward：實現閉環自我進化的框架**

針對統一多模態模型（unified multimodal models），作者進一步推出了 Self-SpectraReward。這是一種特殊的應用場景：

- **閉環機制**：讓策略模型（Policy）自身的「理解分支」直接作為其「生成分支」的報酬模型。
- **無需外部知識**：這種設計形成了一個閉環的自我改進框架，不需要依賴外部的報酬模型或外部知識。

📊 **實驗結果：效能提升且具備跨模型通用性**

研究人員針對多種配置進行了廣泛的實驗驗證，包含兩種擴散模型（diffusion models）、三種 RL 演算法，以及橫跨 4B 到 235B 引數規模、來自四個不同家族的九種 MLLM 骨幹網路。

- **效能表現**：SpectraReward 與 Self-SpectraReward 在五個分佈外（out-of-distribution）的圖文生成基準測試中，皆展現出顯著且一致的生成效能提升，表現優於以往基於 MLLM 訓練的報酬方法。
- **關鍵發現**：
    - 較大的報酬 MLLM 並不總是表現更好。
    - Self-SpectraReward 的表現可以媲美甚至超越規模大得多的外部報酬模型。
    - 研究指出，「報酬與策略之間的對齊（reward-policy alignment）」是實現有效影像生成 RL 的關鍵因素。

🎯 **實務啟示**

對於開發者而言，SpectraReward 提供了一種極低成本的方案，讓開發者在進行影像生成模型的強化學習時，無需投入大量資源進行偏好資料收集與模型微調，即可利用現有的 MLLM 預訓練能力來最佳化生成品質。

🔗 **來源**
- 標題：Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation
- 作者／機構：Runhui Huang, Qihui Zhang, Zhe Liu, Yu Gao, Jie Wu
- 連結：http://arxiv.org/abs/2607.11886v1

#MLLM #ReinforcementLearning #DiffusionModels #SpectraReward #ZeroShot #ComputerVision #TextToImage #AIResearch #MachineLearning #SelfImprovement
