---
title: Automated agent evaluation with Amazon Bedrock AgentCore and GitHub Actions
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/automated-agent-evaluation-with-amazon-bedrock-agentcore-and-github-actions/
model: claude-code/sonnet
generated_at: '2026-09-08T20:10:55.279375'
score: 87
---

📌 用 GitHub Actions 幫 Agent 建一道「品質關卡」:AWS Bedrock AgentCore 實戰

TL;DR：AWS 展示如何用 AgentCore Evaluate API 搭配 GitHub Actions,在 PR 階段自動偵測 agent 品質退化並擋下合併。

工程師改了一段 system prompt,agent 開始給出更差的答案,卻要等到使用者抱怨才會被發現——這是多數團隊在 agent 開發上遇到的共同痛點。AWS 這篇文章給出一套具體做法:把 agent 評估變成 CI 流程裡會擋 PR 的關卡。

🤔 **OAuth 保護的 MCP 伺服器,CI 該用誰的身分**

情境是這樣的:agent 部署在 Amazon Bedrock AgentCore runtime 上,透過受 OAuth 保護、具角色權限控管的 MCP 伺服器呼叫工具。每次有人改 system prompt、換模型或調整工具設定,團隊都想知道 agent 是變好還是變差,但人工測試無法規模化。難題在於 CI pipeline 沒有使用者情境(user context),而 MCP 伺服器預期收到的是帶角色宣告的 JWT——headless 的 CI runner 沒辦法走互動式 OAuth 同意流程。

🧩 **AgentCore Evaluations:建立在既有 trace 之上的評分層**

AgentCore Evaluations 是 Bedrock AgentCore 平臺中的品質量測層,與負責承載 agent 的 AgentCore runtime、負責擷取 trace 的 AgentCore Observability 並列,共同組成 build → deploy → observe → evaluate 的生命週期。它預設用 LLM-as-a-judge 評分,也可選擇透過 AWS Lambda 做程式碼式評估,運作基礎是 agent 本來就會透過 Observability 送出的 OpenTelemetry trace。文章列出三種評估模式:即時評估直接在 API 呼叫中提供 span 資料,線上與批次評估則從 CloudWatch 讀取。Evaluate API 接收 sessionSpans,每次呼叫只能包含單一 session 的 trace,混用會觸發 ValidationException;也可透過 evaluationReferenceInputs 提供選用的 ground truth,例如給 Correctness 用的 expectedResponse、給 GoalSuccessRate 用的 assertions、給軌跡評估器用的 expectedTrajectory,沒有 ground truth 時則退回無真值評估。

架構上,pipeline 在共用的 Cognito user pool 之下部署兩個 AgentCore runtime,一個跑 Strands agent、一個跑 MCP 伺服器;同一個 Cognito pool 同時服務機器對機器(M2M)與使用者範圍(user-scoped)兩種驗證流程。GitHub Actions workflow 會把 agent 堆疊部署到開發環境,向 Cognito 取得 JWT,用評估資料集呼叫 agent,再分析 CloudWatch Logs 中產生的 trace,依門檻自動核准或擋下 PR。

💡 **三種繞過 OAuth 難題的做法,權衡各不相同**

文章給出三種方案。方法 A 是把評估與即時 MCP 呼叫完全解耦:staging pipeline 先跑一次 agent,把 trace 存成 JSON fixture,PR 階段直接評估這些既有 trace,不需要即時呼叫,也就完全繞開 OAuth 問題,缺點是評估的是 staging 部署的行為,而非當前 PR 的程式碼(對照 repo 中的 evaluate_stored_traces.py 與 fixtures 目錄)。方法 B 是建立專用測試使用者,手動完成一次 OAuth 同意流程,把 refresh token 存進 Secrets Manager 供 CI 使用,缺點是 token 會過期,需要輪替機制。方法 C 是讓 MCP 伺服器同時支援 M2M 與 user-scoped 兩種授權類型:CI 用 M2M token(只有 scope、沒有角色宣告,因此角色檢查會被跳過,可存取所有工具),互動使用者則走一般 OAuth 流程,持有帶 custom:roles 宣告的 token 並受角色限制存取工具。這個跳過機制之所以安全,是因為 M2M token 需要用戶端密鑰(client secret),而該密鑰從不會暴露給終端使用者。文章建議先用方法 A 快速建立品質關卡,再進階到方法 C,以取得真正測試 PR 程式碼變更的端到端 CI。

方法 C 的 MCP 伺服器靠三層機制運作:第一層是 AgentCore 平臺透過 Custom JWT Authorizer 在請求進入程式碼前驗證簽章、發行者、受眾與過期時間,不需額外實作;第二層透過在兩個 runtime 上設定 request_header_allowlist=["Authorization"],讓 JWT 原封不動轉發到 agent 與 MCP 容器;第三層是一個 FastMCP 原生 middleware(AuthMiddleware),透過 fastmcp.server.dependencies.get_http_headers() 讀取 JWT、用 PyJWT 解碼宣告,並依工具的 meta 資訊檢查 custom:roles——M2M token 取得完整存取權,使用者 token 則必須符合對應角色。整個 Cognito pool、兩個 runtime、IAM 角色與預建測試使用者,都由一份 CDK 堆疊一鍵部署完成。

🎯 **實務啟示**

如果你的 agent 架在 AgentCore 上,想要把「agent 有沒有變差」這件事從主觀感受變成 CI 訊號,可以直接參考本文附上的完整參考實作。若團隊還沒準備好處理 OAuth 與角色權限的複雜度,先用方法 A(儲存 trace + 離線評估)是成本最低的起點,之後再視需要升級到方法 C 做端到端驗證。

🔗 **來源**
- 標題：Automated agent evaluation with Amazon Bedrock AgentCore and GitHub Actions
- 作者／機構：Mahsa Paknezhad, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/automated-agent-evaluation-with-amazon-bedrock-agentcore-and-github-actions/

#AWS #BedrockAgentCore #CICD #AIAgents #GitHubActions #MCP #OAuth #MLOps #LLMEvaluation #AgenticAI
