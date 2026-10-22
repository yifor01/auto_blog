---
title: 'Show HN: Omnara – Open-source alternative to Claude Managed Agents'
source: Hacker News
url: https://github.com/omnara-ai/omnara
model: claude-code/sonnet
generated_at: '2026-10-22T21:01:34.686803'
score: 86
---

📌 Claude Managed Agents 的開源版：Omnara 讓 Agent 永不斷線

TL;DR：Omnara 是開源持久代理框架，用 Postgres 存狀態、無狀態 worker 跑迴圈，Agent 閒置免費、不怕斷線。

如果你用 Claude Code 或 Codex 跑過長時間任務，應該都遇過這個痛點：筆記型電腦一闔上，Agent 就斷了。Omnara 團隊一開始做的是遠端操控本機 Claude Code 的手機 App，後來發現問題的根源不是「遠端操控」，而是 Agent 本來就該活在雲端。

🤔 **從遠端控制筆電，到讓 Agent 住進雲端**

在 Hacker News 的 Show HN 貼文中，Omnara 團隊說明他們最早做的是透過 relay 遠端控制跑在筆電上的 Claude Code / Codex 的手機 App。這個架構的問題很直接：筆電關機，relay 就跟著斷線；若想搬到雲端 sandbox，又得處理程式碼與 Agent 狀態在機器間同步的麻煩。Anthropic 與 OpenAI 都在推出各自的代管版本（Claude Managed Agents、OpenAI Agents API），而 Omnara 要做的是一個可以自架、可以換模型的開源版本。

🧩 **把 Agent 狀態全部搬進 Postgres**

和多數 harness（Claude Code、Codex、OpenCode、Pi、Goose 等）把整個 Agent loop 放在單一長駐 process、log 寫進 JSONL 或 SQLite 不同，Omnara 把每一次 model call 或工具呼叫都當作型別化的 row 寫進 Postgres 的 append-only event log。Agent loop 本身跑在無狀態的 control-plane worker 上：一個 worker 執行一次迴圈（可能是一次模型呼叫，也可能是它產生的工具呼叫），寫完就釋放這個 agent，並把下一次迴圈排進 Postgres 佇列，由任何空閒的 worker 接手。每次迴圈的結果（模型輸出、工具呼叫、用量、下一次喚醒時間）都在同一個 transaction 內一起提交；worker 若中途掛掉，交易不會提交，租約到期後由另一個 worker 重試。等待使用者、工具或重試中的 Agent 不會佔用 worker，因此一個 worker 可以多工處理數千個 Agent。

另一個關鍵設計是「執行環境」與「控制平面」分離：跑 Agent loop 的 worker 機器，並不是實際執行指令的機器。任何一臺裝了 omnarad 這個小型 daemon 的 macOS 或 Linux 機器（可以是筆電，也可以是雲端 sandbox）都能主動連出到 Omnara，不需要開任何入站埠。一個 Agent 可以同時連接多臺機器，作者舉例：筆電開著時 Agent 在筆電上寫程式碼並推上 GitHub，闔上筆電後，Agent 偵測到筆電離線，自動把最新的程式碼 pull 到雲端 sandbox 繼續執行。

🧩 **怎麼用**

Omnara 提供標準的 harness 功能：檔案與 shell 工具、subagent、compaction、permission prompt、MCP、skills、memory 等。整套程式碼在 GitHub 上開源，可以用 docker compose 在單一機器上自架，也有提供 hosted 版本（omnara.com）。

🎯 **實務啟示**

對於要長期運行、跨裝置協作的 Agent 任務，這種「狀態存在資料庫、迴圈跑在無狀態 worker、執行環境可插拔」的設計值得參考，它把持久性、擴展性和執行環境的綁定問題都拆開處理了。如果你正在設計多 Agent 排程系統，這套用 Postgres 做 event log 加租約／重試的模式，比把所有狀態塞進單一 process 更穩健。

🔗 **來源**
- 標題：Show HN: Omnara – Open-source alternative to Claude Managed Agents
- 作者／機構：kmansm27（Omnara）
- 連結：https://github.com/omnara-ai/omnara

#OpenSource #AIAgents #Postgres #DevTools #ClaudeCode #Codex #AgentOrchestration #CloudComputing #Automation #SoftwareEngineering
