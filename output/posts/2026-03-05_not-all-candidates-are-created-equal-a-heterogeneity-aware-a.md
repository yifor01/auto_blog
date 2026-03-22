---
title: "Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking in Recommender Systems"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.03770
score: 113
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-05T12:22:31.382767
---

📌 【ByteDance 最新研究】推薦系統的效率革命：不是所有候選人都一樣

你知道嗎？你每天刷的 TikTok、今日頭條，背後的推薦系統正在進行一場效率革命。ByteDance 的研究團隊發現：傳統的預排序方法，其實浪費了大量的計算資源。

🤔 **推薦系統為什麼要預排序？**

現代大型推薦系統通常採用多階段級聯：召回 → 預排序 → 排序 → 重排序。預排序階段承擔著從海量候選中快速篩選出幾百個的重任，是整個系統的效率瓶頸。

🧪 **問題在哪裡？**

傳統預排序方法的最大問題是：把所有候選人都當成一回事。研究團隊發現，從不同來源採樣的訓練樣本本質上是異質的：

- 粗粒度召回的樣本：相對容易預測
- 細粒度排序的樣本：相對困難
- 曝光反饋的樣本：中等難度

當這些異質樣本混在一起訓練時，會產生「梯度衝突」：困難樣本主導訓練過程，而簡單樣本被低估利用，導致模型表現不佳。

 **不是所有候選人都一樣**

研究團隊提出了一種異質性感知的適應性預排序框架 (HAP)，核心理念很簡單卻很有效：**對待不同難度的候選人，採取不同的策略**。

具體來說：
- 輕量級模型處理所有候選，確保覆蓋率
- 重型模型專門處理困難候選，保證準確性
- 根據難度動態分配計算預算

這種方法不僅提升了預排序效果，還降低了計算成本。

⚡ **真實世界的成效**

HAP 已經在今日頭條的生產系統中部署了 9 個月，取得了令人印象深刻的成果：

- 用戶使用時長提升 0.4%
- 活躍天數提升 0.05%
- 沒有額外計算成本

在工業級別的推薦系統中，這種微小的提升往往意味著巨大的商業價值。

🎯 **為什麼這很重要？**

這項研究為工業級推薦系統的擴展策略提供了實用的視角。它告訴我們：

1. 異質性是現實，而不是需要被消除的問題
2. 智慧分配資源比一視同仁更有效
3. 效率提升可以與準確性提升並行不悖

🔗 **論文連結**
📝 Not All Candidates are Created Equal: A Heterogeneity-Aware Approach to Pre-ranking in Recommender Systems
👤 Pengfei Tong, Siyuan Chen, Chenwei Zhang, Bo Wang, Qi Pi @ ByteDance
🔗 論文：arxiv.org/abs/2603.03770
🔗 數據集：已開源的大型工業混合樣本數據集

#推薦系統 #機器學習 #效率優化 #ByteDance #今日頭條 #TikTok #InformationRetrieval

你認為這種異質性處理方法還可以應用在哪些領域？歡迎分享你的想法 👇
