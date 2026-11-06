---
title: Taxonomy of agentic primitives in Amazon Quick
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-agentic-primitives-in-amazon-quick/
model: claude-code/sonnet
generated_at: '2026-11-06T22:32:54.338762'
score: 74
---

📌 Trigger、Agent、Capability：Amazon Quick的智能體三元分類法

TL;DR：用When/What/Who/How四個問題，統一定義agent系統的核心元件。

「幫我監控Slack頻道、每天寄一份摘要給我」——這句話背後藏著一個問題：這是要建一個新agent、排一個排程指令，還是寫一個workflow？沒有共同詞彙，這些問題會混成一團，連產品團隊自己都答不清楚。

🤔 **同一組概念，被用不同名字重複發明**

Amazon Quick團隊打造agent系統的過程中，agent的能力從回答問題演進到真正採取行動：排會議、做研究、生成報告。隨著系統演進，同一組概念不斷用不同名字被重複發明：一個執行工作的actor、一個觸發工作的signal、一套打包好的流程、一個把經驗延續下去的記憶。這種重複不只發生在內部工程，也滲透進產品設計，最終讓使用者面對一個本該簡單卻變得混亂的選擇。

🧩 **四個問題拆解agentic work**

團隊收斂出的分類法，把agentic work拆解成四個問題：

Trigger承載When與What：Trigger是啟動工作的機制，同時也帶著任務指示，一則人類訊息既是啟動的瞬間，也是要做什麼的描述。觸發的類型會影響執行方式：排程型的背景任務傾向保守（不確定時什麼都不做），人類發起的任務則傾向積極回應（不確定時主動提問而非停住）。

Agent承載Who：Agent被定義為「一個持續存在、會學習的actor」，是任何一次執行背後的「Who」，也是學習累積的錨點。兩個agent即便收到相同輸入也可能有不同表現，因為它們承載不同的instructions、capabilities與歷史。底層LLM只是可替換的模型參數，對話歷史是每個session的狀態，trigger屬於平臺，這些都是agent之外的東西（extrinsic）。這個定義也帶來一個結論：使用者說「我想要一個agent監控我的Slack、每天早上寄摘要」，通常不是要建一個新agent或workflow，而是為既有agent加一個trigger。這個框架讓chat、排程與「自主」agent合併成同一個actor：可以跟它聊天、幫它排程，它也能協調並檢視自己過去的工作。

Capability承載How：橫跨一個光譜，從完全agentic到完全deterministic，本質上是一種「信心合約」——agent保留多少自由度，相對使用者事先固定多少規則：
- Tools：帶typed schema的原子操作，例如寄一封信、查一個資料庫、讀一個檔案。無論是本地函式、MCP server，還是另一個agent，呼叫者看到的介面都一樣：name、description、parameters、result。
- Skills：結構化的指引，留有判斷空間，把instructions與資源（templates、scripts、examples）打包成一種做法的描述而非死板的步驟。它們透過progressive disclosure載入，agent一開始只看到名稱與簡短描述，用到時才讀入完整instructions，因此一個skill可以包含任意深度的專業知識卻不必付出固定成本。
- Workflows：deterministic的協調機制，宣告好的步驟、控制流程、分支與錯誤處理依固定順序執行，決策邏輯寫在程式碼而非模型推論中，例如一套採購簽核流程：預算檢查、主管簽核、再到財務，每一步都有紀錄。步驟順序固定，但每一步裡的判斷仍是agent的。

💡 **Skills與Workflows不會被更強的模型淘汰**

文章特別指出，即便模型能力持續進步，skills與workflows不會因此變得多餘，因為它們的價值獨立於模型能力之外：skills是捕捉、版本化與分享組織內部專業知識的單位；workflows提供可審計性、逐步可見性與跨服務的確定性協調。兩者也不是固定不變的，一個被充分理解的skill可以收斂成workflow（crystallization），而一個不斷碰到edge case的workflow也可能鬆動回skill（dissolution），這個轉換透過Quick的持續學習框架完成。回到「監控Slack、每天摘要」這個例子，同一個請求可以用三種方式滿足，差別在於「信心合約」：信任agent的使用者想要最自主的做法，曾被agent搞砸過的使用者想要較保守的做法，跑合規敏感流程的使用者則需要最嚴格把控的做法。隨著學習累積，一句話起步的任務（例如「幫我檢查信箱有沒有緊急事項」）會逐漸累積出有效查詢方式、偏好的格式、該留意哪些寄件人，第十次執行時明顯比第一次更好，而這些都不需要人工手動編碼。

⚠️ **目前只是理念層的分類法**

素材本身聚焦在概念分類與設計理念，並未提供實作程式碼或量化評估，這套taxonomy目前僅說明Amazon Quick內部收斂出的架構語言，具體技術落地細節留待系列後續文章（agentic operating system、背景學習、主動推播等）說明。

🎯 **實務啟示**

對正在設計多agent產品或平臺的工程團隊，這套「When/What/Who/How」四問分類法提供了一個低成本的溝通工具：先問清楚一個使用者請求到底該落在trigger、agent本身，還是capability（tool／skill／workflow）的哪一層，可以避免把同一組邏輯用不同名字重複實作，也能讓「要多自主」這個問題變得可被設計者明確決定，而不是隱性堆疊在程式碼裡。

🔗 **來源**
- 標題：Taxonomy of agentic primitives in Amazon Quick
- 作者／機構：Thomas Delteil, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/taxonomy-of-agentic-primitives-in-amazon-quick/

#AgenticAI #AmazonQuick #AWS #AIAgents #LLM #AgentArchitecture #MachineLearning #WorkflowAutomation #MCP #AIEngineering
