---
title: Weak-to-Strong Generalization via Direct On-Policy Distillation
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.05394
score: 92
model: tencent/hy3:free
generated_at: '2026-07-14T08:00:09.762258'
---

📌 【Weak-to-Strong Generalization】利用 RL 政策位移，將小模型成果蒸餾至大模型

TL;DR：透過 Direct On-Policy Distillation，利用 RL 產生的政策位移作為隱式獎勵，實現高效的模型規模擴充套件。

🤔 **如何讓大模型繼承小模型的強化學習能力？**

當我們透過強化學習（RL）提升了小型模型的能力時，如何將這些進步有效地轉移（Transfer）到規模更大的模型上？傳統方法往往需要在目標大模型上重新執行昂貴且耗時的 RL 訓練，這在計算資源受限時極具挑戰。

🧩 **Direct On-Policy Distillation：將政策位移轉化為獎勵**

這項研究提出了一種名為 Direct On-Policy Distillation 的方法，其核心設計理念在於：

- **核心機制**：利用強化學習（RL）過程中所產生的「政策位移」（Policy Shift）作為一種「隱式獎勵」（Implicit Reward Signal）。
- **轉移流程**：將小型模型在 RL 訓練中獲得的改進，直接蒸餾給較大的目標模型。
- **效率優勢**：由於不需要在目標大模型上重新執行昂貴的 RL 流程，這為模型訓練的規模化（Scaling）提供了一種更高效的途徑。

🎯 **實務啟示**

對於資源有限的開發團隊，這種「從弱到強」（Weak-to-Strong）的蒸餾策略，提供了一種在不重複進行高成本 RL 訓練的情況下，實現模型效能擴充套件的新思路。

🔗 **來源**
- 標題：Weak-to-Strong Generalization via Direct On-Policy Distillation
- 連結：https://huggingface.co/papers/2607.05394

#MachineLearning #ReinforcementLearning #Distillation #ModelScaling #AIResearch #DeepLearning #OnPolicy #WeakToStrong #LLM #AIEngineering
