---
title: "StoryAlign: Evaluating and Training Reward Models for Story Generation"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.04831
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:24:38.490244
---

📌 【Tsinghua】StoryAlign：首個故事偏好基準與模型  
你以為大語言模型寫出的故事已經夠好？實際上，現有獎勵模型只能在三分之一的情況下選出人類偏好的故事。  
StoryAlign 提出 StoryRMB 基準與 StoryReward 模型，將故事生成的對齊推進到新階段。  

🤔 **現有故事生成仍缺乏人類偏好的量化衡量**  
大型語言模雖能產出流暢文字，但在複雜敘事結構與人類偏好方面仍與人類創作有落差。主要原因是缺乏對人類故事偏好的有效建模，而這類偏好本具主觀性且研究不足。  

🧪 **構建 1,133 筆人類驗證的故事偏好基準 StoryRMB**  
研究團隊首次提出 StoryRMB 基準，包含 1,133 組經人工驗證的樣本，每組由一個提示、一個人類偏好的故事（chosen）以及三個被排斥的故事（rejected）組成，用以評估獎勵模型對故事偏好的辨識能力。  

 **現有獎勵模型在 StoryRMB 上僅達 66.3% 準確率**  
在 StoryRMB 基準上，現有最佳的獎勵模型僅能達到 66.3% 的正確選擇率，顯示目前的模型在捕捉人類故事偏好方面仍有顯著不足。  

💡 **利用 約 100k 高品質故事偏好對訓練出 StoryReward，顯著超越更大模型**  
為彌補此缺口，團隊構建了約 100,000 組高品質的故事偏好數據，並在此基礎上訓練出 StoryReward 模型。StoryReward 在 StoryRMB 上達到最先進表現，且優於許多參數量更大的現有獎勵模型。  

⚠️ **基準規模有限且僅評估靜態選擇，長期生成一致性尚未驗證**  
StoryRMB 的樣本數相對有限，且評估焦點在單次最佳故事的選擇（best‑of‑n），未涵蓋長篇故事的連貫性與長期偏好一致性，這方面的效果仍需後續研究驗證。  

🎯 **在 Best-of-n 應用中驗證 StoryReward 能選出更符合人類偏好的故事，並開放資源**  
研究進一步將 StoryReward 應用於 best‑of‑n（BoN）故事生成任務，實驗顯示其選出的故事整體更符合人類偏好。為促進後續研究，團隊將開放 StoryRMB 數據集、StoryReward 模型及相關程式碼（GitHub：https://github.com/THU-KEG/StoryReward）。  

🔗 **論文連結**  
📝 StoryAlign: Evaluating and Training Reward Models for Story Generation  
👤 Haotian Xia, Hao Peng, Yunjia Qi, Xiaozhi Wang, Bin Xu @ Tsinghua University  
🔗 論文：https://arxiv.org/abs/2605.04831  

你對使用獎勵模型來引導故事生成有什麼經驗或看法？歡迎在留言區分享 👇  

#AI #StoryGeneration #RewardModel #Tsinghua #LLM #NLP #MachineLearning #StoryAlign #StoryReward
