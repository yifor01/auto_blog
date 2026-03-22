---
title: "From Pixels to Patches: Pooling Strategies for Earth Embeddings"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.02080
score: 118
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T19:58:59.595931
---

📌 【地理空間 AI 新突破】從像素到圖斑：基礎模型池化策略大評比

當 AI 模型從圖斑級別 (patch-level) 轉向像素級別 (pixel-level) 的地理空間嵌入時，從業者面臨一個關鍵挑戰：如何將數千個像素向量聚合為圖斑表示，同時保持類別識別能力並匹配下游標籤解析度？

🤔 **平均池化丟失 10% 準確率？**

地理空間基礎模型正在從圖斑級別轉向像素級別的嵌入，但預設的平均池化 (mean pooling) 會丟失圖斑內部的變異性，在空間偏移下準確率可能下降超過 10%。

🧪 **EuroSAT-Embed：81,000 個嵌入的 GeoTIFF 資料集**

為了評估這一問題，研究團隊建立了 EuroSAT-Embed，包含來自三個基礎模型的 81,000 個嵌入 GeoTIFF：AlphaEarth、OlmoEarth 和 Tessera。他們對 11 種免訓練和 2 種參數化池化方法進行了評估，測試了隨機和地理上不相交的測試集分區。

 **豐富池化方案提升準確率 5%**

- 更豐富的池化方案可將地理泛化差距縮小高達 40%
- 在空間分區上準確率提升高達 5%
- 平均池化在空間偏移下的表現最差

💡 **Generalized Mean Pooling：最佳的替換方案**

- GeM (Generalized Mean Pooling) 被推薦為平均池化的替代方案
- 在不增加嵌入維度的情況下提升準確率
- 對於最大準確率，Stats 池化 (min/max/mean/std 的串聯) 表現最佳
- Stats 池化需要 4 倍的嵌入大小

⚠️ **池化效果因嵌入來源而異**

研究發現池化方法的有效性因嵌入來源而異，更高維度的嵌入最能從分佈統計中受益。

🎯 **實務建議**

- 從平均池化切換到 GeM，簡單提升準確率
- 若需要最大準確率且不介意維度增加，使用 Stats 池化
- 根據嵌入來源和維度選擇合適的池化策略

🔗 **論文連結**
📝 From Pixels to Patches: Pooling Strategies for Earth Embeddings
👤 Isaac Corley, Caleb Robinson, Inbal Becker-Reshef, Juan M. Lavista Ferres
@ Wherobots; Microsoft AI for Good Research Lab
🔗 arxiv.org/abs/2603.02080

你在使用哪種池化策略？歡迎分享你的經驗 👇

#地理空間AI #ComputerVision #基礎模型 #機器學習 #衛星影像 #AI研究
