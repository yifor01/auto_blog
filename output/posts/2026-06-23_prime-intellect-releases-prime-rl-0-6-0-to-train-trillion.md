---
title: Prime Intellect Releases prime-rl 0.6.0 to Train Trillion-Parameter MoE Models
  on Agentic RL Workloads
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/23/prime-intellect-releases-prime-rl-0-6-0-to-train-trillion-parameter-moe-models-on-agentic-rl-workloads/
score: 101
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:24:53.466911'
---

📌 Prime Intellect 發布 prime-rl 0.6.0：支援兆引數 MoE 模型的 Agentic RL 訓練

TL;DR：開源框架 prime-rl 0.6.0 透過非同步 RL 與 FP8 最佳化，讓兆引數 MoE 模型能高效處理長序列軟體工程任務。

在訓練大型模型處理複雜的 Agentic 任務（如軟體工程）時，最令人頭痛的不是平均速度，而是那些執行數小時的「長尾離群值」。如果所有 GPU 都要等待這些慢速任務完成才能更新策略，運算資源將被嚴重浪費。

🧩 **非同步 RL 架構解決 GPU 空轉問題**

prime-rl 採用非同步強化學習（Asynchronous RL）設計，將訓練器（Trainer）與推論系統（Inference systems）解耦，使其能獨立執行與擴充套件。

- **權重即時推送**：一旦最佳化器完成步驟，推論策略會立即更新，無需等待所有 rollout 完成。
- **快取管理機制**：已發出的 rollout 會保留其活動的字首快取（prefix cache），這意味著單次 rollout 產出的 token 可能混合了多個不同版本的策略。
- **KV 快取強制更新**：新發出的 rollout 會透過「KV-cache salt」強制重新填充快取，即使字首相同也會重新計算。
- **過時請求過濾**：透過 `max_off_policy_steps` 設定閾值，直接捨棄來自過舊策略的請求，確保訓練效率。

📊 **GLM-5 訓練實測：28 個 H200 節點處理 131k 長度**

Prime Intellect 團隊利用此框架訓練 zai-org/GLM-5.1 處理軟體工程（SWE）任務，展現了極高的資源利用率：
- **序列長度**：最高支援達 131k。
- **執行效率**：Step time 保持在 5 分鐘以內。
- **資源配置**：Batch size 為 256 rollouts，僅使用 28 個 H200 節點。
- **部署便捷性**：在 Slurm 叢集上僅需單一指令即可啟動完整執行。

💡 **針對推論瓶頸的兩大效能最佳化**

由於推論通常是 RL 系統的吞吐量瓶頸，prime-rl 採取以下技術提升效能：

1. **FP8 推論**：利用 FP8 低精度加速 prefill 與 decode 階段，並搭配 DeepEP 與 DeepGEMM 核心（kernels）。
2. **寬專家並行（Wide Expert Parallelism）**：將專家（Experts）分佈在 32 個或更多 GPU 上，並搭配大規模資料並行（Data-parallel）來提升處理能力。

🎯 **實務啟示**

對於需要訓練兆引數 MoE 模型（如 Kimi-K2.7-Code 或 NVIDIA-Nemotron-3-Ultra）且面臨長序列 Agentic 任務的工程師，prime-rl 提供的「非同步更新」與「推論/訓練解耦」架構，是降低 GPU 空轉率、提升吞吐量的關鍵實作方向。

🔗 **來源**
- 標題：Prime Intellect Releases prime-rl 0.6.0 to Train Trillion-Parameter MoE Models on Agentic RL Workloads
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/06/23/prime-intellect-releases-prime-rl-0-6-0-to-train-trillion-parameter-moe-models-on-agentic-rl-workloads/

#RL #MoE #AgenticAI #PrimeIntellect #GLM5 #ReinforcementLearning #FP8 #DistributedTraining #LargeLanguageModels #SoftwareEngineering
