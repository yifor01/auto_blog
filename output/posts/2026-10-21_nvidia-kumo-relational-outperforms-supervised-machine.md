---
title: NVIDIA Kumo Relational Outperforms Supervised Machine Learning on Relational
  Data, No Training Required
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/kumo-relational
model: claude-code/sonnet
generated_at: '2026-10-21T20:56:51.986549'
score: 102
---

📌 【NVIDIA】關聯式資料庫免訓練，基礎模型完勝監督式 ML

TL;DR：NVIDIA Kumo Relational 不用訓練、不用特徵工程，直接在資料庫上做預測，效能超越 XGBoost 與 AutoGluon。

企業資料團隊最熟悉的夢魘之一，就是為了一個 churn 預測專案，花上好幾週做特徵工程、調 pipeline，結果業務需求一變，整套流程又要推翻重做。NVIDIA 最新發布的 Kumo Relational，想把這整個流程壓縮成「連上資料庫、寫一句查詢」。

🤔 **關聯式資料被迫攤平成一張表，訊號就丟了**

真實世界的資料不是單一表格，而是 users、orders、products 這類跨表且隨時間演化的關聯式結構。過去要做預測，得先靠人工把這些關係攤平成一張表（例如手動算出「過去 30 天平均訂單金額」），這個過程既耗費人力，也會丟掉細粒度的結構訊號。Kumo Relational 的設計目標，就是讓模型直接尊重資料庫原本的表格、外鍵（foreign key）與時間戳記，不需要攤平。

🧩 **一次 forward pass，做三件事**

Kumo Relational 是一個預訓練好的 Relational Foundation Model，透過 in-context learning 在推論時讀取多達 10,000 筆歷史案例作為上下文，每筆案例是「某個實體在某個時間點的局部子圖」搭配其真實標籤（例如「這位使用者流失了」）。要做出一次預測，模型需要完成三件事：

1. 理解每張表內的數值（column 與 row 的語意）
2. 關聯不同表之間的記錄
3. 將帶有已知標籤的上下文案例與待預測的實體相互對照

具體流程分三步：

- **自動上下文生成**：任務用 Predictive Query Language（PQL）這種宣告式介面描述，使用者只需說明「要預測什麼」而非「怎麼做」。對於有時間性的任務，模型會回放歷史資料庫狀態，在某個錨點時間之前取樣以實體為中心的子圖，並只用該時間點之前的資料推論，標籤則來自之後發生的事件，藉此避免資料洩漏。
- **表內推理**：一個輕量網路獨立處理每張表，交替進行 column attention（關聯同一欄位內的值）與 row attention（關聯同一行內的特徵），學習哪些欄位與記錄重要，過濾噪音。
- **跨表推理**：一個較大的網路透過 graph attention，沿著主鍵／外鍵關係把 row embedding 分散到整個關聯結構中，並與跨樣本的 cross-sample attention 交錯進行，這正是「把使用者檔案連結到交易歷史」這類關聯推理發生的地方。由於這一階段處理的是 row embedding 而非每個 cell，避免了平方級的運算成本，因此能擴展到大型上下文與更深的子圖。

📊 **41 個任務、15 個資料庫，贏過專家調校的梯度提升樹**

根據論文，Kumo Relational 是第一個在常見關聯式基準測試上，以 few-shot 方式超越監督式機器學習的基礎模型：

| 基準測試 | 對比對象 | 結果 |
|---|---|---|
| RelBench V1 分類任務 | 專家特徵工程 + 梯度提升樹（GBT） | 平均 AUROC 高出近 4 個百分點 |
| SAP SALT 企業基準 | 專家特徵工程 + XGBoost | 開箱即用高 7 個 MRR 百分點，微調後高 13 個百分點 |
| SAP SALT 企業基準 | AutoGluon ensemble | MRR 高出 8% |

它在 41 個任務、15 個資料庫上的測試中，整體超越了監督式關聯式深度學習模型與專家調校的 GBT pipeline，並宣稱可擴展到 500B+ 行規模的資料庫。

💡 **訓練資料全是合成的，為了涵蓋真實世界的多樣性**

由於多樣化的真實關聯式資料庫很少公開，Kumo Relational 的預訓練完全使用合成資料，模擬反映真實世界資料庫特性的多樣化預測查詢，訓練過程分階段進行，從單一表格逐步過渡到越來越複雜的關聯結構。其生成器延伸自 PluRel（Kothapalli et al., ICML 2026）的方法，Kumo 團隊成員也參與了 PluRel 論文的共同撰寫。PluRel 分三階段生成資料庫：先建立 schema，再生成會像真實資料一樣群聚的外鍵連結，最後透過帶有時間趨勢與跨表依賴的結構因果模型（Structural Causal Model）生成欄位數值。

🎯 **對工程師的啟示**

如果你的團隊正在維護一堆針對 churn、demand、fraud 的獨立 XGBoost pipeline，Kumo Relational 提供了另一條路：把「開發一個新預測」從一個專案縮短成一條查詢。它已透過開源的 GPU-native structured-data-models 函式庫或 NVIDIA NIM 提供，且設計上本就考慮讓 agent 透過 PQL 直接呼叫，值得在評估下一代預測基礎設施時納入比較。

🔗 **來源**
- 標題：NVIDIA Kumo Relational Outperforms Supervised Machine Learning on Relational Data, No Training Required
- 作者／機構：NVIDIA（Joshua Przybylko、Jure Leskovec、Matthias Fey 等）
- 連結：https://huggingface.co/blog/nvidia/kumo-relational

#NVIDIA #RelationalAI #FoundationModel #MachineLearning #InContextLearning #GraphAttention #EnterpriseAI #DataScience #XGBoost #PredictiveAnalytics
