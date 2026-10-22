---
title: Ensemble forecasting with IBM Granite time-series models
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1
model: claude-code/sonnet
generated_at: '2026-10-22T21:01:34.687130'
score: 84
---

📌 不用重新訓練：IBM Granite 用四模型集成做時序預測

TL;DR：IBM Granite Timeseries Ensemble 用四個預訓練模型做零訓練集成預測，GIFT-Eval 排名優於任一單一模型。

時序預測最麻煩的地方往往不是訓練模型，而是挑模型，擅長處理平滑工業訊號的模型，換成雜訊很大的零售需求資料可能就失準。IBM Research 這次給的答案很直接：不挑了，四個都用上。

🤔 **把選模型的難題變成一個預設值**

HuggingFace Blog 文章指出，預訓練的時序模型可以在不針對你的資料集訓練的情況下直接做預測，但使用者仍然得選擇用哪一個模型，而最佳選擇取決於資料序列與任務本身。Granite Timeseries Ensemble 把這個選擇問題簡化成一個「合理的預設值」：一套 recipe 組合四種互補的 Granite 架構，回傳中位數與分位數（quantile）預測，不需要重新訓練，也沒有要擬合的集成權重。文章把這個想法類比氣象預報，像北美多模式集成（North American Multi-Model Ensemble）那樣，把不同模型對未來的不同看法合併成一個預測。

🧩 **四個成員模型與使用方式**

預設 recipe 結合了四個架構不同的 Granite 模型：

| 模型 | 架構 |
|---|---|
| Granite PatchTST-FM-r1 | Patched Transformer |
| Granite PatchTST-FM-r2 | Patched Conformer |
| Granite FlowState-r1.1 | State-space model |
| Granite TTM-r3 | Tiny Time Mixers（MLP mixer）|

文章說明，這些架構用不同方式捕捉趨勢、季節性與局部變化，因此各自的誤差不必然重疊。安裝方式是 `pip install "granite-tsfm>=0.3.11"`，接著用 `QuantileEnsembleForecaster.from_pretrained("ibm-granite/granite-timeseries-ensemble-r1")` 載入，呼叫時傳入資料、timestamp 欄位、目標欄位、context length 與 prediction length，就能同時取得 `result.prediction_outputs`（點預測）與 `result.quantile_outputs`（預設涵蓋 0.1 到 0.9 的分位數，例如 0.1 與 0.9 分位數可以組成名義涵蓋率 80% 的預測區間）。文章提醒，recipe 儲存的是集成設定而非合併後的權重，第一次執行時會即時下載四個成員模型的 checkpoint，因此需要額外時間。

🧩 **兩種合併方式怎麼選**

Probabilistic Ensemble（均勻機率池化）是推薦的預設做法，每個成員擁有相同影響力，在機率空間中把各自的分位數預測池化，再從合併後的結果中取出需要的分位數；因為權重固定，不需要擬合步驟，也沒有需要針對新序列調整的超參數。文章引用一篇橫跨 50 年的預測組合文獻回顧指出，等權重的簡單組合在點預測上經常不輸給估計權重的方法。IQR Ensemble 則依據各成員的預測區間寬窄動態加權，區間越窄的成員影響力越大，透過最接近 25、75 百分位的分位數估計四分位距（IQR），且權重會依樣本、目標與預測步數而變化；它額外提供溫度（temperature）參數（數值越高權重越趨向均勻）與單一成員權重上限可供調整，並用 isotonic regression 避免分位數交叉。文章也提醒，區間較窄不代表預測更準或校準更好，IQR 加權有可能偏向一個過度自信的成員。要切換成 IQR 版本，只需要把 `subfolder` 改成 `"recipes/granite-iqr"`。

📊 **97 組資料集的評比結果**

文章在 GIFT-Eval 的 97 組資料集設定上評估了兩種 recipe，模型皆未針對測試目標微調或挑選集成方法，結果以 2026 年 10 月 20 日公開排行榜數據為準：

| 預測方式 | MASE ↓ | MASE 排名 ↓ | CRPS/MWQL ↓ | CRPS 排名 ↓ |
|---|---|---|---|---|
| Granite Ensemble R1 — Prob | 0.683（最佳） | 47.175（最佳） | 0.471 | 50.948 |
| Granite Ensemble R1 — IQR | 0.684 | 48.773 | 0.471 | 47.619（最佳） |
| Granite PatchTST-FM-r2 | 0.685 | 51.371 | 0.467（最佳） | 48.918 |
| Granite FlowState-r1.1 | 0.701 | 66.474 | 0.490 | 69.485 |
| Granite PatchTST-FM-r1 | 0.717 | 74.794 | 0.488 | 68.134 |
| Granite TTM-r3 | 0.724 | 83.062 | 0.520 | 88.959（最佳） |

兩種集成方式在整體 MASE 與平均 MASE 排名上都優於四個單一成員模型；Probabilistic Ensemble 在這六種預測方式中取得最低的 MASE（0.683，優於第二名 PatchTST-FM-r2 的 0.685）。文章也提醒，排名欄位是跟完整的 GIFT-Eval 參考排行榜比較後的平均排名，並非只在這六者之間比較，因此數值會隨排行榜新增項目而變動。

🎯 **實務啟示**

如果你正在挑時序預測模型卻不想一個個 benchmark，Probabilistic Ensemble 提供了一個不用訓練、不用調參、直接可用的起點；若你的應用在意預測區間的不確定性表現，再拿 IQR Ensemble 跟它比較看看。整套 recipe 和預設的四個 Granite 模型都是寬鬆授權，對於需要快速落地預測功能、但沒有餘裕做大規模模型選型的團隊，是一個低成本的起手式。

🔗 **來源**
- 標題：Ensemble forecasting with IBM Granite time-series models
- 作者／機構：IBM Research（Fearghal O'Donncha 等）
- 連結：https://huggingface.co/blog/ibm-research/granite-timeseries-ensemble-r1

#TimeSeries #Forecasting #IBMGranite #EnsembleLearning #OpenSource #HuggingFace #MachineLearning #DataScience #MLOps #ProbabilisticForecasting
