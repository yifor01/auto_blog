---
title: "What Matters in Practical Learned Image Compression"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.05148
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:30:38.625569
---

📌 【Apple 最新研究】Learned Image Codec：2‑3× 省傳輸，iPhone 實時編碼  

你以為壓縮越快就越糟嗎？  
Apple 最新研究證明，感知優化的 Learned 編碼器既能大幅降低位元率，  
又能在 iPhone 17 Pro Max 上實時處理 12MP 圖片。  

🤔 **感知優化是 Learned Codec 的潛力，但實用方案仍缺**  
傳統硬編碼難以直接迎合人類視覺系統，而 Learned codec 有此潛力，卻尚未同時兼顧壓縮效率與運行速度的實用方案。  

🧪 **全面消融研究結合效能感知的神經架構搜尋**  
團隊系統性地探討影響實用 Learned image codec 的關鍵建模選項，並加入數種新消融技術。在此基礎上，對數百萬種 backbone 配置進行效能感知的 neural architecture search，以在符合目標 on‑device 運行時間的前提下最大化感知壓縮表現。  

 **主觀實驗顯示 2.3‑3× 比特率節省，iPhone 編碼 230ms/解碼 150ms**  
經過嚴格的主觀使用者研究，新 codec 在感知品質上相較於 AV1、AV2、VVC、ECM 與 JPEG‑AI 實現 2.3‑3× 的位元率節省；相較於目前最佳的 Learned codec 替代方案，則節省 20‑40%。在 iPhone 17 Pro Max 上，12MP 圖片的編碼時間為 230ms，解碼時間為 150ms，速度快過多數在 V100 GPU 上運行的頂尖 ML‑based codec。  

💡 **將感知損失與運行時間納入搜尋目標是關鍵**  
將感知度量直接作為優化目標，並將運行時間作為搜尋的硬性約束，使得搜尋出的模型不僅在壓縮率上領先，同時能在真實邊端設備上達到實時需求。這種聯合優化是實現同時提升速度與感知品質的核心。  

⚠️ **研究聚焦單一設備與特定解析度，長期跨平台表現待驗證**  
實驗主要在 iPhone 17 Pro Max 上進行，針對 12MP 圖片；尚未報告其他硬體平台、不同解析度或長時間使用情況下的穩定性與功耗表現。  

🎯 **對邊端設備的感知壓縮提供可直接部署的 backbone 選擇**  
開發者可將此研究中搜尋出的 backbone 配置作為起點，在對感知品質與延遲有嚴格要求的應用（如 AR/VR、即時視訊傳輸）中直接採用或微調，以獲得顯著的位元率節省而不犧牲使用體驗。  

🔗 **論文連結**  
📝 What Matters in Practical Learned Image Compression  
👤 Kedar Tatwawadi, Parisa Rahimzadeh, Zhanghao Sun, Zhiqi Chen, Ziyun Yang @ Apple  
🔗 論文：https://arxiv.org/abs/2605.05148  

#AI #ImageCompression #LearnedCodec #Apple #PerceptualQuality #OnDeviceAI #CVPR2026 #深度學習 #邊端運算
