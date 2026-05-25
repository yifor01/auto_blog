---
title: "SkillOpt: Executive Strategy for Self-Evolving Agent Skills"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.23904
score: 132
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:20:28.370225
---

📌 **SkillOpt：可控的文本空間優化器，讓 Agent 技能自我進化**

你以為 Agent 的技能只能靠手工調整或一次性生成？一種新方法把技能當成外部狀態來優化，卻不增加任何推論開銷。  
實驗顯示，在多個基準與模型上，它竟然全場領先。

🤔 **手工與一次性生成無法像深度學習優化那樣穩定提升技能**  
現有的 Agent 技能多半是人工撰寫、一次性 LLM 生成，或是鬆散控制的自我修訂。這些方式缺乏類似權重空間優化的紀律，難以在回饋中持續超越起點。SkillOpt 的核心主張是：將技能文件視為凍結 Agent 的外部狀態，採用優化器式的嚴格更新機制。

🧪 **可控的文字空間優化器：評分驅動的增删替編輯**  
SkillOpt 包含一個獨立的優化模型，將已評分的 rollout 轉化為單一技能文件的有界 add/delete/replace 編輯。只有當編輯嚴格提升留出驗證分數時才會被接受。設計中還加入了文字學習率預算、被拒編輯緩衝區以及 epoch 級的慢/ meta 更新，以確保訓練穩定，且在部署時零額外模型調用。

📈 **六個基準、七個目標模型、三種執行環境全場領先或持平**  
在 52 個 (model, benchmark, harness) 組合中，SkillOpt 均為最佳或與最佳持平，並擊敗了所有人工、一次性 LLM、Trace2Skill、TextGrad、GEPA 與 EvoSkill 的每個細胞競爭者。具體來說，在 GPT-5.5 上，直接聊天場景下平均無技能準確度提升 +23.5 點；在 Codex agentic 迴路中提升 +24.8 點；在 Claude Code 中提升 +19.1 點。遷移實驗進一步顯示，優化後的技能 artefactual 在不同模型規模、在 Codex 與 Claude Code 執行環境間，以及相近的數學基準上仍保有價值，無需再次優化。

💡 **將技能視為外部狀態，使優化過程可重現且無推論開銷**  
與傳統的權重空間優化類似，SkillOpt 把技能文件當作可優化的外部狀態，透過嚴格的驗證門檻與學習率預算，使更新過程具備可重現性。因為所有優化發生在離線階段，部署時不會產生額外的模型推論呼叫，這對於對延遲敏感的 Agent 應用尤為重要。

⚠️ **實驗主要聚焦在特定基準與模型，長期遷移能力尚需更多證據**  
雖然跨模型、跨執行環境的遷移實驗顯示正向結果，但論文尚未報告更長時程或更遠任務的表現。此外，實驗範圍限於所列的六個基準與三種執行 harness，其他領域的適用性仍需後續驗證。

🎯 **將技能文件納入優化流程，可獲得零開銷的效能提升**  
對於工程師而言，SkillOpt 提供了一種可控、基於編輯的技能改進工具：先收集任務 rollout 的分數，再讓優化模型產生受限的文本編輯，只有通過驗證的編輯才會被納入技能檔案。這意味著在不犧牲推論效率的前提下，持續提升 Agent 的任務表現。

🔗 **論文連結**  
📝 SkillOpt: Executive Strategy for Self-Evolving Agent Skills  
👤 Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou (Microsoft; Shanghai Jiao Tong University; Tongji University; Fudan University)  
🔗 https://arxiv.org/abs/2605.23904  

你目前是怎樣為 Agent 撰寫或更新技能的？SkillOpt 這種「外部狀態優化」的思路是否能改變你的工作流程？歡迎留言討論 👇  

#AI #Agent #SkillOptimization #Microsoft #LLM #AutoML #技術成長
