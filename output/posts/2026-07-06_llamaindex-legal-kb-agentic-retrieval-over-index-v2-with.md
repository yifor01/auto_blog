---
title: 'LlamaIndex ‘legal-kb’: Agentic Retrieval over Index v2 with retrieve, find,
  read, and grep Tools'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/05/llamaindex-legal-kb-agentic-retrieval-over-index-v2-with-retrieve-find-read-and-grep-tools/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:25:38.820484'
---

📌 LlamaIndex 推出 legal-kb：用「檔案系統操作」實現 Agentic 檢索

TL;DR：透過將檢索模擬為檔案操作（find/grep/read），讓 Agent 能在 LlamaIndex Index v2 上進行多步驟探索。

傳統的 RAG 往往依賴單次 Embedding 搜尋（Single-shot Retrieval），但面對複雜或不斷變動的法律檔案庫，一次搜尋很難精準命中所有答案。LlamaIndex 推出的 `legal-kb` 專案提出了一種不同的模式：Retrieval Harness。

🤔 **從「單次搜尋」轉向「Agent 探索」**

`legal-kb` 並非一個函式庫，而是一個基於 TanStack Start 的完整 Web 應用程式。其核心理念是將檢索過程轉化為 Agent 的探索過程。Agent 不再僅僅是「搜尋 $\rightarrow$ 回答」，而是像工程師操作檔案系統一樣，透過一系列工具在知識庫中爬行（crawl）以解決任務。

🧩 **將檢索 API 封裝成檔案系統工具**

在 `src/lib/agent.ts` 中，Agent 被賦予了四個對應到 Index v2 檢索 API 的工具，讓其能以類似檔案操作的邏輯運作：

- `findFiles`：建立檔案清單（Document Inventory）。
- `retrieve`：進行混合搜尋（Hybrid Search）以縮小範圍。
- `readFile`：讀取檔案內容以確認精確措辭。
- `grepFile`：使用正規表示式（Regex）在檔案中搜尋特定字串。

為了確保準確性，系統提示詞（System Prompt）強制規定了操作順序：Agent 必須先執行 `findFiles` 確定有哪些檔案 $\rightarrow$ 使用 `retrieve` 縮小範圍 $\rightarrow$ 最後透過 `readFile` 或 `grepFile` 確認細節後才進行引用。

📊 **自動化的資料管線與同步機制**

`legal-kb` 建立了一套持久化的資料管線，將使用者上傳的檔案與 LlamaCloud Index v2 串接：

1. **上傳流程**：檔案位元組（Bytes）被推送至 LlamaCloud 來源目錄，同時透過 Prisma 將紀錄寫入 PostgreSQL。
2. **背景索引**：系統會觸發索引同步（Index Sync），UI 會持續輪詢（Poll）狀態直到就緒。
3. **版本管理**：版本控制是以（專案, 檔名）作為範圍進行管理。

🎯 **實務啟示：將檢索工具「通用化」**

對於開發者而言，`legal-kb` 最大的價值在於其「Retrieval Harness」的設計模式。將檢索操作定義為 `find`、`grep`、`read` 等通用工具，意味著這套管線可以輕鬆地掛載到任何自定義的 Agent 中。如果你處理的是結構複雜、需要精確對齊原文的專業檔案（如法律、合約），這種「先定位、後縮小、再確認」的 Agentic 流程會比單次向量搜尋更可靠。

🔗 **來源**
- 標題：LlamaIndex ‘legal-kb’: Agentic Retrieval over Index v2 with retrieve, find, read, and grep Tools
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/07/05/llamaindex-legal-kb-agentic-retrieval-over-index-v2-with-retrieve-find-read-and-grep-tools/

#LlamaIndex #AgenticRAG #LlamaCloud #KnowledgeBase #RetrievalHarness #LLM #LegalTech #InformationRetrieval #TanStack #VectorDatabase
