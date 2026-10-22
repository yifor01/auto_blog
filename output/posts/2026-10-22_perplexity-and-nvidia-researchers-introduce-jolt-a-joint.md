---
title: 'Perplexity and NVIDIA Researchers Introduce JOLT: a Joint Teacher-Student
  Reinforcement Learning Method'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/21/perplexity-jolt-joint-on-policy-learning-teaching/
model: claude-code/sonnet
generated_at: '2026-10-22T20:44:10.928940'
score: 102
---

📌 Perplexity × NVIDIA 的 JOLT：教師也要一起練，學生才學得快

TL;DR：JOLT 讓教師與學生角色在同一個模型中聯合訓練，MATH 任務僅用約六分之一的 token 就追平 GRPO 準確率。

強化學習做後訓練時，一整段冗長的嘗試往往只換來一個獎勵分數，模型根本不知道哪一步做對了、哪一步做錯了。這個稀疏獎勵問題，正是 Perplexity 與 NVIDIA 研究團隊這次想解決的。

🤔 **稀疏獎勵的老問題，teacher 卻可能在「抄答案」**

像 GRPO 這類 outcome-reward RL，每次嘗試只給一個獎勵，訊號稀疏，也不說明是哪些 token 真正有貢獻；在長鏈的 agentic 任務上，成功案例本就稀少，學習速度因此很慢。On-Policy Distillation 的做法是找一個更強的 teacher，對 student 產生的每個 token 評分，藉此緩解稀疏性。On-Policy Self-Distillation（OPSD）更進一步，不另外找 teacher，而是讓同一個模型在拿到「特許資訊」（例如已驗證過的解答）時，自己扮演 teacher。

研究團隊指出這還不夠：手上握有答案的 teacher，可能會抄捷徑，走一條 student 根本學不來的路，給出的指導超出 student 能力所及。論文中也觀察到，在 MATH 任務訓練過程中，OPSD 的 teacher 與 student 之間的分歧會逐漸擴大。

🧩 **讓 teacher 的回饋方向跟 student 的獎勵梯度一致**

JOLT（Joint On-policy Learning and Teaching）同時訓練一個共享模型的兩個角色：teacher 看得到特許資訊，student 看不到；關鍵差異在於 teacher 本身也會被訓練，確保它的回饋始終有用。方法核心是追求一個「reward-consistent」的 teacher：它的 distillation 更新方向應該要跟 student 的獎勵梯度方向一致，理想中的 teacher 會偏好高 advantage 的動作，同時盡量貼近 student 目前的策略，而不是遠遠跑在前面抄答案。

📊 **5 種設定全面贏過 GRPO，MATH 準確率省下 6.5 倍 token**

研究團隊在 5 種設定下測試，每種設定搭配不同的基礎模型與不同類型的特許資訊，結果 JOLT+（含 student 獎勵的版本）在每一種設定下的平均分數都最高。

| 評測任務 | GRPO | JOLT+ | 差距 |
|---|---|---|---|
| GSM8K | 基準 | +1.5 | 勝出 |
| MATH | 68.36%（plain JOLT 對照） | 72.14%（plain JOLT）/ +4.2（JOLT+） | 勝出 |
| LCBv6 | 基準 | +3.0 | 勝出 |
| AppWorld | 基準 | +9.9 | 勝出 |
| Terminal-Bench 2.1（pass@1 / pass@32） | 8.25% / 30.34% | 10.96% / 34.83% | 勝出 |

值得注意的是，即使是不含 student 獎勵的「plain JOLT」，在 MATH 上也已經贏過 GRPO（72.14% 對 68.36%）。

在 token 效率方面，研究團隊針對 MATH 任務，把準確率對訓練 token 預算擬合曲線：要達到 63.44% 準確率，GRPO 的 checkpoint 用掉 840 萬個已處理訓練 token，JOLT 擬合曲線只需 130 萬個，等於減少 6.5 倍；若只算 completion token，差距擴大到約 13 倍。在 55% 至 65% 準確率的區間內，省下的 token 比例落在 4.3 倍到 7.4 倍之間。JOLT 最終也收斂在更高的準確率天花板，接近 72%，相較之下 GRPO 約 70%、OPSD 約 62%。作為對照，Terminal-Bench 的基礎模型本身只有 5.18% pass@1、22.81% pass@32。

⚠️ **數據全部來自 Perplexity 自家實驗**

以上所有分數均來自 Perplexity 在 JOLT 論文中自行執行的實驗結果，且各方法的超參數都是分別調校過的，仍屬自我回報的結果，尚待第三方或更多外部場景驗證。

🎯 **實務啟示**

對正在跑 RL 後訓練的團隊來說，JOLT 把「teacher 要不要被訓練」這個看似細節的選擇，直接轉化成實際的算力問題：同樣的準確率目標，用更一致的 teacher 回饋，就能用遠少的訓練 token 達到，對長鏈 agentic 任務這種本來訓練成本就高的場景尤其有吸引力。

🔗 **來源**
- 標題：Perplexity and NVIDIA Researchers Introduce JOLT: a Joint Teacher-Student Reinforcement Learning Method
- 作者／機構：Asif Razzaq（MarkTechPost）；研究團隊來自 Perplexity 與 NVIDIA
- 連結：https://www.marktechpost.com/2026/10/21/perplexity-jolt-joint-on-policy-learning-teaching/

#ReinforcementLearning #JOLT #Perplexity #NVIDIA #GRPO #SelfDistillation #LLMPostTraining #OnPolicyLearning #AgenticAI #MachineLearning
