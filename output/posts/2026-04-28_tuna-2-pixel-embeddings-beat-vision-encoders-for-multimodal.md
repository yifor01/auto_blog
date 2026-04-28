---
title: "Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.24763
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:05:26.841545
---

📌 **像素嵌入統一多模態理解與生成**

你以為多模態模型必須依賴預訓練視覺編碼器才能做好理解與生成？Tuna-2 直接從像素出發，證明端到端學習不只能與傳統 latent-space 方法匹敵，更在需要細粒度感知的任務上展現更強的多模態理解。

🤔 **預訓練編碼器真的必不可少嗎？**  
現行統一多模態模型普遍採用預訓練視覺編碼器（如 VAE 或 representation encoder），並為理解與生成分別維護不同的視覺表示。這種雙軌設計不僅增加模型複雜度，還導致兩任務之間的表示不對齊，阻礙完全端到端的優化。研究團隊質疑：是否可以跳過這些編碼器，直接在像素空間上完成理解與生成？

🧪 **以像素嵌入取代視覺編碼器的架構設計**  
Tuna-2 採用最簡單的 patch embedding 層將原始圖像轉換為 pixel embeddings，完全移除傳統的視覺編碼器模組。理解與生成兩個任務共享同一套像素表示，使模型能夠從原始像素開始進行端到端訓練。實驗顯示，這種設計在多模態基準上達到 state-of-the-art 性能，證明像素空間的建模可以與 latent-space 方法在高質量圖像生成上競爭。

🔥 **編碼器自由設計在規模上帶來更強的理解能力**  
雖然保留編碼器的變體在預訓練早期階段收斂速度更快，但 Tuna-2 的編碼器自由版本在規模擴大後展現出更優的多模態理解，特別是對需要細粒度視覺感知的任務。這表明，預訓練視覺編碼器並非多模態建模的必要條件；端到端的像素空間學習提供了一條可擴展的路徑，同時提升生成與感知的表示質量。

💡 **端到端像素學習的實務意義**  
- 對於希望減少模組化複雜度、追求端到端優化的工程師來說，直接使用 patch embedding 可簡化架構並降低維護成本。  
- 在需要精細視覺辨識的應用（如圖像細節編輯、細粒度 VQA）中，encoder-free 設計可能提供更好的理解基礎。  
- 未來工作可探索如何在更大規模的資料與計算資源下進一步發揮像素空間學習的潛力。

🔗 **論文連結**  
📝 Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation  
👤 Zhiheng Liu, Weiming Ren, Xiaoke Huang, Shoufa Chen, Tianhong Li (Meta AI; The University of Hong Kong; University of Waterloo)  
🔗 https://arxiv.org/abs/2604.24763

你目前的多模態管線是否仍依賴預訓練視覺編碼器？歡迎在留言區分享你的看法與經驗 👇

#AI #Multimodal #Tuna2 #PixelEmbedding #MetaAI #CVPR #端到端學習 #視覺理解 #圖像生成
