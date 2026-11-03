---
title: 'NVIDIA Releases Auto Ontology: An Open Semantic Layer That Grounds AI Agent
  SQL'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/01/nvidia-auto-ontology-open-source-semantic-layer-ai-agents/
model: claude-code/sonnet
generated_at: '2026-11-03T00:01:04.902468'
score: 92
---

📌 NVIDIA 開源 Auto Ontology:讓 AI Agent 寫出可信 SQL 的語義層

TL;DR:NVIDIA 開源語義層框架,讓 agent 透過經認證的業務定義生成 SQL,而非憑空猜測資料表結構。

一個反應飛快的營收數字,如果算錯了就毫無價值。NVIDIA 在 Auto Ontology 的 repository 裡用這句話點出問題核心:AI agent 能快速查資料倉儲,不代表查出來的東西是對的。

🤔 **Agent 和資料倉儲之間缺了一層**

Auto Ontology 是一個介於 agent 與資料倉儲之間的 context layer,它告訴 agent 資料存在哪裡、欄位代表什麼意思,還有該不該用這個欄位、怎麼用、資料來源是什麼。NVIDIA 開發者頁面把輸出定位為一個「起始 ontology」,業務專家仍需要測試、修正並正式認證,而不是生成出來就直接拿去上線。

🧩 **四個服務組成的架構**

整套系統由 4 個核心服務構成:Next.js 16 打造的前端處理網頁介面與身分驗證（port 3000);FastAPI 搭配 LangChain 的後端負責聊天、NL-to-SQL 與目錄（catalog)API（port 3001);ingestion worker 負責寫入 embeddings（port 3002);Postgres 搭配 pgvector 則儲存 catalog、ontology 與向量資料。來源資料庫可以是 Databricks、Postgres、Snowflake 或 DuckDB,模型則透過環境變數中的「endpoint、key、model」三元組設定,並分成 reasoning、non-reasoning、embedding、reranking 四種角色,理論上任何 OpenAI 相容的 endpoint 都能接上。

MCP server 文件描述了 9 個唯讀工具,其中 ask_question 會把答案、對應 SQL 與資料列分開回傳,結果上限為 100 列;check_readiness 用來確認已編譯完成的語義層與資料庫連線都存在。值得注意的是,這裡沒有讓 agent 瀏覽原始 schema 的工具,NVIDIA 刻意這樣設計,目的是讓 agent 只能透過語義層接觸資料。底層 OpenAPI 規格公開了 87 個操作,登入走 OAuth,每次呼叫都帶著登入使用者的權限。

📊 **用確定性比對做評測,不靠 LLM 評審**

NVIDIA 另外提供一套評測工具 auto-ontology-eval,在 NeMo Gym 中跑兩個對照組:僅靠 schema 的 LLM control,以及有 ontology 支撐的 agent,評分方式是確定性的執行結果比對（deterministic execution match),不使用 LLM 當評審。內建資料集包括 BIRD Dev（1,534 題,涵蓋 11 個資料庫)與 Mini-Dev（500 題),另外加上 FDABench-Lite（169 題)以及預設抽樣 100 題的 BEAVER。

⚠️ **評測本身有兩個限制**

harness 的 repository 自己列出兩點:few-shot 範例與 value anchors 只給了 ontology 這一組,所以搭配這些輸入測出的分數差異,反映的是這些輸入帶來的效果,而不是單純語義層 grounding 本身的效果;另外,測試用的設定讓兩組都是透過 NVIDIA 的 inference gateway 走 Claude 模型,這點在解讀評測結果時需要留意。

🎯 **實務啟示**

本機部署只需要填好 .env 後執行 docker compose up -d --build,Kubernetes 使用者則有 Helm chart 與 DEPLOYMENT.md 指南可以參考,NVIDIA 也把後端打包成 NGC container 釋出;要跑預設模型需要從 build.nvidia.com 取得 API key。對已經在做 NL-to-SQL agent、卻常被數字算錯困擾的團隊,Auto Ontology 提供的是一個可以直接插入既有資料倉儲的語義層骨架,而不是要工程師從零打造 ontology,整體概念雖非全新,但工程落地的完整度值得參考。

🔗 **來源**
- 標題:NVIDIA Releases Auto Ontology: An Open Semantic Layer That Grounds AI Agent SQL
- 作者／機構:Asif Razzaq,MarkTechPost
- 連結:https://www.marktechpost.com/2026/11/01/nvidia-auto-ontology-open-source-semantic-layer-ai-agents/

#AutoOntology #NVIDIA #SemanticLayer #NLtoSQL #AIAgents #DataWarehouse #OpenSource #MCP #TextToSQL #EnterpriseAI
