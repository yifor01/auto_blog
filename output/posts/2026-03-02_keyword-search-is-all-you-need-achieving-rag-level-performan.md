---
title: "Keyword search is all you need: Achieving RAG-Level Performance without vector databases using agentic tool use"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2602.23368
score: 128
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-03T00:55:21.030877
---

📌 【Amazon AWS 最新研究】RAG 真的需要向量資料庫嗎？我們用關鍵字搜尋打敗了 90% 的 RAG

Retrieval-Augmented Generation (RAG) 已經成為基於知識庫生成準確回應的標準方法。但你知道嗎？這套系統可能比你想像的還要「複雜」。

🤔 **RAG 的隱藏成本：你可能不需要向量資料庫**

RAG 的挑戰不只在於技術複雜度，還包括：
- 向量資料庫的維護成本
- 向量嵌入的計算開銷
- 知識庫更新時的重新編目需求
- 整合與部署的技術門檻

但如果我告訴你，有種方法可以達到 RAG 90% 的效果，卻不需要向量資料庫，你會相信嗎？

🧪 **Amazon AWS 的關鍵字搜尋實驗**

這項研究直接比較了兩種架構：
- 傳統 RAG 系統（使用向量資料庫）
- 工具增強的 LLM 代理（只用關鍵字搜尋）

研究團隊設計了一個代理，只給它基本的關鍵字搜尋工具，然後讓它與傳統 RAG 系統進行對決。

 **關鍵結果：90% 的效能，0 個向量資料庫**

- 工具增強代理的效能指標達到 **90.2%**（相較於傳統 RAG）
- 完全不需要向量資料庫、嵌入模型或複雜的向量索引
- 實作簡單、成本效益高、特別適合需要頻繁更新知識庫的場景

💡 **為什麼關鍵字搜尋可以這麼強大？**

關鍵在於「代理的智能」。當 LLM 能夠：
1. 動態決定搜尋策略
2. 多輪查詢以精煉結果
3. 根據上下文調整搜尋詞彙
4. 自行判斷資訊的相關性

...那麼傳統向量搜尋的優勢就大幅縮小了。

⚠️ **這不是說 RAG 沒用，而是說有更簡單的選擇**

向量搜尋在某些特定場景仍然有其必要性（如模糊匹配、語意相關性）。但對於許多企業應用來說，這項研究顯示：我們可能高估了向量資料庫的必要性。

🎯 **實務啟示：你該考慮的三種情境**

1. **知識庫頻繁更新**：每次更新都得重新向量化，關鍵字搜尋免除這個成本
2. **預算有限的專案**：省下向量資料庫的開銷，用於其他優化
3. **快速原型開發**：不用搭建複雜的向量搜尋基礎設施

🔗 **論文連結**
📝 Keyword search is all you need: Achieving RAG-Level Performance without vector databases using agentic tool use
👤 Shreyas Subramanian, Adewale Akinfaderin, Yanyan Zhang, Ishan Singh, Mani Khanuja @ Amazon Web Services
🔗 論文：arxiv.org/abs/2602.23368

你們的 RAG 系統現在用的是什麼架構？有考慮過這種替代方案嗎？歡迎分享你的想法 👇

#RAG #VectorDatabase #LLM #AI #InformationRetrieval #AmazonAWS #機器學習 #軟體工程

---

💡 **小補充**：這篇論文的關鍵洞察是「智能工具使用」可以彌補搜尋技術的不足。就像給一個聰明人一把普通的錘子，可能比給一個新手一整套專業工具還有效。
