---
title: 'Article: The Evolution of Agentic Harnesses: From Chains to Graph to Code'
source: InfoQ.com
url: https://www.infoq.com/articles/agentic-ai-architecture-harness-evolution/
model: claude-code/sonnet
generated_at: '2026-10-27T21:40:37.733415'
score: 83
---

📌 Agent 架構三部曲:從鏈、圖到可執行程式碼

TL;DR:InfoQ 文章點出 agentic LLM 系統的架構演進:Chain → Graph → Code-executing harness。

同樣是「讓 LLM 自己完成任務」,底層的 harness(執行框架)設計卻經歷了一次明顯的架構轉向,從線性串接走向會執行程式碼驗證結果的系統。

🤔 背景:Agent 系統的執行骨架怎麼演進

InfoQ 這篇文章(作者 Karthik Ramgopal)指出,agentic LLM 系統的發展經歷了從線性的 prompt chain(提示鏈),到 graph-based workflow(圖形化工作流),再到近期的 code-executing harness(可執行程式碼的框架)三個階段。

🧩 三種架構各自的特點

文章對三個階段的特性做了簡潔的對比:
- Chain(鏈):結構最簡單,但也最脆弱,一旦某一步出錯,整條鏈容易連帶失敗。
- Graph(圖):在鏈的基礎上加入分支、重試與驗證機制,讓流程能根據中間結果做決策,而不只是單向往下走。
- Code harness(程式碼執行框架):透過實際執行程式碼來驗證輸出結果,而不只是依賴模型自身的判斷。

💡 深入分析:驗證方式的本質轉變

把這三個階段放在一起看,核心轉變在於「如何確認 agent 的輸出是對的」。Chain 幾乎沒有驗證機制,流程走到哪算到哪;Graph 開始引入結構化的分支與重試邏輯,讓系統有機會在出錯時自我修正;Code harness 則更進一步,把「驗證」這件事交給可執行的程式碼本身去檢查結果是否正確,而不是單純信任模型的輸出。這個方向與目前業界常見的「讓 agent 寫程式碼、跑測試、看結果」的做法是一致的。

⚠️ 限制

由於這篇文章提供的素材相當精簡,目前僅能確認三個階段的定性描述,文章後續是否提供具體案例、效能比較或實作建議,還需要參考原文完整內容才能進一步評估。

🎯 實務啟示

如果你正在設計或選型 agent 框架,這個三階段的分類提供了一個簡單的檢查點:先確認你的系統屬於哪個階段,再判斷是否需要往「用程式碼執行驗證輸出」的方向升級,尤其是在任務本身有明確、可程式化驗證的正確答案時(例如程式碼是否通過測試),code-executing harness 的設計思路通常比純粹依賴模型自我回報的鏈式或圖式架構更可靠。

🔗 來源
- 標題:The Evolution of Agentic Harnesses: From Chains to Graph to Code
- 作者/機構:Karthik Ramgopal, InfoQ
- 連結:https://www.infoq.com/articles/agentic-ai-architecture-harness-evolution/

#AI #AgenticAI #LLM #SoftwareArchitecture #AIAgents #CodeExecution #WorkflowAutomation #PromptEngineering #AIEngineering #InfoQ
