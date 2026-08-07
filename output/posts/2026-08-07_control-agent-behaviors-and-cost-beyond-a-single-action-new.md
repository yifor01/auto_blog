---
title: 'Control agent behaviors and cost beyond a single action: new capabilities
  in Amazon Bedrock AgentCore'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/
model: tencent/hy3:free
generated_at: '2026-08-07T07:47:04.403888'
score: 85
---

📌 【Amazon Bedrock AgentCore】超越單一動作的管控：如何透過時序策略解決 AI Agent 的安全與成本風險

TL;DR：Amazon Bedrock AgentCore 推出時序策略與流量限制，解決 Agent 序列行為難以預測的安全與成本問題。

隨著 AI Agent 趨向自主化，企業面臨的挑戰已不再是「單一動作是否合法」，而是「一系列動作加起來是否安全」。McKinsey 研究指出，約 80% 的組織已遇到 AI Agent 的風險行為，這已成為規模化 Agentic AI 的主要障礙。

🤔 **當「合法的請求」組合出「錯誤的結果」**

傳統的防護欄（Guardrails）多針對可預測的軟體設計，但 Agent 的行為是動態決定的。這會導致以下情境：

*   **隱蔽的風險**：Agent 查詢客戶帳戶，接著轉帳到不同帳號。單看兩步都是合法操作，但組合起來卻是違規。
*   **預算失控**：Agent 執行一系列金額皆低於審核門檻的訂單，但總額已大幅超出預算。
*   **資源耗盡**：Agent 因工具錯誤陷入無止盡的重試迴圈，消耗掉所有 Token 預算。

這些問題的共同點是：問題不在於單一請求，而在於「模式（Pattern）」。

🧩 **Amazon Bedrock AgentCore：將控制權移至基礎設施層**

為了應對上述挑戰，Amazon Bedrock AgentCore 提出一個核心原則：**安全控制應屬於基礎設施層（Infrastructure layer）**，而非寫在每個團隊各自開發的應用程式碼中。

AgentCore 的閘道（Gateway）作為完全託管的無伺服器入口點，負責路由所有 AI 流量（包含 MCP 伺服器、LLM、Agent 與知識庫）。因為所有請求都必須經過閘道，這讓「在行為發生前進行攔截」成為可能。

🚀 **Dogwood 與時序策略：從「單點檢查」進化到「序列監控」**

為了實現對 Agent 序列行為的精準管控，Amazon 推出了新功能：

*   **時序策略（Temporal policies）**：不再僅僅判斷單一請求的權限，而是會檢查 Agent 在該工作階段（Session）中已經做過什麼。例如：要求轉帳目標值必須與前一個步驟回傳的值一致，或是當總預算達到上限時直接攔截下一個購買動作。
*   **Dogwood 開源語言**：這是專為 AI Agent 設計的新型策略語言。它建立在 Cedar 的基礎之上，並加入了處理 Agent 治理所需的時序建構式，包含速率限制、時間窗口、前置步驟與升級觸發機制。目前 Dogwood 已以 Apache 2.0 授權開源。

📊 **解決 Agentic AI 的成本隱憂**

Forrester 研究發現，Agentic AI 難以規模化的主因之一就是成本。由於 Agent 會根據任務需求決定步驟數量，其 Token 消耗與呼叫次數具有不可預測性。

AgentCore 透過閘道提供**速率限制（Rate limiting）**，讓開發者能針對使用者、工具、模型或 Agent 設定上限：

*   **請求量（Request volume）**：針對重試迴圈導致的頻繁呼叫。
*   **Token 數量**：針對推理密集型任務的消耗。
*   **連線時間（Connection duration）**：針對長時間研究任務佔用的連線。

透過對每秒或每分鐘的窗口進行限制，平臺團隊可以設定容量配置，而無需修改任何 Agent 的程式碼。

🎯 **實務啟示**

對於工程師與架構師而言，這代表了從「開發者自律」轉向「平臺強制執行」的典範轉移。將安全性與成本控制從應用層（Application code）抽離，放入基礎設施層，能確保即使 Agent 表現出非預期行為，邊界（Boundary）依然穩固，且具備可追蹤、可驗證的決定性（Deterministic）控制能力。

🔗 **來源**
- 標題：Control agent behaviors and cost beyond a single action: new capabilities in Amazon Bedrock AgentCore
- 作者／機構：Madhu Parthasarathy @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/control-agent-behaviors-and-cost-beyond-a-single-action-new-capabilities-in-amazon-bedrock-agentcore/

#AI #AgenticAI #AmazonBedrock #AWS #MachineLearning #Dogwood #Cybersecurity #LLM #AIGovernance #CloudComputing
