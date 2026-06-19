---
title: VectifyAI/OpenKB
source: GitHub Trending
url: https://github.com/VectifyAI/OpenKB
score: 101
model: google/gemma-4-31b-it:free
generated_at: '2026-06-19T20:03:22.397899'
---

📌 **【VectifyAI】OpenKB：捨棄向量資料庫，用 LLM 自動構建結構化知識維基**

TL;DR：將原始文件編譯為互連的 Wiki 式知識庫，透過 Reasoning-based 檢索取代傳統 RAG。

大多數 RAG 系統在每次查詢時都像在「從零開始」搜尋碎片資訊，導致知識無法累積且缺乏結構。如果我們能像人類建立維基百科一樣，先將知識編譯成結構化、可互連的知識庫，會發生什麼事？

🤔 **傳統 RAG 的侷限：缺乏知識累積**

傳統 RAG 的運作方式是在每次查詢時重新發現知識，這意味著系統沒有記憶，資訊無法隨時間複合成長。OpenKB 則採取截然不同的路徑：將原始文件預先編譯成一個持續更新且持久化的 Wiki，讓知識在編譯階段就完成合成與交叉引用，而非在查詢時才即時推導。

🧩 **核心架構：從原始文件到結構化 Wiki**

OpenKB 的設計理念受 Andrej Karpathy 的概念啟發，將系統分為兩個層級：

1. **Wiki 基礎層**：利用 LLM 將原始文件編譯成包含摘要、概念頁面（Concept Pages）與交叉引用的結構化知識庫，並自動維護其時效性。
2. **生成層**：包含查詢（Query）、聊天（Chat）與 Skill Factory，將維基中的結構化知識轉化為最終輸出。

其技術核心在於使用 PageIndex 的「無向量（Vectorless）」且基於推理的檢索機制，能有效處理長文件並維持上下文感知能力。

📊 **關鍵功能與技術特點**

- **無向量檢索（No Vector DB）**：透過 PageIndex 的樹狀索引（Tree Indexing）處理長且複雜的文件，不再依賴傳統的向量資料庫。
- **原生多模態支援**：不僅能處理文字，還能檢索並理解圖表、表格與圖片。
- **廣泛的文件格式支援**：支援 PDF, Word, Markdown, PowerPoint, HTML, Excel, CSV, 純文字及 URL 等多種格式。
- **知識合成與衝突偵測**：在編譯過程中，系統會自動建立交叉引用，並能標記出資訊之間的矛盾之處。

🎯 **實務啟示**

對於需要處理大量長文件且對知識結構有高度要求的工程師，OpenKB 提供了一種從「即時檢索」轉向「先編譯後檢索」的新思路。這種方法能減少重複推導的成本，並讓 LLM 能夠在一個具有結構的知識體系中進行推理，而非在碎片化的 Chunk 中尋找答案。

🔗 **來源**
- 標題：OpenKB
- 作者／機構：VectifyAI
- 連結：https://github.com/VectifyAI/OpenKB

#AI #OpenSource #LLM #RAG #KnowledgeBase #Vectorless #MultiModality #PageIndex #KnowledgeManagement #VectifyAI
