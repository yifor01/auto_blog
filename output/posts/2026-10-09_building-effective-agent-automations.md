---
title: Building effective agent automations
source: Claude Blog
url: https://claude.dev/blog/building-effective-agent-automations/
model: claude-code/sonnet
generated_at: '2026-10-09T21:47:16.116915'
pinned: true
---

📌 【Anthropic 官方指南】讓排程 AI 代理不再悄悄失靈

TL;DR：Claude Managed Agents 參考實作教你打造會記錄進度、會老實說「這次沒讀到什麼」的排程代理。

排程代理最怕的不是明顯報錯，而是「悄悄」出錯：存取權限過期了沒人發現，使用者的偏好設定沒被遵守，結果往往要等到有人發現漏訊才會察覺。這正是 Anthropic 這篇文章想解決的問題。

🤔 **背景：簡單的自動化，難做得「穩」**

Anthropic 在文中指出，隨著 AI 加速工作節奏，團隊越來越常靠簡單的 agent automation（依排程在背景蒐集資訊、主動回報重點）來跟上進度。但這類自動化很難做得可靠：代理可能悄悄失去某個資料來源的存取權卻沒人發現，或是沒有遵循使用者的偏好設定。

🧩 **六個元件撐起一套參考實作**

Anthropic 用 Claude Managed Agents（beta）打造了一個參考實作，定期讀取像 Slack 頻道、GitHub pull request 這類自訂來源，追蹤「從上次執行後有什麼變化」，再把結果寫到指定的目的地（如 Slack）。整套設計拆成六個元件：

- **Sources（來源）**：列出要讀取地點的清單，預設是 Slack 頻道與 GitHub PR，清單放在使用者的偏好設定檔裡，可擴充到其他來源。
- **Destination（目的地）**：代理可以寫入的地方，範例是固定發到某個 Slack 頻道，每次執行發一篇帶日期的貼文。
- **Agent（代理本體）**：agent.md 裡定義的模型、工具與執行步驟，每次執行照步驟跑完就停止。
- **Schedule（排程）**：用 cron 排程定期觸發，整個流程跑在 Anthropic 的基礎設施上，不需要使用者的機器保持開機。
- **Memory（記憶）**：使用者的偏好設定，以及代理自己的書籤、帳本、筆記與執行紀錄。
- **Guardrails（防護機制）**：凡是只讀取的地方一律設為唯讀權限，且每次執行設有花費上限。

在憑證管理上，Managed Agents 把真正的密鑰放在 vault 裡，跑在沙盒之外：呼叫 GitHub 走 MCP server，由沙盒外的 proxy 依網址比對找出對應憑證；呼叫 Slack 則是在沙盒內用 bash 搭配 curl，沙盒裡只會看到像 $SLACK_BOT_TOKEN 這樣的佔位符，請求離開沙盒時才會被平臺換成真正的 token，且只換給允許的網域。

針對「讀取窗口」，文章點出一個常見錯誤：如果代理每次只抓「過去 24 小時」，執行得晚會漏東西，執行得早又會重複回報。參考實作改用「書籤」機制：每個來源各自記錄「讀到的最新一筆項目的時間戳」，存在跨執行保留、且每次執行都會掛載進沙盒的記憶體資料夾 /mnt/memory/ 裡，下一次執行就從書籤接續讀取，窗口會隨上次執行時間自動伸縮。

文章也處理「讀取失敗」與「誤判沒新消息」之間的落差：如果某個 MCP server 當掉或 token 過期，這次執行依然會啟動，只是少了那個來源的工具，而代理看不到任何來自那個來源的內容就可能誤報「沒有新消息」。agent.md 裡訂了三條規則來避免這個問題：來源失敗時書籤原地不動、用其他來源的內容照常發出當次簡報、並在簡報最後加一行寫明「這次讀不到哪個來源」，讓讀者知道有缺漏。

在「確認貼文真的送出」這件事上也有一套防呆設計：代理會先檢查頻道最近的訊息裡是否已經有今天的標題，避免重複發文；貼文只有在 Slack 回傳 "ok": true 並帶出訊息 ts 時才算真正送出；帳本與書籤也只有在確認送出後才會更新。如果結果不明確，代理會把這次執行標記成「可能已發送」，其他狀態維持不變，避免漏報或重複發送。代理在記憶體裡替每次執行留一筆紀錄，狀態依序標記成「發文中」「已發文（含訊息 ID）」或「可能已發文」。

怎麼用：這個參考實作需要先準備一個 Slack app（可用提供的 manifest 建立）與一個 GitHub token。設定檔包含 agent.md（模型、工具、指令）、deployment.md（排程、時區、預算、輸入訊息）、environment.yaml（網路白名單）、兩個 memory_store yaml 檔（偏好設定與狀態）、vault.yaml（憑證所在的 vault），以及 claude-lock.json（寫入資源 ID 的記錄檔）。流程上先用 ant apply vault.yaml 建立 vault，再用 TypeScript SDK 把像 Slack bot token 這樣的憑證加進 vault，然後把 vault ID 填進 deployment.md 裡。文中也提到可以在 Claude Code 裡執行一行指令，透過 claude-api skill 依本文說明互動式完成設定。

⚠️ **目前仍是 beta**

Anthropic 把 Claude Managed Agents 標註為 beta，功能與設定方式仍可能調整。整套設計目前也只示範了 Slack 與 GitHub 兩種來源，接其他系統需要自己擴充。

🎯 **實務啟示**

如果你也在打造會定期執行、會主動回報的 AI 代理，這篇文章提供三個值得直接套用的工程模式：一是用「每來源書籤」取代「固定時間窗口」，避免漏訊或重複回報；二是貼文前先查重、送出後才更新狀態記錄，確保一次執行只對應一次結果；三是讓失敗的來源「靜音但不裝沒事」，在簡報裡老實寫出哪裡沒讀到，而不是讓讀者誤以為今天真的沒事發生。

🔗 **來源**
- 標題：Building effective agent automations
- 作者／機構：Anthropic
- 連結：https://claude.dev/blog/building-effective-agent-automations/

#Anthropic #Claude #AIAgents #Automation #MCP #AgenticAI #DevOps #Slack #GitHub #ManagedAgents
