---
title: 'Gemini API Managed Agents: 3.6 Flash, hooks, and more'
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/
model: tencent/hy3:free
generated_at: '2026-07-29T14:05:25.197329'
pinned: true
---

📌 【Google DeepMind】Gemini API Managed Agents 進化：預設改用 3.6 Flash 並新增環境 Hooks

TL;DR：Gemini API 的 Managed Agents 升級，預設模型更換為 3.6 Flash，並新增環境 Hooks 與預算控制功能。

Google 正在持續強化 Gemini API 中的 Managed Agents 功能。透過 Gemini Interactions API，開發者只需單次 API 呼叫，即可在隔離的雲端沙盒（sandbox）中完成推理、程式碼執行、套件安裝、檔案管理與網路檢索等一系列複雜任務。

🧩 **預設模型升級至 Gemini 3.6 Flash**

目前的 `antigravity-preview-05-2026` agent 已改為預設使用 Gemini 3.6 Flash，開發者無需修改任何程式碼，下次互動時即可自動套用。

若有特殊需求，開發者仍可透過 `agent_config.model` 參數明確指定模型：
- 使用 Gemini 3.5 Flash-Lite 以降低成本。
- 或鎖定（pin）至您偏好的特定模型。

💡 **新增環境 Hooks：強化沙盒監控能力**

為了提升安全性與開發靈活性，新的環境 Hooks 允許開發者在沙盒內對工具呼叫（tool calls）進行以下操作：
- 阻斷（Block）
- 檢查（Lint）
- 稽核（Audit）

這項功能讓開發者能在程式碼執行前，更有效地控管 Agent 的行為。

🎯 **更多開發者工具與功能更新**

除了模型與安全性控管，這次更新還包含：
- **預算控制（Budget controls）**：協助管理資源消耗。
- **排程觸發（Scheduled triggers）**：實現自動化流程。
- **免費層級存取（Free tier access）**：降低開發門檻。

這些功能是在先前推出的背景任務（background tasks）與遠端 MCP 伺服器整合功能之上的進一步擴展。

🛠️ **快速上手指南**

若您正在使用 AI 程式碼助手，可以在終端機執行以下指令，賦予其使用 Interactions API 的能力：
`npx skills add google-gemini/gemini-skills --skill gemini-interactions-api`

針對 TypeScript/JavaScript 開發者，可使用 `@google/genai` SDK：
`npm install @google/genai`

對於 Python 或 cURL 使用者，可參考 Antigravity agent 的相關文件。

🔗 **來源**
- 標題：Gemini API Managed Agents: 3.6 Flash, hooks, and more
- 作者／機構：Philipp Schmid & Mariano Cocirio @ Google DeepMind
- 連結：https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/

#GeminiAPI #GoogleDeepMind #GenerativeAI #LLM #ManagedAgents #Gemini36Flash #SoftwareDevelopment #CloudSandbox #AIInfrastructure #DeveloperTools
