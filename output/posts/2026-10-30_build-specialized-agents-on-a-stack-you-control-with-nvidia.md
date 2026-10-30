---
title: Build Specialized Agents on a Stack You Control with NVIDIA NemoClaw
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/build-specialized-agents-on-a-stack-you-control-with-nvidia-nemoclaw/
model: claude-code/sonnet
generated_at: '2026-10-30T21:42:17.442777'
score: 88
---

📌 【NVIDIA 開放方案】NemoClaw：在你自己掌控的技術堆疊上建置專用 Agent

TL;DR：NemoClaw 不是新的 agent harness，而是把模型最佳化、觀測工具與安全執行時包裝進你現有的 harness。

多數團隊以為打造 agent 要在「直接用前沿 agent」與「從零自建」之間二選一。NVIDIA 的 NemoClaw 想說的是，你其實可以用自己已經在用的 harness，疊上一套開放、可擁有、可客製的完整堆疊。

🤔 **生產環境的 agent 需要四件事**

一個 agent 需要一個能推理的模型、一個定義如何運作的 harness、延伸能力的工具與技能，以及一個能治理 agent 在生產環境中能存取與執行什麼的執行時（runtime）。當 agent 要碰真實的企業系統與資料時，光是「能力夠強」還不夠，還要「安全可控」。NemoClaw 針對這個落差提供標準做法，目前支援三種開放 harness：能存取檔案與應用、寫程式碼、產生子 agent 並維持跨 session 上下文的 OpenClaw；來自 Nous Research、會把團隊修正過的工作模式沉澱成可重用技能的 Hermes Agent；以及結合規劃、檔案式上下文管理、記憶與子 agent 委派的 LangChain Deep Agents。

🧩 **四個元件組成一套開放堆疊**

NemoClaw 本身不是競爭的 harness，也不是執行時，而是一組 blueprint，在開發者選定的 harness 上組裝出完整堆疊。每個 NemoClaw blueprint 結合四個元件：一個針對 NVIDIA Nemotron 調校過的開放 harness（Hermes Agent、LangChain Deep Agents 或 OpenClaw）；Nemotron 開放模型；用於觀測與改善 agent 執行的 NVIDIA NeMo 工具（包括 NeMo Relay，以及能改善吞吐量、成本與可靠性的路由能力）；以及治理 agent 存取檔案、網路、憑證與工具的安全執行時 NVIDIA OpenShell。

模型與 harness 的協同最佳化之所以重要，是因為兩者不匹配時，agent 可能重複要求上下文、提早停止，或原地打轉沒有進展。文中舉了一個例子：LangChain 針對 Nemotron 3 Ultra 調校 Deep Agents harness，只調整 prompt、工具與中介層，沒有重新訓練模型，就讓 Nemotron 3 Ultra 達到接近前沿模型的效能，每次執行成本卻比領先的封閉模型低約 10 倍。這套調校直接打包進對應的 NemoClaw blueprint，任何用 LangChain Deep Agents 搭配 Nemotron 3 Ultra 的開發者都能直接取用，不必重複調校工作。

| 項目 | Agent Harness | NemoClaw Blueprint |
|---|---|---|
| 是什麼 | 管理 agent 如何用工具、維持上下文、執行任務的軟體 | 結合支援 harness、模型、最佳化工具與執行時的參考堆疊 |
| 提供什麼 | 工具、技能、記憶、orchestration | 調校過的 harness、模型、最佳化工具、OpenShell 執行時控管 |
| 何時使用 | 打造並客製 agent 的行為 | 組裝並在開放堆疊上運行 agent，附帶模型/harness 最佳化與執行時治理 |

NemoClaw 社群儲存庫裡有一個以 Hermes 打造的「記憶驅動幕僚長（Chief of Staff）」範例：agent 持續維護一份人類可讀的模型，記錄接觸過的人、專案、優先事項與工作模式，不必每次任務都從零重建上下文。在這個範例中，OpenShell 治理 agent 對檔案系統、process 與網路的存取，並把用於受管推理與 MCP 連線的憑證留在沙箱之外，即使 agent 的記憶或檢索到的上下文把它導向非預期行動，仍受政策約束；NeMo Relay 則原生整合進 Hermes session，在新 session、reset 或過期等真實 session 邊界關閉 trace span，並匯出執行軌跡供稽核與後續最佳化。

⚠️ **治理不是附加選項**

每個 NemoClaw 參考架構都包含 OpenShell，用來在 agent harness 與工具周圍加上安全性與政策強制，治理模型可以採取的行動。官方教學示範了如何建立第一個政策以防止資料外流到 GitHub，更複雜的 OpenShell 政策則能治理 agent 跨多個內部工具、站點與溝通管道的連線。

🎯 **實務啟示**

NemoClaw agent 可以跑在雲端、資料中心、NVIDIA DGX Spark 以及 RTX PC／工作站上，同一套堆疊可以同時服務醫院的臨床 agent 與電子設計自動化的模擬 agent，只是換上不同的工具與技能。它也能與前沿 agent 協作：Claude、Codex 或 Cursor 可以把特定領域的子任務委派給跑在開放模型與自有基礎設施上的 NemoClaw 專用 agent。如果你已經在用 OpenClaw、Hermes Agent 或 LangChain Deep Agents，不需要重寫 agent 本身，就能透過對應的 NemoClaw blueprint 補上模型最佳化、觀測與執行時治理。

🔗 **來源**
- 標題：Build Specialized Agents on a Stack You Control with NVIDIA NemoClaw
- 作者／機構：Nicola Sessions（NVIDIA Developer）
- 連結：https://developer.nvidia.com/blog/build-specialized-agents-on-a-stack-you-control-with-nvidia-nemoclaw/

#NVIDIA #NemoClaw #AgenticAI #Nemotron #OpenSource #LangChain #AIGovernance #LLMOps #EdgeAI #OpenModels
