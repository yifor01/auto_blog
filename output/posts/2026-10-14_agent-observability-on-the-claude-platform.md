---
title: Agent observability on the Claude Platform
source: Claude Blog
url: https://claude.com/resources/articles/agent-observability-on-the-claude-platform
model: claude-code/sonnet
generated_at: '2026-10-14T20:50:10.157800'
pinned: true
---

📌 Claude Platform 新增 OpenTelemetry Agent 追蹤

TL;DR：Claude 平臺的 Agent 現可輸出標準 OTel trace,直接接入既有觀測工具。

🎣 當你把更多權限交給一個 agent 之前,第一件該做的事不是信任它,而是先看清楚它每一步做了什麼。Claude Platform 這次更新,就是把這件事變成一行設定就能完成的事。

🤔 問題：Agent 的黑盒子怎麼debug

無論是 Claude Managed Agents、Messages API 還是 Claude SDKs,agent 在生產環境執行時會呼叫模型、使用工具、串接 MCP server,但這些步驟過去往往散落在各自的日誌裡,難以和既有的服務監控系統放在一起比對。Anthropic 的做法是讓這些呼叫以標準 OpenTelemetry（OTel）trace 的形式送出,開發者可以在把 agent 的存取權限放大之前,先逐步檢視它的 trace 記錄,確認其可靠性後再擴大授權。

🧩 架構：遵循 OTel GenAI 語意慣例

這些 trace 遵循 OpenTelemetry 的 GenAI semantic conventions,因此 Claude 產生的資料能和其他模型供應商的資料在同一套工具與儀表板中呈現,內容包含延遲（latency）、token 用量與各類 ID。在 Claude Console 中新增一個目的地（destination)後,每一次 agent turn、模型呼叫與工具使用都會以標準 trace 形式送出。Managed Agents 與 Messages API 需要在 Console 設定目的地,Claude SDKs 則會自動匯出 trace。

📊 可以接入的觀測工具

根據 Anthropic 的介紹,這些 trace 可以分三類方式使用：
- 與既有維運堆疊並排除錯：Grafana Cloud、Honeycomb、Sentry、Splunk,讓 agent trace 與現有的日誌、指標放在一起,快速定位是哪個服務造成延遲或失敗。
- 用生產資料改善 agent：Arize AI、Braintrust、Datadog、Langfuse、LangSmith by LangChain、New Relic、PostHog,把真實 trace 轉成評測（evals),用來抓出品質問題並驗證改動是否真的有效。
- 追蹤組織層級的用量：送到 Databricks Unity Gateway,讓平臺與安全團隊按團隊檢視 token 用量並標記異常活動。
除此之外,任何能接收標準 OTLP endpoint 的 OpenTelemetry 工具都可以串接。

💡 客戶怎麼用它

幾位客戶分享了實際應用場景。機器人除錯平臺 Foxglove 的共同創辦人兼 CTO Roman Shtylman 表示,原生 OTel 匯出讓他們能在 PostHog 中同時分析 agent 互動與產品使用數據。企業卡公司 Ramp 的資深工程師 David Traina 提到,他們打造了名為 Reflect 的 agent 系統,透過評分 Langfuse trace 找出重複發生的失敗並提出修正方案,在部分 agent 上已將 token 用量降低 10% 至 20%,並讓 session 速度提升 30%。量化交易公司 Sterling Labs 的 CTO Hyon Lee 則形容 Langfuse 是他們 24 小時監控市場的「pit wall」,原生匯出讓團隊不必再寫自訂 instrumentation。另一位基礎設施負責人 Ankush Sharma 則指出,當 agent 牽涉到公司帳務時,能把每次模型呼叫和對帳、分錄流程放在同一條時間軸中,方便稽核時回答「agent 做了什麼、為什麼這麼做」。

⚠️ 目前狀態

這項功能目前以公開 beta 形式提供,意味著介面與行為仍可能調整,正式導入生產環境前建議留意後續更新。

🎯 實務啟示

如果你的團隊已經把 Claude Code 或 Cowork 的 trace 接到某個觀測工具,現在用 Claude Platform 建的 agent 也能出現在同一個地方,不需要重新搭建一套監控管線。對正在擴大 agent 自主權限的團隊來說,這是一個相對低成本就能補上的「先觀察、再放權」機制。

🔗 來源
- 標題：Agent observability on the Claude Platform
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/agent-observability-on-the-claude-platform

#Claude #OpenTelemetry #AgentObservability #LLMOps #AIAgents #Anthropic #Langfuse #Grafana #Datadog #MCP
