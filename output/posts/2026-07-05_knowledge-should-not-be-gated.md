---
title: Knowledge Should Not Be Gated
source: Hacker News
url: https://www.formaly.io/blog/knowledge-should-not-be-gated
score: 70
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:38:00.221040'
---

📌 知識不應被封閉：為什麼 RAG 的複雜基礎設施可能成了阻礙？

TL;DR：作者主張捨棄複雜的 RAG 管道，回歸 Markdown 形式以降低知識獲取的門檻。

過去幾年，當我們想讓 AI 系統掌握企業知識時，標準做法是建立一套複雜的基礎設施：將檔案切片 (Chunking) $\rightarrow$ 選擇 embedding 模型 $\rightarrow$ 搭建向量資料庫 $\rightarrow$ 調校檢索 $\rightarrow$ 包裝成 SDK。

🤔 **當知識被鎖在「工具鏈」之後**

這種做法導致了一個反直覺的結果：公司的知識不再是可以直接閱讀的內容，而是變成了一種必須透過 pipeline、服務與特定框架才能查詢的「物件」。作者認為，這種方式將原本不需要被封閉的知識，強行地封閉在技術工具之中。

🧩 **RAG 的歷史必然與現在的成本**

作者指出，檢索增強生成 (RAG) 在過去是合理的解決方案，因為當時面臨兩個限制：
1. 上下文視窗 (Context Windows) 太小。
2. 模型推論成本過高。

為了在有限的空間內運作，工程師必須將知識切片並僅餵入相關片段。後來的 Graph RAG 則進一步將實體與關係結構化，讓模型能進行跨連線的推理而非僅處理孤立切片。

⚠️ **轉換過程中的「知識形變」**

雖然這些技術有效，但代價是高昂的。要將知識放入 RAG 系統，必須將檔案轉換成僅有該系統才能理解的形狀（例如 embedding），這使得知識的儲存與存取變得依賴於特定的工具鏈。

🎯 **實務啟示：回歸簡單的 Markdown**

作者提出一個極其簡單的修正方案：使用 Markdown。在上下文視窗擴大、模型成本降低的今天，我們或許不再需要將知識鎖在複雜的檢索系統中，而應讓知識回歸到人類可讀且易於處理的純文字格式。

🔗 **來源**
- 標題：Knowledge Should Not Be Gated
- 作者／機構：nezhar
- 連結：https://www.formaly.io/blog/knowledge-should-not-be-gated

#AI #RAG #LLM #KnowledgeManagement #Markdown #VectorDatabase #GraphRAG #DeveloperExperience #ContextWindow #SoftwareArchitecture
