---
title: 'Mitra-v2: Scaling synthetic pretraining for tabular foundation models'
source: Amazon Science
url: https://www.amazon.science/blog/mitra-v2-scaling-synthetic-pretraining-for-tabular-foundation-models
model: claude-code/sonnet
generated_at: '2026-11-11T23:38:45.746245'
score: 110
---

📌 【Amazon Science】Mitra-v2:純合成資料訓練的表格基礎模型升級版

TL;DR：Mitra-v2用更大、更多樣的合成表格重新預訓練,在TabArena上全面超越前代,權重與程式碼已開源。

表格資料是企業最常見卻最麻煩的機器學習素材:每換一張新表,就得重新選演算法、做特徵工程、調超參數、搭建處理流程。Amazon 去年推出的 Mitra,試圖用一個預訓練模型終結這個循環,但在大型、寬表格、多分類問題上後繼無力。這次推出的 Mitra-v2,正是針對這個瓶頸而來。

🤔 **表格基礎模型要解決的問題**

梯度提升決策樹(gradient-boosted decision trees)等標準工具,產出的模型只適用於特定的那張表。表格基礎模型的願景是:一個預訓練好的模型讀取一張從未見過的表格中已標註的資料列,就能直接預測其餘內容,中間不需要額外的訓練過程。Mitra 第一代驗證了這個方向在小、中型表格上可行,但在大表格、寬表格、類別數量多的問題上遇到容量限制。

🧩 **合成預訓練,規模加大、種類加多**

Mitra 系列模型完全不使用真實資料(更不用說客戶資料)進行預訓練,而是在數百萬個合成的預測問題上訓練,部署時則把真實表格中已標註的資料列當作範例,讓模型用 in-context learning 的方式去預測未標註的資料列。模型要學的是「欄位之間如何相互關聯」的一般性原則,而不是記住任何一份真實資料集的內容。

架構本身沒有變,仍是一個同時關注表格的「列」與「欄」的 Transformer。改變的是預訓練時所見範例的規模:Mitra-v2 所用的表格,列數是前代的 10 倍,欄數大約是 3 倍,讓模型實際見過企業真實使用的表格大小。團隊也加入一種新的合成表格生成方式——hybrid SCM prior,在單一因果圖中,每段因果關係可以是一個小型神經網路、決策樹、從 Gaussian process 取樣的平滑函數,或是具時間相依性的自回歸過程,讓單張合成表格就能同時涵蓋真實資料中常見的多種關係型態,並搭配新的 hybrid optimizer 讓這類更複雜的訓練保持穩定。

在部署階段,團隊加了兩個輕量化的擴充機制:面對極寬的表格,用 SVD(singular-value decomposition)把資料壓縮成符合模型容量限制、又能保留原始資料大部分變異量的合成表格;而 Mitra-v2 的輸出層僅有 10 個節點(對應 10 個類別),因此對類別數更多的任務,會把每個節點的輸出送進一個層級式樹結構做進一步分類。預設情況下,Mitra-v2 會針對每張新表格自動做簡短的微調,產生 8 份副本並把預測結果平均(即 bagging),因此嚴格來說它並非純粹的 zero-shot 模型,但換來的是更高的準確度。

📊 **TabArena與ScoringBench的成績**

在獨立學術團隊維護的公開基準 TabArena(涵蓋 51 個真實世界資料集,用類似棋類 Elo 的方式依固定一小時運算預算下的對戰結果排名)上,Mitra-v2 在單一模型類別中排名第一。在兩個模型都能原生執行的 33 個資料集中,Mitra-v2 在其中 32 個都勝過 Mitra-v1;而在全部 51 個資料集上,Mitra-v2 都能在一小時預算內完成,相比之下 Mitra-v1 有超過三分之一的資料集無法在時限內跑完。在涵蓋約 300 個資料集的 TALENT 基準上,Mitra-v2 同樣名列前段,在類別數超過 10 的分類任務上表現最強。在評估迴歸模型預測區間校準度的公開基準 ScoringBench 上,微調後的 Mitra-v2 排名第一。

⚠️ **並非純zero-shot,仍有微調開銷**

值得留意的是,Mitra-v2 預設會對每張新表格做自動微調並產生 8 份副本,這帶來一定的運算開銷,使用前應將這部分成本納入評估。

🎯 **實務啟示**

Mitra-v2 的分類與迴歸模型、推論與微調程式碼,已經以 Apache-2.0 授權開放在 Hugging Face 上,對需要處理結構化業務資料(例如客戶互動歷史、營運情境中的事件發生機率預測)的團隊,這代表少一次「為每張新表格重新設計 pipeline」的循環,可以直接拿預訓練模型試跑,再視情況決定是否要走微調路徑。

🔗 **來源**
- 標題：Mitra-v2: Scaling synthetic pretraining for tabular foundation models
- 作者／機構：Amazon
- 連結：https://www.amazon.science/blog/mitra-v2-scaling-synthetic-pretraining-for-tabular-foundation-models

#TabularML #FoundationModel #MachineLearning #AmazonScience #SyntheticData #InContextLearning #OpenSource #HuggingFace #DataScience #Mitra
