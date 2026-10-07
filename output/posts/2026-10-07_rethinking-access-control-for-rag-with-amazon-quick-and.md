---
title: Rethinking access control for RAG with Amazon Quick and Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/rethinking-access-control-for-rag-with-amazon-quick-and-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-07T22:20:14.734397'
score: 93
---

📌 RAG 權限控管新解法：Amazon Quick 與 Bedrock 的即時 ACL 架構

TL;DR：以「快照式權限同步」是企業 RAG 的安全漏洞，AWS 改用查詢當下即時驗證權限的雙層架構。

🎣 想像一位員工昨天被公司撤銷了某份機密文件的存取權，但今天他問 AI 助理同樣的問題，助理卻還是把文件內容吐了出來。這不是假設情境，而是企業導入 RAG（Retrieval Augmented Generation）時最容易忽略的安全破口。

🤔 「複製再過濾」式的權限控管，三個結構性弱點

企業知識庫通常橫跨 SharePoint、Google Drive、Confluence 等多個系統，每個系統各自有一套複雜的權限模型。文章指出，常見的 RAG 存取控制做法是把文件層級的權限（ACL）複製一份到 AI 系統裡做過濾，但這種做法有三個根本問題：

- AI 系統自行扛起權限執行責任，卻不是權限的權威來源，必須靠連接器（connector）精準複製各來源各自獨立的繼承階層、群組成員、條件式存取與拒絕規則，非常容易出錯。
- 多數連接器採用「拉取式」排程同步，ACL 只是最後一次同步時的快照；即便有事件驅動更新，也並非每個來源都支援，例如 Confluence 並不會在群組成員變動時發出事件通知。
- 資料來源本身的權限機制會不斷演進，SharePoint 或 Google Drive 任何一次權限模型的調整，都可能在連接器更新之前產生曝險缺口。

🧩 雙層架構：快取過濾 + 查詢當下即時驗證

為了解決這個問題，Amazon Quick 與 Amazon Bedrock Knowledge Bases 在既有的「檢索前 ACL 過濾」之上，再疊加一層即時驗證：

1. 使用者對使用 Google Drive 知識庫的 Amazon Quick agent 提問時，系統先對向量索引做語意搜尋，並套用索引中已儲存的 ACL，產生一組候選文件（這一步是為了避免對索引中每份文件都即時呼叫 API，否則大規模下成本過高）。
2. 接著 Amazon Quick 即時呼叫 Google Drive API，透過管理員提供的服務帳號憑證，以模擬（impersonation）方式產生使用者專屬的存取權杖，向 Google Drive（也就是權限的權威來源）逐一驗證候選文件。
3. 使用者未獲授權的文件會被排除，只有通過驗證的文件段落才會被送進 LLM 作為上下文生成回答。

這個設計用快取 ACL 保住效能，再用即時驗證補上正確性，另外還搭配 Amazon Bedrock Guardrails 做內容過濾、grounding 檢查降低幻覺，以及可設定的安全政策。

📊 已在超過 35,000 名員工規模落地

文章引用 Mondelēz International 的 M365 Innovation 資深專員 Jamahl Wiggins 的說法：公司的安全與合規團隊在評估 AI 方案時最在意「同事只能看到自己有權限的資訊」，而 Amazon Quick 的即時存取控制設計讓內部審查委員會有信心推進，並為 AI 治理打下基礎。文章提到 Mondelēz 已在四個地區、超過 35,000 名員工規模導入 Amazon Quick。

🎯 實務啟示

如果你的團隊正在設計企業 RAG 系統，這個架構提供一個可借鏡的原則：權限過濾不能只靠「同步快照」，應該把「檢索前過濾」與「查詢當下對權威來源做即時驗證」分成兩層來設計，尤其是在處理敏感文件（策略文件、財務數據、HR 資訊）時，即時驗證是避免存取控制「過期」的關鍵最後一道防線。

🔗 來源
- 標題：Rethinking access control for RAG with Amazon Quick and Amazon Bedrock
- 作者／機構：Amit Choudhary，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/rethinking-access-control-for-rag-with-amazon-quick-and-amazon-bedrock/

#RAG #AccessControl #AmazonBedrock #AWS #EnterpriseAI #AIGovernance #Security #KnowledgeBase #LLM #CloudSecurity
