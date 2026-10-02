---
title: Scaling cloud migrations with agentic AI on Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/scaling-cloud-migrations-with-agentic-ai-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-10-02T21:34:09.173161'
score: 85
---

📌 300 多個應用程式、一個財政年度期限：AWS 用四個 Agent 把 IaC 開發時間從週級壓到分鐘級

TL;DR：AWS Professional Services 在 Bedrock AgentCore 上打造四代理架構，與 AWS Transform／DMS 並行加速大型雲端遷移。

一個雲端遷移專案要在固定的財政年度期限內，處理超過 300 個應用程式，這時候一個很實際的問題是：哪些工作該交給既有的托管服務，哪些需要自己動手做自動化？AWS 在這篇文章給出的答案是「兩者並行」。

🤔 為什麼托管服務不夠用

在這個專案裡，AWS Transform 負責伺服器、網路、主機、.NET 與應用程式碼等工作負載的遷移與現代化，AWS DMS 負責資料庫層，這些都是托管服務。但這個專案多了一個額外條件：來源與目的地系統，都必須透過組織自己建置、自己維護的 Model Context Protocol（MCP）工具來存取。為了補上這一塊，AWS Professional Services 建了一套以 Strands Agents SDK 開發、跑在 Amazon Bedrock AgentCore 上的客製化 agent 系統，每個 agent 都透過 AgentCore Gateway 暴露的 MCP 工具去接觸自己的來源與目的地。

🧩 兩條旅程、四個 Agent

整套架構分成兩條旅程：migration journey 涵蓋從盤點到部署，由多個 agent 分工；operations journey 則由一個 agent 負責遷移後的監控。文中具體描述了其中兩個 agent 的運作方式。

Intake Agent 透過 MCP 工具讀取存放在文件與協作系統中的遷移輸入資料，包括架構文件、應用程式清單、盤點問卷與相依性紀錄，產出目標 AWS 架構、建議的遷移模式、資源規模建議與合規驗證報告，這份輸出直接餵給 IaC Agent，形成從盤點到佈建的自動交接。

IaC Agent 是整個產品組合中最先部署、也是效益最直接可衡量的一個，運作分五個步驟：先讀取 wave 團隊提供的 steering document，擷取部署範圍、合規限制與安全辦公室核准的 wave 層級例外；再解讀 Intake Agent 輸出的目標架構圖，辨識基礎設施元件及其相依關係；接著依組織既有的 IaC 範本產生程式碼，填入 wave 專屬參數，設定遠端 state 管理，並套用強制標籤與監控設定；在執行之前，AgentCore 中的 Policy 元件會依 Cedar 規則驗證每一次工具呼叫，計算潛在變更範圍、檢查與並行 wave 的相依衝突、確認合規時窗是否仍然有效；最後交由中央執行平面觸發 IaC、監控部署，並透過 AgentCore Observability 回報結果，部署後驗證自動執行，合規指標即時更新。

Amazon Bedrock AgentCore memory 儲存 session 狀態與共享上下文，讓超過 300 個應用程式的遷移進度得以跨 agent 追蹤：Intake Agent 完成盤點後，會把目標架構與相依性對應寫進 AgentCore memory，IaC Agent 直接讀取這份共享上下文就能開始產生程式碼，不需要人工交接。

🔒 安全設計內建在每個環節

AgentCore Identity 用最小權限的 IAM 角色驗證每一次 agent 呼叫，並結合組織的身分供應商；輸入會在邊界先依 schema 驗證，格式異常直接拒絕；任何憑證或機敏值都不會流經 agent context，因為 AgentCore Identity 會在執行期間，從集中式憑證提供者即時解析密鑰；AgentCore Observability 與 AWS CloudTrail 則把每一個 agent 動作寫入不可竄改的集中稽核軌跡。Policy 元件執行的 Cedar 規則，能防止單一操作影響超過設定門檻的範圍，而且這組策略集是由安全辦公室制定與維護，不是交給 agent 自行決定。

📊 IaC 開發時間從週級壓到分鐘級

根據內部專案追蹤資料，這套四 agent 模式把每個應用程式的 IaC 開發時間，從原本的三到四週縮短到幾分鐘。

🎯 實務啟示

當組織既有的托管遷移服務已經覆蓋大部分流程，真正值得自建 agent 的地方，往往是那些組織自維護的客製整合點，例如自建的 MCP 工具層，而不是重造整條遷移管線。另一個值得借鏡的設計是：把身分治理、政策驗證與可觀測性內建到 agent 的每一次工具呼叫路徑中，而不是事後補強，這是讓大規模、跨 300 個應用程式運作的 agent 系統能被稽核、被信任的關鍵。

🔗 來源
- 標題：Scaling cloud migrations with agentic AI on Amazon Bedrock AgentCore
- 作者／機構：Nikhil Jha（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/scaling-cloud-migrations-with-agentic-ai-on-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #AgenticAI #CloudMigration #MCP #StrandsAgents #InfrastructureAsCode #AIAgents #EnterpriseAI #AWSTransform
