---
title: Authenticate with Private Key JWT using Amazon Bedrock AgentCore Identity
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/authenticate-with-private-key-jwt-using-amazon-bedrock-agentcore-identity/
model: tencent/hy3:free
generated_at: '2026-07-30T08:30:03.980666'
score: 71
---

📌 【AWS 新功能】Amazon Bedrock AgentCore Identity 支援 Private Key JWT，提升 Agent 認證安全性

TL;DR：AgentCore Identity 現在支援使用 Private Key JWT 進行認證，取代傳統的 OAuth 2.0 Client Secret。

🤔 **為何不再僅依賴 Shared Client Secret？**

在傳統的 OAuth 2.0 流程中，Agent 通常使用一個共享的 Client Secret 來向身份提供者（Identity Provider, IdP）請求 Token。然而，這種方式存在安全性風險，因為 Secret 必須在兩端傳遞或儲存。

🧩 **透過 Private Key JWT 實現更安全的認證流程**

Amazon Bedrock AgentCore Identity 現在支援使用「簽署過的 JSON Web Token (JWT) 客戶端斷言（Client Assertion）」來進行認證。其設計核心在於：

1. **非對稱加密**：你只需在身份提供者（IdP）端註冊公鑰（Public Key），而對應的私鑰（Private Key）則安全地儲存在 AWS Key Management Service (AWS KMS) 中。
2. **簽署與驗證**：當 Agent 需要認證時，AgentCore Identity 會調用 AWS KMS 進行簽署，並將簽署後的 JWT 發送給 IdP；IdP 則使用預先註冊的公鑰來驗證該斷言。
3. **減少機密洩漏風險**：由於私鑰始終留在 AWS KMS 內，從而避免了在傳輸或設定過程中洩漏 Client Secret 的問題。

📊 **支援的授權流程與應用場景**

此功能支援三種授權流程（Grant Flows），適用於機器對機器（Machine-to-Machine）的 Token 請求場景。

例如：一個客戶支援型 Agent 需要從受保護的內部訂單 API 讀取客戶的訂單歷史紀錄。透過此機制，Agent 能以安全的方式向保護該 API 的 IdP 請求存取權限。

💡 **實作步驟概覽**

若要在 AWS Management Console 上配置此功能，流程如下：

1. **建立 KMS 簽名金鑰**：建立一個非對稱（Asymmetric）的 AWS KMS 金鑰，供 AgentCore Identity 用於簽署 JWT。
2. **註冊公鑰**：將對應的公鑰匯出並註冊到你的身份提供者（IdP）。
3. **配置憑證提供者**：在 AWS 管理控制台中，將此方法配置為 Agent 的憑證提供者。
4. **稽核與追蹤**：所有的 Agent 存取行為都會被記錄在 AWS CloudTrail 事件中，便於審計。

*註：若你的 IdP 已產生金鑰對並提供私鑰，你也可以選擇將其匯入（Import）至 AWS KMS 中。*

🎯 **實務啟示**

對於需要串接內部企業系統（如訂單系統、客戶資料庫）的 AI Agent 開發者來說，改用 Private Key JWT 能顯著提升安全性。建議在設計 Agent 架構時，優先考慮將敏感的認證金鑰封裝在 KMS 中，而非直接在設定檔中寫死 Client Secret。

🔗 **來源**
- 標題：Authenticate with Private Key JWT using Amazon Bedrock AgentCore Identity
- 作者／機構：Swara Gandhi @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/authenticate-with-private-key-jwt-using-amazon-bedrock-agentcore-identity/

#AWS #AmazonBedrock #AgentCoreIdentity #KMS #JWT #OAuth2 #MachineLearning #CyberSecurity #CloudComputing #AIagents
