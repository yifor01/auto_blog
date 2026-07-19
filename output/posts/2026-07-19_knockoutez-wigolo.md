---
title: KnockOutEZ/wigolo
source: GitHub Trending
url: https://github.com/KnockOutEZ/wigolo
score: 99
model: tencent/hy3:free
generated_at: '2026-07-19T08:02:27.549073'
---

📌 【開源專案】wigolo：讓 AI 代理擁有本地優先的網頁操作層

TL;DR：wigolo 提供無金鑰、免雲端、不計費的本地網頁工具集，直接接上你的 coding agent。

🎣 開場鉤子
當 AI 代理每次搜尋、爬取網頁都要繫結 API 金鑰、擔心雲端費用飆漲，KnockOutEZ 推出的 wigolo 反其道而行：所有資料留在本地，用量再大也不會收到帳單。

🤔 為誰解決什麼問題
wigolo 鎖定使用 AI agent 的開發者與自架代理的團隊，目標是給 agent 一個「耐用介面（durable surface）」處理所有網頁相關任務——包含 search、fetch、crawl、extract、cache、find-similar、research，以及 autonomous gather loops。它強調 local-first：不需要 API keys、不連雲端、不按量計費，且任何被讀取的內容都不會離開 ~/.wigolo/ 資料夾。

🧩 核心設計與部署方式
README 指出 wigolo 的架構彈性，能跑在 agent 所在的位置：
- 作為 MCP server 貼著你的 coding agent 跑
- 作為 REST/MCP endpoint 放在自架 agent 的機器上
- 透過 SDK 嵌入你自己的應用程式內

它宣稱可相容 Claude Code、Cursor、Codex、Gemini CLI、VS Code、Windsurf、Zed、Antigravity 等工具，也支援 LangChain、CrewAI、LlamaIndex、Vercel AI SDK、n8n 與任何 MCP client，或單純用 REST 呼叫。

🎯 怎麼用：一條指令完成接線
環境需求為 Node ≥ 20 與約 1.5 GB 可用磁碟空間，支援 macOS、Linux、Windows。
執行以下指令即可將本地引擎接進 agent：
`npx wigolo init --agents=<your-agent>`
其中 `<your-agent>` 可逗號分隔填入 claude-code、cursor、codex、gemini-cli、vscode、windsurf、zed、antigravity 等。

作者說明 `init` 指令預設無互動（unattended），適合指令碼與 CI 環境；它會一次性完成：下載瀏覽器引擎與裝置端模型（on-device models）、執行健康檢查、印出各元件狀態摘要，讓設定問題在第一次呼叫前就暴露，而不是靜默失敗。wigolo 會寫入對應的 MCP 設定檔。

🎯 實務啟示
對在意隱私與成本的工程師，wigolo 提供一個可本地部署、免金鑰的網頁工具層，適合在 CI 或自架 agent 管線中取代需雲端金鑰的爬蟲／檢索方案。先從 `npx wigolo init` 接上日常用的 coding agent，評估本地模型在 extract 與 research 任務上的實用度。

🔗 來源
- 標題：KnockOutEZ/wigolo
- 作者／機構：KnockOutEZ
- 連結：https://github.com/KnockOutEZ/wigolo

#AIagents #MCP #localfirst #webintelligence #opensource #privacy #nodependency #CLI #selfhosted #RAG
