---
title: "Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.21724
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-04-24T19:31:16.797790
---

📌 【中科院等】X-GRAM 高效扩展模型容量

你以為擴大模型容量只能堆算力、漲記憶體？0.73B參數規模下，這篇研究用僅50%大小的嵌入表，準確度反而比基準線高出4.4個點。

🤔 **傳統大Token嵌入表擴容的3大核心痛點**
現有的大Token索引查找表（存儲詞嵌入的靜態參數表，推理時透過Token ID直接查找對應向量）本來提供了一條算力解耦的擴展路徑，不需要增加浮點運算（FLOPs）就能擴大模型容量，但實際增益長期受限於三大問題：一是符合齊普夫分布（少數高頻Token佔據多數出現次數，大量低頻長尾Token訓練不足）導致的長尾欠訓練；二是不同神經網絡層對嵌入的需求存在異質性，統一大小的嵌入表無法匹配各層需求；三是槽位坍塌（Slot Collapse，嵌入表產生大量冗餘、無效的嵌入向量），嚴重浪費參數與記憶體。

🧪 **0.73B/1.15B規模驗證，50%表大小勝過強基線**
針對上述痛點，中科院、北大等機構的研究團隊提出X-GRAM，一套頻率感知的動態Token注入框架。核心設計包括：1. 混合哈希（Hybrid Hashing）與別名混合（Alias Mixing）技術，壓縮長尾Token的嵌入存儲，同時保留高頻頭部的嵌入容量；2. 透過歸一化SwiGLU ShortConv（結合SwiGLU激活函數與輕量短卷積）提取多樣化的局部n-gram特徵；3. 使用深度感知門控（Depth-Aware Gating），將提取的特徵信號整合到注意力值流與層間殘差中，讓靜態嵌入記憶體與動態上下文對齊。整體設計引入了以記憶體為中心的擴展軸，徹底解耦模型容量與FLOPs（算力）。

 **小50%嵌入表，準確度最高提升4.4個點**
團隊在0.73B與1.15B參數規模下進行廣泛評測，結果顯示：X-GRAM相比原始模型主幹（Vanilla Backbone）平均準確度最高提升4.4個點，相比強檢索基線也高出3.2個點。值得注意的是，這些提升是在僅使用50%配置的更小嵌入表的前提下達成的，參數效率顯著優於現有方案。

 **解耦算力與容量，開闢記憶體中心擴展新路徑**
傳統模型擴容要麼堆嵌入表大小（漲記憶體、參數效率低），要麼堆模型層數/寬度（漲算力、FLOPs增加），X-GRAM的創新在於把容量擴展從算力綁定中解放出來：針對長尾問題用混合哈希壓縮尾部，針對層異質問題用深度門控適配不同層需求，針對槽位坍塌問題用動態Token注入減少冗餘，最終實現靜態記憶體的高效利用，為未來記憶增強架構提供了可落地的設計範式。

⚠️ **僅驗證0.7-1.1B規模，更大模型效果待確認**
目前論文僅在0.73B與1.15B參數規模下完成驗證，尚未覆蓋更大參數規模的場景，擴展性仍有待後續研究確認。

🎯 **小模型部署可優先嘗試，開源代碼可直接復現**
對於資源受限的端側部署、小參數模型優化場景，X-GRAM的高參數效率特性非常實用，能在不增加算力負擔的前提下提升模型效果。研究團隊已開源完整實作代碼，開發者與研究者可直接拉取復現，也可參考其記憶體中心的擴展思路，優化現有NLP模型的嵌入層設計。

🔗 **論文連結**
📝 論文標題：Beyond N-gram: Data-Aware X-GRAM Extraction for Efficient Embedding Parameter Scaling
👤 作者：Yilong Chen, Yanxi Xie, Zitian Gao, He Xin, Yihao Xiao
🏫 所屬機構：Chinese Academy of Sciences; University of Chinese Academy of Sciences; Peking University; IQuest Research
🔗 論文地址：https://arxiv.org/abs/2604.21724
💻 開源代碼：https://github.com/Longyichen/X-gram

你最近在優化小參數模型時遇到過嵌入層效率問題嗎？歡迎分享你的經驗👇

#AI #NLP #機器學習 #模型優化 #嵌入技術 #中科院 #XGRAM #記憶體優化 #小模型部署
