---
title: "AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.07926
score: 96
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:53:15.107522
---

📌 **AgentEscapeBench：長程工具推理測試**  

你以為 AI 已經能熟練使用工具？  
當任務需要跨越多個步驟的長程依賴時，  
表現卻會急劇下降。  

🤔 **長程工具推理仍是代理人的薄弱環節**  
現有評測多聚焦於單步或短範圍的工具使用，缺少對超出熟悉工作流、具備明確長程依賴的場景的考量。AgentEscapeBench 正是為了填補這個空白而設計的逃脫房間風格基準測試。

🧪 **270 個逃脫房間任務，五個難度層級**  
每個任務定義一個有向無環依賴圖，代理人必須呼叫真實外部函式、追蹤逐步揭露的隱藏狀態、傳遞中間結果，最後提交可決定性驗證的答案。基準支援完全自動評估，涵蓋五個難度層級（從 difficulty‑5 到 difficulty‑25），共 270 個實例。

📈 **隨著依賴深度增加，成功率呈指數下降**  
- 人類參與者：在 difficulty‑5 時成功率 98.3%，在 difficulty‑25 時降至 80.0%。  
- 最佳 LLM 代理人（共測試十六種）：在 difficulty‑5 時成功率 90.0%，在 difficulty‑25 時降至 60.0%。  

🔍 **失敗主要源於長程狀態追蹤、線索遵循與中間結果傳遞**  
軌跡分析顯示，模型在處理局部工具調用時表現尚可，但當需要保存並傳遞多步驟的資訊時，狀態追蹤中斷、對關鍵線索的遵循不足以及中間結果無法正確傳遞成為主要失因。

⚠️ **僅測試特定逃脫房間結構，泛化能力尚待觀察**  
基準設計圍繞有向無環依賴圖與明確的最終驗證目標，是否能直接推廣至更開放、結構較鬆散的真實工具使用場景仍需後續研究驗證。

🎯 **改進代理人時應著重長程上下文管理與中間結果的可靠傳遞**  
- 在訓練或提示設計中加入明確的狀態追蹤機制。  
- 強調代理人對線索的遵循與中間值的傳遞，而非僅追求單步工具調用的正確率。  
- 利用 AgentEscapeBench 作為診斷工具，檢視新訓練策略在深度依賴任務上的實際提升。

🔗 **論文連結**  
📝 AgentEscapeBench: Evaluating Out-of-Domain Tool-Grounded Reasoning in LLM Agents  
👤 Zhengkang Guo, Yiyang Li, Lin Qiu, Xiaohua Wang, Jingwen Xv (Fudan University; Meituan Longcat Team)  
🔗 https://arxiv.org/abs/2605.07926  

你在開發 LLM 代理人時，是否已經注意到長程依賴的挑戰？歡迎在留言區分享你的觀察與解決方案 👇  

#AI #LLM #Agent #ToolUse #Benchmark #Fudan #Meituan #MachineLearning #NLP #AgentEscapeBench
