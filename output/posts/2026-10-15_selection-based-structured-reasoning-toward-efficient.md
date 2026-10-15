---
title: 'Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents'
source: Apple ML
url: https://machinelearning.apple.com/research/selection-structured-reasoning
model: claude-code/sonnet
generated_at: '2026-10-15T20:37:52.405125'
score: 100
---

📌 小模型不用寫長篇推理,選選項就好:Apple的SSR框架

TL;DR:Apple提出SSR,把agent推理從生成改成選擇,推理延遲降低逾九成。

多模態搜尋agent每次行動前都要先生成一段推理文字,但對小模型來說,這段文字常常又長又沒什麼用,還拖慢整個agent的反應速度。Apple ML的新研究給出一個反直覺的解法:別讓模型寫推理,讓它選推理。

🤔 小模型的推理,常常是又長又沒用
多模態agent通常會在每個action之前生成freeform(開放式)的推理文字。但對小模型而言,有限的模型容量常常導致生成出來的推理冗長,卻沒辦法為後續的action提供多少有用的引導,同時還會拉高推理成本。

🧩 把「生成推理」改成「選擇推理」
Apple ML提出的Selection-based Structured Reasoning(SSR)框架,把推理重新定義為「選擇」而不是「開放式生成」。具體做法是:把常見的高層次推理預先定義成一組可重複使用的自然語言候選(pre-specified, reusable natural-language candidates)。每一輪,模型會根據目前的context,依據這些候選的likelihood來做選擇,而且不需要額外的輔助任務頭(auxiliary task head)。由於推理候選是事先指定好的,SSR可以用teacher-forced prefilling同時計算候選內部與候選之間的token likelihood,並共用同一個context KV cache,實現平行評分(parallel scoring),取代原本必須逐個生成候選再比較的做法。

📊 推理延遲降低逾九成,成功率仍具競爭力
研究團隊在七個多模態搜尋benchmark上,用2B與4B兩種規模的模型測試SSR,訓練方式涵蓋多種強化學習(RL)目標與監督式微調(SFT)。結果顯示,SSR的平均成功率可以與同規模的領先搜尋agent相競爭,同時把每輪的推理延遲降低超過90%,整題的總推理延遲則降低28%到54%。

💡 把推理瓶頸從「模型容量」轉成「候選設計」
這篇研究點出一個值得留意的方向:當我們把推理看作「從有限候選中挑選」,而不是「自由生成一串token」,小模型因容量不足而寫出冗長無效推理的問題,可以透過結構化、可平行評分的方式繞開,而不必單純依賴堆大模型參數來解決。對於需要在裝置端或資源受限環境執行agent的場景,這種「推理即選擇」的思路,可能比一味追求更長的chain-of-thought更務實。

🎯 實務啟示
如果你正在設計資源受限(2B、4B等級)的多模態搜尋或agent系統,SSR提示了一個可以嘗試的方向:把常見的推理模式先枚舉成候選集合,用likelihood選擇取代生成,一方面能透過共用KV cache做平行評分省下時間,另一方面也避免小模型寫出又長又沒有引導力的推理內容。

🔗 來源
- 標題:Selection-Based Structured Reasoning: Toward Efficient Multimodal Search Agents
- 作者/機構:Feiyu Gavin Zhu、Xiaoyu Zhu、Jiqi Yang、Rui Yang、Arnab Kumar Mondal、Yancheng Wang、Xinke Deng、Jean Oh、Reid Simmons、Joerg Liebelt、Xiang Kong、Zhongyu Jiang(Apple ML,部分作者分別來自Carnegie Mellon University與University of Illinois Urbana-Champaign)
- 連結:https://machinelearning.apple.com/research/selection-structured-reasoning

#AppleML #MultimodalAI #SearchAgents #StructuredReasoning #LLM #ReinforcementLearning #AIAgents #EfficientInference #MachineLearning #EdgeAI
