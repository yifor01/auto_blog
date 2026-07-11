---
title: 'TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon
  Agent Training'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.05804
score: 30
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T13:41:43.150687'
---

📌 TurnOPD：讓 On-Policy 蒸餾具備「回合感知」能力

TL;DR：針對長視程代理訓練，提出 TurnOPD 策略，透過回合級預算分配解決全輪廓 rollout 的低效問題。

🎣 **長視程訓練的隱形殺手：Token 分佈不均與計算浪費**

在訓練具備長期規劃能力的 AI 代理（Agent）時，傳統的全輪廓 rollout（full-horizon rollouts）往往效率低下。更關鍵的是，生成的 Token 在時間軸上的分佈極度不均，導致計算資源大量浪費在無效或重複的區域。這不僅拖慢了訓練速度，更限制了模型在複雜任務中的表現上限。

🧩 **TurnOPD 的核心架構：回合級預算分配**

TurnOPD 針對上述痛點，提出了一種「回合感知」（Turn-Aware）的 On-Policy 蒸餾策略。其核心理念並非均勻地分配訓練預算，而是引入 Turn-level budgeting（回合級預算分配）機制。

這種設計旨在解決兩個主要問題：
1. **Full-horizon rollouts 的低效**：透過精確控制每個回合的計算資源，避免在整個長序列上進行不必要的探索。
2. **淺層 Token 集中問題**：調整 Token 生成的分佈，防止模型過度依賴短期回饋而忽視長期目標，確保訓練過程中的資訊流動更加均衡且有效。

📊 **技術實作邏輯**

雖然具體的數學公式未於摘要中詳述，但 TurnOPD 的運作邏輯可歸納為以下步驟：
- **識別回合邊界**：將長視程任務拆解為多個獨立的回合（Turns）。
- **動態預算分配**：根據每個回合的複雜度或資訊增益，動態調整 On-Policy 蒸餾過程中的計算資源預算。
- **高效蒸餾**：在預算範圍內執行 Policy Distillation，確保教師模型（Teacher Model）的知識能最有效地傳遞給學生模型（Student Model），同時減少冗餘計算。

⚠️ **限制與待確認細節**

目前的公開資訊僅涵蓋策略概念與解決的問題。具體的實驗資料（如訓練速度提升百分比、最終效能指標）、對比的 Baseline 模型名稱、以及適用的具體任務領域（如遊戲、程式生成或機器人控制），仍需等待論文全文發布後才能確認。

🎯 **實務啟示**

對於正在研發長視程代理的工程師而言，TurnOPD 提供了一個重要的方向：**不要均勻撒網，而要精準打擊**。在資源有限的情況下，透過對訓練過程中的「回合」進行細粒度的預算管理，可以顯著提升 On-Policy 方法的訓練效率。這意味著未來的 Agent 訓練框架可能需要引入類似「回合感知」的資源排程模組，以應對日益增長的序列長度需求。

🔗 **來源**
- 標題：TurnOPD: Making On-Policy Distillation Turn-Aware for Efficient Long-Horizon Agent Training
- 連結：https://huggingface.co/papers/2607.05804

#TurnOPD #OnPolicyDistillation #LongHorizonAgents #RLHF #AIResearch #HuggingFacePapers #EfficientTraining #BudgetAllocation #AgentTraining #MachineLearning
