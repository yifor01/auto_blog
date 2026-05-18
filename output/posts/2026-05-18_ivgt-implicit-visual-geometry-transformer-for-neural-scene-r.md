---
title: "IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.16258
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-18T20:42:29.257182
---

📌 **IVGT：無需相機姿態即可學習連續 3D 場景表示**

🎣 **你以為重建 3D 場景一定需要已知相機姿態？最新研究顯示，連這個前提都可以省略**

🤔 **從有姿態到無姿態：未解的幾何重建瓶頸**  
多視角圖像重建傳統上依賴已知相機位姿，否則幾何一致性難以保證。現有的視覺幾何基礎模型多半透過回歸像素對齊的點圖來顯式預測幾何，這種方式往往帶來冗餘且難以保證幾何的連續性。

🧪 **透過 Transformer 隱式建模幾何的實驗設計**  
IVGT 採用 Transformer 架構，將來自無姿態多視圖像的特徵隱式編碼為一個位於標準座標系的連續神經場景表示。該表示支援任意 3D 位置的空間查詢，透過輕量解碼器即可得到符號距離 (SDF) 與顏色值，進而直接提取連續且幾何連續的曲面。

🔑 **隱式幾何表示支援任意 3D 位置的連續查詢**  
因為幾何是以隱式方式建模，IVGT 能在任何 3D 座標進行局部特徵檢索，從而預測該點的 SDF 與顏色。這使得從任意視點合成 RGB 圖像、深度圖以及法線圖變得直接可行，無需先顯式重建點雲或網格。

💡 **多任務泛化與幾何正則化的訓練策略**  
訓練階段採用多數據集聯合優化，同時利用 2D 監訊號與 3D 幾何正則化項。這樣的設計讓模型在未見過的場景中仍能保持幾何一致性，並在網格與點雲重建、新視角合成、深度與法線估計以及相機姿態估計等任務上展現不俗的泛化能力。

⚠️ **僅在多數據集聯合優化下驗證，具體泛化邊界尚未探討**  
目前的實驗僅在多個公開數據集上的聯合訓練與測試下進行，未具體說明在極端稀疏視角或完全無重疊的圖像集合上的表現，亦未針對長時間序列或動態場景做驗證。

🎯 **對於需要靈活視點合成的系統，隱式表示提供新可能**  
IVGT 證明，透過隱式神經表示與 Transformer 的結合，可以在不知道相機姿態的情況下學習到連續且幾何連貫的場景表示。對於需要即時視點切換、AR/VR 渲染或機器人環境感知的應用，這種範式提供了一種免除顯式姿態估計步驟的潛在路徑。

🔗 **論文連結**  
📝 **IVGT: Implicit Visual Geometry Transformer for Neural Scene Representation**  
👤 Yuqi Wu, Tianyu Hu, Wenzhao Zheng, Yuanhui Huang, Haowen Sun (Tsinghua University)  
🔗 https://arxiv.org/abs/2605.16258  

你認為在無姿態條件下進行 3D 重建，是否會成為未來視覺感知系統的標準做法？歡迎在留言區分享你的看法 👇  

#CVPR #3DReconstruction #NeuralRadianceFields #Transformer #Tsinghua #ComputerVision #Graphics #AIResearch
