---
title: Agentic Search. More accurate and efficient results from your AI systems.
source: Mistral AI
url: https://mistral.ai/news/agentic-search/
model: claude-code/sonnet
generated_at: '2026-08-21T06:25:46.278502'
pinned: true
---

📌 【Mistral AI 新產品】財報問答正確率從 26.7% 衝到 86%：Agentic Search 怎麼做到的

TL;DR：Mistral 推出 Agentic Search，讓模型能像操作檔案系統一樣搜尋、開啟、導覽並驗證文件內容，準確率與延遲雙雙改善。

問模型「1953 年每個月的國防支出加總是多少」，傳統一次性 RAG 只翻到半年資料就直接作答；Mistral 的新方案則會自己發現資料不完整，換個搜尋詞再找一次，直到真的找到完整的 12 個月表格才回答。

🤔 **傳統 RAG 卡在哪裡**

Mistral 在部落格中指出，傳統的一次性（one-shot）RAG 是先檢索一批固定的文字區塊，再讓模型基於這些區塊一次性作答。這在答案剛好落在檢索結果前幾名時沒問題，但一旦要跨文件比對、追蹤參照、或是答案藏在特定表格、註腳、條款裡，就容易失準。Mistral 歸納出三個核心限制：檢索與推理脫節（模型只能用拿到的區塊回答，無法主動要求換一批）、卡在區塊層級（找到對的文件卻打不開、導覽不到對的表格）、以及無法迭代（很多問題需要多輪搜尋、比對、追蹤才能湊齊答案，一次性 RAG 沒有「再試一次」的機制）。

🧩 **把搜尋變成五個工具的迴圈**

Agentic Search 建立在既有的 Mistral Search Toolkit 索引之上，讓模型可以呼叫五個類似檔案系統操作的工具：search（在既有索引中找相關文件）、open（開啟特定文件）、navigate（移動到文件中的頁面、段落或區域）、read（讀取該位置的內容）、grep（在已開啟的文件內找特定字串）。這代表模型不再只能從最初檢索到的 top-k 結果裡作答，而是可以先檢視找到的東西、視需要重新搜尋、開啟相關文件、導覽到特定段落，讀完內容後才回答。索引負責找出可能的來源，Agentic Search 則負責決定要在這些來源裡、以及跨來源之間，實際檢視哪些內容。Mistral 也強調這些工具不需要額外微調或針對特定模型訓練，代表隨著底層模型的推理與工具使用能力進步，檢索品質也會跟著提升，而不會被固定的切塊（chunking）策略綁死。

📊 **在 FinanceBench 上正確率 3 倍成長**

Mistral 公布的基準測試數據如下：

| 測試項目 | 一次性 RAG | Agentic Search |
|---|---|---|
| FinanceBench（財報文件問答） | 26.7% | 86%（約 3 倍） |
| OfficeQA Pro（多表格、多文件問答） | 6.3% | 51.9%（+45.6 個百分點） |
| p90 延遲 | — | 最多降低 39.6% |
| Token 消耗 | — | 最多減少約三分之一 |

以文章中舉的 1953 年國防支出範例來看，一次性 RAG 只呼叫一次 search，只找到上半年資料就作答；Agentic Search 則多跑了一輪 search 加上一次 read，找到完整的 12 個月數據表格後才給出加總結果 44,463（單位百萬美元）。

⚠️ **不是所有情境都需要**

Mistral 也明確指出 Agentic Search 的適用邊界。適合用在：長文件（財報、合約、規範手冊、報告等答案可能藏在特定頁面、表格、條款或註腳的場景）、需要跨多份文件比對驗證的問題、答案必須可追溯到具體出處的場景（例如財務數字、法律條款），以及以表格與結構化內容為主、意義depend on 行列與版面配置的文件。相對地，如果只是簡單的直接查找（答案通常就在前幾個檢索結果裡）、或是大量高頻的關鍵字／語意搜尋且不需要推理導覽，傳統的索引檢索仍是更合適的起點。

🎯 **實務啟示**

對正在處理企業內部長文件（財報、合約、法規）的 RAG 系統來說，Agentic Search 提供的思路是：與其不斷優化切塊策略，不如把「搜尋」本身變成模型可以多輪操作的工具鏈。這類架構特別適合資料必須留在隔離環境（雲端或地端自建）、且答案必須可回溯到明確出處的企業場景。

🔗 **來源**
- 標題：Agentic Search. More accurate and efficient results from your AI systems.
- 作者／機構：Mistral AI
- 連結：https://mistral.ai/news/agentic-search/

#MistralAI #AgenticSearch #RAG #LLM #EnterpriseAI #InformationRetrieval #AIAgents #FinanceBench #DocumentAI #AITools
