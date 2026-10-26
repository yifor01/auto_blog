---
title: Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk/
model: claude-code/sonnet
generated_at: '2026-10-26T21:49:49.662650'
score: 85
---

📌 用CDK打造企業級Agentic Retrieval架構

TL;DR：AWS 示範如何用 CDK 在 Managed Bedrock Knowledge Base 上建出具備多輪推理、語意路由與可觀測性的 agentic retrieval 系統。

傳統 RAG 的套路很簡單：把問題做 embedding，從一個索引抓最相近的片段，餵給模型，產出答案。一次檢索、一次生成。問題是，一旦答案需要跨兩個語料庫、或者該用哪個知識庫取決於問題本身、或者需要先看一次結果再回頭檢索一次，這套簡單流程就沒有機制處理，只會流暢地給出一個不完整的答案。

🤔 **單次檢索失效的三種場景**

文章點出單一索引、單次檢索會卡住的三種情況：答案跨越兩個語料庫時，一次檢索只拿到一半資訊；最適合的來源取決於問題內容時，單一索引沒有選擇機制；需要看過第一次結果後再檢索一次時，流程裡沒有這個「再看一次」的空間。企業級 agentic retrieval 的解法，是把一個推理 agent 放進迴圈裡，由它決定是否檢索、該查哪個知識庫，以及要不要在組成答案前再查一次。

🧩 **架構：Managed Knowledge Base + Gateway + Agent**

這正是 Amazon Bedrock Knowledge Bases 近期的演進方向。隨著 Managed Knowledge Base 推出，檢索不再是單次 embed-and-fetch 呼叫，而成為一項 agentic 能力：多輪規劃、工具驅動的檢索、以及有引用來源的答案，透過 `AgenticRetrieveStream` API 以服務原生功能的形式提供，而不必自己拼裝一套 orchestration 層。

Managed Knowledge Base（Type: MANAGED）由 Amazon Bedrock 代管資料擷取、儲存、索引與檢索，預設包含服務代管的 embedding 與 reranking 模型，不需要自行佈建、擴充或修補向量資料庫；這與 Customer-managed（DIY）Knowledge Base 需要自己選擇並維運向量儲存（例如 Amazon OpenSearch Serverless）不同。由於 agentic retrieval 與 AgentCore Gateway 連接器只在 managed knowledge base 上提供，這也是該架構選用 Managed 版本的主要原因。

系統中一個問題的完整路徑是：使用者的問題進入跑在 AgentCore Runtime 上的 agent，透過 AgentCore Gateway 路由到兩個 `AgenticRetrieveStream` 工具之一（分別對應財務與天氣兩個知識庫，皆由 Amazon S3 擷取），Gateway 把每個知識庫都暴露成 agent 可呼叫的工具，Managed Knowledge Base 負責搜尋並附上引用來源，而這個迴圈會依問題需要重複執行。沿途所有行為都會送進 Amazon CloudWatch。

🧩 **為什麼是 CDK：四個緊密交叉引用的 Stack**

文章特別說明選用 CDK 的理由：這套架構的四個 stack 之間高度交叉引用——Gateway 需要兩個知識庫的 ID，agent 需要 Gateway 的 URL 與 ARN，而儀表板需要知識庫 ID、Gateway ARN 與 agent runtime ID，共七個數值跨越 stack 邊界，每一個都是某個指標的維度或某個連接器的目標。若用原始範本手刻，就得自己維護一組 stack exports 與跨 stack 查詢，外加一支確保部署順序正確、依序傳遞輸出的腳本，而且只要有東西被重新命名，這些手刻的對應關係就會跟著失準。在 CDK 裡，直接把 construct 傳進去，export 與依賴關係就會自動從這個動作推導出來，一個指令即可部署全部，部署順序則由 CDK 自行推算。作為對照，2024 年的版本只有三個 stack、依賴關係幾乎是線性的，到了四個 stack、七個跨界數值時，這個差異就不再只是風格問題。

📊 **可觀測性是內建設計，不是事後補強**

這套方案提供兩個涵蓋七層遙測資料的 CloudWatch 儀表板，加上兩種形式的評估（on-demand 與 continuous），全部由同一個 CDK 應用程式佈建。文章強調，一個會推理、會迴圈檢索的 agent，每個問題走的路徑都不一樣，預設情況下你看不到它走了哪條路、也看不到答案品質好壞，可觀測性因此從「附加功能」變成「唯一能確認系統正常運作」的方式。引用來源可以追溯回原始段落，讓回應保持可被稽核，而忠實度與正確性分數則能讓你在生產環境之外就先發現答案逐漸偏離來源。

🎯 **實務啟示**

如果你的 RAG 系統已經開始出現「答案來自錯誤語料庫」或「答案看起來流暢但其實缺資訊」的狀況，這篇文章點出的三種失效場景值得拿來對照自己的使用案例；而其強調的「可觀測性與評估要跟架構一起設計，而不是事後補」，對任何打算把推理迴圈放進檢索系統的團隊,都是值得先想清楚的部分。

🔗 **來源**
- 標題：Build agentic retrieval on a Managed Amazon Bedrock Knowledge Base with CDK
- 作者／機構：Prabhakar Chandrasekaran（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/build-agentic-retrieval-on-a-managed-amazon-bedrock-knowledge-base-with-cdk/

#AmazonBedrock #AgenticRetrieval #RAG #AWSCDK #KnowledgeBase #AIAgent #CloudWatch #Observability #LLMOps #AWS
