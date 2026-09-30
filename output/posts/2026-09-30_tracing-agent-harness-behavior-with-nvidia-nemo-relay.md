---
title: Tracing Agent Harness Behavior with NVIDIA NeMo Relay
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/
model: claude-code/sonnet
generated_at: '2026-09-30T21:43:47.068149'
score: 88
---

📌 NeMo Relay揪出Agent看不見的繞路

TL;DR：NVIDIA NeMo Relay 用三種追蹤格式記錄 agent 執行細節，讓開發者不只看「有沒有成功」，還能看「怎麼成功的」。

Agent 最後給出正確答案，不代表過程有效率。一次失敗的搜尋可能觸發第二次搜尋，一次被截斷的檔案讀取可能導致重複抓取同樣內容，這些多餘的步驟全都被「答案正確」這個結果蓋過去，卻實實在在拖慢延遲、多耗 token，也增加了出錯的機會。

🤔 **成功與否不能解釋過程**

要改善 agent 的行為，開發者需要同時知道任務有沒有成功，以及 agent 是怎麼走完這條路的。單純的成功檢查沒辦法說明 agent 為什麼從工具錯誤中恢復、為什麼提早停止，或為什麼需要額外呼叫模型。

🧩 **三種追蹤格式各有用途**

NeMo Relay 原生整合進熱門的 Hermes Agent harness，把 session、turn、model call、tool call 對應到自己的 scope 階層，並記錄每個工作開始與結束的生命週期事件，保留時序與親子關係。素材中整理出三種追蹤輸出格式：

- **ATOF（Agent Trajectory Observability Format）**：JSONL 格式的 scope 開始／結束與時間點標記，附帶 ID 與時間戳，用來除錯或稽核個別事件、時序與親子關係。
- **ATIF（Agent Trajectory Interchange Format）**：從生命週期事件組裝出的逐步 JSON 紀錄，記下 agent 的互動、工具呼叫與觀察結果，適合逐步檢視或評估 agent 走過的路徑。
- **OpenTelemetry + OpenInference**：把整個執行過程記成有親子關係的 span，OpenInference 負責標記 agent、LLM、工具各類 span 並定義其屬性，可以在 Arize Phoenix 這類支援 OTEL 的工具中檢視模型與工具呼叫、耗時、token 用量與錯誤。

值得注意的是，ATIF 裡的工具請求只顯示模型「要求」執行什麼，不代表確認了實際結果；要驗證真正發生的事，得回頭查 ATOF 裡對應的工具開始／結束事件與任何記錄下來的錯誤。事件用共同的 uuid 配對，parent_uuid 則把工具呼叫連回其上層的呼叫。

📊 **實測跑一次簡單任務的追蹤數據**

教學的第一個實驗刻意做得很小：Hermes 在隔離的 Docker 容器中執行一支固定輸出 VALUE=42 的 Python 腳本，容器無法連網、無法存取儲存庫或 API 金鑰，藉此提供一個精確的成功判準。一次驗證通過的執行留下的 ATOF 摘要為：74 個事件、2 個完成的 llm scope、prompt tokens 7239、completion tokens 96、總計 7335 tokens、1 次工具呼叫、0 次工具錯誤；對應的 ATIF 摘要則是：模型 nvidia/nemotron-3.5-lightning-30b-a3b、3 個步驟、2 次 llm 呼叫、1 次工具呼叫請求，最終輸出 "Task verified: VALUE=42"。

第二個實驗則升級為多工具研究任務：Hermes 拿到一份帶有線索的旅行紀錄，必須找出對應的機器學習研討會、在官網確認資訊、把結果寫進報告並回傳研討會名稱，過程中用 NeMo Relay 的 OpenInference exporter 把 OpenTelemetry span 透過 OTLP 送到 Arize Phoenix。

⚠️ **追蹤資料要小心處理**

分享追蹤結果前務必先檢查內容，因為依設定不同，裡頭可能含有 prompt、模型回應、工具參數與結果、檔案路徑等應用程式資料。

🎯 **拿證據去評估harness的改動**

素材提到一個 Hermes ToolPerf 案例研究，示範如何用同一套追蹤方法，搭配任務驗證結果，評估對 agent harness 做出的改動在多次重複執行下的表現差異，而不是只看單次成功與否。

🔗 **來源**
- 標題：Tracing Agent Harness Behavior with NVIDIA NeMo Relay
- 作者／機構：William Markito Oliveira, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/tracing-agent-harness-behavior-with-nvidia-nemo-relay/

#NVIDIA #NeMoRelay #AgentObservability #OpenTelemetry #HermesAgent #LLMOps #AgentTracing #ArizePhoenix #AIDebugging #AgenticAI
