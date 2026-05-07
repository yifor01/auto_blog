---
title: "Geometry-Aware State Space Model: A New Paradigm for Whole-Slide Image Representation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.05164
score: 95
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:52:02.670848
---

📌 几何感知SSM：WSI表征新范式

你以為病理AI只要堆更多patch就能更準？錯，空間幾何選不對，再多的數據也沒用。
現有模型大多把組織patch嵌在歐幾里得空間，完全忽略病理組織的層級結構與區域異質性，分類準確度早就碰到天花板。

🤔 **病理切片AI卡在歐幾里得空間的局限**
全切片圖像（WSI）是將組織標本數位化的吉像素級影像，是病理診斷與治療規劃的核心依據，但需聚合數千個patch才能完成切片級預測。現有方法多採用多實例學習（MIL）兩階段範式，將tile級嵌入與切片級預測解耦，但大多將patch表示隱式嵌入齊次歐幾里得空間，忽略了病理組織的層級結構與區域異質性，導致模型難以捕捉全局組織架構與細粒度細胞形態。

🧪 **雙幾何空間結合S4與分塊MoE的BatMIL框架**
本研究提出混合雙曲-歐幾里得表示，將WSI特徵嵌入雙幾何空間，實現層級組織結構與局部形態細節的互補建模。基於此設計的BatMIL框架，採用結構化狀態空間序列模型（S4）作為骨幹，以線性計算複雜度編碼數千個patch的長程依賴；同時引入分塊級混合專家（MoE）模組，將patch分組為區域並動態路由至專用子網絡，在提升表徵能力的同時減少冗餘計算。實驗涵蓋7個WSI數據集、6種癌症類型，驗證切片級分類任務性能。

💡 **切片級分類持續優於現有SOTA MIL方法**
在7個涵蓋6種癌症類型的WSI數據集上，BatMIL的切片級分類性能持續優於現有最先進的MIL方法，證明幾何感知表徵學習是下一代計算病理的有力方向。

💡 **雙幾何空間互補是性能提升核心**
雙曲幾何天然適合建模病理組織的層級結構（如細胞-組織-器官的層級關係），歐幾里得空間則更擅長表徵局部細胞形態細節，兩者互補解決了傳統單空間嵌入的缺陷。S4的線性計算複雜度避免了Transformer處理長序列時的二次複雜度問題，可高效處理數千個patch的序列；分塊MoE則針對不同區域的組織異質性，動態分配計算資源，進一步提升表徵效率。

⚠️ **公開摘要未提及具體研究限制**
目前釋出的論文摘要未說明具體研究限制，完整實驗細節、消融實驗結果與侷限性分析可參考arxiv完整論文。

🎯 **計算病理可採用幾何感知表徵思路**
該研究的幾何感知表徵範式為計算病理的WSI分析提供了清晰且技術豐富的新方向，其混合雙空間設計、高效序列建模與區域異質性處理思路，也可供其他需處理大規模序列、區域異質性數據的計算機視覺任務參考。

🔗 **論文連結**
📝 Geometry-Aware State Space Model: A New Paradigm for Whole-Slide Image Representation
👤 Enhui Chai, Sicheng Chen, Tianyi Zhang, Chad Wong, Kecheng Huang
🏫 PuzzleLogic Pte Ltd; University of California, Irvine; National University of Singapore
🔗 https://arxiv.org/abs/2605.05164

#計算病理 #計算機視覺 #MIL #狀態空間模型 #WSI #病理AI #CVPR #機器學習
