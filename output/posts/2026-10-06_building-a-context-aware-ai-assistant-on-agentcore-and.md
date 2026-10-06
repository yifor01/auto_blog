---
title: Building a context-aware AI assistant on AgentCore and OpenClaw
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-a-context-aware-ai-assistant-on-agentcore-and-openclaw/
model: claude-code/sonnet
generated_at: '2026-10-06T22:03:44.810795'
score: 79
---

📌 用 AgentCore 和 OpenClaw,打造記得住你的 AI 助理

TL;DR:AWS 展示如何用 Amazon Bedrock AgentCore 搭配開源 OpenClaw,做出會累積長期記憶的個人助理。

你三週前跟助理提過,你的花床排水太快,只用有機肥料,矮牽牛在熱浪中快撐不住了。今天你問「該怎麼照顧我的花」,它卻完全不記得這些事,要你從頭解釋一次。問題不在回答品質,而在助理沒有「你」的記憶。AWS 這篇文章用一個取名 Sprout 的園藝助理,示範如何解決這個問題。

🤔 無狀態助理的根本限制

多數現成 AI 助理擅長回答單一問題,但每次對話都是從零開始,把「重新解釋情境」的負擔丟給使用者。AWS 提出的做法是讓 OpenClaw(一套開源 agentic 系統)跑在 Amazon Bedrock AgentCore runtime 上,再透過 AgentCore memory 把「用過即丟的對話」變成「可持續查詢的知識」,並用結構化 metadata 標記記憶,讓助理只抓取跟當下問題相關的記錄。文中強調這個架構是領域無關的,換掉人格設定與技能清單,同一套 pipeline 就能變成客服機器人、健身教練或內部服務臺。

🧩 兩個入口,匯聚到同一個 agent

架構上,Telegram webhook 與 Amazon EventBridge Scheduler(例如晨間澆水提醒)是兩個獨立入口,分別透過 API Gateway + Lambda 和 cronjob Lambda,呼叫同一個 AgentCore runtime 的 InvokeAgentRuntime API。runtime 裡有一個精簡的 server.py 行程,負責協調 OpenClaw gateway、AgentCore memory,以及 Amazon Bedrock Converse API。其餘元件分工明確:Amazon S3 提供工作區儲存、AWS KMS 負責加密、AWS Secrets Manager 存放 bot token、Amazon CloudWatch 收集日誌與指標。整套系統只用一份 CloudFormation 範本,一行指令就能部署。

🧩 容器契約與文字/圖片雙路由

AgentCore runtime 的容器契約很單純:監聽 port 8080,提供 GET /ping 做健康檢查、POST /invocations 作為 agent 進入點。範例容器是 linux/arm64,以官方 OpenClaw 映像檔為基礎,再疊一層 Python 多階段建置。文字對話會走 OpenClaw gateway,帶著技能與 session 狀態;但圖片理解刻意繞過 gateway,改由 server.py 直接呼叫 Bedrock 的 LLM,把影像位元組作為多模態內容傳入——原因是容器內的 OpenClaw 版本會在送到 Bedrock 前把 image_url 內容區塊丟掉。兩條路徑共用同一份 system prompt(人格設定加記憶),維持體驗一致。模型 ID 透過 MODEL_ID、VISION_MODEL_ID 環境變數設定,換模型不用重新建置映像檔。

🧩 技能是設定檔,不是程式碼

能力以 community-skills.json 清單宣告,部署時的腳本會把技能寫進容器,並在建置映像檔前註冊到 OpenClaw 設定。Sprout 目前出廠內建天氣、提醒、植物筆記三種技能。換一份清單,同一套 pipeline 就能服務完全不同的領域,這也是作者強調這是「可重用模式」而不只是一個聊天機器人的原因。

🧩 為什麼選 Telegram

Telegram 是 webhook 式架構,整條鏈路都能維持無伺服器(serverless),不需要開發用戶端,使用者裝置上大多已經裝好,且原生支援文字、圖片與格式化文字。BotFather 發出的 bot token 存進 Secrets Manager,部署時把 webhook 註冊到 API Gateway 端點。文章也提到一個實務教訓:Telegram 舊版 markdown 對未轉義字元非常不寬容,模型回覆裡一個多出來的底線就可能讓整則訊息送不出去,所以助理會先把模型輸出轉成 Telegram 安全的 HTML 再發送。

💡 真正的差異化在 AgentCore memory

AgentCore memory 分兩層。短期記憶透過 CreateEvent 把每一回合對話存成事件,用 actorId(Telegram chat ID)與 sessionId 當 key,這是原始逐字稿。長期記憶則由管理式提取策略(managed extraction strategies)非同步運作,產生結構化、可長久保存的記錄,文中提到設定了三種策略。Sprout 把記錄分別寫入每個使用者各自的命名空間(namespace),因此不同聊天絕不會混在一起;chat ID 是唯一變動的區段,讓隔離性很容易驗證。每一回合,agent 都會檢索相關長期記錄、排序後注入 system prompt,而組裝步驟會讓「明確說過的偏好」排在「推論出來的事實」之前,同一類別內順序穩定,並在注入前做數量上限控制。命名空間回答「這是誰的記憶」,metadata 則回答「這段記憶在講什麼」。

📊 成本:消費制計價 vs. 常駐執行

AgentCore runtime 採消費制計價,只為 agent 實際耗用的運算付費,等待模型回應等 I/O 時間不計費。文中估算,個人輕量使用下,每月成本約 1-2 美元,相較之下一臺常駐執行的 Amazon EC2 執行個體約需 35 美元/月(以 2026 年 7 月的估算為準,實際費率請查 AgentCore pricing)。

🎯 實務啟示

這套架構的價值不是「發明了新東西」,而是把一個開源 agent 框架用一層薄薄的 server.py 包裝,套進 AgentCore 的容器契約,再用 AgentCore memory 補上「跨對話記憶」這塊長期缺口。如果你手上已經有一個能跑在本機行程的 agent 框架,這個 wrapper 模式幾乎可以直接複用,不需要改框架本身;真正值得抄的細節反而是記憶的分層設計與 metadata 排序邏輯,這對任何想做「有記憶的助理」的團隊都是現成的參考架構。

🔗 來源
- 標題:Building a context-aware AI assistant on AgentCore and OpenClaw
- 作者/機構:Thiago Verney(AWS ML Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/building-a-context-aware-ai-assistant-on-agentcore-and-openclaw/

#AWS #AmazonBedrock #AgentCore #OpenClaw #AIAgent #LLM #Telegram #AgenticAI #CloudArchitecture #MemoryAI
