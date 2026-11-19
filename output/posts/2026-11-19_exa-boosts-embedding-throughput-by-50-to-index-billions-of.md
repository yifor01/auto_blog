---
title: Exa boosts embedding throughput by 50% to index billions of documents on AWS
  AI chips
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/exa-boosts-embedding-throughput-by-50-to-index-billions-of-documents-on-aws-ai-chips/
model: claude-code/sonnet
generated_at: '2026-11-19T23:47:23.207918'
score: 95
---

📌 Exa 如何靠自訂 Kernel 把 Embedding 吞吐量硬拉高 50%

TL;DR：Exa 用自製 NKI kernel 優化 AWS Neuron 晶片，讓數十億文件的 embedding 成本降了近五成。

當你的索引規模是「數十億到數百億份文件」時，省下每份文件 1% 的 embedding 成本,乘上規模之後就是一筆可觀的數字。Exa 這次用一場「被迫加倍的負載」逼出了一套完整的硬體優化方法論。

🤔 **一次模型升級，讓推論負載直接翻倍**

Exa 建構的是一個以語意搜尋為核心的網路索引系統,用 multi-tower semantic ML 模型把網頁內容與查詢同時嵌入同一個向量空間，背後靠自研向量資料庫服務。原始資料流程是 Crawlers → Parse → Moderate and filter → Embed，最後送進向量資料庫。

這次優化的起點是一次模型遷移：Exa 決定換用更好的文件模型，必須把 300 億份高優先文件重新 embedding。既有索引的即時 embedding 流程還得照常運作，等於兩條管線並行,直接把推論負載加倍。Exa 把這次「被迫的壓力測試」當成重新評估硬體選型的時機，目標鎖定 AWS Inferentia2 與 AWS Trainium2（統稱 AWS Neuron 硬體家族）。

🧩 **從 FP16 基礎版，一路榨到自訂 Kernel**

Exa 的初版實作是在 inf2.xlarge（單晶片、雙 NeuronCore）上做最單純的資料並行、FP16 表示法。之後的優化是一連串疊代，依序是：

1. **weight layout optimization**：調整權重排列方式配合模型排程與佈局，消除不必要的 transpose。
2. **autocast**：讓編譯器在矩陣乘法時降精度運算，同時保留動態範圍。輸出必須通過 0.999 cosine similarity 的正確性門檻才算合格。
3. **NKI（Neuron Kernel Interface）預建 kernel**：直接套用現成的 attention kernel，快速清除最明顯的低效率問題。
4. **自訂 weight-stationary fused SwiGLU MLP kernel**：用 Neuron Explorer 剖析發現大量 HBM（高頻寬記憶體）spill/reload，Tensor Engine 沒被餵飽。Exa 先用預建 MLP kernel 當墊腳石找出問題，再手寫融合版 kernel 消除 HBM 停滯。
5. **針對實際模型形狀重寫 attention kernel**：發現雙核同時跑時的實測吞吐量遠低於理論值,代表核心間存在資源競爭,而 Tensor Engine 尚未被完全餵飽。於是 Exa 按模型 head 架構的真實形狀砍掉 padding 浪費的 FLOPS，並把多步驟的 attention 運算融合成單一 matmul，減少內迴圈運算與 HBM 來回次數。

📊 **最終成績：每百萬份文件的效能與成本改善 47%**

從最初的naive compile到最終版本，吞吐量（docs/sec）累積提升約 1.5 倍，整體換算成每百萬份文件的效能與成本，改善幅度達 47%。

💡 **讓 Agent 自己找優化方向，而非工程師手動調**

這些優化幾乎全部由 AI agent 在一套三段式驗證框架裡自主完成，用 Flyte 工作流平臺讓每個 agent 跑自己的流程：編譯出 NEFF 可執行檔，對照基準資料集驗證正確性（必須達到 0.999 cosine similarity），接著剖析一次前向傳播，再做 30 分鐘的飽和度壓力測試。

Exa 依任務難度分派不同成本的 agent：輕量模型做網格搜尋編譯參數之類的瑣碎工作並做正確性把關，推理型 agent 負責驗證複雜假設、找瓶頸,最強的程式碼生成模型才負責寫自訂 kernel。這套分工既控制了成本,也用驗證機制避免強力 agent 在沒有護欄的情況下跑偏。

⚠️ **目前只調好了一個區域**

Exa 目前的優化成果僅在美西（Oregon，us-west-2）區域驗證過。單一區域、單一機型的供應量有限，容易撞上運算短缺。為此 Exa 用同一套 Kubernetes 控制平面跨多區域排程，依效能與成本比把 pod 排到最便宜的節點上，並隨 embedding 需求動態調度。

🎯 **實務啟示**

如果你的推論工作負載是高度重複、規模巨大的任務，把優化拆成「正確性驗證 → 剖析瓶頸 → 針對性改 kernel」三步，再讓不同成本等級的 agent 各司其職,是一條值得參考的路徑。重點不是盲目追求最強硬體，而是先確認瓶頸在哪（這次是 HBM spill 與 FLOPS 浪費），再決定要不要寫自訂 kernel。

🔗 **來源**
- 標題：Exa boosts embedding throughput by 50% to index billions of documents on AWS AI chips
- 作者／機構：Summer Devlin, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/exa-boosts-embedding-throughput-by-50-to-index-billions-of-documents-on-aws-ai-chips/

#AWS #Inferentia2 #Trainium2 #Embedding #VectorDatabase #NeuronSDK #AIInfrastructure #SemanticSearch #AgenticAI #MLOps
