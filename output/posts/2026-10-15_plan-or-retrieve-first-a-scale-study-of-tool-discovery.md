---
title: Plan or Retrieve First? A Scale Study of Tool Discovery Architectures
source: Apple ML
url: https://machinelearning.apple.com/research/plan-retrieve-tool-discovery
model: claude-code/sonnet
generated_at: '2026-10-15T20:41:33.850563'
score: 97
---

📌 先規劃還是先檢索？Apple 用大規模實驗找出工具發現的最佳解

TL;DR：ToolBench 實驗顯示「先規劃再檢索」或「先檢索再規劃」誰更好，取決於查詢的複雜度。

直覺上，讓 LLM 先想清楚自己需要什麼工具、再去檢索，聽起來理應比盲目地拿使用者的問題去搜尋更聰明——但這篇 Apple ML 的研究發現，答案要看查詢有多複雜。

🤔 工具太多，context window 塞不下

Tool-augmented 的 LLM agent 在規劃執行前，得先從龐大的 API 清單中找出相關工具，但有限的 context window 不可能把所有工具定義都塞進一個 prompt。目前主流做法是 Retrieve-then-Plan（RtP）：把使用者查詢做 embedding，再用近似最近鄰（approximate nearest-neighbor）搜尋，從登錄表中找出相似工具。

🧩 先讓 LLM「猜」出工具長什麼樣子，再拿去檢索

研究團隊提出另一種做法：Plan-then-Retrieve（PtR）。LLM 先產生 Abstract Tool Stubs——也就是對所需能力的假設性函式簽名（function signature）——再拿這些 stub 當作檢索查詢，去比對登錄表中的真實工具。簡單說，RtP 是「拿問題直接找工具」，PtR 是「先猜工具的樣子，再拿猜測去找工具」。

📊 複雜度決定贏家：單工具查詢 RtP 贏，多工具查詢 PtR 贏

研究在 ToolBench 上進行評估，該資料集涵蓋 46,984 個不重複的 API endpoint、50 個分類，並拆成三種子集：單工具查詢（G1）、同分類多工具查詢（G2）、跨分類多工具查詢（G3）。結果出現明確的「複雜度交叉」現象：RtP 在單工具查詢上表現優於 PtR，但 PtR 在多工具查詢上反過來勝出。

這個交叉現象在各種 retrieval budget（k=1 到 20）下都存在，在登錄表規模從 1,000 個到 47,000 個 API 之間也維持穩定，並且在不同模型家族（Gemini 2.5 Flash 與 gpt-oss-120b）上都一致。

💡 stub 幻覺：同一個機制，簡單查詢時是缺點，複雜查詢時是優點

研究團隊觀察到一種「stub 幻覺」的失敗模式：LLM 會編造出看似合理但實際不存在的 API 名稱。這個機制是雙面刃——在簡單查詢上，PtR 產生的 stub 會把專有名詞（proper noun）訊號抽象掉，而這些訊號本來是 RtP 可以直接匹配上的，因此 PtR 在簡單查詢上反而吃虧；但在複雜查詢上，同一個抽象化機制能把多面向的意圖拆解成一個個功能性子需求，讓 PtR 更容易命中正確工具。

研究也分析了 token 開銷：PtR 多出的一次 discovery 呼叫，大約讓推論成本翻倍。這個額外成本在多工具查詢上值得付出，但在單工具查詢上反而是虧本的。

🎯 實務啟示：用現成訊號做複雜度自適應路由

研究建議的實務方向是 complexity-adaptive routing——依查詢複雜度動態決定要用 RtP 還是 PtR。而且這個路由決策不需要額外的判斷模型：RtP 本身的 top-1 檢索分數，就是 pipeline 裡現成、零成本的訊號，可以直接拿來當作切換 RtP／PtR 的依據。

🔗 來源
- 標題：Plan or Retrieve First? A Scale Study of Tool Discovery Architectures
- 作者／機構：Mingfei Zhang, Amit Surana, Ziauddin Majid, Chenxi Wang, Michael Xu（Apple ML）
- 連結：https://machinelearning.apple.com/research/plan-retrieve-tool-discovery

#LLMAgents #ToolUse #RAG #ToolRetrieval #AppleML #AIResearch #ToolBench #AgenticAI #PromptEngineering #EMNLP
