---
title: 'Multi-tenant LLM analytics with row-level security: How we built a secure
  agent on AWS'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/multi-tenant-llm-analytics-with-row-level-security-how-we-built-a-secure-agent-on-aws/
score: 86
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:34:16.568317'
---

📌 【AWS 實作分享】如何建立具備 Row-Level Security 的多租戶 LLM 分析代理人？

TL;DR：透過三層架構（SigV4 簽名、Bedrock 語義驗證、Split-Plane SQL）確保多租戶 LLM 分析系統的資料隔離。

當企業將 LLM 引入資料分析，最令人不安的風險不是 AI 產生幻覺，而是「許可權越界」：如果兩個不同公司的經理問同樣的問題，AI 是否會不小心把 A 公司的銷售額回報給 B 公司？

🤔 **多租戶環境下的 Text-to-SQL 安全挑戰**

PAR Technology 為超過 300 家餐飲企業提供技術支援，其目標是讓非技術使用者能用自然語言詢問業務問題並快速獲得答案。然而，在這種規模的系統中，挑戰不在於生成 SQL 語法，而是在於如何確保每一筆查詢都嚴格限制在該使用者的授權範圍內。

例如，當兩位使用者同時詢問「上週總銷售額是多少？」時，系統必須根據身分精準區分：加盟商只能看到其經營的兩間分店資料（例如 84,000 美元），而品牌經理則應看到整個品牌的資料。

🧩 **三層防禦架構：防止跨租戶資料洩漏**

為了確保即使 LLM 被操縱或失效也不會導致資料外洩，PAR 採取了三層獨立運作的防禦機制：

1. **請求簽名層 (Cryptographic Request Signing)**：利用 AWS SigV4 進行加密簽名，從最底層確保請求的合法性。
2. **語義驗證層 (Semantic Validation)**：透過 Amazon Bedrock 進行語義層級的驗證，確保 LLM 生成的意圖符合預期。
3. **資料隔離層 (Programmatic Data Isolation)**：採用 Split-Plane SQL 進行程式化資料隔離，從執行面強制執行 Row-Level Security (RLS)。

這三層架構相互獨立，旨在將資料存取、正確性與安全性在規模化運作時同步達成，確保每個使用者僅能存取其授權的資料切片。

🎯 **實務啟示**

對於開發企業級 AI Agent 的工程師來說，這提供了一個關鍵思考：**不要將安全性寄託在 LLM 的 Prompt 上**。

單純依靠 Prompt 要求 LLM 「請不要存取其他租戶資料」是不夠的。真正的企業級隔離必須將安全邏輯從 LLM 中抽離，透過底層的加密簽名與資料庫層級的強制隔離（如 Split-Plane SQL）來建立硬性防線，將 LLM 定位為「翻譯者」而非「許可權管理員」。

🔗 **來源**
- 標題：Multi-tenant LLM analytics with row-level security: How we built a secure agent on AWS
- 作者／機構：Anuranjan Mondal / AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/multi-tenant-llm-analytics-with-row-level-security-how-we-built-a-secure-agent-on-aws/

#AWS #LLM #MultiTenancy #TextToSQL #DataSecurity #RowLevelSecurity #AmazonBedrock #EnterpriseAI #DataIsolation #CloudArchitecture
