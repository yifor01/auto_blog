---
title: How Databricks Uses AI to Accelerate Incident Investigation
source: Databricks
url: https://www.databricks.com/blog/how-databricks-uses-ai-accelerate-incident-investigation
model: claude-code/sonnet
generated_at: '2026-08-25T06:20:11.570580'
score: 98
---

📌 Databricks 如何用 AI 加速事故調查

TL;DR：Databricks 打造 AI SRE 代理，在事故發生瞬間自動展開排查，協助工程師快速定位根因。

凌晨兩點，一個面向客戶的 API 延遲飆升，值班工程師被叫醒，開始熟悉的排查流程：翻日誌、查指標、對照最近的部署紀錄、翻閱 runbook。每一項工具單獨看都沒問題，但把這些訊號串起來判斷「到底發生了什麼」，這件事完全發生在工程師的腦子裡。老手可能幾分鐘就抓到熟悉的模式，新手可能要花上幾小時，甚至得升級求援。

🤔 背景：Databricks 要在 1500+ Kubernetes 叢集上找答案

Databricks 目前在三朵雲、70 多個地區，維運橫跨 1500 多個 Kubernetes 叢集的數百個微服務。團隊沒有一開始就動手做 agent，而是先花數週訪談了跨數十個團隊的值班工程師，閱讀事後檢討報告與調查文件，追問一個簡單的問題：時間都花在哪裡？卡關又是卡在哪裡？從這些訪談中，團隊確認排查工作其實是一連串可重複的調查步驟，加上工程師的專家判斷，這讓「用 AI agent 加速排查」這件事變得可行，但也意識到沒有任何單一團隊能打造出理解所有服務、訊號與失效模式的 agent，因此需要一個共用平臺，把蒐集情境、執行工具與 runbook、關聯證據等共通建構模組做好，同時讓各團隊能用自己的維運知識擴充它。

🧩 AI SRE：自動觸發的三路並行調查

AI SRE 支援兩種互補的使用情境：事故一觸發就自動啟動的自動分診（automatic triage），以及讓工程師主動探索假設的互動式調查（interactive investigation）。

事故一觸發，AI SRE 會在工程師打開筆電之前就啟動三條並行調查軌道：

- 平臺健康檢查：檢視服務所在環境的狀態，先排除一大類「假警報」，避免工程師花 30 分鐘查應用程式碼，結果發現根因其實是大規模基礎設施問題。
- 服務層分析：拉取受影響服務及其直接依賴的日誌、指標與追蹤，檢視最近的部署與設定變更，並找出相對於服務基準行為的異常，例如指出「CPU 在凌晨 2:47 飆升 3 倍，恰好與一次改動批次大小的部署同時發生」，而不只是「CPU 過高」。
- Runbook 執行：AI SRE 會扮演團隊專屬的角色，執行各團隊自訂的排查程序。團隊可以用 skills 把既有 runbook 轉換成 agentic runbook，這些 skills 會參考程式碼庫、可觀測性資料與過往事故紀錄，讓 runbook 執行更準確、更貼合情境，並在數秒內完成原本需要專家花數分鐘進行的檢查。

等工程師第一次讀到事故詳情時，AI SRE 已經整理好一份完整的診斷摘要：哪裡壞了、改了什麼、團隊的 runbook 建議檢查什麼，所有訊號、關聯與下一步都在同一個畫面上。並非每次調查都靠自動分診就能結案，AI SRE 的介面也提供互動式排查環境，讓工程師能用自然語言追問，例如「這次告警前 10 分鐘，Kafka consumer lag 有沒有異常」，AI SRE 會抓取對應指標、疊在事故時間軸上並解釋發現。

🧩 分層架構：從原始資料到可對話的除錯環境

團隊把 AI SRE 設計成分層平臺：最底層是 Primitives，也就是每次調查最終都依賴的原始維運資料（指標、告警、日誌、發布資訊與程式碼）；往上是 API 層，透過 Observability API、Deployment API、Alerts API 統一處理身分驗證、速率限制與資料正規化，把「原始基礎設施」變成「可除錯的基礎設施」；再往上是核心引擎，由 bot 框架負責編排，處理平行執行、結果關聯與 LLM 驅動的綜合分析；最上層則是應用層，也就是平臺層級的事故分診 bot 運作的地方，同時也是第三方 AI 工具可以接入、補充能力的地方。

💡 可信任的關鍵：結構化檢查先行、結論可追溯

要讓 LLM 驅動的 agent 在講求信任的事故應對場景中可靠，團隊遵循了幾個原則：先跑確定性的平臺健康檢查與 runbook 步驟，LLM 只負責綜合與解釋結果，資料蒐集本身不交給模型自由判斷；每個結論都要能連回底層證據，例如具體的指標、日誌行或部署差異，讓工程師能驗證推理過程，而不是單純相信結果；如果 AI SRE 無法有信心地判定根因，它會明確說出來，並把已蒐集到的證據按相關性整理呈現，團隊認為誠實的部分調查，遠比一個幻覺出來的診斷更有用。

🎯 實務啟示

對正在打造內部可觀測性或事故應對工具的團隊來說，AI SRE 的分層設計值得參考：把原始資料、統一 API、編排引擎與應用邏輯拆開，才能讓中央維護的工作流程與團隊自訂的 runbook 並存，而「結構化檢查先行、結論可追溯、誠實承認不確定」這三個原則，也是任何要把 LLM 放進高風險決策場景的系統都該留意的底線。

🔗 來源
- 標題：How Databricks Uses AI to Accelerate Incident Investigation
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/how-databricks-uses-ai-accelerate-incident-investigation

#Databricks #AISRE #IncidentResponse #Observability #Kubernetes #LLMAgent #SRE #Runbook #RootCauseAnalysis #AIOps
