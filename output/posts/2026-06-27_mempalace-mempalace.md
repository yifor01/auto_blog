---
title: MemPalace/mempalace
source: GitHub Trending
url: https://github.com/MemPalace/mempalace
score: 82
model: google/gemma-4-31b-it:free
generated_at: '2026-06-27T19:36:59.884817'
---

📌 MemPalace：將對話紀錄原封不動儲存，打造 Local-first 的 AI 記憶宮殿

TL;DR：一個 Local-first 的 AI 記憶庫，透過結構化索引與語義搜尋實現高精準度檢索，且完全不依賴外部 API。

大多數 AI 記憶方案傾向於對對話進行摘要（Summarization）或提取關鍵字，但這往往導致原始語境的流失。如果我們能將對話原封不動地儲存，並用一種像「記憶宮殿」般的結構來管理，檢索精度會如何？

🤔 **拒絕摘要，追求原封不動的 Verbatim Storage**

MemPalace 的核心設計理念是「逐字儲存」（Verbatim storage）。它不對內容進行摘要、提取或改寫，而是將對話歷史作為原始文本儲存，並透過語義搜尋（Semantic search）來檢索。這種做法確保了資訊的完整性，避免了在摘要過程中產生資訊損失。

🧩 **像記憶宮殿一樣的結構化索引**

為了避免在扁平的資料庫（Flat corpus）中進行低效搜尋，MemPalace 引入了結構化索引設計，將記憶空間類比為建築：
- **Wings（翼樓）**：用於區分不同的「人物」與「專案」。
- **Rooms（房間）**：用於分類不同的「主題」。
- **Drawers（抽屜）**：存放最終的「原始內容」。

透過這種層級設計，搜尋範圍可以被精確地限定在特定範圍內，而非在所有資料中盲目搜尋。

🧩 **可插拔的後端架構與隱私保護**

MemPalace 採取 Local-first 原則，除非使用者主動同意，否則所有資料都不會離開本地機器。其技術實作重點在於：
- **可插拔後端**：檢索層（Retrieval layer）採取 pluggable 設計。目前預設使用 ChromaDB，但開發者可以透過 `mempalace/backends/base.py` 定義的介面，在不影響系統其他部分的情況下替換不同的後端。
- **效能表現**：在 LongMemEval 測試中，其 R@5 原始得分達到 96.6%，且達成此結果的過程中完全沒有呼叫任何外部 API。

⚠️ **安裝與安全提醒**

- **安裝建議**：由於 MemPalace 提供 CLI 工具，建議在隔離環境（Isolated environment）中安裝，以避免在 Debian、Ubuntu 或 Homebrew Python 環境中遇到 PEP 668 錯誤。
- **安全警告**：官方僅提供 GitHub 儲存庫、PyPI 套件及 `mempalaceofficial.com` 網站。請警惕任何 `.tech`、`.net` 或其他 `.com` 變體域名，以免下載到惡意軟體。

🎯 **實務啟示**

對於追求極高隱私、且需要精確回溯對話細節的開發者，MemPalace 提供了一個可行的方向：透過「結構化分層（Wings → Rooms → Drawers）」而非單純依賴向量搜尋，可以有效縮小搜尋範圍並提升檢索精準度。

🔗 **來源**
- 標題：MemPalace/mempalace
- 作者／機構：MemPalace
- 連結：https://github.com/MemPalace/mempalace

#AI #LocalFirst #VectorDatabase #ChromaDB #SemanticSearch #OpenSource #Privacy #MemoryManagement #RAG #Python
