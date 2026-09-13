---
title: 'AWS Introduces Pizza Bot: An Open Source Inbox for Background AI Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/13/aws-introduces-pizza-bot-an-open-source-inbox-for-background-ai-agents/
model: claude-code/sonnet
generated_at: '2026-09-13T19:34:46.815268'
score: 89
---

📌 AWS 開源 Pizza Bot：背景 Agent 的專屬收件匣

TL;DR：AWS 把內部用的背景 Agent 收件匣工具開源，統一管理完成結果與待審核決策。

當你的 Agent 在背景默默跑完一個小時的任務，結果要放哪裡？直接丟一堆訊息在聊天視窗裡顯然不夠用。AWS 開源的 Pizza Bot 給出的答案，是把這些結果整理成一個像 email 收件匣的介面。

🤔 **從 Amazon 內部 2,000+ 人用到開源專案**

Pizza Bot 是一個自架應用，專門處理「使用者去做別的事時，AI 任務仍在背景繼續跑」的場景，把已完成的結果與待決策事項整理進一個 email 風格的收件匣。早期版本已在 Amazon 內部服務超過 2,000 人，用於會議準備、email 草稿、Slack 摘要、CRM 紀錄與研究工作，這次公開發布的版本是重新打造後的開源專案，程式碼採 Apache 2.0 授權。

🧩 **收件匣式介面加上多客戶端架構**

Pizza Bot 提供 macOS、Windows、Linux 桌面版，以及連接本機或獨立後端的瀏覽器版與終端機客戶端。任務被分成三類：All（完整對話紀錄）、Unread（等待審閱的已完成工作）、Action（暫停等待核準或回覆的工作），使用者可以把對話串整理進資料夾，並在 Activity 面板檢視被委派出去的 worker。任務可以手動啟動、透過 cron 排程，或透過 webhook 觸發，排程由伺服器端統一掌管，即使斷線一段時間，錯過的 cron 區間也只會補跑一次而非逐一重播，觸發紀錄會被持久化保存。技術架構上，Pizza Bot 用 DeepAgents 與 LangGraph 處理有狀態的執行流程，一個 Hono API 伺服器負責執行與儲存；Electron 桌面版與瀏覽器版共用同一套 React 介面，所有客戶端透過 HTTP 與 server-sent events 與伺服器溝通。LangGraph 的 checkpoint 機制保留對話狀態與核准暫停點，另外還有獨立的 SQLite 儲存跨對話記憶與應用程式中繼資料，客戶端重新連線後可以重播緩衝的事件。值得注意的是，關閉對話串或中斷客戶端連線並不會停止伺服器上正在跑的任務，但如果直接退出桌面應用程式，會連帶關閉內嵌的伺服器並終止正在執行的任務，checkpoint 雖然會保留對話狀態，但進行到一半的步驟可能會遺失，所以要讓任務在桌面應用關閉後持續運作，需要一個常駐的後端。

🧩 **多模型供應商加上細緻的授權控管**

Pizza Bot 支援 Amazon Bedrock、Anthropic、Google Gemini、OpenAI、OpenRouter 與 Ollama，使用前需在 Settings > Providers 設定好供應商。Agent 本身具備 scratch-file 操作能力，以及一個沒有網路與主機檔案系統存取權限的沙箱化 JavaScript 直譯器；當有已就緒的 skill worker 時，可以透過 task 機制把工作委派出去。檔案系統層另外支援明確的資料夾授權與持久性記憶，MCP 伺服器則用來對外暴露工具。每個 SKILL.md 定義一個 worker 的指令與有範圍限制的工具存取權限，只有在其宣告的依賴都存在時，該 skill 才能被呼叫；既有的 Claude Code 相容 `.mcp.json` 設定可以直接沿用，外掛（plugin）也能把 skill 與 MCP 伺服器打包在一起。Skill 作者可以透過 `interruptOn` 與 `allowedDecisions` 設定，要求特定工具在執行前必須經過核准，使用者依照這個政策可以核准、編輯提議的參數，或直接拒絕該動作，這些控管都需要針對相關工具事先設定好才會生效。

🎯 **實務啟示**

Pizza Bot 示範的是一個具體的「AI 收件匣」範例場景：先啟動一份研究簡報，接著關閉桌面應用讓任務繼續跑，過程中若自訂 skill 用 `interruptOn` 卡住了發布動作，之後重新打開桌面應用就能在收件匣裡審閱結果。對想串接背景 Agent 到日常工作流的工程師來說，這個架構把「常駐後端 vs. 桌面端」的取捨與「哪些動作需要人工核准」都做成了明確的設定項，值得作為自建類似系統時的參考起點。

🔗 **來源**
- 標題：AWS Introduces Pizza Bot: An Open Source Inbox for Background AI Agents
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/13/aws-introduces-pizza-bot-an-open-source-inbox-for-background-ai-agents/

#AWS #PizzaBot #OpenSource #AIAgents #LangGraph #DeepAgents #MCP #AgenticAI #DeveloperTools #Automation
