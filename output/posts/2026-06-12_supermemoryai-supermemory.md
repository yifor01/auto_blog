---
title: supermemoryai/supermemory
source: GitHub Trending
url: https://github.com/supermemoryai/supermemory
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-12T20:42:24.514473'
---

📌 【GitHub Trending】解決 AI 「金魚記憶」：Supermemory 打造 AI 的持久化記憶層

你是否發現，即便使用了 RAG，AI 依然無法真正「認識」你？每次開啟新對話，它就像個陌生人，必須重新閱讀長長的 Prompt 才能找回上下文。

這種「對話間失憶」的痛點，正是 Supermemory 試圖解決的核心問題。它不只是另一個向量資料庫，而是一個完整的記憶與上下文引擎（Memory and Context Engine），旨在為 AI 建立一個可演進的「個人或企業大腦」。

🤔 **AI 記得碎片，但並不理解「關係」與「時間」**

傳統 RAG 雖然能檢索文件，但缺乏對用戶狀態的動態追蹤。例如：如果你在三個月前說過「我喜歡 Python」，但上週說「我現在改用 Rust」，傳統 RAG 可能會同時檢索到這兩條衝突資訊，導致 AI 產生混亂。

Supermemory 的設計目標是讓 AI 能像人類一樣，不僅能記錄事實，還能處理知識的更新、矛盾衝突，並在資訊過時時自動「遺忘」。

🧪 **橫掃三大記憶基準測試：LongMemEval, LoCoMo, ConvoMem**

這項專案在 AI 記憶領域的三大指標性基準測試中均排名第一：
- **LongMemEval**：測試長程記憶的檢索能力。
- **LoCoMo**：測試局部上下文記憶的精準度。
- **ConvoMem**：測試對話記憶的維持能力。

這證明了其在處理複雜上下文與長期記憶維持上的效能優於現有方案。

⚙️ **核心技術架構：從事實抽取到混合檢索**

Supermemory 將整個上下文堆疊（Context Stack）整合進單一系統，其核心能力包含：

- **自動化記憶管理**：從對話中自動提取事實 (Fact Extraction)，並建立用戶檔案 (User Profiles)，將穩定事實與近期活動分開維護。
- **動態知識更新**：能處理時間軸上的資訊變更與邏輯矛盾，並實作自動遺忘機制，確保 AI 獲取的是最正確的當前上下文。
- **混合搜尋 (Hybrid Search)**：將 RAG（知識庫文件）與 Memory（個人化上下文）整合在單次查詢中，且用戶檔案的呼叫延遲僅約 50ms。
- **多模態提取器**：支援 PDF、圖片 (OCR)、影片 (轉錄) 以及對程式碼的 AST-aware chunking（基於抽象語法樹的分塊），確保程式碼片段的語義完整性。

🔌 **全方位連接器與即時同步**

為了讓記憶層能真正落地，Supermemory 提供了豐富的生態連接器，支援 Google Drive, Gmail, Notion, OneDrive 與 GitHub。透過 real-time webhooks，AI 的記憶能與外部工具同步，而非僅依賴手動上傳。

⚠️ **單一本体結構的維護挑戰**

Supermemory 將所有資訊整合在單一的記憶結構與本体 (Ontology) 中。雖然這提升了檢索效率，但在極大規模的知識庫中，如何維持本体的一致性以及防止記憶污染，將是實作時需要關注的挑戰。

🎯 **工程實踐：如何將其導入你的 AI 產品？**

對於想要開發「個人助理」或「企業知識助手」的工程師，Supermemory 提供了明確的實作路徑：
- **自託管部署 (Self-host)**：支持私有化部署，確保敏感數據的安全。
- **整合記憶圖譜**：利用其持久化記憶圖譜 (Persistent Memory Graph)，讓 AI 在跨對話中保持一致的人格與記憶。
- **替代傳統 RAG**：若你的產品需要「記得用戶偏好」而非僅是「檢索文件」，建議將其作為記憶層整合進現有的 LLM 工作流。

🔗 **專案連結**
📝 supermemoryai/supermemory
👤 supermemoryai
🔗 GitHub：https://github.com/supermemoryai/supermemory

如果你正在思考如何讓你的 AI Agent 擁有真正的「長期記憶」，這個專案非常值得研究。

#AI #RAG #OpenSource #LLM #Supermemory #GitHubTrending #AI工程師 #長期記憶
