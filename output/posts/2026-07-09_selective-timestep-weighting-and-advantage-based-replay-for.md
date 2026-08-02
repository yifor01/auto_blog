---
title: Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient
  Diffusion RLHF
source: arXiv
url: http://arxiv.org/abs/2607.07693v1
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T10:02:26.143759'
---

📌 【研究】Diffusion RLHF 效率突破：透過時間步權重與重播機制提升 6 倍樣本效率

TL;DR：針對 Diffusion RLHF 回饋效率低的問題，提出時間步權重最佳化與 Advantage-Based Replay，將樣本效率提升至 6 倍。

在對生成模型進行人類回饋強化學習 (RLHF) 時，Diffusion Model 面臨一個巨大的痛點：獲取回饋的成本極高。目前的做法通常需要海量的 Reward Model 評估或人類標記，這使得 Diffusion RLHF 在實際應用中受限於回饋獲取的瓶頸。

🤔 **回饋訊號在去噪過程中分佈不均**

作者觀察到，Diffusion Model 的去噪軌跡 (trajectories) 中，獎勵資訊的分佈並不均勻。並非所有的去噪時間步 (timesteps) 或所有軌跡對學習獎勵訊號的貢獻都相同，這意味著目前的最佳化方式在更新梯度時，並未充分利用最具資訊量的部分。

🧩 **兩項互補策略：權重最佳化與軌跡重播**

為了提高回饋效率並維持對未知提示 (unseen prompts) 的泛化能力，論文提出了兩種核心方案：

1. **時間步權重方案 (Per-timestep Weighting)**：
   在策略最佳化過程中，對不同的去噪步驟重新分配權重。作者在理論上將此權重設計與 Proximal Policy Optimization (PPO) 的最佳收斂特性掛鉤，並透過經驗方式近似其權重趨勢，藉此強化資訊量較高的時間步。

2. **基於優勢的重播機制 (Advantage-Based Replay)**：
   引入一種重播機制來優先處理具有高資訊量的軌跡。這讓模型能夠重複利用過去的樣本，而不需要為了每一次更新而反覆查詢新的獎勵訊號。

📊 **樣本效率提升最高達 6 倍**

在相同的超參數設定下，這套組合策略展現了顯著的效能提升。與目前廣泛使用的 Diffusion RLHF 基準線 (baselines) 相比，該方法在樣本效率上最高達 6 倍的提升，且能有效維持模型的泛化能力。

🎯 **實務啟示**

對於開發 Diffusion RLHF 的工程師而言，這項研究提供了一個關鍵方向：不要將去噪過程中的所有時間步視為等價。透過對「高價值」的時間步與軌跡進行加權或重播，可以在減少對 Reward Model 依賴的同時，加速模型的收斂速度。

🔗 **來源**
- 標題：Selective Timestep Weighting and Advantage-Based Replay for Sample-Efficient Diffusion RLHF
- 作者／機構：Eric Zhu, Abhinav Shrivastava, Soumik Mukhopadhyay
- 連結：http://arxiv.org/abs/2607.07693v1

#DiffusionModel #RLHF #PPO #SampleEfficiency #ReinforcementLearning #GenerativeAI #MachineLearning #RewardModel #DeepLearning #Optimization
