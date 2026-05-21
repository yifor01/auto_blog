---
title: "Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.20834
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:52:35.970129
---

📌 【HKUST 等最新研究】DPO 與 RLHF 等價性其實有條件？  

你以為 DPO 已經證明與 RLHF 完全等價，可以放心取代複雜的強化學習流程？實際上，這種等價性依賴一個常被忽略的隱含假設——一旦該假設失效，DPO 可能在降低自身損失的同時，反而學會偏好人類不喜歡的回答。  

🤔 **研究背景**  
當 DPO 被視為 RLHF 的簡化替代方案時，一個關鍵假設常被忽視：RLHF 最佳策略必須傾向於人類偏好的回答。  

🧪 **研究設計**  
作者先以理論推導證明 DPO 與 RLHF 的等價性僅在該假設成立時成立；進一步刻畫假設違反時的失敗模式，並提出 Constrained Preference Optimization (CPO) 作為補救方案。最後在標準基準上進行實驗，驗證 CPO 的表現。  

🔥 **核心發現**  
當隱含假設不成立時，DPO 最適化的是相對於參考策略的優勢，而非絕對對齊人類偏好；此時會出現「病態收斂」——策略在降低 DPO 損失的同時，實際上更偏好人類不喜歡的回答。  

💡 **深入分析**  
透過軟邊界排名的幾何解讀，研究顯示 DPO 實際上執行的是帶有潛在負目標的 margin ranking；這說明為什麼在假設失效時，優化目標與人類偏好會背道而馳。  

⚠️ **研究限制**  
理論分析建立在特定數學條件之上；實驗僅在常見的基準資料集上進行，尚未在大規模真實對話系統上進一步驗證。  

🎯 **實務啟示**  
工程師在採用 DPO 前應先檢查該隱含假設是否滿足；若不確定，可改用 CPO——在保持 DPO 簡單實作的同時，獲得可證明的人類偏好對齊。  

🔗 **論文連結**  
📝 Conditional Equivalence of DPO and RLHF: Implicit Assumption, Failure Modes, and Provable Alignment  
👤 Zhiqin Yang, Yonggang Zhang, Wei Xue, Dong Fang, Bo Han (HKUST; LIGHTSPEED; HKBU)  
🔗 論文：https://arxiv.org/abs/2605.20834  
💻 程式碼：https://github.com/visitworld123/CPO  

你目前的偏好優化流程是否已檢查過這個假設？歡迎在留言區分享你的經驗與看法 👇  

#AI #RLHF #DPO #Alignment #HKUST #MachineLearning #LLM #CPO
