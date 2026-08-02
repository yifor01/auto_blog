---
title: 'Conformal Thinking: Risk Control for Reasoning on a Compute Budget'
source: Apple ML
url: https://machinelearning.apple.com/research/conformal-thinking-risk-control
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:50:41.396728'
---

📌 【Apple ML】Conformal Thinking：在運算預算與推理風險之間取得最佳平衡

TL;DR：透過分佈自由的風險控制框架，在保證錯誤率的前提下，動態調整 LLM 推理的 token 預算。

當 LLM 透過 test-time scaling 提升準確率時，我們面臨一個兩難：該花多少 token 預算才夠？花太多會浪費運算資源，花太少則會降低可靠性。

🤔 **推理預算的「風險-準確率」權衡難題**

目前的 LLM 推理傾向於「適應性推理（adaptive reasoning）」，即在能提升可靠性時增加 token 投入，而在額外計算無助時提前停止。然而，如何設定 token 預算以及停止推理的閾值（threshold）是一個實務挑戰，這涉及到風險與準確率之間的權衡。

🧩 **將預算設定重新定義為「風險控制」**

Apple ML 提出的 Conformal Thinking 框架，將預算設定問題轉化為風險控制問題，目標是在限制錯誤率（error rate）的同時，將運算量最小化。該框架引入了兩種停止機制：

- 上限閾值（Upper Threshold）：當模型表現出足夠信心時停止推理，此時面臨的是輸出錯誤的風險。
- 參數化下限閾值（Parametric Lower Threshold）：針對無法解決的例項提前停止，此時面臨的是過早停止的風險。

透過在驗證集上使用分佈自由（distribution-free）的風險控制方法，該框架能根據使用者設定的目標風險，最佳化地指定這兩種停止機制。

📊 **實驗證明能有效降低運算成本且符合風險目標**

在多樣化的推理任務與模型上，實驗結果顯示此風險控制方法具有顯著成效：
- 下限閾值與整合停止機制（ensemble stopping mechanisms）帶來了明顯的運算效率提升。
- 在提升效率的同時，能嚴格遵守使用者指定的風險目標（risk target）。

🎯 **實務啟示**

對於需要大規模部署 LLM 推理的工程師而言，這提供了一種量化管理運算成本的方法。不再需要憑感覺設定 token 限制，而是可以定義「可接受的錯誤率」，讓系統自動決定哪些問題需要深度思考，哪些應快速跳過，從而最佳化推論成本。

🔗 **來源**
- 標題：Conformal Thinking: Risk Control for Reasoning on a Compute Budget
- 作者／機構：Xi Wang, Anushri Suresh, Alvin Zhang, Rishi More, William Jurayj, Benjamin Van Durme, Mehrdad Farajtabar, Daniel Khashabi, Eric Nalisnick @ Apple ML / Johns Hopkins University
- 連結：https://machinelearning.apple.com/research/conformal-thinking-risk-control

#LLM #Reasoning #RiskControl #ComputeBudget #TestTimeScaling #MachineLearning #AdaptiveReasoning #AppleML #Efficiency #ConformalPrediction
