---
title: 'Prior Labs Releases TabPFN-3.5: A Tabular Foundation Model That Beats the
  Winning Otto Kaggle Solution With Default Settings'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/15/prior-labs-releases-tabpfn-3-5-a-tabular-foundation-model-that-beats-the-winning-otto-kaggle-solution-with-default-settings/
model: claude-code/sonnet
generated_at: '2026-09-16T20:15:39.941181'
score: 102
---

📌 免調參打敗十年Kaggle冠軍：TabPFN-3.5的表格基礎模型野心

TL;DR：不用訓練、不用調參，TabPFN-3.5用預設設定贏過2015年Kaggle冠軍解法。

2015年那場Otto Group產品分類賽，3,505支隊伍搶10,000美元獎金，冠軍是兩位曾登上Kaggle grandmaster世界第一的高手，用36個模型疊出的複雜stacking方案。十一年後，一個從沒看過這份資料、只靠合成資料預訓練的模型，用預設設定、一分鐘內就把成績刷過了冠軍。

🤔 **AutoGluon追了六年，最後一哩路最難**

Otto Group Product Classification Challenge要求參賽者用93個經過模糊化處理的計數特徵，把商品分到9個類別，以multi-class log loss評分（越低越好）。冠軍Gilberto Titericz與Stanislav Semenov的方案是基於手工特徵的36模型多層stack。AutoGluon共同創辦人、現任Prior Labs研究員Nick Erickson多年來持續追蹤這個分數：AutoGluon在2020年論文中排名第23，2023年的1.0版衝到第14，2026年8月的1.6版來到第9。但最後一段路特別硬，從排名50到排名10，log loss只從0.41降到0.40；但從排名10要追到冠軍的0.382，還得再降0.018，幾乎是前段的兩倍努力。

🧩 **一次前向傳播，沒有per-dataset訓練**

Prior Labs推出的TabPFN-3.5是一款表格基礎模型（tabular foundation model），核心特色是直接對一張表做forward pass進行預測，不需要針對個別資料集做訓練或調參。根據Erickson的說法，TabPFN-3.5在Otto資料集上是用原始資料、預設設定跑出來的，在一臺RTX PRO 6000 GPU上僅花約一分鐘。這個模型只用合成資料預訓練，從未見過Otto或任何Kaggle資料集。相關的可重現Kaggle notebook已公開。

📊 **私有排行榜0.375，七項benchmark第一**

TabPFN-3.5在Otto私有排行榜上跑出0.375，優於冠軍的0.382。技術報告則指出它在TabArena、BeyondArena、STRABLE、MulTaBench、RelArena-α、TALENT、ScoringBench共七項benchmark拿下第一，不過拿冠軍的並非總是基礎模型本身：TabPFN-3.5-Thinking在TabArena、BeyondArena、STRABLE、MulTaBench四項稱王，而一個內部的TabPFN-Rel harness預覽版則拿下RelArena-α。

在涵蓋51個資料集的TabArena上，Thinking版Elo達1910，基礎模型1866，領先TabFM+的1823。Prior Labs表示基礎模型以130 Elo的差距、五分之一的時間打敗AutoGluon 1.6 extreme。在涵蓋142個資料集、包含分組、時間序列、寬表、文字密集與高基數資料的BeyondArena上，TabPFN-3.5比先前總排行榜第一名高出約150 Elo，但在分組、時間序列與大資料量的子集上，經過調參與ensemble的MLP仍然領先。

⚠️ **KV cache沒漲，但大訓練集反而變慢**

儘管參數量約為TabPFN-3的四倍，KV cache大小卻大致維持不變，快取後的單筆預測速度也與TabPFN-3相當；但在大訓練集情境下，基礎模型的運算速度最多會比TabPFN-3慢兩倍。此外，開放權重版本可在本機執行，適用於研究、評估與Kaggle，但正式生產環境需要透過Prior Labs的API或取得商業授權。

🎯 **實務啟示**

對於需要快速在表格資料上取得基準成績的工程師，TabPFN-3.5提供了一個「先跑一次forward pass」再決定是否需要客製化pipeline的新起點，尤其適合原型驗證與資料探索階段；但涉及大規模訓練資料或生產部署時，仍需評估授權條件與推論速度的實際權衡。

🔗 **來源**
- 標題：Prior Labs Releases TabPFN-3.5: A Tabular Foundation Model That Beats the Winning Otto Kaggle Solution With Default Settings
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/15/prior-labs-releases-tabpfn-3-5-a-tabular-foundation-model-that-beats-the-winning-otto-kaggle-solution-with-default-settings/

#TabPFN #TabularML #FoundationModel #Kaggle #AutoML #MachineLearning #DataScience #AutoGluon #PriorLabs #Benchmark
