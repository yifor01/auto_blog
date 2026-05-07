---
title: "Every Step Counts: Step-Level Credit Assignment for Tool-Integrated Text-to-SQL"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.04719
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-05-07T21:00:45.075277
---

📌 **逐步賦分：提升 Tool‑Integrated Text‑to‑SQL 效率**

你以為讓 AI 寫 SQL 只要給對答案就好？實際上，中間每一步的好壞也決定最終效率——模型可能走冗餘路徑仍拿到同樣獎勵。

🤔 **結果導向的獎勵讓模型學會走冗餘路徑**  
現有強化學習方法多依賴粗粒度的結果監督：只要最終 SQL 正確，過程中是否多餘或錯誤都不影響獎勵。這種稀疏訊號導致模型被鼓勵探索低效的推理空間，影響效率與泛化能力。

🧪 **基於 BIRD 基準的逐步強化學習實驗**  
研究團隊提出 FineStep 框架，分三步進行：  
1. 設計獨立的過程獎勵，稀疏結果訊號變得更密集。  
2. 提出逐步信用分配機制，精確量化每一步的價值。  
3. 基於逐步優勢的策略優化方法，進行高效參數更新。  
實驗在 BIRD 基準上進行，使用 4B 規模模型驗證。

🔍 **核心發現：FineStep 在 4B 模型上平均 EX 提升 3.25%，並減少冗餘工具調用**  
相比於 GRPO 基線，FineStep 達到 State‑of‑the‑art 性能，平均 Exact Match (EX) 提升 3.25%。同時，因為每一步都有明確價值反饋，模型產生的不必要工具呼叫顯著下降。

💡 **逐步獎勵與優勢函數讓模型學會挑選高效路徑**  
過程獎勵提供了即時回饋，讓模型能區分哪一步真正推進正確解決；優勢函數則將這些回饋轉為策略更新的方向，使學習聚焦於高效、簡潔的推理路徑，而非單純追求最終正確答案。

⚠️ **僅在 BIRD 基準上驗證，長期泛化與其他工具未探討**  
本研究主要在 BIRD 數據集上進行，未涉及其他基準或不同工具集的表現；此外，僅考慮了短期訓練效果，長期使用中的穩定性尚需後續工作驗證。

🎯 **可直接套用於工具增強的 Text‑to‑SQL 系統，提升效率與準確度**  
對於希望減少不必要工具調用、提升生成 SQL 準確度的團隊，FineStep 提供了一種可即插即用的逐步信用分配方法。在實務上，可先在現有 RL 框架中加入過程獎勵與優勢計算，觀察是否能減少冗餘步驟並提升 EX 指標。

🔗 **論文連結**  
📝 Every Step Counts: Step-Level Credit Assignment for Tool-Integrated Text-to-SQL  
👤 Yaxun Dai, Baolin Sun, Junying Wang, Pengfei Wang, Yingqi Gao (Soochow University; Ant Digital Technologies, Ant Group; University of Science and Technology of China)  
🔗 https://arxiv.org/abs/2605.04719  

你的 Text-to-SQL 系統是否也在浪費步驟？歡迎在留言區分享你的優化經驗 👇  

#AI #Text-to-SQL #ReinforcementLearning #FineStep #BIRD #SoochowUniversity #AntGroup #USTC #機器學習 #資料科學
