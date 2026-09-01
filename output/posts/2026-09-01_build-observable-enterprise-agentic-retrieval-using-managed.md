---
title: Build observable enterprise agentic retrieval using Managed Amazon Bedrock
  Knowledge Base with AWS CloudFormation
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-observable-enterprise-agentic-retrieval-using-managed-amazon-bedrock-knowledge-base-with-aws-cloudformation/
model: claude-code/sonnet
generated_at: '2026-09-01T10:45:21.966959'
score: 106
---

📌 【AWS 實作】企業級 Agentic 檢索最怕「黑箱」，七層可觀測性怎麼補上

TL;DR：AWS 展示以 CloudFormation 一鍵部署、內建七層可觀測性的 Managed Bedrock 知識庫 Agentic 檢索架構。

單一知識庫、單次檢索的 RAG，遇到答案橫跨多個來源、或系統得先判斷該問哪個資料源的問題時就開始吃力。企業級 agentic 檢索的解法，是讓一個 agent 對問題進行推理、把問題路由到對的知識庫、反覆檢索、最後產出帶引用的答案。但問題也隨之而來：一旦 agent 開始在迴圈裡推理與檢索，你就很難再看清楚它到底做了什麼、答得好不好。

🤔 **從單次檢索到多輪規劃**

AWS 先前的文章曾用自管向量儲存的知識庫，自動化了單次 RAG 流程。這次的重點是 Amazon Bedrock Knowledge Bases 推出的 Managed Knowledge Base（`Type: MANAGED`）：Bedrock 直接管理文件的擷取、儲存、索引與檢索，預設就內建服務管理的 embedding 與 reranking 模型，不需要自己建置、擴充或維運向量資料庫。搭配新推出的 `AgenticRetrieveStream` API，檢索不再是單次查找，而是 agent 主導的多步驟流程：判斷是否要檢索、可反覆檢索以精煉答案、選擇該諮詢哪個知識庫（語意路由），最後才組合出帶引用的答案。

🧩 **架構：兩層路由 + AgentCore + 四段式 CloudFormation**

這套方案把路由拆成兩層：agent 的推理模型負責跨知識庫路由——每個知識庫對應一個檢索工具，agent 依照系統提示挑出符合問題主題的工具；`AgenticRetrieveStream` API 則負責單一知識庫內部的工作，把問題拆解成子查詢、反覆檢索、產出帶引用的答案。整體上 agent 跑的是一個 reason-and-act 迴圈：呼叫 LLM、決定該叫哪個知識庫工具、透過 Gateway 讀回結果，往往還會再檢索一次，才組成最終答案。

Amazon Bedrock AgentCore 的 Gateway 把每個知識庫的 `AgenticRetrieveStream` 暴露成一個 MCP 工具，agent 因此每個知識庫拿到一個工具，不需要額外維護 Lambda 或容器；AgentCore runtime 則負責跑 agent 本體，並自動送出 OpenTelemetry span。整套方案以四個原生 AWS CloudFormation stack 串接部署（知識庫、Gateway、agent、dashboard），輸出彼此串連。文章提到 `03-agent-runtime` 這個 stack 會用 CodeBuild 建置 agent 容器，大約需要 8 至 10 分鐘，完成後四個 stack 均達到 `CREATE_COMPLETE`。

📊 **七層遙測、兩種評估、一套可重現的部署**

方案內建兩個 CloudWatch dashboard，涵蓋七層遙測資料，外加兩種評估形式（隨選評估與持續評估），全部由同一組範本佈建。其中第 1、4、5 層是自動產生的，第 3、6、7 層則由驅動用的 notebook 以自訂指標形式發布。文章也提到示範資料採用兩個刻意區隔的小型合成語料庫，分別放進兩個獨立知識庫（而非一個知識庫掛兩個資料來源），目的是讓 agent 必須真正做出路由決策，同時讓每個知識庫的指標（索引大小、檢索品質、token 用量、評估分數，皆以 `KnowledgeBaseId` 區分）保持乾淨可分離。文中展示的擷取結果顯示：兩個知識庫各索引一份文件，且擷取失敗數為零。

💡 **為什麼觀測性要「內建」而不是事後補**

每個設計選擇都指向同一個目標：打造一套「可維運」的企業級 agentic 檢索。Managed Knowledge Base 是基礎，因為 agentic 檢索與 AgentCore Gateway 連接器只在這個型態上可用，也免除了自建向量資料庫的維運負擔；AgentCore runtime 自動送出 OpenTelemetry span，是第 5 到 7 層遙測資料能「零額外接線」出現的關鍵；CloudFormation 把整套系統（包含 dashboard 與持續評估）串成同一條可重現的部署鏈，確保每次拉起來的環境一致。

🎯 **實務啟示**

對正在把 RAG 升級成 agentic 檢索的團隊來說，這篇文章示範的重點不是「agent 會不會路由」，而是路由發生之後你看不看得到、評不評得了。把可觀測性與評估從一開始就當成架構的一部分，而非事後補上的儀表板，是把 agentic 系統真正推上生產環境前該補的一課。

🔗 **來源**
- 標題：Build observable enterprise agentic retrieval using Managed Amazon Bedrock Knowledge Base with AWS CloudFormation
- 作者／機構：Luis Felipe Yepez Barrios（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/build-observable-enterprise-agentic-retrieval-using-managed-amazon-bedrock-knowledge-base-with-aws-cloudformation/

#AWS #AmazonBedrock #AgenticRAG #KnowledgeBase #Observability #AgentCore #CloudFormation #LLMOps #RAG #EnterpriseAI
