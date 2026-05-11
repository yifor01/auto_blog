---
title: "SOD: Step-wise On-policy Distillation for Small Language Model Agents"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.07725
score: 125
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:19:40.564859
---

📌 **SOD：逐步蒸馏提升小型模型 Agent 推理效能**  

你以為只要把大模型的知識蒸餾到小模型就能得到同等推理？實際上，錯誤會一步步放大，導致小模型完全失效。  

🤔 **Tool‑integrated reasoning 在小模型上易失控**  
工具整合推理（TIR）需要模型在多步驟中反复調用外部工具。小型語言模型受限於容量與長程交互的不穩定性，單靠稀疏的 episode 級獎勵（如群體相對策略優化）難以提供足夠的監督訊號。近期的 on‑policy distillation (OPD) 雖能從教師模型獲得密集的 token 級標註，但我們的實驗發現，當學生模型在某一步驟犯錯時，錯誤會隨著後續推理步驟遞增放大，使教師提供的標註逐漸失去可靠性。  

🧪 **以步驟為單位的發散度重新加權**  
我們提出 SOD（Step‑wise On‑policy Distillation），在每個推理步驟動態評估學生與教師軌跡的發散度，根據此發散度調整蒸餾強度：發散度大的步驟降低蒸餾權重，以減少可能誤導的教師訊號；發散度小的步驟保持較高權重，保留密集的指導信號。如此設計，SOD 能在高發散區域抑制錯誤傳播，同時在對齊良好的區域維持有效的監督。  

📊 **在數學、科學與程式碼基準上，SOD 比第二佳基準高出多達 20.86%；0.6B 學生模型在 AIME 2025 上達到 26.13%**  
實驗覆蓋具挑戰性的數學、科學與程式碼基準。與現有最佳基準相比，SOD 提升幅度最高達 20.86%。特別是，參數僅 0.6B 的學生模型在 AIME 2025 上取得 26.13% 的正確率，顯示即使是輕量級模型也能有效繼承具代理能力的推理行為。  

💡 **步驟級別重新加權如何抑制錯誤傳播**  
當某一步驟的學生‑教師軌跡發現較大偏離時，SOD 會降低該步驟的蒸餾係數，使教師的 token 級標註對該步驟的影響變弱。這樣可以防止單一錯誤被後續步驟放大。相反，在學生與教師高度一致的步驟，SOD 保持較高蒸餾強度，繼續提供密集的梯度資訊，從而在整體軌跡上獲得更穩定的學習訊號。  

⚠️ **實驗主要聚焦於特定基準，長期穩定性與更大規模工具尚未驗證**  
目前的結果僅在數學、科學與程式碼基準上獲得驗證。未涉及其他領域（如常識推理或多模態任務），亦未探討 SOD 在更長時間窗口或更複雜工具集合上的表現。這些方面的擴展仍需後續工作。  

🎯 **適合資源受限設備上的 Agent 部署，提供可行的小模型推理解決方案**  
對於需要在邊緣設備或移動端運行的 Agent，SOD 表明：透過步驟級別的蒸餾調整，即使是極小的語言模型也能獲得接近更大模型的推理表現。開發者可將此方法作為輕量化 Agent 的訓練策略，同時參考我們提供的開源實作。  

🔗 **論文連結**  
📝 SOD: Step-wise On-policy Distillation for Small Language Model Agents  
👤 Qiyong Zhong, Mao Zheng, Mingyang Song, Xin Lin, Jie Sun (Zhejiang University; Tencent; University of Science and Technology of China; National University of Singapore)  
🔗 論文：https://arxiv.org/abs/2605.07725  
💻 程式碼：https://github.com/YoungZ365/SOD  

你認為在資源受限的環境中，哪種蒸餾策略最實用？歡迎在留言區分享經驗與看法 👇  

#AI #SmallLanguageModel #Agent #Distillation #TIR #SOD #ZhejiangUniversity #Tencent #MachineLearning #開源 #AIME #CodeGeneration #MathReasoning #ScienceQA
