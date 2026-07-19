---
title: elder-plinius/G0DM0D3
source: GitHub Trending
url: https://github.com/elder-plinius/G0DM0D3
score: 85
model: tencent/hy3:free
generated_at: '2026-07-19T08:05:40.305743'
---

📌 【開源專案】G0DM0D3：把多模型聊天介面推向紅隊與認知研究

TL;DR：一款開源、隱私可透視的多模型聊天介面，主打紅隊測試與自由 AI 互動。

當大多數聊天介面在幫你「控管」模型行為時，G0DM0D3 反其道而行：它要的是認知不受控管（cognition without control），並把整套介面開放出來給駭客與研究者拆。

🤔 **為誰打造的解放式 AI 介面**

根據 GitHub README，G0DM0D3 是一套完全開源、隱私可透視（privacy-transparent）的多模型聊天介面，目標受眾是駭客、哲學研究者與系統調校者。它將後訓練層（post-training layer）的邊界推到極限，應用場景鎖定在紅隊測試（red teaming）、認知研究，以及不受限制的 AI 互動。

🧩 **核心設計：並行競速與多層評估**

README 列出幾項關鍵架構與功能設計：

- 多供應商支援：可接 60 個 OpenRouter 列出模型、最多 44 個 Venice 模型，或自架本機模型。
- GODMODE CLASSIC：5 組經實戰驗證的提示詞＋模型組合平行競速，挑出最佳回應。
- ULTRAPLINIAN：跨 5 個層級（12–60 個 OpenRouter 模型）的多模型評估引擎，採複合評分（composite scoring）。
- 本機模型：可透過 Ollama、LM Studio、llama.cpp 或 vLLM 在本機硬體跑 ULTRAPLINIAN。
- Parseltongue：輸入擾動引擎，含 3 個強度層級、共 33 種紅隊技術。
- AutoTune：針對 20 種查詢情境的自適應取樣引數引擎。
- 隱私控制：預設僅收集 metadata 等級的應用遙測，可切到 No-Log 或 Local-only 模式關閉。
- 本機歷史：對話與設定儲存在本機（README 片段至此截斷）。

🎯 **實務啟示**

對做紅隊或模型行為研究的工程師，這套介面把「多模型並行比較」與「輸入擾動」直接做成內建功能，不必自己接多個 API 再寫 orchestration；且本機模式與可關閉遙測的設計，適合在敏感環境下做可控實驗。

🔗 **來源**
- 標題：elder-plinius/G0DM0D3
- 作者／機構：elder-plinius
- 連結：https://github.com/elder-plinius/G0DM0D3

#OpenSource #MultiModel #RedTeaming #ChatInterface #AI #Privacy #LocalModels #PromptEngineering #Cognition #G0DM0D3
