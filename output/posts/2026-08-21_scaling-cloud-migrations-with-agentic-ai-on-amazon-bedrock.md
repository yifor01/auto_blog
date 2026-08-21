---
title: Scaling cloud migrations with agentic AI on Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/scaling-cloud-migrations-with-agentic-ai-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-08-21T06:33:25.358206'
score: 86
---

📌 【AWS案例】IaC撰寫從三週壓到幾分鐘

TL;DR：AWS用多代理架構，把雲遷移IaC撰寫時間從三週壓縮到幾分鐘。

300多套應用系統、一個固定的會計年度死線，光是搞懂每套系統現在長什麼樣，就要耗掉數週時間，這幾乎注定進度會落後。AWS Professional Services面對這種規模的資料中心退場遷移專案時，選擇用一套多代理框架把重複性工作交給AI。

🤔 三個卡住遷移專案的瓶頸

大型企業資料中心退場遷移專案，普遍會卡在三個環節。第一是人工盤點負擔過重：多數遷移從探索階段開始，得理解地端架構、盤點清單、依賴關係與問卷內容，人工探索每個應用要耗費數週，300多套應用光是這一項瓶頸就足以威脅積極的遷移時程。第二是重複的基礎設施開發：工程師定義好目標架構後，得為每個應用從零撰寫IaC，沒有自動化的話通常要3到4週，300多套應用累加起來就是數年的工程投入。第三是被動的遷移後維運：團隊仰賴人工監控與被動回應，缺乏主動偵測效能劣化或自動修復的能力,長期下來營運負擔會不斷累積。

🧩 架構：Strands Agent + Bedrock AgentCore，多個Agent接力

這套框架把agent分成兩條旅程：遷移旅程涵蓋探索到部署，維運旅程則負責遷移後的監控，整體共包含四個agent。每個agent都是一個Strands agent，由基礎模型、system prompt與一組工具定義而成，並託管在Amazon Bedrock AgentCore runtime上，具備無伺服器環境下的session隔離與多代理協調能力。每個agent透過AgentCore Gateway呼叫範圍限定於自身職責的MCP工具，Gateway能把既有的API、AWS Lambda函式與服務轉換成MCP相容工具；AgentCore Identity則透過範圍限定的IAM角色與身分提供者驗證每一次呼叫。Amazon Bedrock AgentCore memory用來儲存agent的session狀態與共享上下文，讓agent之間能追蹤300多套應用的遷移進度：Intake Agent完成探索後，會把目標架構與依賴關係映射寫入memory，IaC Agent再直接讀取這份共享上下文開始產生程式碼，不需要人工交接。

📊 IaC Agent的五步驟工作流程

第一步，讀取來自遷移波次（wave）團隊的steering document，取得部署範圍、合規限制，以及經Security Office核准的波次專屬例外規則。第二步，解讀Intake Agent輸出的目標狀態架構圖，辨識基礎設施元件及其關係與依賴。第三步，依據組織既有的IaC規範產生程式碼，帶入波次專屬參數、設定遠端狀態管理，套用強制標籤，並加上組織要求的監控設定。第四步，在執行前先經過Amazon Bedrock AgentCore中的Policy驗證：依Cedar規則評估每一次工具呼叫，計算潛在變更範圍，檢查與其他並行波次的依賴衝突，並確認是否落在合規允許的時間窗口內。第五步，由集中式執行平面觸發IaC、監控部署過程，並透過AgentCore Observability回報結果；部署後驗證會自動執行，合規指標也即時更新。每個動作都會經過AgentCore Gateway暴露的自訂MCP工具，並受AgentCore Identity與Policy in AgentCore管控，Identity以最小權限的IAM角色驗證每個agent的行動，框架本身也會依schema驗證輸入，在邊界處拒絕格式錯誤的輸入。

💡 效果的量測基礎要看清楚

文章指出，這套框架把300多套應用組合中，每個應用的IaC開發時間從3到4週縮短到幾分鐘，但這個數字是根據內部專案追蹤資料得出，並非經第三方稽核或公開基準測試驗證，讀者在評估這項成果時值得留意這個前提。

⚠️ 重現這套模式的前提不低

要跟著這套架構走，需要具備Amazon Bedrock AgentCore與Bedrock基礎模型的存取權限，並熟悉Strands Agents SDK、MCP伺服器模式，以及自身組織既有的IaC工具鏈，這些前提對一般團隊而言仍有一定門檻。

🎯 實務啟示

無論是否使用AWS的工具鏈，這個案例有兩個做法值得借鏡：第一，把每個生命週期階段產生的上下文（例如目標架構、依賴關係映射）寫入共享的memory機制，讓下游agent不必依賴人工交接就能接續工作；第二，讓每一次agent產生的基礎設施變更，在執行前都先經過政策或規則的評估關卡，而不是等出了問題才事後補救。

🔗 來源
- 標題：Scaling cloud migrations with agentic AI on Amazon Bedrock AgentCore
- 作者／機構：Nikhil Jha（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/scaling-cloud-migrations-with-agentic-ai-on-amazon-bedrock-agentcore/

#AgenticAI #AWS #CloudMigration #AmazonBedrock #InfrastructureAsCode #MultiAgentSystems #StrandsAgents #MCP #DevOps #EnterpriseAI
