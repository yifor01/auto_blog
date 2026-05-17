---
title: "Nous Research Proposes Lighthouse Attention: A Training-Only Selection-Based Hierarchical Attention That Delivers 1.4–1.7× Pretraining Speedup at Long Context"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/16/nous-research-proposes-lighthouse-attention-a-training-only-selection-based-hierarchical-attention-that-delivers-1-4-1-7x-pretraining-speedup-at-long-context/
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-05-17T19:35:27.419108
---

📌 **Lighthouse Attention：長文預訓練提速1.4–1.7倍**  

🎣 **你以為加速長文訓練只能靠更好的硬體？Nous Research 顯示，只要改變注意力機制，就能在不犧牲損失的前提下，讓預訓練速度提升1.4–1.7倍**  

🤔 **長序列注意力的二次方瓶頸**  
訓練長上下文語言模型時，Scaled Dot‑Product Attention (SDPA) 的計算與記憶體需求會隨序列長度 N 以 Θ(N²) 增長。雖然 FlashAttention 透過 IO‑aware tiling 大幅降低了記憶體佔用，但其底層的 Θ(N²) 計算複雜度仍未改變。許多先前的稀疏注意力方法（NSA、HISA、DSA、MoBA）雖然嘗試壓縮 key/value，但它們仍把選擇邏輯寫進自訂注意力核心，導致無法直接復用現代 GPU tensor core 已優化的密集注意力核心。此外，訓練時的稀疏方法必須經過更嚴格的檢驗：訓練結束後，得到的權重在推理時仍需能表現出稱職的密集注意力行為。  

🧪 **對稱多層池化＋核心外選擇的設計**  
Lighthouse Attention 在兩個關鍵設計上與先前工作區分開來：  
1. 對查詢 (Q)、鍵 (K)、值 (V) 進行對稱的多層金字塔式池化，而非只壓縮 K/V。  
2. 把選擇邏輯完全放在注意力核心之外；選擇後，系統將被挑選的條目收集成一個連續的密集子序列，然後交給已優化的密集注意力核心進行計算。  
這種「訓練專用」的選擇機制使得 Lighthouse 能在不改變推理流程的前提下，復用高效的密集核心，同時滿足訓練時的正確性標準——訓練完成後得到的權重仍能產出稱職的密集注意力模型。  

🔑 **1.40×–1.69× 的端到端時鐘加速，損失不升反降**  
在相同的 cuDNN‑backed SDPA 基線上，Lighthouse Attention 實現了 1.40× 到 1.69× 的端到端時鐘速度提升。最終的訓練損失與基線相當甚至略低，證明加速並未犧牲模型品質。  

💡 **為何對稱池化＋外部選擇能同時提速與保持品質**  
- 對稱池化讓 Q、K、V 在多個尺度上都獲得資訊壓縮，減少了參與點積運算的 token 數，從而直接降低計算量。  
- 將選擇邏輯移出核心，使得後續的密集注意力計算可以完全使用已經過硬體優化的 tensor core 核心，避免了自訂核心帶來的核心啟動與記憶體搬運開銷。  
- 因為選擇是在訓練階段完成且只影響哪些 token 參與密集計算，訓練得到的權重在推理時仍可用完整的密集注意力進行運算，符合訓練時的正確性標準。  

⚠️ **目前僅報告預訓練階段的加速效果，具體消融與更長序列或不同模型規模的驗證尚未在說明中完整呈現**  

🎯 **訓練階段即插即用的加速方案，無需改動推理管線**  
對於大規模長上下文模型的研究與工程團隊，Lighthouse Attention 提供了一種「只改訓練」的加速手段：  
- 直接替換原有的 SDPA 實現，即可獲得 1.4–1.7× 的預訓練時鐘提升。  
- 因為不改變模型結構或推理流程，現有的推理優化（如 FlashAttention、量化等）仍可疊加使用。  
- 此方法尤其適合需要在長文本上進行大規模預訓練的場景，例如代碼模型、長文檢索或多模態序列建模。  

🔗 **論文連結**  
📝 Lighthouse Attention: A Training‑Only Selection‑Based Hierarchical Attention  
👤 Nous Research (Asif Razzaq 報導)  
🔗 https://www.marktechpost.com/2026/05/16/nous-research-proposes-lighthouse-attention-a-training-only-selection-based-hierarchical-attention-that-delivers-1-4-1-7x-pretraining-speedup-at-long-context/  

你在長序列模型的訓練上遇到過計算瓶頸嗎？歡迎在留言區分享你的經驗或對 Lighthouse Attention 的看法 👇  

#AI #LLM #AttentionMechanism #NousResearch #LighthouseAttention #預訓練加速 #長文本 #機器學習 #深度學習 #GPU優化
