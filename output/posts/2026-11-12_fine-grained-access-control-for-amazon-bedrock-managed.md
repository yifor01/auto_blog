---
title: Fine-grained access control for Amazon Bedrock Managed Knowledge Base tools
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/fine-grained-access-control-for-amazon-bedrock-managed-knowledge-base-tools/
model: claude-code/sonnet
generated_at: '2026-11-12T22:58:47.763684'
score: 93
---

📌 【AWS技術解析】同一個Agent、同一個知識庫，如何確保每個員工只看到自己的文件？

TL;DR：AWS示範如何在Bedrock AgentCore Gateway層注入驗證身分，避免LLM自己決定搜尋權限。

員工問內部助理「比較我部門的業務計畫和全公司通知，列出落後的項目」，另一個部門的員工問了完全一樣的問題——如果系統沒有針對使用者做搜尋範圍限制，A部門員工的答案裡可能混進B部門的機密業務計畫。這不是假設，而是企業導入共享 Agent 之後必須正面處理的問題。

🤔 **LLM決定查詢參數，身分驗證就出現破洞**

在傳統應用程式裡，程式碼本身會判斷登入使用者是誰，再用該使用者的權限去搜尋。但在 Agent 架構裡，大型語言模型（LLM）在執行時自行決定呼叫哪個工具、帶什麼參數。如果搜尋工具把「以誰的身分搜尋」當成參數，LLM 就能自己決定這個值——一旦遇到 prompt injection 或模型判斷錯誤，Agent 就可能用錯誤的身分去搜尋，讓資料外洩到不該看到的人手上。這個問題在多租戶（multi-tenant）SaaS 架構下同樣存在，只是把部門換成客戶公司。

AWS 在這篇文章中用一家虛構公司 AnyCompany 做示範：知識庫裡存放了A部門業務計畫、B部門業務計畫、以及全公司通知三份文件，user-a 與 user-b 兩位使用者透過同一個 Agent 搜尋。

🧩 **把身分驗證從LLM手中拿回來，分層防守**

這個方案的核心設計原則是：絕對不讓 LLM 自己決定使用者是誰，而是由可信任的程式碼根據身分提供者（identity provider）驗證過的資訊來決定，並在此之上疊加多層獨立防線。

架構用的是 Amazon Bedrock Managed Knowledge Base 作為搜尋後端，透過 Amazon Bedrock AgentCore Gateway 把它包裝成 MCP（Model Context Protocol）工具，並以 Strands Agents 打造、部署在 AgentCore runtime 上的 Agent 來呼叫，預設使用 Claude Sonnet 5.5（透過 global cross-Region 推論設定檔 global.anthropic.claude-sonnet-5-5）。整個 Agent 本身不含任何權限控制邏輯，只把登入使用者的 access token 轉送給 Gateway。

真正做事的是兩個關鍵機制：

- Gateway層的 request interceptor：在工具呼叫發出前，把已驗證的使用者屬性注入到 tool call 的參數裡，而不是讓 LLM 自己填。
- Managed Knowledge Base的 ACL awareness：搜尋請求帶上 userContext（包含使用者的 email，放在 userId 欄位）時，知識庫只回傳該使用者有權限看到的文件。

ACL 的定義方式，是在 Amazon S3 資料來源的每份文件旁放一個 metadata 檔案（也可以用整個 S3 前綴共用一份全域 ACL 檔案）。沒有 ACL 項目的文件不會被納入索引；更改全域 ACL 檔案需要重新索引整個前綴，而逐文件的 metadata 檔案只需重新索引受影響的文件，且優先權高於全域檔案。

AWS 另外補上兩層次要防線：AgentCore 的 Policy，以及 Knowledge Base 的 resource-based policy——後者是給帳號中其他擁有 bedrock:Retrieve 權限的呼叫者使用，屬於保險機制。

⚠️ **ACL awareness不是萬能鎖**

文章特別強調，ACL awareness 本身信任它收到的 userContext，並不做身分驗證，驗證身分永遠是呼叫端的責任。而且 S3 沒有即時的 ACL 驗證機制，ACL 變更要等下一次同步才生效；更麻煩的是 ACL 設定錯誤不會跳出任何錯誤訊息，受影響的文件只會悄悄地被排除在搜尋結果外，排查起來並不直覺。

🎯 **實務啟示**

對正在把內部文件搜尋包進 Agent 工具鏈的工程團隊來說，這篇文章給出一個清楚的設計準則：身分判斷永遠要交給可信任的程式碼層（如 Gateway 的 interceptor），絕不能讓 LLM 的工具呼叫參數變成權限邊界。AWS 也把整套架構包成單一 AWS CDK stack（repo：sample-managed-knowledge-base-patterns 的 agentcore-access-control 目錄），方便直接部署驗證。

🔗 **來源**
- 標題：Fine-grained access control for Amazon Bedrock Managed Knowledge Base tools
- 作者／機構：Renya Kujirada
- 連結：https://aws.amazon.com/blogs/machine-learning/fine-grained-access-control-for-amazon-bedrock-managed-knowledge-base-tools/

#AWSBedrock #AgentCore #AccessControl #MultiTenant #RAG #MCP #AIAgents #LLMSecurity #KnowledgeBase #CloudSecurity
