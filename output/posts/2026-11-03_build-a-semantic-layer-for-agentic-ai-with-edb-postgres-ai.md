---
title: Build a semantic layer for agentic AI with EDB Postgres AI and Amazon Bedrock
  AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-and-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-03T22:45:31.622548'
score: 73
---

📌 把語義層直接塞進 Postgres:EDB Postgres AI 搭 Bedrock AgentCore

TL;DR:這篇示範用 EDB Postgres AI 的 AIDB 擴展,在資料庫內建語義層,讓 Bedrock AgentCore 上的 agent 能正確理解業務語意並受權限控管。

多數語義層方案都是另外架一套系統,再想辦法跟資料庫同步。這篇文章示範的做法反過來:語義層不搬出資料庫,業務定義、join 關係和存取權限,全部留在 Postgres 原生機制裡。

🤔 Agent 要正確回答業務問題,缺的不是模型而是「意義」

文章指出,一個能從即時資料回答業務問題的 agent 需要三層:負責規劃與寫查詢的模型層、告訴 agent 資料代表什麼意思的語義層,以及負責託管 agent、控管身分與存取權的執行層。這個系列此前已經用 Stardog 的知識圖譜、Denodo 的資料虛擬化平臺、AtScale 的維度模型、Strategy Mosaic 的連結模型分別示範過同一套 Customer 360(C360)案例,這篇則換成 EDB Postgres AI。模型層沿用前幾篇的 Amazon Bedrock 上的 Anthropic Claude(模型可用性依 AWS 地區而異),執行層是 Amazon Bedrock AgentCore 的 runtime,AgentCore Gateway 負責處理對內的授權驗證,AgentCore Identity 則保管對外呼叫工具所需的憑證。這篇文章的差異點在於語義層:EDB Postgres AI 把語義層做成一個叫 SemKB 的東西,直接活在營運用的 Postgres 資料庫裡,schema 定義跟業務說明一起被索引,存取控管則透過 Postgres 原生的 GRANT、row-level security 與 column-level 權限執行,而不是靠系統提示詞這種「建議性」的約束。

🧩 資料與語義怎麼建:三個表、一個視圖,加上欄位註解

示範用的資料集是 Stardog C360 Knowledge Kit,載入單一 EDB Postgres AI 實例中一個獨立的 c360 schema。資料模型包含四個表與一個衍生視圖:customers 表裡的客戶對應一個 location,會產生 purchases,每筆 purchase 又參照一個 product,這是一個單純的 Postgres join 關係圖。文章點出三個欄位名稱看不出來的業務概念:客戶所在的「州」並不在 customer 資料列上,而要透過 customers.location 這個外鍵到 locations 表才能查到,這點由該欄位上的 comment 告訴 SemKB 去哪裡找;purchases.price 記錄的是訂單總額,如果 agent 把它誤讀成單價再乘以數量,算出來的總額就會是錯的;而「big spender(高消費客戶)」是一個業務方自訂的名詞,文章的做法是把它定義成一個視圖,並用 COMMENT ON VIEW 語句附上說明,讓這個定義只存在一個地方,所有 agent、儀表板與查詢都讀取同一份定義。

請求路徑是:分析師先用 Amazon Cognito 驗證身分,帶著拿到的 JSON Web Token(JWT)以 Bearer token 的形式呼叫 AgentCore Gateway;Gateway 的 inbound JWT authorizer 會驗證這個 token,再用 Cedar policy 比對 token 中的 claims,決定這個 agent 代表這個使用者可以呼叫哪些工具,才轉送給 AgentCore runtime;runtime 呼叫 Amazon Bedrock 上的 Claude 做規劃。Agent 的工具呼叫本質上是一個 MCP 請求,AIDB 的 edb-endpoints HTTP 伺服器本身就支援 streamable HTTP MCP 加上 HTTP Basic authentication,因此 Gateway 可以直接把它當成一個 MCP server target,不需要額外的轉接層;前面架一個帶 HTTPS listener 與 ACM 證書的 Application Load Balancer,轉給 EDB Postgres AI VPC 裡 EC2 執行個體上的 edb-endpoints,AgentCore Identity 的憑證提供者會把 Postgres 角色的憑證以 Basic auth 的方式注入每一次對外請求,agent 的程式碼本身完全看不到這個 Postgres 憑證。因為 AIDB 本身就說 MCP,這整套架構不需要用到 AWS Lambda。觀測性方面,AgentCore 把追蹤資料送到 Amazon CloudWatch,AIDB 則把 SQL 執行的 OpenTelemetry 追蹤寫成 Postgres 裡 aidb_otel schema 的資料列,可以用一般 SQL 查詢。

📊 語義知識庫索引的是 schema,不是資料本身

文章強調,AIDB 的語義知識庫(SemKB)索引的對象是 Postgres 的 schema,而不是實際資料:它把每個表、視圖、欄位的定義(連同 COMMENT ON 的文字)嵌入(embed)進一個向量資料庫,讓 agent 可以用自然語言去搜尋。文章列出三項建構語義層的工作:寫 COMMENT ON 語句、把業務術語定義成帶有自己註解的視圖、以及把常見問題註冊為語義別名(semantic alias)。其中寫 comment 是最簡單的一項,卻對 text-to-SQL 準確率的提升最大,無論是給人用還是給 agent 用。建立 c360_kb 這個 SemKB 時要註冊名稱、embedding 模型、目標 schema 與自動處理模式;文中使用的 embedding 模型是隨 AIDB Amazon Machine Image 附帶的本地 llama.cpp 模型(llamacpp_embeddings),由於一個 SemKB 只能用一個 embedding 模型,所有條目才會落在同一個向量空間裡;若要換成遠端的 embedding 模型,如 Amazon Bedrock 上的 Amazon Titan Text Embeddings,則需要先用 aidb.create_model 註冊這個遠端模型,再把名稱填進 SemKB 的 model 參數。auto_processing 參數可選 Disabled、Live 或 Background,Live 模式會透過 Postgres 的事件觸發器(event trigger)對 schema 變更做出反應。

🎯 實務啟示

如果團隊已經把業務資料放在 Postgres,而不想為了接上 agent 另外建一套語義層系統、再處理跟來源資料庫的同步問題,這篇展示的模式值得參考:用 COMMENT ON 語句把業務定義寫在 schema 旁邊、用視圖固化業務術語的定義、靠資料庫原生的 GRANT 與 row-level security 做權限控管,再透過 AIDB 內建的 MCP 端點直接讓 AgentCore 之類的 agent runtime 接上,省掉額外的轉接層與目錄同步工作。需要留意的是,這是該系列第五篇用同一套 C360 範例比較不同語義層廠商方案的介紹性教學,實際評估時仍需搭配自身的資料規模與查詢模式做驗證。

🔗 來源
- 標題:Build a semantic layer for agentic AI with EDB Postgres AI and Amazon Bedrock AgentCore
- 作者／機構:Rajesh Nagpal
- 連結:https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-with-edb-postgres-ai-and-amazon-bedrock-agentcore/

#SemanticLayer #Postgres #AgenticAI #AmazonBedrock #AgentCore #MCP #TextToSQL #RAG #AWS #DataGovernance
