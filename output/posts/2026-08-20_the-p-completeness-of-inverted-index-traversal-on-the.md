---
title: 'The P-Completeness of Inverted Index Traversal: On the Complexity of Evaluating
  Boolean Query DAGs'
source: Apple ML
url: https://machinelearning.apple.com/research/the-p-completeness-of-inverted-index-traversal
model: claude-code/sonnet
generated_at: '2026-08-20T06:37:27.979257'
score: 82
---

📌 【Apple 研究】AI Agent 組出的搜尋條件，為何會讓查詢引擎卡死

TL;DR：Apple 證明布林查詢 DAG 求值是 P-Complete 問題，並提出 ComputePN 演算法避開指數爆炸與全域掃描代價。

當 AI agent 開始自動組出層層疊疊、彼此纏繞的搜尋條件時，傳統倒排索引（inverted index）的兩種主流查詢執行策略，可能同時踩中「運算量指數爆炸」與「記憶體全域掃描」這兩個坑——而這篇論文說，這不是工程沒做好，而是理論上的天花板。

🤔 AI agent 組出的查詢，正踩在理論極限上

現代 AI agent 越來越常依賴搜尋基礎設施來執行複雜的 neuro-symbolic 推理流程，這些流程常會編譯成深度巢狀、非單調（non-monotonic）的布林查詢，作用在文字欄位上。論文指出，標準的倒排索引查詢評估策略面對這類結構時，會遇到嚴重的理論極限。

🧩 P-Complete 的證明，與 ComputePN 怎麼繞過爆炸

論文分析了兩種主流的查詢求值模型，各自卡在不同的地方：
- Document-at-a-Time（逐文件迭代式模型）：結構上受限於 NC^1 等級的公式求值能力，當查詢中出現「重新匯聚」的邏輯（同一個子條件在 DAG 裡被多條路徑重複參照）被展開成樹狀結構時，最差情況下會產生 O(2^|Q|)（Q 為查詢大小）的指數級運算爆炸。
- Term-at-a-Time（逐詞彙具現化模型）：在計算邏輯「否定」時，必須對整個文件宇宙進行掃描，付出 Ω(|U|)（U 為文件總數）的空間複雜度代價，論文稱之為「全域掃描」（Universal Scan）問題。

作者形式化了一套以 DAG（有向無環圖）為基礎的檢索語言 L_R，並證明其求值問題屬於嚴格的 P-Complete（P-完全）等級，代表在複雜度理論的框架下，這類查詢原則上難以被有效平行化求解。為了讓這類查詢仍能在實務上被高效處理，論文提出 ComputePN：一個確定性、具稀疏感知能力的求值演算法，核心設計是把邏輯否定與「對整個文件宇宙具現化」這件事解耦，改用一種新穎的「正向-負向雙重表示」，並搭配對 DAG 結構原生的 memoization（記憶化，即快取重複子計算結果），將求值時間嚴格限制在 O(|Q|·|U_active|)（查詢大小乘以實際活躍文件集合大小）。

💡 證明邊界的意義，而非打破邊界

這篇論文的價值不在於「跑得更快」的工程優化，而是先把問題釘死在複雜度理論的座標上：證明 L_R 的求值是 P-Complete，等於告訴工程師不要期待有平行演算法能徹底解決這類查詢的最壞情況，同時點出兩種傳統策略各自的病灶——Document-at-a-Time 死在邏輯重複展開的指數爆炸，Term-at-a-Time 死在否定運算的全域掃描。ComputePN 並沒有、也無法打破 P-Complete 這個理論邊界，而是透過正負雙重表示與 DAG memoization，把實際可達的複雜度壓到 O(|Q|·|U_active|)，讓這類查詢能「原生」跑在倒排索引上，不必依賴外部的樹展開或全庫掃描。

🎯 實務啟示

如果你的系統正讓 AI agent 自動組裝越來越複雜的搜尋條件，例如 RAG 前置的過濾邏輯或 multi-hop 推理查詢，這篇論文提醒了一個容易被忽略的風險：查詢一旦出現大量「重新匯聚」的子條件或深層否定，傳統倒排索引執行策略可能在毫無預警下踩到指數級或全域掃描的效能懸崖。檢查搜尋層是否具備類似 ComputePN 的稀疏感知與 DAG 級去重能力，會是規模化 agentic search 時值得留意的一項基礎設施指標。

🔗 來源
- 標題：The P-Completeness of Inverted Index Traversal: On the Complexity of Evaluating Boolean Query DAGs
- 作者／機構：Amir Aavani, Apple
- 連結：https://machinelearning.apple.com/research/the-p-completeness-of-inverted-index-traversal

#Apple #ComplexityTheory #InformationRetrieval #InvertedIndex #BooleanQuery #SearchEngine #AIAgents #TheoreticalCS #Algorithms #PComplete
