---
title: 'Adaption Labs Introduces ‘Invent a Dataset’: Training Data Generated From
  a Task Description, Not a Seed Corpus'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/04/datasets-invent-api-training-data-without-labeling-adaptive-data-autoscientist/
model: claude-code/sonnet
generated_at: '2026-09-05T19:19:29.272111'
score: 73
---

📌 免種子語料：Adaption Labs 讓你用一句話生成訓練資料

TL;DR：Adaption Labs 推出 Invent a Dataset，僅憑任務描述就能生成可直接訓練的資料集，省去種子語料與人工標註流程。

多數資料工作流的起點，是你手上已經有一堆資料，然後花數週去標註、篩選、重塑，讓它盡量貼近你想要的任務。Adaption Labs 這次的主張是反過來：連那堆原始資料都不需要，直接從「你想讓模型學會的行為描述」出發。

🤔 **問題出在哪：現有資料撐不起想要的行為**

Adaption 團隊指出，這種「先有資料再湊任務」的做法，會把模型品質的天花板鎖死在「現有資料跟目標行為有多接近」。對於專屬且高度特化的任務，真正有用的訊號通常散落在內部系統、非結構化文字或工作流日誌裡，很難乾淨地轉換成聚焦的訓練集。團隊也特別區分自己與既有合成資料工具的差異：現有工具是在人類已經定義好 schema、任務分佈與生成策略之後，才自動化生成資料；而 Invent a Dataset 從更早一層開始，直接從「行為」本身出發。

🧩 **API 怎麼用：domain code、輸出格式與成本估算**

Invent a Dataset 現已在 Adaption app、Python SDK 與 REST API 上線，生成的資料可下載為 JSONL、JSON、CSV 或 Parquet，是你可以帶走、在任何地方訓練的檔案。不過生成過程本身跑在 Adaption 的託管平臺上並消耗 credits，文件中沒有提到自架生成的路徑。

核心操作流程：
1. 呼叫 `datasets.invent` 建立資料集並啟動生成，立即回傳狀態 `running`。
2. 輪詢 `datasets.get`，直到狀態變成 `succeeded` 或 `failed`，再下載資料列。
3. 用 `datasets.invent_domains` 動態取得目前可用的 domain code（不要寫死），例如傳入 `medical`，也可以用更細的 subdomain code 如 `medical.symptoms_diagnosis` 進一步縮小範圍；至少要指定一個 domain 或 subdomain，也可以同時傳多個 domain 到同一次生成。若 domain 沒有指定 subdomain，就會從整個範圍取樣。

輸出格式有兩種：`instruction_dataset`（預設，產出 prompt-completion 配對，用於 SFT）與 `preference_pairs`（產出 chosen／rejected 配對，用於 DPO 這類 preference-based 訓練）。

三個關鍵參數：`estimate=True` 可以在不真正建立與扣款的情況下，精確估算這次請求需要的 credits 與目前可用額度；`prompt` 最多接受一萬字元，用來引導生成內容的方向；`idempotency_key` 最多 255 字元，讓網路重試變安全，重複呼叫會回傳原本的資料集而不是重新啟動一次生成。資料列數量則受你方案的單次上限限制。

另外還有 `language_expansion` 機制，分兩種模式：`translate` 為每個目標語言生成一個新的資料列變體，`localize` 則針對每組國家與語言配對生成在地化用詞的變體，而非直接翻譯；`sample_rate` 介於 0.01 到 1 之間，控制要擴充多少比例的資料列，計費則是依擴充後的輸出列數，而非原始列數。傳入不支援的 code 會回傳 400 錯誤並附上一組有效值範例。

📊 **接上 AutoScientist 後的內部評估數據**

生成的資料集 ID 可以直接傳給 `autoscientist.create`，讓它針對你的目標同時最佳化資料與訓練配方。AutoScientist 於 2026 年 5 月上線，是 Adaptive Data 這個產品支柱在訓練端的對應方案。Adaption 表示，AutoScientist 平均比自家研究人員手動配置的訓練成果高出 35%，勝率從 48% 提升到 64%；這些數字來自跨八個垂直領域的內部特化評估，資料集規模介於 5,000 到 100,000 列，架構則是 Together AI 提供微調服務的那些模型。

⚠️ **目前的限制**

生成完全依賴 Adaption 的託管平臺並按 credits 計費，沒有記載任何自架方案；上述效能數字也全部來自 Adaption 自家的內部評估，尚未見到第三方獨立驗證。

🎯 **對工程師的啟示**

如果你手上的任務缺乏乾淨的種子語料，卻能清楚用文字描述目標行為，這類工具值得評估：它把資料建構的起點從「整理既有資料」搬到「描述你要的行為」，理論上能省下不少標註前置作業，但落地前仍建議先用 `estimate=True` 抓清楚成本規模，並用小樣本驗證生成資料是否真的貼近你的任務分佈。

🔗 **來源**
- 標題：Adaption Labs Introduces 'Invent a Dataset': Training Data Generated From a Task Description, Not a Seed Corpus
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/09/04/datasets-invent-api-training-data-without-labeling-adaptive-data-autoscientist/

#SyntheticData #FineTuning #DatasetGeneration #AdaptionLabs #AutoScientist #SFT #DPO #TrainingData #MLOps #LLMTraining
