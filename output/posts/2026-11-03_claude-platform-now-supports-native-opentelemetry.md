---
title: Claude Platform now supports native OpenTelemetry observability in Databricks
  MLflow
source: Databricks
url: https://www.databricks.com/blog/claude-platform-now-supports-native-opentelemetry-observability-databricks-mlflow
model: claude-code/sonnet
generated_at: '2026-11-03T22:40:15.844566'
score: 81
---

📌 Claude 原生支援 OpenTelemetry,接進 Databricks MLflow

TL;DR：Claude Platform 現在能把執行軌跡原生匯出到 Databricks MLflow,方便工程師除錯與評估 agent。

Agent 給出一個看起來很合理的答案,卻漏掉了關鍵發現,或是重複讀了同一份資料來源三次——光看最終輸出,你永遠不會知道哪裡出了問題。Databricks 這次宣布的整合,就是為了把這個「看不見的黑箱」打開。

🤔 **答案本身說明不了失敗的原因**

Databricks 指出,問題的根源在於:agent 的錯誤往往不是答案本身有問題,而是中間過程——漏讀的上下文、失敗的工具呼叫,或是模型如何使用工具回傳結果——出了狀況。要找到原因,必須看到模型與工具呼叫背後的完整執行軌跡（trace）。

🧩 **Trace 如何從 Claude 一路流到 Unity Catalog**

MLflow Tracing 建立在 OpenTelemetry 這個開放標準之上。一筆 trace 會把 agent 的執行拆成一個個 span,例如一次模型請求或一次工具呼叫。Claude 的原生 instrumentation 會產生這些 span,並用 OpenTelemetry Protocol 匯出。資料流向是這樣的:

1. Claude 端(Anthropic SDK、Messages API、Managed Agents)產生 span。
2. 透過 Zerobus Ingest 送進 Databricks。
3. 資料落地到 Unity Catalog 的表格,並連結到對應的 MLflow experiment。

Databricks 強調,這個組合能同時帶來「低延遲、高 QPS 的 trace 寫入」與「對 agentic trace 中敏感資料的存取治理」兩個好處,因為 Unity Catalog 本身就負責權限控管,資料也可以直接用 SQL 查詢。

設定方式是在 Databricks 的 Experiments 分頁建立新 Experiment,Trace storage location 選擇 Unity Catalog,指定既有的 catalog 與 schema,再用 workspace ID、region 與 spans table 設好 Databricks destination。Anthropic SDK 這端則要安裝對應套件、設定 OTel tracer provider 與 exporter。Claude Code 與 Claude Agent SDK 也支援 OpenTelemetry,只要在啟動前多設幾個環境變數,一樣能把 trace 送到同一個 destination。文中也特別提到,trace 裡的 input 與 output 只有在把 content mode 設成「full」時才會被完整記錄。

📊 **Trace 進了 MLflow 之後能做什麼**

資料到位後,Databricks 列出幾個具體的後續用法:

- **Analyze trace / Genie Code**:檢視某次執行的記錄,幫忙解釋哪裡出錯,還能針對缺少的上下文、失敗的工具呼叫或昂貴的步驟繼續追問。
- **MLflow Issues(Beta)**:用 Genie Code 檢視回應、工具呼叫、時間與評分,把相關的問題分組,並附上支撐用的 trace 連結,例如重複搜尋浪費 token、缺少參數導致工具失敗、回應格式不符要求等情境。這項分析也能排程持續執行,修復後還能追蹤問題是否復發。
- **MLflow Review Queues**:把挑選出的 trace 與問題交給人類審核者,由他們判斷缺了什麼、給出預期答案,再把回饋用於後續的評估基準。
- **MLflow Agent Evaluation**:針對 Claude trace 執行評估,測試修改 prompt、skill 或工具後 agent 是變好還是變差,例如用 LLM judge 檢查 agent 是否出現多餘的工具呼叫,兩個版本的評估結果還能在 MLflow UI 中並排比較。

🎯 **實務啟示**

對已經在用 Claude 建置 agent 的團隊,這代表除錯與評估流程可以直接搬進既有的 Databricks/MLflow 生態系,不用額外接一套 observability 工具;而 Unity Catalog 的治理能力,對需要管控敏感 trace 資料存取權限的企業環境尤其實用。

🔗 **來源**
- 標題：Claude Platform now supports native OpenTelemetry observability in Databricks MLflow
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/claude-platform-now-supports-native-opentelemetry-observability-databricks-mlflow

#Claude #Anthropic #OpenTelemetry #Databricks #MLflow #AgentObservability #LLMOps #Tracing #AIEngineering #Observability
