---
title: "On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.11882
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-13T20:48:46.649839
---

📌 **從失敗軌跡學習的智能體自我進化**

你以為讓 AI 變得更安全只需要加更多規則？其實讓它從自己的失敗中學習，或許才是提升安全與效能的關鍵。

🤔 **安全與效能常被視為零和博弈**

在 LLM‑based 智能體的開發中，提升安全常伴隨效能下降，反之亦然。研究團隊指出，傳統的對齊方法多依賴事先規則或人類示範，難以在實際互動中即時調整安全與效能的平衡。

🧪 **以失敗軌跡為驅動的 on‑policy 自我進化迴圈**

FATE 框架提出一個 on‑policy 的自我迴流：智能體在執行任務時記錄失敗軌跡（即導致安全違規或效能低落的行動序列），將這些軌跡作為學習信號，透過 Pareto‑aware 的更新規則同時朝著更高安全與更好效能的方向演進。整個過程不需要離線重新訓練，而是在線上持續自我調優。

🔥 **Pareto‑aware 優化讓安全‑效能權衡更具彈性**

透過將失敗軌跡納入優化目標，FATE 能在安全與效能的 Pareto 前線上尋找更優的解。也就是說，在不犧牲效能的前提下提升安全門檻，或在保持安全水準的情況下提升任務完成率。作者認為這種「從失敗中學」的機制讓智能體能夠在真實交互中自發修正行為模式。

💡 **失敗不是終點，而是改進的訊號**

傳統強化學習多聚焦於獎勵最大化，往往忽略失敗所蘊含的結構性資訊。FATE 把失敗視為對策空間的負向梯度，利用這些梯度進行校正，使得智能體在面對類似情境時更有可能規避先前的錯誤。這種「失敗導向」的更新方式被認為是提升鲁棒性的潛在途徑。

⚠️ **實驗細節尚待進一步披露，需更大規模驗證**

目前公開的摘要僅描述了框架概念與優化目標，未提供具體的基準測試結果、樣本規模或 ablation 研究。因此，雖然理論上具備改進安全‑效能權衡的潛力，仍需在更多任務與環境中進行實證驗證，才能確定其在真實應用中的穩定性與擴展性。

🎯 **對工程師的啟示：將失敗納入回饋迴圈**

- 在構建 LLM‑based 智能體時，可考慮記錄並重新使用失敗軌跡作為額外的訓練信號。  
- 使用 Pareto 前線的概念，可視覺化安全與效能的 trade‑off，幫助團隊做出更明確的決策。  
- 初期可在模擬或受限環境中先驗證該迴圈是否能減少安全違規，再逐步擴展至產品環境。

🔗 **論文連結**  
📝 On-Policy Self-Evolution via Failure Trajectories for Agentic Safety Alignment  
👤 作者團隊（詳見論文）  
🔗 https://huggingface.co/papers/2605.11882  

你在開發 AI 智能體時，會如何利用失敗資訊來提升安全？歡迎在留言區分享你的經驗與想法 👇

#AI #LLM #AgentAlignment #Safety #ReinforcementLearning #HuggingFacePapers #FATE #自我進化
