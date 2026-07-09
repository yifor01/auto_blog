---
title: Graphify-Labs/graphify
source: GitHub Trending
url: https://github.com/Graphify-Labs/graphify
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T10:01:51.511887'
---

📌 **別再用 Grep 找程式碼了：用 Graphify 將整個專案轉化為可查詢的知識圖譜**

TL;DR：透過 AST 解析將程式碼與檔案轉為本地知識圖譜，讓 AI 助手能追蹤概念路徑而非僅靠向量搜尋。

當專案規模大到連最熟練的工程師也無法在腦中建立完整的呼叫圖譜時，我們通常只能依賴 `grep` 或 IDE 的全域搜尋，但這類方法只能找到「字串」，而非真正的「邏輯關係」。

🤔 **從「字串搜尋」轉向「路徑追蹤」**

Graphify 旨在解決開發者在大型專案中難以快速掌握結構的問題。它不採取傳統的向量索引（Vector Index）或 Embedding 方式，而是將程式碼、檔案、PDF、圖片與影片直接對映為一個知識圖譜（Knowledge Graph）。這意味著你可以直接查詢概念之間的路徑，或要求 AI 解釋某個特定概念，而非在大量檔案中盲目搜尋。

🧩 **結合 AST 解析與語義分析的混合架構**

Graphify 的核心設計在於區分「確定性解析」與「語義推理」，以兼顧效能與隱私：

- **程式碼解析（Code Maps）**：完全在本地執行且免費。使用 tree-sitter AST（抽象語法樹）進行確定性解析，不經過 LLM，確保程式碼不會離開使用者機器。
- **非結構化資料（Docs, PDFs, Images, Videos）**：透過 AI 助手的模型或配置的 API Key 進行語義分析（Semantic Pass）。
- **關係標記**：圖譜中的每一條邊（Edge）都有明確解釋，並標記為 `EXTRACTED`（來源中明確存在）或 `INFERRED`（由 Graphify 推理得出），讓使用者能分辨哪些是直接讀取，哪些是 AI 推論。

📊 **視覺化與互動體驗**

Graphify 能將整個專案（例如 FastAPI 的程式碼庫）轉換為視覺化圖譜。在產出的 `graph.html` 中，每個節點代表一個概念，且透過顏色區分檢測出的社群（Communities），所有節點均可點選互動。

🎯 **實務啟示：如何快速部署到 AI 助手**

對於希望強化 AI 助手對專案理解能力的工程師，可以透過以下步驟在 30 秒內完成安裝：

1. 安裝 CLI 工具：`uv tool install graphifyy`（或使用 `pipx install graphifyy`）。
2. 註冊技能：執行 `graphify install` 將其整合至 AI 助手。
3. 使用方式：在 AI 助手中輸入 `/graphify` 即可開始對映專案。

🔗 **來源**
- 標題：Graphify-Labs/graphify
- 作者／機構：Graphify-Labs
- 連結：https://github.com/Graphify-Labs/graphify

#Graphify #KnowledgeGraph #AST #TreeSitter #AI #CodingAssistant #LocalLLM #SoftwareArchitecture #DeveloperTools #FastAPI
