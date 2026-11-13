---
title: Architecture patterns for fast session startup on Amazon Bedrock AgentCore
  runtime
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/
model: claude-code/sonnet
generated_at: '2026-11-13T22:54:45.735544'
score: 82
---

📌 Amazon Bedrock AgentCore V2：用一次建置、無數次快照還原砍掉 Session 冷啟動

TL;DR：AgentCore runtime V2 改成只初始化一次並做快照還原，讓 Agent Session 啟動更快更穩定。

當 Agent 坐在聊天或語音這類互動體驗背後，使用者多等 2 秒都嫌太久。Amazon Bedrock AgentCore runtime V2 的解法是：把初始化這件事只做一次，之後每個新 session 都靠還原快照來啟動。

🤔 **每個 Session 都重新 pull image、重新初始化，冷啟動自然隨映像檔大小增加**

AgentCore runtime 讓每個 session 跑在獨立的 microVM 裡，平臺可以 scale to zero，只對實際用到的資源計費。但在 V1 架構下，每個新 session 都要從 Amazon ECR 重新拉取容器映像檔、啟動容器，再跑一次初始化程式碼才能處理第一個請求；映像檔拉取的時間主導了整體冷啟動，映像檔越大就越慢。

🧩 **把 init 搬到建置階段，session 只需要「醒過來」**

V2 的做法是：每次 create 或 update runtime 時，先在一個全新的 microVM 裡啟動容器，等到第一次 GET /ping 回應健康（須在 120 秒內完成），接著清掉作業系統的檔案快取以縮小快照體積，凍結這個 microVM，把記憶體與磁碟狀態存成一份快照。這個 build 流程只在每次 create/update 時跑一次，因此每次 create/update 都會多花幾分鐘。這裡的「init」指的是在 AgentCore Python SDK 裡 app.run() 之前的所有程式碼；若自己架 HTTP 伺服器，則要等初始化真正完成才回報健康。

當新 session 進來時，平臺直接從快照還原出一個新的 microVM，process 會回到被凍結時的狀態，imports、物件、client 全部已經就位；映像檔裡的檔案則是 lazy load，每個區塊是在 session 第一次讀取時才去抓取。但如果 init 階段啟動過一個獨立的 process（像 CLI 工具或瀏覽器 binary）後就結束了，這類資源在快照還原後並不會留在記憶體裡，需要靠新支援的 build hook 額外處理。

量測延遲要分兩段看：AgentCore 在 CloudWatch 的 AWS/Bedrock-AgentCore namespace 下發布 Latency（到第一個 byte 的時間）與 OverheadLatency（平臺啟動 microVM、還原快照所花的時間）兩個指標，建議用 P90/P99 或 TM90 這類 trimmed mean 而不是平均值，並且用跟正式環境相近的新 session 啟動比率去做測試，才不會被少量 session 的結果誤導。

💡 **跟一般 cold start 優化思路相反：該把工作搬進 init，不是搬出來**

一般冷啟動優化建議是 lazy import、把初始化壓到最小，但在 V2 架構下 init 只在建置快照時跑一次，而延後到 handler 裡做的工作卻是每個新 session 都要重新付一次代價。因此 Perplexity……（此處應為 AWS）建議反過來：在 init 階段就建立好物件而不只是 import 模組、把 client（像 boto3）在 init 階段建立好（endpoint 解析、憑證解析、client 模組都會跟著快照回來，雖然 socket 不會，但 boto3 client 可以在第一次呼叫時乾淨地重新連線）、把靜態資料（prompt、設定、小型索引）用物件形式保留在記憶體中、讓常駐工具（像 language server）在 init 時就啟動並長駐，透過 pipe 或 socket 通訊而不是每次請求都重新啟動 subprocess、把無法留在記憶體裡的檔案複製到 /dev/shm 這類 RAM-backed 磁碟、並設定 UV_COMPILE_BYTECODE=1 讓 bytecode 提前編譯好。

⚠️ **搬進 init 的工作越多，快照越大，記憶體成本也隨之上升**

把更多工作搬進 init 可以縮短 handler 的執行時間，但任何留在記憶體裡的東西都會讓快照變大，而且每個 session 都要為這份保留的記憶體付費，這是一個需要權衡的取捨。

🎯 **先分清瓶頸在平臺還是自己的程式碼，再決定搬什麼到 init**

若在 AgentCore 上跑互動式 Agent，建議先用 CloudWatch 的 Latency 與 OverheadLatency 區分瓶頸來源，再評估哪些 client、常駐工具、靜態資料值得提前到 init 階段建立。這個思路跟 AWS Lambda SnapStart 的 priming 策略相通，用過 SnapStart 的團隊可以直接套用類似的心智模型。

🔗 來源
- 標題：Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime
- 作者／機構：Evandro Franco, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/

#AWS #AmazonBedrock #AgentCore #Serverless #ColdStart #AIAgents #CloudComputing #MicroVM #Latency #DevOps
