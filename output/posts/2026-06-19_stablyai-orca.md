---
title: stablyai/orca
source: GitHub Trending
url: https://github.com/stablyai/orca
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-06-19T20:06:09.521160'
---

📌 **【Stability AI 開源】Orca：讓多個 AI Agent 在獨立工作區並行運作的協作平台**

TL;DR：Orca 讓開發者能讓不同 AI Agent 在獨立 git worktree 中並行運作，並透過 UI 整合與手機遠端監控提升開發效率。

在 AI 編程時代，我們常在 ClaudeCode、OpenCode 或 Codex 之間切換，但每個 Agent 的修改紀錄散落在不同地方，比對結果與整合程式碼成了巨大的心智負擔。

🧩 **讓多個 AI Agent 在獨立 Worktree 中並行運作**

Orca 的核心理念是將 AI Agent 的運作與 git worktree 深度綁定。開發者可以將同一個指令（Prompt）同時分發給五個不同的 Agent，每個 Agent 都在一個完全隔離的 git worktree 中執行。這樣能讓開發者直接比較不同模型的產出結果，並選擇最佳版本進行合併（Merge）。

🧩 **整合開發流程的 UI 與遠端能力**

為了減少開發者的上下文切換（Context Switch），Orca 提供了多項整合功能：
- **Design Mode**：可直接點擊 Chromium 視窗中的 UI 元素，將 HTML、CSS 及截圖直接傳送給 Agent。
- **原生整合 GitHub 與 Linear**：在 App 內瀏覽 PR、Issue 與專案看板，並能直接從特定任務開啟對應的 worktree。
- **遠端執行與 SSH**：支援在高效能遠端伺服器上執行 Agent，並提供自動重新連線與連接埠轉發（Port Forwarding）。
- **AI Diff 註釋**：可直接在 diff 行中留下評論並回傳給 Agent 進行修正。

🧩 **高效能終端機與自動化工具**

- **WebGL 渲染終端機**：提供類似 Ghostty 的終端機體驗，支援無限分屏（Infinite Splits），且捲動紀錄（Scrollback）在重啟後依然保留。
- **Orca CLI**：支援透過指令碼自動化工作流，例如使用 `orca worktree create`、`snapshot`、`click` 與 `fill` 等指令驅動 Agent。
- **編輯器體驗**：內建類似 VS Code 的編輯器且支援全域自動儲存，可直接將檔案或圖片拖入 Agent 的 Prompt 中。

📱 **透過手機監控與引導 Agent**

Orca 提供 iOS 與 Android 行動端應用，讓開發者無需守在電腦前，即可接收 Agent 完成工作的通知，並在任何地方發送後續指令（Follow-ups）來引導 Agent。

🎯 **實務啟示**

對於習慣使用多個 AI 編程工具的工程師，Orca 的價值在於將「模型比對」從手動複製貼上，轉化為「Git 分支級別」的並行實驗。這種將 Agent 運作與工作區（Worktree）隔離的設計，能有效避免 AI 隨意修改主分支，讓 review 過程更安全且透明。

🔗 **來源**
- 標題：stablyai/orca
- 作者／機構：stablyai
- 連結：https://github.com/stablyai/orca

#AI #OpenSource #StabilityAI #DeveloperTools #AIagent #GitWorktree #Productivity #CodingAssistant #GitHub #SoftwareEngineering
