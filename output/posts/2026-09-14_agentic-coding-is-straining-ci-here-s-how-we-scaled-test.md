---
title: Agentic coding is straining CI. Here’s how we scaled test impact analysis at
  Anthropic
source: Claude Blog
url: https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic
model: claude-code/sonnet
generated_at: '2026-09-14T21:03:18.659059'
pinned: true
---

📌 Claude 寫程式碼太快，反而把 Anthropic 自家 CI 逼到極限

TL;DR：6 個月內 CI job 量暴增 25 倍，Anthropic 修補三次後才重新設計出可水平擴展的測試選擇服務。

當寫程式碼不再是瓶頸，壓力會轉移到哪裡？Anthropic 工程團隊給出的答案是：CI。過去六個月，他們的 CI job 量暴增 25 倍，逼得團隊三度緊急打補丁，補丁分別只撐了 70 天、29 天、不到一天，最後才痛下決心重新設計整個服務。

🤔 **AI 把 PR 產出量拉高，CI 先撐不住**

Anthropic 工程師平均每季產出的程式碼量是 2021 到 2025 年間的 8 倍，其中 80% 由 Claude 撰寫，Claude 也大量參與 PR 審查與核准工作。與此同時，整個程式碼庫的測試量成長了 10 倍，工程師人數只小幅增加。這些因素疊加，讓 CI job 量在六個月內暴增 25 倍（並非每個 PR 都會跑全部測試）。

🧩 **測試選擇服務的架構：listener 與 selector**

Anthropic 內部有一套「確定性測試影響分析」（test impact analysis）服務，依據過往表現與套件相關性，決定每次變更該跑哪些測試，而非每次改動都跑全部測試。它依賴兩個元件保持同步：「listener」記錄每次 CI 執行的測試結果，「selector」讀取測試結果歷史，決定每個開啟的 PR 該跑哪些測試。這套 v0 架構以單一 process 運作，因為維護每個測試的持續歷史需要單一寫入者，這也讓服務無法水平分片。

📊 **三次補丁，一次比一次撐得更短**

去年 10 月服務開始出現吃緊跡象，團隊連續兩天被叫醒處理。第一次補丁是直接把運行服務的核心數加倍，撐了 70 天。第二次補丁把 listener 依套件分片，讓每個套件的狀態各自有獨立 worker，只撐了 29 天。第三次在今年 3 月，process 常在平日下午就達到記憶體上限，團隊試過換記憶體配置器、調整垃圾回收都沒用，最後靠每日重啟頂著，但這次補丁不到一天就失效，且重啟反而讓服務逐漸落後：一旦落後超過一小時，大量 job 結果就沒被 listener 記錄下來，導致 selector 用過時資料決定測試範圍，結果多半是重複跑那些早已知道會 flaky 或大範圍失敗的測試。文中特別說明，這不代表 CI 沒有跑或未測試的程式碼被推上線，而是測試選擇的依據資料變得不準確。listener 落後 20 分鐘，就可能造成數萬筆測試更新沒有套用到 selector。

**重新設計：讓 listener 變成無狀態、可水平擴展**

團隊最終給測試選擇服務加了一個記憶體內資料庫（in-memory data store），把大量原本由單一 process 處理的記憶體運算卸載出去。現在任何 listener worker 都能處理任何結果，把它寫進 journal 後就結束，不需要在記憶體中保留狀態，因而做到無狀態、可水平擴展。一個獨立的小型 consumer process 每隔幾秒把 journal 匯整成每個測試的歷史紀錄，selector 便能快速查詢相關結果。這個專案由一名工程師花了三週完成，作者提到若在一年前，同樣的工作恐怕要花上一季。

💡 **教訓：永遠要為指數成長做準備**

作者強調，加大機器、平行化、重啟服務這些具體技巧本身並不是重點，重點在於這些權宜之計能爭取到的時間一次比一次短，反而是整個服務的重新設計，如今花的時間比過去更短、也更能撐得住。過程中，團隊用內部版本的 Claude Tag 開了一個長期監控此服務的對話，只要 listener 延遲超過 5 萬個 job，Claude 就會主動提醒並延續先前討論，多次建議直接大改架構，但團隊起初多半還是選擇再打一次補丁。

⚠️ **新架構的代價**

作者也坦言，這套分散式架構的運行成本比單體服務更高，但相對地更容易擴展與做記憶體效能分析。此外，在問題浮現初期，服務的歸屬權其實一度不明確，沒有團隊主動想接手維運這塊基礎設施。

🎯 **實務啟示**

隨著 agentic coding 讓程式碼與 PR 產出量持續攀升，測試選擇與 CI 架構很可能是下一個瓶頸；與其反覆用「加機器、重啟」爭取喘息空間，不如及早評估架構能否水平擴展，把重新設計的成本提前攤提。

🔗 **來源**
- 標題：Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic
- 作者／機構：Sachin Malhotra／Anthropic
- 連結：https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic

#Anthropic #ClaudeCode #CI #AgenticCoding #SoftwareEngineering #TestAutomation #DevOps #ScalableSystems #SDLC #EngineeringCulture
