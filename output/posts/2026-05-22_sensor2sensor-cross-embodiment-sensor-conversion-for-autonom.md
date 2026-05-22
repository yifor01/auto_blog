---
title: "Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.22809
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:20:14.753384
---

📌 【Waymo x Google DeepMind】Sensor2Sensor：從行車鏡頭影片生成多模態自駕車感測資料  

想像一下，你手機裡的行車記錄器影片，能直接變成自駕車所需的相機與雷達資料——這樣的資料瓶頸是不是就被打破了？  

🤔 **自駕資料需求與現有來源的落差**  
訓練與驗證自駕系統（ADS）需要龐大且多樣化的多模態感測資料。真實車隊（AV）收集的日誌雖然保真，但規模有限、感測器配置單一，且難以覆蓋長尾行為與新穎場景。相反，公開的行車鏡頭、網路影片等「在野」視訊資源規模龐大、場景豐富，卻缺乏ADS所需的結構化、多模態輸入（多視角相機＋LiDAR點雲），無法直接用於訓練或驗證。  

🧪 **以 4D 高斯溜射建立無配對訓練管線，再用擴散模型完成跨身體轉換**  
研究團隊先將真實AV日誌透過 **4D Gaussian Splatting (4DGS)** 重建為時空一致的場景，並進行新視角渲染，得到類似行車鏡頭的單目影片。這一步提供了「真實AV日誌 → 行車鏡頭影片」的配對資料，使得後續能以無配對的方式學習反向映射。接著，**擴散模型** 接收單目行車鏡頭影片，生成對應的多視角相機圖像與LiDAR點雲，完成從單一視角的在野視訊到完整多模態AV感測套件的生成。  

📊 **生成資料的真實感與保真度經量化評估達可用水準**  
在多個基準上進行量化評估，顯示Sensor2Sensor產出的相機圖像與點雲在幾何一致性、紋理真實感等指標上接近真實AV日誌。進一步展示，團隊將具有挑戰性的網路與行車鏡頭影片（例如低光、遮蔽、非標準視角）轉換後，得到的多模態資料在視覺與幾何層面均保持高逼真度，證明該方法能有效橋接在野視訊與ADS所需的感測格式。  

💡 **跨身體（cross‑embodiment）生成開闢新資料增強途徑**  
核心創新在於利用4DGS先重建場景的時空幾何，使得無配對學習成為可能；擴散架構則負責將單一視角的稀疏資訊擴展為完整的多模態感測套件。這種「從行車鏡頭影片 → AV感測資料」的轉換不依賴於昂貴的多感測器車隊資料，而是透過生成模型把海量在野影片轉化為訓練可用的數據源，顯著提升資料規模與長尾場景覆蓋。  

⚠️ **目前評估侷限於生成資料的保真度，尚未見端到端駕駛效益報告**  
論文主要定量評估了生成相機與點雲的視覺與幾何品質，未提供在端到端自駕模型上的實際訓練提升或安全指標改善。此外，4DGS重建步驟依賴於較高品質的AV日誌來建立場景先驗；對於完全缺乏對應車輛日誌的場景，可能需要額外的適配或替代重建方式。  

🎯 **工程師可將此生成模組納入資料管線，低成本擴充訓練集**  
對於自駕車開發團隊來說，Sensor2Sensor提供了一條可行的路徑：將公開的行車鏡頭、網路影片等低成本資源透過該模型轉換為訓練所需的多視角相機與LiDAR點雲，從而在不增加實車採集成本的情況下，顯著擴充資料規模與場景多樣性。後續工作可專注於評估此類生成資料在真實駕駛任務上的遷移效益，以及進一步降低對AV日誌的依賴。  

🔗 **論文連結**  
📝 Sensor2Sensor: Cross-Embodiment Sensor Conversion for Autonomous Driving  
👤 Jiahao Wang, Bo Sun, Yijing Bai, Vincent Casser, Songyou Peng (Waymo; Johns Hopkins University; Google DeepMind; University of Washington)  
🔗 https://arxiv.org/abs/2605.22809  

你認為這種「影片轉感測」的方式會在未來的自駕資料策略中扮演什麼角色？歡迎在留言區分享你的看法 👇  

#AutonomousDriving #SensorFusion #4DGaussianSplatting #DiffusionModel #Waymo #GoogleDeepMind #DataAugmentation #AI #SelfDriving #CVPR2026
