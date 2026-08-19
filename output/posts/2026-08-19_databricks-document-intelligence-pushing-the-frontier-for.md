---
title: 'Databricks Document Intelligence: pushing the frontier for complex document
  extraction'
source: Databricks
url: https://www.databricks.com/blog/databricks-document-intelligence-pushing-frontier-complex-document-extraction
model: claude-code/sonnet
generated_at: '2026-08-19T06:37:04.511097'
score: 90
---

📌 Databricks 新模式讓複雜文件抽取準確率衝上 94.7%

TL;DR：結合自訂模型與 agentic 架構，Precision Mode 在超長、超複雜文件抽取上贏過前沿模型 7 個百分點。

企業裡最有價值的資料，往往被困在最難處理的文件裡：兩千頁的技術手冊、幾千行明細的發票、超過三百個巢狀欄位的申請表。丟給一般的 LLM 單次呼叫，很快就會撞上 context 上限而漏東西。Databricks 這次沒有只換一個更強的模型，而是重新設計了整條抽取管線。

🤔 三種現有方案都會卡關的難題

Databricks 團隊在服務 Panasonic、EY-Parthenon、Intercontinental Exchange 等客戶、每週處理數百萬份文件的過程中，發現既有的 LLM 或規則式抽取方案在三類任務上特別吃力：長文件（最長可達 2,000 頁）、含大量明細列的發票、密集的多頁表格與圖表，以及需要跨頁交叉比對資訊的推理型任務，加上動輒超過 300 個深度巢狀欄位的複雜 schema。單一模型呼叫的做法在這類文件上很快就會失效，因此團隊改用更貼近工程師實務作法的基準線：chunk-and-merge，也就是把文件切塊、各自抽取再合併結果。

🧩 自訂模型加上 agentic harness 的雙層優化

Precision Mode 的做法是把兩層一起優化：一層是針對文件抽取任務客製化訓練的模型本身，另一層是包在模型外面的 agentic harness，用來處理長文件、大量輸出與需要推理的 schema。這套架構被設計成能扛住 chunk-and-merge 常見的失敗模式。

📊 9,000 份文件實測，準確率贏過 GPT-5.6 Sol 七分

Databricks 用大約 9,000 份文件做評測，涵蓋 10-K 財報、提單、技術手冊、財務文件、臨床病歷、政府專利與資助申請等類型，資料來自兩組基準測試集。他們用 GPT、Claude、Gemini 等主流模型在預設 API 設定下跑 chunk-and-merge，再與 Precision Mode 比較。結果 Precision Mode 達到 94.7% 準確率，比表現最好的前沿模型基準 GPT-5.6 Sol 高出七個百分點。尤其在長文件任務上，團隊觀察到前沿模型的 chunk-and-merge 方案會出現 chunk 逾時、輸出被截斷、最終合併結果不符 schema 等操作性失敗，而 Precision Mode 的 agentic 設計對這些狀況更穩健。

🎯 實務啟示

如果你的抽取流程正卡在長文件、超大 schema 或需要跨頁推理的任務上，這是一個值得評估的方向。Databricks 已將 Precision Mode 開放使用，只要在呼叫 ai_extract 函式時將模式設為 precision，或在 Agents 頁面的 Information Extraction UI 裡開啟 precision mode 切換即可。

🔗 來源
- 標題：Databricks Document Intelligence: pushing the frontier for complex document extraction
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/databricks-document-intelligence-pushing-frontier-complex-document-extraction

#Databricks #DocumentIntelligence #LLM #AIExtraction #AgenticAI #DataEngineering #EnterpriseAI #MachineLearning #InformationExtraction #AIAgents
