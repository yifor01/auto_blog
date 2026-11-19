---
title: Amazon Bedrock AgentCore harness adds Strands harness defaults, built-in tools,
  and lifecycle hooks
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-adds-strands-harness-defaults-built-in-tools-and-lifecycle-hooks/
model: claude-code/sonnet
generated_at: '2026-11-19T23:55:34.680239'
score: 78
---

📌 Bedrock AgentCore Harness 導入 Strands 預設與生命週期 Hook,退款前先過一關

TL;DR:AWS Bedrock AgentCore harness 升級採用開源 Strands harness,新增 lifecycle hooks,讓你在代理執行迴圈中插入確定性檢查。

打造一個 AI 代理,選模型只是第一步。代理還需要工具、完成任務的指示、長 session 下的 context 管理方式,以及在執行任何有後果的動作(例如核准退款)之前的防護機制。AWS 這次更新,就是在補齊最後這一塊。

🤔 **選模型之後,真正難的事**

Amazon Bedrock AgentCore harness 現在升級為採用 Strands harness,這是 AWS 今年早些時候以 Apache 2.0 授權開源的代理 harness。這次更新沒有引入新的資源類型或整合點,現有已在用 AgentCore harness 的代理,會自動拿到更新。

🧩 **管理預設值升級了什麼**

採用管理預設值的代理現在會得到:建議的模型、任務導向的系統提示(system prompt)、自動 prompt caching(目前先支援 Amazon Bedrock 上的 Anthropic 模型),以及主動式 context 管理。此外還新增了規劃、網路檢索、檔案系統存取、context 卸載、任務委派等內建工具,讓代理在長任務中能追蹤子任務、降低 context window 用量、並把工作分派出去。

Strands harness 負責組裝出帶有建議指示、工具與 context 管理的代理基礎,Amazon Bedrock AgentCore harness 則把這套基礎作為受管服務來運行,每個 session 跑在 AgentCore runtime 裡一個經 kernel 隔離的 microVM 中,背後接上 session 持久化、串流回應、使用量 metadata、觀測性、AgentCore memory、Identity、Gateway、Browser、Code Interpreter 等服務。開發者仍保有對模型、指示、工具、權限與生命週期政策的控制權,底層執行環境則交給 AgentCore 管理。

值得注意的是,當 `allowedTools` 被省略或設為 `["*"]` 時,harness 會套用目前建議的內建工具集,而這個集合會隨時間增加能力,因此官方建議,若應用程式有固定的安全或能力邊界,應該明確列出需要的工具,而不要依賴萬用字元。

🧩 **Lifecycle hooks:把非決定性的代理行為變成可治理的流程**

透過 lifecycle hooks,開發者可以在代理執行迴圈的特定節點執行自己的確定性程式碼。只有 AWS Lambda 掛載的 hook 能真正改變執行迴圈走向,同步執行並回傳 allow 或 deny(可附理由);Amazon SNS 或 Amazon EventBridge 掛載的 hook 則純粹作為通知用途,不會阻擋流程。

官方給的範例是客服退款場景:代理可以自行調查訂單,但 `before_tool_call` hook 會在退款工具真正執行前,先檢查金額是否超過核准額度。一旦 Lambda 判斷拒絕,harness 就會跳過退款動作,代理接著能告知顧客需求已被升級處理;每個決策也會出現在 `InvokeHarness` 的回應串流中,標記為 `hookEvent`。這套檢查同樣套用在代理委派給 subagent 的任務上,代理無法藉由委派繞過退款政策。hooks 透過 `CreateHarness` 或 `UpdateHarness` 設定;若 Lambda 函式逾時或回傳錯誤,會依 `failureMode` 處理,預設為 deny。

💡 **動手試一個多代理協作範例**

官方給出一個 Research Coordinator 範例:單一指令就能建立一個帶有任務導向系統提示、以摘要為基礎的截斷策略的 harness,一次呼叫中依序跑 researcher、synthesizer、reviewer 三個 subagent,最終彙整成一份報告。省略 model、memory、execution role 時,harness 會套用目前建議的模型與受管 memory,CLI 也會自動在 IAM 中建立執行角色。安裝 AgentCore CLI 只需透過 npm,建立完成後用新的 session ID 呼叫,先問一個基本問題,coordinator 會直接回答而不呼叫 subagent;接著在同一 session 要求完整研究報告,coordinator 就會規劃並依序委派給三個 subagent,最多跑一輪 reviewer 要求的修訂迴圈。

⚠️ **限制**

素材僅列出部分生命週期事件(如 `before_tool_call`、`beforeInvocation`、`afterInvocation`),並未完整列出全部四種事件名稱;素材也沒有說明除 Anthropic 模型之外,其他模型供應商的 prompt caching 時程規劃。

🎯 **實務啟示**

如果團隊已經在用 AgentCore harness,這次升級幾乎是無痛的,不需要改整合方式就能拿到新的 context 管理與工具能力。若應用情境涉及高風險動作(退款、刪除資料等),現在可以用 Lambda hook 把審批規則寫成確定性程式碼,而不是只靠 prompt 要求模型自律,這對需要稽核軌跡的場景特別有意義。

🔗 **來源**
- 標題:Amazon Bedrock AgentCore harness adds Strands harness defaults, built-in tools, and lifecycle hooks
- 作者/機構:Evandro Franco @ AWS
- 連結:https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-adds-strands-harness-defaults-built-in-tools-and-lifecycle-hooks/

#AWS #BedrockAgentCore #Strands #AIAgent #LifecycleHooks #AgenticAI #MultiAgent #CloudAI #AgentOrchestration #LLMOps
