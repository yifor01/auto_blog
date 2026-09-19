---
title: Claude Code now reads AGENTS.md if there is no Claude.md
source: Hacker News
url: https://code.claude.com/docs/en/changelog
model: claude-code/sonnet
generated_at: '2026-09-19T19:30:04.899107'
score: 82
---

📌 【Anthropic】Claude Code 沒有 CLAUDE.md 時，改讀 AGENTS.md 了

TL;DR：Claude Code 新版在專案缺少 CLAUDE.md 時會自動改讀 AGENTS.md，同一週也悄悄調整了 auto mode 的分類器計費方式。

每次啟動 AI coding agent，它得先搞清楚這個專案的規矩：用什麼框架、怎麼測試、哪些檔案碰不得。這份「專案說明書」過去在 Claude Code 裡只認 CLAUDE.md 一種格式，9 月中的兩次更新，替這件事開了一道備援。這則消息在 Hacker News 拿下 709 分、262 則留言，討論熱度不小。

🤔 **從單一格式到有備援的專案指示**

Claude Code 官方 changelog 顯示，2.1.277 版（9 月 18 日）新增了 AGENTS.md 支援：當專案目錄裡沒有 CLAUDE.md 時，Claude Code 會改讀 AGENTS.md 作為專案指示來源，判斷邏輯可以理解為「CLAUDE.md 不存在 → 讀取 AGENTS.md」。這項行為可以在 `/config` 的「Project instructions」底下調整，但目前 Bedrock、Vertex、Foundry 這三個平臺還不支援。

隔天的 2.1.278 版則調整了 auto mode 的計費方式：針對 Claude API、Enterprise 用戶，以及跑在 Bedrock、Vertex、Foundry 和各種 gateway 上的部署，auto mode 預設改用 server-side classifier，且不再針對這個分類器本身的運算收費。想退出這個預設行為的 Bedrock/Vertex/Foundry/gateway 用戶，可以設定 `CLAUDE_CODE_AUTO_MODE_SERVER=0`；如果最終還是退回計費的 fallback 路徑，系統會跳出警告。`/status` 面板也新增一列，顯示當前 session 的 auto mode 分類器究竟跑在 server 端還是本機。

💡 **一長串穩定性修復，比新功能更值得留意**

這兩版加起來還修了相當多穩定性問題，例如：`claude -p` 與 Agent SDK 在內部錯誤後可能卡住不回應的狀況、`--resume` 後某些對話會因為空的文字區塊而整段請求失敗、Edit 工具在處理非 ASCII 字元時誤判跳脫字元、以及 Grep/Glob 在系統資源不足時直接回報「找不到結果」而非明確錯誤。對長時間在終端機裡跑 agent 的工程師來說，這類修復雖然不起眼，但直接影響日常使用的穩定度。

⚠️ **這是例行更新，不是架構級突破**

整體來看，這兩版沒有帶來新的模型能力或架構變化，本質上是相容性與計費機制的微調，加上一批 bug 修復。AGENTS.md 支援也還沒覆蓋所有雲端平臺。

🎯 **實務啟示**

如果團隊本來就已經為其他 agent 工具維護 AGENTS.md，現在可以不用重複寫一份 CLAUDE.md；若使用 API/Enterprise 或雲端閘道部署，建議留意 `/status` 裡新增的 auto mode 欄位，確認自己是否吃到 server-side classifier 的免費分類額度。

🔗 **來源**
- 標題：Claude Code now reads AGENTS.md if there is no Claude.md
- 作者／機構：datadrivenangel（Hacker News）
- 連結：https://code.claude.com/docs/en/changelog

#ClaudeCode #Anthropic #AIAgents #DeveloperTools #AGENTSmd #LLMTooling #CodingAssistant #DevOps #SoftwareEngineering #AIProductivity
