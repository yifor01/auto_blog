---
title: How Jumio built a real-time feature store on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-jumio-built-a-real-time-feature-store-on-aws/
model: claude-code/sonnet
generated_at: '2026-08-19T06:43:22.393772'
score: 78
---

📌 P50 讀取 8.44ms：Jumio 用 AWS 打造即時 Feature Store，年省約 12 萬美元

TL;DR：身分驗證商 Jumio 用 SageMaker Feature Store + Flink 打造串流優先的即時特徵平臺，P95 延遲 16.9ms。

詐欺偵測模型要即時判斷一筆交易可不可疑，卻要等特徵計算跑完才能推論，這中間的每一毫秒都是可利用的視窗。身分驗證服務商 Jumio 在建置集中式即時 Feature Store 之前，各團隊各自定義特徵，部署仰賴人工，一次上線流程要花上數週。

🤔 背景：特徵重複定義、部署靠人工、延遲難控管

Jumio 的機器學習模型高度仰賴特徵才能做出即時判斷，但在建置真正的即時 Feature Store 之前，公司面臨資料重複、特徵工程分散、特徵一致性難以維持、部署仰賴人工、延遲不可控等問題。因為 Jumio 的核心業務是身分驗證，及時且準確的詐欺偵測是不能妥協的需求。

🧩 架構：串流優先設計，即時與離線兩條路徑並行

Jumio 的 Feature Store 架構部署在三個 AWS 區域：美國東部（維吉尼亞北部，us-east-1）、歐洲（法蘭克福，eu-central-1）、亞太（新加坡，ap-southeast-1）。整體資料流分成即時與離線兩條並行路徑：

即時路徑：事件透過 Amazon Kinesis Data Streams 進來，由跑在 Amazon Managed Service for Apache Flink 上的 Flink 應用即時處理與加工，再把特徵直接寫入 Amazon SageMaker Feature Store。

離線路徑：事件透過 Amazon Data Firehose 送進 Amazon S3，S3 事件通知觸發 Amazon EMR 執行較重的轉換工作，處理完的特徵一方面回寫進 SageMaker Feature Store 當作冷資料，另一方面寫入 Apache Iceberg 表，作為離線特徵儲存與模型訓練資料來源。

監控上，Jumio 針對即時特徵儲存追蹤 Flink 各階段的紀錄建立延遲、Flink 應用程式本身的運行健康度、SageMaker Feature Store 的效能與可靠性指標，以及 Amazon Data Firehose 的關鍵指標，防止特徵儲存悄悄劣化而污染模型預測結果。

📊 數據：P95 延遲 16.9ms，一年省下約 12 萬美元

這套架構的延遲表現達到 Jumio 詐欺偵測 SLA 要求的 sub-100ms：95 百分位回應時間為 16.9 毫秒。細看讀寫延遲，讀取延遲 P50 為 8.44 毫秒，寫入延遲 P50 為 18.6 毫秒。

在成本面，透過善用 SageMaker Feature Store 的記憶體內儲存（in-memory store），相較於過去分散的特徵儲存方案，Jumio 估計每年節省約 12 萬美元的營運成本。此外，新架構具備處理遲到事件（late-arriving events）的能力，並把過去分散在各團隊、需要人工實作、耗時數週的部署流程，改為集中化且自動化。

💡 深入分析：五個原則構成一套「架構得住」的 Feature Store

Jumio 團隊把實戰經驗歸納成五項原則：串流優先設計讓特徵能即時提供給模型；集中化的特徵定義維持跨團隊的一致性與可重用性；分層儲存策略（記憶體內儲存搭配標準儲存）在延遲與成本間取得平衡；持續監控特徵儲存的健康度與延遲，避免悄悄劣化污染模型預測；貫穿這一切的，是後端、機器學習、資料工程團隊之間的跨職能協作，讓特徵開發從發想到上線不被交接卡住。

🎯 實務啟示

如果你的團隊也在為 sub-100ms 的即時推論場景煩惱特徵一致性與部署效率，Jumio 這套「Kinesis + Flink 寫即時、Firehose + EMR 寫離線，兩邊都收斂到同一個 Feature Store」的模式，是經過生產環境驗證、可直接參考的分工方式，尤其是記憶體內儲存搭配標準儲存的分層策略，值得在設計階段就納入考量而非事後補救。

🔗 來源
- 標題：How Jumio built a real-time feature store on AWS
- 作者／機構：Amit Peshwani，AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/how-jumio-built-a-real-time-feature-store-on-aws/

#AWS #MachineLearning #FeatureStore #SageMaker #ApacheFlink #RealTimeML #FraudDetection #StreamProcessing #MLOps #DataEngineering
