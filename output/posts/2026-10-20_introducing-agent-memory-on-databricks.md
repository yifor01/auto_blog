---
title: Introducing Agent Memory on Databricks
source: Databricks
url: https://www.databricks.com/blog/introducing-agent-memory-databricks
model: claude-code/sonnet
generated_at: '2026-10-20T20:47:10.841430'
score: 96
---

📌 Databricks 把 MemCurrent 做成產品:Agent Memory 開放 Beta

TL;DR:Databricks 在 Agent Bricks 推出 Agent Memory,把研究中的 MemCurrent 架構產品化,內部測試通過率翻三倍、token 省 31%。

研究論文裡的架構很漂亮,但多數團隊自己動手做記憶系統時,第一個卡關的問題永遠是:記憶要存在哪裡、怎麼整理、怎麼取回。Databricks 這次直接把答案做成了平臺功能。

🤔 **沒有記憶,agent 會不斷犯一樣的錯**

Agent 一旦從 demo 走到日常使用,馬上會冒出兩個問題:忘記使用者偏好、重複犯已經被糾正過的錯誤。許多開發者因此自己動手刻記憶系統,卻會一路卡在「記憶該存哪、怎麼合成、怎麼取回」這些設計決策上。Databricks 想提供的,是「同時讓 agent 更便宜、更懂使用者」的記憶功能,而不需要團隊另外再搭一套系統。

🧩 **建在 Lakebase 上的 MemCurrent 產品化版本**

Agent Memory 今天在 Agent Bricks(Databricks 的 agent 開發平臺)上以 Beta 形式開放,跑在 Lakebase(Databricks 的 serverless Postgres)之上,確保記憶的存取延遲夠低、能隨 agent 流量擴展。它的底層就是 Databricks Research 提出的 MemCurrent 架構,結合三種存取模式:plugin 自動記錄與載入 context、agent 可隨時呼叫的 tool,以及在背景整理記憶的離線「dreaming」pipeline。實際運作上,agent 會把每輪對話附加到受管理的 session 中,直接呼叫工具存取記憶,再由背景的記憶 pipeline 把 session 提煉成長期記憶,整套流程都跑在你工作區內、由 Databricks 代管的 Lakebase 上。

同一套底層架構,目前已經在為 Genie(Databricks 的自然語言商業使用者體驗)提供記憶功能。

📊 **內部基準:通過率翻三倍,token 少 31%**

Databricks 研究團隊的核心發現是:記憶最好分兩層運作 — 一層是「發生過什麼」的原始紀錄,一層是「值得記住什麼」的提煉紀錄,並由背景流程持續保持最新,而非讓 agent 在任務中隨手寫入。這樣設計下,品質與效率可以同時改善:在內部的企業資料任務基準上,有記憶的 agent 通過的任務數量大約是沒有記憶時的三倍,完成得更快,用的 token 也更少。

🎯 **對想要落地記憶功能的團隊的啟示**

這個功能不需要在使用者端另外佈建基礎設施:透過 Agent Bricks CLI,幾分鐘內就能部署一個帶記憶與 session 功能的 agent,之後每次與特定使用者的新對話,都會從上次學到的東西繼續接續。Agent Memory 只是 Agent Bricks 平臺的一部分,其餘還包含 agent hosting、Databricks Sandbox、Unity Gateway、預建的 MCP 伺服器,以及追蹤與評估工具,提供建置正式環境 agent 所需的完整基礎設施。對已經在用 Agent Bricks,或正在評估企業 agent 平臺的團隊來說,這是一個值得納入選型清單的現成選項。

🔗 **來源**
- 標題:Introducing Agent Memory on Databricks
- 作者/機構:Databricks
- 連結:https://www.databricks.com/blog/introducing-agent-memory-databricks

#AgentMemory #Databricks #AgentBricks #Lakebase #LLMAgents #EnterpriseAI #MemCurrent #ProductionAI #AIInfrastructure #MachineLearning
