---
title: Reduce RAG costs on Amazon Bedrock with query-aware compression
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/
model: claude-code/sonnet
generated_at: '2026-08-22T06:12:56.087577'
score: 98
---

📌 幫 RAG 瘦身:用小模型過濾,大模型的 token 帳單少三成

TL;DR:在檢索與生成之間插入一次小模型過濾,Amazon Bedrock 上的 RAG 應用可省下約三成成本,答案品質幾乎不變。

RAG 系統的檢索設計通常追求高召回率,寧可多抓一些可能相關的內容片段,也不想漏掉關鍵資訊。但這個設計選擇有代價:送進主力模型的 input token 數量,往往是整個 RAG 應用中最主要的成本來源之一。

🤔 高召回率的另一面,是昂貴的 input token 帳單

以典型的技術文件或法律類 RAG 工作負載來說,檢索 5 到 20 個片段、加上一般的片段大小,每次查詢送進模型的 token 數就可能達到數千個。Amazon Bedrock 的開放、可組合架構,讓開發者能在檢索之後插入自訂的後處理步驟,先精煉內容,再交給主力模型作答。

🧩 先讓小模型抓重點,再讓大模型作答

這個模式的做法是:檢索完成、生成最終答案之前,先用 Amazon Bedrock 上一個較小、成本較低的模型,依照使用者的查詢過濾檢索到的片段,主力模型接著只根據過濾後的內容作答。文章示範中使用 Claude Haiku 作為壓縮模型,但這個模式也適用於同一模型家族內其他大小模型的組合。整個流程中,壓縮呼叫與主力模型的回答呼叫都在同一個 AWS Lambda 函式內完成,上游由檢索器（例如以 Amazon OpenSearch Serverless 為後端的 Amazon Bedrock 知識庫）負責將查詢向量化並回傳前 k 個片段。

壓縮提示詞是這個實作中最關鍵的部分:它必須指示小模型「擷取原文片段」而非「摘要」,禁止改寫與重述,並保留足夠的上下文,確保後續引用來源時仍然準確。壓縮呼叫以溫度 0.0 執行,讓擷取結果保持確定性,使小模型能逐字複製原文片段。整體經濟效益取決於兩個因素:小模型與主力模型之間的單位 token 價格比,以及小模型達成的壓縮比。

📊 省下三到四成成本,幻覺率也跟著降

團隊在一個語料庫、一個領域、一組查詢分布上做了實測評估（結果會因不同語料與查詢而異）。壓縮模式達成 33% 的成本節省,或者說送進主力模型的 token 減少了 8.6 倍;加上 Rerank API 之後,成本節省提升到 36%,token 減少 10.1 倍。在四個答案品質維度的 LLM 評審評分（1 到 5 分）中,正確性與基準相比差異在 0.07 以內,完整性與引用準確度略微下降,簡潔度則略微提升。幻覺率方面,基準做法為 51%,壓縮模式降到 44%,Rerank 加壓縮進一步降到 38%。團隊也比較了一般查詢與困難查詢兩種集合:成本節省在一般查詢集合可達 37%（Rerank 加壓縮為 40%）,但在困難查詢集合上分別降到 26% 與 30%。

⚠️ 三件事要在採用前想清楚

第一是延遲:多了一次小模型呼叫,雖然 Claude Haiku 針對速度做了最佳化,而且主力模型處理的內容變少,部分時間可以在回答呼叫時補回來,但淨影響取決於主力模型原本在多大程度上受限於運算量,對於次秒級的即時對話場景,需要用自己的上下文大小實測延遲。第二是品質權衡:完整性與引用準確度會略微下降,是否可接受取決於應用場景。第三是這些數據都來自單一語料庫與單一查詢分布,換成自己的文件與問題類型,結果會不同。

🎯 可以疊加其他 Bedrock 能力一起省

這個模式可以和既有的 Amazon Bedrock 能力疊加使用,例如 prompt caching、Amazon Bedrock Intelligent Prompt Routing,以及 Rerank API,取得更多成本節省的複合效果。在導入之前,建議先用自己的語料庫與查詢跑一次類似的評估,同時盤點小模型與主力模型的價格比與實際壓縮比,確認經濟效益是否成立。

🔗 來源
- 標題：Reduce RAG costs on Amazon Bedrock with query-aware compression
- 作者／機構：Aakanksha Veesam, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/

#AmazonBedrock #RAG #CostOptimization #ClaudeHaiku #LLM #PromptEngineering #AIInfrastructure #AWS #TokenEfficiency #GenerativeAI
