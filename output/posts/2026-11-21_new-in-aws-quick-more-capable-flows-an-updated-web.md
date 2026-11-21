---
title: 'New in AWS Quick: More capable flows, an updated web experience, and agents
  that work together'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/new-in-aws-quick-more-capable-flows-an-updated-web-experience-and-agents-that-work-together/
model: claude-code/sonnet
generated_at: '2026-11-21T22:26:11.032488'
score: 62
---

📌 AWS Quick 更新：用聊天建流程、讓多個專長 AI 代理協同回答一個問題

TL;DR：AWS Quick 這次更新讓團隊能把個人流程變成共享自動化,並透過多代理協作取得更完整的答案。

很多團隊導入 AI 助理後都遇到同一個瓶頸：效率提升往往只停留在「某一個人」身上。那個人知道怎麼做月報、怎麼抓數據、怎麼寫評論,但他不在,流程就卡住,換人做結果還不一樣。AWS Quick 這次更新，想解的正是這個問題。

🤔 **一個人的習慣,怎麼變成整個團隊的流程**

AWS 以一個虛構案例說明：零售業財務規劃分析經理 Maya 每月要整理成本與利潤變動報告，流程全靠記憶與個人checklist，一旦她請假,同事就得從頭重建,每次做出來的報告都長得不一樣。

🧩 **在聊天裡直接建流程,並讓多個代理分工合作**

AWS Quick Flows 現在能完全在對話中建立、執行與調整：使用者用自然語言描述自己的作業流程（像在教新人一樣）,Quick 會把描述轉換成流程,並在對話旁同步顯示步驟圖供確認。流程可以整合 agents、skills、工具與資料,處理更長的流程與更多資料，並支援在 web、desktop、mobile 任一入口啟動與接續。

另一項更新是多代理編排（multi-agent orchestration）：當一個問題需要跨領域知識時，使用者詢問的代理可以同時呼叫多個專長代理各自處理自己熟悉的部分，再把結果整合成單一回覆，使用者可清楚看到每個代理各自貢獻了什麼。此外,Quick 新增了透過 Model Context Protocol（MCP）伺服器串接 Meta 廣告與 Amplitude 的連接器，讓團隊能用自然語言操作廣告活動或查詢產品使用行為，所有連接器都延續既有權限設定，且在執行任何「寫入」動作前都會先徵求使用者同意。

📊 **客戶案例：資料團隊的角色從「代工」變成「賦能」**

Latin American fintech 公司 Pomelo 的資料部門負責人 Rodrigo Marini 表示，導入 AWS Quick 後,團隊沒有擴編,但每月使用資料工作的人數成長近四倍,資料團隊因此能專注在最複雜、高影響力的工作上；其中一個使用案例每月就省下 80 小時的工作量。

🎯 **實務啟示**

對工程師來說,值得關注的技術細節是:流程建構從「寫程式/寫規則」轉移到「自然語言描述 + 代理自動生成」,以及多代理編排中「各代理保有自己的指令、知識與上下文」的設計,讓不同團隊可以獨立維護各自的代理而不互相干擾。若你的團隊已在評估企業級 AI workspace,MCP 連接器的權限繼承機制與寫入動作需人工核可的設計,是值得參考的安全邊界範本。

🔗 **來源**
- 標題：New in AWS Quick: More capable flows, an updated web experience, and agents that work together
- 作者／機構：Hillary Lovric, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/new-in-aws-quick-more-capable-flows-an-updated-web-experience-and-agents-that-work-together/

#AWSQuick #AIAgents #Automation #EnterpriseAI #MultiAgent #MCP #WorkflowAutomation #AWS #Productivity #GenerativeAI
