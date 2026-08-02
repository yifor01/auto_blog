---
title: 'SpaceXAI Open-Sources Grok Build: The Rust Agent Harness, TUI, and Tool Layer
  Behind Its Coding CLI'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/15/spacexai-open-sources-grok-build-the-rust-agent-harness-tui-and-tool-layer-behind-its-coding-cli/
score: 94
model: tencent/hy3:free
generated_at: '2026-07-16T08:15:25.249031'
---

📌 【SpaceXAI 開源】Grok Build：Rust 打造的 AI 編碼代理框架與工具層

TL;DR：SpaceXAI 開源終端 AI 編碼代理 Grok Build，含 Rust 代理框架、TUI 與工具層，採 Apache 2.0。

AI 編碼助手不稀奇，但把整套 agent harness、終端 UI 與工具層用 Rust 寫出來並直接開源，還讓你完全本地端跑起來——這才是工程師會眼睛一亮的事。

🤔 **Grok Build 是什麼，解決什麼問題**

SpaceXAI 將其 grok CLI 背後的終端 AI 編碼代理 Grok Build 開源，原始碼已登上 GitHub，採 Apache 2.0 授權。它是一個能理解程式碼庫、編輯檔案、執行 shell 指令、搜尋網頁並管理長時間任務的代理，以全螢幕、支援滑鼠互動的 TUI（Terminal UI）形式運作。此專案早於 2026 年 5 月 25 日以早期 beta 推出。

🧩 **代理框架、TUI 與工具層的設計拆分**

README 指出，harness 是模型外的 scaffolding：負責組裝上下文、呼叫模型、解析回覆並分派 tool calls。SpaceXAI 列出四個已公開的領域：

- agent loop：上下文組裝、回應解析、tool-call 分派
- tools：代理如何讀取、編輯與搜尋程式碼
- terminal UI：渲染、輸入處理、plan 審閱與 inline diff viewer
- extension system：skills、plugins、hooks、MCP servers 與 subagents

這些領域對應到具名 crates，建議閱讀順序為先從 xai-grok-shell 看 loop，再讀 xai-grok-tools。

⚠️ **容易忽略的建置細節**

根目錄的 Cargo.toml 是自動生成的，README 明確說明應將其視為唯讀、不要手動改。

🎯 **能完全本地端跑起來的實務價值**

SpaceXAI 強調一項實際產出：Grok Build 現在可 fully local-first 運作。自行編譯後，指向本地推論（local inference），並從 config.toml 驅動所有設定；執行 `grok inspect` 會印出 harness 在當前目錄發現的內容，包含 config 來源、instructions、skills、plugins、hooks 與 MCP servers。對重視資料主權與離線開發的團隊，這比雲端綁定型 CLI 更有彈性。

🔗 **來源**
- 標題：SpaceXAI Open-Sources Grok Build: The Rust Agent Harness, TUI, and Tool Layer Behind Its Coding CLI
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/15/spacexai-open-sources-grok-build-the-rust-agent-harness-tui-and-tool-layer-behind-its-coding-cli/

#Rust #AIAgent #OpenSource #GrokBuild #SpaceXAI #TUI #CodingCLI #LocalFirst #AgentHarness #MCP
