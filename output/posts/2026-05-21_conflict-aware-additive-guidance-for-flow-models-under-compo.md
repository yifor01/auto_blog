---
title: "Conflict-Aware Additive Guidance for Flow Models under Compositional Rewards"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.20758
score: 99
model: tencent/hy3-preview:free
generated_at: 2026-05-21T21:04:31.501416
---

📌 【NUS & HIT】Conflict‑Aware Additive Guidance：讓多重約束的生成模型不再偏離真實分布  

你以為疊加多個限制條件就能得到更精準的 AI 生成？實際上，這樣做常讓模型「跑偏」，產出偏離真實數據的結果。  

🤔 **當多個約束共同作用時，生成模型為何會漂移？**  
在推理時透過導引採樣（guidance）可以把擴散或流模型視為可控軌跡，無需微調即可注入外部約束（例如成本函式或預訓練驗證器）。然而，當同時施加多個約束時，既有方法常會導致生成軌跡偏離真實數據流形，產生離 manifold 的漂移。作者指出，這種漂移的根源在於梯度不對齊導致的逼近誤差會隨著衝突程度急劇放大。  

🧪 **從合成資料到圖像編輯與決策規劃的驗證實驗**  
研究團隊在多個領域驗證所提出的方法：包括合成資料集、圖像編輯任務，以及用於規劃與控制的生成式決策實驗。實驗設計上，他們將新方法與現有基線進行對照，觀察生成保真度與計算開銷的變化。  

💡 **Conflict‑Aware Additive Guidance 如何動態偵測並化解梯度衝突**  
基於上述發現，他們提出 **Conflict‑Aware Additive Guidance（gᶜᵃʳ）**，這是一種輕量且可學習的導引方式。gᶜᵃʳ 能在採樣過程中即時檢測梯度衝突，並主動修正離 manifold 的漂移，從而在不顯著增加運算負擔的情況下提升生成品質。  

⚠️ **方法輕量但需進一步在更大規模任務上檢驗**  
雖然實驗顯示 gᶜᵃʳ 能有效降低離 manifold 漂移並在多個領域超越基線，但目前的驗證主要集中在合成資料、圖像編輯與決策規劃等範圍。長期效果、更大規模的實際應用以及與其他導引技術的組合仍需後續研究進一步探討。  

🎯 **對工程師的實務建議：可直接插入現有流程的低開銷指引**  
對於需要同時滿足多個約束的生成任務（例如圖像編輯中的風格與內容限制、規劃中的安全與效率約束），gᶜᵃʳ 提供了一種可即插即用、運算開銷低的解決方案。工程師可在不重新訓練模型的前提下，將此導引層加入現有的推理管線，以獲得更貼近真實分布的輸出。  

🔗 **論文連結**  
📝 Conflict‑Aware Additive Guidance for Flow Models under Compositional Rewards  
👤 Xuehui Yu, Fucheng Cai, Meiyi Wang, Xiaopeng Fan, Harold Soh (National University of Singapore; Harbin Institute of Technology)  
🔗 論文：https://arxiv.org/abs/2605.20758  
💻 程式碼：https://github.com/yuxuehui/CAR-guidance  

你在使用多重約束的生成模型時，是否也遇過「越約束越不準」的情況？歡迎在留言區分享你的經驗與看法 👇  

#AI #FlowModels #Guidance #GenerativeAI #NUS #HIT #MachineLearning #DiffusionModels #CodeAvailable
