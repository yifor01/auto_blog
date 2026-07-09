---
title: Securing Amazon Bedrock AgentCore Runtime with AWS WAF
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/securing-amazon-bedrock-agentcore-runtime-with-aws-waf/
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T10:01:23.228584'
---

📌 【AWS 技術分享】如何透過 AWS WAF 為 Amazon Bedrock AgentCore 建立安全防線？

TL;DR：透過 ALB 與 VPC Endpoint 整合 AWS WAF，並解決 AgentCore 認證導致的健康檢查失效問題。

當你將 Amazon Bedrock AgentCore 的生成式 AI Agent 部署為生產環境的 API 端點時，單純的 API 呼叫是不夠的。你需要 WAF 來實施速率限制（Rate Limiting）、防禦常見網頁威脅以及建立稽核控制，但如何在不破壞認證機制的狀況下完成整合？

🤔 **為什麼選擇 ALB 而非 CloudFront 或 API Gateway？**

在選擇整合 AWS WAF 的路徑時，作者分析了三種方案的適用性：
- **Amazon CloudFront**：主打快取與內容傳遞，但 Agent 呼叫是即時且動態的，快取機制並不適用。
- **Amazon API Gateway**：雖可整合，但其自有的認證與請求轉換層，容易與 AgentCore 內建的 SigV4 或 OAuth 產生「雙重認證」衝突。
- **Application Load Balancer (ALB)**：最理想的選擇。它能透明地傳遞 Header、支援 VPC 內部路由，且可直接掛載 AWS WAF 的 WebACL。

🧩 **核心挑戰：認證機制導致健康檢查失效**

雖然 ALB 是最佳整合點，但會遇到一個技術瓶頸：**健康檢查（Health Checks）**。
ALB 需要透過健康檢查確認後端目標是否可用，但 AgentCore Runtime 要求所有 API 呼叫（包含健康檢查）都必須經過 SigV4 或 OAuth 認證。由於標準的 ALB 健康檢查傳送的是「未認證請求」，導致請求在預設情況下會直接失敗。

💡 **兩種解決健康檢查問題的架構模式**

為了在維持生產流量認證的同時讓健康檢查通過，本文提出了兩種模式，兩者皆透過 VPC Interface Endpoint 連線至 AgentCore Runtime：

- **模式 1：Lambda Proxy 代理**
  在 ALB 與 VPC Endpoint 之間放置一個 AWS Lambda 函式。這讓開發者能完全控制請求的轉換（Request Transformation），藉此處理健康檢查與認證的邏輯。
- **模式 2：直接對接 ENI IP**
  ALB 直接將流量導向 VPC Endpoint 的彈性網路介面（ENI）IP 位址，完全移除 Lambda 這一層跳轉，降低延遲。

⚠️ **防止後門：使用資源原則（Resource Policy）**

為了確保安全性，不能僅僅在前端加上 WAF。作者提醒必須設定資源原則，關閉直接存取 AgentCore 的後門，強制所有流量必須經過 AWS WAF 與 ALB 的路徑。

🎯 **實務啟示**

對於需要在企業級環境部署 AI Agent 的工程師，這套方案提供了在「強認證」與「基礎設施監控」之間取得平衡的方法。關鍵在於利用 ALB 作為 WAF 的進入點，並針對 AgentCore 的認證特性調整健康檢查路徑，最後以資源原則封鎖非授權路徑。

🔗 **來源**
- 標題：Securing Amazon Bedrock AgentCore Runtime with AWS WAF
- 作者／機構：Puneeth Komaragiri @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/securing-amazon-bedrock-agentcore-runtime-with-aws-waf/

#AWS #AmazonBedrock #AWSWAF #ALB #CloudSecurity #GenerativeAI #VPC #AgentCore #NetworkSecurity #AWSArchitecture
