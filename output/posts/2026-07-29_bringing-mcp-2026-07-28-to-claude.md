---
title: Bringing MCP 2026-07-28 to Claude
source: Claude Blog
url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
model: tencent/hy3:free
generated_at: '2026-07-29T08:28:14.200938'
pinned: true
---

📌 【Anthropic 重大更新】MCP 邁向無狀態架構，正式支援企業級身份驗證

TL;DR：MCP 新版本轉向 Request/Response 模型，支援 Serverless 部署並強化 OAuth 2.0 認證。

隨著 MCP（Model Context Protocol）成為連接 AI Agent 與應用程式的產業標準，其月度 SDK 下載量已突破 4 億次，成長速度在今年內翻了 4 倍。Anthropic 於 2026 年 7 月 28 日發布了 MCP 的第五個規格版本，這是一次重大的架構演進。

🧩 **從雙向狀態化轉向 Request/Response 模型**

在這次的 MCP 2026-07-28 規格中，核心架構從原有的雙向狀態化（Bidirectional Stateful）協議，轉向了「無狀態（Stateless）」的核心設計。

- **架構改變**：改用 Request/Response 模型。
- **工程影響**：由於核心變為無狀態，開發者現在可以輕鬆地將 MCP Server 部署在 Serverless 或 Edge 基礎設施上。這大幅簡化了為 Claude 構建 MCP Server 的體驗，並能隨著使用量增加輕鬆進行擴展。

🧩 **標準化擴充功能與企業級認證**

除了底層架構的變動，新版本也針對開發者生態系推出了更成熟的框架：

- **標準化擴充（Standardized Extensions）**：MCP Apps 與 Tasks 現在採用版本化的擴充框架。開發者無需修改核心協議，即可正式加入如互動式使用者介面（Interactive UIs）或長時間運作任務（Long-running work）等功能。
- **認證強化（Auth Hardening）**：授權機制現在與生產環境中的 OAuth 2.0 及 OIDC 部署對齊。這意味著 MCP Server 現在可以直接連接至 Entra 或 Okta 等企業級身份識別系統，不再需要額外的規避方案（Workarounds）。

💡 **產業應用與實務價值**

隨著架構的演進，開發者能將設計與程式碼整合在單一的連接流程中。例如 Figma 的工程副總裁 Josh Clemm 指出，無狀態架構讓其能隨著使用量增長而擴展，並透過 MCP Apps 與企業管理認證，讓團隊在 Figma 畫布中更流暢地探索與精煉由 AI 產出的內容。

🎯 **實務啟示**

對於需要將 AI Agent 整合進企業工作流的工程師來說，MCP 的無狀態化與標準化認證，意味著未來可以更安全、更具擴展性地將 AI 能力與現有的企業內部工具（如 Figma 或 Intuit 等）進行深度整合。

🔗 **來源**
- 標題：Bringing MCP 2026-07-28 to Claude
- 機構／作者：Anthropic
- 連結：https://claude.com/blog/bringing-mcp-2026-07-28-to-claude

#AI #MCP #Anthropic #Claude #LLM #AIAgent #MachineLearning #SoftwareArchitecture #OAuth2 #Serverless
