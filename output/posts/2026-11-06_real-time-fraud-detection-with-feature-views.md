---
title: Real-time fraud detection with Feature Views
source: Databricks
url: https://www.databricks.com/blog/real-time-fraud-detection-feature-views
model: claude-code/sonnet
generated_at: '2026-11-06T22:32:54.338650'
score: 76
---

📌 從Kafka到風控分數：Databricks Feature Views終結訓練推理不一致

TL;DR：一份Feature定義同時產出訓練資料與即時推論管線，避免兩套邏輯各自飄移。

兩位客戶月均消費都是300美元，但一位標準差100美元、一位600美元。同樣一筆900美元的付款，對其中一人是六個標準差的異常，對另一人只是略高於平均一個標準差。這正是即時反欺詐系統必須在幾秒內判斷清楚的難題。

🤔 **訓練與推論各走一套邏輯，差異會悄悄侵蝕模型品質**

即時反欺詐仰賴三種特徵：客戶幾秒前做了什麼、客戶平常怎麼消費、當前交易與過去相比是否異常。訓練階段只能使用交易當下存在的資訊（point-in-time correct），推論階段卻要在交易發生後幾秒內更新這些特徵。若訓練與推論各自維護一套邏輯，兩者之間的細微差異就會造成data leakage與training-serving skew，悄悄侵蝕模型品質。approving一筆欺詐交易會讓客戶損失金錢，攔截一筆正常交易則會打斷付款體驗、侵蝕客戶對平臺的信任。

🧩 **一份定義，兩條管線：Feature View的設計**

Feature View是Databricks Feature Store裡的一個定義，描述特徵的來源（source）、實體鍵（entity keys）、時間語意與轉換邏輯。同一份定義會計算出歷史數值供訓練使用，也會驅動受管理的管線讓特徵在上線推論時保持最新。一套API同時涵蓋batch、streaming與on-demand特徵，並由Unity Catalog統一管理其定義、權限與lineage（來源追蹤）。

架構上分成兩條路徑，皆從Unity Catalog中的同一份特徵定義出發：歷史路徑讀取Stream的ingestion table，建立point-in-time訓練集；線上路徑則將彙總結果materialize到Online Feature Store，供Model Serving在請求時讀取。

文章用一筆900美元的付款，示範交易如何從Kafka stream一路流到Model Serving吐出的風險分數：

- 客戶交易事件以Kafka streams抵達，一個註冊過的Stream保存連線、schema與ingestion設定，StreamSource再參照它來計算即時特徵。因為Kafka topic保留不了足夠的歷史資料，Databricks會維護一份ingestion table作為stream的離線副本：訓練或回填online store時用ingestion table算歷史值，最新資料則直接讀Kafka feed。
- 用RollingWindow定義「過去五分鐘交易次數」這類短窗特徵，十分鐘總額則用相同的source與keys，搭配Sum與十分鐘的RollingWindow。
- SawtoothWindow用於長回顧期的彙總，其最舊邊界以天為單位往前推進，結合批次計算的歷史與串流更新的近況，為這筆900美元付款補上30天消費基準線。因為最舊邊界是以天推進而非連續推進，實際回顧期會略長於30天。基準線使用內建的Avg、StddevPop與Count聚合函式計算payment amount。
- 若需要Stream建立之前的歷史資料，StreamBackfillSource可以在建立Stream時提供自訂歷史，讓新的Sawtooth特徵一上線就能使用，不必等30天資料累積。
- amount_deviation這類on-demand特徵在請求當下計算，結合請求中的即時數值與已儲存的特徵。推論時的資訊用RequestSource表示（此例為請求中的transaction_amount），再搭配一個註冊在Unity Catalog的Python UDF，計算(current_amount - average) / standard_deviation。當沒有足夠可用歷史時，函式回傳0作為fallback，並用一個獨立指標區分「真正的0」與「fallback造成的0」。

💡 **同一個特徵定義，訓練與推論各吃一種輸入**

這套設計的核心價值在於，同一個衍生特徵在訓練時用歷史輸入評估，在推論時則用當前請求加上查詢到的統計值評估，邏輯只寫一次。開發階段可以用notebook裡的compute_features()檢視特徵在歷史資料上的數值，但對於像amount_deviation這種依賴請求欄位的特徵，要改用create_training_set()從標註樣本提供當下的付款欄位。團隊也可以在部署前，用歷史交易比較不同時間窗（例如五分鐘與15分鐘的交易次數）或不同基準線（平均值 vs. 加入標準差）哪個訊號更強。

⚠️ **時間語意的細節陷阱**

Sawtooth window的實際回顧期會因為「最舊邊界以天推進」而略長於設定值30天，是需要留意的時間語意細節；on-demand特徵在歷史不足時以0 fallback，仰賴額外指標避免誤判，顯示系統仍需要額外設計才能完整處理冷啟動情境。

🎯 **實務啟示**

對正在打造即時風控或任何需要「即時特徵＋歷史訓練」場景的工程團隊而言，這個案例示範了用單一特徵定義驅動兩條路徑，是避免training-serving skew的務實做法，值得在自家feature platform設計時參考這套source／entity keys／time semantics三段式定義方式。

🔗 **來源**
- 標題：Real-time fraud detection with Feature Views
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/real-time-fraud-detection-feature-views

#Databricks #FeatureStore #FraudDetection #MachineLearning #MLOps #RealTimeML #DataEngineering #Kafka #ModelServing #UnityCatalog
