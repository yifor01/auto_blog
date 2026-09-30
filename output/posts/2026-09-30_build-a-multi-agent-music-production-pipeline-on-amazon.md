---
title: Build a multi-agent music production pipeline on Amazon Bedrock AgentCore Runtime
  Instances
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-music-production-pipeline-on-amazon-bedrock-agentcore-runtime-instances/
model: claude-code/sonnet
generated_at: '2026-09-30T21:43:47.068072'
score: 89
---

📌 AWS讓多個Agent共用GPU跑好幾天的協作

TL;DR：AWS Bedrock AgentCore 新推出 Runtime Instances，讓多個 agent 共享 GPU 與檔案系統，支援長達 14 天的持續協作工作流。

單一 agent 回答客服問題，短短幾小時的 serverless session 綽綽有餘；但如果是三個 agent 要花好幾天合作完成一段音樂創作，彼此需要共享上下文、接續對方的產出，傳統 serverless 的 session 時限根本撐不住。AWS 這篇教學就示範了怎麼用新的運算選項解決這個問題。

🤔 **多代理系統改變了基礎設施需求**

Amazon Bedrock AgentCore 原本提供 MicroVMs 這種無伺服器選項：冷啟動快、session 彼此隔離、按用量計價。這次新增的 Runtime Instances，則是 AWS 代管的 EC2 基礎設施，專為長時間執行的 agent 工作流設計。兩者共用同一套 runtime API，差別在於底層運算模型：MicroVMs 是一個 runtime 對應一個 agent，Runtime Instances 則能讓多個 agent 共用同一個 session，只要用相同的 runtimeSessionId 呼叫，多個 runtime 就會被安排到同一臺 EC2 執行個體上，共享檔案系統並協同作業。

🧩 **三個 agent：作曲、後製、合規把關**

這次示範的音樂製作系統包含三個專責 agent。composition agent 用 Claude Sonnet 4.6 把製作人的需求轉成音樂簡報，再呼叫 ACE-Step 這個生成式音訊基礎模型，在該 instance 的 GPU 上實際算出一段音訊。delivery agent 從共享檔案系統讀取這段 .wav，測量後用 Claude Sonnet 4.6 決定 EQ 頻段與壓縮器設定，套用訊號處理後再重新測量一次，確認結果真的達標，而不是單憑推論。compliance agent 接著獨立重新測量，核對 delivery agent 宣稱的交付目標，並比對工作室既有作品庫檢查和聲相似度；一旦發現雷同，就會回頭呼叫 composition agent 產生替代版本。

**架構細節**：capacity provider 負責指定 instance 類型與 VPC 配置，由 AgentCore 代管佈建與生命週期；需要兩個信任 bedrock-agentcore.amazonaws.com 的 IAM 角色；命名時要用底線而非連字號。每個 agent 都部署成獨立的 runtime，並在呼叫時各自掛上 capacity provider，指定要掛載哪些 volume，最後用同一個 runtimeSessionId 逐一呼叫，就能讓它們落在同一臺機器上互相交棒。

🎯 **實作眉角與運維要點**

文中提到兩個容易搞錯、而且出錯訊息很模糊的地方：SDK 是靠參數名稱 params[1] == "context" 來判斷、讀取 session ID（agent 要靠這個找到彼此的檔案並互相呼叫）；另外 Agent 物件要建在 handler 內部而非模組層級，否則多個並行請求共用同一個模組層級 Agent，會被 Strands 拒絕並丟出「Agent is already processing a request」錯誤。對話歷史則透過掛在 volume 上的 FileSessionManager 保存，讓幾天後恢復的 session 依然記得先前的決策。

第一次呼叫會比較慢，因為要佈建 instance；之後的呼叫都會直接路由到已經在跑的機器上。呼叫 StopRuntimeSession 後，instance 會自動閒置下來，閒置期間不計費；之後再次呼叫會恢復 session，前提是落在同一個可用區（Availability Zone）。由於 Amazon EBS volume 是綁定可用區的，若原本的 AZ 容量不足，volume 就無法重新掛載、持久狀態也會跟著遺失，需要用 AZ 綁定的 ODCR 或指定 MODELS_SNAPSHOT_ID 來因應。Session 最長可持續 14 天。

這個架構也讓獨立部署變得簡單：某個團隊要更新 composition agent，只需要更新自己的 runtime，delivery 與 compliance agent 完全不受影響，不需要協調、不共用部署流程，也不會有互相打架的風險。要結束整個 pipeline，先刪除 session 就會一併解除佈建 EC2 instance、網路介面與 EBS volume，是停止計費最直接的方式。

🔗 **來源**
- 標題：Build a multi-agent music production pipeline on Amazon Bedrock AgentCore Runtime Instances
- 作者／機構：Evandro Franco, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/build-a-multi-agent-music-production-pipeline-on-amazon-bedrock-agentcore-runtime-instances/

#AWS #BedrockAgentCore #MultiAgent #AgenticAI #GPU #StrandsAgents #CloudInfrastructure #AudioAI #AgentOrchestration #MLOps
