---
title: "Via Negativa for AI Alignment: Why Negative Constraints Are Structurally Superior to Positive Preferences"
source: ChatPaper/AI
url: https://arxiv.org/abs/2603.16417
score: 124
model: gpt-4o-free
generated_at: 2026-03-18T20:47:31.444956
---

📌 Via Negativa for AI Alignment: 負面約束為何結構上優於正面偏好  

你以為讓模型學會「人類喜歡什麼」才是對齊的關鍵？最新研究指出，我們可能走錯了方向，只教模型「什麼是錯的」反而更穩定。  

🤔 正面偏好難以穩定：人類價值是連續且依賴情境的  
論文指出，正面偏好（「哪個更好」）本質上是連續的、隨情境變化的人類價值。因為無法窮盡列出所有偏好，模型容易學會表面相關的訊號，例如迎合使用者的說法（sycophancy），而非真正內化對齊目標。  

🧪 負面約束是離散且可驗證的邊界  
相對地，負面約束（「什麼是錯的」）被描述為離散、有限且可以獨立驗證的禁止規則。這類規則較易形成一個穩定的決策邊界，模型在學習時較不會被情境噪聲干擾。  

📊 為何負訊號方法在實證上表現不俗  
作者彙總了幾項近期實證結果：Negative Sample Reinforcement 在數學推理任務上與 PPO 持平；Distributional Dispreference Optimization 僅使用不偏好樣本即可有效訓練；Constitutional AI 在無害基準上優於純 RLHF。這些現象被解釋為負訊號結構優勢的體現。  

🔎 理論根源：波普爾的證誤與負知識認識論  
論文將此非對稱性追溯到波普爾的證誤原則——科學知識通過 falsification（證偽）累積，以及負知識 epistemology（知道什麼不對）在概念上更具確定性。這提供了為何負訊號在對齊上更具穩定性的哲學基礎。  

⚠️ 研究的邊界：理論框架為主，尚需更多實驗驗證  
目前的貢獻主要是理論闡述與對既有實證結果的重新解釋。文中未呈現新的大規模實驗或消融研究，因此理論的實際適用範圍與潛在限制仍需後續工作進一步驗證。  

🎯 對齊研究的轉向：從「學習偏好」到「學習拒絕」  基於上述分析，作者主張對齊社群應將重心從「學習人類偏好」轉移至「學習人類拒絕的內容」。這不僅能降低迎合風險，亦有望藉由明確的負約束設計出更可驗證、更安全的訓練流程。  

🔗 論文連結  
📝 Via Negativa for AI Alignment: Why Negative Constraints Are Structurally Superior to Positive Preferences  
👤 Quan Cheng (Tsinghua University)  
🔗 https://arxiv.org/abs/2603.16417  

你認為在模型訓練中，應該更多地設置「不能做什麼」而不是「應該做什麼」嗎？歡迎留言討論 👇  

#AI #Alignment #LLM #RLHF #Tsinghua #MachineLearning #AI安全
