---
title: Codex Security
source: Hacker News
url: https://github.com/openai/codex-security
model: tencent/hy3:free
generated_at: '2026-07-29T14:15:41.347992'
score: 75
---

📌 【OpenAI 開源】Codex Security：透過 CLI 與 SDK 自動掃描並修復程式碼漏洞

TL;DR：OpenAI 推出 Codex Security，提供 CLI 與 TypeScript SDK 來尋找、驗證並修復程式碼中的安全漏洞。

隨著 AI 輔助開發成為常態，程式碼安全性也面臨新的挑戰。OpenAI 推出的 Codex Security 專案，旨在將安全性檢查整合進開發流程中。

🧩 **集掃描、驗證與修復於一身**

這是一個專為開發者設計的安全工具，其核心功能包含：
- 掃描專案儲存庫 (Repositories)。
- 審查程式碼變更 (Review changes)。
- 追蹤發現的安全問題並觀察其隨時間的變化。
- 在 CI (持續整合) 流程中執行安全性檢查。

🛠️ **快速上手與整合方式**

該工具提供 CLI 工具與 TypeScript SDK，並支援透過 Docker 部署。

**環境需求：**
- Node.js 22 或更高版本
- Python 3.10 或更高版本

**基本操作範例：**
1. 安裝：`npm install @openai/codex-security`
2. 登入：`npx codex-security login`
3. 掃描當前目錄：`npx codex-security scan.`

**CI 流程整合：**
在 CI 環境中，不需要進行互動式登入，只需設定 `OPENAI_API_KEY` 環境變數即可。若同時存在 ChatGPT 登入資訊與 API Key，系統會優先使用 API Key。開發者也可以透過參數明確指定驗證方式：
- 使用 ChatGPT 驗證：`npx codex-security scan. --auth chatgpt`
- 使用 API Key 驗證：`npx codex-security scan. --auth api-key`

🎯 **實務啟示**

對於需要將安全性檢查自動化的團隊，Codex Security 提供了一種將 AI 能力直接帶入 CI/CD 流程的路徑，讓安全性檢查不再只是開發後端的額外負擔，而是開發流程的一部分。

🔗 **來源**
- 標題：Codex Security
- 作者／機構：bakigul @ OpenAI
- 連結：https://github.com/openai/codex-security

#OpenAI #CodexSecurity #CyberSecurity #DevSecOps #CLI #TypeScript #OpenSource #CodeSecurity #SoftwareDevelopment #CI/CD
