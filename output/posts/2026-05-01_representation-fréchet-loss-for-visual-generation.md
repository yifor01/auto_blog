---
title: "Representation Fréchet Loss for Visual Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.28190
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-05-01T19:30:14.524848
---

📌 【OpenAI、USC、CMU、CUHK等】解耦FD損失 優化視覺生成訓練

長期以來，Fréchet Distance（FD）被學界公認不適合作為生成模型的訓練目標，僅能用於評估分數計算。
但最新研究成功將其轉化為可直接優化的損失函數，還讓ImageNet一步生成器的FID達到0.72？
關鍵改動非常簡單：僅解耦了FD估計與梯度計算的批次規模設定。

🤔 **FD長期被視為不可訓練的評估指標，缺乏優化路徑**
Fréchet Distance（FD）是生成模型領域常用的分佈距離指標，用於衡量生成數據與真實數據的分佈差異，但過去由於估計FD需要大規模總體樣本，與梯度計算的批次大小需求衝突，長期被認為無法作為訓練目標直接優化。本研究目標正是突破這一限制，將FD轉化為可在表示空間中有效優化的損失函數。

🧪 **解耦FD估計與梯度計算的批次大小，提出FD-loss**
研究團隊的核心設計十分簡潔：將FD估計所需的總體樣本數（例如5萬筆）與梯度計算所需的批次大小（例如1024筆）完全解耦，讓FD可以在表示空間中被穩定優化，這種方法被命名為FD-loss。

💡 **一步生成器FID達0.72，免蒸餾壓縮多步模型**
優化FD-loss後出現多項重要發現：
1. 使用FD-loss對基礎生成器進行後訓練，在不同表示空間中都能一致提升視覺質量；在Inception特徵空間下，一步生成器在ImageNet 256x256任務上達到0.72 FID。
2. 相同的FD-loss可以將多步生成器直接轉化為性能強大的一步生成器，全程無需教師蒸餾、對抗訓練或逐樣本目標設定。
3. 傳統FID
