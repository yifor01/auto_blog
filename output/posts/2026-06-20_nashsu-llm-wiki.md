---
title: nashsu/llm_wiki
source: GitHub Trending
url: https://github.com/nashsu/llm_wiki
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:38:00.510128'
---

📌 **自動化知識庫 llm_wiki：讓 LLM 幫你讀文件並構建結構化 Wiki**

TL;DR：一個能自動讀取文件、生成結構化 Wiki 並同步更新的個人知識庫管理工具。

面對大量雜亂的 PDF 或文件，手動整理 Wiki 往往比閱讀本身更耗時。如果能讓 LLM 扮演「知識管理員」，自動分析內容、建立索引並維護結構，是否能真正解決資訊過載的問題？

🧩 **從文件到結構化知識的自動化流程**

llm_wiki 並非簡單的 RAG 聊天機器人，而是一個能「自我構建」的知識庫。其核心設計在於將非結構化文件轉化為具備可追溯性的 Wiki 頁面：

- **兩階段 Chain-of-Thought 導入**：LLM 先進行分析，隨後才生成 Wiki 頁面，確保內容具備來源可追溯性（Source Traceability），並透過增量快取（Incremental Cache）提升處理效率。
- **多模態影像處理**：能從 PDF 中提取嵌入影像，利用 Vision LLM 生成事實性說明，並在搜尋結果中提供 Lightbox 預覽與跳轉回原文件的功能。
- **彈性 PDF 解析**：預設使用本地解析器，但可選擇整合 MinerU 雲端解析，以處理包含表格、公式或複雜佈局的艱難文件。
- **自動同步機制**：支援遞迴導入資料夾並保留目錄結構，且具備自動監控功能（Auto-Watch），當原始文件變動時，會同步更新或清理對應的 Wiki 內容。

💡 **結合知識圖譜與向量搜尋的雙路檢索**

為了避免單純向量搜尋（Vector Search）可能遺失的結構化關聯，該專案引入了圖論分析來挖掘知識間的深層聯繫：

- **四信號知識圖譜 (4-Signal Knowledge Graph)**：透過直接連結、來源重疊、Adamic-Adar 演算法以及類型親和力（Type Affinity）來計算關聯度。
- **社群偵測與洞察**：利用 Louvain 演算法自動發現知識集群（Cluster），並透過凝聚力評分（Cohesion Scoring）找出意外的連結或知識缺口。
- **混合檢索機制**：在上述圖譜基礎上，可選擇開啟基於 LanceDB 的向量語義搜尋，並支援任何相容 OpenAI 的端點。

🛠️ **工程實作細節**

- **持久化導入隊列**：採用序列化處理，具備崩潰恢復、取消、重試以及進度視覺化功能，確保大量文件導入時的穩定性。
- **上下文感知**：導入資料夾時，會將資料夾路徑作為 LLM 分類時的提示（Hint），讓生成的 Wiki 結構更符合原有的邏輯。

🎯 **實務啟示**

對於需要管理大量技術文檔或研究資料的工程師來說，llm_wiki 提供了一種從「被動搜尋」轉向「主動結構化」的思路。比起單純的問答，將 LLM 用於「建立索引」與「發現知識缺口」能讓知識管理更具系統性。

🔗 **來源**
- 標題：nashsu/llm_wiki
- 作者／機構：nashsu
- 連結：https://github.com/nashsu/llm_wiki

#LLM #KnowledgeGraph #Wiki #RAG #Multimodal #LanceDB #MinerU #KnowledgeManagement #OpenSource #InformationRetrieval
