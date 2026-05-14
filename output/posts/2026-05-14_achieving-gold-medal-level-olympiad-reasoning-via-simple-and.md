---
title: "Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.13301
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:33:41.454715
---

📌 【上海AI實驗室等】簡單三步食譜變奧數金牌解題器  

你以為解國際數學或物理奧林匹克金牌題一定需要龐大模型和雜湊的技巧？最新研究顯示，只要遵循一個統一的訓練食譜，即使是 30B‑A3B 規模的骨幹也能達到金牌水準。  

🤔 **奧林匹克級別的推理仍然是 AI 的難關**  
近年雖有模型在 IMO、IPhO 等競賽中表現亮眼，但多數做法依賴於任務專門的調整與額外工具，缺乏一套可通用的訓練路徑。這使得將後訓練骨幹直接轉化為嚴格證明求解器的過程顯得零散且難以複製。  

🧪 **逆 perplexity 課程 + 雙階段 RL + 測試時擴展的統一流程**  
論文提出一個簡單且統一的食譜：  
1. 以逆 perplexity 為課程進行監督微調 (SFT)，在約 340K 長度不超過 8K token 的軌跡上，培養嚴格的證明搜索與自檢行為；  
2. 採用兩階段強化學習 (RL)：先以可驗證的獎勵進行 RL，再進入更細緻的證號層級 RL，共計約 200 步；  
3. 最終透過測試時擴展 (test‑time scaling) 提升解題表現。  
在此流程下，團隊訓練得到模型 SU‑01，基礎為 30B‑A3B 的後訓練骨幹。  

🔥 **SU‑01 模型在 IMO/USAMO 與 IPhO 上達到金牌水準，並支援超長推理軌跡**  
- SU‑01 能在難題上產生超過 100K token 的推理軌跡，證明其在長 horiz​on 問題上的穩定性；  
- 在數學與物理奧林匹克競賽（含 IMO 2025/USAMO 2026、IPhO 2024/2025）上表現達到金牌級別；  
- 此外，該模型在超越數學與物理的科學推理領域也展現出良好的泛化能力。  

💡 **訓練食譜如何將後訓練骨幹轉化為嚴格的證明搜索與自檢行為**  
逆 perplexity 課程鼓勵模型學習在低概率（即較為嚴格、不易生成）的區域進行探索，這有助於建構證明的搜索空間；隨後的兩階段 RL 則逐步強化在可驗證獎勵下的正確推理，最後再進階到證號層級的細膩優化。測試時擴展則允許模型在推理過程中動態分配更多計算資源，從而在不改變參數規模的情況下提升解題成功率。  

⚠️ **模型規模仍較大，即時部署成本高，未探討更小規模的適用性**  
雖然 SU‑01 展現了強大的推理能力，但其 30B‑A3B 的參數量對許多工程師而言仍屬較重的部署負擔；論文未提供更小模型採用同一食譜的結果，因此對資源受限環境的實用性尚需進一步驗證。  

🎯 **未來可將此食譜應用於其他科學推理領域，或作為訓練較小模型的基礎**  
- 該統一流程不依賴於特定競賽的額外標註，理論上可遷移至化學、生物學等科學領域的推理任務；  
- 對於希望在有限資源下獲得更強推理能力的團隊，可先以此食譜在較小骨幹上進行預訓練，再根據具體應用進行微調。  

🔗 **論文連結**  
📝 Achieving Gold-Medal-Level Olympiad Reasoning via Simple and Unified Scaling  
👤 Yafu Li, Runzhe Zhan, Haoran Zhang, Shunkai Zhang, Yizhuo Li (Shanghai AI Laboratory; The Chinese University of Hong Kong; Tsinghua University; Shanghai Jiao Tong University; Peking University)  
🔗 論文：https://arxiv.org/abs/2605.13301  

你認為這種「簡單食譜」是否能成為未來訓練推理模型的標準做法？歡迎在留言區分享你的看法 👇  

#AI #Reasoning #Olympiad #IMO #IPhO #ShanghaiAILab #CUHK #Tsinghua #SJTU #PekingU #MachineLearning #大型語言模型 #科學推理
