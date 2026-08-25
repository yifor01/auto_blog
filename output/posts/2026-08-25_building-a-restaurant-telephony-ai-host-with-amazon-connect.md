---
title: Building a restaurant telephony AI host with Amazon Connect
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-a-restaurant-telephony-ai-host-with-amazon-connect/
model: claude-code/sonnet
generated_at: '2026-08-25T06:27:04.136441'
score: 90
---

📌 【AWS 實作教學】免 App、免登入，用 Amazon Connect 打造餐廳電話點餐 AI 總機

TL;DR：AWS 釋出開源範例，串接 Amazon Connect、Lex V2、AgentCore 與 MCP，讓 AI 直接接電話幫餐廳點餐。

很多餐廳的訂單其實還是靠電話進來，接電話的往往是同一位正在櫃檯忙的員工，客人在電話那頭等待，訂單靠手寫，一忙就兩頭出錯。做一個 App 或網站能照顧到願意上線點餐的客人，卻幫不到那位就是想打電話點餐的人。AWS 這篇文章示範了如何蓋一套語音點餐系統，從問候到訂單確認全程自動化，不需要 App、網站或登入。

🤔 **電話點餐的痛點：沒有帳號，也沒有畫面**

這個方案處理的是電話這個通路本身的特殊性：語音是透過電話網路而非瀏覽器傳來，系統要靠來電號碼辨識客人，而不是靠登入。設計上把 agent 邏輯和後端服務拆成獨立模組，讓點餐邏輯不依附在特定通路上。

🧩 **三個角色各司其職：通話、對話、資料分開管**

整套架構刻意把三件事分開：Amazon Connect 負責接電話，Amazon Connect AI agent 負責跑對話，後端則保存菜單、購物車、訂單與門市位置資料。來電進入 Amazon Connect 後，contact flow 會開啟一個 AI agent session 並把客人接進去；Amazon Connect Agentic Voice 在通話全程提供語音辨識與語音合成，AI agent 負責推理，並透過 AgentCore Gateway 暴露的 MCP 工具存取後端。因為 MCP 是連接 agent 與外部工具的開放標準，後端可以獨立變動而不需要改動 agent 本身。整個部署分四段：後端基礎設施用 DynamoDB 存客人／訂單／菜單／購物車／門市資料，Amazon Location Service 處理地址與路線規劃，Lambda 跑商業邏輯，API Gateway 用 IAM 授權對外暴露；AgentCore Gateway 在部署時讀取 REST API 的 OpenAPI schema，把每個端點註冊成具名的 MCP 工具，並用自訂 JWT 授權驗證來自 Amazon Connect 執行個體的 token；Amazon Connect 執行個體與 AI agent 這段建立 Lex V2 bot（搭配 Agentic Voice 做進階語音辨識）、定義具備內容安全政策的 AI Guardrail，並以 Anthropic Claude Haiku 4.5 撰寫系統提示來定義 AI agent；最後由電話通路段建立 contact flow 並認領電話號碼。

🧩 **一通電話怎麼走完全程**

Contact flow 是每通進線電話的入口：先啟用日誌記錄，把文字轉語音設為 Agentic Voice，擷取來電號碼，接著開啟 AI agent session，用一個 Lambda 函式把客人的電話號碼帶入該 session 讓 agent 能辨識來電者，播放問候語，再把客人接進 Lex V2 bot。Lex bot 提供即時語音層，用 Agentic Voice 的進階 ASR 聆聽、TTS 說話，AI agent 則負責推理與工具呼叫。部署前需確認帳號中已可使用 Amazon Connect Agentic Voice、Anthropic Claude Haiku 4.5、Amazon Connect AI agents 與 AgentCore Gateway，文中建議從美國東部（維吉尼亞北部，us-east-1）開始。完整方案放在 GitHub 的範例儲存庫中，clone 後執行部署腳本並帶入一個 deployment prefix（讓同一個帳號可以部署多份），腳本會先跑 preflight 檢查，再依相依順序部署每個 AWS CDK stack：先建後端（DynamoDB 資料表、Location Service 資源、Lambda 函式、API Gateway REST API）並灌入範例菜單與門市資料，接著建立 Amazon Connect 執行個體與 AI Agents 助理，在後端 API 前面掛上 AgentCore Gateway，定義 Lex V2 bot、AI Guardrail 與協調用的 AI agent，最後建立 contact flow 並認領電話號碼，整個過程不需要 Docker 或 Python，腳本跑完會直接印出可撥打的電話號碼。

💡 **把通路和邏輯拆開的價值**

這個設計最值得工程師借鏡的地方，不是「串了哪些 AWS 服務」，而是把 contact flow、語音層與 agent 邏輯這些「怎麼接電話」的部分，跟 backend 這個「知道什麼」的部分徹底分離。AgentCore Gateway 讀取 OpenAPI schema 自動生成 MCP 工具這一步，讓後端可以獨立迭代，agent 端幾乎不用跟著改。

🎯 **實務啟示**

如果你的產品已經有一套後端 API，這個架構提供了一條把它接上語音通路的現成路徑：不需要重寫業務邏輯，只要把既有 REST API 包成 MCP 工具，語音辨識、合成與對話編排都交給 Amazon Connect 內建的 Agentic Voice 與 AI agent 處理即可。

🔗 **來源**
- 標題：Building a restaurant telephony AI host with Amazon Connect
- 作者／機構：Sergio Barraza（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/building-a-restaurant-telephony-ai-host-with-amazon-connect/

#AWS #AmazonConnect #VoiceAI #ConversationalAI #MCP #AgenticAI #BedrockAgentCore #SpeechRecognition #RestaurantTech #CloudArchitecture
