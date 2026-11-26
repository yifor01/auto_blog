---
title: ByteDance Researchers Open-Sources Laminar, an Async Reinforcement Learning
  RL Post-Training Framework
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/24/bytedance-seed-laminar-async-rl-post-training-framework/
model: claude-code/sonnet
generated_at: '2026-11-26T01:07:40.153958'
score: 107
---

📌 ByteDance開源Laminar：非同步RL訓練，不再讓GPU等最慢的那條路徑

TL;DR：香港大學與ByteDance Seed開源Laminar，用完全解耦架構解決長尾rollout拖垮訓練吞吐量的問題。

訓練coding agent時最浪費GPU的瞬間，往往不是模型在算，而是整個叢集在等一條特別長的rollout軌跡跑完。這正是Laminar想解決的問題。

🤔 **為什麼rollout的尾巴會拖垮整個訓練**

香港大學與ByteDance Seed團隊開源了Laminar，一個針對LLM與long-horizon agent的強化學習（RL）後訓練框架。核心想法很直接：不要再強迫每一條軌跡、每一張GPU都等最慢的那一條跑完。對於訓練長且分佈偏態（skewed）rollout的coding agent團隊來說，這正是GPU時間流失最多的地方。Laminar把rollout、buffering、training與weight transfer拆成各自獨立的迴圈，分別運作。

🧩 **三層技術棧，三個設計原則**

專案建構在verl與Uni-Agent之上，以Apache-2.0授權釋出。官方部落格把整個技術棧分成三層：verl提供訓練與推論的運算後端；Uni-Agent負責agent執行、工具呼叫與sandbox；Laminar則負責叢集規模的調度。整體設計立基於三個原則：完全解耦、細粒度非同步，以及容錯。

在對應的研究論文中，relay被設計成CPU process，每臺rollout機器各一個，透過pipeline化的RDMA鏈路廣播權重；文中提到一個72B模型能在1.6秒內把權重傳播到其他127個relay。多數非同步系統採用version-mixed的partial rollout：每次權重更新都要中斷正在跑的軌跡，在新policy下重新開始，這會造成反覆的re-prefill。Laminar額外支援一種version-consistent模式：每條軌跡只用同一個policy版本跑完，各replica各自獨立更新權重，不需要全域的weight-switch barrier。部落格指出這能保留prefix KV cache完整，並主張在頻繁更新的情況下，re-prefill成本會隨序列長度以三次方的速度膨脹。至於已經在用舊版本跑的「尾巴」軌跡，則由Repack機制處理：把舊版本殘留的軌跡整合到較少的replica上，騰出來的replica就能立即載入新版本繼續工作。

容錯方面，故障被限制在local：如果某個rollout replica失敗，router只會隔離（fence）那一個replica，它重啟後從本地relay重新載入權重，並從自己已生成的token前綴繼續；就算失敗發生在權重載入當下，也不會卡住trainer。Trainer的checkpoint會同步對齊model狀態、prompt遊標與已發布的權重版本；laminar.eval則能在訓練過程中，同時以批次或串流方式評估多個常駐replica上的checkpoint。

🎯 **實務啟示**

研究團隊用Laminar訓練了Qwen3-Coder-30B-A3B-Instruct（資料來自SWE-rebench），並以greedy decoding在全部500個SWE-bench Verified任務上評估。如果你的團隊正在訓練長horizon的coding agent，且大量GPU時間都耗在等待拖尾的rollout，Laminar「完全解耦＋version-consistent」這套思路，以及把容錯限制在單一replica層級的做法，值得納入自建RL pipeline時的參考架構。

🔗 **來源**
- 標題：ByteDance Researchers Open-Sources Laminar, an Async Reinforcement Learning RL Post-Training Framework
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/24/bytedance-seed-laminar-async-rl-post-training-framework/

#ReinforcementLearning #RLHF #LLMTraining #ByteDance #OpenSource #AsyncRL #AgentTraining #MachineLearning #GPUOptimization #CodingAgents
