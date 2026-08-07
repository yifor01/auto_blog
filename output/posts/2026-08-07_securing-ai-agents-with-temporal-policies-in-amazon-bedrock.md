---
title: Securing AI agents with temporal policies in Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/securing-ai-agents-with-temporal-policies-in-amazon-bedrock-agentcore/
model: tencent/hy3:free
generated_at: '2026-08-07T07:29:32.002786'
score: 104
---

📌 【Amazon Bedrock AgentCore】單看單一動作不夠安全：引入「時序策略」管控 AI Agent 的行為軌跡

TL;DR：透過 Amazon Bedrock AgentCore 的時序策略（Temporal Policies），能依據 Agent 的歷史行為（Trajectory）來執行狀態化（Stateful）的授權，防止 Agent 繞過安全流程。

🎣 **當 AI Agent 變得太聰明，傳統的「無狀態」權限控制失效了**

傳統應用程式的存取控制通常將每個動作視為獨立事件，並依賴確定性的業務邏輯來確保動作順序與資料時效。然而，AI Agent 的行為模式完全不同：它們會在執行時（Runtime）自行決定要呼叫哪些工具、使用什麼參數，以及執行順序。

這種靈活性帶來了巨大的安全挑戰。單一工具呼叫在孤立狀態下可能是安全的，但若放在上下文（Context）中看，卻可能極度危險。例如：在讀取了不可信的資料源後，緊接著進行敏感操作，這時單靠傳統的無狀態（Stateless）權限檢查（僅檢查「誰能呼叫哪個工具」）是無法察覺風險的。

🤔 **從無狀態到狀態化：為什麼需要時序策略？**

目前的存取控制（如 AgentCore Policy）主要執行無狀態、確定性的規則。但面對 Agent 時，這往往不足以應對以下情境：

*   **違反工作流順序**：Agent 跳過了必要的資料檢核步驟，直接執行敏感指令。
*   **資料偽造**：在工具呼叫之間，Agent 可能利用模型特性產生虛假資訊來誘導下一個步驟。
*   **累積風險過高**：單次交易金額在安全範圍內，但多筆交易累計後的總金額已超過限制。

為了補足這點，Amazon Bedrock AgentCore 引入了**時序策略（Temporal Policies）**。它透過評估當前請求在 Agent 軌跡（Trajectory）中的歷史背景，來決定是否授權。

🧩 **AgentCore 的防禦機制：在邊界外執行，讓 Agent 無法干預**

時序策略的設計核心在於其「位置」與「運作邏輯」：

1.  **邊界執行（At the Perimeter）**：策略是在 AgentCore Gateway 執行，位於 Agent 程式碼之外。這意味著無論 Agent 如何被提示（Prompting）或程式碼存在什麼 Bug，都無法攔截或操縱這些控制規則。
2.  **軌跡感知（Trajectory-aware）**：策略會追蹤一個由「主體（Principal）」與「工作階段 ID（Session ID）」定義的動作序列。
3.  **單一入口管理**：由於 Gateway 路由了所有 Model Context Protocol (MCP) 工具呼叫、Agent 間的呼叫以及模型推論，時序策略可以統一治理這三種呼叫，提供一致的行為判斷。
4.  **安全性原則**：延續現有的設計，採用「預設拒絕（Deny by default）」以及「禁止優先於允許（Forbid wins over permit）」的原則。

📊 **技術細節：工作階段與 Dogwood 語言**

*   **工作階段（Session）的定義**：
    *   每個請求必須攜帶 `x-amzn-bedrock-agentcore-policy-session-id`。
    *   工作階段結合了 Session ID 與終端使用者的身份，確保不同使用者即便使用相同的 ID 也會被視為獨立的軌跡。
    *   **時效性**：軌跡事件最多保留 24 小時，超過時間的事件會自動刪除。
    *   **更新機制**：一旦修改了 Policy 規則，現有的工作階段會立即失效，確保所有請求都依據最新的規則進行評估。
*   **Dogwood 語言**：
    *   時序策略使用一種名為 **Dogwood** 的開源治理語言。
    *   它支援評估現有的 Cedar 策略，並允許加入時序條件（Temporal conditions），因此使用者不需要遷移現有的 Cedar 策略。

💡 **實務範例：私人銀行代理人的安全防線**

假設有一個協助理財顧問管理客戶投資組合的 Agent，其工具包含：`get_client_profile`（獲取客戶資料）、`load_portfolio`（載入投資組合）以及 `rebalance_portfolio`（重新平衡投資組合）。

為了符合合規要求，團隊設定了以下時序控制：

*   **強制執行工作流順序**：
    *   **規則**：必須依序完成 `get_client_profile` → `load_portfolio` → `rebalance_portfolio`。
    *   **防禦效果**：如果 Agent 試圖跳過「載入投資組合」的步驟，直接執行「重新平衡」，即便該動作本身在權限範圍內，也會被 Gateway 直接拒絕。

🎯 **實務啟示**

對於正在開發 AI Agent 的工程師來說，安全設計不應僅停留在「工具的權限管理」，更應轉向「行為的流程管理」。透過在 Gateway 層級實施時序策略，可以有效在不侵入 Agent 核心邏輯的情況下，建立一道堅實的防禦屏障，確保 Agent 的行為不僅符合權限，更符合預期的業務邏輯與合規流程。

🔗 **來源**
- 標題：Securing AI agents with temporal policies in Amazon Bedrock AgentCore
- 作者／機構：Sean Eichenberger @ AWS ML
- 連結：aws.amazon.com/blogs/machine-learning/securing-ai-agents-with-temporal-policies-in-amazon-bedrock-agentcore/

#AI #MachineLearning #AWS #AmazonBedrock #AIAgent #Cybersecurity #CloudComputing #SoftwareEngineering #MachineLearningOps #BedrockAgentCore
