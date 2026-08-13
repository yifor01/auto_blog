---
title: How OneAdvanced deployed over 50 AI agents on UK-sovereign AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/
model: claude-code/sonnet
generated_at: '2026-08-13T07:33:08.085605'
score: 94
---

📌 三週上線超過 50 個 AI Agent，OneAdvanced 的 UK 主權 AI 之路

TL;DR：英國企業軟體商自架 Llama 4 Maverick 與 Guard 4，三週內用 Strands SDK 上線 50 多個 agent。

當你要用的模型還沒在所在區域上架成受管服務時，該怎麼辦？OneAdvanced 的答案是：自己架。

🤔 背景：資料主權是硬性需求

OneAdvanced 是英國企業軟體供應商，服務超過 10,000 個客戶，涵蓋醫療、法律等高度監管產業，這些客戶每天處理病歷、法律案件檔案、合規文件等敏感資料，對 AI 工具的資料落地、安全與隱私標準要求嚴格。OneAdvanced CTO Andrew Henderson 在 OneAdvanced AI launch video 中提到，資料主權，特別是在英國，是許多客戶的硬性需求，尤其是公部門與高度監管產業的客戶，他們需要確切知道資料存放位置、誰能存取，以及資料是否留在英國的法律與監管框架內，以支持完整合規與信任。

OneAdvanced 最初用 Amazon Bedrock 做原型，在兩週衝刺內就完成聊天完成、查詢英國成文法的 Amazon Bedrock Agent、Snowflake 資料整合與圖表產生等功能。但為了滿足主權要求，他們需要把模型完全架在自己的英國 AWS 帳戶內。當時他們想用的 Llama 4 Maverick 與 Llama Guard 4，在英國區域還沒有受管服務可用，於是 OneAdvanced 選擇自行部署、服務並擴展這些模型。

🧩 架構：vLLM 服模型、Strands SDK 跑 Agent、pgvector 做檢索

解決方案由四個部分組成：vLLM 在 Amazon SageMaker AI 上、於倫敦（eu-west-2）區域的 p5.48xlarge 執行個體上服務 Llama 4 Maverick（FP8）與 Llama Guard 4；超過 50 個 Strands agent 跑在 Amazon ECS 上，每個都有自己的 system prompt、工具設定與選用的輸入表單，agent 設定存在 Amazon DynamoDB；上傳到 Amazon S3 的文件會被轉成 markdown、切塊並嵌入 pgvector 供檢索；Llama Guard 4 會在請求送進主模型前先檢查是否含有害內容。

典型請求流程是：使用者送出訊息，Llama Guard 先檢查有害內容（在主推理模型之前評估），請求接著被路由到對應的 Strands agent，agent 視需要呼叫工具、從 pgvector 與 S3 擷取相關文件，或呼叫網頁搜尋等專用工具。

模型 serving 的細節上，他們使用 meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 與 meta-llama/Llama-Guard-4-12B，透過 Hugging Face 模型與 AWS Deep Learning Containers，在 p5.48xlarge 上部署。更長的 context window 是轉向 P5 機型的主因，OneAdvanced 目標支援 120K–128K token 的 context length，以應付大型文件分析與多輪對話等情境；在與 AWS 的顧問合作期間，於 P5 上用 vLLM 做的負載測試驗證了基礎架構能滿足吞吐量需求。他們最初用 p4d.24xlarge，正式環境才轉為 p5.48xlarge，同時也利用了 GPU 運算的預留執行個體折扣。Llama Guard 4 取代了先前部署的 Llama Guard 3，原因是 OneAdvanced 觀察到 Llama Guard 3 有較高的 false rejection rate；Guard 模型在主模型之前序列執行，負責在推理開始前篩查使用者輸入內容。

🧩 50 多個 Agent 怎麼在三週內長出來

OneAdvanced 的 agent library 涵蓋醫療、法律、人資、行銷、物流等領域，超過 50 個任務專屬 agent，包括 Care Incident Response 助理、Clinical Safety Bulletin 產生器、教育用的 scheme of work 產生器、operational scenario 模擬、績效考核助理、文件比對工具，以及 AWS Architect Agent 等。從第一個 agent 到超過 50 個只花了三週，多數 agent 在一天內就完成建置。

評估過 LangChain、LangGraph 等多個 agentic 框架後，他們選擇了 Strands Agents SDK，原因是 Strands 採 model-first 做法、不強制固定的 workflow 定義，支援輪流對話與 interview 式互動，能讓團隊快速從構想推進到部署完成的 agent。OneAdvanced 首席軟體工程師 Nick Heap 表示：評估後 Strands 是這個專案的明確首選，其完整的工具套件不僅滿足了需求，也提供了與內部願景高度契合的前瞻性解法。

每個 agent 由 system prompt、一組工具與選用的結構化輸入表單定義，容器化後部署在 Amazon ECS 上，執行期設定存於 Amazon DynamoDB，使用者瀏覽 agent 目錄、挑選符合任務的 agent。OneAdvanced 還打造了一個無需寫程式的 agent builder，讓非工程背景的使用者透過視覺化介面建立與設定 agent：定義 agent 的 persona、用拖放欄位設計輸入表單、撰寫 system prompt 並用 @ 語法引用表單欄位的值、從工具庫中挑選要用的工具，讓產品經理、臨床人員、業務分析師都能在不寫程式的情況下建立 agent。

共用工具庫包含計算機、圖表產生、檔案內容讀取、Mermaid 圖表產生器、組織與個人知識庫搜尋、試算表查詢（含 Snowflake 整合）、文字檔查詢、英國成文法搜尋，以及依組織與使用者逐次選擇加入的網頁搜尋。例如一個 agent 可以在單次互動中查詢 Snowflake 資料庫，再從結果產生圖表。OneAdvanced 也用 sub-agent 與進階 agentic pattern 在複雜互動中維持 context window，其中一個值得注意的設計是 interview 式 agent。

🎯 實務啟示

這個案例顯示，在受管服務尚未涵蓋所需模型或區域的情況下，自架開放權重模型（搭配 vLLM、SageMaker AI）是滿足主權合規要求的可行路徑，不必等待雲端供應商補齊服務清單。用可設定 system prompt、工具與輸入表單的輕量 agent 框架（如 Strands），搭配 no-code 建置介面，能讓 agent 的產出速度不被工程資源綁死，交由更貼近業務的角色自行組裝。

🔗 來源
- 標題：How OneAdvanced deployed over 50 AI agents on UK-sovereign AWS
- 作者／機構：Astrid Bowser, Alex Savage, Nick Heap；AWS ML Blog（與 OneAdvanced 團隊共同撰寫）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-oneadvanced-deployed-over-50-ai-agents-on-uk-sovereign-aws/

#AIAgents #DataSovereignty #AWS #Llama4 #StrandsAgents #SageMakerAI #RAG #EnterpriseAI #UKTech #LLMOps
