---
title: "One Pool, Two Caches: Adaptive HBM Partitioning for Accelerating Generative Recommender Serving"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.04450
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:19:40.160172
---

📌 【阿里巴巴 x 浸大】動態分配 HBM，推薦系統延遲大降 38%

生成式推薦系統（Generative Recommender）雖然效果驚人，但在 GPU 記憶體管理上卻有一個隱形殺手。當 Embedding Cache 與 KV Cache 在有限的 HBM 中爭奪地盤時，僵化的靜態分配正讓你白白浪費 20-30% 的性能提升空間。

🤔 **生成式推薦系統的 HBM 記憶體拉鋸戰**

在生成式推薦服務中，Embedding 熱快取（EMB）與 KV Cache 是兩大核心元件，兩者都高度依賴高頻寬記憶體（HBM）。現有系統通常將兩者分開優化，忽略了一個關鍵事實：在不同工作負載下，兩者的最佳記憶體分配比例會動態變化，幅度甚至高達 0.35。這種「各管各的」策略，導致了顯著的延遲浪費。

🧪 **32 節點 A100 集群與三層 PPO 控制器**

香港浸會大學與阿里巴巴團隊提出 HELM 框架，透過兩大機制解決這個問題：
1. **自適應記憶體分配**：採用三層 PPO 架構（凍結基礎策略、線上殘差適配器、突發感知恢復控制器），能在 32 微秒內完成決策，精準追蹤離線最佳比例。
2. **感知式排程**：在請求路由時，同時考量 KV 駐留狀態、Embedding 局部性與節點負載，避免因異質分配造成的路由效率低下。

 **P99 延遲降低 38%，SLO 達成率近 100%**

在生產級數據集上的大規模測試顯示，HELM 顯著優於現有最佳靜態策略：
- **延遲優化**：P99 延遲降低 24-38%。
- **穩定性提升**：在穩定、趨勢與突發（Burst）三種負載下，SLO（服務等級目標）達成率高達 93.5-99.6%。
- **決策效率**：控制器決策延遲僅 32µs，且分配比例誤差控制在 0.024-0.029 之間。

💡 **打破孤立優化，實現聯合管理**

這項研究的核心洞察在於，記憶體分配不應是靜態配置，而應與請求調度協同運作。透過將 EMB 與 KV 的競爭關係納入統一的控制框架，HELM 解決了傳統方法在線上重新分配時產生的 H2D（Host to Device）傳輸瓶頸，避免了關鍵路徑上的 SLO 違規。

⚠️ **未開源程式碼，實際部署需自行實作**

儘管論文提供了詳細的架構設計與實驗數據，但目前並未釋出開源程式碼。對於希望採用此技術的企業而言，需要基於論文中的 PPO 三層架構自行開發，增加了落地門檻。此外，實驗環境基於 A100 集群，在新型號 GPU 上的表現尚待驗證。

🎯 **動態資源調度將成為高效能推薦系統的標配**

隨著生成式 AI 推薦模型的參數量與服務規模持續增長，傳統的靜態記憶體管理將難以應付複雜多變的流量。HELM 展示了一種可行的路徑：利用強化學習進行微秒級的資源決策，這對於追求極致效能的推薦系統團隊極具參考價值。

🔗 **論文連結**
📝 One Pool, Two Caches: Adaptive HBM Partitioning for Accelerating Generative Recommender Serving
👤 Wenjun Yu, Shuguang Han, Amelie Chi Zhou
🏫 Hong Kong Baptist University; Alibaba Inc
🔗 https://arxiv.org/abs/2605.04450

你們在部署生成式推薦系統時，有遇到 HBM 記憶體不足的問題嗎？歡迎分享你的解法 👇

#AI #RecommenderSystem #GPU #HBM #SystemOptimization #Alibaba #HKBU #MachineLearning #高效能運算
