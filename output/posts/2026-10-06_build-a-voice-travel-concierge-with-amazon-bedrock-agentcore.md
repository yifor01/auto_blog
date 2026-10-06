---
title: Build a voice travel concierge with Amazon Bedrock AgentCore, Managed Knowledge
  Base and Nova Sonic
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-voice-travel-concierge-with-amazon-bedrock-agentcore-managed-knowledge-base-and-nova-sonic/
model: claude-code/sonnet
generated_at: '2026-10-06T22:03:44.811113'
score: 74
---

📌 幫航空公司 App 裝上語音:AgentCore + Nova Sonic 打造旅遊語音管家

TL;DR:AWS 示範用 AgentCore、Managed Knowledge Base 與 Nova Sonic,三個全託管服務拼出可改座位、查行李政策的語音旅遊助理。

想像你正在趕飛機,不想在手機上一層一層點選選單改座位,只想開口說「幫我換到靠走道的位子」,系統就懂了,還會先跟你確認一次才送出變更。

🤔 語音層聽起來簡單,工程上卻處處是坑

航空公司通常已經有 App 讓旅客查詢航班、選座位、管理訂票,加上語音層可以把這些操作變成開口就能做的事。但要做到這件事,得同時處理雙向串流音訊、在多輪對話間維持上下文、串接既有後端系統又不能跟它緊密耦合,還要在旅遊旺季流量暴增時撐得住。AWS 這篇文章用三個託管服務拼出一套解法:Amazon Bedrock AgentCore(建置、部署、安全維運 AI agent 的平臺)、Amazon Nova Sonic(即時語音的 speech-to-speech 模型)、Amazon Bedrock Knowledge Bases(全託管的 RAG 服務,把回答錨定在自己的文件上)。

🧩 旅客能開口做到的事

旅客開口後,管家可以叫出行程、改座位、更新餐點偏好、回答政策問題,也能在旅客要求時轉接真人客服。這套語音管家是跟既有畫面並存,不是取而代之,旅客可以在同一個 session 裡在「點選」和「說話」之間自由切換。範例串接的是帶合成資料的航空公司後端,方便套用到自家系統時直接參考這個模式。

🧩 四層架構:後端、Gateway、Runtime、前端

整個方案拆成四個區塊。區塊 A 是後端基礎設施,五個 CDK stack 部署 DynamoDB 資料表、Lambda 函式、API Gateway 端點、Amazon Bedrock Knowledge Bases 與 Amazon Cognito。區塊 B 是 AgentCore Gateway,一個 CDK stack 建立支援 MCP(Model Context Protocol,一套讓 AI 應用程式串接外部工具與資料的開放標準)的 Gateway,把每個後端端點都包裝成一個 agent 可以直接呼叫的具名工具。區塊 C 是 AgentCore runtime,兩個 CDK stack 負責建置環境:Amazon ECR 存容器映像檔、Amazon S3 存原始碼上傳、AWS CodeBuild 產出 ARM64 的 Docker 映像檔;runtime 用 Strands Agents 框架搭配 Amazon Nova 2.5 Sonic,並支援 WebSocket。區塊 D 是前端,一個 CDK stack 把 React 應用程式部署到 AWS Amplify。整套方案用單一 CDK 腳本部署。

🧩 用 RAG 回答政策問題,靠 MCP 接上後端工具

旅客問行李限重、改票手續費、寵物同行或會員條款,這些問題由 Amazon Bedrock Knowledge Bases 做的 RAG 來回答,答案錨定在航空公司自己的政策文件上。範例倉庫附帶行李、取消退款、改票、票價艙等規則、會員條款、寵物同行、特殊協助、升等這幾類政策文件;文件上傳到 Amazon S3 並建立一次知識庫後,後續的 embedding、chunking、索引、儲存與檢索都由 Bedrock 自動處理。儲存層用的是 Amazon S3 Vectors,Smart Parsing 負責先處理來源 PDF,讓表格與結構化版面也能被正確檢索。知識庫接上 agent 的方式也很直接:在 AgentCore Gateway 把知識庫加成 Connectors target,選擇標準或 agentic 檢索,Gateway 就會把它曝露成一個具名的 MCP 工具,跟後端 API 工具並列,agent 執行時直接依名稱呼叫,不用寫任何自訂的 Lambda 或檢索程式碼。要換自己的政策文件,只要把 PDF 或文字檔放進政策文件資料夾重新部署知識庫 stack 即可,政策更新後同步知識庫,新內容馬上可用,不需要重跑整條部署流程。

🧩 資料與身分:DynamoDB、Cognito、SigV4

Amazon DynamoDB 存放示範用的航空公司資料模型,涵蓋客戶資料、訂票、乘客、座位圖、購買紀錄、偏好設定、對話逐字稿與航班狀態,具備個位數毫秒延遲與隨需擴充能力。身分驗證用 Amazon Cognito User Pools 與 Identity Pools 做角色制存取控制:旅客用帳密登入後拿到 JWT(access token 與 ID token),前端再用 ID token 向 Cognito Identity Pool 換取臨時 AWS 憑證(access key、secret key、session token),這組憑證再用 SigV4 替 WebSocket 連線與 API Gateway 請求簽章。

💡 語音管線的實際流程

前端把音訊以 16kHz PCM 透過 WebSocket 串流進 AgentCore runtime;Amazon Nova 2.5 Sonic 轉錄語音,agent 選擇合適的工具,透過 MCP 呼叫;AgentCore Gateway 把每個 MCP 呼叫轉譯成 REST 請求,Lambda 執行商業邏輯回傳結果,Amazon Nova 2.5 Sonic 再把結果揉進語音回覆裡說出來。Agent 本身用 Strands BidiAgents 框架定義 system prompt、工具與對話流程。文中列出 Nova 2.5 Sonic 在這個場景下的三個實際效益:能可靠地串接並完成多步驟請求的工具呼叫(例如先查行程再改座位)、嚴格遵循 system prompt 裡的格式規則(例如把確認碼跟航班號一個字元一個字元唸出來)、以及能正確處理不當請求的 responsible-AI 行為。

⚠️ 隔離與防護設計

每個 session 都跑在 AgentCore runtime 上有 microVM 隔離的受管容器裡,讓高流量下不同旅客的對話彼此分離;AgentCore 提供自動擴充、內建監控與 session 路由。正式環境建議加上 Amazon Bedrock Guardrails,過濾 prompt injection 並驗證回覆是否真的有依據。方案本身採用「寫入前先確認」的模式,要求旅客在系統真正送出變更前先確認,搭配知識庫回答附帶的來源引用,已經構成一個基本的 responsible AI 實務底線。

🎯 實務啟示

這套方案的價值不在發明新模型能力,而是示範如何把語音、RAG、既有後端這三件事用 MCP 鬆耦合地接起來,同時把 session 隔離、身分驗證與 guardrails 這些維運細節一次處理好。如果你的團隊想幫既有的 Web/App 產品加一層語音互動,這份架構拆解,尤其是 AgentCore Gateway 把後端 API 跟知識庫統一曝露成具名 MCP 工具的做法,值得直接拿來對照自己的系統設計。

🔗 來源
- 標題:Build a voice travel concierge with Amazon Bedrock AgentCore, Managed Knowledge Base and Nova Sonic
- 作者/機構:Ravi Kumar(AWS ML Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/build-a-voice-travel-concierge-with-amazon-bedrock-agentcore-managed-knowledge-base-and-nova-sonic/

#AmazonBedrock #AgentCore #NovaSonic #VoiceAI #RAG #MCP #AIAgent #AWS #ConversationalAI #KnowledgeBase
