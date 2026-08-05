---
title: 'Y Combinator Open-Sources QM: An MIT-Licensed Multiplayer Agent Harness That
  Runs In Slack And The Web'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/03/y-combinator-open-sources-qm-multiplayer-ai-agent-harness/
model: tencent/hy3:free
generated_at: '2026-08-05T08:46:28.432228'
score: 89
---

📌 【YC 開源專案】打造企業級 AI 助手：多人協作框架 QM 正式釋出

TL;DR：YC 開源多代理人框架 QM，支援 Slack 與 Web，讓 AI 助手能以個人助理身份進行協作。

隨著 AI Agent 從單機實驗走向企業實務，如何讓 AI 在複雜的組織架構中安全、協作且具備記憶？Y Combinator (YC) 團隊決定將內部使用的多代理人框架（Multi-agent Harness）—— QM (Quartermaster) 開源，並採用 MIT 授權。

🤔 **不只是個人助理，而是組織內的協作節點**

目前的 AI Agent 大多被設計為「單人助理」，但 YC 團隊認為，若試圖用一個單一助手來處理整個公司的業務，複雜度會迅速失控。

QM 的設計理念是為每位員工提供一個「隔離的工作空間」，確保彼此互不干擾，同時支援在頻道（Channel）、群組訊息與專案中與 Agent 共同協作。

🧩 **架構設計：核心驅動與多端整合**

QM 的設計強調「架構中立性」（Harness-agnostic），這意味著你不會被單一模型供應商綁架。

- **核心驅動**：所有回合（Turn）都透過一個中央無頭核心（Headless Core）進行，該核心負責 API、身份驗證、策略與排程。
- **模型解耦**：核心可以驅動 Pi、OpenCode、Codex 或 Claude Code 等不同模型，部署結果不會受限於特定廠商。
- **技術棧**：核心直接在 Node 上執行 TypeScript 並使用 Fastify 處理 HTTP；Slack 插件使用 Bolt；Web UI 則由 Vite 與 Lit 構建。
- **持久化層**：使用 Postgres 儲存使用者資料、對話紀錄及其他持久化狀態。

📊 **具備「範圍感知」的記憶與技能**

為了在組織內運作，QM 為每個使用者與每個房間（Room）都配置了獨立的資源：

- **隔離資源**：每個範圍擁有專屬的記憶體（Memory）、檔案、鑰匙圈檢視（Keychain view）、權限、排程（Crons）以及可持續運行的沙盒（Durable sandbox）。
- **技能共享**：技能（Skills）是屬於特定範圍的，但可以透過授權進行共享，並經由管理員批准後推廣至整個組織。
- **自動化執行**：支援 Crons 與 Watches，可以在背景不經人工干預的情況下執行工作。

⚠️ **安全性：以「使用者身份」運行的代理人**

QM 遵循「本地編碼代理人」（Local coding agents）的模式，Agent 會以使用者的身份與憑證進行操作，因此所有行為都必須受到審計。

為了平衡效率與安全，QM 提供了三種不同的操作模式（Posture）：

1. **Auto（預設模式）**：在外部資料與工具結果傳遞給模型前，會先透過分類器（Classifier）進行來源標記與篩選。
2. **Strict（嚴格模式）**：除了兩個無影響的結尾動作外，每一次工具調用都會暫停並等待人工確認。
3. **Dangerous（危險模式）**：移除內容篩選並取消暫停，適合需要高度自動化的場景。

此外，系統內建了預先聲明的命令策略，對於像是遞迴刪除（Recursive deletes）或破壞性 SQL 指令等危險操作，即使在 Dangerous 模式下也會強制拒絕。

🎯 **實務啟示：適合誰使用？**

QM 並非傳統的桌面應用程式，而是一個組織級軟體。部署時需要準備雲端帳戶、Postgres 資料庫，並需要具備基礎設施管理能力的工程師。

- **適用對象**：規模約 10 到 500 人的新創公司或中型企業。
- **適用場景**：金融科技、法律運作、會計作業、B2B SaaS 內部工具開發。
- **應用範例**：同時搜尋內部筆記、郵件、文件與資料庫；定期自動分類並草擬郵件回覆；在現有的程式碼庫中執行測試、開啟 PR 並監控 CI；或在共享頻道中追蹤專案進度。

🔗 **來源**
- 標題：Y Combinator Open-Sources QM: An MIT-Licensed Multiplayer Agent Harness That Runs In Slack And The Web
- 連結：https://www.marktechpost.com/2026/08/03/y-combinator-open-sources-qm-multiplayer-ai-agent-harness/

#AI #YCombinator #OpenSource #MultiAgent #AIagent #SoftwareEngineering #Productivity #Slack #MachineLearning #EnterpriseAI
