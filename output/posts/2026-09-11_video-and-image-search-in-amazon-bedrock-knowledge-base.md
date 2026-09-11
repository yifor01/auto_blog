---
title: Video and image search in Amazon Bedrock Knowledge Base using Marengo 3.0
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/video-and-image-search-in-amazon-bedrock-knowledge-base-using-marengo-3-0/
model: claude-code/sonnet
generated_at: '2026-09-11T19:53:51.551699'
score: 84
---

📌 AWS Bedrock 知識庫整合 Marengo 3.0，影片也能語意搜尋

TL;DR：Amazon Bedrock Knowledge Bases 正式支援 TwelveLabs Marengo Embed 3.0，讓影片、音訊、圖片可用自然語言直接檢索。

「幫我找出下半場那顆點球」——如果你的素材庫是幾百小時的比賽錄影，這句話過去得靠人工翻帶才能實現。現在 AWS 把這件事變成一個 S3 上傳加一次 Sync 就能完成的流程。

🤔 **影片搜尋的老問題：管線太複雜**

媒體、體育數據分析、教育、安全監控、零售等產業都有同樣的痛點：影片和媒體資產內容豐富，卻幾乎無法用語意檢索。過去要做到這件事，得自行串接語音轉文字、影格擷取、embedding 模型、向量資料庫與時間軸同步邏輯，是一條相當長的客製化管線。

🧩 **Managed Knowledge Bases 怎麼接住 Marengo 3.0**

Amazon Bedrock Knowledge Bases 是全代管的 RAG（Retrieval Augmented Generation）服務，涵蓋儲存、擷取、embedding、重新排序（re-ranking）與檢索。它原生支援 MP4、MOV 影片檔、JPEG、PNG 圖片，並可透過 Amazon S3、SharePoint、Confluence 等連接器匯入資料。

Marengo Embed 3.0 是一個多模態 embedding 模型，能把影片、音訊、圖片與文字聯合編碼進一個 512 維、體積精簡的向量空間。當它成為 Knowledge Bases 的可選 embedding 模型後，Managed Knowledge Bases（Managed MKB）會自動完成分段、影格取樣與逐字稿轉錄，並把視覺、文字、語音、音訊訊號統一成一組向量表示，整條管線不再需要工程團隊手動拼接。

實際操作流程大致是：

1. 把影片檔上傳到 S3 bucket，不需要任何前處理。
2. 在 Bedrock 主控臺建立 Managed KB，於 Additional Configuration 中將 Embeddings model 從預設的 Amazon Titan Text 改選為 TwelveLabs Marengo Embed 3.0。
3. 設定 Data source 為 Amazon S3，指向存放影片的 bucket。
4. 在 Advanced configurations 的 Audio/video segmentation 設定音訊與影片的分段長度，預設皆為 4 秒。
5. 建立 KB 後執行 Sync，Managed MKB 會自動擷取影格、轉錄音訊、為每個片段產生 Marengo Embed 3.0 embedding 並寫入索引。

📊 **一句自然語言查詢，回傳帶時間戳的片段**

文中以 2022 世界盃決賽的 10 分鐘片段作示範，輸入查詢「show me the penalty kicks from this soccer match」後，KB 會回傳排序過的結果，並附上每個片段的起訖時間、來源 URI 與 embedding 類型等 metadata，方便直接擷取對應片段。開發者也可以在 KB 建立完成後，透過 Amazon Bedrock 的 Retrieve API 呼叫下游應用，或將其作為 Amazon Bedrock AgentCore 中 Bedrock Gateway 的目標。

⚠️ **目前僅限兩個 Region，計費按標準模型呼叫費率**

Marengo 3.0 的 Managed Knowledge Bases 目前僅在 US East（N. Virginia，us-east-1）與 US West（N. California，us-west-1）提供。費用模式是「用多少付多少」：儲存與檢索照標準收費，Marengo Embed 3.0 的 embedding 產生則按 Amazon Bedrock 標準模型呼叫費率計費。

🎯 **實務啟示**

對已經在用 Bedrock Knowledge Bases 做文字 RAG 的團隊，這個更新的意義在於「不用換架構」：只要把資料來源指向存放影片的 S3 bucket、切換 embedding 模型，就能把既有的檢索應用擴充到多模態內容。對於還在自建影片搜尋管線的團隊，這是評估「代管 vs. 自建」成本的一個具體參考點——尤其是轉錄、分段、向量化這幾個原本最耗工的環節，現在都內建在服務裡。

🔗 **來源**
- 標題：Video and image search in Amazon Bedrock Knowledge Base using Marengo 3.0
- 作者／機構：Eric Kim, AWS ML Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/video-and-image-search-in-amazon-bedrock-knowledge-base-using-marengo-3-0/

#AWS #AmazonBedrock #TwelveLabs #Marengo #RAG #MultimodalAI #VideoSearch #KnowledgeBase #VectorSearch #GenAI
