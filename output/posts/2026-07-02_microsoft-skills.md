---
title: microsoft/skills
source: GitHub Trending
url: https://github.com/microsoft/skills
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:56:28.230790'
---

📌 【Microsoft 開源】為 AI Agent 提供 175 個即用技能，強化 Azure SDK 領域知識

TL;DR：Microsoft 提供一套可安裝的 Agent Skills 集合，讓 AI 編碼助手快速掌握 Azure SDK 與 AI Foundry 的領域知識。

Copilot CLI 或 VS Code 中的 GitHub Copilot 雖然強大，但它們對特定 SDK 的最新領域知識（Domain Knowledge）仍有不足。雖然這些模式可能已存在於預訓練權重中，但如何精準地「啟用」這些知識，才是提升開發效率的關鍵。

🧩 **透過 Skill 補足 AI Agent 的領域知識缺口**

Microsoft 推出的 `microsoft/skills` 專案旨在提供一套可複用的技能集，讓 AI 編碼助手能更有效率地與 Azure SDKs 及 Microsoft AI Foundry 協作。目前該專案包含 175 個可供瀏覽與安裝的技能，且正處於積極開發狀態，持續更新 SDK 模式並擴充套件測試。

⚙️ **快速安裝與整合方式**

開發者可以透過以下兩種方式將技能匯入至 AI Agent 的配置目錄中（例如 `.github/skills/`）：

1. **快速啟動（推薦）**
   使用 `npx` 命令直接透過嚮導選擇所需技能：
   `npx skills add microsoft/skills`

2. **手動安裝**
   透過 `git clone` 複製專案，並將特定技能複製或建立符號連結（symlink）至專案目錄：
   - 複製特定技能：`cp -r agent-skills/.github/skills/azure-cosmos-db-py your-project/.github/skills/`
   - 跨 Agent 共享：利用 `ln -s` 將技能同步至 `.opencode/skills` 或 `.claude/skills` 等不同 Agent 的設定目錄。

💡 **支援多種 Agent 與 MCP 配置**

此專案不僅提供技能集，還包含自定義 Agent 設定、`AGENTS.md` 模板，以及針對 AI 編碼助手的 MCP（Model Context Protocol）配置，讓不同平臺的 AI 助手能共享同一套知識庫。

🎯 **實務啟示**

對於大量使用 Azure 服務的工程師，不再需要花時間在 Prompt 中反覆解釋 SDK 的使用方式。透過安裝這些預定義的 Skills，可以直接為 AI Agent 提供正確的上下文（Context），將開發模式從「手動引導」轉向「上下文驅動開發（Context-Driven Development）」。

🔗 **來源**
- 標題：microsoft/skills
- 作者／機構：Microsoft
- 連結：https://github.com/microsoft/skills

#Microsoft #Azure #AI #Agent #GitHubCopilot #SDK #MCP #ContextDrivenDevelopment #DeveloperTools #OpenSource
