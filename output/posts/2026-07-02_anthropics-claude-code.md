---
title: anthropics/claude-code
source: GitHub Trending
url: https://github.com/anthropics/claude-code
score: 114
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:48:58.486231'
---

📌 【Anthropic 新工具】Claude Code：把 AI 代理直接搬進終端機的程式設計助手

TL;DR：Anthropic 推出的終端機代理工具，可透過自然語言執行常規任務、解釋程式碼並管理 git 工作流。

大多數 AI 程式設計助手將我們留在 IDE 的對話方塊中，但真正的開發流程往往在終端機（Terminal）裡切換。Anthropic 這次推出的 Claude Code，將 AI 代理（Agentic tool）直接整合進開發者的命令列環境。

🧩 **在終端機中直接操作 codebase**

Claude Code 並非單純的聊天機器人，而是一個具備代理能力的程式設計工具。它能直接理解你的整個 codebase，並透過自然語言指令協助開發者完成以下任務：
- 執行重複性的常規程式設計任務。
- 解釋複雜的程式碼邏輯。
- 處理 git 工作流（git workflows）。

除了在終端機中使用，它也支援在 IDE 中運作，或在 GitHub 上透過標記 @claude 進行互動。

⚙️ **快速安裝與啟動方式**

README 指出，目前已不建議使用 npm 進行安裝。根據作業系統，推薦的安裝路徑如下：
- MacOS/Linux：使用 `curl -fsSL https://claude.ai/install.sh | bash` 或透過 Homebrew (`brew install --cask claude-code`)。
- Windows：使用 `irm https://claude.ai/install.ps1 | iex` 或透過 WinGet (`winget install Anthropic.ClaudeCode`)。

安裝完成後，只需進入專案目錄並執行 `claude` 指令即可啟動。

💡 **可擴充的外掛系統與回饋機制**

為了強化功能，此專案提供了一系列外掛（Plugins），允許開發者透過自定義指令與代理（Agents）來擴展 Claude Code 的能力。

此外，Anthropic 內建了直接的回饋路徑，使用者可以在工具內使用 `/bug` 指令直接回報問題，或透過 GitHub issue 與 Discord 社群進行交流。

🎯 **實務啟示**

對於習慣在終端機操作的工程師來說，這種「代理式」的工具能減少在 IDE 與 Terminal 之間來回切換的認知負荷。將 Git 操作與程式碼分析整合在同一介面，能讓日常的維護與重構流程更為流暢。

🔗 **來源**
- 標題：anthropics/claude-code
- 作者／機構：Anthropic
- 連結：https://github.com/anthropics/claude-code

#AI #ClaudeCode #Anthropic #Terminal #AgenticAI #CodingAssistant #DeveloperTools #GitHub #Git #Programming
