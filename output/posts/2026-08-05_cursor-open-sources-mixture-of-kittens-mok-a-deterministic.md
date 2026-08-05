---
title: 'Cursor Open-Sources Mixture-of-Kittens (MoK): A Deterministic MoE Training
  Megakernel for GB300 NVL72 Racks'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/04/cursor-open-sources-mixture-of-kittens-mok-a-deterministic-moe-training-megakernel-for-gb300-nvl72-racks/
model: tencent/hy3:free
generated_at: '2026-08-05T08:38:32.736380'
score: 99
---

📌 【Cursor 開源】MoK 專案登場：針對 GB300 NVL72 打造的 MoE 訓練 Megakernel

TL;DR：Cursor 開源 MoK 專案，透過融合通訊與計算，讓 MoE 訓練效能提升最高達 2.37 倍。

在訓練大規模 Mixture-of-Experts (MoE) 模型時，GPU 間的通訊往往成為效能瓶頸。Cursor Research 團隊針對這一痛點，推出了名為 Mixture-of-Kittens (MoK) 的開源 Megakernel，旨在透過高度整合的運算架構，解決大規模 GPU 叢集中的通訊與計算同步問題。

🧩 **將通訊與計算融合為單一決定性 Kernel**

在以往的架構中，MoE 層的通訊與計算通常是分開處理的，這導致通訊往往會成為訓練過程中的限制因素，甚至佔據端到端訓練時間的一半以上。

MoK 的核心設計理念是將每一次 MoE 的通訊與計算步驟，全部融合（Fuse）進一個單一且具備「決定性」（Deterministic）特性的 Megakernel 中。這種設計不僅提升了效率，還能確保訓練過程的穩定性。

📊 **效能大幅提升：比最強的 Baseline 快 2.37 倍**

在針對多種模型架構（如 Kimi K2.7 Code, GLM-5.2, Qwen3.5-397B-A17B, DeepSeek-V4-Pro）的測試中，MoK 展現了極強的競爭力：

- **MXFP8 精度測試**：
  - Forward（前向傳播）：比最強的 Baseline 快 up to 2.37x。
  - Backward（反向傳播）：比最強的 Baseline 快 1.78x。
- **BF16 精度測試**：
  - Forward（前向傳播）：提升 1.92x。
  - Backward（反向傳播）：提升 1.58x。
- **端到端（End-to-end）測試**：
  - 在 512 顆 GPU 的 GB300 NVL72 叢集上，每顆 GPU 每秒處理的 Token 數從 760.9 增加至 1,070.2，效能提升了 1.41x。

⚠️ **硬體門檻極高，僅適合大型機構**

儘管效能驚人，但 MoK 的硬體需求非常嚴苛，這也限制了其目標受眾的範圍：

- **硬體要求**：必須使用 NVIDIA Blackwell SM100 或 SM103 GPU，具體應用於 GB200 NVL72 或 GB300 NVL72 機架。
- **軟體依賴**：需要 Python 3.12+、PyTorch 2.10+ 以及 CUDA toolkit 13.0+。
- **架構限制**：由於依賴 PyTorch symmetric memory 進行 GPU 間緩衝，這意味著單機 8-GPU 的小型團隊無法直接受益，受眾僅限於擁有或租用 NVL72 容量的大型實驗室、資助模型的新創公司、GPU 雲端基礎設施供應商或國家級運算中心。

💡 **為什麼這對工程師很重要？**

MoK 的出現，解決了在 Blackwell 架構下，由於 Grace CPU 相對於 GPU 運算速度較慢，導致 CPU-GPU 同步壓力巨大的問題。透過 Megakernel 架構，MoK 能夠在 NVLink 域內實現精細的重疊（Overlap）運算，並透過 Cluster Launch Control 調度，避免 RDMA 通訊被序列化。

對於需要訓練 DeepSeek-V3 風格 MoE 模型，或進行需要高度決定性的強化學習（On-policy RL）後訓練、內部消融實驗（Ablations）的團隊來說，MoK 提供了一個極具價值的技術工具。

🎯 **實務啟示**

如果你正在處理超大規模的 MoE 模型訓練，且硬體環境具備 NVIDIA Blackwell NVL72 架構，MoK 提供了一種從底層 Kernel 層級優化通訊與計算的全新路徑。這標誌著 MoE 訓練正在從「分散式運算」轉向「高度整合的 Megakernel 運算」演進。

🔗 **來源**
- 標題：Cursor Open-Sources Mixture-of-Kittens (MoK): A Deterministic MoE Training Megakernel for GB300 NVL72 Racks
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/04/cursor-open-sources-mixture-of-kittens-mok-a-deterministic-moe-training-megakernel-for-gb300-nvl72-racks/

#AI #MachineLearning #MoE #MixtureOfExperts #NVIDIA #Blackwell #Cursor #DeepLearning #GPU #HighPerformanceComputing
