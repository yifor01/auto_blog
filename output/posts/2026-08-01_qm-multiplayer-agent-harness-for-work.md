---
title: qm – Multiplayer agent harness for work
source: Hacker News
url: https://github.com/yc-software/qm
model: tencent/hy3:free
generated_at: '2026-08-01T08:19:26.064352'
score: 71
---

📌 【開源專案】qm：專為新創團隊設計的多人協作 AI Agent 架構

TL;DR：qm 提供具備隔離工作區、可擴展模型與多端同步能力的 AI Agent 框架。

當目前的 AI Agent 多半被設計為「個人助理」時，如何將其規模化到整個公司，且不讓複雜的權限與資料混亂，成為企業導入 AI 的痛點。qm 專為新創公司設計，讓員工在擁有獨立工作空間的同時，也能在 Slack 或 Web 端進行協作。

🧩 **核心架構：解耦模型與介面，實現高度靈活性**

qm 的設計哲學是「核心與插件分離」，這意味著你的部署不會被單一供應商綁架。

- **Headless Core (無頭核心)**：負責 API、身分識別、策略與排程。
- **Agent Loop (代理迴圈)**：支援多種模型與架構，如 Pi、OpenCode、Codex 以及 Claude Code，可以隨時切換。
- **Per-scope Sandbox (作用域沙盒)**：每個使用者或專案擁有獨立的檔案、工具、登入服務與持久化環境，確保任務執行時的安全性與隔離性。
- **Persistence Layer (持久化層)**：使用 Postgres 儲存 Session、記憶體與任務隊列。

🔌 **多端同步與功能整合**

qm 不僅僅是一個後端框架，它透過插件化提供多種互動介面：
- **Slack & Web 雙端同步**：無論是在 Slack 頻道還是 Web App，使用者的身份與設定都能保持一致。
- **內建 Web Apps**：開發者可以快速建立內部專用 App 並發布給特定人員。
- **背景工作 (Crons & Watches)**：支援排程執行任務，實現自動化工作流。

📊 **應用場景：從搜尋資料到自動化開發**

- **整合資訊檢索**：同時搜尋公司內部的筆記、郵件、文件、資料庫與 Web 資訊。
- **郵件與寫作風格**：學習使用者的寫作風格，並依排程自動分類與草擬郵件回覆。
- **程式碼庫操作**：在現有的 Repository 中執行測試、開啟 PR、監控 CI 以及檢查系統日誌。

⚠️ **安全性設計：分級管理權限與審核**

qm 採用「代理代表使用者執行」的模式，所有的操作都會被審核。根據安全性需求，提供三種等級：
- **Strict (嚴格)**：除了兩項無影響的終止指令外，所有工具調用都必須經過人類批准。
- **Auto (預設)**：使用分類器對外部資料與工具結果進行篩選，再交給模型處理。
- **Dangerous (危險)**：不進行內容篩選，也不在工具調用之間進行暫停。
*註：無論何種模式，針對刪除或毀滅性 SQL 等指令，皆有預設的強制拒絕政策。*

🎯 **實務啟示：如何部署與維護**

對於工程師來說，qm 提供了一套清晰的部署與客製化路徑：
- **快速初始化**：透過 `qm init` 指令，可快速完成基礎設施、Web 登入與 Slack 連結的部署。
- **私有化客製化**：建議使用 `git clone --bare` 的方式建立私有 Fork，而非使用 GitHub 的 Fork 功能，以確保組織專有的設定、工具與沙盒映像檔不會流向公有端，同時又能與上游 (upstream) 保持同步。

🔗 **來源**
- 標題：qm – Multiplayer agent harness for work
- 連結：https://github.com/yc-software/qm

#AI #Agent #OpenSource #MultiplayerAgent #LLM #SoftwareEngineering #Startup #Productivity #Automation #MachineLearning
