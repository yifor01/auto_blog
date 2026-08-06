---
title: How we built an MCP bridge to give our AgentCore-hosted AI agent access to
  local MCP tools
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-we-built-an-mcp-bridge-to-give-our-agentcore-hosted-ai-agent-access-to-local-mcp-tools/
model: tencent/hy3:free
generated_at: '2026-08-06T08:31:12.136035'
score: 99
---

📌 【AWS 技術分享】如何透過 MCP Bridge，讓雲端 AI Agent 操控你電腦裡的本地工具

TL;DR：透過 WebSocket 與 Native Messaging 建立橋樑，讓部署在雲端的 AI Agent 能直接存取本地端的 MCP 工具。

🎣 **當雲端 Agent 遇上本地端檔案：如何跨越雲端與桌機的鴻溝？**

想像一下，你的 AI Agent 運行在雲端（如 Amazon Bedrock AgentCore），但你的關鍵數據——例如 Excel 試算表——卻靜靜地躺在你的筆電硬碟裡。這中間存在著巨大的鴻溝：雲端 Agent 無法直接讀取你的本地檔案，而傳統的 MCP（Model Context Protocol）標準雖然解決了模型與工具的連接問題，但它預設的通訊機制（如 stdio 或 HTTP）往往難以直接跨越「雲端服務」與「本地處理程序」之間的界限。

🤔 **為什麼我們需要一個「橋樑」？**

Anthropic 在 2024 年 11 月推出的 MCP 標準，旨在統一 AI 模型連接外部數據與工具的方式。目前的 MCP 架構主要依賴兩種傳輸機制：
- **stdio**：用於同一臺機器上的本地處理程序通訊。
- **streamable HTTP**：用於遠端伺服器與客戶端之間的通訊。

然而，當「MCP Client 在雲端」而「MCP Server 在本地」時，現有的機制就失效了。這對於需要處理本地 Excel 檔案進行財務分析的專業人士來說，是一個嚴重的痛點。為了讓雲端 Agent 能像 Claude Code 或 Amazon Quick 那樣調用本地工具，我們需要一種機制來封裝並傳輸這些訊息。

🧩 **架構解析：透過 WebSocket 與 Native Messaging 實現通訊**

為了實現這個目標，我們開發了一套基於「橋樑（Bridge）」的概念，將訊息在不同層級間進行封裝與解封裝。

🚀 **訊息傳輸的四個關鍵步驟**

1.  **建立安全連線**：瀏覽器擴充功能透過一個預簽章（Presigned）的 WebSocket URL 與 AgentCore 運行時建立連線。為了安全性，該 URL 使用 AWS SigV4 簽章，且有效期僅 5 分鐘，由本地端的 SDK 負責更新，確保憑證不會離開使用者的電腦。
2.  **發送請求**：當 Agent 需要呼叫工具時，它會發送一個包裝在 JSON 封套（Envelope）中的 MCP JSON-RPC 請求，經由 WebSocket 回傳至瀏覽器擴充功能。
3.  **本地轉譯**：擴充功能透過 **Native Messaging**（一種瀏覽器與本地程式通訊的機制）將訊息轉交給本地的「MCP Bridge」。Bridge 會拆解封套，提取原始的 JSON-RPC 內容。
4.  **執行工具**：Bridge 將內容透過 stdio 傳送給本地的 MCP Server。當 Server 回傳結果後，Bridge 會重新包裝訊息，依原路徑傳回雲端 Agent。

💡 **MCP Bridge 的內部設計：雙迴圈與非同步處理**

為了確保效能與穩定性，MCP Bridge 內部採用了雙迴圈（Two-loop）設計，並透過 `FastMCP` proxy 進行管理：
- **主迴圈**：負責讀取來自瀏覽器的訊息、解析 JSON 並將其放入輸入佇列（Input Queue）。
- **背景迴圈**：負責從輸出佇列（Output Queue）提取結果，封裝後寫回 stdout 給瀏覽器。

這種設計將「瀏覽器的請求頻率」與「MCP Server 的處理速度」解耦合（Decouple），避免了因為某個工具執行過慢而導致整個通訊通道阻塞的問題。此外，透過 `asyncio.Future` 機制，系統可以同時處理多個正在進行中的工具呼叫（In-flight tool calls），而不會產生歧義。

📊 **開發實作細節**

- **工具發現（Tool Discovery）**：Agent 在每次發送訊息時會呼叫 `tools/list`。一旦 MCP Server 新增了工具，Agent 無需更改程式碼即可自動獲得新能力。
- **通訊限制**：為了保護瀏覽器，單筆訊息的最大容量限制為 1 MB。
- **配置簡化**：新增一個 MCP Server 僅需修改 `mcp.json` 檔案中的一行配置，其餘複雜的通訊邏輯皆由 Bridge 處理。

🎯 **實務啟示**

對於需要處理高度敏感數據（如金融報表、本地開發環境）的企業來說，這種「雲端思考、本地執行」的模式提供了極大的靈活性。開發者可以利用雲端強大的運算能力與模型，同時保有對本地數據的控制權與安全性，無需將所有私密檔案都上傳至雲端。

🔗 **來源**
- 標題：How we built an MCP bridge to give our AgentCore-hosted AI agent access to local MCP tools
- 作者／機構：Rohan Lekhwani @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/how-we-built-an-mcp-bridge-to-give-our-agentcore-hosted-ai-agent-access-to-local-mcp-tools/

#AI #MCP #AWS #AmazonBedrock #AgentCore #MachineLearning #SoftwareArchitecture #CloudComputing #LLM #DeveloperTools
