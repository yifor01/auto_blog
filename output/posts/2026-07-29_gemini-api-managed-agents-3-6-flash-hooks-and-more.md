---
title: 'Gemini API Managed Agents: 3.6 Flash, hooks, and more'
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/
model: tencent/hy3:free
generated_at: '2026-07-29T08:24:09.674332'
pinned: true
---

📌 【Google DeepMind】Gemini API 升級：Managed Agents 預設換上 Gemini 3.6 Flash 並新增環境 Hooks

TL;DR：Gemini API 的 Managed Agents 預設改用 Gemini 3.6 Flash，並新增環境 Hooks 與預算控制功能。

Google 正在持續擴展 Gemini API 中 Managed Agents 的能力。透過 Gemini Interactions API，開發者只需單次 API 呼叫，即可在隔離的雲端沙盒（sandbox）中完成推理、程式碼執行、套件安裝、檔案管理與網頁檢索等複雜協作任務。

🧩 **預設模型升級至 Gemini 3.6 Flash**

從現在起，`antigravity-preview-05-2026` agent 已預設使用 Gemini 3.6 Flash 運行，開發者無需修改程式碼即可自動升級。

- **模型選擇靈活性**：開發者可以透過 `agent_config.model` 參數明確指定模型。
- **成本優化**：若追求更低的成本，可以選擇使用 Gemini 3.5 Flash-Lite。

🛠️ **新增環境 Hooks：強化沙盒安全性**

為了提升在沙盒內執行工具呼叫（tool calls）時的安全性與可控性，新的環境 Hooks 允許開發者執行以下操作：
- 阻斷（Block）
- 檢查（Lint）
- 稽核（Audit）

💰 **新增預算控制與排程觸發**

除了安全性提升，Google 也為 Managed Agents 引入了更多管理功能：
- **預算控制（Budget controls）**：防止非預期的成本支出。
- **排程觸發（Scheduled triggers）**：讓任務可以依據預定時間執行。
- **免費層級存取（Free tier access）**：降低開發門檻。

🚀 **如何快速整合**

如果你正在使用 AI 程式碼助手，可以直接在終端機執行以下指令，賦予其使用 Interactions API 的能力：
`npx skills add google-gemini/gemini-skills --skill gemini-interactions-api`

針對使用 TypeScript/JavaScript SDK 的開發者，可以透過 `@google/genai` 套件進行開發；而 Python 或 cURL 用戶則可以參考 Antigravity agent 的相關文件。

🎯 **實務啟示**

對於需要處理複雜工作流（如自動化編程或數據分析）的工程師來說，Managed Agents 提供的「單次呼叫即完成多項任務」的能力極具價值。新增的 Hooks 功能，讓開發者在將 Agent 部署至生產環境時，能更有效地控制沙盒內的行為，降低執行未知程式碼帶來的風險。

🔗 **來源**
- 標題：Gemini API Managed Agents: 3.6 Flash, hooks, and more
- 作者／機構：Philipp Schmid & Mariano Cocirio @ Google DeepMind
- 連結：https://blog.google/innovation-and-ai/technology/developers-tools/expanding-managed-agents-gemini-api-3-6-flash-hooks/

#Gemini #GoogleDeepMind #GeminiAPI #ManagedAgents #LLM #AI #SoftwareDevelopment #CloudSandbox #Gemini36Flash #DeveloperTools
