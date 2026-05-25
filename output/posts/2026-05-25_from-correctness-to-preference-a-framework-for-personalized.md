---
title: "From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.23382
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:24:27.348046
---

📌 【中科大+阿里巴巴】個人化 Agentic RL 框架：PARPO 與 PSGM  

同一個問題，對不同用戶可能需要完全不同的工具使用策略——傳統強化學習卻難以區分。  

🤔 **用戶需求多樣化，通用獎勵無法捕捉個體偏好**  
現有 Agentic RL 在有明確成功訊號的任務上表現不錯，但真實場景中，同樣的查詢常因使用者背景、習慣或目標而需要不同的規劃路徑與工具選擇。若仍用單一的通用獎勵函式，訊號會被平均化，導致代理無法學習到使用者特有的行為模式。  

🧪 **將個人化嵌入訓練時的獎勵分離與圖記憶機制**  
研究團隊提出一個統一的個人化 Agentic RL 框架，核心包含兩部分：首先是 **Personalized Anchor Reward‑Decoupled Policy Optimization (PARPO)**，它把通用任務品質獎勵與個人化偏好獎勵分開處理，並使用使用者專屬的錨點來穩定不同獎勵尺度下的學習過程；其次是兩階段的偏好解耦獎勵模型與 **Preference‑Aligned Skill Evolution Graph Memory (PSGM)**，前者提供個人化的監督訊號，後者以圖結構儲存並檢索與使用者偏好對齊的技能。這三者共同形成偏好辨識 → 政策優化 → 結構化技能積累的閉環。  

💡 **在三個基準上持續勝過現有記憶與強化學習基線**  
在 ETAPP、ETAPP‑Hard 以及 SJAgent 三個數據集上的實驗顯示，該框架在任務成功率與偏好適配度上均顯著優於現有的記憶輔助強化學習方法與傳統基線。實驗亦表明，透過 PARPO 的獎勵分離與 PSGM 的偏好對齊檢索，代理能在不牺牲通用任務表現的前提下，更好地捕捉並執行使用者特定的策略。  

⚠️ **實驗基於特定基準，長期偏好穩定性尚未探討**  
目前的評價僅限於上述三個基準，未涉及跨域泛化或長期使用者偏好漂移的情況；此外，框架的複雜度較高，需額外的計算資源來維護使用者錨點與圖記憶結構。  

🎯 **個人化代理設計可先嘗試獎勵分離與圖式記憶**  
對於工程師而言，若要開發能依使用者偏好調整行為的助手或工具，可參考 PARPO 的思路：先把任務品質與使用者偏好分開建模，再使用使用者特定的錨點來 stabilise 學習；同時，採用圖結構來儲存與檢索個人化技能，有助於在後續互動中快速呼叫符合偏好的行為模式。  

🔗 **論文連結**  
📝 From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning  
👤 Ranxu zhang, zeyang li, Jiacheng Huang, Rui Zhang, Xiaozhou Xu (University of Science and Technology of China; Alibaba Group)  
🔗 https://arxiv.org/abs/2605.23382  

你認為在開發個人化 AI 助手時，哪個部分（獎勵分離、錨點設計、圖記憶）最具挑戰性？歡迎留言討論 👇  

#AI #ReinforcementLearning #AgenticRL #個人化 #PARPO #PSGM #中科大 #阿里巴巴 #機器學習 #強化學習 #技術趨勢
