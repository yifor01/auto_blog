---
title: HKUDS/nanobot
source: GitHub Trending
url: https://github.com/HKUDS/nanobot
score: 93
model: tencent/hy3:free
generated_at: '2026-07-16T08:16:22.348089'
---

📌 【HKUDS 開源】nanobot：可自架、輕量的個人 AI 代理執行環境

TL;DR：nanobot 是開源輕量個人 AI agent 框架，含 WebUI、工具、記憶體與多通道整合。

想自己擁有一套能長期跑任務、連多種聊天軟體、還能自架的 AI 代理，但不想被綁死在封閉平臺？HKUDS 推出的 nanobot 把代理核心做得小而可讀，同時把實務需要的零件一次打包。

🤔 **為什麼需要可自有的個人 AI agent**

nanobot 定位為 self-hosted 的個人 AI agent runtime（執行環境），強調「open-source、ultra-lightweight、you can truly own」。它把 agent core 保持小巧且可讀，同時提供真實長時間任務所需的實用模組：WebUI、聊天通道、tools、memory、MCP、model routing、automation 與 deployment。

🧩 **核心能力與設計取向**

README 指出 nanobot 能做的事包括：

- 在瀏覽器 WebUI 或終端機中執行
- 連線 Telegram、Discord、Slack、WeChat、Email、Mattermost 等聊天應用
- 使用 tools：files、shell、web search、web fetch、MCP、cron、image generation、subagents
- 透過 Dream 機制保留 session history 與 long-term memory
- 執行 long-horizon goals 與排程自動化
- 提供 Python SDK 與 OpenAI-compatible API 供整合
- 部署為長時間運作的本地或伺服器端 agent gateway

🎯 **不同背景使用者的上手路徑**

專案提供分眾入口，降低門檻：

- 無終端機／設定背景：Start Without Technical Background
- 想快速裝好並取得一次 CLI 回覆：Install and Quick Start
- 想開啟內建瀏覽器 UI：WebUI
- 想接 Telegram、Discord 等聊天應用：Chat Apps
- 想設定 providers、fallback models、Langfuse、MCP、web tools 或安全選項：Docs and Configuration
- 想理解或擴充內部：Architecture and Development

⚠️ **最新版本與已知範圍**

最新釋出為 v0.2.2「Durability Release」，重點包含：Segmented WebUI transcripts、Python SDK runtime controls、Automation management。素材未提及效能基準、支援模型清單細節或具體部署規格，實際規模需參考倉庫後續檔案。

🎯 **實務啟示**

對想自架個人助理的 AI/ML 工程師，nanobot 提供了一個模組齊全且強調可讀核心的起點：可用 WebUI 或 CLI 快速試跑，再透過 Python SDK 與 OpenAI-compatible API 接進現有系統；若需要多聊天通道與長期記憶，也可直接沿用其內建機制，減少從零組裝的成本。

🔗 **來源**
- 標題：HKUDS/nanobot
- 作者／機構：HKUDS
- 連結：https://github.com/HKUDS/nanobot

#AI #Agent #OpenSource #SelfHosted #nanobot #HKUDS #WebUI #MCP #PythonSDK #Automation
