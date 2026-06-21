---
title: modem-dev/hunk
source: GitHub Trending
url: https://github.com/modem-dev/hunk
score: 80
model: google/gemma-4-31b-it:free
generated_at: '2026-06-21T19:51:16.824094'
---

📌 為 AI Agent 打造的終端機 Diff 檢視器：hunk

TL;DR：基於 OpenTUI 的終端機工具，提供側邊欄導覽與 AI 註釋，最佳化 Agent 產出程式碼的審查流程。

當 AI Agent 自動生成大量程式碼變更時，傳統的 `git diff` 純文字輸出往往讓審查者在大量變更中迷失。如何能像在 GitHub PR 一樣，在終端機中快速切換檔案並同步閱讀 AI 的修改說明？

🧩 **以「審查優先」設計的 TUI 介面**

hunk 是一個專為 Agent 產出的變更集（changesets）設計的終端機 Diff 檢視器，其核心設計在於將「程式碼比對」與「註釋閱讀」整合在同一個視窗中：

- **多檔案審查流**：提供側邊欄導覽，讓使用者在多個變更檔案間快速切換。
- **AI 註釋整合**：支援在程式碼比對旁直接顯示 AI 與 Agent 的註釋（annotations）。
- **靈活佈局**：提供 Split（分欄）、Stack（堆疊）以及響應式自動佈局。
- **多元操作**：同時支援鍵盤、滑鼠、Pager 以及 Git difftool 整合。

⚙️ **支援多種版本控制系統與即時監控**

hunk 不僅支援標準的 Git 流程，還針對現代版本控制工具進行了最佳化：

- **Git 深度整合**：指令模式映象 Git 的 diff 習慣，例如 `hunk diff` 檢視當前變更（含未追蹤檔案），`hunk show` 檢視特定 commit。
- **原生支援 Jujutsu 與 Sapling**：能自動偵測 jj 或 Sapling 工作區，並直接使用其原生的 revsets 進行查詢。
- **即時監控模式**：透過 `--watch` 引數，可以在工作區變更時自動重新載入，適合在 Agent 寫 Code 時即時監控。
- **純檔案比對**：無需 VCS 也能直接比對兩個檔案（例如 `hunk diff before.ts after.ts`）。

🛠️ **快速安裝與啟動**

hunk 依賴 Node.js 18+，支援 macOS、Linux 與 Windows。

- **安裝方式**：
  - npm: `npm i -g hunk`
  - Homebrew: `brew install modem-dev/tap/hunk`
  - Nix: 可使用 `flake.nix` 導出的預設套件。

- **常用指令**：
  - `hunk diff`：審查當前儲存庫變更。
  - `hunk diff --watch`：監控工作區變更並自動更新。
  - `hunk show HEAD~1`：審查特定的歷史 commit。

🎯 **實務啟示**

對於頻繁使用 AI 編碼助手（如 Auto-dev 工具）的工程師，hunk 將「審查」從單純的文字比對提升到「導覽 + 註釋」的維度。將其設定為 Git 的 difftool，可以在不離開終端機的情況下，更直覺地確認 AI 修改的意圖，減少在 IDE 與終端機之間切換的心智負荷。

🔗 **來源**
- 標題：modem-dev/hunk
- 作者／機構：modem-dev
- 連結：https://github.com/modem-dev/hunk

#TUI #Git #Diff #AI #Agent #OpenTUI #DeveloperTools #Jujutsu #Sapling #Nodejs
