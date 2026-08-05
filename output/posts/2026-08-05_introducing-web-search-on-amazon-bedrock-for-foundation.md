---
title: Introducing Web Search on Amazon Bedrock for foundation model grounding
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-for-foundation-model-grounding/
model: tencent/hy3:free
generated_at: '2026-08-05T08:57:05.168508'
score: 71
---

📌 【Amazon Bedrock 新功能】內建 Web Search，讓模型不再「一本正經地胡說八道」

TL;DR：Amazon Bedrock 推出內建 Web Search 工具，透過單一參數即可實現模型知識與即時網路資訊的對齊（Grounding）。

當基礎模型（Foundation Model）需要回答「上週的財報內容」、「昨天的法規變更」或是「今天早上的天氣預報」時，它需要的是訓練資料中未曾包含的即時知識。將模型與當前網路知識進行「對齊」（Grounding），能有效解決模型無法處理時效性問題，並減少幻覺（Hallucinations）現象。

🤔 **傳統做法的開發痛點**

過去，若要讓模型連結網路知識，開發者必須：
- 尋找、整合並維護第三方搜尋引擎供應商。
- 處理額外的外部 API 調度與管理。
- 進行複雜的第三方供應商安全性審核。
- 面臨數據駐留（Data Residency）與營運成本的風險。

🧩 **Amazon Bedrock Web Search 的設計理念**

Amazon Bedrock 將 Web Search 轉化為伺服器端（Server-side）的內建工具，讓對齊過程成為原生能力，主要具備以下特點：

- **多源對齊機制**：結合了 Amazon 營運、持續更新的數十億筆文件索引，以及內建的知識圖譜（Knowledge Graph）。當問題涉及事實性資訊（如：某本書的作者）時，系統會優先使用知識圖譜來回答，而非單純從網頁文本中進行推論，以減少細微的事實錯誤。
- **高效率的檢索（Context-efficient retrieval）**：系統不會直接將原始網頁丟給模型，而是進行「語義片段提取」（Semantic snippet extraction），僅提取與查詢相關的段落並針對模型的 Context Window 進行最佳化，減少 Token 消耗並降低延遲。
- **單一參數啟用**：透過與 OpenAI 相容的 API 呼叫，只需在現有的 API 請求中加入單一參數即可啟用，無需定義 Function Schema，也無需建立客戶端（Client-side）的工具使用迴圈（Tool-use loop）。

📊 **運作流程：從請求到帶有引用（Citations）的回答**

當使用者發送請求時，Bedrock 在伺服器端自動完成以下步驟：
1. **識別需求**：模型判斷該問題需要即時網路知識。
2. **執行搜尋**：Bedrock 構建搜尋查詢，從索引與知識圖譜中檢索內容。
3. **注入上下文**：將相關片段、來源 URL 與標題注入模型的 Context Window。
4. **生成回應**：模型對檢索內容進行推理，並生成帶有結構化引用註解（Annotations）的回應，包含 URL 與頁面標題。

⚠️ **安全性與合規性**

對於企業級應用，安全性至關重要：
- **零數據外流（Zero data egress）**：預設情況下，Web Search 在 AWS 環境內運作，數據不會離開您的 AWS 環境。
- **完整稽核軌跡**：與 AWS CloudTrail 整合，會記錄呼叫者身份、時間戳記與動作，方便安全性團隊進行審核，但不會記錄具體的查詢文本或檢索內容以保護隱私。

🎯 **實務啟示：如何快速整合**

開發者可以透過三個步驟快速導入：
1. **配置權限**：使用現有的 AWS IAM 身份，並透過 `aws-bedrock-token-generator` 套件產出短暫（最多 12 小時）的 Bearer Token。
2. **啟用搜尋**：在 OpenAI 相容的 API 請求中，於 `tools` 陣列中加入 `web_search` 項目。
3. **讀取結果**：從回應的 `annotations` 陣列中提取 `url_citation` 物件，利用其 `start_index` 與 `end_index` 來實現行內腳註（Inline footnotes）功能。

🔗 **來源**
- 標題：Introducing Web Search on Amazon Bedrock for foundation model grounding
- 作者／機構：Anuj Jauhari @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-for-foundation-model-grounding/

#AmazonBedrock #AWS #GenerativeAI #LLM #WebSearch #Grounding #MachineLearning #AIInfrastructure #CloudComputing #DeveloperTools
