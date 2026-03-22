---
title: "Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.10700
score: 105
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-12T19:18:44.013715
---

# 📌 用知識圖譜提升 RAG 準確率 29.6%，這套方案值得所有 AI 團隊關注

當 AI 助手面對複雜查詢時，背後的 RAG (Retrieval-Augmented Generation) 系統往往捉襟見肘。WordLift 團隊提出了一個簡單但有效的解法：讓 Schema.org 結構化資料成為記憶層，讓 Agent 能夠自主探索知識網路。

🤔 **為什麼傳統 RAG 系統準確率總是不夠高？**

傳統 RAG 把文件當作一團「純文字」處理，忽略了其中隱含的知識結構。就像讓人只看書頁上的字，卻看不到章節目錄、交叉引用和知識脈絡。這樣的限制在面對多步推理或跨領域查詢時特別明顯。

🧪 **四大領域、52 個測試案例的實驗設計**

這項研究在 Vertex AI Vector Search 2.0 上測試了七種條件組合：
- 三種文件格式：純 HTML、含 JSON-LD 的 HTML、增強型實體頁面
- 兩種檢索模式：標準 RAG vs. 具備多跳連結遍歷的 Agentic RAG
- 還有一個增強版 (Enhanced+)，加入麵包屑導航和實體互聯

測試領域涵蓋編輯、法律、旅遊和電商，確保結果具備普適性。

 **關鍵發現：結構化資料帶來 29.6% 準確率提升**

- 標準 RAG + 增強實體頁面：準確率從 3.75 → 4.85（+29.6%）
- Agentic RAG + 增強實體頁面：準確率從 3.74 → 4.86（+29.8%）
- 增強版 (Enhanced+) 的完整性評分最高：4.55/5

特別值得注意的是，單純加入 JSON-LD 標記的效果有限，關鍵在於「增強實體頁面」的設計，包括 LLM.txt 風格的代理指令、導航麵包屑和神經搜尋能力。

💡 **為什麼結構化資料能大幅提升 AI 表現？**

這背後的原理類似於人類閱讀時的「知識組織」：
1. Schema.org 提供統一的語義框架，讓 AI 理解「這是日期」「這是價格」「這是地點」
2. 可解參照的實體頁面讓 Agent 能像人一樣「跳轉」到相關知識
3. 多跳連結遍歷模擬人類的深度探索思維

這不只是搜尋的優化，而是讓 AI 獲得了「知識導航」的能力。

⚠️ **研究限制與實務考量**

- 實驗主要使用 Vertex AI 平台，其他向量資料庫的效能待驗證
- 增強版的額外收益雖然最高，但統計上不顯著
- 實作需要額外的工程成本來生成結構化資料和實體頁面

🎯 **對開發者的實際啟示**

如果你正在建構 RAG 系統，這項研究建議：
- 從 Schema.org 開始結構化你的資料
- 實作可解參照的實體頁面，讓 AI 能夠「點進去看」
- 考慮加入類似 LLM.txt 的代理指令，引導 AI 行為
- 評估增強型實體頁面 vs. 增強版的成本效益

🔗 **論文連結**
📝 Structured Linked Data as a Memory Layer for Agent-Orchestrated Retrieval
👤 Andrea Volpini, Elie Raad, Beatrice Gamba, David Riccitelli (WordLift)
🔗 論文：arxiv.org/abs/2603.10700

WordLift 團隊還開源了他們的資料集、評估框架和增強實體頁面模板，有興趣的團隊可以直接基於這些資源進行改進。

你們的 RAG 系統有考慮過加入結構化資料嗎？分享你的經驗或問題 👇

#RAG #知識圖譜 #Schemaorg #AI工程 #資訊檢索 #WordLift #VertexAI
