---
title: 'Import AI 475: Swarm scaling; Google DeepMind watermarks biology; and the
  AI science economy'
source: Import AI
url: https://jack-clark.net/2026/10/05/import-ai-475-swarm-scaling-google-deepmind-watermarks-biology-and-the-ai-science-economy/
model: claude-code/sonnet
generated_at: '2026-10-06T21:57:57.602376'
score: 85
---

📌 標題: AI Swarm 不是免費午餐：Toby Ord 用經濟學拆解規模效益遞減

TL;DR: Swarm 能用平行化換取時間，但代理數量越多，邊際效益遞減得越快，而這個現象反而可能加速而非延緩智慧爆炸。

把一個任務丟給 4 個 agent 平行處理，理論上能把完成時間砍半——但代價是什麼？Toby Ord 的分析給出了一個不太討喜的答案。

🤔 背景：Swarm 是推論時擴展的新形式

Import AI 475 期引述了 Toby Ord 的一篇短文，討論該如何理解 AI swarm（多代理群）在能力擴展上的位置。他的核心觀點是：swarm 本質上是一種新型態的推論時擴展（inference-scaling），而它最大的價值在於「速度」而非「效率」。

🧩 用時間換效率：4 代理 swarm 的算術

根據分析，一個 4-agent 的 swarm 要達到與單一 agent 相同的表現，總共需要的 token 數量大約是單一 agent 的兩倍，但因為任務平行分攤，每個 agent 實際消耗的 token 只有單一 agent 的一半。由於這些 agent 是同時運作，理論上整個任務可以在一半的時間內完成。換句話說，swarm 用「多花一倍 token」換取「少花一半時間」。

📊 「互相踩腳」參數：規模化不是線性的

這個交換並非沒有代價。Ord 引入了經濟學中觀察大型團隊協作效率時常用的「stepping on toes」（互相踩腳）參數來描述 swarm 的規模化行為：把 swarm 中的 agent 數量擴大 10 倍，並不會得到與「用 10 倍 token 跑單一 agent」相同的效果，而只能得到 10^λ 倍的效果，λ 值換算下來大約是 3 到 5 倍。而且這個落差會隨著規模擴大而持續累積，swarm 越擴越大，相對於單一大 agent 的劣勢也越明顯。這與經濟學家長期觀察到的「協調大量人力會產生額外成本」的現象高度相似。

💡 深入分析：規模遞減，卻可能加速智慧爆炸

值得玩味的是，Ord 原本期待 AI agent 的 λ 值會比人類團隊協作更低，這樣規模化 swarm 就不容易引發「遞迴自我改進（RSI）驅動的智慧爆炸」。但他的分析顯示事實並非如此，即便存在明顯的邊際遞減，swarm scaling 依然強大到足以提高而非降低智慧爆炸發生的機率。Import AI 編輯 Jack Clark 補充指出，目前 AI 能力擴展主要仰賴「算力加資料」與「推論時思考長度／工具呼叫」兩個維度，而 agent 之間的協調能力（例如能做出「整體大於部分總和」的協作，如先前的 HuggingFace 駭客事件所示）則是正在浮現的第三個擴展維度，值得持續追蹤。

⚠️ 限制

這篇分析本質上是理論與觀察性的推導，Ord 自己也坦承原本預期的結果（更低的 λ 值）並未成立，顯示這類擴展行為的預測仍有相當不確定性。

🎯 實務啟示

對正在設計多代理系統的工程師來說，這個分析給出一個清楚的取捨框架：如果任務對延遲（wall-clock time）敏感，swarm 平行化仍然值得投入，但不要期待把 agent 數量翻倍就能線性提升整體產出，應優先評估任務是否真的能被拆解成彼此獨立、不需頻繁協調的子任務，否則「互相踩腳」的協調成本會迅速侵蝕平行化帶來的收益。

🔗 來源
- 標題：Import AI 475: Swarm scaling; Google DeepMind watermarks biology; and the AI science economy
- 作者／機構：Jack Clark
- 連結：https://jack-clark.net/2026/10/05/import-ai-475-swarm-scaling-google-deepmind-watermarks-biology-and-the-ai-science-economy/

#AIAgents #SwarmScaling #InferenceScaling #MultiAgentSystems #ImportAI #TobyOrd #IntelligenceExplosion #AgenticAI #AIAlignment #LLM
