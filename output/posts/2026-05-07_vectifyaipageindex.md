---
title: "VectifyAI/PageIndex"
source: GitHub Trending
url: https://github.com/VectifyAI/PageIndex
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:19:10.461303
---

📌 【GitHub Trending】不用向量資料庫，PageIndex 用「推理」重寫 RAG 規則

你還在為了解決 RAG 檢索不準的問題，不斷微調 Embedding 模型或調整 Chunk 大小嗎？最近在 GitHub Trending 上爆紅的 PageIndex，直接拋棄了向量資料庫，改用「推理」來處理長文件。這項技術在一天內拿到了 953 顆星，顯然戳中了許多工程師的痛點。

🤔 **相似度不等於相關性，傳統 RAG 的致命傷**

目前的 RAG 系統大多依賴語意相似度（Semantic Similarity）來找答案。但在專業文件（如法律、醫療、金融）中，語意相近不代表答案正確。例如，搜尋「公司違約條款」，可能會撈出一堆不相關的「合約範本」，因為它們語意相近，但缺乏針對具體情境的「相關性」。PageIndex 認為，真正的解法不是算出更準的向量，而是讓模型學會「推理」。

🧪 **受 AlphaGo 啟發，建立階層式樹狀索引**

PageIndex 提出了一種無向量（Vectorless）的架構。它不將文件切成碎塊（Chunking），而是構建一個階層式的樹狀索引（Hierarchical Tree Index）。這個設計靈感來自 AlphaGo，核心在於讓 LLM 能夠像人類專家一樣，透過「推理」在索引結構中導航，而不是盲目地計算餘弦相似度。

 **Agentic 推理：從「搜尋」轉向「思考」**

這個系統被定義為 Agentic RAG。它不僅是檢索，而是讓 LLM 具備上下文感知能力（Context-Aware），能夠在多步驟推理中判斷哪個分支包含真正的答案。這對於需要深度專業知識和多步邏輯推演的長文件分析來說，是一個極具潛力的替代方案。

💡 **擴展到百萬級文件：PageIndex File System**

光是單一文件推理還不夠，PageIndex 還推出了 File System 層。這是一個檔案級別的樹狀結構，讓推理能力可以擴展到整個語料庫，而不僅限於單一文件。這意味著它試圖解決的是企業級「海量專業文檔」的檢索難題，而不僅僅是單一 PDF 的問答。

⚠️ **實務限制與觀察**

雖然概念新穎，但作為一個新興開源專案，目前仍處於快速迭代階段。由於完全依賴 LLM 進行推理，其延遲（Latency）與成本（Cost）會是傳統向量搜尋的數倍。此外，這種「推理式檢索」在處理結構化數據或簡單事實查詢時，效率可能不如傳統的倒排索引或向量搜尋。

🎯 **工程師的實驗清單**

如果你正在評估 RAG 架構，PageIndex 值得你花時間測試：
- 專案支援自架（Self-hosted），並整合了 OpenAI Agents SDK。
- 提供 MCP (Model Context Protocol) 與 API 介面，方便串接現有系統。
- 對於「長篇專業文件」的處理，可以嘗試用它來對比 LangChain 或 LlamaIndex 的傳統 RAG 效果。

🔗 **專案連結**
📝 PageIndex: Vectorless, Reasoning-based RAG
👤 VectifyAI
🔗 GitHub: https://github.com/VectifyAI/PageIndex

你覺得「無向量 RAG」是未來的趨勢，還是只是另一種昂貴的實驗？歡迎在留言區聊聊你的看法 👇

#AI #RAG #LLM #GitHub #OpenSource #MachineLearning #VectorDB #AgenticAI
