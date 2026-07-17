---
title: 'GRASP: GRanularity-Aware Search Policy for Agentic RAG'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.10463
score: 92
model: tencent/hy3:free
generated_at: '2026-07-17T08:12:58.611617'
---

📌 【HuggingFace Daily Papers】GRASP：用 RL 訓練 Agent 自適應協調檢索粒度

TL;DR：GRASP 以強化學習讓 Agent 在多步推理中動態選用檢索工具，提升 Agentic RAG 成效。

靜態 RAG 遇到需要多跳推理的問題往往力不從心，而讓模型自己決定「何時檢索、用哪種檢索、讀多細」卻始終是難題。太多無關 token 混進上下文，反而會幹擾 Agent 的推理判斷。

🤔 **Agentic RAG 的檢索控制難題**

Agentic RAG 讓語言模型能迭代式推理、產生搜尋查詢、檢索證據並預測答案。但模型仍難以決定：何時該檢索、該用詞彙匹配（lexical matching）還是語意相似度（semantic similarity）、以及如何控制上下文粒度（context granularity），避免不相關 token 幹擾 agent 推理。

🧩 **GRASP：以 RL 框架協調三種檢索動作**

論文提出 GRASP，一個 reinforcement learning (RL) 框架，訓練 agent 在多步推理過程中自適應協調互補的檢索工具。框架提供三類動作：
- semantic search（語意搜尋）
- keyword search（關鍵字搜尋）
- paragraph-reading（段落閱讀）

Agent 可檢索句子層級（sentence-level）證據，並僅在必要時擴充套件更多上下文。訓練時使用的 reward 同時考量四項：answer accuracy（答案正確性）、grounded reading（有根據的閱讀）、complementary search（互補搜尋）、turn efficiency（回合效率）。

📊 **多跳推理基準上的表現提升**

在 multi-hop reasoning benchmarks 的實驗中，GRASP 相比以下三類方法，在檢索召回率（retrieval recall）與下游問答效能（question answering performance）均有提升：
- single-step retrieval（單步檢索）
- prompting-based agentic RAG（基於提示的 agentic RAG）
- RL-based retrieval baselines（基於 RL 的檢索基線）

📊 **學到的策略具可解釋的略讀與掃描行為**

定性分析與消融研究（qualitative and ablation analyses）顯示，學到的 policy 發展出可解釋的 skimming 與 scanning 行為：用 semantic search 做廣泛探索、paragraph reading 做區域性驗證、keyword search 找特定實體證據。這顯示學會協調檢索訊號與上下文粒度，對 agent 正確推理相當關鍵。

🎯 **實務啟示**

對建構 Agentic RAG 系統的工程師而言，與其只接單一檢索管線，不如把多種檢索工具（語意、關鍵字、段落閱讀）開放給 agent 並用 RL 訓練其排程策略；同時 reward 設計應納入正確性以外的閱讀根據與效率，才有可能學出可解釋且不浪費上下文的推理行為。

🔗 **來源**
- 標題：GRASP: GRanularity-Aware Search Policy for Agentic RAG
- 連結：https://huggingface.co/papers/2607.10463

#AgenticRAG #ReinforcementLearning #RetrievalAugmentedGeneration #MultiHopReasoning #GRASP #SemanticSearch #KeywordSearch #ContextGranularity #LLM #AgentReasoning
