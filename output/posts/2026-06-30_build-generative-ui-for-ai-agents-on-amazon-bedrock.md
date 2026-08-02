---
title: Build generative UI for AI agents on Amazon Bedrock AgentCore with the AG-UI
  protocol
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-generative-ui-for-ai-agents-on-amazon-bedrock-agentcore-with-the-ag-ui-protocol/
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-30T20:28:26.705659'
---

📌 【AWS】透過 AG-UI 協定在 Amazon Bedrock AgentCore 打造生成式 UI

TL;DR：AG-UI 提供一套開放標準，讓 AI Agent 能在不同前端框架中渲染互動式介面與狀態同步。

AI Agent 的能力不應僅限於對話。如果 Agent 能夠在對話中直接渲染互動式圖表、即時更新共享畫布，或在執行關鍵步驟前暫停請求使用者確認，將能大幅提升使用者體驗。然而，要實現這些「生成式 UI (Generative UI)」與「人機協作 (Human-in-the-loop)」功能，後端 Agent 與前端介面之間需要一套標準的溝通協定。

🤔 **解決 Agent 後端與前端的耦合問題**

目前的挑戰在於 Agent 後端如何向前端傳遞動態事件。AG-UI (Agent-User Interaction Protocol) 旨在定義這套標準，讓 Agent 的邏輯與前端呈現完全解耦。開發者可以自由選擇後端框架（如 Strands Agents, LangGraph, CrewAI）以及前端函式庫（如 React, Angular, Vue），透過 AG-UI 協定將兩者連線。

🧩 **Amazon Bedrock AgentCore 的整合架構**

Amazon Bedrock AgentCore 是一個用於安全、大規模構建與執行 AI Agent 的平臺。其 Runtime 提供了一個無伺服器 (serverless) 的託管環境，並支援三種關鍵協定：
- Model Context Protocol (MCP)：連線 Agent 與工具。
- Agent2Agent (A2A)：連線 Agent 與其他 Agent。
- AG-UI：連線 Agent 與使用者。

當開發者部署帶有 AG-UI 標記的 Agent 容器時，AgentCore 會扮演透明代理 (transparent proxy) 的角色，負責處理身分驗證（透過 SigV4 或 Amazon Cognito 的 OAuth 2.0）、會話隔離 (session isolation)、擴展以及可觀測性。

💡 **實作路徑：從 FAST 模板到 CopilotKit**

在實務部署上，AG-UI 被整合進 Fullstack AgentCore Solution Template (FAST) 中，用以構建互動式前端。此外，透過 CopilotKit 的擴充，開發者可以在 Amazon Bedrock AgentCore 上實現更複雜的生成式 UI、共享狀態管理以及人機協作互動。

在技術實作層面，部署的容器需提供以下兩個端點：
- `POST /invocations`：處理 AG-UI 的請求。
- `GET /ping`：用於健康檢查。

🎯 **實務啟示**

對於開發 AI Agent 的工程師而言，採用 AG-UI 這種標準化協定的核心價值在於「靈活性」。你不再需要為每一種前端框架撰寫專用的 API 對接邏輯，只要後端遵循 AG-UI 規範，即可在不同前端環境中實現一致的互動體驗，並利用 Bedrock AgentCore 處理繁瑣的基礎設施（如驗證與擴展）問題。

🔗 **來源**
- 標題：Build generative UI for AI agents on Amazon Bedrock AgentCore with the AG-UI protocol
- 作者／機構：Ryan Razkenari @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/build-generative-ui-for-ai-agents-on-amazon-bedrock-agentcore-with-the-ag-ui-protocol/

#AWS #AmazonBedrock #AgentCore #GenerativeUI #AGUI #AIAgents #LLM #CopilotKit #HumanInTheLoop #Serverless
