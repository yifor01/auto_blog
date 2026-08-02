---
title: 'End-to-End Forecasting with TimesFM 2.5: Backtesting, Covariates, Anomaly
  Detection, and Scalable Colab Deployment'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/01/end-to-end-forecasting-with-timesfm-2-5-backtesting-covariates-anomaly-detection-and-scalable-colab-deployment/
model: tencent/hy3:free
generated_at: '2026-08-02T08:04:15.228172'
score: 83
---

📌 【TimesFM 2.5 實作指南】從零建構端對端時間序列預測工作流

TL;DR：透過 TimesFM 2.5 實現包含回測、共變量整合與異常檢測的完整預測流程。

在處理真實世界的時間序列任務時，僅僅生成一個預測點值（Point Forecast）是遠遠不夠的。工程師需要的是能夠處理外部因素（如促銷、氣溫）、具備不確定性量化能力，且經過嚴謹回測驗證的穩健系統。

🧩 **建立包含多重因素的零售模擬數據集**

為了模擬真實場景，本教學展示了如何生成一個包含多個商店的零售數據集，其中融入了以下複雜變數：
- 趨勢（Trend）與季節性（Seasonality，包含週與年）
- 價格效應與促銷活動（Promotions）
- 節日影響與氣溫變化
- 隨機需求雜訊

🚀 **TimesFM 2.5 的 Zero-shot 預測與不確定性量化**

使用 TimesFM 2.5 模型進行 Zero-shot（零樣本）預測時，不僅能輸出預測值，還能透過機率分位數（Probabilistic Quantiles）生成扇形圖（Fan Chart），藉此視覺化預測的置信區間（Confidence Intervals），幫助評估預測的不確定性。

📊 **多維度的效能評估與回測機制**

為了確保模型在實務中可靠，教學中實作了多種評估指標與驗證策略：
- **評估指標**：包含 MAE、RMSE、MAPE、sMAPE、MASE、Pinball Loss 以及預測區間覆蓋率（Prediction-interval coverage）。
- **滾動原點回測（Rolling-origin Backtesting）**：不依賴單一的測試集，而是透過多個歷史時間點的切分，觀察模型在不同預測週期下的穩定表現。
- **消融研究（Ablation Study）**：測試不同的上下文長度（Context-length）對預測準確度與推論時間的影響。

💡 **整合外部資訊：透過 XReg 引入共變量**

單純依賴歷史數據往往不足以預測未來，教學展示了如何利用 TimesFM 的 XReg 功能整合外部資訊：
- **整合對象**：數值型、類別型及靜態共變量（如價格、氣溫、促銷、節日、星期、區域與商店資訊）。
- **融合模式**：比較了 `xreg + timesfm` 與 `timesfm + xreg` 兩種融合模式，以找出最適合的預測方式。

⚠️ **異常檢測與長時預測策略**

除了預測未來，模型還能轉化為監控工具：
- **異常檢測**：將觀測值與 TimesFM 預測的機率區間進行對比，並根據偏離程度賦予「警告（Warning）」或「嚴重（Critical）」等級。
- **長時預測策略**：對比「直接預測（Direct）」與「遞迴預測（Recursive）」兩種策略在長預測區間內的準確度與誤差累積差異。

🎯 **實務啟示：邁向生產級預測系統**

這套工作流為工程師提供了一個結構化的基礎，可用於需求預測、營運規劃與異常監控。透過測試模型對缺失值、極短歷史紀錄及正值限制（Positive-value clipping）的魯棒性（Robustness），確保模型在實際部署時能應對各種不穩定輸入。

🔗 **來源**
- 標題：End-to-End Forecasting with TimesFM 2.5: Backtesting, Covariates, Anomaly Detection, and Scalable Colab Deployment
- 作者／機構：Sana Hassan @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/01/end-to-end-forecasting-with-timesfm-2-5-backtesting-covariates-anomaly-detection-and-scalable-colab-deployment/

#TimesFM #TimeSeries #Forecasting #MachineLearning #DeepLearning #AnomalyDetection #RetailTech #ZeroShot #DataScience #Python
