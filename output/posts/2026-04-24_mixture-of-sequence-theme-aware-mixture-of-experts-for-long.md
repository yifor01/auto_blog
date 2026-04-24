---
title: "Mixture of Sequence: Theme-Aware Mixture-of-Experts for Long-Sequence Recommendation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2604.20858
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-04-24T19:23:53.944251
---

📌 【UIUC & Meta 聯合研究】MoS：解決長序列推薦中的「興趣漂移」難題

長序列推薦系統（Sequential Recommendation）一直有個痛點：使用者行為跨度越大，裡面混雜的雜訊就越多。UIUC 與 Meta 的研究團隊發現，使用者在長序列中往往存在「Session Hopping（跨時段跳躍）」現象，這讓模型很難抓準當下的真實意圖。

🤔 **長序列推薦的致命傷：Session Hopping 與主題漂移**

在預測點擊率（CTR）時，雖然長序列能捕捉動態興趣，但使用者的興趣在短時間內（Session）雖穩定，跨 Session 後卻可能劇烈轉變，甚至過幾個 Session 又繞回來。這種行為模式導致原始序列中充滿了不相關或誤導性的資訊（Noise），傳統模型很難有效過濾。

🧪 **MoS 框架：主題感知路由 + 多尺度融合**

研究團隊提出了 **Mixture of Sequence (MoS)**，這是一個 Model-Agnostic（與模型架構無關）的 MoE（專家混合）方法。其核心設計有兩大機制：

1.  **主題感知路由 (Theme-Aware Routing)**：自適應地學習使用者序列的潛在主題，將原始序列組織成多個連貫的子序列。每個子序列僅包含與特定主題對齊的 Sessions，從而過濾掉因興趣轉移帶來的雜訊。
2.  **多尺度融合機制 (Multi-Scale Fusion)**：引入三類專家（Experts）分別捕捉：
    *   全域序列特徵
    *   短期使用者行為
    *   主題特定的語義模式

 **SOTA 性能與更低 FLOPs 的雙重勝利**

實驗結果顯示，MoS 在長序列推薦任務中穩定達到了 SOTA（State-of-the-Art）性能。更重要的是，與其他 MoE 架構相比，MoS 引入了更少的 FLOPs（浮點運算數）。這證明了該框架在「效能」與「效率」之間取得了極佳的平衡。

💡 **MoE 的設計哲學：過濾雜訊而非堆疊參數**

這篇論文的一個重要啟示在於，MoE 架構的優勢不僅在於增加模型容量，更在於其「路由機制」能針對性過濾長序列中的無關資訊。透過將「Session」視為基本單位進行主題切分，MoS 解決了長期困擾推薦系統的「主題漂移」問題。

⚠️ **聚焦長序列場景，通用性需視應用而定**

雖然 MoS 是 Model-Agnostic 的，但論文主要驗證其在長序列推薦場景下的有效性。在短序列或使用者行為變化極快的場景中，其多尺度融合的複雜度是否帶來邊際效益遞減，尚需進一步觀察。

🎯 **工程實踐：關注主題粒度的切割**

對於開發者而言，MoS 提供了一個極佳的實作範本。如果你正在處理含有大量雜訊的長序列數據（如使用者瀏覽歷史、日誌分析），不妨參考其「主題感知路由」的設計，嘗試將序列按潛在主題切分，或許能顯著提升模型準確度。

🔗 **論文連結**
📝 Mixture of Sequence: Theme-Aware Mixture-of-Experts for Long-Sequence Recommendation
👤 Xiao Lin, Zhicheng Tang, Weilin Cong, Mengyue Hang, Kai Wang (UIUC & Meta)
🔗 論文：https://arxiv.org/abs/2604.20858
💻 開源程式碼：https://github.com/xiaolin-cs/MoS

你們在處理推薦系統序列建模時，遇過哪些關於「長序列雜訊」的問題？歡迎在留言區交流 👇

#推薦系統 #MoE #MachineLearning #序列建模 #MetaAI #UIUC #AIResearch #DeepLearning
