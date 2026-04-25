---
title: "Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)"
source: Hacker News
url: https://github.com/nex-crm/wuphf
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:06:07.333086
---

📌 【開源專案】用 Markdown + Git 打造 Karpathy 風格的 Agent 知識庫

當大家都在幫 AI Agent 堆疊 Postgres、Neo4j 或向量資料庫來解決記憶問題時，有沒有想過，最簡單的基礎設施或許就藏在 Git 和純文字裡？

🤔 **Agent 記憶的痛點：與其重貼上下文，不如讓知識跨會話累積**

Andrej Karpathy 曾提出一個概念：LLM 原生的知識基底（Knowledge Substrate）應該讓 Agent 既能讀取也能寫入，讓上下文在會話間自然累積，而不是每天早上重新貼上相同的背景資訊。然而，目前的實作往往過於沉重，引入了複雜的中間件。這個名為 **WUPHF** 的開源專案，試圖用最基礎的元件來實踐這個理念。

🧪 **極簡主義的技術選型：Markdown + Git + BM25**

作者 najmuzzaman 選擇了一條「返璞歸真」的路。這個 Wiki 層的核心架構如下：
- **儲存層**：使用 Markdown 檔案作為真相來源（Source of Truth），並透過 Git 進行版本控制。資料儲存在本地的 `~/.wuphf/wiki/`，使用者隨時可以 `git clone` 帶走所有知識。
- **索引層**：使用 Bleve 實作 BM25 全文檢索，搭配 SQLite 儲存結構化元數據（如實體、事實日誌）。
- **Agent 互動**：每個 Agent 擁有私有筆記本 (`agents/{slug}/notebook.md`)，並共享團隊 Wiki。透過「草稿到 Wiki」的推廣流程（Draft-to-wiki promotion），確保進入知識庫的內容經過審核。

 **85% Recall@20，BM25 證明自己還能打**

在尚未引入向量資料庫的情況下，這套系統在內部基準測試（500 個工件、50 個查詢）中達到了 **85% 的 Recall@20**。
這個數據驗證了作者的核心假設：在許多場景下，傳統的 BM25 關鍵字檢索加上良好的知識結構，已經足以支撐 Agent 的上下文需求，不需要一開始就引入複雜的 Embedding 流程。

💡 **知識溯源與自動化治理**

為了讓 Agent 寫入的內容具備可追溯性，系統設計了幾個有趣的機制：
- **Pam the Archivist**：所有的 Git 提交皆使用一個名為「Pam」的虛擬身份，讓知識的變更歷程在 `git log` 中清晰可見。
- **實體事實日誌**：採用 Append-only 的 JSONL 格式記錄事實，並有合成工作者（Synthesis worker）定期重建實體摘要。
- **自動維護**：內建每日 Lint 檢查，自動偵測矛盾、過時條目與斷裂連結（Wikilinks），模擬人類維護知識庫的過程。

⚠️ **單一辦公室範疇，合成品質依賴輸入**

目前的限制也很明確：這套系統目前僅適用於單一辦公室場景，尚未支援跨辦公室聯邦（Federation）。此外，合成品質遵循「垃圾進，垃圾出」原則，如果 Agent 的觀察品質不佳，產生的知識摘要也會受限。Lint 機制雖能輔助，但並非判斷引擎。

🎯 **向量資料庫不是起點，而是備案**

作者提供了一個很棒的實務觀點：不要預設複雜度。系統預留了 `sqlite-vec` 作為後備方案，只有在 BM25 的召回率低於門檻時才會考慮引入向量搜尋。對於正在設計 Agent 系統的開發者來說，這是一個值得參考的「由簡入繁」架構範例。

🔗 **專案連結**
📝 Show HN: A Karpathy-style LLM wiki your agents maintain (Markdown and Git)
👤 najmuzzaman
🔗 GitHub: https://github.com/nex-crm/wuphf
🎬 終端機 Demo: https://asciinema.org/a/vUvjJsB5vtUQQ4Eb

如果你正在煩惱 Agent 的長期記憶該怎麼存，會選擇這種極簡的 Git + Markdown 方案，還是會直接上向量資料庫？歡迎在留言區聊聊你的架構選擇 👇

#AI #Agent #LLM #KnowledgeManagement #OpenSource #Git #Markdown #SoftwareArchitecture #WUPHF
