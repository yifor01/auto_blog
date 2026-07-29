---
title: How AgentCore Gateway supports the MCP 2026-07-28 spec
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/
model: tencent/hy3:free
generated_at: '2026-07-29T14:15:12.700452'
score: 77
---

📌 【AWS 技術更新】MCP 協議迎來重大版本更新，AgentCore Gateway 已支援無狀態架構

TL;DR：MCP 2026-07-28 規格轉向無狀態架構，Amazon Bedrock AgentCore 可透過單一設定即可啟用。

隨著 AI Agent 應用規模擴大，如何讓模型與外部工具之間的溝通更具擴展性成為關鍵。Model Context Protocol (MCP) 近期發布了 2026-07-28 規格，這是該協議自發布以來規模最大且最重要的修訂。

🧩 **從有狀態轉向無狀態：解決企業級擴展挑戰**

這次更新最核心的技術變動是將 MCP 轉變為「無狀態（stateless）」協議。

- 基礎變更：協議現在可以基於一般的 HTTP 基礎設施進行擴展。
- 核心動機：協議維護者認為，轉向無狀態架構是應對企業級部署中擴展性（scaling）挑戰的必要手段。

⚠️ **引入不相容的變更，但未來將更穩定**

由於本次更新包含與舊版不相容（backward-incompatible）的變動，開發者需要注意。不過，為了避免未來頻繁出現破壞性更新，新版規格引入了全新的治理機制：

- 功能生命週期政策（Feature lifecycle policy）
- 擴充機制（Extensions framework）
- 符合性套件要求（Conformance-suite requirement）

這些機制旨在確保協議在演進的過程中，不會破壞核心功能。

🚀 **AgentCore Gateway 如何支援新規格**

對於使用 Amazon Bedrock AgentCore 的開發者來說，可以立即在 AgentCore Gateway 上使用最新的協議版本。

- 啟用方式：透過呼叫 `UpdateGateway` 並提供你希望 Gateway 支援的版本列表即可。
- 向下相容：現有的客戶端（clients）將維持原樣運作，不需要針對個別目標進行操作。
- 版本協商：Gateway 會透過單一配置欄位宣告其支援的協議版本，而客戶端則會在每次請求時選擇對應的版本。

🎯 **實務啟示**

這次更新對 AI Agent 的開發者來說，意味著底層通訊層變得更具企業級的穩定性與擴展性。由於升級是「選擇性加入（opt-in）」的，開發者可以根據需求，在確保客戶端與 Gateway 同步支援的情況下，平滑地遷移至新版本。

🔗 **來源**
- 標題：How AgentCore Gateway supports the MCP 2026-07-28 spec
- 作者／機構：Sean Eichenberger @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/

#AI #MCP #AWS #AmazonBedrock #AgentCore #MachineLearning #LLM #SoftwareArchitecture #CloudComputing #TechUpdate
