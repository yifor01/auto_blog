---
title: THUDM/slime
source: GitHub Trending
url: https://github.com/THUDM/slime
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:34:53.349864'
---

📌 【THUDM 開源】slime：支撐 GLM 系列模型的 RL 後訓練框架

TL;DR：結合 Megatron 與 SGLang，提供高效能訓練與靈活數據生成的 RL Scaling 框架。

在強化學習（RL）的後訓練過程中，開發者經常面臨一個痛點：訓練器、Rollout 服務與 Agent 框架之間彼此脫節，導致系統變成一堆沉重的獨立組件，維護與除錯極其困難。

🧩 **將訓練與 Rollout 整合在同一路徑**

slime 的設計核心在於打破碎片化，將 Megatron 的訓練能力與 SGLang 的推論能力深度整合。其設計目標是讓「高效能訓練」與「靈活數據生成」相互強化，而非僅僅是工具的堆疊。

在 slime 的架構中，以下流程全部流經同一條「訓練 / Rollout / Data Buffer」路徑：
- Megatron 訓練
- SGLang Rollout
- 自定義數據生成
- 獎勵計算 (Reward Computation)
- 驗證器回饋 (Verifier Feedback)
- 環境互動 (Environment Interaction)

🚀 **高效能訓練與靈活的數據生成**

- **高效能訓練**：透過連接 Megatron 與 SGLang，支持多種模式下的高效能訓練。
- **靈活數據生成**：提供自定義的數據生成介面與基於伺服器的引擎，允許開發者建立任意的訓練數據生成工作流。

💡 **經由 GLM 系列模型驗證的實戰能力**

slime 並非僅提供單一範例，而是一個經過完整訓練迴路驗證的框架。它直接支撐了多個 SOTA 等級模型的發布，包括：
- GLM-5.2、GLM-5.1、GLM-5
- GLM-4.7、GLM-4.6、GLM-4.5

📊 **以「正確性」為優先的基礎設施**

由於 RL 的 Bug 往往是「靜默」的（不報錯但效果不佳），slime 在工程實踐上採取以下策略：
- **明確的數據流**：保持 Dataflow 透明，降低除錯難度。
- **獨立除錯路徑**：支持單獨的 Rollout-only 與 Train-only 除錯模式。
- **工程化優先**：將可再現性 (Reproducibility)、容錯能力 (Fault Tolerance)、追蹤 (Tracing)、效能分析 (Profiling) 與 CI 視為一等公民。

🎯 **實務啟示**

對於需要進行 RL Scaling 的工程師來說，slime 提供了一個「體量適中」且「經過實戰驗證」的參考實現。它證明了將訓練與推論路徑統一能有效降低系統複雜度，對於追求模型穩定性與開發效率的團隊具有高度參考價值。

🔗 **來源**
- 標題：THUDM/slime
- 作者／機構：THUDM
- 連結：https://github.com/THUDM/slime

#RL #PostTraining #LLM #Megatron #SGLang #GLM #ReinforcementLearning #MachineLearning #OpenSource #THUDM
