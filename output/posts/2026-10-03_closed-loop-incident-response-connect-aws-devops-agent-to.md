---
title: 'Closed-loop incident response: connect AWS DevOps Agent to OpenSearch'
source: Amazon.com
url: https://aws.amazon.com/blogs/devops/closed-loop-incident-response-connect-aws-devops-agent-to-opensearch/
model: claude-code/sonnet
generated_at: '2026-10-03T19:57:28.626848'
score: 79
---

📌 半夜兩點告警響起，讓 AWS DevOps Agent 自己去查根因

TL;DR：用 MCP 把 AWS DevOps Agent 接上 OpenSearch 的可觀測性資料，告警一觸發就自動展開根因調查。

凌晨兩點，告警聲響起，值班工程師還沒睜開眼，AI 代理已經在著手追查根因了。

🤔 事件回應的最後一哩路

當 Amazon OpenSearch Service 的可觀測性資料觸發告警時，傳統流程仍需要工程師醒來後手動排查。這篇 AWS 部落格要解決的，是把「告警」與「自動根因調查」之間的斷點接起來，形成一個封閉迴圈（closed-loop）的事件回應流程。

🧩 用 MCP 串接 DevOps Agent 與 OpenSearch

做法是透過 Model Context Protocol（MCP），將 AWS DevOps Agent 連接到 OpenSearch Service 的可觀測性資料。文章提到涵蓋三種 MCP 伺服器的架設方式，其中一種是在 Amazon EC2 上自行架設（self-managed）。效果是：告警一觸發，代理就能自主展開根因調查，不需要人工先行介入。

🎯 實務啟示

對維運團隊而言，「告警 → MCP → 代理自動調查」是把 LLM 代理接入既有觀測性堆疊的具體案例。如果團隊已經在用 OpenSearch 做日誌與監控，這篇教學提供了用 MCP 把既有資料接上代理工作流程的切入點，值得在正式導入前詳讀原文中三種 MCP 伺服器架設路徑的完整比較。

🔗 來源
- 標題：Closed-loop incident response: connect AWS DevOps Agent to OpenSearch
- 作者／機構：Sitaraman Vijay Krishna, Amazon.com
- 連結：https://aws.amazon.com/blogs/devops/closed-loop-incident-response-connect-aws-devops-agent-to-opensearch/

#AWS #DevOps #OpenSearch #MCP #AIAgents #IncidentResponse #Observability #CloudComputing #SRE #Automation
