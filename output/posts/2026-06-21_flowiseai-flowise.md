---
title: FlowiseAI/Flowise
source: GitHub Trending
url: https://github.com/FlowiseAI/Flowise
score: 84
model: google/gemma-4-31b-it:free
generated_at: '2026-06-21T19:50:03.933570'
---

📌 【開源專案】Flowise：透過視覺化介面快速建置 AI Agents

TL;DR：一個讓開發者能以視覺化方式建置 AI Agents 的開源工具，支援自定義部署與模組化擴展。

想要建置 AI Agent 但不想在繁瑣的程式碼中定義每個流程？Flowise 提供了一種直觀的視覺化方法，讓 AI 代理的建置過程從撰寫程式碼轉向視覺化組裝。

🧩 **模組化設計的 Mono Repository 架構**

Flowise 在技術實作上採用單一儲存庫 (mono repository) 管理，將系統拆分為三個核心模組，方便開發者針對不同層級進行開發或整合：

- server：負責提供 API 邏輯的 Node.js 後端。
- ui：基於 React 構建的前端使用者介面。
- components：整合第三方節點 (nodes) 的擴充模組。
- api-documentation：透過 express 自動產生的 swagger-ui API 檔案。

🐳 **多樣化的部署與快速啟動方式**

對於工程師而言，Flowise 提供了多種快速部署路徑，降低了環境建置的門檻：

- 直接安裝：只要 Node.js 版本在 20.0.0 以上，可透過 `npm install -g flowise` 安裝後直接執行 `npx flowise start`。
- Docker 部署：支援 Docker Compose 一鍵啟動，或直接使用 Docker Image 進行本地建置與執行。
- 自主託管：除了雲端版本 (Flowise Cloud)，專案也詳細說明了 Self Host 的部署流程。

👨‍💻 **開發者整合與建置指南**

若需要對 Flowise 進行二次開發，專案使用了 pnpm 作為套件管理工具。開發流程如下：
`git clone` → `pnpm install` (安裝所有模組依賴) → `pnpm build` (建置程式碼)。

⚠️ **建置時的記憶體限制**
README 特別提醒，若在執行 `pnpm build` 時遇到 `Exit code 134 (JavaScript heap out of memory)` 錯誤，開發者需要增加 Node.js 的 heap size 後再次嘗試。

🎯 **實務啟示**

對於需要快速驗證 AI Agent 概念 (PoC) 的工程師，Flowise 的視覺化節點設計能大幅縮短從「想法」到「原型」的時間。由於其模組化結構，開發者可以透過 `components` 模組將特定的第三方服務整合進流程，而無需重寫整個後端邏輯。

🔗 **來源**
- 標題：FlowiseAI/Flowise
- 作者／機構：FlowiseAI
- 連結：https://github.com/FlowiseAI/Flowise

#AI #AIAgents #OpenSource #LowCode #NodeJS #React #Docker #LLM #VisualProgramming #Flowise
