---
title: 'Andrew Ng Just Released OpenWorker: An Open-Source, Local-First Desktop AI
  Coworker That Returns Finished Deliverables Instead of Chat'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/23/andrew-ng-just-released-openworker-an-open-source-local-first-desktop-ai-coworker-that-returns-finished-deliverables-instead-of-chat/
model: tencent/hy3:free
generated_at: '2026-07-24T08:13:01.491727'
score: 98
---

根據您提供的資訊，這屬於「開源專案」與「產業新聞」的結合。我將以「開源專案」的架構為核心，並結合新聞中提到的技術細節進行轉寫。

---

📌 【Andrew Ng 重磅釋出】OpenWorker：不再只是聊天，而是直接交付成果的開源 AI 協作助手

TL;DR：OpenWorker 是一款強調「交付成果」而非「對話」的開源桌面 Agent，支援本地運算與多模型切換。

🤖 **從「輸入 Prompt」轉向「要求成果」**

目前的 AI 助手大多停留在對話階段，但 Andrew Ng 釋出的 OpenWorker 試圖改變這一現狀。它不要求使用者輸入 Prompt，而是要求一個「結果」（Outcome），例如：一份潤飾過的文件、一封包含實際資料的 Slack 回覆、更新後的行事曆，或是整理好的收件匣。

🧩 **核心設計：將任務拆解為步驟並執行**

OpenWorker 的運作邏輯是將使用者要求的結果拆解成具體的執行步驟，並能跨越本地檔案與已連線的應用程式進行操作。為了確保安全性，在執行任何具有影響力的操作前，它會先向使用者確認。

🛠️ **技術棧：基於 aisuite 的多模型支援**

OpenWorker 本身並不提供推理服務，使用者需自行貼上 API Key 或指向本地執行環境。其技術架構如下：
- **核心引擎**：建立在 Andrew Ng 開發的 provider-agnostic（與供應商無關）LLM 函式庫 `aisuite` 之上。
- **模型矩陣**：提供 30 個精選模型選項，包含：
    - **原生供應商**：OpenAI (GPT-5.6 系列)、Anthropic (Claude 5 系列)、Google (Gemini 3.1 系列)。
    - **相容供應商**：DeepSeek V4、Qwen3 Max、Mistral Large 等。
    - **開源模型**：透過 Together AI 或 Fireworks 使用開源權重模型，或透過 Ollama 執行完全本地化的模型（無需 API Key）。

⚠️ **嚴密的許可權管理：將「核准機制」視為核心層級**

與許多將核准機制視為 UI 點綴的 Agent 專案不同，OpenWorker 將核准視為一個「型別化層級」（typed layer）。系統將所有工具呼叫（tool call）分為四種風險等級：
- `read`：讀取操作，無副作用。
- `write_local`：修改工作區內容，受路徑範圍限制。
- `exec`：執行指令。
- `external`：產生機器外部的副作用。

針對這些操作，系統提供五種許可權模式：
- `discuss and plan`：唯讀模式。
- `interactive`（預設）：在執行寫入、指令或外部動作前會詢問使用者。
- `auto`：允許所有操作，但仍受路徑範圍限制。
- `custom auto-approves`：自動核准使用者清單中指定的工具。

🎯 **實務啟示

對於開發者而言，OpenWorker 展示了 AI Agent 從「對話方塊」轉向「工作流」的趨勢。它透過嚴謹的許可權分類與本地化模型支援，解決了 AI Agent 在執行自動化任務時最令人擔憂的安全性與隱私問題。

🔗 **來源**
- 標題：Andrew Ng Just Released OpenWorker: An Open-Source, Local-First Desktop AI Coworker That Returns Finished Deliverables Instead of Chat
- 連結：https://www.marktechpost.com/2026/07/23/andrew-ng-just-released-openworker-an-open-source-local-first-desktop-ai-coworker-that-returns-finished-deliverables-instead-of-chat/

#OpenWorker #AndrewNg #AI #OpenSource #LLM #AIAgent #MachineLearning #LocalAI #Productivity #SoftwareEngineering
