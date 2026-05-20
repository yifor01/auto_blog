---
title: "TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O-aware Expert Offload"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.20179
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:13:51.520915
---

📌 **TIDE：MoE Diffusion LLM 無損加速**  

你以為 MoE 模型只會讓推理更重？TIDE 卻證明在單 GPU‑CPU 上能把吞吐提升 1.5×，且完全無損。  

🤔 **擴散 LLMs 與 MoE 的部署瓶頸**  
擴散大語言模型 (dLLM) 透過並行區塊級解碼提供更好的硬體利用率與雙向上下文，但隨著模型規模採用混合專家 (MoE) 架構，專家的載入與切換會在資源受限設備上產生巨額 I/O 開銷或運算瓶頸，成為在邊緣或 modest hardware 上大規模部署的主要阻礙。  

🧪 **TIDE：基於專家激發時間穩定性的 I/O‑aware 推理系統**  
論文提出 TIDE，一個無需重新訓練的推理系統。它利用擴散過程中，專家激發在區塊內具有時間穩定性的特性，採用間隔式專家更新策略：以 I/O 為感知的方式決定何時將專家載入或卸載。為求最佳效能，TIDE 將推理排程建模為一個數學規劃問題，解出能同時最小化 I/O 流量與 CPU 計算的最適間隔。整個過程完全是 lossless（無損），不需要任何模型微調或額外訓練。作者在單 GPU‑CPU 平台上，對 LLaDA2.0‑mini 與 LLaDA2.0‑flash 兩個模型進行了對比實驗。  

📊 **用 TIDE 的系統吞吐提升最高達 1.5×**  
- 在 LLaDA2.0‑mini 上，相較於先前基線，吞吐提升最高達 **1.4×**。  
- 在 LLaDA2.0‑flash 上，提升最高達 **1.5×**。  
這些提升是在不犧牲準確度的前提下達成的，證明 TIDE 能提供「免費午餐」式的加速。  

💡 **時間穩定性如何轉化為 I/O 減少**  
因為專家在短時間內的激發模式變化緩慢，TIDE 可以在較長的間隔內保持相同的專家配置，減少頻繁的載入/卸載操作。同時，I/O‑aware 的決策確保只有在實際需要時才觸發資料搬移，從而同時降低 I/O 流量與 CPU 在等待資料上的開銷。數學規劃步驟則自動尋找該間隔的最佳點，使兩種開銷的綜合成本最低。  

⚠️ **評價僅限於單 GPU‑CPU 系統**  
目前的實驗僅在單一 GPU‑CPU 配置下進行，未報告多 GPU、異質加速器或更大規模分佈式環境的表現。長期穩定性以及不同工作負載下的適應性仍需後續工作進一步驗證。  

🎯 **對工程師的實務建議**  
- 若您正在資源受限的設備上部署擴散 MoE LLMs，TIDE 可直接作為 plug‑and‑play 推理後端使用，無需重新訓練模型。  
- 透過調整間隔參數（由數學規劃解出），可在 I/O 帶寬與 CPU 計算之間取得最佳平衡。  
- 對於追求吞吐提升而不願犧牲準確度的場景（例如即時聊天、程式碼補全等），TIDE 提供了一種零成本的優化途徑。  

🔗 **論文連結**  
📝 **TIDE: Efficient and Lossless MoE Diffusion LLM Inference with I/O‑aware Expert Offload**  
👤 Zhiben Chen, Youpeng Zhao, Yang Sui, Jun Wang, Yuzhang Shang (University of Central Florida; Mobi.AI; Rice University)  
🔗 https://arxiv.org/abs/2605.20179  

你的推理管線是否已經開始嘗試類似的專家調度策略？歡迎在留言區分享經驗或疑問 👇  

#AI #MoE #DiffusionLLM #TIDE #InferenceOptimization #UCF #MobiAI #RiceUniversity #LLM #EfficientAI
