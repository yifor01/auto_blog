---
title: ryoppippi/ccusage
source: GitHub Trending
url: https://github.com/ryoppippi/ccusage
score: 101
model: google/gemma-4-31b-it:free
generated_at: '2026-06-11T00:40:33.553754'
---

📌 **【GitHub Trending】用 AI Agent 寫 Code 很快，但你的 Token 帳單還在掌控中嗎？**

當我們在 Cursor、Claude Code 或 GitHub Copilot CLI 之間切換，追求最高效的編碼體驗時，最讓人不安的往往是後台不斷跳動的 Token 計費。尤其在使用多個 AI Agent 的開發流程中，很難精確掌握每天到底花在哪些工具上，以及成本分佈如何。

🤔 **開發效率提升了，但成本黑洞在哪裡？**

許多開發者在使用 AI 編程助手時，面臨的最大痛點不是 AI 不夠強，而是「缺乏統一的成本可視化」。目前的工具通常分散在各個平台的 Dashboard 中，要計算「本週總共花了多少錢」或「哪個 Agent 最耗資源」需要手動對帳，極其低效。

🧪 **一個輕量化的跨平台 Token 分析工具：ccusage**

由開發者 ryoppippi 開發的 `ccusage` 正是為了解決這個問題。它不透過複雜的 API 串接，而是直接讀取本地端（local data）的編碼代理 CLI 使用紀錄，將其轉換為直觀的成本報表。

🚀 **單一指令，橫跨多個主流 AI Agent 的成本分析**

`ccusage` 的強大之處在於其廣泛的支援度，幾乎涵蓋了目前市面上主流的 AI 編程助手：

- **主流大廠**：Claude Code, GitHub Copilot CLI, Gemini CLI
- **開源與新興 Agent**：OpenCode, Goose, OpenClaw, Kilo, Qwen, Kimi, pi-agent 等
- **其他工具**：Codex, Amp, Droid, Codebuff, Hermes Agent

只要輸入簡單的指令，就能快速產出不同維度的分析報表：
- `ccusage daily`：查看每日消耗
- `ccusage weekly`：查看每週趨勢
- `ccusage monthly`：查看每月總額
- `ccusage session`：分析單次對話的成本

💡 **無需安裝，即時分析的輕量化設計**

對於開發者來說，最討厭的就是安裝一大堆依賴。`ccusage` 提供了極其便捷的執行方式，推薦使用 `bunx` 或 `npx` 即可直接運行，無需全域安裝：

```bash
# 推薦使用 bunx 直接執行
bunx ccusage daily

# 或者使用 npx
npx ccusage@latest daily
```

這種設計讓開發者可以在需要對帳時快速啟動，分析完後不留下冗餘的環境垃圾。

⚠️ **依賴本地數據，僅限於支援的 CLI 工具**

需要注意的是，`ccusage` 是透過讀取「本地數據」來分析。這意味著它僅能分析那些會將使用紀錄儲存在本地的 CLI 工具。若某些工具完全將數據封裝在雲端且不提供本地紀錄，則無法被偵測。

🎯 **從「隨便用」轉向「精準用」的成本優化**

對於習慣使用多模態 AI 助手的工程師或團隊管理者，`ccusage` 提供了一個簡單的量化指標。透過分析 `session` 報表，你可以發現哪些任務在特定 Agent 上成本過高，進而優化你的 Prompt 策略或切換更經濟的模型，在維持產能的同時降低雲端開支。

🔗 **專案連結**
📝 ryoppippi/ccusage
👤 作者：ryoppippi
🔗 GitHub：https://github.com/ryoppippi/ccusage

你目前最常使用的 AI 編程助手是哪一個？你會擔心 Token 費用暴漲嗎？歡迎在下方分享你的成本管理心得 👇

#AI #GitHubTrending #LLM #TokenCost #ClaudeCode #Copilot #開發者工具 #成本優化
