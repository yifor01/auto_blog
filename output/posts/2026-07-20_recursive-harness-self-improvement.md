---
title: Recursive Harness Self-Improvement
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.15524
score: 96
model: tencent/hy3:free
generated_at: '2026-07-20T08:51:14.658554'
---

📌 【HuggingFace Daily Papers】用 RHI 讓輕量 Agent 超越高推理成本設定

TL;DR：RHI 迭代最佳化使用者自建 harness，少數回合即提升軌跡品質並省下最多 60% 推論成本。

當大家都在堆高 LLM 的推理運算量（reasoning effort）來換取效能，一篇新論文指出：真正該動的，可能是包住模型的那層「harness」。

🤔 **Harness 不只是推論支架，更是訓練資料的源頭**

摘要提出 model–harness co-evolution 的觀點：harness 不只是 inference-time 的腳手架，它的執行軌跡（execution traces）會回頭影響未來 foundation model 的訓練資料。這催生了 harness-in-the-loop learning——同時最佳化 harness 的即時 agent 表現，以及其產生軌跡對未來模型訓練的品質。但持續改動 provider 建好的 scaffold 既貴又耗人力，因此作者轉向一個輕量問題：針對任務最佳化「使用者自建的 harness」，能否在極少更新回合內改善軌跡品質？

🧩 **RHI：把 Agent Loop 當成 Prompt 規格來迭代精煉**

為此，作者提出 Recursive Harness Self-Improvement (RHI)。其核心設計是將 harness 表示為 agent loop 的 prompt-level 規格，並基於自身的修訂歷史（revision history）取得 pairwise feedback，反覆精煉這份規格。也就是說，harness 不是改程式碼，而是在 prompt 層級自我修正，且只需少數更新迭代。

📊 **30 個合成 ML 研究任務：少數迭代就拉高天花板**

在橫跨量化金融、機器人學與藥學的 30 個合成機器學習研究任務上，僅需幾次 RHI 迭代，就能大幅抬高低推理成本（low-reasoning-effort）agent 的效能天花板：

- 低推理 effort agent + RHI：表現超越同設定下的最大推理 effort 版本
- 推論成本：最多降低 60%

作者進一步分析，這些增益主要來自更好的任務特定上下文管理（task-specific context management），也就是更有效的 inter-agent 資訊流，而非更長的推理軌跡。

💡 **從資訊理論角度看 RHI 的隱含目標**

論文最後將此行為形式化為一個資訊理論假說，用以描述 RHI 的隱含最佳化目標，並主張 RHI 可視為 model–harness co-evolution 範式下、用於持續學習（continual learning）的實用演算法。

🎯 **實務啟示**

對工程師而言，與其盲目調高模型的推理預算，不妨把 agent 外層的 harness 視為可自我最佳化的 prompt 規格：用少量迭代與自身修訂回饋來精煉它，有可能以更低推論成本達到甚至超越重推理設定的表現，同時產出更高品質的執行軌跡供日後訓練使用。

🔗 **來源**
- 標題：Recursive Harness Self-Improvement
- 連結：https://huggingface.co/papers/2607.15524

#RHI #Harness #AgentLoop #SelfImprovement #LLM #ContinualLearning #ModelHarnessCoEvolution #PromptOptimization #InferenceCost #AgenticSystem
