---
title: 'Mistral AI Releases Timestral: A 209M Forecasting Model Family That Outperforms
  Google’s TimesFM-3'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/18/mistral-timestral-time-series-foundation-model/
model: claude-code/sonnet
generated_at: '2026-10-19T21:43:44.773114'
score: 91
---

📌 【Mistral AI】209M 參數模型，CPU 就能做時序預測

TL;DR：Mistral 首款時序基礎模型 Timestral 開放權重，最大版本在多個 zero-shot 榜單排名第一，且不需要 GPU 推論。

多數時序預測工具要嘛像 ARIMA 得每條序列各自擬合，要嘛像 PatchTST 得針對每個資料集從頭訓練。Mistral AI 這次推出的 Timestral 想做的是另一件事：預訓練一次，直接 zero-shot 套用到沒看過的資料上，而且最大的模型也只有 209M 參數。

🧩 **預訓練一次，到處 zero-shot**

Timestral 是一個時序基礎模型（TSFM），在大量多樣的語料上預訓練後，可以直接對完全沒見過的資料做 zero-shot 預測，而不是像傳統深度模型那樣針對每個資料集重新訓練。它會對每個時間步輸出 21 個分位數（quantile），可以同時對多變量目標做聯合預測，並且能接受「只知道過去」「已知未來」以及類別型的 covariate。

架構上，Timestral 是一個因果（causal）、以 patch 為單位的 transformer，同時具備 time attention 與 variate attention。209M 版本使用 24 層、embedding 維度為 768，每個 patch 涵蓋 32 個時間步。單次前向傳遞可以預測最多 1,024 步；更長的預測長度則採取分段方式，把每一段的中位數結果回饋當作下一段的輸入繼續預測。

📊 **模型愈大不一定愈準，CPU 推論也夠快**

Mistral 釋出了 4 種規模的模型，從 5M 到 209M 參數。有趣的是，尺寸放大在頂端出現了平緩甚至打平的現象：Timestral-123M 在 GIFT-Eval 上的 MASE 為 0.659，209M 則是 0.658，差距幾乎可忽略。Mistral 團隊也提到，28M 模型在 GIFT-Eval 與 TIME 上的表現勝過 Chronos-2，而 Chronos-2 的參數量大約是它的 4 倍。

延遲方面，Mistral 團隊在一臺 8 執行緒的標準伺服器 CPU 上測試，任務是用 3 週的 15 分鐘頻率歷史資料預測未來 1 天：5M 模型耗時 10 毫秒，209M 模型耗時 140 毫秒，28M 模型的速度則是 209M 的 5 倍；而 123M 模型用 209M 約四分之三的延遲，就能拿到只差 0.2% 的分數。以上數字皆為單一 checkpoint、不經 ensemble 的 zero-shot 結果，來自 Timestral-209M 的 model card。文中也提到 Google 與 Amazon 並未在自家模型頁面公布對應數字，可供比較的 Chronos-2 數字則取自 Datadog 的 model card，Mistral 自己列出的對應數字是 0.642／0.539。

🧩 **安裝與取得權重**

安裝方式為 `pip install git+https://github.com/mistralai/timestral.git`，需要 Python 3.10 以上與 torch 2.4 以上，依賴套件包含 PyTorch、NumPy、safetensors 與 huggingface_hub。權重可從 Hugging Face 下載，分別是 5M 版 21MB、28M 版 111MB、123M 版 490MB。Mistral 的文件把 Timestral 1.0 209M 標示為 Public Preview，若要在私有資料上微調，可透過 Mistral Forge，部署方式支援 on-prem、VPC 或 air-gapped 環境。

⚠️ **目前仍是 Public Preview**

209M 版本官方標示仍處於 Public Preview 階段，意味著介面與效能數字未來可能還會調整。

🎯 **實務啟示**

對需要大量時序預測但沒有 GPU 資源的團隊（例如邊緣裝置、既有 CPU 伺服器叢集），Timestral 提供了一個可以直接下載權重、在 CPU 上跑出機率預測結果的選項，不必重新訓練模型。

🔗 **來源**
- 標題：Mistral AI Releases Timestral: A 209M Forecasting Model Family That Outperforms Google's TimesFM-3
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/18/mistral-timestral-time-series-foundation-model/

#MistralAI #TimeSeries #Forecasting #ZeroShot #FoundationModel #OpenWeights #MachineLearning #CPUInference #MASE #GIFTEval
