---
title: "A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.04913
score: 131
model: gpt-4o-free
generated_at: 2026-04-07T13:02:03.456701
---

📌 **【Amazon 聯手 JHU 提出】一幀僅需一個 Token，影片世界模型算力砍 99.5%**

你以為生成高畫質未來影格，必須堆疊數百億參數與龐大算力？最新研究給出反直覺答案：只要把相鄰幀的特徵差值壓縮成單一 Token，生成多樣未來不僅可行，還能把計算量砍掉 2000 倍。

🤔 **世界模型的算力瓶頸：要精準預測，還是多樣生成？**

影片世界模型的核心挑戰在於預測不確定的未來。傳統辨別式模型只能給出單一確定性輸出，本質上是對所有可能未來的平均化，失去真實世界的多樣性。現有生成式模型雖能產出多樣結果，但計算成本極高，難以擴展。近期研究指出，直接在視覺基礎模型 (VFM) 的特徵空間預測，比傳統像素還原的潛空間需要更少參數，但多數仍停留在辨別式架構。如何兼顧生成多樣性與計算效率，成為產業落地關鍵。

🧪 **3D 時空壓成 1D 序列的極致壓縮設計**

團隊提出 `DeltaTok` 分詞器與 `DeltaWorld` 生成模型。核心設計在於不直接編碼單一影格，而是計算相鄰幀之間在預訓練 VFM 空間中的特徵差值，將其編碼為單一連續的 delta token。這將原本三維的時空影片表示，直接坍縮為一維的時間序列。以 512x512 解析度為例，Token 數量減少超過 1024 倍。基於此輕量表示，團隊能進行多假設平行訓練，同時生成多個未來路徑，僅對最接近真實的假設進行監督學習。

📊 **35 倍參數縮減，2000 倍 FLOPs 下降**

在密集預測任務上，DeltaWorld 的預測結果與真實物理結果的吻合度顯著提升。實驗數據顯示：
- 模型參數量較現有生成式世界模型減少 35 倍以上
- 計算浮點運算量 (FLOPs) 降低達 2000 倍
- 推論階段僅需單次前向傳播，即可輸出多樣化的合理未來預測

💡 **用「差值」建模，避開像素重構的冗餘計算**

為什麼 Delta Token 能同時兼顧效率與多樣性？關鍵在於 VFM 已具備高階語意與空間結構理解，相鄰幀的差異主要集中在物體運動與局部變化，而非背景靜態資訊。直接建模特徵差值，等於讓模型專注於動態變化量，跳過冗餘的靜態像素重建。搭配多假設訓練策略，模型在推論時自然能解碼出不同運動軌跡的分支，無需依賴傳統自回歸模型耗時的逐步生成。

⚠️ **依賴預訓練 VFM 品質，測試場景限於密集預測**

此架構的效能高度綁定上游 VFM 的特徵表達能力，若 VFM 對特定領域特徵提取不佳，Delta Token 的預測上限將受影響。此外，實驗主要聚焦於密集預測任務的短期到中期未來生成，尚未驗證極長時序或開放式場景下的穩定性。多假設訓練雖高效，但僅監督最佳假設的策略在極端分佈外推時，可能面臨模式崩潰風險。

🎯 **輕量化多假設生成，適合邊緣部署與即時模擬**

對於正在開發影片預測、自動駕駛模擬或機器人世界模型的團隊，此架構提供明確的工程路徑：
- 以 VFM 特徵差值取代原始像素或光學流，大幅降低輸入維度
- 捨棄逐步自回歸，改用平行多假設推論，實現即時多樣化預測
- 在算力受限的邊緣裝置或即時互動應用中，此架構比傳統 Video LVM 更具部署可行性
- 建議搭配動態路由或置信度閾值，進一步篩選推論階段的多假設輸出

🔗 **論文連結**
📝 A Frame is Worth One Token: Efficient Generative World Modeling with Delta Tokens
👤 Tommie Kerssies, Gabriele Berton, Ju He, Qihang Yu, Wufei Ma @ Amazon; Eindhoven University of Technology; Johns Hopkins University
🔗 論文：https://arxiv.org/abs/2604.04913
💻 程式碼與權重：https://deltatok.github.io

你目前的世界模型架構，是卡在算力瓶頸，還是預測結果過於單一？歡迎留言討論你的實戰經驗 👇

#WorldModel #ComputerVision #GenerativeAI #VideoGeneration #VFM #AmazonResearch #AI模型優化 #多模態 #邊緣運算
