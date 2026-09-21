---
title: How Benchling secured multi-tenant AI agents with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-21T21:16:39.319457'
score: 96
---

📌 Benchling 如何讓 AI Agent 生成的程式碼跑在數千個租戶上而零資安事故

TL;DR：靠 Amazon Bedrock AgentCore 搭配獨立帳號、DNS Firewall 與 VPC endpoint 政策，Benchling 每天安全跑 600 多次程式碼執行工作。

讓 AI agent 幫研究人員即時生成並執行科學運算程式碼，聽起來很方便，但當服務對象是數千個受監管的生技產業租戶，「傳統沙箱夠不夠」就不再是個假設性問題。Benchling 的資安團隊發現，就算擋掉了 HTTP、限制了 outbound port，DNS 解析往往還是留著一道後門，而且系統預設的限制未必在你的可視範圍與控制之內。

🤔 **問題：既要隔離租戶，又不能養出上千個 IAM 角色**

Benchling 的資安需求相當明確：每個執行 session 只能存取該租戶自己的資料，不能有跨租戶的可視性；程式碼不能建立未授權的網路連線，也不能透過任何管道外洩資料；每個執行 session 必須完全隔離；而且解決方案不能靠「一個租戶一個 IAM 角色」來達成，因為在這個規模下會造成角色數量失控（role sprawl）。

在安全審查階段，團隊評估了 Amazon Bedrock AgentCore Code Interpreter 各種網路模式的隔離特性。Sandbox 模式雖然把出向流量限制在 Amazon S3 操作，但 Benchling 的資安基準要求的是「客戶自己掌控」的網路隔離——他們要能精確定義哪些網域可以解析、哪些端點可以連線，並透過自己的整合測試套件持續驗證這些控制。對於處理受監管生技資料、面對數千租戶的應用來說，光靠應用層自行管理的網路限制並不足夠。

🧩 **縱深防禦架構：獨立帳號 + DNS 三層防火牆 + VPC endpoint**

Benchling 的解法是把不受信任的程式碼執行整個搬到一個獨立的 AWS 帳號（Untrusted Code Account），與主要正式環境帳號分開。這個帳號裡放置 AgentCore Code Interpreter（ACCI），也並存 Benchling 既有的、基於 gVisor（一種攔截系統呼叫、提供核心層級隔離的容器沙箱執行環境）的容器執行環境；後者是既有的運算隔離層，並非本文所述架構的一部分。兩套執行環境各自擁有範圍受限的 IAM 角色，確保彼此都無法越權存取超出各自邊界的資源。

任務從正式環境帳號派送到未受信任帳號時，資料存取是逐工作（per-job）授權：只有該工作實際需要的特定資料才會被開放存取，正式環境的憑證與更大範圍的客戶資料儲存都不會直接暴露給未受信任的程式碼。為了避免維護上千個租戶各自的 IAM 角色，Benchling 改用 AWS STS，在每個 ACCI session 建立時動態注入逐工作的憑證，而不累積靜態角色。

ACCI 所在的 VPC 採「預設全擋，明確允許才放行」的設計：沒有 Internet gateway，也沒有 NAT gateway，裡面執行的程式碼無法直接連上網際網路。Code Interpreter 運行在專屬的 Security Group 中，僅開放 443 埠，且沒有通往公開網際網路的出向路徑。

DNS 外洩防禦的核心是 Amazon Route 53 Resolver DNS Firewall，採用三層優先級的 resolver policy，遵循「黑名單、白名單、全擋」的模式：優先級 10 先擋掉已知的惡意網域，作為威脅情資的快速通道，同時這一層的查詢紀錄也能提早示警沙箱內是否有可疑行為；優先級 100 只允許明確列在白名單上的端點解析，實務上這份清單被刻意壓到只剩下工作執行所需的 S3 端點；優先級 200 則擋掉其餘所有查詢。VPC Endpoints（一個 S3 Gateway endpoint 加一個 Interface endpoint）提供僅有的合法網路路徑，並透過 NACL 與 Prefix List 路由把流量限制在這些端點上。

一套持續驗證（Continuous Validation）套件會跑整合測試，模擬資料外洩嘗試，用來驗證整套配置是否仍然有效。

📊 **上線後的規模與結果**

這套架構目前每天處理超過 600 次程式碼執行 session，覆蓋每週超過 250 個租戶，至今零資安事故。

🎯 **實務啟示**

這個案例的價值在於它точно指出多租戶 AI agent 沙箱最容易被忽視的破口：DNS 解析。即使你已經擋掉了 outbound HTTP 和限制了連接埠，只要 DNS 還能解析出未授權的網域，資料外洩的路徑就還在。把「拒絕解析未授權網域」和「拒絕連線未授權端點」拆成 DNS Firewall 與 VPC endpoint policy 兩道獨立防線，再用獨立帳號做爆炸半徑（blast radius）隔離、STS 逐工作授權取代角色爆炸，是把多租戶執行不受信任程式碼這件事做到可稽核、可持續驗證的具體範本。

🔗 **來源**
- 標題：How Benchling secured multi-tenant AI agents with Amazon Bedrock AgentCore
- 作者／機構：Jeremy Stashewsky, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-benchling-secured-multi-tenant-ai-agents-with-amazon-bedrock-agentcore/

#AWSBedrock #AgentCore #AIAgentSecurity #MultiTenant #DNSFirewall #CloudSecurity #VPC #ZeroTrust #LifeSciences #SecureAI
