---
title: openai/codex
source: GitHub Trending
url: https://github.com/openai/codex
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:25:31.984928'
---

📌 【OpenAI 新工具】Codex CLI：將 AI 程式碼代理直接部署在本地終端機

TL;DR：OpenAI 推出 Codex CLI，讓工程師能以本地代理（Agent）形式在終端機中執行 AI 程式碼操作。

如果你習慣在終端機（Terminal）中完成所有開發流程，不再想在瀏覽器與編輯器之間切換，OpenAI 這次將 Codex 以 CLI（命令列介面）的形式提供，讓 AI 代理直接在你的電腦本地端執行。

🧩 **多端整合的部署選擇**

根據 README 說明，Codex 提供了三種不同的使用路徑，視你的開發習慣而定：
- 本地終端機：安裝 Codex CLI，直接在本地電腦執行。
- 編輯器整合：若要在 VS Code、Cursor 或 Windsurf 中使用，應直接安裝對應的 IDE 外掛。
- 桌面與雲端：提供桌面應用程式（Codex App）以及雲端版本（Codex Web）。

🛠️ **快速安裝與啟動指南**

Codex CLI 支援多種安裝方式，開發者可依作業系統選擇最快路徑：

- Mac 或 Linux：
  `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
- Windows：
  `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`
- 套件管理工具：
  - npm：`npm install -g @openai/codex`
  - Homebrew：`brew install --cask codex`

此外，使用者也可以從 GitHub Release 下載對應平臺的二進位檔（Binary），包含 macOS (Apple Silicon/x86_64) 與 Linux (x86_64/arm64) 等版本。下載後解壓縮並將執行檔重新命名為 `codex` 即可開始使用。

🎯 **實務啟示**

對於追求開發效率的工程師而言，CLI 工具的價值在於能將 AI 能力與現有的 Shell 工作流結合。透過 `codex` 指令直接在終端機啟動並登入 ChatGPT 帳號，可以減少切換視窗的認知負荷，讓 AI 代理更貼近底層操作環境。

🔗 **來源**
- 標題：openai/codex
- 作者／機構：OpenAI
- 連結：https://github.com/openai/codex

#OpenAI #Codex #CLI #CodingAgent #DeveloperTools #GitHub #ChatGPT #Automation #Terminal #Productivity
