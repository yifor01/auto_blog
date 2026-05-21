---
title: "Learning from Language Feedback via Variational Policy Distillation"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.15113
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:48:10.273032
---

📌 【語言反饋驅動的變分策略蒸餾】

你以為只靠人類標註就能讓 LLM 在複雜推理上持續進步？實際上，單向蒸餾早已遇到瓶頂。

🤔 **語言反饋提供新訊號，但傳統蒸餾難以捕捉**  
現有的 RLHF 或被動策略蒸餾依賴預先收集的獎勵模型或固定教師政策，在需要細緻語言指導的推理任務上，教師與學生之間的互動難以同步更新，導致學習效果受限。

🧪 **透過變分期望最大化共同演化教師與學生**  
論文提出 Variational Policy Distillation (VPD) 框架：在每個訓練迭代中，以變分期望-最大化 (Variational EM) 的方式，讓教師政策根據語言反饋更新，同時學生政策嘗試模仿教師的分布；兩者共同演化，使語言反饋得以直接強化學生的決策過程。

🔑 **VPD 能在複雜推理任務中從語言反饋中學習，克服被動蒸餾的瓶頸**  
理論分析與實驗表明，透過教師與學生的共同演化，VPD 能將自然語言指導轉化為有效的策略更新訊號，在需要多步推理或結構化輸出的情境下，表現出比單向蒸餾更好的對齊能力。

💡 **關鍵在於「雙向更新」而非單向模仿**  
傳統蒸餾將教師視為固定目標，學生只被動擬合；VPD 則讓教師也能根據學生的表現與語言反饋進行調整，形成閉環回饋。這種互動式更新讓語言指導的細節（例如「為什麼這一步更好」）能被納入策略學習中，而不會被簡化為單一的獎勵分數。

⚠️ **目前僅提出理論框架與初步驗證，尚未大規模基準測試**  
論文主要闡述方法設計與理論優勢，實驗規模與基準任務皆屬探索性；長期穩定性、在不同規模模型上的泛化以及實際部署的成本仍需後續工作進一步探討。

🎯 **對齊研究可嘗試將語言反饋納入策略演化的訓練循環**  
- 在構建 RLHF 替代方案時，考慮使用變分 EM 讓教師模型隨學習過程動態調整。  
- 若已有語言標註資料（如錯誤說明、改進建議），可嘗試以 VPD 框架進行政策共同演化，而不僅依賴獎勵模型。  
- 關注開源實作（若有）以評估在複雜推理基準（如數學推理、代碼生成）上的實際表現。

🔗 **論文連結**  
📝 Learning from Language Feedback via Variational Policy Distillation  
🔗 https://huggingface.co/papers/2605.15113  

你目前的專案是否已在嘗試用語言反饋直接微調策略？歡迎在留言區分享經驗或疑問 👇

#AI #LLM #ReinforcementLearning #PolicyDistillation #LanguageFeedback #HuggingFace #GenAI #研究解讀
