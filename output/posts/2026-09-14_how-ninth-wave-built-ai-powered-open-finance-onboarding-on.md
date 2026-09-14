---
title: How Ninth Wave built AI-powered open finance onboarding on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-14T21:12:14.616349'
score: 76
---

📌 Ninth Wave用七個AI代理，把銀行開放金融對接時間砍下來

TL;DR：Ninth Wave 在 Amazon Bedrock AgentCore 上打造多代理助理 Compass，把過去要靠信件與試算表拉鋸數週的銀行 API 對接流程，變成自助式協作工作區。

一家銀行要加入開放金融（open finance）網路，理論上只要串一次 API；實際上，每家銀行的欄位命名、格式慣例都不同，跟 FDX（Financial Data Exchange）標準之間永遠有落差。驗證 API、比對欄位、評估上線就緒度，過去得靠專家團隊在信件與試算表間來回確認數週。Ninth Wave 決定用 AI 代理系統把這段流程自動化。

🤔 **開放金融的老問題：每家銀行都是一座孤島**

Ninth Wave 的核心業務是把銀行 API 正規化為 FDX 標準，讓銀行只需對接一次 Ninth Wave 平臺，就能連上包含 Plaid、Finicity、MX 等聚合商，以及 Intuit QuickBooks、Xero、Sage 等記帳系統的整個開放金融網路。但正規化之前的「驗證與映射」階段，仍高度仰賴人工判讀每家銀行 API 與 FDX 標準的落差。為此，Ninth Wave 打造了 AI 上線助理 Compass，讓銀行工程師、聚合商整合團隊與 Ninth Wave 自家的上線團隊，能在同一個 AI 協作工作區裡完成對接。

🧩 **為何選多代理架構，而不是單一 RAG**

團隊評估過兩種替代方案：在 Amazon EC2 上自架模型，可以完全掌控但維運負擔重；單一代理的 Retrieval Augmented Generation（RAG）架構較簡單，但在映射、分析、搜尋、互動問答等不同任務上準確度不足。最終選擇多代理架構：前期設計成本較高，但每個代理只專注單一任務、擁有自己的情境與指令提示，不會互相搶佔 prompt 空間，準確度也能隨任務類型增加而擴展。

架構上，請求進入系統後會經過幾個關鍵環節：
- 邊緣安全層：流量先經過 Amazon CloudFront（TLS 1.2+、HSTS）與 AWS WAF v2 的預設拒絕規則過濾，確保每個請求在進入應用邏輯前就先限定在單一銀行租戶範圍內。
- 身分驗證：Amazon ECS on AWS Fargate 對接強制多因子驗證（MFA）的 OAuth2/OIDC 身分提供者，並透過 AWS Secrets Manager（每個環境獨立的客戶自管 KMS 金鑰）取得憑證，AWS IAM 落實最小權限，AWS CloudTrail 記錄 API 活動。
- 租戶隔離的資料基底：呼叫代理前，Compass 會先從 Amazon OpenSearch Service（依租戶分索引）與 Amazon S3（依租戶分前綴）取出該銀行專屬的 API 文件、設定資料與過往互動紀錄，避免不同銀行的資料在共用模型基礎設施上互相滲透。
- 多代理協作：經過情境組裝的請求會透過跨帳戶 IAM 角色進入獨立的 Amazon Bedrock AgentCore 執行環境，讓 AI 工作負載與應用工作負載在帳戶層級分離。由 Strands Agents 框架搭建的 Primary Compass Agent 負責意圖分類，並路由到七個專責代理之一。
- 知識庫檢索：其中負責「就緒度分析」的代理是唯一會查詢 Amazon Bedrock 知識庫的代理，因為它需要綜合一整批份量過大、無法一次塞進單一請求的 FDX 參考文件，其餘代理則完全在應用層取得情境，方便團隊自行掌控檢索邏輯與排序。
- FDX 就緒度分數：這個分數並非由模型估算，而是根據 OpenSearch 中必要欄位的映射覆蓋率，以應用程式碼確定性地算出，滿足稽核對可驗證性的要求。
- 可觀測性：ECS 會把每個代理的呼叫次數、token 用量、延遲與成本送到 Amazon CloudWatch，透過 Amazon SNS 發出告警，並匯入 Amazon Managed Grafana 儀表板，讓團隊能在單一代理層級偵測效能退化。

💡 **分而治之，讓準確度隨任務數量成長**

這套架構的核心設計哲學是「意圖分類先行、上下文互不干擾」：一個映射請求不會與文件搜尋請求爭奪 token 空間，行為與安全邊界也是在應用層逐一代理設定，調整一個代理的範圍不會波及其他代理。Amazon Bedrock 則把多代理編排、多模型存取、IAM／KMS／私有網路等企業級安全控管整合在單一服務內，讓團隊可以專注在領域邏輯，而不是自建大型語言模型基礎設施。

專案以五個聚焦的衝刺（sprint）逐步交付：第一階段建立 AI 應用基礎，包含依租戶分索引的 OpenSearch、S3 文件與知識庫儲存，以及用 AWS CDK 管理跨工作負載、Bedrock、共享服務帳戶的 CloudFormation 堆疊，並設定好按任務混搭模型的 AgentCore 與跨帳戶 IAM 角色；第二階段則打造銀行工程師與聚合商夥伴實際互動的開發者入口網站，包括自動化的映射指南產生、上線腳本與客製化品牌的夥伴入口。

🎯 **實務啟示**

對正在評估多代理系統的團隊而言，Ninth Wave 的取捨提供了一個清楚的判斷依據：當任務類型夠多、彼此對準確度要求夠高時，把單一代理拆成多個專責代理，即便前期設計成本較高，長期反而更容易擴展；而像「合規分數」這種需要可稽核性的輸出，交給確定性的應用邏輯計算，會比讓模型直接生成更站得住腳。

🔗 **來源**
- 標題：How Ninth Wave built AI-powered open finance onboarding on Amazon Bedrock
- 作者／機構：Shawn Kelly, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-ninth-wave-built-ai-powered-open-finance-onboarding-on-amazon-bedrock/

#AmazonBedrock #AgentCore #MultiAgent #OpenFinance #FDX #AIOnboarding #AWS #StrandsAgents #FinTech #CloudArchitecture
