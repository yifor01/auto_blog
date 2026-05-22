---
title: "Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.22791
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:56:25.924817
---

📌 【NVIDIA 最新研究】Gated DeltaNet-2：解耦刪除與寫入的線性注意力  

你以為線性注意力只要犧牲精準度就能換取效率？其實難點不在「忘記什麼」，而在「如何編輯這個固定大小的記憶狀態，卻不把既有的關聯弄亂」。  

🤔 **線性注意力的記憶編輯難題**  

線性注意力用固定大小的遞迴狀態取代 softmax 的無界快取，使序列混合變為線性時間、解碼變為常數記憶。然而，要在這個壓縮狀態裡進行「寫入」時，必須先決定要刪除多少舊內容（erase），再決定要寫入多少新內容（write）。先前的 Delta‑rule 與 Kimi Delta Attention (KDA) 都只用一個純量門控同時控制這兩件事，導致刪除與寫入無法獨立調整。  

🧪 **雙通道門控的設計**  

Gated DeltaNet-2 繼承了自適應遺忘與通道級衰減的優點，但引入了兩個獨立的通道門控：  
- **抹除門控 b_t** 決定每個通道要刪除多少舊資訊  
- **寫入門控 w_t** 決定每個通道要寫入多少新資訊  

當 b_t 與 w_t collapse 到同一個純量時，模型退化為 KDA；當通道級衰減也 collapse 時，則退化為 Gated DeltaNet。論文進一步提供：  
- 快速權重更新的視角  
- 將通道級衰減吸進非對稱抹除因子的 chunkwise WY 演算法  
- 保持高效平行訓練的 gate‑aware 反向傳播  

📊 **在 1.3B 參數、100B FineWeb‑Edu tokens 上的表現**  

在相同規模下，Gated DeltaNet-2 在語言建模、常識推理與檢索三個維度上，均優於 Mamba‑2、Gated DeltaNet、KDA 與 Mamba‑3 變體。其優勢在長情境 RULER needle‑in‑a‑haystack 基準上最為顯著：  
- 在多鍵檢測設定中提升評估分數  
- 在純遞迴與混合遞迴/Transformer 設定下皆保持強勢  

💡 **為何分離門控能帶來提升**  

將「刪除」與「寫入」解耦讓模型能依據每個通道的狀態做更細膩的調整：當某個維度需要保留舊資訊時，可降低 b_t；同時若該維度需要吸收新知識，則可提升 w_t。這種獨立控制減少了因單一門控而在記憶狀態上造成的干擾，從而在長距離依賴的任務中保留更多有用結構。  

⚠️ **已知的限制**  

- 實驗主要聚焦在語言建模與檢索基準，其他模態（如視覺、音訊）未涉及  
- 模型規模固定於 1.3B，更大規模的行為尚未探索  
- 門控之間的互動雖被分離，但理論上仍可能受到訓練目標的耦合影響  

🎯 **對工程師的實務啟示**  

- Gated DeltaNet-2 可作為現有線性注意力或 Mamba 風格模型的直接替換，無需改變訓練管線  
- 開放原始碼（GitHub：https://github.com/NVlabs/GatedDeltaNet-2）讓團隊能快速在自己的長情境任務上驗證  
- 未來設計注意力變體時，考慮將「刪除」與「寫入」的門控分離，或許是提升記憶編輯精細度的一個有效方向  

🔗 **論文連結**  
📝 Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention  
👤 Ali Hatamizadeh, Yejin Choi, Jan Kautz @ NVIDIA  
🔗 arXiv：https://arxiv.org/abs/2605.22791  
💻 程式碼：https://github.com/Nvlab s/GatedDeltaNet-2  

你目前的模型是否也在為「怎麼編輯記憶而不破壞關聯」而苦惱？歡迎在留言區分享你的看法或實驗經驗 👇  

#AI #LinearAttention #Mamba #NVIDIA #DeepLearning #語言模型 #檢索 #GatedDeltaNet2
