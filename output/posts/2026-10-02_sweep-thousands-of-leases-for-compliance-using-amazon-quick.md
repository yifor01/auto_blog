---
title: Sweep thousands of leases for compliance using Amazon Quick and the Adjudicated
  Query pattern
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/sweep-thousands-of-leases-for-compliance-using-amazon-quick-and-the-adjudicated-query-pattern/
model: claude-code/sonnet
generated_at: '2026-10-02T21:38:26.866008'
score: 77
---

📌 規則引擎加對話介面:用AI稽核上萬份租約

TL;DR：AWS提出Adjudicated Query模式，用決定論規則引擎做合規判定，LLM只負責翻譯問題與講解結果。

當RAG的相似度搜尋說「這是最相關的結果」，卻沒人能說出「這代表全部」時，合規稽核這種高風險場景就會出問題，而且錯了也看不出來。

🤔 五萬份租約，遇上不斷變動的法規

文章設定的情境是:一個持有五萬份租約、橫跨多州的不動產營運商，每個州的房東房客法規(滯納金上限、通知期限、押金上限等)各自獨立修法。法規一變，合規團隊就得找出哪些租約已經不合規。小規模時人工審閱還可信，一旦量體變大，工作只能交給軟體，卻冒出新問題:螢幕上跳出的數字，沒有人能獨立驗證。文章指出，這正是合規稽核和一般企業搜尋的本質差異:RAG能解決「找得到資料」的問題，卻解決不了「判定是否完整、正確」這兩個要求。相似度搜尋沒有一個閾值能代表「全部都檢查過了」;排序後取樣，也永遠不知道被排除在外的是什麼。Text-to-SQL雖然能縮小這個落差，但帶著一種類別層級的風險:模型幻覺出的查詢條件，可能悄悄縮小了查詢母體範圍，而算出來的數字看起來依然精確，實際範圍卻是錯的。

🧩 Adjudicated Query:讓LLM只做翻譯與講解

AWS提出的Adjudicated Query模式，把對話介面做成一層有邊界的外殼，包在決定論式的規則引擎外面。模型只做兩件事:把自然語言問題翻譯成對一組固定、型別化操作(typed operations)的呼叫，以及把回傳結果用白話講出來。它不會自己寫查詢、不會決定查詢母體範圍，也不做任何合規判定。規則引擎本身把規則視為「版本化的資料」而非程式碼，只認得gte、lte、equals、exists這類通用比較運算子，程式碼裡不含任何指名特定州或主題的分支。法規一變，只是改一列規則表資料，而不是一次程式部署。每次合規掃描都會產出一張「完整性收據(completeness receipt)」:合規數加違規數加模糊案件數加無法判讀數必須等於掃描總數，這個等式在任何資料落地之前就先被計算與驗證,算不出這筆帳的掃描，根本不會被視為完成，也就沒有紀錄被悄悄漏掉的空間。對話介面只呈現統計數字、完整性收據與抽樣案例;完整的結果集(可能高達數萬列)則留在另一個直接讀同一份資料的儀表板上，逐筆可下鑽查核。

📊 架構組成

整體架構中，合規人員在Amazon Quick裡同時使用對話代理與Quick Sight儀表板兩個介面。對話代理先透過Amazon Cognito取得OAuth權杖，再以MCP(Model Context Protocol)請求經由Amazon API Gateway HTTP API驗證後送進AWS Lambda;Lambda裡同時跑著MCP伺服器與規則引擎，透過RDS Data API讀寫Amazon Aurora Serverless v2(Postgres + pgvector)。Quick Sight儀表板則直接透過VPC連線讀同一份Aurora資料，確保兩個介面看到的是同一套真相來源。Amazon Bedrock只在「探索式條款搜尋」這條支線路徑被呼叫:用Amazon Titan Text Embeddings V2做語意相似度排序，用Anthropic Claude Sonnet 5(透過跨區域推論設定檔)做條款的定性評估,但這條路徑完全不涉及正式的合規判定。MCP伺服器只對外暴露六個工具，每個工具語意明確單一，讓模型沒有辦法組合出錯誤的查詢母體範圍。

⚠️ 模型講解結果時仍要防堵改寫風險

文章特別提醒，把模型排除在「判定」之外，卻又讓它負責把結果「講出來」，等於在流程尾端重新引入風險:團隊在實測中發現講解時可能出現改寫(paraphrase)導致的問題，因此設計了三項工程防護手段來因應,核心原則是,安全保障機制如果撐不過模型的改寫，就等於沒有防護。

🎯 實務啟示

這個模式的適用場景很明確:當使用者需要用對話方式存取資料，而漏掉一筆紀錄會構成真正的法律或財務風險(而不只是體驗上的小瑕疵)時，就該讓LLM只負責「問」與「答」，把「判定」牢牢留在可稽核、可版本控管的規則引擎裡。同樣的架構思路也能套用到制裁名單篩查、保險理賠裁定、出口管制等其他高風險合規領域。

🔗 來源
- 標題：Sweep thousands of leases for compliance using Amazon Quick and the Adjudicated Query pattern
- 作者／機構：Anand Komandooru
- 連結：https://aws.amazon.com/blogs/machine-learning/sweep-thousands-of-leases-for-compliance-using-amazon-quick-and-the-adjudicated-query-pattern/

#AWS #AmazonBedrock #ComplianceAI #RAG #MCP #LLMArchitecture #RulesEngine #AmazonQuick #AuroraServerless #AIGovernance
