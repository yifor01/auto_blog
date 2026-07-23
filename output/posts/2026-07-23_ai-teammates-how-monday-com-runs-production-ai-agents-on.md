---
title: 'AI Teammates: how monday.com runs production AI agents on Amazon Bedrock'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/ai-teammates-how-monday-com-runs-production-ai-agents-on-amazon-bedrock/
model: tencent/hy3:free
generated_at: '2026-07-23T08:20:16.524419'
score: 89
---

這篇素材屬於「產業新聞／部落格報導」，重點在於 monday.com 如何在生產環境中大規模部署 AI Agents。

📌 【AWS 案例分享】monday.com 如何在生產環境執行大規模 AI Agents：不僅是 Demo，而是真正的團隊成員

TL;DR：monday.com 透過 Sphera 系統將 AI Agent 整合進工作流，使人均 PR 吞吐量提升超過 50%。

🎣 隨著 AI 輔助工具普及，九成開發者每月都會使用 AI 編碼工具，而 monday.com 已將這項技術從「綠地開發的 Demo」推向了「大規模生產環境的實踐」。

🤔 **面對十年歷史與複雜架構的挑戰**

對於一個擁有十年歷史、數百個微前端（microfrontends）與微服務，且服務數百萬使用者的 SaaS 平臺來說，部署 AI Agent 並非只是寫個 Prompt。當 Agent 開啟一個 Pull Request (PR) 時，這個變動必須進入一個對穩定性要求極高的系統，且不能影響現有使用者的使用體驗。

🧩 **Sphera 架構：將 AI Agent 視為正式的團隊成員**

monday.com 開發了名為 Sphera 的內部 Agent 系統。與傳統的任務佇列（job queue）不同，Sphera 的核心是一個「Teams 頁面」，其設計理念是將 Agent 與人類工程師放在同一個層級：

- **身分識別**：每個 Agent 都有穩定的身分（Identity），其 Profile、經理（Manager）、許可權範圍（Scope）與效能評分（Performance score）與人類成員一致。
- **跨平臺整合**：Agent 的身分會流經 Slack、GitHub 與 monday 平臺。這意味著人類可以像對待同事一樣，對 Agent 進行標記（Tag）、指派任務（Assign）、進行程式碼審核（Code-review）或停用（Deactivate）該 Agent。
- **核心 Agent「Atlas」**：作為軟體工程師角色的 Agent，其工作流程是：接收 Ticket → 撰寫 PR → 交付功能。它沒有專用的 IDE，而是與人類工程師共用相同的 Backlog。

📦 **三種一級優先順序的「收件匣」**

為了讓 Agent 能夠實質參與工作，monday.com 為其設計了三種核心收件匣，所有訊息都會進入同一個 Agent Session：
1. Slack 的 @mention。
2. monday 平臺的專案指派（item assignment）。
3. GitHub 的 PR 審核請求（PR review request）。

📊 **實測資料：人均 PR 吞吐量提升超過一半**

根據 monday.com 自身的內部生產資料顯示：
- **開發效率**：每位工程師的 PR 吞吐量（PR throughput）提升了超過 50%。
- **工具普及率**：開發者使用 AI 編碼工具的比例從半年前的約 50% 成長至目前的 90%。

⚠️ **邁向完全自動化的挑戰**

雖然目前已能顯著提升效率，但要達到「完全自主」仍有差距。目前 monday.com 正在開發「具備信心評分的合併機制（confidence-scored merge play）」，試圖解決 Agent 在自動合併程式碼時的可靠性問題。

🎯 **實務啟示**

對於企業級應用而言，AI Agent 的價值不在於「寫出漂亮的 Demo」，而在於「如何處理合規性、處理線上維運（on-call）以及如何讓 AI 像人類一樣在既有的工作流中負責任」。

🔗 **來源**
- 標題：AI Teammates: how monday.com runs production AI agents on Amazon Bedrock
- 作者／機構：Claudio Mazzoni @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/ai-teammates-how-monday-com-runs-production-ai-agents-on-amazon-bedrock/

#AI #AgenticAI #AWS #AmazonBedrock #mondaycom #SoftwareEngineering #Productivity #MachineLearning #LLM #DevOps
