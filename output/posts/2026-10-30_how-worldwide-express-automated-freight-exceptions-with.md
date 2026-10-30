---
title: How Worldwide Express automated freight exceptions with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-worldwide-express-automated-freight-exceptions-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-30T21:42:17.442670'
score: 90
---

📌 物流巨頭如何用多智能體 AI 解開 $15M 帳務卡關

TL;DR：Worldwide Express 用 Amazon Bedrock 打造三智能體系統，六個月內讓貨運帳務爭議減少 75%，釋出 $10M 現金流。

每個月有 $15 百萬美元的自由現金流，不是因為沒賺到，而是卡在沒人處理的帳務爭議裡，這是 Worldwide Express 的真實處境。公司系統性營收約 50 億美元，合作超過 75 家 LTL（less-than-truckload，零擔貨運）承運商，服務超過 13 萬名客戶，規模夠大，卻也讓例外帳務愈積愈多。

🤔 **14% 的發票卡在三方比對失敗**

在 LTL 貨運流程中，約 14% 的發票無法通過標準的「採購單、收貨單、承運商發票」三方比對。比對失敗就進入例外處理，而每一筆例外都要走一套五步手動流程：對照承運商各自的附加費規則、比較運費資料、判斷爭議是否成立。由於每家承運商的關稅結構與爭議流程都不同，這件事幾乎吃掉了 FinOps 團隊大部分的時間，過去甚至外包給團隊逐案打電話給客戶與承運商處理。規則式的 RPA 能處理結構化流程，但例外判斷需要上下文推理，這正是促使 Worldwide Express 轉向 agentic AI 的原因。

🧩 **三個專責 agent，各管一種爭議類型**

2025 年 6 月，AWS 的 Business Transformation & Value Advisory 團隊協助 Worldwide Express 在 Order-to-Cash 流程中找出 19 個自動化機會，公司在不到 6 個月內從評估走到正式上線。整套方案跑在 AWS 上：Amazon Bedrock 提供 AI 推理能力，Amazon EC2（搭配 Auto Scaling）是執行引擎。系統偵測到帳務例外後，會路由給三個專責的 AI agent 之一，每個 agent 處理特定類型的帳務爭議。每個 agent 都有明確的指令 prompt（定義角色、決策邊界與輸出格式）、一組串接 SpeedShip TMS 的 actions，以及存取承運商專屬的知識庫（關稅規則、附加費定義、爭議流程、容許誤差門檻）。agent 透過與分析師相同的 API 連進 SpeedShip，看到的資料（合約費率、貨運明細、送達證明）與人工審核者完全一致，解決方案也寫回同一套工作流程，因此同一組三個 agent 就能處理所有承運商，不需要為每家客製程式碼。

每次例外解決後，系統會生成一段白話文說明，記錄發現了什麼、採取了什麼行動，確保每個自動化決策都可被稽核。上線初期，人工審核者仍須在既有的 SpeedShip 介面上核准建議，等到準確率超過 99%，批量核准才成為預設流程。團隊也建置了儀表板，追蹤各承運商的自動化比例、各例外類型的錯誤率、解決時間與人工覆核頻率；一旦審核者否決建議，系統會記錄回饋，用來持續優化 prompt 與知識庫。

📊 **六個月後：例外積壓減少七成五**

六個月後，這套方案已覆蓋超過 40 家 LTL 承運商，每週自動結案約 10,000 筆例外（約佔整體一半），錯誤率低於 1%。最直接的成果是帳務例外積壓從 2025 年 6 月的 1,500 萬美元降到 400 萬美元，減少 75%；公司因此釋出 1,000 萬美元的一次性自由現金流，每年額外節省超過 100 萬美元成本，第一年投資回報率達 60 倍，時間到現金（time-to-cash）改善了四週。Worldwide Express FinOps 副總裁 Nathanael Pearson 表示：「透過 AWS，我們自動化了超過 40% 的每週帳務例外，大幅降低成本並把帳務週期從數天縮短到數分鐘，現在我們每週能多釋出約 1,000 萬美元的客戶帳款，這在過去根本不可能做到。」

⚠️ **人工覆核不是過渡期的妥協，是信任的基礎**

人工審核這一步在初期導入時是必要的，它讓 FinOps 團隊能在信任自動化之前持續驗證準確率，也讓每個決策保有可解釋性與財務控管，這對帳務爭議這種需要被稽核的場景格外重要。

🎯 **實務啟示：先挑最頻繁的例外類型下手**

對管理大量承運商的物流公司而言，可行路徑是先自動化最重複出現的例外類型，證明準確率後再擴大到整個組合。Worldwide Express 目前已把這套模式延伸到 Order-to-Cash 流程的其他環節，顯示一個範圍界定清楚的業務問題，搭配 agentic AI、承運商專屬知識庫與人在迴圈（human-in-the-loop）的設計，能在維持財務控管的同時快速落地。

🔗 **來源**
- 標題：How Worldwide Express automated freight exceptions with Amazon Bedrock
- 作者／機構：Saumya Shah
- 連結：https://aws.amazon.com/blogs/machine-learning/how-worldwide-express-automated-freight-exceptions-with-amazon-bedrock/

#AmazonBedrock #AgenticAI #AWS #Logistics #FinOps #MultiAgentSystems #ProcessAutomation #EnterpriseAI #CloudComputing #AIinProduction
