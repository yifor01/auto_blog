---
title: vercel-labs/skills
source: GitHub Trending
url: https://github.com/vercel-labs/skills
score: 84
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:09:38.594147'
---

📌 **Vercel Labs 推出 skills CLI：打造跨 Agent 的開放技能生態系**

TL;DR：一個讓開發者能快速安裝並將特定技能（Skills）注入 Claude Code、Cursor 等 70 多種 AI Agent 的 CLI 工具。

目前 AI Coding Agent 雖然強大，但如何讓不同 Agent 快速獲得相同的「專業知識」或「設計準則」？Vercel Labs 釋出的 `skills` 專案試圖透過標準化的 CLI，讓技能在不同 Agent 之間可移植且易於分發。

🧩 **跨 Agent 的技能分發機制**

`skills` 定義了一個開放的技能生態系，讓使用者能將預定義的技能（如設計指南或特定開發規範）直接套用到支援的 Agent 中。目前該工具已支援 OpenCode、Claude Code、Codex、Cursor 以及另外 68 個 Agent。

🛠️ **如何安裝與使用技能**

根據 README，`skills` 提供了兩種主要的使用模式：

1. **永久安裝**：將技能安裝至專案或全域目錄。
   - 安裝指令：`npx skills add vercel-labs/agent-skills`
   - 可使用 `-g` 參數安裝到使用者目錄，或用 `-s` 指定安裝特定技能。

2. **即時使用（無需安裝）**：直接產生 Prompt 並啟動 Agent。
   - 產生 Prompt 並輸出至 stdout：`npx skills use vercel-labs/agent-skills@web-design-guidelines | claude`
   - 直接啟動互動式 Agent：`npx skills use vercel-labs/agent-skills --skill web-design-guidelines --agent claude-code`

💡 **靈活的來源解析與支援格式**

`skills` 的 `add` 與 `use` 指令支援多種路徑解析方式，讓技能來源不限於單一平臺：
- **GitHub 簡寫**：`owner/repo`
- **完整 URL**：支援 GitHub、GitLab 及任何 Git URL
- **精確路徑**：可直接指定 Repo 中的特定目錄（如 `/tree/main/skills/...`）
- **本地路徑**：支援 `./my-local-skills` 等本地路徑

🎯 **實務啟示**

對於需要維護團隊開發規範（Coding Standard）或 UI/UX 設計準則的工程師，這個工具提供了一種「將知識模組化」的可能性。不再需要每次對不同 Agent 重複輸入相同的 System Prompt，而是將其封裝成 Skill，透過 CLI 快速分發給團隊成員，確保所有 AI Agent 的輸出品質保持一致。

🔗 **來源**
- 標題：vercel-labs/skills
- 作者／機構：vercel-labs
- 連結：https://github.com/vercel-labs/skills

#AI #Agent #Vercel #CLI #ClaudeCode #Cursor #DeveloperTools #OpenSource #PromptEngineering #SoftwareEngineering
