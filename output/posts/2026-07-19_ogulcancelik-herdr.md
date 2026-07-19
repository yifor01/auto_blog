---
title: ogulcancelik/herdr
source: GitHub Trending
url: https://github.com/ogulcancelik/herdr
score: 102
model: tencent/hy3:free
generated_at: '2026-07-19T08:02:00.244516'
---

📌 【開源專案】herdr：終端機裡的 agent 多工管理器

TL;DR：herdr 是純 Rust 寫的終端 agent 多工器，讓多個 AI agent 在分頁中各自執行、可隨時 detach 重連。

在終端機裡同時盯著好幾個 AI agent 跑任務，畫面切來切去、一關視窗就全停——這大概是很多工程師的日常痛點。herdr 宣稱能把這件事變簡單：所有 agent 的狀態一眼看盡，而且離線也不中斷。

🤔 **解決什麼問題、為誰而做**

herdr 定位為「agent multiplexer」，活在終端機裡。它要解決的是：當你同時跑多個 agent，很難一眼掌握誰卡住、誰在動、誰做完了。README 指出，它提供真實的終端檢視（real terminal views），而非包裝過的轉譯介面；並且支援 detach 後 agent 繼續跑，可從任何終端機甚至透過 ssh 重新連回來，session 在重啟後也還在。

🧩 **核心架構與設計理念**

- 單一 Rust 二進位檔，沒有 Electron，直接跑在你既有的終端機裡。
- agent 也能用 herdr：提供純 socket API，agent 可以自己開分頁（pane）、讀輸出、互相等待。
- 操作方式同時給「鍵盤與滑鼠」一等公民地位：tmux 風格的 prefix 快捷鍵，以及點選、拖曳、分割畫面；可視當下情境選用，不必綁死某種工具。
- 支援外掛（plugins）擴充分頁與工作流程，並有 marketplace 可瀏覽安裝。

🎯 **怎麼用：安裝與最小可行流程**

README 提供的安裝方式：
- macOS / Linux：`curl -fsSL https://herdr.dev/install.sh | sh`，或 `brew install herdr`，也可用 `mise use -g herdr`
- Windows（beta）：`powershell -ExecutionPolicy Bypass -c "irm https://herdr.dev/install.ps1 | iex"`
- 或直接下載二進位檔

起步流程：在專案目錄執行 `herdr` 啟動 → `run` 你的 agents、分割分頁 → 走開也沒關係。`ctrl+b q` 可 detach，之後用 `herdr` 指令 reattach。完整檔案在 herdr.dev/docs（含 quick start、concepts、supported agents、keyboard、configuration、session state、remote、integrations、plugins、socket api）。

⚠️ **適用場景與限制**

素材指出 Windows 版仍為 beta；其餘如支援哪些 agent、remote 實作細節、外掛相容性，README 僅列出檔案章節而未展開，實際邊界需查閱 docs 或試用確認。

🎯 **實務啟示**

如果你已經在終端機裡同時操弄多個 coding agent 或自動化指令碼，herdr 這種「不換終端機、純二進位、可 ssh 重連」的多工器，值得作為 tmux 之外、專為 agent 協作設計的候選。對想讓 agent 彼此協調的工程師，socket API 讓「agent 生 agent 分頁、互相等待」成為可程式化的流程，而非手動監看。

🔗 **來源**
- 標題：ogulcancelik/herdr
- 作者／機構：ogulcancelik
- 連結：https://github.com/ogulcancelik/herdr

#terminal #agent #multiplexer #rust #tmux #AIagents #socketAPI #plugins #ssh #CLI
