---
title: facebook/astryx
source: GitHub Trending
url: https://github.com/facebook/astryx
score: 82
model: google/gemma-4-31b-it:free
generated_at: '2026-06-27T19:35:34.161757'
---

📌 【Meta 開源】Astryx：支援 AI Agent 協作且可完全自定義的設計系統

TL;DR：Meta 開源內部使用 8 年的設計系統，主打可組成性與 AI Agent 友善的介面建構。

大多數的設計系統（Design System）往往像個黑盒子，元件封裝得太死，導致工程師在需要微調時得花大量時間覆寫樣式；而現在，Meta 將其內部支撐 13,000 個 App 的開發經驗開源了。

🧩 **從 Meta 內部工具演進而來的設計基礎**

Astryx 是 Meta 在其 monorepo 中經過 8 年迭代的產物，旨在提供一致且具備可存取性（accessible）的介面。它基於 React 與 StyleX 構建，提供基礎設施、元件、模板與主題，讓開發者能快速建構大規模的應用程式。

💡 **三大核心設計特點**

- **開放的內部結構 (Open Internals)**：所有原語 (primitives) 均被匯出且可組成（composable），而非隱藏在封裝之中，允許開發者在任何層級進行組合，精準建構所需功能。
- **自動化間距處理 (Automatic Spacing)**：透過感知上下文的間距補償（spacing compensation），解決常見的「雙重內邊距 (double padding)」問題，讓版面維持整潔而無需手動修正。
- **原生主題化支援 (Themeable)**：利用 CSS 變數級聯（variable cascade）實現一等公民的主題化支援，內建 10 組預設主題且完全可自定義。

🤖 **讓 AI Agent 能像工程師一樣建構 UI**

Astryx 最特別之處在於其「Agent ready」的設計，讓 AI 代理能與人類使用相同的工具鏈：
- **Composition Hints**：透過 JSDoc 註釋提供組合提示。
- **工具整合**：提供 CLI 與 MCP 伺服器，讓 AI Agent 能直接進行快速搭建 (scaffold)、瀏覽元件及撰寫檔案。

🎯 **實務啟示**

對於前端工程師而言，Astryx 的價值在於將「可組成性」推向極限，避免了許多 UI 框架中常見的樣式衝突與覆寫痛點。而其對 MCP 伺服器與 JSDoc 的支援，則為未來「AI 自動生成 UI」提供了一個標準化的 API 基礎，讓 AI 產出的程式碼能更符合設計系統的規範而非隨機生成。

🛠️ **快速上手**

使用 pnpm 可透過以下指令安裝核心套件與中性主題：
`pnpm add @astryxdesign/core @astryxdesign/theme-neutral`
`pnpm add -D @astryxdesign/cli`

🔗 **來源**
- 標題：astryx
- 作者／機構：facebook
- 連結：https://github.com/facebook/astryx

#Meta #React #StyleX #DesignSystem #OpenSource #AIAgent #MCP #Frontend #UIUX #WebDevelopment
