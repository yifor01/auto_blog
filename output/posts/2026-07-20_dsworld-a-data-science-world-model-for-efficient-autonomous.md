---
title: 'DSWorld: A Data Science World Model for Efficient Autonomous Agents'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.15901
score: 101
model: tencent/hy3:free
generated_at: '2026-07-20T08:49:30.505336'
---

📌 【HuggingFace Daily Papers】DSWorld：用世界模型替資料科學代理省下大量運算

TL;DR：DSWorld 以世界模型預測操作結果，代理訓練加速約 14 倍、推論快 3–6 倍。

現有的自主資料科學代理（autonomous data science agents）雖然在資料理解與決策上表現不錯，但實際跑起來往往靠反覆試錯，每一次嘗試都燒掉昂貴的運算資源。如果能先在腦中模擬「這步操作會發生什麼」，是不是就不用每步都真實執行？

🤔 **試錯式工作流程是自主代理的運算瓶頸**

論文指出，當前自主資料科學代理高度依賴 trial-and-error 的工作流程，涉及昂貴的計算成本。這個瓶頸促使研究者思考：能否在建構真實執行前，就先預測資料科學操作會帶來的影響。

🧩 **DSWorld 框架：把環境狀態轉換先模擬一遍**

作者提出 Data Science World Model 的概念，透過條件化於「當前工作流程狀態」與「候選操作」，來預測環境狀態的轉換（state transitions）。實作的 DSWorld 框架結合了四個設計：

- 結構化狀態建構（structured state construction）
- 成本感知路由（cost-aware routing）
- 輕量級真實執行（lightweight real execution）
- 基於 LLM 的模擬器，用於昂貴操作（LLM-based simulator for expensive operations）

📊 **訓練資料與錯誤感知的最佳化策略**

為了支援訓練，作者建構了一個 8K 規模的轉換軌跡資料集（transition trajectory dataset）。同時提出 Reflective World Model Optimization，這是一種錯誤感知的 reinforcement learning 策略，用來改善狀態轉換的預測能力。

📊 **訓練加速 14 倍，推論快 3–6 倍，預測勝出 35.6%**

實驗結果顯示：

- 基於 RL 的代理訓練加速約 14 倍
- 基於搜尋的推論（search-based inference）加速約 3–6 倍
- 在轉換預測任務上，比最強的 LLM baseline 高出 35.6%
- 上述加速同時維持了具競爭力的效能

🎯 **把模擬擺在真實執行前面，才是省運算的關鍵**

對工程師來說，DSWorld 展示了一條務實路線：用世界模型先過濾掉明顯無效的操作，只在必要時做輕量真實執行，昂貴操作交給 LLM 模擬。在運算預算有限的自主代理場景，這種 cost-aware 的設計值得直接借鏡。

🔗 **來源**
- 標題：DSWorld: A Data Science World Model for Efficient Autonomous Agents
- 連結：https://huggingface.co/papers/2607.15901

#DataScience #WorldModel #AutonomousAgents #LLM #ReinforcementLearning #DSWorld #Simulation #CostAware #TrajectoryDataset #HuggingFacePapers
