---
title: "NVIDIA AI Releases Gated DeltaNet-2: A Linear Attention Layer That Decouples Erase and Write in the Delta Rule"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/24/nvidia-ai-releases-gated-deltanet-2-a-linear-attention-layer-that-decouples-erase-and-write-in-the-delta-rule/
score: 91
model: tencent/hy3-preview:free
generated_at: 2026-05-24T19:43:07.142230
---

📌 【NVIDIA AI】Gated DeltaNet-2：解耦刪除與寫入的線性注意力層  

你以為線性注意力只能犧牲表現來換取效率？NVIDIA 最新的 Gated DeltaNet-2 卻證明，你可以兩者兼得。  

🤔 **線性注意力省下記憶體，卻在「編輯」時卡關**  
傳統的 softmax attention 需要 unbounded 的 KV cache，佔用大量顯存；線性 attention 用固定大小的遞迴狀態 Sₜ 取代，使序列混合變為線性時間、解碼變為常數記憶。然而，如何在這個壓縮的記憶裡進行「刪除舊資訊」與「寫入新資訊」而不打亂既有關聯，一直是難題。  

🧪 **1.3B 參數、100B Token 的訓練與雙通道閘設計**  
Gated DeltaNet-2 在 1.3B 參數規模上，以 100B 個 FineWeb-Edu token 進行訓練。它在原始 Delta Rule 的基礎上，提出 **Gated Delta Rule‑2**：  
- 在 key 軸引入通道勢刪除閘 **bₜ ∈ [0,1]ᵈᵏ**  
- 在 value 軸引入通道勢寫入閘 **wₜ ∈ [0,1]ᵈᵛ**  
兩個閘皆由 token 表示經 sigmoid 投影產生，更新公式可寫為  

```
Sₜ = (I − kₜ (bₜ ⊙ kₜ)ᵀ) Dₜ Sₜ₋₁ + kₜ (wₜ ⊙ vₜ)ᵀ
Dₜ = diag(αₜ)
```

這使「刪除」與「寫入」兩個原本耦合的操作得以分開控制。  

🚀 **在研究基準上優於 Mamba‑2、Gated DeltaNet、KDA 與 Mamba‑3**  
根據作者提供的評估，Gated DeltaNet-2 在該研究的基準套件中，**超越** 先前的 Mamba‑2、原始 Gated DeltaNet、Kimi Delta Attention (KDA) 與 Mamba‑3。具體提升幅度未在摘要中詳述，但作者指出這是一個「真實且有意義的」架構改進。  

💡 **閘的解耦讓記憶編輯更具彈性**  
過去的做法（如 Mamba‑2 的標量衰減 αₜ、Gated DeltaNet 的標量步長 βₜ）無法同時獨調「要忘記多少」與「要寫入多少」。KDA 雖將衰減做成通道向量，但仍保留單一標量 βₜ，導致刪除與寫入仍被綁定。Gated DeltaNet-2 的通道勢閘讓模型能在不同特徵維度上，**分別決定保留多少舊資訊與寫入多少新資訊**，從而在不破壞既有關聯的前提下，進行更精細的記憶更新。  

⚠️ **僅在研究基準上驗證，程式碼尚未公開**  
目前的說明僅基於研究基準表現，尚未見大規模下游任務（如語言建模、零樣本推理）的結果；亦未提及原始碼是否已開放。這意味著在實際工程落地前，仍需進一步驗證其穩定性與擴展性。  

🎯 **可作為 softmax attention 的直接替換，提升吞吐與降低顯存**  
若未來釋出開源實作，Gated DeltaNet-2 有潛力成為 **drop-in 替代方案**，在保持或提升語言模型表現的同時，降低 KV cache 的記憶體佔用與解碼延遲，符合當前對高效 LLM 與狀態空間模型的強烈需求。  

🔗 **論文連結**  
📝 Gated DeltaNet-2: A Linear Attention Layer That Decouples Erase and Write in the Delta Rule  
👤 Asif Razzaq (MarkTechPost 報導)  
🔗 https://www.marktechpost.com/2026/05/24/nvidia-ai-releases-gated-deltanet-2-a-linear-attention-layer-that-decouples-erase-and-write-in-the-delta-rule/  

你對此類線性注意力的改進有什麼看法？歡迎在留言區分享你的觀察與使用經驗 👇  

#AI #LinearAttention #GatedDeltaNet #NVIDIA #LLM #EfficientAI #MachineLearning #深度學習
