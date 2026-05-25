---
title: "Metacognition as Reward: Reinforcing LLM Reasoning via Knowledge and Regulation Signals"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.23384
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:42:00.099290
---

📌 **Metacognition-as-Reward：讓模型學會思考思考**

你以為強化學習只能看最終答案對錯？實際上，模型的中間思考過程也能被獎勵。這篇論文提出一個無需為每題設計規則的通用框架。

🤔 **現有獎勵設計難以兼顧過程與通用性**  
目前的強化學習方法主要分為兩類：一類依賴可驗證的最終答案（RLVR），雖能給出明確的勝負訊號，但對中間推理步驟幫助有限；另類使用自然語言規則作為獎勵（RaR），能評估推理品質，但往往需要針對每個實例撰寫專屬規則，設計成本高。這兩種方式都難以在不額外人工成本的情況下，同時提供過程導向的指導與良好的泛化能力。

🧪 **以 Metacognition 為核心的兩維度獎勵框架**  
論文提出 Metacognition-as-Reward (MaR)，將模型的推理軌程拆解為兩個一般性維度：  
1. **Metacognitive knowledge** —— 辨識與當前任務相關的資訊，無需手工編寫實例特定的規則；  
2. **Metacognitive regulation** —— 規劃並調整推理過程，使模型能在超出最終答案的範疇上獲得回饋。  
MaR 以 trajectory‑level 的獎勵同時考量任務知識覆蓋度、規則忠誠度以及最終答案正確性，從而在保持獎勵信號可解釋的同時，將回饋延伸到完整的推理路徑。

🚀 **在 22 個基準測試上一致提升，且能縮小與前沿模型的差距**  
實驗顯示，MaR 在 22 個不同基準上均使模型表現提升：相較於基礎模型最高可獲得 7.7% 的絕對提升，相較於傳統 DAPO 最高可達 11.0% 的提升。具體來說，使用 Qwen3.5-9B + MaR 後，模型在整體平均成績上已經超越 GPT‑OSS‑120B，並在數個單項基準中表現優於更強的模型。過程層面的分析進一步顯示，推理品質（如步驟的完整性與正確性）也有顯著改善。此外，MaR 具備跨域泛化能力：在未見過的資料集上，接受 MaR 訓練的模型平均優於各自的基礎模型。

💡 **關鍵在於將「思考」本身納入獎訊號**  
MaR 的核心貢獻在於把原本隱含的 metacognitive 行為——知識辨識與過程調整——顯性化、可量化，並直接作為強化學習的獎勵。這意味著模型不僅被鼓勵得到正確答案，更被引導去「思考如何思考」，從而在不需要為每題撰寫規則的情況下，獲得更穩健、可遷移的推理能力。

⚠️ **實驗主要聚焦於現有基準與短期訓練效果**  
論文未報告具體的資料量、訓練時長或模型規模細節，僅提供了 aggregated 的基準表現提升。長期訓練或在極大規模模型上的行為仍需後續工作驗證。

🎯 **實務上可視為一種通用的「思考獎勵」插件**  
對於正在使用強化學習提升 LLM 推理的團隊，MaR 提供了一種無需撰寫 instance‑specific rubrics 的替代方案。在實際應用時，可先嘗試在現有的 RL 管線中加入 metacognitive knowledge 與 regulation 的評估模組，觀察是否能在不額外標註成本的情況下提升模型的推理穩定性與遷移性。

🔗 **論文連結**  
📝 Metacognition as Reward: Reinforting LLM Reasoning via Knowledge and Regulation Signals  
👤 Sirui Chen, Lei Xu, Yuying Zhao, Yutian Chen, Yu Wang (Tongji University; Shanghai AI Laboratory; Nanyang Technological University; University of Science and Technology of China; EPFL; Wuhan University)  
🔗 https://arxiv.org/abs/2605.23384  

你在使用 AI 輔助推理時，是否也曾希望模型能「思考自己的思考」？歡迎在留言區分享你的看法 👇  

#AI #LLM #ReinforcementLearning #Metacognition #Reasoning #TongjiUniversity #ShanghaiAILab #NanyangTech #USTC #EPFL #WuhanUniversity #Qwen #GPT-OSS #DAPO #研究分享
