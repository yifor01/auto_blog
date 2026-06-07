---
title: moorcheh-ai/memanto
source: GitHub Trending
url: https://github.com/moorcheh-ai/memanto
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-07T19:33:42.967823'
---

📌 【GitHub Trending】不再只是被動檢索：Memanto 試圖定義 AI Agent 的「主動記憶」

目前的 AI Agent 雖然能透過 RAG 或向量資料庫獲取資訊，但大多數記憶工具其實是「被動」的：Agent 必須先發出查詢、解析結果，再思考下一步。這種模式讓記憶像是一個靜態的快照，而非真正的認知過程。

如果你也發現 Agent 在長對話中容易產生混淆，或者無法區分「昨天剛決定的需求」與「半年前的舊設定」，那 Memanto 提出的設計理念值得關注。

🤔 **記憶不應是靜態快照，而應是能互動的代理**

Memanto 的開發核心來自於一個有趣的洞察：開發團隊直接詢問 AI 模型關於記憶的痛點。其中一個模型的回答成了設計藍圖：「我的記憶是以靜態快照形式注入上下文，這雖然有用，但本質上是被動的。我無法在對話中查詢它、更新它，也無法區分『我知道這件事』與『我曾被告知過這件事』。」

這揭示了現有記憶機制（如簡單的 Vector DB）與人類記憶模式之間巨大的鴻溝。

🧪 **從 6 個核心缺陷出發的設計實作**

Memanto 並非單純的儲存層，而是一個專門負責記憶的「Memory Agent」。它將記憶操作簡化為三個核心動作：`remember` (記憶)、`recall` (回想) 與 `answer` (回答)，旨在解決以下四大關鍵技術缺口：

1. **從「注入」轉向「查詢」**：記憶不再是以一大塊文本 (blob) 形式強行塞入 Context，而是可根據相關性被動態查詢。
2. **引入時間衰減 (Temporal Decay)**：解決「六個月前的偏好與昨天的期限權重相同」的問題，透過版本控制與時間信號，讓 Agent 能區分資訊的新舊。
3. **追蹤來源與信心度 (Provenance)**：為每條記憶加上元數據，讓 Agent 能分辨這是「明確的事實」還是「推論出的模式」，並標記信心水準。
4. **結構化分層記憶 (Typed Memory)**：不再將情節記憶 (Episodic)、語義記憶 (Semantic) 與程序記憶 (Procedural) 全部壓扁在同一個維度，而是採取分層管理。

💡 **主動式記憶如何提升 Agent 的可靠性？**

Memanto 的設計核心在於將記憶「代理化」。當記憶層具備主動管理能力時，Agent 能夠在對話過程中動態更新狀態，而不需要依賴繁瑣的 Prompt 工程來提醒模型如何處理檢索結果。

這種「零導入延遲 (Zero Ingestion Latency)」與「狀態感知」的設計，能讓 Agent 在追求長期目標時，減少因上下文過載而產生的混淆，真正實現跨 Session 的持續上下文 (Persistent Context)。

⚠️ **目前僅揭露核心設計，實際效能仍需實測**

由於目前資訊主要集中在設計理念與功能定義，關於其在極大規模數據下的檢索精準度、以及與主流向量資料庫（如 Pinecone 或 Milvus）在延遲上的量化對比，仍需在實際部署後進一步驗證。

🎯 **對 AI 工程師的實務啟示：重新思考記憶層設計**

如果你正在開發複雜的 AI Agent，建議可以從 Memanto 的分層記憶 (Typed Memory) 與時間衰減機制中獲取靈感：
- **區分記憶類型**：嘗試將「用戶偏好」與「操作步驟」分開儲存。
- **加入時間權重**：在檢索時，給予近期資訊更高的權重。
- **標記信心度**：讓 Agent 在回答時能誠實地表示「這是我推論的」而非「這是既定事實」。

🔗 **專案連結**
📦 **Memanto - Memory that AI Agents Love!**
👤 moorcheh-ai
🔗 GitHub: https://github.com/moorcheh-ai/memanto

你認為 AI Agent 最缺乏的記憶能力是什麼？是對時間的感知，還是對資訊來源的判斷？歡迎在下方討論 👇

#AI #AIAgents #OpenSource #LLM #MemoryAgent #GitHubTrending #軟體工程
