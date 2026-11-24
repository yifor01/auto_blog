---
title: How to build and maintain an agentic evaluation
source: HuggingFace Blog
url: https://huggingface.co/blog/agentic-evals
model: claude-code/sonnet
generated_at: '2026-11-24T03:37:01.255772'
score: 92
---

📌 模型沒換，分數卻能差30%：HuggingFace拆解Agentic評測的八個步驟

TL;DR：HuggingFace發布指南，拆解agentic評測的架構與常見錯誤，主張用開源方式建立可信評測。

同一個模型，只換一套agent harness，準確率就能差將近30個百分點——這不是模型出了問題，而是評測本身的設計出了問題。HuggingFace最新發布的指南，正是要帶工程師看清agentic評測裡每一個環節如何悄悄左右最終分數。

🤔 **評測演進三階段，agentic評測正當紅**

HuggingFace指出，AI評測設計隨模型能力提升經歷三個階段：MMLU、GPQA等問答式benchmark檢查模型的答案；SWE-bench、WebArena等agentic benchmark則把範圍擴大到agent在真實環境中解決軟體問題、完成網站任務；近期多智慧體研究更進一步，開始評測一整個團隊或swarm協作完成的成果。文章聚焦在agentic評測，原因之一是其正成為模型發布公告裡最受矚目的評測類型，原因之二是它最適合用來理解評測設計如何影響模型表現。

現況也不樂觀：98.2%的模型-benchmark分數都是由單一方自行報告，缺乏獨立驗證；而Artificial Analysis在2026年10月發布的Intelligence Index v5中，六成評測仰賴私有測試集或保留答案。Google DeepMind甚至試驗了「雙盲評測」，用安全隔離環境讓外部評測方的測試題對模型提供者保密，同時模型權重對評測方保密——但文章強調，隱私本身不保證品質，隱藏佐證材料反而讓專家審查更困難。

🧩 **一個任務的八步旅程：從主張到分數**

HuggingFace以「讓agent分析物理實驗室拉曼光譜（Raman spectrum）峰值」為例，走過建立一套agentic評測的八個步驟：
1. 定義claim（要驗證agent具備什麼能力）
2. 找一個現有任務作為起點
3. 原封不動先跑一次，確認基準行為
4. 依實際需求調整任務
5. 檢查評測本身是否可靠
6. 讀取rollout留下的trace
7. 報告分數
8. 用同一套評測比較不同模型

文章也拆解了agentic評測的解剖結構：task給agent指令，agent harness把模型與工具包進一個固定的環境中運作，一次rollout是agent從頭到尾嘗試任務的過程（可能執行多次指令、檢查輸出、再試一次），evaluation harness會對每個任務跑多次rollout，rollout結束後由verifier評分環境的最終狀態，每次rollout也會留下trace，最終trace與分數共同構成發布證據。這也解釋了為什麼光是換掉agent harness，就能讓Terminal-Bench上同一個模型的準確率相差29.9個百分點。

📊 **HuggingFace Hub上的評測生態規模**

HuggingFace Hub目前host約3500個評測排行榜，過去一年評測資料集數量成長約16倍，達到約17000個。近期平臺也加入了多項與agentic評測相關的抽象概念：方便審閱分享的Traces（agent工作紀錄）、用於排行榜的Benchmarks資料集、以及用作agentic RL或評測環境的Environments。

💡 **開放不代表沒有保護，而是分層決定什麼該公開**

文章主張，即使部分測試集需要保密以降低污染風險，建構者仍應盡可能公開基礎設施、評分方法與任務設計的佐證資料。審查的前提，是讓他人有辦法質疑測量方式並糾正錯誤，必要時也可以採用受控的審閱方式而非完全公開發布。

⚠️ **私有不等於高品質**

保留測試集或答案雖然能降低資料污染，但文章也提醒，私密本身並不保證評測品質，反而可能讓外部專家更難檢視任務設計與評分邏輯是否存在錯誤。

🎯 **對工程師的實務啟示**

在設計或採用agentic benchmark時，不能只看模型分數，還要問清楚背後的agent harness、verifier邏輯與trace是否可追溯、可比較；而複用現有的開源task與environment，能把精力留給真正需要的領域專業驗證工作，而不是重造輪子。

🔗 **來源**
- 標題：How to build and maintain an agentic evaluation
- 作者／機構：Avijit Ghosh、Ben Burtenshaw、Irene Solaiman（Hugging Face）
- 連結：https://huggingface.co/blog/agentic-evals

#AgenticAI #AIEvaluation #HuggingFace #Benchmarking #OpenSource #LLMEval #ReproducibleResearch #AIBenchmarks #MachineLearning #EvalInfrastructure
