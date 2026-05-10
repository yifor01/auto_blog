---
title: "NVIDIA AI Releases Star Elastic: One Checkpoint that Contains 30B, 23B, and 12B Reasoning Models with Zero-Shot Slicing"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/09/nvidia-ai-releases-star-elastic-one-checkpoint-that-contains-30b-23b-and-12b-reasoning-models-with-zero-shot-slicing/
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-05-10T19:17:50.484565
---

📌 【NVIDIA 最新研究】Star Elastic：單檢點包含 30B、23B、12B 推理模型  

你是否曾為了支援不同模型大小而維護多個檢查點、多份儲存空間？NVIDIA 的 Star Elastic 讓一個檢查點就能零切片出三種規模的推理模型，省去重複訓練與額外微調的成本。  

🤔 **為何需要「彈性」模型？**  
傳統上，若要同時提供 8B、30B、70B 等不同參數量的 LLM，每個尺寸都需要獨立的完整訓練、獨立的儲存與獨立的部署堆疊。這意味著計算成本會隨著想支援的模型數量線性增長。對於大規模推理的團隊來說，這既浪費資源又增加維護複雜度。  

🧪 **Star Elastic 的核心設計**  
Star Elastic 是一種 **後訓練（post‑training）方法**，透過單次訓練 run 把多個巢狀子模型嵌入到一個父模型中。以 NVIDIA 的 **Nemotron Nano v3**（混合 Mamba–Transformer–MoE，總參數 30B、活躍參數 3.6B）為基礎，該方法產出 23B（2.8B 活躍）與 12B（2.0B 活躍）的巢狀變體，全部訓練約使用 160B 權杖。所有變體共享同一個檢查點，且可直接 **零切片（zero‑shot slicing）** 取出，無需額外 fine‑tuning。  

重要性估計（importance estimation）會為模型的每個組件打分——包括 embedding channels、attention heads、Mamba SSM heads、MoE experts 與 FFN channels——根據其對模型準確度的貢獻程度進行排名。排名最高的連續子集會被較小預算的子模型使用，這種特性被稱為 **巢狀權重共享（nested weight‑sharing）**。該方法同時支援多個軸向的 nesting：SSM 維度、embedding channels、attention heads、Mamba heads 與 head channels、MoE expert 數量以及 FFN 中間維度。對於 MoE 層，Star Elastic 進一步採用 **Router‑Weighted Expert Activation Pruning (REAP)** 來決定哪些 expert 該被保留。  

🔑 **直接可用的實務優勢**  
- **單一檢查點**：30B、23B、12B 三種模型大小只需維護一份權重檔，顯著降低儲存與版控開銷。  
- **零切取**：在推理時即可依需求切出對應大小的子模型，無需額外微調或重新載入。  
- **彈性伸縮**：團隊可依流量或延遲需求即時切換模型規模，提升資源利用率。  

⚠️ **目前已知的限制**  
- 該方法目前僅在 **Nemotron Nano v3**（混合 Mamba–Transformer–MoE）上得到驗證，是否能直接推廣至純 Transformer、純 Mamba 或其他架構尚需進一步探索。  
- 重要性估計本身需要額外的計算步驟，雖然只在後訓練階段進行，但對極大模型可能仍有非凡開銷。  
- 零切片保證子模型的權重來自父模型的最高排名子集，但未在給定資訊中提及子模型在特定基準測試上的準確度表現，實際效果仍需依實際應用場景評估。  

🎯 **對工程師的啟示**  
如果你的服務需要同時支援多種模型大小（例如隨流量動態切換），Star Elastic 提供了一種「訓練一次、隨用切取」的範式，可顯著簡化 CI/CD 流程與基礎設施成本。未來值得關注的是該方法在其他模型家族（如純 LLM、多模態模型）上的遷移潛力，以及是否能進一步降低後訓練階段的重要性估計開銷。  

🔗 **論文連結**  
📝 Star Elastic: One Checkpoint that Contains 30B, 23B, and 12B Reasoning Models with Zero-Shot Slicing  
👤 Asif Razzaq (MarkTechPost 報導)  
🔗 https://www.marktechpost.com/2026/05/09/nvidia-ai-releases-star-elastic-one-checkpoint-that-contains-30b-23b-and-12b-reasoning-models-with-zero-shot-slicing/  

你是否已經在專案中嘗試過類似的「一檢多模」策略？歡迎在留言區分享你的經驗與疑問 👇  

#AI #NVIDIA #StarElastic #LLM #模型壓縮 #零切斷 #推理優化 #MarkTechPost #機器學習 #深度學習
