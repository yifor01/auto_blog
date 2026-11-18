---
title: SID AI Releases SID-2 Agentic Search Model With 0.720 NDCG Swarm Mode
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/17/sid-ai-sid-2-agentic-search-swarm/
model: claude-code/sonnet
generated_at: '2026-11-18T23:40:16.752696'
score: 98
---

📌 SID-2:用代理式搜尋取代固定 RAG,Swarm 模式衝出 0.720 NDCG

TL;DR:SID AI 發布第二代搜尋模型 SID-2 與多代理版本 Swarm,把「搜尋」本身變成可自主決策的 agent 任務。

RAG 的標準流程大家都很熟:rewrite、embed、search、rerank,固定順序跑一次就結束。但如果答案藏在第三次搜尋才能找到的文件裡呢?SID AI 這次的答案很直接:讓模型自己決定下一步搜什麼。

🤔 **固定管線的侷限,換成會「邊讀邊搜」的模型**

SID-2 是一個小型搜尋專家模型,不是通用對話模型。它的工作方式是搜尋、閱讀結果、調整策略、再搜尋一次,直到收斂。開發者只需要把自己的後端接上兩個工具:`text_search`(關鍵字搜尋)與 `search`(向量搜尋),模型在整個 episode 結束時呼叫 `report_helpful_ids` 回傳排序後的文件 ID。因為 SID-2 只看工具回傳的內容,不需要重新索引或搬動資料。

🧩 **Swarm 模式與可調節的推理強度**

SID-2 Swarm 讓多個 agent 互相傳訊息,並把自己的 context 分叉(fork)成新的 agent,各自探索語料庫的不同切片。SID AI 的論點是:搜尋任務從「讀更多文件」得到的提升,比「對每份文件想得更久」更大。

模型提供低、中、高三個推理強度(effort),每個強度各自訓練成獨立的專家模型,再透過多教師 on-policy distillation 合併回單一模型。另外還有 Metric Steering 功能,使用者可以指定要優化 NDCG、F1 或 Recall@k(k 從 1 到 50)。

訓練採用兩階段強化學習:第一階段只優化檢索品質,第二階段加入一個乘法型的延遲懲罰,且只作用在正向獎勵上。同時用一個 proposer-solver 的 self-play 迴圈,針對凍結的 SID-1 solver 生成高難度查詢。SID AI 表示這套訓練框架比 SLIME 預設設定有 6 倍的訓練吞吐量提升。

📊 **19 個語料庫、506 道題目的自建基準**

SID AI 建了一個涵蓋 19 個語料庫、506 道問題的驗證集,包含 HotpotQA、Enron 郵件、SEC 文件、PubMed 與 BrowseComp-Plus。以下數字均為 SID AI 自行公布於報告 Table 2–4:

- 高強度 SID-2 相較基礎模型,各指標平均高出 0.14 到 0.22。
- Swarm 模式在 19 個語料庫中,有 11 個取得領先。
- 在 WixQA 上,單一高強度 agent 的表現可與 Astra 打平,但成本低約 232 倍。
- 最低強度的 SID-2,表現優於 4 個平行跑的 SID-1,且 FLOPs 少了 13 倍。

(NDCG、時間與成本數據皆為 SID AI 在自家基準上測得,且不計入檢索後端本身的時間。)

🎯 **對工程師的意義**

如果你的 RAG 管線常常因為「一次檢索不夠」而漏掉關鍵文件,SID-2 提供的是另一種架構選擇:把搜尋策略的決策權交給模型本身,而不是寫死在管線裡。SID-2 已上架 SID 自家 API 與 Baseten,並提供 Python(`sid-sdk`)、TypeScript(`@sid-ai/sid-sdk`)、Go(`github.com/sidhq/sid-go`)SDK,以及 AWS SageMaker 部署輔助工具,參考實作採用 OpenAI client 格式,方便接入現有工具鏈。計費為每百萬 input token $0.25、output token $1.00,Swarm 模式則是 $0.50 與 $2.00,快取輸入價格為原價的 10%。

🔗 **來源**
- 標題:SID AI Releases SID-2 Agentic Search Model With 0.720 NDCG Swarm Mode
- 作者/機構:Michal Sutter, MarkTechPost
- 連結:https://www.marktechpost.com/2026/11/17/sid-ai-sid-2-agentic-search-swarm/

#AgenticAI #RAG #InformationRetrieval #SearchEngine #LLM #ReinforcementLearning #MultiAgent #NDCG #SIDAI #MachineLearning
