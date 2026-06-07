---
title: withastro/flue
source: GitHub Trending
url: https://github.com/withastro/flue
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-07T19:34:05.635526'
---

📌 【Astro 團隊新作】Flue：把 Claude Code 的體驗轉化為可程式化的 Agent 框架

如果你曾使用過 Claude Code 或類似的 AI 編程助手，你一定能感受到那種「直接給目標，AI 自行思考並執行任務」的快感。但如果我們想把這種能力封裝成一個自動化服務，而不是讓人類在終端機對話，該怎麼做？

Astro 團隊推出的實驗性專案 **Flue** 給出了答案：將 Agent 的「執行環境 (Harness)」標準化，讓開發者能用 TypeScript 構建 100% Headless 的自主 Agent。

🤔 **從「對話界面」到「可程式化運行時」的轉移**

目前的 AI Agent 工具大多分為兩極：一種是像 Claude Code 這樣強大但依賴 TUI（終端界面）與人類操作的工具；另一種則是像 LangChain 等 SDK，雖然靈活但開發成本高且邏輯分散。

Flue 的核心設計理念是：**「像使用 Claude Code 一樣構建 Agent，但不需要人類操作員。」** 它不再是一個簡單的 SDK，而是一個 runtime-agnostic（運行時無關）的框架。這意味著它定義了 Agent 如何運作的標準，而開發者只需定義邏輯，即可部署到任何環境。

🧪 **以 Markdown 驅動邏輯，降低開發複雜度**

Flue 最有趣的設計在於它將 Agent 的「邏輯」與「程式碼」分離。大部分的 Agent 行為並非寫在複雜的 TypeScript 邏輯中，而是定義在 Markdown 檔案裡：

- **Skills & Context**：透過 Markdown 定義 Agent 擁有的技能與上下文。
- **AGENTS.md**：定義 Agent 的身份與運作規則。

這種設計讓 Agent 的行為配置變得極其直觀，開發者可以用更像「寫文檔」的方式來定義 AI 的行為，而 TypeScript 則負責底層的運行時控制與整合。

💡 **Headless 設計：讓 Agent 真正進入自動化管線**

Flue 捨棄了 TUI 與 GUI，完全採用 Headless 模式。這讓 Agent 可以被整合進各種自動化場景：

- **多樣化部署**：支持 Node.js、Cloudflare Workers、GitHub Actions、GitLab CI/CD 等。
- **靈活的輸入機制**：支持透過 HTTP 或 WebSocket 接收訊息（`/agents/:name/:id`），或由應用程式透過 `dispatch(...)` 觸發異步輸入。
- **模組化架構**：
    - `@flue/runtime`：負責 Harness（執行環境）、Session 管理、工具調用與 Sandbox。
    - `@flue/cli`：提供開發工具與構建流程。

⚠️ **目前仍處於實驗階段，API 變動頻繁**

由於 Flue 目前標記為 **Experimental** 且處於積極開發中，其 API 可能會隨時變更。對於追求穩定性的生產環境，目前建議將其視為技術探索，而非直接用於核心業務。

🎯 **對工程師的實務啟示：從 SDK 轉向框架思維**

Flue 的出現代表了一種趨勢：AI 開發正在從「調用 API (SDK)」轉向「定義運行環境 (Framework)」。

如果你需要構建一個能自主執行任務、且不需要人類時刻監控的 Agent（例如：自動化 Code Reviewer、自動化部署監控助手），Flue 提供了一套將「Markdown 定義 $\rightarrow$ TypeScript 執行 $\rightarrow$ 多平台部署」的快速路徑。

🔗 **專案連結**
📝 Flue: The Agent Harness Framework
👤 withastro
🔗 GitHub: https://github.com/withastro/flue

你認為 Agent 的邏輯應該寫在程式碼裡，還是定義在 Markdown 裡？歡迎在下方分享你的看法 👇

#AI #TypeScript #Astro #AIagents #ClaudeCode #WebDevelopment #Cloudflare #GitHubActions
