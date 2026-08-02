---
title: Multilingual Semantic Retrieval for Apple Music Search
source: Apple ML
url: https://machinelearning.apple.com/research/multilingual-semantic-retrieval
score: 86
model: tencent/hy3:free
generated_at: '2026-07-15T08:35:06.690178'
---

📌 【Apple ML】混合檢索助 Apple Music 搜尋轉換增 2.28%

TL;DR：Apple Music 用多語語意檢索系統提升長尾查詢召回，線上轉換率升 2.28% 且免重訓 ranker。

🎣 每天數十萬新曲目湧入、橫跨 150 多個商店與數十種語言，Apple Music 的搜尋該如何應對拼錯字、音譯與跨語言查詢？更棘手的是，佔據多數獨特查詢的長尾搜尋，正是召回品質最薄弱的一環。

🤔 **長尾與跨語查詢成為召回瓶頸**
Apple Music 服務 150 多個 storefront（商店），支援數十種語言，曲庫每天增長數十萬首。在這種規模下，錯別字、音譯（transliteration）與跨語言查詢的搜尋召回，成為會話品質的關鍵驅動因子；尤其是佔大多數獨特查詢的長尾查詢（tail queries），其檢索難度最高。

🧩 **305M 參數 Siamese bi-encoder 與混合檢索架構**
這篇發表於 RecSys 2026 的論文提出一套多語言語意檢索系統，核心為一個 305M 參數的 Siamese bi-encoder，從 GTE-multilingual-base 微調（fine-tuned）而來，訓練採用 curriculum-scheduled multi-objective training（課程排程多目標訓練）。

部署上，系統透過混合檢索架構（hybrid retrieval architecture）整合進現有搜尋堆疊：將 dense nearest-neighbor（密集最近鄰）結果與既有的 token-based index（基於字詞的索引）混合，並使用 quantile distribution matching（分位數分佈匹配）對齊分數分佈。這樣做的好處是，下游 ranker 無需重新訓練即可上線。

資料流概念：使用者查詢 → bi-encoder 產生語意向量 → 密集檢索取 top-k → 與 token-based 索引結果依分位數匹配融合 → 輸出給既有排序器。

📊 **離線 Hit@10 提升 69%，線上全商店無衰退**
離線評估相對於基礎模型 GTE-multilingual-base，Hit@10 有 69% 的相對提升。

全球線上 A/B 測試結果：

| 指標 | 相對變化 |
|------|----------|
| 整體轉換率 (CR) | +2.28% |
| 無結果率 (no-result rate) | -86% |
| 長尾查詢 CR | +7.93% |
| 中頻查詢 CR | +0.89% |
| 高頻查詢 CR | +0.14% |

所有 storefront 均觀察到增益，且沒有出現任何衰退（regression）。改善集中於最需要的長尾查詢，而高頻熱門查詢幾乎不受幹擾，顯示語意檢索補強了困難查詢的召回，而不破壞既有服務。

🎯 **混合檢索是兼顧效能與部署成本的實務解方**
對工程師而言，這套架構的啟示在於：匯入 dense retrieval 不必推翻原有 token-based 系統，透過分佈匹配做分數融合，就能在不動下游 ranker 的前提下上線。且資源應優先投向長尾查詢體驗，因為語意檢索的紅利主要集中在那裡。

🔗 **來源**
- 標題：Multilingual Semantic Retrieval for Apple Music Search
- 作者／機構：Vishalaksh Aggarwal, Kevin Sebastian, Vivek Kanojiya, Leo Le, Nick Tucey, Santosh Shankar（* equal contribution；機構未提及）
- 連結：https://machinelearning.apple.com/research/multilingual-semantic-retrieval

#AppleMusic #MultilingualRetrieval #SemanticSearch #SiameseBiEncoder #HybridRetrieval #RecSys #SearchQuality #TailQueries #ConversionRate #ABTesting
