---
title: 'CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent
  Economies'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.16613
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:06:44.670451'
---

📌 CoffeeBench：在異質多代理經濟模擬中測試 LLM 的長期決策能力

TL;DR：透過 90 天的經濟模擬環境，評估 LLM Agents 在多代理競爭環境下的獲利能力與溝通模式。

當我們討論 LLM Agents 的能力時，大多數基準測試仍集中在單次任務或短期對話。但如果將 Agents 丟進一個需要長期運作、且必須與其他競爭者互動的經濟系統中，它們還能維持理性決策並最大化獲利嗎？

🤔 **長期決策與異質代理的挑戰**

CoffeeBench 提出了一個全新的評估框架，將 LLM Agents 置於一個異質的多代理經濟模擬（Multi-Agent Economic Simulation）之中。這個環境的核心挑戰在於「長週期（Long-Horizon）」：Agents 必須在長達 90 天的模擬時間內進行互動，而非僅僅完成單次指令。

🧩 **以獲利最大化為目標的經濟競爭**

在 CoffeeBench 的設定中，LLM Agents 扮演的是企業（Firms）角色。其核心運作邏輯如下：
- 目標：在 90 天的模擬期間內，透過與其他企業的互動來最大化利潤。
- 互動機制：不同模型（Models）的 Agents 在同一經濟體系中競爭與協作。
- 評估指標：研究重點在於觀察不同模型在獲利表現上的差異，以及它們在溝通模式（Communication Patterns）上的不同表現。

📊 **揭露模型間的表現差異**

透過此基準測試，研究發現不同模型在面對長期經濟壓力時，展現出顯著的差異。這不僅體現在最終的獲利數字上，更體現在它們如何與其他代理溝通、如何調整策略以應對市場變動的模式中。

🎯 **實務啟示**

對於開發 AI Agent 的工程師而言，CoffeeBench 提醒我們：評估 Agent 的能力不能只看單次任務的成功率，而應關注其在長期、動態且具有競爭性質的環境中，是否能維持策略的一致性與獲利能力。這為開發更具備經濟理性與長期規劃能力的 Agents 提供了量化評估的基準。

🔗 **來源**
- 標題：CoffeeBench: Benchmarking Long-Horizon LLM Agents in Heterogeneous Multi-Agent Economies
- 連結：https://huggingface.co/papers/2606.16613

#LLM #AIagents #MultiAgentSystems #Benchmarking #EconomicsSimulation #LongHorizon #DecisionMaking #CoffeeBench #ArtificialIntelligence #MachineLearning
