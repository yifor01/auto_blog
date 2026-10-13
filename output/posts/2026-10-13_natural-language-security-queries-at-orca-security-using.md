---
title: Natural language security queries at Orca Security using Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/natural-language-security-queries-at-orca-security-using-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-13T22:06:43.130045'
score: 88
---

📌 查詢成本砍 90%:Orca Security 用 Bedrock 重構 NL 轉查詢 pipeline

TL;DR:把整套雲端安全 schema 塞進單一 prompt 行不通,Orca 用九階段 pipeline 把成本、延遲雙雙砍掉九成。

把自然語言問題丟給 LLM,讓它直接生出一條能跑的資料庫查詢,聽起來像是 RAG 的入門範例。但當你的 schema 有超過 900 種模型、18 種運算子、層層巢狀的父子關係時,「把全部塞進 prompt 裡」這個直覺做法,會在生產環境中原形畢露。

🤔 **分析師不該被查詢語言綁住**

Orca Security 提供涵蓋雲端、程式碼與 AI 的情境式安全服務,其 Sonar 查詢系統讓使用者搜尋、過濾並探索整個資料圖譜,涵蓋超過 900 種雲端基礎設施與應用程式模型(例如一個 Amazon EC2 執行個體或一個 Amazon S3 儲存貯體)。問題是,要寫出一條有效的 Sonar 查詢,使用者得組出精確的 JSON 物件,從 18 種運算子中選擇,還要在不同雲端供應商之間穿梭於父子層級關係——這需要對 Sonar schema 有深入了解,安全分析師不該被這道門檻擋住。

🧩 **第一版踩到的三個坑**

Orca 最初的概念驗證,是把完整的 Sonar schema(900 多個模型定義、所有關係類型、大量範例查詢)全部塞進單一 prompt,交給當時最大的可用模型處理。輸出品質不差,設計夥伴與內部使用者反應正面,但擴大到生產規模後,三個問題浮現:每個 workload 大約消耗 200 萬個輸入 token,成本居高不下;端到端回應時間約 60 秒,延遲過高;面對巢狀關係與多條件的複雜查詢時,準確度有限,常需要額外修正。

🧩 **九階段 pipeline:每一步配對最合適的模型**

Orca 與 AWS 合作,將解決方案重新設計為結合 Retrieval Augmented Generation(RAG)與 schema-aware 查詢構造的混合架構,取名 Discovery AI,透過九階段 pipeline 把自然語言問題轉換成合法的 Discovery 篩選條件,每一階段都配對最適合的 Amazon Bedrock 模型。選擇 Bedrock 的原因在於它用單一 API 提供多模型存取,讓團隊不必為每個模型各自維護整合介面;同時 Bedrock 透過 AWS IAM、VPC 端點與 AWS CloudTrail 繼承既有的 AWS 治理控制,滿足 Orca 的安全要求;模型無關(model-agnostic)的架構也讓團隊能隨新模型推出直接替換,無需重新設計整條 pipeline。

其中一個關鍵環節是 **Model Selector**,運行在 Anthropic Claude Haiku 4.5 上,處理的是每個模型的精簡語意化表示(名稱、用途、關鍵欄位與關鍵關係),針對使用者的問題,只回傳 Generator 真正需要的模型,Generator 才會拿到那些被選中模型及其關聯關係的完整 schema 細節——這直接繞開了「900 多個 schema 塞進每個 prompt」這個不可行的做法。

另一個決定性環節是**範例檢索策略**的選擇。團隊比較了多種做法:純粹的 top-K 語意搜尋(基於 Amazon Titan embeddings)速度快,但容易回傳近乎重複的範例,讓 Generator 缺乏多樣性;Maximal Marginal Relevance(MMR)提升了多樣性,卻在最佳候選本身就是正確答案時反而犧牲相關性。最終勝出的做法是:先用 Titan embeddings 做 top-20 近鄰檢索,再用 Cohere Rerank 3.5 重新排序並篩到前五名,在不犧牲覆蓋率或精準度的情況下,給 Generator 一組小而多樣、高度相關的範例集。

📊 **成本降 90%,延遲降 75%**

部署到生產環境後,Discovery AI 相較初始基準版本,在成本、延遲與準確度三方面全面提升:查詢成本降低 90%,輸入 token 用量降低 93%,延遲降低 75%。目前系統每天處理數千筆查詢,回應時間約 15 秒。

💡 **讓系統持續變聰明的回饋迴路**

Orca 建置了持續評估框架,結合精心策劃的評估資料集、LLM-as-judge 評分層(評估正確性、完整性與語意等價性),以及按切片(slice)拆解的量測方法,讓每一次 prompt、模型、檢索參數或範例的變更,都先經過這套框架驗證才上線。團隊也打造了內部標註工具,讓產品經理、支援工程師與安全研究人員能標記查詢、修正輸出,並一鍵把修正推入範例庫;系統還會自動收集信心分數偏低的生產查詢,派送給對應領域專家每日標註,下一次 pipeline 執行時,Cohere Rerank 3.5 就能檢索到新範例,準確度隨即提升,不需要重新部署。Orca Security AI 總監 Or Gabay 表示:「這套標註介面是我們為長期品質所做的最重要投資,它讓 Discovery AI 從一次性部署,變成一個領域專家能在日常工作流程中持續改進的活系統。」

🎯 **實務啟示**

這個案例給正在做 NL-to-query 或 NL-to-API 系統的團隊一個明確的提醒:schema 龐大時,「全塞進 prompt」是最直覺但最貴、最慢的做法。先用一個輕量模型做 schema 篩選,再讓重模型只處理縮小後的子集,搭配檢索加重排序而非單一語意搜尋,往往是把成本與延遲壓低一個數量級的關鍵路徑。同樣重要的是,把標註與回饋迴路設計進系統架構裡,而不是當成事後補救。

🔗 **來源**
- 標題:Natural language security queries at Orca Security using Amazon Bedrock
- 作者/機構:Deniz Yilmaz, AWS Machine Learning Blog(含 Orca Security Or Gabay 引言)
- 連結:https://aws.amazon.com/blogs/machine-learning/natural-language-security-queries-at-orca-security-using-amazon-bedrock/

#AmazonBedrock #RAG #NaturalLanguageQuery #CloudSecurity #LLMOps #ClaudeHaiku #CohereRerank #AWSML #SecurityAutomation #OrcaSecurity
