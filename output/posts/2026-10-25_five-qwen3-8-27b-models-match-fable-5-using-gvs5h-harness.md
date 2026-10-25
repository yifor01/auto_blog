---
title: Five Qwen3.8-27B models match Fable 5 Using GVS5H Harness
source: Hacker News
url: https://github.com/slee-persis/GVS5H
model: claude-code/sonnet
generated_at: '2026-10-25T19:48:02.663638'
score: 93
---

📌 五個 Qwen3.8-27B 互相開會，跑出比 Claude Fable 5 更高分？

TL;DR：免訓練多實例協作法，讓開源小模型逼近甚至打平旗艦模型表現。

遇到困難的程式題，多數人的直覺是換一個更貴的模型。這篇研究反而讓五個便宜模型的「新鮮實例」互相留言、互相監督，結果分數不輸甚至超過旗艦模型。

🤔 為什麼要這麼做
Frontier級的程式能力，過去幾乎只能靠更大、更貴的closed-weight模型取得。這份研究想驗證：如果不動模型權重、不做額外訓練，只靠推理階段的組織方式，能不能把便宜模型的表現推到frontier等級。

🧩 Ledger-based zero-shot self-orchestration
作者把這套方法稱為ledger-based zero-shot self-orchestration：同一個模型開出多個「新鮮實例」(fresh instances)，負責拆解問題；這些實例透過一個共享檔案系統互相協調，裡面存放plan、notes與目前的solution，全程不需要額外訓練(training-free)。研究團隊在11個開源與閉源模型上，用LiveCodeBench Hard最新100題做測試。

📊 93% pass@1，只花9%成本
- 在pinned backend上，這套方法帶來最高25.6個百分點的提升。
- Orchestrated Qwen3.8 Flash Next達到93.0% pass@1，高於Claude Fable 5的90.4%，成本僅為後者的9%。
- 本地自架的開源權重Qwen3.8-27B，單模型表現從66.8%提升到92.4%。
- 但增益並非對所有模型都成立，部分模型分數不變甚至變差。作者對逐字稿(transcript)的分析認為，增益主要來自「拆解問題」與「跨實例的持久context」這兩點。

⚠️ 一個比較上的但書
作者特別註明，Claude Opus 5的分數是跑在較早版本的scaffold上，透過OpenRouter以單次呼叫完成，而非像其他模型一樣跑五個實例在pinned backend上，兩者條件並不完全對等。

🧩 怎麼跑
專案需要uv與對應模型的API key，在`codebase/v2-current`目錄下設定好環境變數後，用`uv run`搭配`escalation/run_bench.py`執行；`--engine multiagent`跑的是多代理管理模式，`--engine single`則是單次呼叫的baseline，結果會印出pass@1分數並寫進`runs/results.json`。程式碼採MIT授權，論文、圖表與執行數據則是CC BY 4.0，LiveCodeBench fork與benchmark題目維持各自原本的授權。

🎯 實務啟示
在考慮要不要換用更貴的旗艦模型之前，這篇研究提供了另一個槓桿：用便宜模型做推理時的組織（拆解+共享筆記），可能比單純升級模型更划算。但前提是要先在你自己的任務上驗證，因為增益明顯因模型而異，不是所有模型都吃這套。

🔗 來源
- 標題：GVS5H: Five Qwen3.8-27B Models Match Claude Fable 5 on LiveCodeBench Hard
- 作者／機構：rzk（Hacker News）
- 連結：https://github.com/slee-persis/GVS5H

#LLM #MultiAgent #LiveCodeBench #OpenSourceAI #Qwen #CodeGeneration #AIOrchestration #InferenceTimeCompute #ClaudeAI #MachineLearning
