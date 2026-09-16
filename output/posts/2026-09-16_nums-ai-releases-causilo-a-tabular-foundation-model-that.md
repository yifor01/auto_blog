---
title: 'Nums AI Releases Causilo: A Tabular Foundation Model That Tops TabArena Among
  Single Models'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/15/nums-ai-releases-causilo-a-tabular-foundation-model-that-tops-tabarena-among-single-models/
model: claude-code/sonnet
generated_at: '2026-09-16T20:24:33.398577'
score: 86
---

📌 表格基礎模型 Causilo：免訓練、單次前向傳播登頂 TabArena

TL;DR：Nums AI 釋出可直接呼叫的表格基礎模型 Causilo，程式碼與權重全開放，在 TabArena 單模型排名中拿下最高 Elo。

分類與迴歸任務長期以來的痛點是「每換一個資料集就要重新訓練一個模型」。Causilo 想解決的正是這件事：呼叫 `fit` 不會更新任何預訓練權重，而是把訓練資料整批當成 context，預測查詢資料時只需一次前向傳播完成。

🤔 為什麼要用 in-context learning 做表格任務

Causilo 是一個預訓練好的 tabular foundation model，提供 scikit-learn 相容介面，程式碼採 Apache-2.0 授權，權重公開在 Hugging Face。輸入可以是 NumPy array 或 pandas DataFrame，支援類別特徵與缺失值，分類最多支援 10 個類別，迴歸預設回傳平均值，1.0.1 版新增中位數與分位數輸出，基於 999 個原生分位點運算。根據其 TabArena 提交說明，Nums AI 只用合成資料預訓練 Causilo，訓練過程並未使用任何 TabArena 的資料集。

🧩 三階段架構：refinement、compression、in-context learning

Nums AI 公開的程式碼與設定檔顯示了架構的具體設計：

- 特徵先以每三個一組進行分組，每個數值用 16 個學習到的 sine/cosine 頻率做 embedding，缺失值則有自己專屬的學習向量。
- 兩個 column stage 各自負責摘要一個特徵組：128 個 latent slot 只讀取訓練列的資料，並把摘要結果傳給該組內的每一列。
- 兩個 column stage 之間夾著一個 row stage，讓不同特徵組能透過 4 個 latent token 互相交流，這裡用的是 cross-attention 而非完整的 self-attention，Nums AI 表示這讓運算成本能與特徵數量維持線性關係。
- 一個 pooling block 接著把每一列壓縮成固定的 512 維向量。
- 標籤被加到訓練列上，由一個 12 層的 prediction block 讓查詢列去 attend 這些已標籤的訓練列；查詢列彼此之間、以及對訓練 context，都不會互相修改。
- 預設會啟用 8 個共享權重的 ensemble 成員，各自依序套用 none、rank2gaussian、robust 或 power 這幾種正規化方式，並搭配種子化的特徵與類別排列組合。

📊 在 TabArena 與 ScoringBench 上的成績

Nums AI 使用官方 TabArena pipeline 進行評測：51 個資料集、816 組 Full splits、8 個 estimator、seed 固定為 42，最終 Elo 為 1794，且有一位 TabArena maintainer 重新跑過整套評估，得到相同結果。同場比較對象包括 Google Research 的 TabFM、LG AI Research 的 EXAONE Tabular，以及 Prior Labs 的 TabPFN-3（overall 1636.2）。

在另一個評測 ScoringBench 上，Nums AI 提交了 Causilo 1.0.1 在 101 個資料集、每個做 5 折交叉驗證、樣本數上限 3,000 的結果，該評測使用 CRPS 等 proper scoring rule，並輔以 RMSE、R² 一併檢視。Nums AI 表示 Causilo 在 CRPS、R²、RMSE 三項指標上都排名第一，結果同樣經過 ScoringBench maintainer 獨立查核。

在一張 H100 80GB GPU、搭配 8 顆 CPU 核心的環境下，Nums AI 另外重跑了三個模型做速度比較，Causilo 在 fit 與 predict 階段都是最快的，但 TabPFN-3 使用的 GPU 記憶體遠低於它。若開啟 `use_kv_cache=True`，可以把 context 相關運算提前搬到 fit 階段執行，用較多的記憶體換取後續重複預測時的速度。

⚠️ 授權與部署限制

目前 Causilo 只開放研究與評估用途，可在 CUDA 或 CPU 上執行；若要商用、正式上線或做成 hosted API，需要另外向 Nums AI 取得授權。執行環境需要 Python 3.10 到 3.12，以及 PyTorch 2.13 以上版本，首次呼叫 `fit` 時會自動下載 checkpoint，也可以先透過 Hugging Face 上的 demo Space 試用。

🎯 實務啟示

對常需要處理表格資料建模的工程師來說，Causilo 提供了一條不用重新訓練、直接把資料丟進 context 就能推論的路徑，適合先在研究與評估階段用開放的程式碼與權重跑跑看，若要導入正式環境，記得先確認授權條款是否符合需求。

🔗 來源
- 標題：Nums AI Releases Causilo: A Tabular Foundation Model That Tops TabArena Among Single Models
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/15/nums-ai-releases-causilo-a-tabular-foundation-model-that-tops-tabarena-among-single-models/

#TabularML #FoundationModel #InContextLearning #MachineLearning #TabArena #OpenSource #ScikitLearn #DataScience #DeepLearning #NumsAI
