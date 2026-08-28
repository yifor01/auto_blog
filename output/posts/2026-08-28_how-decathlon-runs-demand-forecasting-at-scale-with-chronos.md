---
title: How Decathlon runs demand forecasting at scale with Chronos-2
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-decathlon-runs-demand-forecasting-at-scale-with-chronos-2/
model: claude-code/sonnet
generated_at: '2026-08-28T18:08:34.427995'
score: 83
---

📌 Decathlon 用 Chronos-2 重構需求預測:WAPE 降 11-15 個百分點

TL;DR:Decathlon 導入 Amazon 的時間序列基礎模型 Chronos-2 取代自建預測系統,準確度與維運效率同步提升。

一副滑雪手套和一塊衝浪板,需求訊號可以完全不同,但零售商得同時精準預測兩者的銷量,否則就是缺貨或囤貨。這正是 Decathlon 每週要面對的難題。

🤔 **上萬品項、多大陸、雙預測窗口的老問題**

Decathlon 是全球最大運動用品零售商之一,擁有超過 10 萬名員工與 4 億使用者,商品橫跨 80 多種運動項目。其預測系統每週針對兩個時間窗口運算:12 週的補貨窗口供採購人員向工業夥伴下單,以及 52 週的策略窗口用於長期庫存與產能規劃。系統部署在歐洲、印度、中國、東南亞、拉丁美洲等多個供應區域(即將擴及中東與非洲),每區最多涵蓋 2.5 萬項商品。在導入 Chronos-2 之前,Decathlon 的預測系統需要每週重新訓練,且擴展到新區域時額外的工程投入不小,團隊需要一套準確度更高、維運複雜度更低的方案。

🧩 **從零售實測到生產架構:LoRA 微調 + 原生 covariate 支援**

為了驗證時間序列基礎模型(TSFM)是否真的適用於自家零售資料,Decathlon 在自有資料上建立了大規模基準測試,同時評估多個 TSFM 的 zero-shot 與微調表現。結果顯示,微調後的 Chronos-2 在兩個預測窗口上都持續超越其他所有受測模型,即使是 zero-shot 模式也能追平甚至超越原本的生產基準線,微調則進一步把預測誤差再壓低數個百分點。

Chronos-2 是一個緊跟 T5 encoder 設計的純 encoder Transformer,提供 base(amazon/chronos-2,1.2 億參數)與 small(autogluon/chronos-2-small,2,800 萬參數)兩種規格。與初代 Chronos 把數值量化成離散 token 不同,Chronos-2 對每條序列做 robust scaling,再切成不重疊的 patch,透過殘差網路映射成連續嵌入,最終由 quantile head 輸出連續分位數預測。其架構核心創新是交替注意力機制:每個 Transformer block 在「時間注意力」(單一序列內的時間軸)與「群組注意力」(同一 patch 位置下、群組內多條序列之間)之間切換,讓相關序列與其 covariate 可以原生做多變量預測,而不像多數 TSFM 需要額外變通處理才能納入 covariate。

生產端的架構是:PySpark 資料準備管線組裝輸入時間序列,每 6 個月透過基於 AutoGluon 的微調工作以 LoRA(Low-Rank Adaptation)方式讓 Chronos-2 適應最新資料,並把結果模型註冊進 MLflow 模型註冊表;非微調週期則跳過此步驟。推論管線抓取最新註冊模型,以 Amazon EC2 執行每週批次推論(由 Databricks jobs 觸發),資料管線則透過 Airflow 在 Decathlon 既有資料平臺上編排。

📊 **12 週補貨窗口 WAPE 改善 11-15 個百分點**

相較於舊有的預測工具,Chronos-2 微調版本在兩個區域、兩個時間窗口上都帶來顯著準確度提升,12 週補貨窗口的 WAPE 改善幅度達 11-15 個百分點。新區域的部署時間也從原本的 6 個月縮短到 2-3 個月,因為只需針對當地歷史資料執行微調,不需重新設計架構。目前 Chronos-2 已在東南亞與拉丁美洲供應區域正式上線,前述數據正是取自這兩個區域。截至撰文時,Chronos-2 系列模型在 Hugging Face 上已被下載超過 1.2 億次,並可透過 AutoGluon-Cloud 或 Amazon SageMaker JumpStart 供 SageMaker AI 使用者使用。

🎯 **實務啟示**

對正在評估是否導入時間序列基礎模型的團隊,Decathlon 的經驗提供了一個務實的驗證路徑:先在自有資料上同時測 zero-shot 與微調表現,並拿現有生產基準線當對照組,而不是直接假設基礎模型一定更好。原生支援 covariate 的架構設計(如 Chronos-2 的群組注意力)可以省下大量針對 covariate 的工程變通,而 LoRA 微調搭配 MLflow 版本管理,則讓新區域擴展不必重新設計架構,直接壓縮上線時間。

🔗 **來源**
- 標題:How Decathlon runs demand forecasting at scale with Chronos-2
- 作者／機構:Vianney Bruned(與 Decathlon 的 Filippo Giruzzi、Belkiss Saidi、Carlos Ramirez 共同撰寫)/ AWS Machine Learning Blog
- 連結:https://aws.amazon.com/blogs/machine-learning/how-decathlon-runs-demand-forecasting-at-scale-with-chronos-2/

#TimeSeriesForecasting #Chronos2 #AWS #AutoGluon #RetailAI #DemandForecasting #LoRA #MLflow #FoundationModels #SupplyChain
