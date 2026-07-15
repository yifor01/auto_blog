---
title: earendil-works/pi
source: GitHub Trending
url: https://github.com/earendil-works/pi
score: 101
model: tencent/hy3:free
generated_at: '2026-07-15T08:05:36.825488'
---

📌 Pi 代理框架：自擴充套件編碼代理

TL;DR：Pi 提供統一多供應商 LLM API 與工具呼叫執行環境，助工程師建構自擴充套件編碼助手。

🎣 多數 AI 編碼工具繫結單一模型供應商，Pi 卻把 OpenAI、Anthropic、Google 等整合進同一套 API，還讓代理能自我擴充套件。

🤔 為何需要可自擴充套件的代理執行環境
Pi Agent Harness 是 self extensible coding agent 的專案首頁，提供開發者建構互動式編碼代理的基礎設施。對於想整合多模型、需要狀態管理與終端介面的開發者，此套件組合提供了從 API 到 UI 的基礎模組。專案目前對新貢獻者採嚴格管控：新 issue 與 PR 預設自動關閉，維護者每日審查自動關閉的專案。

🧩 四個核心套件組成模組化架構
README 將專案拆為數個獨立套件，各自負責不同層次：
- `@earendil-works/pi-ai`：統一多供應商 LLM API（OpenAI、Anthropic、Google 等）
- `@earendil-works/pi-agent-core`：具備 tool calling 與狀態管理的代理執行環境（agent runtime）
- `@earendil-works/pi-coding-agent`：互動式編碼代理 CLI
- `@earendil-works/pi-tui`：具備差異渲染的終端 UI 函式庫

此外，Slack/chat 自動化與工作流程被拆分至獨立倉庫 `earendil-works/pi-chat`，保持核心輕量。

💡 官網 demo 與自解釋 agent 降低上手門檻
雖然 README 未提供安裝指令，但指出學習途徑有三：造訪 pi.dev 專案網站觀看 demo、閱讀檔案，或直接讓 agent 解釋自身設計。這種「問代理本人」的作法呼應其自擴充套件理念。

⚠️ 預設無許可權沙箱，需自行容器化
Pi 並未內建限制檔案系統、程式、網路或憑證存取的許可權系統，預設以啟動使用者與程式的許可權執行。若部署環境需要更強邊界，README 建議自行容器化或沙箱化，並在 `packages/coding-agent/docs/containerization.md` 提供三種模式，例如 Gondolin extension：將 pi 與供應商認證留在主機，內建工具與 `!` 指令則路由至隔離環境（摘要內容於此截斷，細節待原文確認）。

🎯 匯入 Pi 時應優先設計容器化邊界
對工程師而言，若打算用 Pi 打造內部編碼助手，第一步不是接模型，而是規劃執行環境隔離。參考官方容器化模式，避免代理在預設許可權下誤改系統或洩漏憑證，才談得上生產可用。

🔗 **來源**
- 標題：earendil-works/pi
- 作者／機構：earendil-works
- 連結：https://github.com/earendil-works/pi

#AI #Agent #LLM #CodingAgent #OpenSource #MultiProvider #ToolCalling #PiAgent #SoftwareEngineering #GitHub
