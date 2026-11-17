---
title: Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/
model: claude-code/sonnet
generated_at: '2026-11-17T01:06:07.330673'
score: 88
---

📌 【AWS 實務拆解】多Agent系統為何總在正式環境卡關？

TL;DR：AWS 用拓撲學方式整理多agent協調模式與反模式，點出可靠性會隨步驟數暴跌。

一個流程只要串接 10 個步驟，每步 95% 可靠，端到端成功率就只剩 59.9%；串到 20 步，更只剩 35.8%。這不是悲觀假設，而是多 agent 系統最常被忽略的數學。AWS 這篇文章也引用 Stanford HAI 的觀察：兩個模型協作的表現，有可能比任何一個模型單獨工作還差，前提是協調的開銷超過了協作帶來的好處。

🤔 **多Agent協調其實是分布式系統問題**

文中指出，企業團隊在導入多 agent 系統時，踩坑的根因很少是模型本身不夠強，而是團隊還沒建立起分布式系統的直覺。素材引用的業界數字顯示，約 88% 的 AI pilot 專案始終無法進入正式環境。團隊往往是「複雜度堆疊的速度」超過了「理解系統的速度」——每多一次 agent 之間的交接（handoff），就多一次風險的乘法效應。

🧩 **兩層協調模式：誰決定流程走向**

AWS 把協調模式分成兩個層級，區分依據是「流程路徑由誰決定」：

**Tier 1：開發者在建置時就定義好路徑**
- Sequential Pipeline（序列管線）：A→B→C 線性執行，每個節點輸出餵給下一個節點，適合文件處理、ETL、保固理賠初篩等順序明確的任務。
- Conditional Workflow（條件工作流）：加入 pass/fail 判斷分支，失敗則迴圈重試最多 N 次，超過上限就升級給人工處理，常透過 AWS Step Functions 的迭代上限來強制設下界線，避免落入「無限迴圈」反模式。
- Conditional Router（條件路由）：分類步驟先讀懂輸入，再把請求導向唯一一條專職 agent 路徑，例如品質、維護、排程三個 agent 各自處理對應問題，每個請求只會走一條路。
- Parallel Workflow（平行工作流）：任務拆成獨立子任務，交給多個 handler 同時處理，再用 fan-in 步驟整合結果；單一路徑失敗只重試該路徑，整體延遲等於最慢的那個 agent，而非所有 agent 時間加總。

**Tier 2：模型在執行時自行決定路徑**，靈活度更高，但會付出更多 token、延遲與除錯成本：
- Plan-based Orchestration（計畫式協調）：一個 orchestrator agent 扮演專案經理，維護明確的任務計畫與依賴關係，worker agent 彼此獨立、無狀態，單一 worker 失敗不會污染其他節點，orchestrator 只需重試失敗的那一個。
- Handoff Pattern（交接模式）：agent 之間以 peer-to-peer 方式局部決策、互相轉移控制權，交接時必須連同「已驗證的任務狀態、證據、尚未解決的問題」一起傳遞——文中特別強調，只透過對話內容傳遞摘要,不算真正的交接。
- Conversation-driven Pattern（群聊式協調，也稱 group chat pattern）：所有 agent 共享同一個對話，由選擇機制決定下一個發言的 agent，協調關係隱含在對話歷史中，近似人類團隊的共同討論。
- Debate / 多方表決模式：多個 agent 各自獨立評估同一輸入,彼此在表態前看不到對方的推理過程,再由多數決、裁判 agent 或人工升級來裁定分歧。文章特別提醒這是成本最高的模式，在感知類任務（如品質檢驗）上,辯論換來的常是延遲而非準確率提升，應保留給「錯了代價很高、量又很少」的高風險決策。

💡 **實務上的預設策略**

文章給出一條清楚的預設路線：先從 Tier 1 開始，只有當子任務在執行過程中才會逐漸浮現、無法在建置時預先定義時，才把任務移往 Tier 2。這等於是提醒團隊：靈活度不是免費的,先用可預測、可除錯的路徑把問題解決,再視需要升級協調複雜度。

🎯 **實務啟示**

在評估是否需要多 agent 之前,先問自己兩個問題:這個任務的步驟數會不會讓端到端可靠性被乘法效應吃掉?流程走向真的無法在建置時定義,還是只是偷懶沒設計好?多數企業場景其實適合 Tier 1 的確定性路徑,Debate 這類最昂貴的模式應該謹慎留給真正高風險、低量的決策。

🔗 **來源**
- 標題：Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing
- 作者／機構：Malini Sethi，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/

#MultiAgent #DistributedSystems #AgentOrchestration #AWS #AIArchitecture #LLMAgents #SystemDesign #Reliability #EnterpriseAI #AgenticWorkflow
