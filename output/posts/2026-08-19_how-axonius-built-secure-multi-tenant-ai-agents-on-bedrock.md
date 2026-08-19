---
title: How Axonius built secure multi-tenant AI agents on Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-axonius-built-secure-multi-tenant-ai-agents-on-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-08-19T06:39:12.556471'
score: 82
---

📌 Axonius 如何在 Bedrock AgentCore 上打造多租戶 AI 代理

TL;DR：SaaS 廠商想加 AI agent 又要維持租戶隔離，AgentCore 提供三種架構選擇。

當 SaaS 廠商想替既有平臺加上 AI agent，安全性、擴充性、上市時間、成本追蹤這些老問題會多一個維度：這一切都要落到「每一個租戶」的層級來管理。

🤔 資產智慧平臺的下一步：讓 AI 幫初階分析師做複雜分析

Axonius 是一個資產智慧平臺，協助資安與 IT 團隊釐清風險並協調修復，透過整合 1,400 多個系統的資料成單一可信來源，幫助團隊減少多達 50% 的人工資安、稽核與合規負擔。Axonius 的 SaaS 基礎架構建立在 AWS 上，管理著數百個彼此隔離的客戶環境。他們規劃中的第一個 AI agent，要能解讀大型企業環境的狀態、找出風險缺口，讓初階分析師也能執行原本需要資深分析師耗費數小時才能完成的複雜分析。

🧩 Silo、Pool、Bridge：三種多租戶部署模式

在 Amazon Bedrock AgentCore 上，SaaS 廠商可以選擇的架構模式分成三種。Pool 模式是單一共享 runtime 服務多個租戶，透過 OAuth 2.0 身份提供者（例如 Amazon Cognito）核發的 JWT，內含租戶識別（例如 custom:tenant_id），由 runtime 內建的 JWT authorizer 驗證 token 後，agent 程式碼再依照該claim 把工具呼叫與資料存取導向正確的租戶環境。Bridge 模式則是租戶共用同一個 runtime，但每一次工具呼叫都要先經過 AgentCore Gateway，Gateway 在執行工具程式碼之前，透過 interceptor 與 Cedar policy 兩層機制強制執行租戶邊界，interceptor 會先豐富請求的上下文，讓後續的 policy 評估更精準，同時可以用 RESPONSE interceptor 依租戶身份過濾可被發現的工具。Silo 模式則是每個租戶都有專屬的 AgentCore runtime，存取控制完全交給 IAM，透過 runtime 與其 endpoint 上的 resource-based policy 決定哪些身份（同帳戶角色或跨帳戶身份）可以呼叫該 agent，租戶之間沒有共享運算資源。

無論哪種模式，AgentCore runtime 都會為每一個 session 配置一個獨立 microVM 做運算隔離；差異在於租戶邊界是靠應用層邏輯（Pool）、Gateway 基礎設施層（Bridge）、還是 IAM（Silo）來強制執行。

Axonius 原本就以 Silo 模式運作，每個客戶的工作負載都跑在專屬的 Amazon VPC 裡，裡面有應用程式負載平衡器（ALB）、網路負載平衡器（NLB）、資料庫與一般運算基礎設施。導入 AI agent 時，Axonius 選擇延續這個既有的租戶管理方式：每個客戶都拿到一個專屬的 AgentCore runtime，這個 per-customer agent 用 Claude 做推理，從 Amazon Bedrock Knowledge Base 拉取產品知識，並回頭呼叫該客戶自己的 Axonius API 來回答資料相關問題。整體架構透過 AWS CloudFormation 做自動化的逐客戶佈建與拆除，讓 Axonius 能隨客戶數量擴充 agent 部署。團隊也評估過把 agent 當作額外容器跑在既有 EC2 執行個體上的作法，但最終認為 AgentCore runtime 的內建能力更直接對應他們的多租戶 SaaS 需求。

💡 沒有長效憑證，agent 只借用當下的 JWT

整個設計的信任邊界很清楚：推理、知識檢索與 guardrail 都跑在 Amazon Bedrock 上，權威資料與身份留在每個客戶自己的 VPC，兩端之間的每一跳都走 AWS 私有網路。Agent 本身不持有長效憑證，而是在單次請求的生命週期內借用使用者的 JWT，每一個 session、記憶、工具呼叫與網路路徑都被限定在單一租戶範圍內。

⚠️ 案例聚焦架構選型，未涉及成本與效能細節

素材沒有提供 Axonius 導入後的效能數據、延遲或成本比較，主要價值在於三種租戶隔離模式的權衡說明，實際導入時仍需自行評估各模式在自身場景下的維運複雜度與成本。

🎯 實務啟示

如果你的產品是 B2B SaaS，正在評估要不要把 agent 放進既有多租戶架構，AgentCore 的 Silo／Pool／Bridge 三分法是一個很實用的起手式：先問自己「租戶邊界要在哪一層強制執行」，再決定用 IAM、Gateway 還是應用層邏輯來實作，而不是直接複製別人的架構。

🔗 來源
- 標題：How Axonius built secure multi-tenant AI agents on Bedrock AgentCore
- 作者／機構：Amir Krispin，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-axonius-built-secure-multi-tenant-ai-agents-on-bedrock-agentcore/

#AWS #BedrockAgentCore #MultiTenant #SaaS #AIAgents #CloudArchitecture #IAM #JWT #EnterpriseAI #Claude
