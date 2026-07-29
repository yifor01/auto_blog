---
title: Bringing MCP 2026-07-28 to Claude
source: Claude Blog
url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
model: tencent/hy3:free
generated_at: '2026-07-29T14:07:38.188705'
pinned: true
---

📌 【Anthropic 重大更新】MCP 邁向無狀態架構，AI Agent 連結應用程式更強大

TL;DR：MCP 新版規格轉向無狀態核心，大幅提升擴展性與企業級認證安全性。

隨著 MCP (Model Context Protocol) 月下載量突破 4 億次，這項將 AI Agent 與應用程式連結的產業標準，正迎來史上最重要的規格演進。

🤔 **從雙向狀態轉向 Request/Response 模型**

在最新的 MCP 2026-07-28 規格中，核心架構發生了根本性的變革：

🧩 **架構轉型：邁向 Stateless Core**
- 從原本的雙向狀態協議 (bidirectional stateful protocol) 轉向請求/回應 (request/response) 模型。
- **工程師的好處**：由於核心變為無狀態，開發者現在可以將 MCP Server 部署在 Serverless 或 Edge 基礎設施上，這讓開發與擴展規模變得更加簡單。

🧩 **功能擴展：標準化的 Extensions 框架**
- MCP Apps 與 Tasks 現在透過版本化的擴展框架 (versioned extensions framework) 發布。
- 讓開發者無需更動核心協定，即可正式加入如互動式使用者介面 (interactive UIs) 或長時間運行的任務 (long-running work) 等能力。

🧩 **安全性強化：對齊企業級認證標準**
- 授權機制現在與生產環境的 OAuth 2.0 及 OIDC 部署保持一致。
- 這意味著 MCP Server 現在可以直接連接到 Entra 或 Okta 等企業級身份識別系統，不再需要額外的規避方案 (workarounds)。

💡 **業界應用與實務影響**

Figma 工程副總裁 Josh Clemm 指出，隨著使用量成長，無狀態架構能有效支撐其規模；結合 MCP Apps 與企業管理認證，能讓設計與程式碼在一個連接的流程中協作。

🎯 **實務啟示**
對於正在構建 AI Agent 的工程師而言，這次更新意味著可以利用更低成本的雲端架構來部署工具，同時能以更符合企業資安規範的方式，安全地將 AI 能力整合進現有的企業工作流中。

🔗 **來源**
- 標題：Bringing MCP 2026-07-28 to Claude
- 機構/作者：Anthropic
- 連結：https://claude.com/blog/bringing-mcp-2026-07-28-to-claude

#Anthropic #MCP #AI #AIAgent #ModelContextProtocol #SoftwareEngineering #Serverless #OAuth #EdgeComputing #TechUpdate
