---
title: 'SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.14777
score: 109
model: tencent/hy3:free
generated_at: '2026-07-17T08:05:32.959588'
---

📌 【HuggingFace Papers】SEED：用後驗技能蒸餾補齊 Agent RL 監督缺口

TL;DR：SEED 把線上軌跡轉成自然語言技能再蒸餾回政策，緩解長程 Agent RL 獎勵稀疏問題。

當 LLM 被訓練成要跟環境多輪互動、呼叫工具、讀取回饋的 agent 時，一個尷尬的狀況出現：基於結果的 reinforcement learning (RL) 只在整段軌跡結束才給獎勵，中間每一步決策幾乎拿不到指引。這道「episode 級結果」與「token 級學習」之間的監督缺口，正是長程任務訓練效率的隱形天花板。

🤔 **Outcome-based RL 只給終點分數，中間決策靠猜**

摘要指出，現有的 outcome-based RL 提供實用的最佳化範式，但其稀疏的軌跡級（trajectory-level）獎勵，對中間決策提供的引導有限，導致在 episode 層級結果與 token 層級政策學習之間存在監督缺口。

🧩 **SEED 框架：讓政策自己分析軌跡、長出技能**

SEED（SElf-Evolving On-Policy Distillation）是一個自我演化框架，核心做法是把已完成的 on-policy 軌跡，在訓練時轉換成 hindsight skills（後驗技能），再把這些行為效應蒸餾回政策模型。流程可拆為三步：

- 第一步：先對政策模型做 fine-tuning，讓它能分析已完成的軌跡，產生自然語言技能，內容可能是可重複使用的工作流程、關鍵觀察、或避錯規則。
- 第二步：在 RL 階段，當前政策同時負責兩件事——收集軌跡，以及擔任分析器從這些軌跡中抽取後驗技能。政策更新因此同步改善後續決策與技能分析，使後驗監督隨政策一起演化。
- 第三步：在普通上下文與技能增強上下文下，重新對取樣動作打分，把技能引發的機率偏移轉換成密集的 token 級 on-policy 蒸餾訊號，與 outcome-based RL 聯合最佳化，確保輔助監督與當前軌跡分佈對齊。

📊 **在文字與視覺 Agent 任務上皆提升效能與樣本效率**

摘要提到，在基於文字與基於視覺的 agentic 任務上進行了廣泛實驗，SEED 一致地改善效能與 sample efficiency（樣本效率），並對未見過的場景展現穩健的泛化能力。具體資料與 baseline 對比細節摘要未提供。

🎯 **把「事後檢討」變成訓練訊號，值得借鏡**

對做 agentic RL 的團隊來說，SEED 的思路是把已完成軌跡的後見之明結構化為可蒸餾的密集訊號，而非只靠終點獎勵。若你正苦於長程任務獎勵稀疏、訓練樣本效率低，這種 on-policy 自我演化蒸餾的設計值得追蹤其開源程式碼實作。

🔗 **來源**
- 標題：SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning
- 連結：https://huggingface.co/papers/2607.14777

#AgentRL #ReinforcementLearning #LLMAgent #Distillation #SEED #OnPolicy #SampleEfficiency #HindsightSkill #TokenLevelReward #SelfEvolving
