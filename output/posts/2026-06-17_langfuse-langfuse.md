---
title: langfuse/langfuse
source: GitHub Trending
url: https://github.com/langfuse/langfuse
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-17T20:36:18.134912'
---

📌 **【開源 LLM 工程平台】Langfuse：從「感覺有效」到「數據證明有效」的 LLM 觀測方案**

開發 LLM 應用時，最痛苦的往往不是寫 Prompt，而是在應用上線後，面對用戶回饋的「AI 胡說八道」時，你根本不知道這次對話中，到底是 Retrieval 抓錯了、Embedding 偏移，還是 Prompt 寫得不夠精準。

許多開發者依賴直覺不斷調整 Prompt，但這種「試錯法」在生產環境中極其低效且危險。

🤔 **LLM 開發的黑盒子：追蹤、管理與評估的斷層**

在傳統軟體開發中，我們有詳細的 Log 與監控指標。但在 LLM 時代，一次完整的請求可能包含：檢索 (Retrieval) $\rightarrow$ 提示詞組合 $\rightarrow$ LLM 生成 $\rightarrow$ 後處理。如果結果不理想，開發者很難快速定位問題出在哪個環節。此外，Prompt 的版本管理與評估（Evaluation）往往散落在不同的文件或表格中，缺乏系統化的迭代機制。

🧪 **整合追蹤、管理與評估的工程閉環**

Langfuse 提供了一個開源的 LLM 工程平台，將開發流程中的三個關鍵環節整合在同一個系統中：

1. **可觀測性 (Observability)**：透過 Instrument 應用程式將 Traces 導入，追蹤所有 LLM 呼叫及其相關邏輯（如檢索步驟、Embedding 或 Agent 行動），讓複雜的用戶對話 session 變得透明且可調試。
2. **提示管理 (Prompt Management)**：將 Prompt 從程式碼中抽離，實現集中管理與版本控制。其伺服器與客戶端強大的快取機制，讓開發者可以在不增加應用延遲的情況下，快速迭代 Prompt。
3. **評估流水線 (Evaluations)**：提供多元的評估機制，包含 LLM-as-a-judge、程式碼評估器、收集用戶回饋、手動標記，以及透過 API/SDK 建立自定義評估流水線。

🚀 **以 ClickHouse 為後端，為生產環境設計的落地方案**

Langfuse 的技術選擇反映了其對高性能需求的考量。它採用 ClickHouse 作為開源數據庫後端，確保在大數據量的 Trace 記錄下仍能保持高效的查詢速度。對於企業而言，它支持快速的 Self-host 部署，滿足數據隱私與安全需求。此外，透過 Dataset 功能，開發者可以建立測試集與基準 (Benchmarks)，實現預部署測試與結構化實驗，將 LLM 的改進過程從「感覺」轉化為「數據驅動」。

💡 **將 LLM 迭代轉化為系統工程**

這類工具的核心價值在於將「提示詞工程」轉化為「軟體工程」。透過 Langfuse，團隊可以建立這樣的工作流：
$\text{監控 Trace} \rightarrow \text{發現失效案例} \rightarrow \text{建立 Dataset} \rightarrow \text{迭代 Prompt} \rightarrow \text{跑評估流水線驗證} \rightarrow \text{部署新版本}$。這種閉環能大幅降低 AI 應用在生產環境中的不確定性。

⚠️ **非首創方案，但勝在開源與整合**

LLM 觀測工具目前市場競爭激烈，Langfuse 並非首創此類功能。但其優勢在於將追蹤、管理與評估這三者深度整合在一個開源平台中，而非讓開發者在多個碎片化工具之間切換。

🎯 **建議 AI 工程師與技術主管嘗試的場景**

- **如果你正在面臨「Prompt 太多、版本管理混亂」**：嘗試將 Prompt 移至 Langfuse 進行集中管理。
- **如果你無法快速定位 LLM 輸出錯誤的原因**：導入 Trace 追蹤，分析完整鏈條的執行路徑。
- **如果你需要建立量化的 LLM 評估指標**：利用 LLM-as-a-judge 或自定義 API 建立自動化評估流水線。

🔗 **專案連結**
📝 Langfuse: Open Source LLM Engineering Platform
🔗 GitHub: https://github.com/langfuse/langfuse

你們在開發 AI 應用時，是如何管理 Prompt 版本與評估效果的？歡迎在下方分享你的工作流 👇

#AI #LLMOps #OpenSource #Langfuse #LLM #軟體工程 #ClickHouse #可觀測性
