---
title: Vercel Open-Sources durable-harness for Crash-Proof Coding Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/21/vercel-durable-harness-crash-proof-coding-agents/
model: claude-code/sonnet
generated_at: '2026-10-22T20:56:53.767915'
score: 88
---

📌 Vercel 開源 durable-harness，讓 Coding Agent 當機後接著跑

TL;DR：Vercel 開源 durable-harness，讓雲端 coding agent 在當機或逾時後仍能從斷點繼續工作。

🎣 一個 function 當掉，過去意味著一整段 agent 工作白做。Vercel 這次開源的工具，想解決的正是這個落差。

🤔 為什麼本地好用的 coding agent，搬上雲端就「失憶」

像 Pi、Claude Code 這類 coding agent harness，原本設計成長時間在本機執行的 process，session 狀態留在記憶體裡。在本機，workspace 和歷史紀錄在同一顆磁碟上，重新接續對話只需要再給一個 prompt。但把這些 agent 搬到雲端 VM 跑，就算用了持久化儲存，VM 本身並不會追蹤哪些呼叫已經完成。Vercel 團隊在公告中指出，一次失敗的 turn 或網路錯誤，就足以讓整段工作遺失。

🧩 把 session 寫進 Workflow SDK 的「World」

durable-harness 是一組 adapter，把既有的 harness（包含 Pi、OpenCode、Claude Code 與 Codex）包裝起來，不需要修改這些 harness 本身。它使用 Vercel Workflow SDK 背後的同一套機制，把每個 session 存進一個「World」，也就是把儲存、佇列（queue）與串流（stream）包在同一介面下的容器。

具體寫入方式是：在每次呼叫模型或工具之前，先記錄一個「意圖（intent）」；呼叫完成後，再記錄「結果（outcome）」。每個 turn 都由 Vercel Queues 上的一則訊息支撐；如果執行的 function 當掉，佇列會把這個 turn 交給一個新的 function，新 function 讀取 log 後接著做。當機之後，log 會清楚顯示哪些步驟已完成、哪些正在執行、哪些還沒開始。

harness 本身的 session 檔案也會被鏡射進這份 log，包括 Claude Code 的 transcript、Codex 的 rollout，以及 OpenCode 的 event store。模型選擇要執行的指令，不會直接跑在該 function 自己的磁碟上；文件列出三種 workspace 選項供選擇。另外，像待辦清單這類結構化的 JSON 文件也會存進 log，單一文件上限 64 KB。

🎯 兩個環境變數就能換儲存後端

對寫 agent 的開發者來說，好消息是程式碼在不同 World 之間保持一致：只要切換 WORKFLOW_TARGET_WORLD 與 WORKFLOW_POSTGRES_URL 這兩個環境變數，就能把同一個 agent 的儲存後端換成 Postgres，不用改動 agent 邏輯本身。

這解決的是一個很具體、很多團隊正在踩的痛點：把 coding agent 從個人筆電搬進雲端跑長任務時，缺乏「斷點續跑」的機制。對正在建置雲端 agent 基礎設施的團隊，durable-harness 提供了一個不需要重寫既有 harness 就能補上持久化的路徑，值得納入架構評估。

⚠️ 畢竟是封裝層，仍依賴底層 harness 的 session 格式

由於 durable-harness 的做法是鏡射既有 harness 的 session 檔案（transcript、rollout、event store），它的相容性仍綁定在這些 harness 既有的儲存格式上；一旦底層 harness 改變了 session 的內部結構，mirror 機制可能需要同步調整。

🔗 來源
- 標題：Vercel Open-Sources durable-harness for Crash-Proof Coding Agents
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/21/vercel-durable-harness-crash-proof-coding-agents/

#Vercel #CodingAgent #OpenSource #WorkflowSDK #AIAgent #DeveloperTools #CloudComputing #ClaudeCode #Codex #SoftwareEngineering
