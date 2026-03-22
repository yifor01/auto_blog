---
title: "RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.03078
score: 108
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-04T19:12:32.370167
---

📌 【Fudan 等校最新研究】LLM Agent 探索受限？這篇論文讓 AI 學會「借鏡他人」

Agentic Reinforcement Learning 讓 LLM 代理具備了多步驟、工具整合的推理能力，但它們的探索策略一直受限於自身生成的路徑。這意味著它們只能在自己的思考框架內打轉，難以發現新的解決路徑。

🤔 **LLM Agent 為什麼探索能力受限？**

現有的 Agentic RL 方法主要依賴純 on-policy 的探索策略，也就是說，代理只能基於自己當前的決策路徑進行下一步推理。這就像一個新手程式設計師只看自己寫的程式碼來學習，從來不看別人的實作，自然很難跳出固有的思維框架。

🧪 **RAPO 如何讓 Agent 借鏡他人？**

來自復旦大學、浙江大學和 UC Davis 的研究團隊提出了 Retrieval-Augmented Policy Optimization (RAPO)，核心創新是讓 LLM Agent 能「借鏡」他人的探索路徑。

RAPO 將訓練過程拆成兩個階段：

**1. 混合策略代理推理 (Hybrid-policy Agentic Rollout)**
讓代理不只看自己的路徑，還能動態融入從外部資料庫中檢索到的 off-policy 步驟級 trace。這就像讓代理在思考時，能隨時調用其他高手的解題思路。

**2. 檢索感知策略優化 (Retrieval-aware Policy Optimization)**
用檢索獎勵和重要性重塑來校準策略梯度估計，穩定訓練並優先探索那些被檢索路徑所揭示的有價值方向。

💡 **為什麼這很重要？**

想像你在學習寫程式時，不只是自己寫 Code，還能隨時看到優秀的開源專案是如何解決類似問題的。RAPO 讓 LLM Agent 具備了這種「站在巨人肩膀上」的能力，從而突破自身思維的侷限。

📊 **實驗結果：5% 性能提升，1.2 倍訓練加速**

在 14 個數據集、3 種代理推理任務上的廣泛實驗顯示，RAPO 平均提升了 5.0% 的性能，同時訓練效率提升 1.2 倍。這意味著不僅效果更好，還能更快收斂。

⚠️ **RAPO 的關鍵洞察**

傳統的 off-policy 方法通常使用完整的軌跡進行策略估計，但這篇論文發現，對於 Agentic RL 來說，更重要的是**步驟級的探索動態**。就像學習時，不只是看別人的完整專案，而是關注對方在解決某個具體問題時的思考轉折點。

🎯 **這對 LLM Agent 的未來意味著什麼？**

RAPO 展示了一種讓 LLM Agent 更聰明地探索世界的可能性。未來的代理不會只是「試錯機器」，而是能夠：

- 主動學習他人的成功經驗
- 動態調整探索策略
- 更快收斂到更優的解決方案

🔗 **論文連結**
📝 RAPO: Expanding Exploration for LLM Agents via Retrieval-Augmented Policy Optimization
👤 Siwei Zhang, Yun Xiong, Xi Chen, Zi'an Jia, Renhong Huang
🏫 Fudan University; Zhejiang University; UC Davis
🔗 arxiv.org/abs/2603.03078

你怎麼看待讓 AI 代理「借鏡他人」的能力？歡迎分享你的想法 👇

#AI #ReinforcementLearning #LLM #AgenticAI #FudanUniversity #ZhejiangUniversity #UCDavis #機器學習 #人工智慧
