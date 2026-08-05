---
title: 'CopilotKit Open Sources Channels SDK: An MIT Licensed Library That Runs Any
  AG-UI Agent Inside Slack And Microsoft Teams'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/04/copilotkit-open-sources-channels-sdk/
model: tencent/hy3:free
generated_at: '2026-08-05T08:41:03.673110'
score: 96
---

📌 【CopilotKit 開源】不用重寫程式碼，讓你的 AI Agent 直接進駐 Slack 與 Microsoft Teams

TL;DR：Channels SDK 透過 AG-UI 協定，讓現有的 AI Agent 能無縫整合至 Slack 與 Teams。

開發者在打造 AI Agent 時，常面臨一個尷尬的局面：你已經寫好了複雜的模型、工具（tools）與業務邏輯，但要讓使用者在 Slack 或 Microsoft Teams 上方便地與它互動，往往得針對每個平臺的 API 重新開發一套介面。

🧩 **不用重寫，只需一個 Adapter**

CopilotKit 推出的 Channels SDK 核心理念非常明確：你已經有一個成熟的 Agent 了，現在你只需要給它一個「工作場所」。

這個 SDK 並非建立一個新的 Agent，它扮演的角色是「傳輸層（Transport）」與「渲染目標（Rendering target）」。開發者只需要撰寫一次訊息，Adapter 就會將其轉換為各平臺的原生格式，例如 Slack 的 Block Kit 或 Microsoft Teams 的 Adaptive Cards，而非單純推送一段純文字。

只要符合 CopilotKit 維護的 AG-UI（Agent-User Interaction Protocol）協定，無論你的架構是 LangGraph、CrewAI、Mastra、Pydantic AI、Google ADK，甚至是自己寫的簡單 HTTP Agent，都能直接使用。

🛠️ **職責分離：你的 Agent 與 Channels 的分工**

為了確保系統穩定，SDK 採用了明確的職責劃分：

*   **開發者負責**：執行 Agent、管理模型憑證、工具與業務邏輯。
*   **Channels 負責**：執行長時運行的 Channels 監聽器（Listener）、管理應用程式狀態、部署與日誌。
*   **Intelligence 負責**：管理 Slack 與 Teams 的平臺憑證、處理平臺入口（Ingress）、憑證傳遞、執行期註冊（Runtime registration）、健康檢查與重連機制。

💡 **以 JSX 進行渲染，並支援複雜互動**

在技術實作上，訊息是以 JSX 撰寫，隨後被轉換為可序列化的中間表示法（Intermediate representation）。這讓開發者可以透過註冊具名的 JSX 元件，實現訊息在重啟後仍能重新渲染並觸發處理函式（Handlers）的能力。

此外，SDK 提供了一套完整的生命週期管理：
*   透過 `channels.ready()` 確保配置錯誤能在啟動時立即被發現。
*   透過 `channels.status()` 監控整體狀態。
*   支援 Node、Hono 與 Express 的 Runtime 監聽。

⚠️ **針對「工作流程」而非「聊天」進行設計**

Channels SDK 的設計目標是處理「在 Thread（執行緒）中發生的工作」，而非單純為了聊天而聊天。

例如在處理 Linear 或 Notion 的資料變更（Mutation）時，可以透過攔截器（Interceptor）實作「核准模式」：在 MCP 請求執行前先攔截，發出 `confirm_write` 訊號，並在獲得使用者核准後才繼續執行。而讀取與渲染動作則不會因此暫停，確保使用者體驗的流暢度。

🎯 **實務啟示**

對於需要將 AI 能力嵌入企業內部溝通工具的工程師來說，Channels SDK 提供了一個標準化的層級。你不需要在每個溝通平臺上重複撰寫 UI 邏輯，只需專注於 Agent 本身的邏輯，並透過 AG-UI 協定實現跨平臺的介面一致性。

🔗 **來源**
- 標題：CopilotKit Open Sources Channels SDK: An MIT Licensed Library That Runs Any AG-UI Agent Inside Slack And Microsoft Teams
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/04/copilotkit-open-sources-channels-sdk/

#AI #Agent #CopilotKit #OpenSource #Slack #MicrosoftTeams #SDK #AGUI #SoftwareEngineering #Productivity
