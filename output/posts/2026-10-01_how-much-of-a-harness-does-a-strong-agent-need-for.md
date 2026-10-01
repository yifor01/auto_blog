---
title: How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?
source: Apple ML
url: https://machinelearning.apple.com/research/harness-autonomous-ml-engineering
model: claude-code/sonnet
generated_at: '2026-10-01T21:59:51.306665'
score: 101
---

📌 強模型用簡單Harness就夠，複雜編排反而多餘

TL;DR：Apple與EPFL消融實驗顯示，精心設計的multi-agent harness對自主MLE任務沒有優勢。

自主機器學習工程（MLE）agent 近年在公開排行榜上進展亮眼，業界的直覺反應是把 harness（agent 的執行架構）越做越複雜：多 agent 編排器、專用的檢索子 agent、層層疊加的機制。一篇來自 Apple 與 EPFL 研究者的新論文，卻用系統性的消融實驗挑戰了這個直覺。

🤔 **複雜編排 vs 極簡 coding agent，沒人比較過**

論文指出，現代 MLE agent 常因長時程任務上的進展停滯、以及 LLM 原始能力（primitives）有限，而被部署在越來越精巧的機制之上。相對地，讓 LLM 直接透過 read、write、bash 這三個基本操作存取執行環境的「極簡 harness coding agent」雖然也在進步，卻鮮少被拿來系統性比較。

🧩 **同樣的時間預算、同樣的 backbone，比出真正的差異**

研究團隊設計了一套大規模的系統性消融實驗：在相同的時間預算、相同的前沿 LLM backbone 條件下，比較開源的 SOTA harness 與單一 session 的極簡 harness coding agent baseline。

📊 **複雜機制層在這個場景下變得多餘**

結果是：在相同時間預算與相同 backbone 下，開源 SOTA harness 相較極簡 harness coding agent baseline 並沒有展現優勢。換句話說，真正決定表現的主要因素是 LLM backbone 本身，而不是包在它外面的編排機制。研究團隊據此主張，在 coding agent 的設定下，多 agent 編排器、專用檢索子 agent 這類機制層變得冗餘。

💡 **把心力花在打磨 harness 上，報酬可能不划算**

論文的結論很直接：針對目前的 MLE benchmark，在強模型外面精心打造手工 harness 所投入的心力，換來的報酬有限。這對整個「agent 工程」領域是個值得警惕的訊號——當大家忙著堆疊 orchestrator、retrieval subagent 時，真正該優先投資的,可能仍是 backbone 模型本身的能力。

⚠️ **結論限定在目前的 MLE benchmark 情境**

論文作者明確把結論框定在「目前的 MLE benchmark」範圍內，這意味著隨著任務類型或評測方式演變，複雜 harness 是否依然多餘，仍有待後續驗證。

🎯 **實務啟示**

在投入資源建構多 agent 編排、專用子 agent 之前，不妨先做一次對照實驗：在相同時間預算與相同模型下，單一 session、僅具備 read/write/bash 原始能力的極簡 coding agent 表現如何。如果兩者打平，省下來的工程複雜度與維運成本，可能比多一層編排機制更有價值。

🔗 **來源**
- 標題：How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?
- 作者／機構：Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé／EPFL；Apple
- 連結：https://machinelearning.apple.com/research/harness-autonomous-ml-engineering

#AIAgents #MLEngineering #LLM #Apple #EPFL #AgentHarness #AutonomousAgents #AblationStudy #CodingAgent #MachineLearning
