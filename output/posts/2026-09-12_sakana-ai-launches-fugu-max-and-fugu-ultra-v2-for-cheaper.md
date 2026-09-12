---
title: Sakana AI Launches Fugu Max and Fugu Ultra v2 for Cheaper, Stronger Multi-Agent
  Orchestration
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/10/sakana-ai-launches-fugu-max-and-fugu-ultra-v2-for-cheaper-stronger-multi-agent-orchestration/
model: claude-code/sonnet
generated_at: '2026-09-12T19:32:19.862074'
score: 83
---

📌 Sakana新模型不比大：靠路由省下2到6倍推理成本

TL;DR：Sakana AI推出Fugu Max與Fugu Ultra v2，用可學習的路由器在多個模型間動態調度任務，主打成本效益與高難度推理兩種場景。

把一個簡單的資料查詢丟給一個上兆參數的模型處理，本質上就是在浪費錢。Sakana AI的Fugu系列想解決的正是這個問題：它不是又一個更大的基礎模型，而是一個學會怎麼把工作分派給對的模型的協調者。

🤔 **Fugu不是單一模型，而是一個學會路由的協調層**

Sakana團隊的論點很直接：真實工作負載同時被能力與成本評判，好的系統應該挑選能解決任務的最便宜方案。團隊用Pareto frontier來描述這個取捨：在這條前緣上，提升品質必然要付出更高成本，砍成本也必然損失一些品質。Fugu是一個部署在單一API背後、把工作路由到一整組其他模型上的學習型協調器，而非單一基礎模型。

這次發布的Fugu Max與Fugu Ultra v2共用同一套核心協調架構，差別只在最佳化目標：Fugu Max追求每一塊錢能換到最好的輸出，Fugu Ultra v2則追求在困難的多步驟任務上取得最高能力。兩者目前都已透過Sakana與OpenAI相容的API上線，沒有開放權重可供自架，且Sakana目前不在歐盟/歐洲經濟區提供此服務。

🧩 **建立在兩篇ICLR 2026論文上的協調機制**

根據Sakana Fugu的技術報告，Fugu本身被定位為一種語言模型：它讀入查詢後，即時建構出一套agentic的執行架構。訓練方式結合大規模微調、演化演算法與強化學習,並建立在兩篇ICLR 2026論文之上——TRINITY用一個輕量級、經演化訓練出的協調器，在多輪對話中分配Thinker、Worker、Verifier三種角色；Conductor則透過強化學習，學會用自然語言發掘協調策略與聚焦提示。

Fugu Max進一步擴大了可調度的模型池，加入大量開放權重與專用模型，其中包含透過Sakana與NVIDIA合作納入的NVIDIA Nemotron家族。Fugu Max會把每個任務路由到能解決它的最精簡模型。

📊 **廠商自報數字：2到6倍成本優勢，但要打個折扣看**

Sakana團隊表示，Fugu Max的表現已能與頂尖模型相去不遠，但成本只要2倍到6倍更低,這項結果來自Sakana內部以自家程式編寫挑戰打造的SWEFish benchmark,屬於廠商自報的訊號,需要保留一定的觀察空間。

Fugu Ultra v2則鎖定複雜推理、自主研究與全端軟體開發，最大的進步幅度出現在對視覺與結構化資料的持續推理任務上。值得注意的是,Fable 5、Fable 5.1與GPT-6-Astra並不在Fugu Ultra v2可調度的模型池之中，其訓練資料截止日為2026年8月28日。

Sakana的核心訴求是：不必依賴任何單一專有模型也能取得前沿等級的輸出，藉此降低對特定廠商的依賴風險，包括vendor lock-in、API權限被收回或服務突然中斷等情境。

⚠️ **只能託管使用，且發布節奏相當快**

Fugu系列的推進速度不慢：今年4月進入beta，6月正式上線，7月加入Fugu-Cyber與Claude Code整合介面。但截至目前，Fugu仍只提供託管API,沒有開放權重可自行部署，也還未在歐盟/歐洲經濟區開放服務,而效能數字目前仍以廠商自建的內部benchmark為主。

🎯 **實務啟示**

如果你的團隊正在評估多模型路由方案以控制推理成本，Fugu提供了一個現成的參考架構：把「該用哪個模型」這個決策本身也交給一個訓練過的協調器，而不是靠人工規則硬編。但在導入前,建議先用自己的任務集驗證SWEFish之類的廠商benchmark是否可信，並評估託管API模式是否符合資料與合規需求。

🔗 **來源**
- 標題：Sakana AI Launches Fugu Max and Fugu Ultra v2 for Cheaper, Stronger Multi-Agent Orchestration
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/10/sakana-ai-launches-fugu-max-and-fugu-ultra-v2-for-cheaper-stronger-multi-agent-orchestration/

#SakanaAI #MultiAgent #LLMRouting #AgenticAI #AIOrchestration #NVIDIA #ICLR2026 #CostEfficientAI #AIInfrastructure #FoundationModels
