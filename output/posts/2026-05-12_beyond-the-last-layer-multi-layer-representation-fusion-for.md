---
title: "Beyond the Last Layer: Multi-Layer Representation Fusion for Visual Tokenizatio"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.10780
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-12T21:02:39.460107
---

📌 【多層融合視覺Tokenizer】

現有視覺Tokenizer只取最後一層特徵，其實中層細節早被稀釋殘留。若把所有層資訊重新組合，能否大幅提升圖像生成品質？

🤔 **只用最後一層會遺失階層資訊**  
現行方法將凍結的預訓練視覺編碼器視為視覺Tokenizer，卻普遍僅取最後一層特徵。這種做法將低層細節壓縮為語義抽象後的微弱殘餘，導致重建與生成品質受限。

🧪 **Depth‑Routed Representation AutoEncoder (DRoRAE)**  
我們提出一個輕量融合模組，透過能量約束的路由與遞增校正，自適應地聚合編碼器的所有層。訓練分為三階段：首先在凍結解碼器的隱含分布約束下學習融合；其次微調解碼器以充分利用經豐富的潛在表示。

 **重建誤差大幅下降，生成品質亦提升**  
在 ImageNet‑256 上，DRoRAE 使 rFID 從 0.57 降至 0.29（改善約 49%），在使用 AutoGuidance 的情況下，生成 FID 從 1.74 下降至 1.65。同樣的提升也轉移到文字到圖像的合成任務中。

💡 **融合容量與重建品質呈對數線性關係**  
我們發現融合容量與重建品質間存在顯著的對數線性規律（R² = 0.86），將「表示豐富度」視為可預測擴充的新維度，類比於 NLP 中詞彙大小對語言模型的影響。

⚠️ **僅驗證在凍結編碼器與特定資料集上**  
本研究主要在 ImageNet‑256 上評估，使用的是凍結的預訓練視覺編碼器；未探討端到端訓練或其他解碼器架構的泛化情況，長期擴展性仍需後續工作驗證。

🎯 **視覺Tokenizer設計可參考語言模型的詞彙擴充策略**  
未來可將多層融合視為提升「表示詞彙量」的手段，在保持編碼器凍結的前提下，透過輕量路由模組獲得更豐富的潛在空間，從而改善重建與生成任務而不需重新訓練大型骨幹網路。

🔗 **論文連結**  
📝 Beyond the Last Layer: Multi-Layer Representation Fusion for Visual Tokenization  
👤 Xuanyu Zhu, Yan Bai, Yang Shi, Yihang Lou, Yuanxing Zhang (Peking University; Meituan Inc; Tsinghua University; IGDL)  
🔗 https://arxiv.org/abs/2605.10780

你認為在視覺Tokenizer中加入中層資訊是否值得投資？歡迎在留言區分享你的看法 👇

#CVPR2025 #視覺Tokenizer #DRoRAE #圖像生成 #多層融合 #PekingUniversity #Meituan #TsinghuaUniversity #AI研究
