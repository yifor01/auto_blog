---
title: "Versioned Late Materialization for Ultra-Long Sequence Training in Recommendation Systems at Scale"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2604.24806
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-04-29T19:54:40.608414
---

📌 **【Meta 實戰】解決推薦系統長序列訓練的 I/O 牆**

當大家都在追求長序列 (Long Sequence) 來提升推薦模型品質時，你是否發現資料基礎設施的成本已經失控？在 Meta 的生產環境中，傳統的「Fat Row」範式正遭遇前所未有的擴展性瓶頸。

🤔 **長序列的代價：當資料冗餘壓垮 GPU 算力**

推薦系統的 Scaling Law 告訴我們，更長的使用者互動歷史 (UIH) 能帶來更好的模型品質。然而，現有的「Fat Row」架構要求將序列預先物化 (Pre-materialize) 到每一筆訓練樣本中。這在多租戶環境下是災難性的，因為不同模型對序列長度的需求不同，導致資料冗餘被極度放大，最終讓資料基礎設施的負載遠超 GPU 訓練所需，形成巨大的 I/O 牆。

🧪 **版本化延遲物化：像資料庫優化般重構訓練流程**

Meta 團隊提出了一種全新的「版本化延遲物化 (Versioned Late Materialization)」範式。不同於傳統的預先展開，該系統將 UIH 規範化地存儲在一個不可變的儲存層，僅在訓練時透過輕量級的版本指標 (Versioned Pointers) 即時重構序列。

🔗 **O2O 一致性與多租戶支援的系統級創新**

這項技術的核心亮點在於解決了產業界的兩大痛點：
1. **O2O 一致性**：透過分叉協議 (Bifurcated Protocol)，有效防止了在串流 (Streaming) 與批次 (Batch) 訓練中的未來資訊洩漏 (Future Leakage)。
2. **多維度投影下推**：針對異構的多租戶模型，提供讀取優化的不可變儲存層，支援按需投影，大幅降低無效 I/O。

💡 **計算資源不再被 I/O 綁架**

為了掩蓋訓練時序列重構的延遲，系統採用了「計算與資料解耦」的預處理架構，配合管線化的 I/O 預取 (Prefetching) 與資料親和性優化。實測結果顯示，這成功將訓練吞吐量轉變為 GPU 運算瓶頸，而非 I/O 瓶頸。

📈 **生產環境驗證：成本下降，品質提升**

部署於 Meta 生產環境的 DLRM 後，該系統不僅顯著降低了訓練資料基礎設施的資源消耗，更支撐了激進的序列長度擴展。這直接轉化為顯著的模型品質提升，並已成為 HSTU 和 ULTRA-HSTU 等現代推薦架構的基石。

⚠️ **技術門檻與架構複雜度**

這是一個高度客製化且依賴 Meta 內部基礎設施的解決方案。對於缺乏強大資料工程團隊的組織，要複製這種「延遲物化」與「不可變儲存層」的設計，在系統維護與除錯上會有較高的門檻。

🎯 **給推薦系統架構師的啟示**

如果你的團隊正面臨長序列訓練的資料膨脹問題，或許該從「資料庫正規化」的角度重新審視訓練樣本的設計。將資料儲存與訓練消費解耦，並針對多租戶場景進行優化，是突破 Scaling Law 成本邊際的關鍵。

🔗 **論文連結**
📝 Versioned Late Materialization for Ultra-Long Sequence Training in Recommendation Systems at Scale
👤 Liang Guo, Ge Song, Litao Deng, Jianhui Sun, Chufeng Hu @ Meta Platforms, Inc.
🔗 https://arxiv.org/abs/2604.24806

你們在處理長序列推薦模型時，也遇到過類似的 I/O 瓶頸嗎？歡迎在留言區交流解決方案 👇

#Meta #RecSys #DeepLearning #DataEngineering #DLRM #HSTU #AIInfrastructure #推薦系統 #系統架構
