---
title: Electric joins Databricks to bring WASM Postgres to AI agent sandboxes
source: Databricks
url: https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes
model: claude-code/sonnet
generated_at: '2026-08-12T07:35:33.389294'
score: 90
---

📌 Electric 加入 Databricks：讓每個 AI Agent 都帶著自己的 Postgres

TL;DR：Databricks 收購 Electric，把 WASM Postgres（PGlite）與即時同步引擎帶進 AI agent sandbox。

當一個任務不再只有一個 agent，而是一整組 agent 在各自的 sandbox 裡平行工作時，共用一個中央資料庫的傳統架構就開始卡關：延遲高、狀態不同步、context 追不上彼此。Databricks 這篇公告說明了他們如何透過收購 Electric 來解決這個問題。

🤔 **Agent 不像傳統應用程式**

傳統應用程式的資料存取模式相對可預測，一個受管理的 Postgres 就能撐住整個系統。但 agentic 應用多了一個新的介面：agent 在解任務過程中會產生快速變動的 context，這些 context 需要低延遲的本地存取，同時又得跟其他 agent 共享一致的最新資訊。這是傳統集中式資料庫架構原本沒有設計要應付的情境。

🧩 **PGlite + Lakebase + 即時同步**

Electric 團隊打造的 PGlite，是一個小到可以直接跑在應用程式或 agent 本身裡面的 WASM Postgres 資料庫，可以部署在 agent sandbox、瀏覽器分頁或使用者裝置上，而不需要獨立的伺服器，藉此提供對本地 context 的極低延遲存取。而 Electric 的即時同步引擎，則負責把分散在各個 agent 之間的狀態持續同步回中央的 Lakebase，讓多個 agent 能在保有各自快速本地 context 的同時，安全地共享雲端的權威記錄（definitive record）。文中特別提到，這套同步架構同樣是 Google Docs、Figma、Notion 等協作類應用背後所採用的模式。

💡 **同源於 Postgres 的兩塊拼圖**

值得一提的是，PGlite 是建立在 Neon 共同創辦人 Stas Kelvich 早期 WASM Postgres 概念驗證的基礎之上，而 Electric 團隊把這個原型發展成如今每週有百萬等級專案在使用的可嵌入式 Postgres——PGlite 的每週下載量在過去十二個月內從 1M 成長到 13M。Electric 與 Lakebase 同樣以 Postgres 為底層技術，這次整合等於是把源自同一個構想的兩條分支重新接回同一家公司。

🎯 **實務啟示**

如果你正在設計多 agent 協作系統，這次整合釋出一個明確訊號：本地端輕量資料庫加上中央同步引擎，可能會成為 agent 基礎設施的標準組件，而不必再自己拼湊本地快取與同步邏輯。對已經在用 Databricks Lakebase 的團隊來說，未來把 PGlite 部署進 agent sandbox、再靠 Electric 的同步機制接回 Lakebase，會是值得關注的落地路徑。

🔗 **來源**
- 標題：Electric joins Databricks to bring WASM Postgres to AI agent sandboxes
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/electric-joins-databricks-bring-wasm-postgres-ai-agent-sandboxes

#Databricks #Electric #Postgres #PGlite #Lakebase #AIAgents #WASM #RealTimeSync #DistributedSystems #DataInfrastructure
