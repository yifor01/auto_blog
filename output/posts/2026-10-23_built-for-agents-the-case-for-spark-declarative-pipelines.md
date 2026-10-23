---
title: 'Built for Agents: The Case for Spark Declarative Pipelines'
source: Databricks
url: https://www.databricks.com/blog/built-agents-case-spark-declarative-pipelines
model: claude-code/sonnet
generated_at: '2026-10-23T20:45:41.519596'
score: 86
---

📌 Databricks 實測：AI Agent 寫 Pipeline，宣告式比程序式省 34 倍算力

TL;DR：Databricks 用 528 次 AI agent 建置實測，證明宣告式 Spark Pipeline 比程序式更省算力、程式碼更短。

如果你的 Pipeline 有七成是 AI agent 寫的，你還會在意「哪個 agent 比較聰明」嗎？Databricks 的答案是：比起挑 agent，你更該在意 agent 被允許用什麼方式寫程式碼。

🤔 **agent 已經寫了超過七成的 SDP pipeline**

Databricks 指出，在 Databricks 平臺上，超過 70% 的 Spark Declarative Pipelines（SDP）現在是由 AI agent 建立的。這帶來兩個現實問題：每次 agent 嘗試都要花算力和時間，所以迭代必須便宜；而程式碼審查變成關鍵關卡，所以程式碼必須精簡、可讀、正確。Apache Spark 提供兩種寫 Pipeline 的方式：程序式（procedural）與宣告式（declarative），差別在於你寫什麼、Spark 能在執行前檢查什麼，以及犯錯的代價有多高。

🧩 **結構性錯誤可以在跑之前就抓到**

程序式 Pipeline 是一步步告訴 Spark 怎麼建出每個資料集的程式碼，唯一驗證方式是真的跑一次。宣告式 Pipeline 則只描述你想要的資料集，由 Spark 決定怎麼建，概念上類似你對 LLM 下提示詞，讓它自己找出對的工具與步驟去完成。

錯誤分兩種：結構性錯誤（未解析的欄位參照、尚不存在的表、不允許的設定變更）可以靠讀程式碼找出來；靜默錯誤（跑完但答案是錯的）只有在執行結束後才會顯形。因為宣告式 Pipeline 是「描述」而非「執行」，Spark 可以在跑之前先用 dry run 讀懂整份描述，這跟型別語言（如 Rust）在編譯期就能檢查資料流動方式類似。Databricks 也指出，程序式寫法中，agent 除了寫資料操作（過濾、join），還要自己寫執行順序與結果儲存的輔助程式碼，這些重複的樣板程式碼在宣告式寫法裡由 Spark 統一處理，agent 寫的程式碼變少，團隊要審查與維護的東西也變少。

📊 **22 個任務、528 次建置的結果**

Databricks 設計了 22 個模擬真實工單的資料工程任務，每個任務各配 12 組帶有真實髒資料特徵的輸入資料集，agent 分別用程序式 PySpark 和 Spark Declarative Pipelines 各寫一次，總共 264 次建置 × 2 種方式 = 528 次建置，全程使用 Opus 4.8，由不知道來源的自動化評分器檢查輸出是否符合表格規格；宣告式版本在跑之前會先經過 Spark 的 dry run 驗證，失敗可在上限次數內修改重試。

結果顯示兩種方式幾乎都能完成任務：程序式完成 264 件中的 255 件，宣告式完成 258 件。差異出現在周邊指標：

| 指標 | 程序式 | 宣告式 |
|---|---|---|
| 叢集時間（executor-seconds） | 596（基準） | 17（約少 34 倍） |
| 程式碼行數（中位數） | 131 行 | 64 行（少約 51%） |
| LLM token 花費（中位數） | 約 $0.26 | 約 $0.50（約 2.3 倍） |

結構性錯誤必須等 Spark 在叢集上真正跑到壞掉的那一步才會現形，程序式建置因此完全無法在執行前擋下任何錯誤；宣告式則靠 dry run 提早攔截，把叢集浪費的算力壓低了 34 倍。程式碼量上，宣告式版本也更精簡、寫法更一致：有 19 個程序式建置用了逐行處理記憶體內資料的捷徑，在測試資料上能過，但資料量變大就可能失敗，而宣告式建置沒有一個這麼做。

💡 **兩個誤差相當的地方：靜默錯誤與前期成本**

dry run 只能抓結構性錯誤，抓不到靜默錯誤——跑得很順但答案是錯的那種，這也是更危險的一種。在這一項上，兩種方式的靜默錯誤率差距在 15% 以內，算不上有實質差異。另外，宣告式方式把更多思考成本挪到前期：agent 反覆在 dry run 上迭代到結構正確為止，這筆 token 花費是固定的一次性成本，不會隨資料量或執行頻率變化；而程序式方式浪費的叢集算力則是會隨資料量重複發生的成本。付一次固定的錢去避免一筆會隨規模持續增長的錢,在 Pipeline 和資料規模變大時只會越划算。

⚠️ **宣告式不是萬靈丹**

dry run 檢查的是結構，不是邏輯。靜默錯誤仍然需要測試與人工審查才能抓到，這點兩種方式打平。而且宣告式在開發階段多花了約 2.3 倍的 token，換來的是在生產規模下不必在注定失敗的 Pipeline 上浪費叢集時間。

🎯 **實務啟示**

在評估要用哪個 agent 寫 Pipeline 之前，先看它被允許用什麼程式設計模型寫。更好的 agent 會犯更少錯，但宣告式架構能讓犯的錯「便宜」,並且在真正花錢之前就被攔下來。Databricks 建議團隊可以直接參考公開的程式設計指南，搭配 PySpark 的 SDP skill 讓 agent 上手。

🔗 **來源**
- 標題：Built for Agents: The Case for Spark Declarative Pipelines
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/built-agents-case-spark-declarative-pipelines

#ApacheSpark #DeclarativePipelines #DataEngineering #AIAgents #Databricks #DataPipeline #LLMOps #CodeReview #CloudComputing #MachineLearning
