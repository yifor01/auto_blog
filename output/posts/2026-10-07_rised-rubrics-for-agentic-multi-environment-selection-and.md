---
title: 'RISED: Rubrics for Agentic Multi-Environment Selection and Self-Distillation'
source: Apple ML
url: https://machinelearning.apple.com/research/rised-multi-environment-selection
model: claude-code/sonnet
generated_at: '2026-10-07T22:20:14.734488'
score: 92
---

📌 Apple ML 新研究：用 Rubric 取代純 Reward，訓練跨環境通用 Agent

TL;DR：RISED 用文字 rubric 取代純量 reward，解決多環境 RL 訓練中資料選擇與同質失敗批次的難題。

🎣 當一個 LLM agent 要同時在多種互動環境裡學習時，單純用一個數字當 reward，往往會漏掉很多重要資訊，比如這一批 rollout 到底「輸在哪裡」「贏在哪裡」。Apple ML 的這篇研究，試圖用文字取代數字，重新設計訓練資料的篩選方式。

🤔 多環境強化學習的兩個卡點

論文指出，把單一 LLM agent 跨多種互動環境聯合訓練，是通往「通用型 agent」的一條重要路徑，但現有的課程設計（curriculum）與資料選擇策略通常是以環境為單位分配訓練資源，或只依賴局部的 reward 訊號，並沒有明確考量「目前這一批不同環境的 rollout 之間」彼此的關係來做提示組（prompt-group）選擇。

同時，由於各環境的學習速度不一致，同一個訓練批次裡可能同時出現「全部失敗」和「全部成功」的 rollout 群組，而這類資料完全沒有組內相對 reward 訊號可用。這兩個問題共同指出：只靠純量 reward，在多環境 RL 裡既缺乏跨環境關係資訊，組內獎勵相同時也沒有對比訊號。這正是論文想引入更豐富的文字回饋（例如描述 rollout 行為的 rubric）來補足的地方。

🧩 RISED：rubric 同時拿來做資料選擇與策略監督

論文提出的 RISED 做法是：

- 用一個 LLM judge，依照一套跨環境共用的預定義 rubric 詞彙表，為每一筆 rollout 打標籤，產生「行為剖面」(profile)。
- 這些剖面被用來引導線上資料選擇，挑出與整個混合環境批次整體行為組成相符、同時跟已選資料重疊度較低的樣本。
- 正向 rubric（描述理想行為）作為 on-policy self-distillation teacher 的特權上下文（privileged context），提供額外的 token 層級監督；
- 負向 rubric（描述不理想行為）則用來引導後續 rollout 生成，避開反覆出現的失敗模式。

這三個元件組合起來就是 RISED：rubric 不只是拿來當 reward，而是同時驅動資料選擇與策略監督。

📊 跨多個模型骨幹都取得最高平均通過率

論文宣稱，在不同的模型骨幹（model backbones）上，RISED 都取得最高的平均通過率（mean pass rate），而且在每一個個別環境中的排名都是第一或第二。摘要並未提供具體的通過率數字或所比較的環境名單，因此本文不補上杜撰的數據。論文也提到可以透過 rubric 做進一步的行為變化分析，解釋這些提升從何而來。

🎯 實務啟示

如果你正在訓練需要跨多種工具／環境運作的 agent，這篇研究提供一個值得參考的方向：與其只盯著 reward 數字做課程編排，不如讓 LLM judge 用結構化的文字 rubric 去描述每次 rollout 的行為模式,再拿這些描述去驅動資料選擇與蒸餾式監督，可能比單純的 reward shaping 更能處理「組內信號缺失」的訓練死角。

🔗 來源
- 標題：RISED: Rubrics for Agentic Multi-Environment Selection and Self-Distillation
- 作者／機構：Jingtan Wang, Sirajul Salekin, Young mok Jung, Javier Movellan, Bryan Kian Hsiang Low, Manjot Bilkhu（Apple ML，部分作者與新加坡國立大學 NUS 合作）
- 連結：https://machinelearning.apple.com/research/rised-multi-environment-selection

#ReinforcementLearning #LLMAgents #AppleML #RubricReward #SelfDistillation #MultiEnvironmentRL #DataSelection #AgenticAI #MachineLearning #CurriculumLearning
