---
title: Asynchronous patterns for calling Amazon Bedrock AgentCore agents in serverless
  pipelines
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/asynchronous-patterns-for-calling-amazon-bedrock-agentcore-agents-in-serverless-pipelines/
model: claude-code/sonnet
generated_at: '2026-08-20T06:37:27.979038'
score: 84
---

📌 呼叫 AI Agent 別用阻塞式呼叫，AWS 教你三種省錢模式

TL;DR：Bedrock AgentCore agent 處理慢，同步等待會讓 Lambda 白白計費，三種非同步模式讓你只付真正用到的運算時間。

想像你的 Lambda function 呼叫一個 AI agent，請它判斷一份不動產融資文件是否完整一致，agent 要「想」上好一陣子才回答，而在這段等待期間，你的 Lambda 什麼事都沒做，卻仍被完整計費。AWS 這篇文章點出的，正是這個容易被忽略的成本陷阱。

🤔 阻塞式呼叫，浪費的錢花在哪裡

AI agent 有個傳統 pipeline 步驟沒有的特性：它需要思考時間，長短取決於 prompt、模型與文件內容，很少是即時的。Amazon Bedrock AgentCore runtime 本身採消費型計費，agent 等待 LLM 生成回應、或等 tool／MCP 呼叫回傳時，只計記憶體費用，不計 CPU 費用。但呼叫端就不是這麼回事：一個用同步方式呼叫 agent 的 Lambda function、容器或 EC2 執行個體，會整段時間卡在那裡，並支付它完整的運算配額，直到 agent 回應為止。換句話說，浪費並非發生在 agent 那一端，而是呼叫端閒置在一條開著的連線上——它的計費時間幾乎等於 agent 的處理時間。

🧩 四種呼叫模式，同一顆 agent 不用重新部署

文章用一個「文件驗證」pipeline 做示範，整條流程不變，只替換其中的 Validate 分支。巧妙之處在於同一顆 agent 服務所有情境：它會檢查收到的呼叫裡有沒有 Step Functions 的 task token、有沒有 durable function 的 callback ID，藉此決定要喚醒哪個流程，或是直接把結果放進回應裡。這代表你能自由切換呼叫模式，完全不用改動或重新部署 agent 本身。

四種模式分別是：
- 阻塞式反樣式（基線）：Lambda 呼叫 agent 並原地等待，函式存活時間約等於 agent 處理時間，全額計費，是最直覺也最常見的第一版實作。
- Task-token callback：Step Functions 用 waitForTaskToken 把 task token 傳給 Lambda，Lambda 用這個 token 啟動 agent 後幾秒內就回傳，執行流程本身暫停等待、不計費，直到 agent 呼叫 SendTaskSuccess 才喚醒；並搭配 timeout 與 heartbeat 作保險，避免 agent 沒回應時流程無限期卡住。
- 直接服務整合（InvokeHarness）：Step Functions 透過 AWS SDK 整合直接呼叫 AgentCore，Validate 分支縮成單一 Task state，完全不需要 Lambda，Standard workflow 按狀態轉換計費，而非等待時長。
- Durable function：用 @aws/durable-execution-sdk-js，pipeline 各階段變成 context.step、平行工作變成 context.parallel，等待 agent 則用 context.waitForCallback，等待期間函式掛起不計費，agent 完成後呼叫 SendDurableExecutionCallbackSuccess 恢復執行。

📊 從 event history 看見等待去了哪裡

文章沒有給出具體金額，而是強調兩個數字之間的關係：Validate 狀態實際活躍的時間，對比 dispatcher 函式真正被計費的時間。在 Step Functions 的 event history 中可以直接觀察到這個現象：採用 task-token 模式時，TaskSubmitted（函式已返回）與 TaskSucceeded（agent 完成並喚醒流程）之間相隔的正是 agent 的處理時間，而這段時間 dispatcher 函式早已結束，不再計費。

💡 三種模式的共同邏輯：把等待丟給不計費的協調層

三種非同步模式雖然實作方式不同，本質上做的是同一件事：把「等待」的責任從按秒計費的運算資源，轉移到不計費（或計費方式不同）的協調層——Step Functions 的暫停執行，或 durable function 的掛起狀態。差別只在於是否需要在 agent 呼叫前後保留自訂邏輯：task-token 模式仍保留一個 Lambda，但只負責短暫的 dispatch；直接整合模式乾脆把 Lambda 拿掉；durable function 則是把整條 orchestration 寫成程式碼，而不是狀態機。

🎯 實務啟示

如果你的 pipeline 裡有呼叫 agent、或任何延遲不固定的外部服務，第一件事是檢查呼叫方式是不是同步阻塞。需要保留自訂前後處理邏輯時用 task-token 模式；只是單純轉呼叫就用 Step Functions 的 SDK 服務整合；想把整個編排邏輯寫成程式碼，就選 durable function。核心原則只有一條：讓等待發生在不計費的協調層，而不是按秒計費的運算資源上。

🔗 來源
- 標題：Asynchronous patterns for calling Amazon Bedrock AgentCore agents in serverless pipelines
- 作者／機構：Daniel Abib, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/asynchronous-patterns-for-calling-amazon-bedrock-agentcore-agents-in-serverless-pipelines/

#AWS #AmazonBedrock #AgentCore #Serverless #AWSLambda #StepFunctions #AIAgents #CloudArchitecture #FinOps #DurableExecution
