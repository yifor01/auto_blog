---
title: Agentic retrieval with LangChain and Amazon Bedrock Knowledge Bases
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agentic-retrieval-with-langchain-and-amazon-bedrock-knowledge-bases/
model: claude-code/sonnet
generated_at: '2026-10-05T23:22:10.084373'
score: 83
---

📌 問一個問題等於問六個,RAG 為什麼只答對一半

TL;DR：Amazon Bedrock 的 agentic retrieval 用規劃迴圈拆解多意圖問題,LangChain 已可直接呼叫。

搜尋結果沒有報錯,相關性分數看起來也正常,答案讀起來很通順——但如果你的問題其實包含六個意圖,一個向量搜尋能照顧到的,可能連一半都不到。

🤔 **一個查詢向量,扛不住六個意圖**

當使用者問一個 RAG 應用「比較兩個產品在三個維度上的差異」,其實是同時問了六個問題。但標準的相似度搜尋用單一查詢向量來代表所有意圖,檢索器產出的是這些意圖的「平均近似值」。結果是:答案簡潔,搜尋沒有出錯,相關性分數看起來合理,但實際檢索到的內容片段雖然主題相關,卻只覆蓋了問題真正問到的一小部分。

🧩 **Retrieve API vs. AgenticRetrieveStream API**

Amazon Bedrock Managed Knowledge Base 提供兩種檢索方式。Retrieve API 執行一次混合搜尋,回傳帶分數的文字片段;AgenticRetrieveStream API 則會先把問題拆成多個子查詢,逐一執行,再判斷證據是否足夠,不夠就再搜一次,整個規劃過程以 trace events 的形式串流回傳。在 langchain-aws 套件中,前者是一個可直接放進 chain 的標準 LangChain retriever（AmazonKnowledgeBasesRetriever）,後者則因為底層 API 是串流形式、不符合同步的 BaseRetriever 介面,因此改以獨立函式 agentic_retrieve 的形式提供,AmazonKnowledgeBasesRetriever 上沒有任何開關可以切換成 agentic 模式。

Amazon Bedrock Managed Knowledge Base 本身把向量儲存、embedding 與重排序模型都從 RAG 架構中移除,開發者只需要設定資料來源,其餘的 chunking、embedding、儲存與檢索都交給服務處理。建立 Knowledge Base 時使用 managedKnowledgeBaseConfiguration,並把 embeddingModelType 設為 MANAGED 以使用服務託管的 embedding 模型,此時請求中不會有 storageConfiguration——這是 API 上最明顯的訊號,代表儲存層完全由 Bedrock 掌管（自管向量儲存的 Knowledge Base 才需要帶這個欄位）。

🔑 **兩套身分,權限不能混用**

Knowledge Base 會假設一個服務角色（service role）去讀取文件並呼叫 embedding 模型,應用程式本身則用 AWS STS caller identity 去查詢,兩者權限不該互通。服務角色需要 s3:ListBucket 與 s3:GetObject,並以 aws:SourceAccount、aws:SourceArn 限縮信任政策,避免 confused deputy 問題。呼叫端身分則需要 bedrock:AgenticRetrieveStream 與 bedrock:InvokeModelWithResponseStream（這兩個動作無法限縮到特定 Knowledge Base ARN）,以及可以限縮到 ARN 的 bedrock:Retrieve 與 bedrock:GetDocumentContent。文章特別提到 bedrock:GetDocumentContent 常被忽略:當 agentic 規劃流程判斷某段文字缺乏足夠上下文、觸發 FullDocumentExpansion 步驟時就會呼叫它,只給 bedrock:Retrieve 的政策會在這一步卡住。

📊 **同一個多意圖問題,兩種檢索方式的落差**

對於意圖單一的問題,Retrieve API 是正確選擇:只需一次呼叫,延遲最低,且完整掌控答案生成方式——多數生產環境的查詢都屬於這種形狀,硬套規劃迴圈反而浪費時間與金錢。但換成「比較兩個服務在三個維度」這種包含六個意圖的問題,標準檢索取五個結果時,單一 embedding 代表六個意圖會漏掉其中兩個;取十個結果雖然涵蓋全部六個意圖,但代價是兩個子意圖被重複覆蓋,還有一個片段完全沒命中任何意圖。問題是結構性的:一個向量無法代表六個意圖,而且整個流程中沒有任何一步會去問「現有證據夠不夠回答這個問題」。

agentic retrieval 透過規劃迴圈解決了這個結構性問題,搭配 generate_response=True 參數時,服務會連同檢索到的片段一併回傳有引用來源的完整答案,不需要再額外接一次模型呼叫生成答案。

⚠️ **使用上的限制**

agentic_retrieve 函式僅適用於 Amazon Bedrock Managed Knowledge Base,且需要 boto3 1.43.32 以上版本（更早版本沒有 agentic_retrieve_stream）。從 AmazonKnowledgeBasesRetriever 取得結果時,要留意用的是 managedSearchConfiguration 而非舊版的 vectorSearchConfiguration（後者是給自管向量儲存的 Knowledge Base 用的路徑,也是多數現有範例展示的寫法）。

🎯 **實務啟示**

不是所有查詢都該套用 agentic retrieval——先判斷問題的意圖數量:單一意圖的查詢用 Retrieve API,延遲低、成本低、多數生產流量都是這種形狀；只有在問題明顯包含多個子意圖、需要規劃與二次搜尋時,才值得接受 AgenticRetrieveStream 的額外延遲與成本。權限設計上務必把 Knowledge Base 的服務角色與應用程式的呼叫身分分開,並記得補上容易被忽略的 bedrock:GetDocumentContent。

🔗 **來源**
- 標題：Agentic retrieval with LangChain and Amazon Bedrock Knowledge Bases
- 作者／機構：Manideep Reddy Gillela, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/agentic-retrieval-with-langchain-and-amazon-bedrock-knowledge-bases/

#AmazonBedrock #LangChain #RAG #AgenticRetrieval #KnowledgeBase #AWS #IAM #VectorSearch #LLMApplications #CloudAI
