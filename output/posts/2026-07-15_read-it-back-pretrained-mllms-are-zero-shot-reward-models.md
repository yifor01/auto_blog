---
title: 'Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image
  Generation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.11886
score: 108
model: tencent/hy3:free
generated_at: '2026-07-15T07:51:34.113307'
---

📌 預訓練 MLLM 作零樣本獎勵模型

TL;DR：SpectraReward 免訓練將預訓練 MLLM 轉為影像生成 RL 獎勵，效能更優。

🎣 要讓擴散模型精準聽從文字指令生成圖片，強化學習（RL）是常見手段，但獎勵模型往往得額外訓練。這篇論文提出反直覺做法：直接拿現成多模態模型，看它能否從生成影像「讀回」原始提示，就能當作獎勵訊號。

🤔 影像生成 RL 的獎勵模型痛點
過去將 MLLM 用於影像生成 RL 獎勵時，常要求模型直接評判圖片好壞，或回答拆解後的驗證問題。本文指出這類方法需要偏好標籤或 reward model 的 fine-tuning（微調），而 SpectraReward 目標是 training-free，把預訓練 MLLM 變成現成（off-the-shelf）獎勵模型。

🧩 用「讀回 prompt」的對數似然當獎勵
SpectraReward 的核心操作：對生成影像進行單次 image-conditioned、teacher-forced 前向傳遞，測量原始 prompt 能被復原的程度。具體取「平均 image-conditioned prompt log-likelihood」作為 reward，直接重用 MLLM 預訓練的 image-text alignment（影像-文字對齊）能力，不須偏好標籤與 fine-tuning（微調）獎勵模型。

進一步提出 Self-SpectraReward，適用於 unified multimodal models：讓 policy 自身的 understanding branch 擔任 generation branch 的獎勵模型，形成無外部獎勵模型、無外部知識的閉環自我改善框架。

📊 橫跨多模型多演算法的實證覆蓋
實驗設計涵蓋兩個 diffusion models、三個 RL 演算法、九個來自四個 MLLM 家族（參數規模 4B 到 235B）的 reward MLLM 主幹，並在五個 out-of-distribution text-to-image 基準上驗證。

結果顯示，SpectraReward 與 Self-SpectraReward 皆能顯著且一致地提升生成表現，並超越先前基於 MLLM 的獎勵訓練方法。

💡 獎勵模型越大不一定越好
進一步分析指出，更大的 reward MLLM 並非總能帶來更好效果；而 Self-SpectraReward 甚至可以匹敵或超越參數規模大得多的外部獎勵模型。這暗示 reward 與 policy 之間的對齊（reward-policy alignment）才是影像生成 RL 有效的關鍵因素。

🎯 直接重用現成 MLLM 省下訓練成本
對工程師而言，這代表在實作文字生成圖片 RL 時，可嘗試直接接入預訓練 MLLM 計算 prompt 復原似然，免去標註與訓練獎勵模型的流程；若採用統一多模態架構，更能搭建自我獎勵閉環，降低對外部模型的依賴。

🔗 來源
- 標題：Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation
- 連結：https://huggingface.co/papers/2607.11886

#MLLM #RewardModel #TextToImage #DiffusionModel #ReinforcementLearning #ZeroShot #SpectraReward #ImageGeneration #SelfImprovement #Multimodal
