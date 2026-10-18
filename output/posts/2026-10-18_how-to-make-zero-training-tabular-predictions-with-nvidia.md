---
title: How to Make Zero-Training Tabular Predictions with NVIDIA Structured Data Models
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/17/how-to-make-zero-training-tabular-predictions-with-nvidia-structured-data-models/
model: claude-code/sonnet
generated_at: '2026-10-18T19:34:17.424474'
score: 82
---

📌 【NVIDIA 開源工具實測】表格基礎模型免訓練預測，打得過 sklearn 嗎？

TL;DR：NVIDIA Structured Data Models 讓表格預測零訓練上手，但預設設定藏著好幾個坑。

你有沒有想過，面對一份全新的表格資料，不用 fit、不用調超參數，直接把標籤範例丟給模型就能預測？NVIDIA 最新發布的 Structured Data Models（SDM）正是把這個願景包成一支函式庫，而 MarkTechPost 的實測教學，不只跑出了數據，還挖出了預設行為悄悄出錯的幾個地方。

🤔 **一支 PyTorch 介面，背後是四個表格基礎模型**

SDM 把多個預訓練的表格基礎模型統一藏在同一個 PyTorch 介面之後，其中 TabICLv2 與 KumoTabular 處理單一表格，KumoRelational 則處理整個關聯式資料庫。三者都透過 in-context learning 運作：把一批已標記的列與要預測的列一起餵進模型，一次前向傳播就回傳機率或完整的預測分佈，沒有訓練步驟。函式庫同時列出每個模型的 checkpoint 大小與授權條款，其中 Google 的 TabFM 與 TimesFM 3 因為體積大且為非商用授權，被排除在這次實測之外。

安裝本身就是第一個坑：套件需從 GitHub 原始碼安裝（PyPI 上只是佔位版本），而關聯式取樣所需的 pyg-lib，其官方 ImportError 訊息會用「完整 patch 版本」組出下載連結（例如 torch-2.14.1+cpu），但 pyg-lib 的 wheel 實際是按「主版本.次版本」發佈的，照著錯誤訊息走會連到一個空頁面，必須自己用主版本與次版本組出正確的索引網址。

🧩 **TableTensor：把每種資料型態分開放**

函式庫的核心是 TableTensor，一個 PyTorch tensor 子類別，依語意型態（numerical、categorical、datetime、text、id）各自保存一個區塊，由 infer_stypes 自動判斷型態。但預設判斷在真實的客服工單資料上出了包：自由文字欄位被誤判成四百個類別值的 categorical，而工單編號被當成數值，兩者都會被當成特徵送進模型；傳入 text 與 id 的型態推斷旗標才能修正。資料轉回 pandas 時數值全部保留，但 dtype 會變：數字一律變成 float32，可為 null 的整數變成帶 NaN 的浮點數，類別字串變成 pandas category。另外，時間戳在底層以整數微秒儲存，Arrow 遇到會丟失精度的轉換（例如含奈秒位數的欄位）會直接拒絕整欄轉換，實測前得先把時間戳向下取整到微秒。

📊 **零訓練 vs. 訓練過的 baseline，差距有多大**

在乳癌資料集（300 列標記、269 列待測）上：

| 模型 | Accuracy | AUC |
|---|---|---|
| TabICLv2（零訓練） | 0.970 | 0.996 |
| KumoTabular（零訓練） | 0.970 | 0.995 |
| Logistic Regression（訓練過） | 0.970 | 0.993 |
| Gradient Boosting（訓練過） | 0.967 | 0.992 |

迴歸任務上，diabetes 資料集（300 列標記）同樣沒有輸出單一數值，而是回傳 999 個分位數構成的完整預測分佈：

| 模型 | RMSE |
|---|---|
| TabICLv2（分佈中位數） | 53.6 |
| RidgeCV（訓練過） | 54.3 |
| Gradient Boosting（訓練過） | 64.7 |

更值得注意的是校準度：10–90 百分位區間實際覆蓋 81.0% 的測試目標（名義值 80%），5–95 百分位區間覆蓋 91.5%（名義值 90%），而 50% 區間則偏窄，只覆蓋 43.7%。在二十分類的合成資料上（每類 30 列標記），TabICLv2 透過錯誤校正輸出碼把問題拆成多個子問題再合併，達到 0.760 準確率，優於同樣資料訓練的 Gradient Boosting（0.615）。另外，若同一批標記資料要回答多批查詢，呼叫 fit 把上下文編碼快取起來，再用 predict 跑查詢列，實測在 CPU 上比每次重新編碼快上數倍。

💡 **預設前處理會悄悄丟掉時間與文字特徵**

前處理由一組可組合的 Recipe 處理器構成，TabICLv2 的預設 Recipe 只針對 categorical 與 numerical 欄位分支，時間戳與文字欄位完全不會變成特徵。在一份工單升級與開單時間、退款等字詞相關的資料上，預設 Recipe 的 AUC 只有 0.525，幾乎等於隨機猜。函式庫確實會丟出 RuntimeWarning 說明哪些欄位被忽略，但這個警告只在程序裡第一次觸發後就被壓制，後續同一個程序裡的所有模型都會悄悄沿用同樣的省略，不會再提醒。加上 AddCalendarFields（把時間戳轉成週期性的小時、星期特徵）可將 AUC 拉到 0.634，再加上 TFIDF（處理文字留言）可進一步拉到 0.789。

函式庫附的 GradientExplainer 也有兩個陷阱：其輸出函式每個 estimator 各呼叫一次並覆寫前一次結果，若只在第一次呼叫時生效，多個 estimator 情況下解釋結果只會反映最後一個 estimator；另外每個 estimator 的類別順序因預設 Recipe 對標籤做了隨機洗牌而互不相同，若用欄位「位置」挑選目標類別的機率，部分種子下特徵符號會整個翻轉，改用欄位「名稱」挑選才能在所有種子下得到正確符號，跨種子平均後才能準確還原出真正有效的特徵。

⚠️ **目前只在 CPU 上驗證，關聯式資料庫功能仍待展開**

本次實測全程在 CPU 上執行，且刻意跳過體積大、授權非商用的 Google 模型。KumoRelational 處理整個關聯式資料庫而非單一表格，相關細節（包括教學提到「區分誠實關聯模型與洩漏模型的那一個參數」）需要進一步閱讀完整程式碼才能確認。

🎯 **實務啟示**

把表格基礎模型當作「免訓練的快速基準」很有吸引力，但預設行為不會主動告訴你它悄悄丟了時間或文字欄位；務必檢查 infer_stypes 的判斷結果，必要時手動加上日曆與文字前處理器，並在使用解釋器時一律用欄位名稱而非位置索引。

🔗 **來源**
- 標題：How to Make Zero-Training Tabular Predictions with NVIDIA Structured Data Models
- 作者／機構：Sana Hassan, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/17/how-to-make-zero-training-tabular-predictions-with-nvidia-structured-data-models/

#NVIDIA #TabularML #InContextLearning #MachineLearning #PyTorch #FoundationModels #DataScience #AIEngineering #TabICL #OpenSource
