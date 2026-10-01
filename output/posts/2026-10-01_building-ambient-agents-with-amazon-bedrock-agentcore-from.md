---
title: 'Building ambient agents with Amazon Bedrock AgentCore: From event-driven signals
  to human-in-the-loop workflows'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-ambient-agents-with-amazon-bedrock-agentcore-from-event-driven-signals-to-human-in-the-loop-workflows/
model: claude-code/sonnet
generated_at: '2026-10-01T22:05:33.088460'
score: 89
---

📌 AWS AgentCore打造「環境式」代理：事件觸發，人類只在需要時介入

TL;DR：AWS展示如何用Bedrock AgentCore打造ambient agent，靠事件觸發取代對話框，並用單一ask_human工具實現human-in-the-loop。

檔案一上傳到S3，幾秒內工作就自動出現在Jobs頁面並開始執行，不需要任何人打開聊天視窗、輸入提示詞。這就是文章所稱的「ambient agent」。

🤔 背景：聊天式agent撐不起事件驅動的場景

多數AI agent體驗遵循請求—回應模式：使用者打開聊天介面、輸入提示、等待回覆。這適合一次性提問，但限制agent一次只能處理一個對話，而且需要人類先描述發生了什麼事，agent才能行動。對於檔案上傳、資料庫變更、排程任務、系統告警這類「事件發生在基礎設施各處」的場景，這套聊天模式就不夠用了。AWS指出，LangChain等業者已提出「ambient agent」這個不同典範：agent監聽事件串流並據此行動，可能同時處理多個事件，而非只由人類訊息觸發。但ambient agent並非完全自主，正式環境的設計會謹慎考慮agent該在什麼時候暫停並與人互動。

🧩 架構：事件→agent→人在迴圈中

文章定義的ambient signal，是一個「事件來源對應agent」的設定。事件發生時，平臺自動幫該agent建立一個job。整個流程端到端如下：Amazon S3發出s3:ObjectCreated通知；Signal Processor Lambda接收通知，查詢ambient-signals資料表的GSI，找出符合的signal，為每個符合項建立job紀錄；API層（或排程器）把job放進Amazon SQS佇列；Job Execution Lambda透過SQS event source把佇列清空，呼叫Amazon Bedrock AgentCore Runtime上的agent，並把結果（以及任何需要人類輸入的請求）寫回Amazon DynamoDB；透過Amazon CloudFront供應的React前端，輪詢一個小型Amazon API Gateway與Lambda層取得更新，讓使用者回應待處理的互動。

Amazon Bedrock AgentCore Runtime提供容器化的agent執行環境，支援長時間執行的workload、內建session隔離，並與Bedrock基礎模型整合。參考實作把每個agent turn的上限設在Lambda的15分鐘逾時，文章表示這在實務上已綽綽有餘。整體加上處理事件的AWS Lambda與管理狀態的Amazon DynamoDB，組成一套全serverless的ambient-agent平臺。

agent與人類的互動，全部透過單一工具ask_human完成，並回傳一個標準化的response envelope：狀態為completed、interrupted或error三者之一，對應欄位分別是result、question、error，另外session_id與job_id會貫穿每個回應以便串接後續輪次。當agent回傳interrupted，平臺會把job狀態改為interrupted並將requiresAction旗標設為true，React前端會在Jobs頁面的Interrupted分頁上用警示圖示標示出來，不需要另外的審核佇列。同一個Jobs畫面同時顯示待回答的問題、等待核準的提案行動、最終結果與失敗的job，讓使用者只需要看一個地方，而不是在多個聊天視窗或郵件串之間來回監看。

這套ask_human機制同時支援幾種提示樣式：Notify（agent單純回報結果）、Question（agent詢問澄清）、Review（agent提出行動並等待APPROVE/REJECT/MODIFY）、Error（失敗被記錄在job紀錄上，由使用者決定是否重試）。文章強調，這些只是agent撰寫問題時的慣例，平臺層面其實只有一條程式碼路徑與一種envelope格式。

💡 為何不用純自動化pipeline就好

文章點出兩種既有方案的侷限：全自動的pipeline（如AWS Step Functions）能編排workflow，但無法對模糊情境做推理或提出澄清問題；聊天式agent能推理，但需要有人先開啟對話。Ambient agent被定位為介於兩者之間的橋樑。AWS也指出，許多組織在AWS上已經具備事件驅動基礎建設（S3事件通知、EventBridge規則、Lambda觸發、DynamoDB streams），缺的只是把這些事件來源接上能推理、能行動、必要時能拉人進來的agent。

⚠️ 限制

素材提到的signal事件來源中，參考範例只實作了S3與排程兩種，其餘（如資料庫變更、系統告警）屬於擴充點，需要自行撰寫新的handler Lambda與對應的Signals頁面欄位。

🎯 實務啟示

如果你的團隊已經有文件落地S3、告警堆積等「沒人即時處理」的場景，這套ambient agent模式提供了一個現成的架構骨架：事件驅動觸發、單一human-in-the-loop工具、統一的Jobs視圖。比起從頭設計agent該何時暫停等人，直接參考這個ask_human envelope的設計（completed/interrupted/error三態）可以省下不少架構決策時間。

🔗 來源
- 標題：Building ambient agents with Amazon Bedrock AgentCore: From event-driven signals to human-in-the-loop workflows
- 作者／機構：Juan Albarran，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/building-ambient-agents-with-amazon-bedrock-agentcore-from-event-driven-signals-to-human-in-the-loop-workflows/

#AWS #BedrockAgentCore #AmbientAgents #HumanInTheLoop #EventDriven #Serverless #AIAgent #AWSLambda #AgenticAI #CloudArchitecture
