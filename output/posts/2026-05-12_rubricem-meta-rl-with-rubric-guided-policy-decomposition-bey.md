---
title: "RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.10899
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:28:09.626168
---

📌 評分規則驅動深度研究Agent  

隨著 AI 需要撰寫長報告、規劃實驗、綜合文獻等任務，傳統強化學習難以發揮作用——這些輸出沒有標準答案可供對比，決策軌跡橫跨多種工具增強的步驟，且事後訓練缺乏把過去經驗轉為可重複使用知識的機制。  

🤔 **把評分規則變成 Agent 的「共同語言」**  

研究團隊提出，評分規則（rubric）不該只作為最終答案的評分標準，而應成為規劃、回饋與記憶之間的共同介面。這樣一來，規則既能指導 Agent 如何一步步完成任務，又能提供更細膩的語義回饋，同時把被判斷過的軌跡蒸餾成未來嘗試可直接參考的指引。  

🧪 **RubricEM：階段化策略分解 + 反思式元策略演化**  

- **階段化策略分解**：Agent 先生成自我評分規則，再依此規則對「規劃、證據蒐集、檢閱、合成」四個階段的策略進行條件約束，使軌跡具備階段意識。  
- **Stage‑Structured GRPO**：利用各階段的規則判決來分配信用，提供比稀疏最終獎勵更密集的語義回饋，利於長 horizion 優化。  
- **共享骨幹反思元策略**：同時訓練一個共享骨幹的元策略，將被規則判斷過的軌跡蒸餾成具規則基礎的指引，供未來嘗試直接重複使用。  

🚀 **RubricEM‑8B 在四個長篇研究基準上表現強勢**  

在公開可比的開放模型中，RubricEM‑8B 取得領先成績；與專有的深度研究系統相比，僅有小幅落後，顯示其在無法直接驗證獎勵的情境下，仍能有效學習與改進。  

🔍 **為何這套方法能行？**  

- 規則在每個階段提供語義豐富的判斷，使信用分配不再只依賴最終的對錯，而是能針對「規劃是否周全」、「證據是否相關」等中間步驟給予回饋。  
- 元策略透過反思把已被評分的軌跡轉化為可重複使用的「規則導向指引」，解決了過去經驗難以被重複利用的問題。  
- 兩者共同構成一個閉環：規則指導行動 → 行動產生軌跡 → 規則判斷軌跡 → 元策略蒸餾指引 → 未來行動受指引導向。  

⚠️ **主要限制：尚未公開原始碼**  

論文未提供明確的開源程式碼，這限制了立即在實務上複製與擴展的可能性；此外，實驗僅在四個長篇研究基準上進行，長期效果及更廣泛任務的適用性仍需後續驗證。  

🎯 **對工程師與研究者的啟示**  

- 在缺乏明確獎訊號的任務中，可考慮將領域專家的評分規則訓練成模型可理解的形式，作為策略、回饋與記憶的共同樞紐。  
- 階段式策略分解與反思式元策略的結合，提供了一種從「可驗證獎勵」跳脫、學習長 horizion 複雜推理的可行路徑。  
- 未來若能開放實作，將有助於加速自主深度研究系統在學術與產業中的落地。  

🔗 **論文連結**  
📝 RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards  
👤 Gaotang Li, Bhavana Dalvi Mishra, Zifeng Wang, Jun Yan, Yanfei Chen (University of Illinois Urbana-Champaign; Google Cloud AI Research)  
🔗 https://arxiv.org/abs/2605.10899  

你認為在沒有標準答案的研究任務中，以評分規則當共同介面是否可行？歡迎在留言區分享你的看法 👇  

#AI #MetaRL #RubricEM #DeepResearch #AgenticAI #GoogleCloud #UIUC #強化學習 #長 horizion 最佳化 #GenAI
