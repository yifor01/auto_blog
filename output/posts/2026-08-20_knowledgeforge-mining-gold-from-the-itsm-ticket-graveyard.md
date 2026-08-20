---
title: 'KnowledgeForge: mining gold from the ITSM ticket graveyard'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/knowledgeforge-mining-gold-from-the-itsm-ticket-graveyard/
model: claude-code/sonnet
generated_at: '2026-08-20T06:33:31.095870'
score: 91
---

📌 從結案工單裡挖出知識庫：AWS KnowledgeForge 如何自動生成又自我清理

TL;DR：KnowledgeForge 用 Bedrock、S3 Vectors 與 Step Functions，把已結案的 ITSM 工單自動轉成知識庫文章，同時清理既有內容。

企業 IT 支援團隊每個月結案數千張工單，每一張都藏著症狀、根因與解法，但這些知識通常只留在工單歷史裡，下一位遇到同樣問題的工程師根本找不到。知識庫本身也沒好到哪去：重複文章持續累積，內容逐漸過時，品質因撰寫者與時間而參差不齊。AWS 提出的 KnowledgeForge，就是想同時解決「工單知識流失」與「知識庫品質腐化」這兩個對立的問題。

🤔 兩個方向相反的問題

支援工程師搜尋答案時，常要在一堆近乎相同的草稿裡篩選，有些正確、有些卻是三個產品版本前的舊資料。這種混亂並非單一原因造成，而是知識庫長期缺乏系統性維護的結果，同時大量有價值的解法又困在已結案工單裡，從未被整理成文件。

🧩 生成與整理，兩套子系統互相餵養

KnowledgeForge 由兩個子系統組成，彼此串連成一個閉環。生成（generation）子系統把分群後的相關工單轉成新草稿：上游流程會依問題主題把已結案工單分群，寫成 JSON 檔案丟進 Amazon S3，每個檔案對應一位客戶，內含關鍵字、文章範疇與工單描述樣本。新檔案觸發 Amazon SQS 事件，由 Amazon ECS on AWS Fargate 上的容器輪詢佇列，一次最多處理五個主題。

寫作之前，系統會先「對照現況」：針對每個主題，從該客戶專屬的 Amazon S3 Vectors 索引中取出五篇最相似的既有文章作為參考context，這種 RAG（Retrieval Augmented Generation）方式讓用詞一致，也減少生成不存在的操作步驟；若完全沒有參考文章，系統就純靠工單資料生成，並標記該文章的步驟需要人工複核。生成本身跑在 Amazon Bedrock 上的 Anthropic Claude Sonnet 4.5，針對每個主題輸出結構固定的知識庫文章與根因分析（RCA）文件兩份文件，並使用回應串流（streaming）讓容器邊收 token 邊組裝文件。

整理（curation）子系統則讓每篇文章，不論新生成或既有，都走過四個步驟：依類型分類、比對重複、評分品質、改寫弱內容。重複偵測是這裡的重頭戲：每篇文章都用 Amazon Titan Text Embeddings V2 產生 1,024 維向量，存進按客戶分開的 Amazon S3 Vectors 索引。新文章生成後同樣做 embedding，查詢索引找出最近鄰向量，餘弦距離在 0.05（相似度 0.95 以上）、Top-K 為 5 之內就視為重複。發現重複時，系統保留較新的文章、汰除較舊的，而不是預設丟棄新文章，符合支援工程師實際想要的行為。整理完成的文章送進 ServiceNow，由知識管理者審核後才正式上線。

🧩 用 Step Functions 分散式 Map 撐住批次規模

整理作業要在大量文章上跑，需要跨 worker 分攤與失敗復原機制，這由 AWS Step Functions 的兩階段分散式 map（distributed map）負責，管理狀態、套用重試與錯誤處理規則，不需要自己寫協調程式碼。每天由 Amazon EventBridge 排程觸發，一個 AWS Lambda 函式找出有新增或變動文章的客戶，把變動分批放進 Amazon SQS FIFO 佇列。

💡 每個服務選型背後都有具體理由

團隊選 Amazon S3 Vectors 而非獨立向量資料庫，是因為它把 embedding 向量直接存在 S3、metadata 隨向量保留可做逐客戶篩選，且按查詢次數與容量計費而非依運行節點計費，讓「每篇文章都存一份向量」變得負擔得起；重跑批次時也能直接讀回已存向量，省下重新計算 embedding 的 Bedrock 呼叫成本。生成作業選 Fargate，是因為單一主題的生成可能耗時數分鐘、且工作量呈突發式（忽然湧入一大批、又安靜一陣子），需要能依佇列深度自動擴縮的長時間執行容器服務。至於整理作業的 Step Functions distributed map，item processor 特意設成 STANDARD 而非 EXPRESS，因為單篇文章的 Bedrock 呼叫常超過 EXPRESS 的 5 分鐘限制，STANDARD 也保留完整執行歷史方便除錯；ItemReader 則指向 S3 上的清單檔而非直接內嵌項目，藉此讓 workflow 狀態維持精簡。

🎯 給正在建生成式 AI 文件處理管線的人

這套架構的核心啟示，是整理子系統儲存的每篇文章向量，會被生成子系統回頭當作 grounding 依據使用，讓知識庫的「品質治理」和「內容生成」形成正向循環，而不是各自為政。如果你也在處理大規模文件處理管線，這種「向量索引兼作檢索與去重雙重用途」、以及依工作負載形態分別選擇 Fargate 或 Step Functions distributed map 的做法，都是可以直接複用的模式。

🔗 來源
- 標題：KnowledgeForge: mining gold from the ITSM ticket graveyard
- 作者／機構：Anmol Dhankhar，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/knowledgeforge-mining-gold-from-the-itsm-ticket-graveyard/

#AWS #AmazonBedrock #S3Vectors #StepFunctions #RAG #ITSM #KnowledgeBase #GenAI #VectorSearch #LLM
