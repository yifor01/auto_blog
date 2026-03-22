---
title: "V-Co: A Closer Look at Visual Representation Alignment via Co-Denoising"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.16792
score: 113
model: gpt-4o-free
generated_at: 2026-03-18T21:18:55.842179
---

📌 【Meta 等機構最新研究】V-Co：像素擴散的視覺對齊指南  

像素空間擴散近年再度受到關注，因為它可以在不依賴預訓練自編碼器的情況下產出高品質圖像。然而，這類模型在語義監督上較弱，難以捕捉高層次的視覺結構。  🤔 **語義監督不足限制了像素擴散的表現**  
傳統像素擴散模型缺乏明確的高階視覺資訊引導，導致生成結果雖清晰但缺少語義一致性。最近的 representation‑alignment 方法（如 REPA）表明，將預訓練視覺特徵注入擴散過程能顯著提升品質，但現有的共同去噪（co‑denoising）設計常將多個選項纏在一起，難以判斷哪些才是關鍵。  

🧪 **在統一 JiT 框架下系統化拆解共同去噪**  
作者提出 V-Co，採用 Just‑in‑Time（JiT）統一框架，將共同去噪的各種設計選項隔離開來，以受控方式評估每個因素的影響。實驗在 ImageNet‑256 上進行，模型規模與訓練資源與基線保持可比。  

🔑 **四個關鍵因素決定共同去噪的效果**  
1. **雙流架構**：保留特徵專屬計算的同時允許彈性跨流互動，是有效特徵對齊的基礎。  
2. **結構化的無條件預測**：為了讓分類器自由引導（CFG）發揮作用，必須明確定義無條件分支的結構。  
3. **感知‑漂移混搭 loss**：結合感知相似度與漂移項，提供比單純 L2 更強的語義監督。  
4. **RMS 特徵重新縮放**：透過根均方（RMS）校正跨流特徵尺度，穩定共同去噪過程。  

💡 **將四個因素組合即可獲得簡單且有效的食譜**  
在相同模型規模下，V-Co 僅需較少訓練週期就能同時超越像素空間擴散基線以及先前的像素擴散方法（如 ADM、DiT），證明上述設計是缺一不可的。  

⚠️ **實驗聚焦於靜態圖像生成，長期與多模態行為尚未探討**  研究僅在 ImageNet‑256 上評估單圖像生成，未涉及視頻、3D 或跨模態任務；此外，未針對不同擴散步數或更大規模模型進行廣泛消融。  

🎯 **對工程師的啟示：先對齊特徵再做去噪**  
若想在像素空間擴散中引入預訓練視覺特徵，可參考 V-Co 的四條設計原則：採用雙流結構、明確無條件分支、使用感知‑漂移混搭 loss，以及以 RMS 進行特徵尺度校正。這樣的配方不僅提升生成品質，還能減少訓練時間。  

🔗 **論文連結**  
📝 V-Co: A Closer Look at Visual Representation Alignment via Co-Denoising  
👤 Han Lin, Xichen Pan, Zun Wang, Yue Zhang, Chu Wang (UNC Chapel Hill; NYU; Meta; AI)  
🔗 https://arxiv.org/abs/2603.16792  

你是否已在專案中嘗試過將預託特徵注入擴散模型？歡迎在留言區分享你的經驗與問題 👇  

#AI #ComputerVision #DiffusionModels #RepresentationAlignment #Meta #UNC #NYU #VCo #ImageGeneration #MachineLearning
