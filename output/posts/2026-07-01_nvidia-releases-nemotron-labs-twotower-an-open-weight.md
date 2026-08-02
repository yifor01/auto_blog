---
title: 'NVIDIA Releases Nemotron-Labs-TwoTower: an Open-Weight Diffusion Language
  Model Built on a Frozen Autoregressive Nemotron-3-Nano-30B-A3B Backbone'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/01/nvidia-releases-nemotron-labs-twotower/
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:30:51.698182'
---

📌 【NVIDIA 新發布】Nemotron-Labs-TwoTower：用雙塔擴散模型將生成速度提升 2.42 倍

TL;DR：NVIDIA 推出開源權重的擴散語言模型，透過分離「上下文」與「去噪」雙塔設計，大幅突破自回歸模型的生成產能瓶頸。

傳統自回歸 (Autoregressive, AR) 模型在生成文字時必須一個 token 接一個 token 地解碼，這種序列化的過程成為了效能的上限。如果能讓 token 並行生成並迭代最佳化，是否能維持品質且大幅加速？

🤔 **打破自回歸的序列化瓶頸**

離散擴散語言模型 (Discrete Diffusion Language Models) 提供了一種不同的路徑：它們能並行生成 token 並透過迭代不斷精煉。然而，大多數擴散模型使用單一網路同時負責「表示乾淨 token」與「對損壞 token 進行去噪」這兩項任務。

🧩 **TwoTower 設計：將上下文與去噪任務分離**

NVIDIA 提出的 Nemotron-Labs-TwoTower 採取了「雙塔」架構，將上述兩項任務拆分，並建立在 Nemotron-3-Nano-30B-A3B 這個混合骨幹 (Hybrid Backbone) 之上：

1. **AR 上下文塔 (Context Tower)**：
   - 狀態：完全凍結 (Frozen)。
   - 運作：以因果方式處理提示詞 (Prompt) 與已確定的 token，產生每層的 KV cache 與最終的 Mamba-2 狀態，保留了原有的自回歸能力。
2. **擴散去噪塔 (Denoiser Tower)**：
   - 狀態：經過訓練。
   - 運作：負責精煉帶雜訊的區塊 (Blocks)。在區塊內部使用雙向注意力 (Bidirectional in-block attention)，但對過去的乾淨區塊仍保持因果關係。

**層級對齊的連線機制**：兩座塔透過層級對齊的交叉注意力 (Layer-aligned cross-attention) 連線，去噪塔的第 $i$ 層會對上下文塔的第 $i$ 層進行 cross-attend，實現多尺度的資訊存取。

📊 **混合骨幹架構與訓練資料**

- **模型組成**：兩座塔均由 Mamba-2、self-attention 與混合專家 (MoE) 層交錯組成。
- **層數配置**：每座塔共有 52 層（23 層 Mamba-2、6 層 self-attention、23 層 MoE）。
- **參數規模**：總參數約 60B，每座塔每個 token 的啟用參數約 3B。MoE 包含 128 個可路由專家（每次啟用 6 個）以及 2 個共享專家。
- **訓練量**：去噪塔使用約 2.1T tokens 進行訓練，僅為骨幹模型 25T tokens 預訓練量的一小部分。

📊 **效能表現：速度大幅提升且品質損失極低**

根據 NVIDIA 提供的資料，TwoTower 在維持高品質生成的同時，顯著提升了產能：
- **生成速度**：牆鐘時間 (Wall-clock) 的生成產能提升了 2.42 倍。
- **品質維持**：保留了自回歸基準 (AR baseline) 約 98.7% 的綜合基準測試品質。

🎯 **實務啟示**

對於追求極高吞吐量 (Throughput) 的工程師來說，TwoTower 證明了「凍結強大 AR 骨幹 + 訓練輕量去噪塔」的方案可行。這種設計在不犧牲太多品質的前提下，能將生成過程從「單一 token 序列」轉向「區塊並行精煉」，為大規模文字生成提供更高效的替代方案。

🔗 **來源**
- 標題：NVIDIA Releases Nemotron-Labs-TwoTower: an Open-Weight Diffusion Language Model Built on a Frozen Autoregressive Nemotron-3-Nano-30B-A3B Backbone
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/07/01/nvidia-releases-nemotron-labs-twotower/

#NVIDIA #Nemotron #DiffusionModel #LLM #Mamba2 #MoE #GenerativeAI #DeepLearning #OpenWeights #Throughput
