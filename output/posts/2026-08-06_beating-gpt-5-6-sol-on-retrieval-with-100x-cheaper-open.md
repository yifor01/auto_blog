---
title: Beating GPT-5.6 Sol on retrieval with 100x cheaper open models
source: Hacker News
url: https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency
model: tencent/hy3:free
generated_at: '2026-08-06T08:37:52.683255'
score: 93
---

📌 【Castform 實踐】用 100 倍便宜的開源模型，在檢索任務上擊敗 GPT-5.6 Sol

TL;DR：透過 RL 後訓練技術，讓小規模開源模型在代理式檢索（Agentic Retrieval）上達到媲美頂尖模型的效果，且成本大幅降低。

🎣 **從單次檢索到代理式檢索的演進**

在 2022 年左右，業界趨向於使用 Embedding 進行向量檢索，工程師手動建構 RAG（檢索增強生成）流程。然而到了 2025 年，開發者開始開發「代理式檢索」（Agentic Retrieval）工作流，將大問題分解為小問題，並透過模型在迴圈中進行多次規劃與搜尋。

這種模式雖然強大，但也帶來了沈重的負擔：每一次迴圈迭代都需要呼叫一次頂尖模型（Frontier Model），這使得典型的多輪搜尋請求不僅耗時（例如使用 gpt-5.6-sol 可能超過 10 秒），且成本昂貴（單次請求約 0.03 美元）。

🧩 **Castform 的解決方案：讓後訓練變得像 Prompt Engineering 一樣簡單**

雖然開源模型（Open-weights models）的成本比頂尖模型便宜 100 倍，但其原生能力通常較弱。Castform 的核心理念是透過 RL（強化學習）後訓練（Post-training）來彌補這一差距。

Castform 解決了企業在進行後訓練時遇到的兩大痛點：
1. **缺乏訓練數據**：將企業內部的專有文件（如產品記錄、維基百科、客戶互動紀錄）轉化為有效的訓練任務。
2. **基礎設施門檻高**：開發者不需要處理複雜的機器學習與 GPU 內部細節。

📊 **如何利用現有的數據庫進行強化學習**

有效的 RL 後訓練需要三個要素：任務（Task）、環境（Environment）與獎勵函數（Reward Function）。Castform 結合 Neon 的 Lakebase Search 來實現這一流程：

1. **資料轉換**：將原始文件存放在 Neon 的 Postgres 中，利用 Castform 自動生成合成數據（Synthetic Data），將文件轉化為「問題—答案」對。
2. **環境互動**：在訓練過程中，代理模型會不斷呼叫搜尋工具（如 Lakebase 的混合搜尋）來獲取正確的上下文。
3. **獎勵機制**：開發者可以定義獎勵函數（例如：檢索到的來源是否正確、引用是否精準、最終答案是否正確），引導模型透過試錯（Trial and Error）來優化效能。

💡 **利用 Neon 解決突發性的計算負載**

在進行 RL 訓練時，代理模型會在成千上萬個並行 Rollouts（試算）中重複呼叫搜尋工具，這會產生極高且不穩定的計算負載。

Neon 的 Lakebase 提供動態計算縮放（Dynamic Compute Scaling），能夠吸收這些突發需求，而不必為了訓練期間的峰值而長期維持高昂的容量配置。此外，Neon 的分支（Branching）與時空旅行查詢（Time-travel queries）功能，讓每個 Rollout 都能在隔離且可重建的資料庫狀態中運行，避免代理行為對生產環境或其他訓練任務造成影響。

🎯 **實務啟示**

對於追求成本效益的工程團隊來說，不需要盲目追求最昂貴的 API。透過將現有的企業知識庫與 Castform 的後訓練流程結合，開發者可以用極低的成本，訓練出專屬於自家業務領域、且在檢索能力上能與頂尖模型抗衡的專用模型。

🔗 **來源**
- 標題：Beating GPT-5.6 Sol on retrieval with 100x cheaper open models
- 連結：https://neon.com/blog/how-castform-neon-beats-frontier-models-on-price-and-efficiency

#AI #MachineLearning #LLM #ReinforcementLearning #RAG #AgenticSearch #OpenSourceAI #Neon #Castform #PostTraining
