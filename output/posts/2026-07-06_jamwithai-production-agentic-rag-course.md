---
title: jamwithai/production-agentic-rag-course
source: GitHub Trending
url: https://github.com/jamwithai/production-agentic-rag-course
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:28:01.009770'
---

📌 【GitHub 趨勢】別再只用向量搜尋：從基礎關鍵字到生產級 Agentic RAG 的實作路徑

TL;DR：透過實作 arXiv 論文策展系統，學習從關鍵字搜尋、資料管線到混合檢索的生產級 RAG 構建流程。

許多 RAG 教程習慣直接跳到向量搜尋（Vector Search），但現實中的生產環境往往需要更穩健的基礎。如果忽略了搜尋基礎而採取「AI-first」的做法，系統往往難以達到企業級的穩定度。

🤔 **跳脫「AI-first」的誤區，回歸搜尋基礎**

這個由 jamwithai 推出的開源課程強調，成功的公司在構建 RAG 系統時，會先建立堅實的搜尋基礎，再用 AI 進行增強。課程的核心理念是：先精通關鍵字搜尋（Keyword Search），隨後再匯入向量技術實現混合檢索（Hybrid Retrieval），而非依賴單一的 AI 方案。

🧩 **從零構建：arXiv 論文研究助理的實作路徑**

學習者將透過構建一個能自動抓取學術論文、解析內容並回答研究問題的「arXiv Paper Curator」系統，逐步掌握以下技術棧：

- **第一階段：基礎設施佈署**
  使用 Docker、FastAPI、PostgreSQL、OpenSearch 與 Airflow 搭建完整的系統基礎環境。
- **第二階段：自動化資料管線**
  實作從 arXiv 自動抓取並解析學術論文的 Data Pipeline。
- **第三階段：生產級關鍵字搜尋**
  實作 BM25 關鍵字搜尋，包含篩選（Filtering）與相關性評分（Relevance Scoring）。
- **第四階段：進階檢索最佳化**
  匯入智慧分塊（Intelligent Chunking）並將關鍵字與語義搜尋結合，實現混合檢索。

🎯 **實務啟示**

對於 AI 工程師而言，本專案提供了一個重要的觀點：生產級 RAG 的關鍵不在於使用最新模型，而在於「搜尋基礎 $\rightarrow$ 混合檢索 $\rightarrow$ AI 增強」的工程路徑。在實作時，優先考慮 BM25 等傳統檢索機制能提供更可預測的結果，再搭配向量搜尋來補足語義理解，才是更穩健的生產級做法。

🔗 **來源**
- 標題：production-agentic-rag-course
- 作者／機構：jamwithai
- 連結：https://github.com/jamwithai/production-agentic-rag-course

#RAG #AI #OpenSource #Python #FastAPI #OpenSearch #Airflow #VectorSearch #BM25 #AIEngineering
