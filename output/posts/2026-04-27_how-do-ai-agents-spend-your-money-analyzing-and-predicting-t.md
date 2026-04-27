---
title: "How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.22750
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-04-27T19:58:52.855012
---

📌 【Google DeepMind & Microsoft AI 聯合研究】花最多 token 的 Agent，不一定寫得出最好的 Code

隨著 AI Agent 全面滲透軟體開發流程，token 消耗正以百倍速度膨脹。一個直覺的假設是：花更多 token ＝ 更高品質。但最新研究顯示，這不僅未必成立，甚至可能讓成本失控、效益邊際遞減。

🤔 **Agent 讓開發變「自動」，卻讓成本變「不可控」**

當 AI Agent 被部署在複雜的人機協同工作流，token 消耗已不再是邊際成本，而是核心架構風險。三大問題浮現：Agent 把 token 花在哪裡？哪個模型最 token-efficient？以及，Agent 能否在執行前預測自己的開銷？

🧪 **8 個前沿模型 × SWE-bench Verified 的 token 解剖實驗**

本研究首次系統性分析 Agentic 編碼任務的 token 消耗模式。  
- 數據來源：SWE-bench Verified  
- 模型陣容：8 個前沿 LLM（涵蓋 Kimi-K2、Claude-Sonnet-4.5、GPT-5 等）  
- 分析對象：完整執行軌跡（trajectories）  
- 評估維度：token 消耗分佈、模型間效率差異、以及自我成本預測能力

☁️ **輸入 token 吃掉 1000 倍成本，且高消耗 ≠ 高準確率**

- Agentic 編碼任務的 token 消耗，達到傳統 code reasoning / code chat 的 **1000 倍**  
- 成本驅動主因是「輸入 token」而非輸出 token  
- 同一任務不同執行間的 token 差異可達 **30 倍**  
- 準確率常在「中間成本」達峰值，隨著 token 增加而飽和，甚至持平或下降  

📉 **Kimi-K2 與 Claude-Sonnet-4.5 平均多耗 150 萬 token，勝負不在速度而在效率**

在相同任務下：  
- Kimi-K2 與 Claude-Sonnet-4.5 比 GPT-5 **平均多消耗超過 150 萬 token**  
- 模型間 token 效率差異顯著，選型直接決定成本曲線  
- 人類專家評估的「任務難度」與實際 token 成本僅弱相關，意即「覺得難」不代表「算得多」

🧠 **我們以為 Agent 能計劃開銷，結果它連自己的用量都猜不准**

- 模型對自身 token 使用的預測能力普遍薄弱  
- 預測值與實際值的相關性最高僅 **0.39**  
- 系統性低估真實成本，揭示目前 Agent 缺乏成本自我感知能力

⚠️ **僅限編碼任務與短期軌跡，長期經濟與泛化性仍未知**

- 研究範圍限於 SWE-bench Verified 的編碼場景  
- 未涵蓋多輪迭代維護或跨項目遷移  
- 長期成本累積與模型更新對效率的影響尚待追蹤

🎯 **把 token 當指標，把預算當設計，依賴刻意規劃而非盲目擴容**

- 成本控制必須前置：將 token 預算納入 Agent 架構設計  
- 引入中繼評估與提早終止機制，避免邊際遞減陷阱  
- 選型不只看能力，也要看 token-efficiency 與穩定性  
- 人機協同流程中，保留成本可觀察層與預警機制

🔗 **論文連結**  
📝 How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks  
👤 Longju Bai, Zhemin Huang, Xingyao Wang, Jiao Sun, Rada Mihalcea  
🏛 University of Michigan; Stanford University; All Hands AI; Google DeepMind; Microsoft AI; MIT  
🔗 https://arxiv.org/abs/2604.22750

你的團隊在導入 AI Agent 時，是否把 token 消耗納入核心指標？歡迎分享實務經驗與控管策略 👇

#AI #Agent #TokenEfficiency #SoftwareEngineering #CostControl #MachineLearning #DeepLearning #GoogleDeepMind #MicrosoftAI #GenAI
