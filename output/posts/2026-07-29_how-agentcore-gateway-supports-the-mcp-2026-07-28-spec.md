---
title: How AgentCore Gateway supports the MCP 2026-07-28 spec
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/
model: tencent/hy3:free
generated_at: '2026-07-29T08:33:56.338961'
score: 88
---

📌 【AWS ML】MCP 協議重大更新：轉向無狀態架構，AgentCore Gateway 已支援 2026-07-28 版本

TL;DR：MCP 協議轉向無狀態設計以解決擴展性問題，Amazon Bedrock AgentCore 可透過單一設定即時支援。

🚀 **MCP 協議迎來史上最大規模版本更新**

Model Context Protocol (MCP) 發布了 2026-07-28 規格，這是自協議推出以來最重要的一次修訂。這次更新不僅帶來了傳輸層（transport）的變動，更將協議轉向「無狀態」（stateless）設計，讓協議能更有效地在一般 HTTP 基礎設施上進行擴展，以應對企業級部署帶來的規模化挑戰。

🧩 **三大核心技術改進：無狀態、強授權與生命週期保障**

這次版本更新引入了數項關鍵設計，旨在提升協議的演進能力與安全性：

* **轉向無狀態設計**：透過轉向無狀態化，解決了企業級部署中的擴展性（scaling）難題。
* **強化授權機制**：更緊密地結合企業實務，與 OAuth 2.0 及 OpenID Connect 進行對齊，提升安全性。
* **建立生命週期保障**：為了避免未來版本更新導致功能損壞，引入了治理增強機制（governance enhancements），包括功能生命週期政策（feature lifecycle policy）、擴充功能框架（extensions framework）以及一致性測試套件（conformance-suite）要求。

⚠️ **版本不相容與平滑升級策略**

由於這次更新包含與舊版不相容（backward-incompatible）的變動，維護者採取了「選擇性加入」（opt-in）的升級策略：

1. **雙向行動機制**：升級是選擇性的，除非使用者與客戶端同時採取行動，否則不會發生任何變化。
2. **AgentCore Gateway 實作**：開發者可以透過呼叫 `UpdateGateway` 並傳入想要支援的版本列表，來讓 Amazon Bedrock AgentCore 的 AgentCore Gateway 支援最新協議。
3. **對既有客戶端透明**：現有的客戶端仍能照常運作，無需針對每個目標進行個別設定。客戶端會在每一次請求中，透過單一配置欄位選擇要使用的協議版本。

🎯 **實務啟示**

對於正在建構 AI Agent 的工程師而言，這次 MCP 的轉向意味著未來部署在大型企業環境中的工具（tools）與代理（agents）將具備更好的擴展性與安全性標準。建議開發者在升級至 2026-07-28 版本前，應確認客戶端已具備選擇版本的能力，並利用新增的擴充功能框架來進行功能演進。

🔗 **來源**
- 標題：How AgentCore Gateway supports the MCP 2026-07-28 spec
- 作者／機構：Sean Eichenberger @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/

#AI #MCP #ModelContextProtocol #AWS #AmazonBedrock #AgentCore #MachineLearning #SoftwareArchitecture #OAuth2 #Scalability
