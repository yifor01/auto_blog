---
title: 'Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of
  Large Language Models'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.19750
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:30:54.756301'
---

📌 Manifold Bandits：利用 LLM 潛在幾何結構最佳化 RL 課程學習

TL;DR：透過貝氏流形課程框架，根據任務間的幾何關係動態取樣，提升 LLM 的推理能力。

強化學習 (RL) 在提升 LLM 推理能力上已有顯著成效，但一個核心挑戰在於：如何決定讓模型「在什麼時間點」練習「什麼難度」的問題？如果取樣太隨機，學習效率會極低；如果太單一，模型則容易陷入區域性最佳解。

🤔 **解決推理能力提升的取樣難題**

目前的 RL 訓練往往面臨任務取樣的挑戰。這篇論文提出了一套「貝氏流形課程 (Bayesian Manifold Curriculum)」框架，旨在將問題取樣過程結構化，不再是隨機挑選，而是基於任務在潛在空間中的幾何關係 (Manifold Relationships) 以及內生的非平穩性 (Endogenous Non-stationarity) 來決定取樣策略。

🧩 **結合流形幾何與貝氏學習的取樣機制**

該框架的核心理念是將 LLM 的推理任務視為分佈在某個流形（Manifold）上的點。其運作邏輯如下：

1. **識別流形關係**：分析不同推理任務在潛在空間中的幾何結構，找出任務之間的關聯性。
2. **貝氏課程排程**：利用貝氏方法動態調整取樣分佈，根據模型目前的學習狀態，在流形上選擇最適合當前進度的任務。
3. **處理非平穩性**：考慮到模型在訓練過程中能力會不斷演進（即內生的非平穩性），框架會隨之調整取樣策略，以維持最佳的學習曲線。

🎯 **實務啟示**

對於開發推理模型 (Reasoning Models) 的工程師來說，這項研究提供了一個新視角：提升模型能力的關鍵可能不在於增加資料量，而在於「取樣的順序與結構」。若能將任務對映到潛在幾何空間並實作動態課程學習，能有效減少 RL 訓練中的盲目探索，提高收斂效率。

🔗 **來源**
- 標題：Manifold Bandits: Bayesian Curriculum Learning over the Latent Geometry of Large Language Models
- 連結：https://huggingface.co/papers/2606.19750

#LLM #ReinforcementLearning #CurriculumLearning #Bayesian #Manifold #Reasoning #MachineLearning #LatentSpace #RLHF #Optimization
