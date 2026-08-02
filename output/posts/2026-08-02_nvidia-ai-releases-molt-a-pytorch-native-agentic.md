---
title: 'NVIDIA AI Releases Molt: A PyTorch-Native Agentic Reinforcement Learning Framework'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/01/nvidia-ai-releases-molt-a-pytorch-native-agentic-reinforcement-learning-framework/
model: tencent/hy3:free
generated_at: '2026-08-02T08:02:53.380122'
score: 90
---

📌 【NVIDIA NeMo 新作】輕量級 PyTorch 原生框架 Molt：專為研究者設計的 Agentic RL 工具

TL;DR：NVIDIA 發布 Molt，以極簡程式碼量與高度整合性，解決 Agentic RL 研究中複雜的 pipeline 修改成本。

🧪 **追求極致精簡：程式碼量僅 8.6K 行**

在 Agentic Reinforcement Learning (RL) 研究中，開發者常需不斷修改演算法、估計器 (estimators) 或 Rollout 方案。在主流框架中，這些更動往往會連動到訓練器、分散式後端與 Rollout 膠水程式碼，增加研究者的負擔。

NVIDIA NeMo 團隊推出的 Molt 旨在降低這種成本。其設計目標是讓程式碼精簡到研究者能完全理解，且 AI 程式碼助手也能輕易閱讀與推理。

📊 **與同類框架的規模對比**

根據對程式碼導入圖 (import graph) 的追蹤，Molt 的 RL 核心程式碼量僅約 8.6K 行，遠比其他框架精簡：

| 框架 | RL 程式碼行數 (估計) |
| :--- | :--- |
| **Molt** | **8.6K** |
| OpenRLHF | 7.2K |
| Slime | 25K |
| verl | 62K |

🧩 **核心架構：解耦合的異步訓練流程**

Molt 採用了高度整合且不需 Fork 原始碼的設計，透過整合現有工具來實現高效能：
- **Ray**：負責資源配置與非同步隊列。
- **vLLM**：負責 Rollout (採樣)。
- **NVIDIA AutoModel (搭配 FSDP2)**：負責訓練。

其執行時 (Runtime) 由三個部分組成：一個 Agent 池、一組位於請求路由器 (Request Router) 後方的 vLLM 引擎，以及單一的可訓練策略 Actor。

為了確保效能，Molt 採用了「部分 Rollout 暫停 (Partial Rollout Pauses)」機制：在 Actor 訓練時會暫停引擎，直接透過 NCCL 將 Actor 的分片 (shards) 廣播至各引擎，並恢復保留的請求，而非直接丟棄。

⚠️ **硬體門檻與適用場景**

雖然 Molt 提供了 Apache 2.0 授權、Slurm 腳本與預建容器，但該研究定位於「研究基礎設施」而非生產級訓練服務。其提供的範例配置假設使用 2 個節點（共 16 顆 H100 GPU），其中 8 顆用於訓練，8 顆用於 Rollout。

這使得 Molt 主要適用於：
- 前沿實驗室與具備充足資金的 AI 新創公司（進行 Post-training）。
- 金融、醫療與機器人領域的企業 AI 研究團隊（針對私有環境訓練 Agent）。
- 擁有多節點 H100/H200 存取權限的學術實驗室。

💡 **確保正確性的三大不變量 (Invariants)**

為了處理複雜的 Agent 任務（如多輪工具使用、程式碼執行、視覺語言環境），Molt 依據以下原則設計：
1. **Token 身份一致性**：定義軌跡的是採樣的 Token ID，而非重新 Tokenize 後的文本。
2. **策略版本語義**：可訓練的 Token 會保留其行為策略的對數機率 (log-probabilities)，非同步使用時會進行 Token 級別的修正。
3. **前向一致性**：Rollout 與 Actor 必須在模型語義上保持一致。針對 Mixture-of-Experts (MoE) 策略，Molt 採用了 **Rollout Routing Replay** 技術，讓訓練時的 Forward Pass 能重現 vLLM 採樣時選擇的專家 (experts) ID，避免數值差異導致的路由錯誤。

🎯 **實務啟示**

對於需要快速迭代 Agent 演算法的研究者而言，Molt 提供了一個「低摩擦」的環境。它不試圖重寫現有的優質工具（如 vLLM），而是透過精簡的介面將它們串聯，讓研究者的注意力能集中在演算法邏輯，而非維護複雜的訓練管線。

🔗 **來源**
- 標題：NVIDIA AI Releases Molt: A PyTorch-Native Agentic Reinforcement Learning Framework
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/01/nvidia-ai-releases-molt-a-pytorch-native-agentic-reinforcement-learning-framework/

#NVIDIA #NeMo #ReinforcementLearning #PyTorch #AgenticAI #MachineLearning #DeepLearning #vLLM #DistributedTraining #AIResearch
