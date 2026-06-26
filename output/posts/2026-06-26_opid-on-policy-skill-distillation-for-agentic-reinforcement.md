---
title: 'OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.26790
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:06:15.573362'
---

📌 OPID：透過 On-Policy 技能蒸餾提升語言 Agent 訓練效能

TL;DR：利用已完成軌跡提取密集事後監督訊號，最佳化語言 Agent 的訓練效率與表現。

在強化學習（RL）訓練 Agent 的過程中，稀疏的獎勵（Sparse Reward）一直是巨大的挑戰。當 Agent 必須完成一連串複雜步驟才能獲得最終回饋時，學習效率往往低得令人沮喪。

🤔 **從稀疏獎勵到密集監督的轉化**

這篇論文提出了一個名為 OPID (On-Policy Skill Distillation) 的框架。其核心目標是解決語言 Agent 在訓練時面臨的效率問題。

🧩 **利用 hindsight 提取技能知識**

OPID 的設計理念在於「事後監督」（Hindsight Supervision）。該框架會從 Agent 已經完成的軌跡（Completed Trajectories）中，回溯並提取出密集的監督訊號。

具體流程為：
Agent 執行任務 → 產生完成軌跡 → 從中蒸餾（Distill）出具體的技能知識 → 將這些知識回饋至訓練過程。

透過這種 On-Policy 的蒸餾機制，Agent 不再僅依賴最終的成功或失敗，而是能從自己的成功經驗中學習到更細粒度的操作技巧。

🎯 **實務啟示**

對於開發 LLM-based Agent 的工程師來說，OPID 提供了一個思考方向：與其單純增加樣本量或調整獎勵函式，不如嘗試將 Agent 成功完成任務的「過程軌跡」轉化為訓練訊號，將「結果」蒸餾為「技能」，以降低對海量隨機探索的依賴。

🔗 **來源**
- 標題：OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning
- 連結：https://huggingface.co/papers/2606.26790

#AI #ReinforcementLearning #LLM #Agent #SkillDistillation #OnPolicy #MachineLearning #HindsightExperience #AgenticAI #RL
