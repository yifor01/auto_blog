---
title: warpdotdev/warp
source: GitHub Trending
url: https://github.com/warpdotdev/warp
score: 97
model: tencent/hy3:free
generated_at: '2026-07-19T08:04:03.027364'
---

📌 【warpdotdev】Warp 開源：從終端機長出的 agentic 開發環境

TL;DR：Warp 開源使用者端程式碼，內建 coding agent 並支援自帶 CLI agent，可觀看 Oz 代理協作。

你用的終端機，現在可能不只是跑指令的地方，而是一個會自己 triage issue、寫 spec、review PR 的 agentic 開發環境。Warp 把整個客戶端程式碼庫開源了，而且背後的 agentic 管理工作流是由 GPT 模型驅動。

🤔 **從終端機演化的 agentic 開發環境**

Warp 定位為「agentic development environment」，起源於終端機。開發者可以使用 Warp 內建的 coding agent，也可以帶入自己的 CLI agent，例如 Claude Code、Codex、Gemini CLI 等。README 指出，OpenAI 是新開源 Warp 儲存庫的創始贊助者，新的 agentic 管理工作流由 GPT 模型提供動力。

🧩 **Oz 代理如何協作開源維運**

在 build.warp.dev 的儀錶板中，可以觀察到數千個名為 Oz 的 agents 執行以下任務：
- triage issues（分類與處理問題回報）
- 撰寫 specs（規格檔案）
- 實作變更
- review PRs（審查拉取請求）

使用者也能檢視頂級貢獻者、進行中的功能，並用 GitHub 登入追蹤自己的 issue，或點進正在運作的 agent session（以網頁編譯的 Warp 終端機呈現）。

💡 **Oz for OSS 夥伴計畫**

對於維護熱門開源專案的主理人，Warp 提供 Oz for OSS 合作計畫：申請 Oz credits 後，可將本儲存庫使用的 agentic 開源管理流程帶到合作的 repo。README 說明，Warp 會直接與 maintainers 合作，實作適合各專案的 issue triage、PR review、社群管理與貢獻者協調工作流。

⚠️ **授權與程式碼範圍須留意**

Warp 的 UI 框架（warpui_core 與 warpui crates）採用 MIT 授權；本儲存庫其餘程式碼則採 AGPL v3 授權。客戶端程式碼庫已開源並存放於此 repo，且專案表示歡迎貢獻，但具體的貢獻流程細節在摘要中未完整提及。

🎯 **實務啟示**

如果你在維護開源專案，Warp 展示了一種可觀察、可帶入自有 agent 的協作模式：先用內建 Oz 流程降低 triage 與 review 負擔，再評估是否透過 Oz for OSS 將類似工作流移植到自己的 repo。對工程師而言，也可直接下載 Warp，把熟悉的 CLI agent 接進去，體驗 agentic 終端機的開發方式。

🔗 **來源**
- 標題：warpdotdev/warp
- 作者／機構：warpdotdev
- 連結：https://github.com/warpdotdev/warp

#Warp #AgenticDevelopment #OpenSource #Terminal #Oz #GPT #ClaudeCode #Codex #GeminiCLI #PRReview
