---
title: Announcing the Agentic Catalog Experience in Amazon Quick
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/announcing-the-agentic-catalog-experience-in-amazon-quick/
model: tencent/hy3:free
generated_at: '2026-08-01T08:23:44.068995'
score: 55
---

📌 【AWS 最新功能】解決 Text2SQL 的最後一哩路：Amazon Quick 推出 Agentic Catalog 體驗

TL;DR：透過 Quick Agent 繼承上游 Catalog 的語義資訊，讓 AI 驅動的分析不再只是「猜」資料。

當企業邁向 AI 驅動的數據分析時，Text2SQL（將自然語言轉為 SQL）的回答品質，完全取決於背後的業務語義（Business Context）。如果資料表與欄位的定義、關聯性沒有被正確傳遞給 AI，生成出的結果將難以被業務決策者信任。

🤔 **解決「孤島式」元數據帶來的最後一哩路挑戰**

企業數據團隊通常已經在 AWS Glue Data Catalog、Databricks Unity Catalog 或 dbt 等平臺上，投入大量心力定義好資料表描述、欄位語義、主外鍵關係以及指標定義。

然而，當這些定義要轉換為使用者（如銷售經理或財務主管）在 Amazon Quick 中使用的「生產級 AI 回答」時，存在著巨大的落差：
- **資訊斷層**：豐富的 Catalog 元數據無法直接流向 AI 產品。
- **配置繁瑣**：數據策劃者（Data Curators）需要手動設定大量的資料集與主題，耗時數週。
- **信任問題**：缺乏語義支撐的 AI 回答，難以達到確定性（Deterministic）的分析結果。

🧩 **Quick Agent：透過對話實現自動化語義繼承**

為了打破這個僵局，AWS 宣佈推出 **Agentic Catalog Experience**。其核心是 **Quick Agent**，這是一個專為目錄（Catalog）情境設計的 AI 代理，負責發現、建立與繼承任務。

其運作流程如下：
1. **自然語言探索**：策劃者無需手動捲動數千個資料表，只需對 Quick Agent 說：「我需要用於季度營收報告與成本分析的資料表。」
2. **自動搜尋與評估**：Agent 會根據業務描述、標籤（Tags）、品質評分（Quality Scores）及詞彙表（Glossary terms）進行搜尋，並向用戶建議最相關的資料表與關係。
3. **一鍵生成資料集與主題**：確認後，Agent 會自動建立「Catalog-Generated Datasets」與「Topics」，並直接繼承上游 Catalog 的語義。

📊 **設計原則：繼承而非取代**

為了保持資料集的精簡與生產就緒（Production-ready），目前的設計採取了精準繼承策略：
- **語義繼承範圍**：目前僅針對「資料表與欄位定義」進行繼承，以避免雜訊。
- **保持單一真理來源**：預設使用 Direct Query 模式，確保上游 Catalog 仍是資料的唯一真理來源。
- **視覺化標記**：繼承了語義的資料集會帶有「Semantics Inherited」標籤，且元數據為唯讀，可透過同步按鈕手動更新以保持一致。
- **預配置關聯**：Agent 能偵測資料表間的關係，並預先配置好 Star Schema（星狀模型）的 Join 關係。

💡 **對業務使用者的實際價值**

當銷售經理詢問：「Q4 各區域的銷售額是多少？」
背後的運作流程是：
- 策劃者只需定義一次上下文邊界（Context Boundary）。
- Quick Agent 將繼承的語義餵入 Amazon Quick 的語義儲存區（Semantic Store）。
- AI 透過統一的上下文進行重新排序（Re-ranking），提供精準且有依據的回答。

🎯 **實務啟示**

對於數據工程師而言，這代表了從「手動維護資料集」轉向「定義語義邊界」的範式轉移。透過將 AWS Glue Data Catalog 與 Athena 結合使用，開發者可以實現「元數據由 Glue 提供，查詢由 Athena 執行」的自動化流程，大幅縮短從連接目錄到產出第一個業務問題的時間。

🔗 **來源**
- 標題：Announcing the Agentic Catalog Experience in Amazon Quick
- 作者／機構：Srikanth Baheti @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/announcing-the-agentic-catalog-experience-in-amazon-quick/

#AWS #AmazonQuick #GenerativeAI #DataCatalog #AWSGlue #DataEngineering #Text2SQL #MachineLearning #DataGovernance #AIAnalytics
