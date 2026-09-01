---
title: Connect an AgentCore Runtime hosted MCP server to Amazon Quick
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/connect-an-agentcore-runtime-hosted-mcp-server-to-amazon-quick/
model: claude-code/sonnet
generated_at: '2026-09-01T10:52:56.722361'
score: 85
---

📌 打通 MCP 伺服器與 Amazon Quick 的完整路徑

TL;DR：AWS 教學示範如何用 AgentCore Gateway，把 MCP 伺服器接進 Amazon Quick。

當每個團隊都各自為 AI Agent 寫一套工具，重複造輪子的成本會隨團隊數量線性上升。AWS 這篇教學提供了一條「部署一次、到處重用」的路徑。

🤔 為什麼要接 MCP 進 Amazon Quick

MCP（Model Context Protocol）讓基礎模型能以標準化、安全的方式存取外部檔案、資料庫與 API，賦予 AI Agent 與真實應用互動、降低幻覺、支援多輪對話的能力，業界也迅速採用它來驅動 agentic AI 工作流程。Amazon Quick 支援 MCP 整合，讓自主執行、即時資料存取與專門子 Agent 的能力，能被接進聊天 Agent 與 Flows 工作流程。若已經有 MCP 伺服器，可以照這篇指南整合進 Amazon Quick；若還沒有，AWS 也提供在 AWS 上部署 MCP 伺服器的 Well-Architected 部署指引。文中強調，這個模式的價值在於重用：客戶能直接透過既有 MCP 伺服器重複使用常用工具與 Agent，不必為每個情境重新開發連接器。

🧩 架構：Gateway 居中橋接兩段 Auth

整合是透過 Amazon Quick 端的 connector 與 AgentCore 端的 Gateway 完成，兩者都屬於 Amazon Bedrock AgentCore（一個用於建構生成式 AI 應用的全託管服務）。從 Amazon Quick 到 AgentCore Gateway 的授權流程稱為 Inbound Auth，負責驗證使用者是否有權存取 MCP 伺服器；從 Gateway 到 AgentCore Runtime 的流程稱為 Outbound Auth，負責機器對機器的驗證。由於 MCP 協定目前要求以 OAuth 2.0 作為驗證協定，Outbound Auth 因此採用 OAuth 2.0。教學中以 Amazon Cognito 作為 Inbound Auth 的身分提供者（也可替換成其他 IdP），Outbound Auth 則交給專為 AI Agent 設計的 AgentCore Identity 服務處理。

💡 從本機 MCP 伺服器到可用工具的六道關卡

第一步是在 AgentCore Runtime 部署一個帶基本測試工具的範例 MCP 伺服器：伺服器使用 FastMCP、設定 stateless_http=True 以符合 AgentCore Runtime 的相容性要求，並固定對外路徑為 0.0.0.0:8000/mcp（多數官方 MCP SDK 的預設路徑），可先用本機用戶端測試。

第二步用 Bedrock starter kit 部署：configure 指令會互動式產生 Dockerfile、.dockerignore，以及儲存執行期設定的 .bedrock_agentcore.yaml，其中 --entrypoint 指定含 @app.entrypoint 主邏輯的檔案，--name 指定該 Agent 在帳號內的唯一識別；接著執行 launch 指令即完成部署。

第三步在 IAM 建立角色，用途選 Amazon Bedrock AgentCore，並附加一段內嵌政策，Resource 填入前面部署好的 MCP 伺服器 Runtime ARN。

第四步在 Amazon Cognito 建立 Inbound Auth 使用者池，負責在請求抵達 Gateway 前先驗證來自 Amazon Quick 的請求；並建立資源伺服器，定義 Gateway 會驗證的自訂 scope「invoke」，記下 Client ID、Secret 與 Discovery URL。

第五步同樣方式建立第二個 Cognito 使用者池作為 Outbound Auth，讓 Gateway 在呼叫 MCP 伺服器時能自我驗證身分；接著在 AgentCore Identity 建立 OAuth 憑證提供者，填入這個使用者池的 Discovery URL、Client ID 與 Client Secret。

第六步在 Amazon Bedrock AgentCore 主控臺建立 Gateway，串起前面設定的 Inbound／Outbound Auth，整條路徑即告完成。

🎯 實務啟示

這篇更像操作手冊而非新方法的發表，價值在於把 MCP 伺服器、Bedrock AgentCore 與 Amazon Quick 三者的驗證鏈路講清楚。如果組織內已有 MCP 伺服器、想讓 Amazon Quick 的 Chat Agent 或 Flows 能呼叫，可以直接套用這套 Inbound／Outbound 雙層 OAuth 模式，搭配 Cognito 與 AgentCore Identity 布局身分驗證，不必自己從零設計授權架構。

🔗 來源
- 標題：Connect an AgentCore Runtime hosted MCP server to Amazon Quick
- 作者／機構：Vivek Ghatala（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/connect-an-agentcore-runtime-hosted-mcp-server-to-amazon-quick/

#AWS #MCP #ModelContextProtocol #AgentCore #AmazonQuick #AIAgents #OAuth #CloudArchitecture #GenerativeAI #Bedrock
