---
title: Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.18953
score: 84
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:35:19.055461'
---

📌 物件中心殘差 RL：解決 VLA 模型從模擬轉向現實的零樣本挑戰

TL;DR：透過物件中心殘差強化學習，讓 VLA 模型在無需現實世界微調的情況下，提升實體機器人的魯棒性。

Vision-Language-Action (VLA) 模型在模擬環境中表現優異，但一旦部署到現實世界，Sim-to-Real 的差距（Gap）往往導致效能大幅下滑。如何在不依賴大量現實資料的情況下，讓模型直接在實體環境中穩定執行？

🤔 **Sim-to-Real 的魯棒性瓶頸**

目前的 VLA 模型在模擬環境中訓練後，常因物理引數差異或視覺雜訊，導致在現實世界中缺乏足夠的魯棒性。傳統方法通常需要大量的實體資料進行微調，但獲取成本極高。

🧩 **利用「殘差 RL」進行零樣本修正**

本研究提出一個物件中心（Object-Centric）的殘差強化學習（Residual Reinforcement Learning）框架，其核心邏輯如下：

- 建立修正策略：在模擬環境中訓練一套專門的「修正策略（Corrective Policies）」。
- 殘差疊加：該策略不取代原有的 VLA 模型，而是計算出一個殘差值，疊加在 VLA 的輸出之上。
- 零樣本遷移：由於修正策略聚焦於物件中心特徵，使其能跨越模擬與現實的差異，實現 Zero-Shot（零樣本）遷移。

🎯 **實務啟示**

對於開發機器人控制系統的工程師而言，這提供了一種新思路：與其試圖建立完美的物理模擬，不如將「基礎動作（VLA）」與「精準修正（Residual RL）」解耦。透過在模擬端訓練對物件敏感的修正層，可以有效降低對現實世界標記資料的依賴，縮短部署週期。

🔗 **來源**
- 標題：Object-Centric Residual RL for Zero-Shot Sim-to-Real VLA Enhancement
- 連結：https://huggingface.co/papers/2606.18953

#VLA #ReinforcementLearning #SimToReal #Robotics #ObjectCentric #ZeroShot #MachineLearning #ResidualRL #ComputerVision # EmbodiedAI
