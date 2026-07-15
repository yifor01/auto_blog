---
title: 'Proactive Agent Research Environment: Simulating Active Users to Evaluate
  Proactive Assistants'
source: Apple ML
url: https://machinelearning.apple.com/research/proactive-agent-research-environment
score: 100
model: tencent/hy3:free
generated_at: '2026-07-15T08:09:21.905908'
---

📌 【Apple ML】Pare：模擬主動使用者評估助理

TL;DR：Pare 以有限狀態機模擬使用者，助工程師評測主動式 AI 助理。

🎣 **評測框架假設錯了，主動助理難進步**
現有的 AI 助理評測框架，大多把應用程式視為一連串扁平的工具呼叫 API。但真實世界的使用者操作是有狀態、有先後順序的——這道鴻溝讓「主動預測需求」的代理人遲遲難以進步。

🤔 **扁平 API 建模，捕捉不到真實互動狀態**
主動代理人（proactive agents）能預測使用者需求並自主執行任務，極具數位助理潛力。然而現有方法將 apps 建模為扁平 tool-calling API，無法呈現數位環境中狀態導向（stateful）與順序性的使用者互動，導致逼真使用者模擬不可行，阻礙發展。

🧩 **應用程式即有限狀態機，啟用主動模擬**
論文提出 Proactive Agent Research Environment (Pare)，一個建構與評估數位環境中主動代理人的框架。Pare 將應用程式建模為 finite state machines（有限狀態機），具備 stateful navigation（狀態導航）與 state-dependent action space（狀態依賴動作空間）供使用者模擬器（user simulator）使用，從而實現 active user simulation（主動使用者模擬）。

📊 **Pare-Bench：143 項任務涵蓋四類 App**
基於 Pare，作者釋出 Pare-Bench 基準，包含 143 個多樣任務，橫跨 communication、productivity、scheduling、lifestyle 四類應用程式。該基準設計用於測試四項能力：context observation（上下文觀察）、goal inference（目標推論）、intervention timing（介入時機）、multi-app orchestration（多 App 協調）。

🎯 **對工程師：可重現地評測「主動」行為**
過去要評估助理何時該出手、如何跨 App 協作，缺乏標準環境。Pare 與 Pare-Bench 提供了一個以狀態機為核心的模擬場域，讓開發者能在受控設定下觀察代理人是否真的理解使用者脈絡並適時介入，而非僅被動回應指令。

🔗 **來源**
- 標題：Proactive Agent Research Environment: Simulating Active Users to Evaluate Proactive Assistants
- 作者／機構：Deepak Nathani, Cheng Zhang, Chang Huan, Jiaming Shan, Yinfei Yang, Alkesh Patel, Zhe Gan, William Yang Wang, Michael Saxon, Xin Eric Wang（UC Santa Barbara、Independent Researcher、University of Washington、Apple 等）
- 連結：https://machinelearning.apple.com/research/proactive-agent-research-environment

#ProactiveAgents #Pare #UserSimulation #FiniteStateMachine #Benchmark #LLM #DigitalAssistant #AppleML #AgentEvaluation #StatefulInteraction
