---
title: 'SWE-Together: Evaluating Coding Agents in Interactive User Sessions'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.29957
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-06-30T20:38:29.009458'
---

📌 SWE-Together：用真實互動紀錄評估 Coding Agent 的多回合編碼基準

TL;DR：基於真實使用者互動建立的新基準，透過 LLM 模擬器評估 AI 編碼代理的正確性與互動效率。

目前的 Coding Agent 評估大多聚焦於「最終結果是否正確」，但忽略了 AI 在與人類協作過程中的互動品質。如果一個 Agent 需要經過無數次低效的來回對話才能修復一個 Bug，即使結果正確，在實務上依然缺乏效率。

🤔 **從單次提交轉向多回合互動評估**

SWE-Together 提出了一套全新的評估框架，其核心在於將評估物件從「單次程式碼生成」轉移到「多回合互動會話」。該基準的資料來源並非合成資料，而是源自真實的使用者與 Agent 之間的互動紀錄，旨在模擬真實開發場景中，AI 如何在連續對話中解決問題。

🧩 **引入 LLM 模擬器評估互動效率**

為了量化 Agent 的表現，SWE-Together 引入了一個反應式 LLM 模擬器（Reactive LLM Simulator）。這個設計讓評估不再僅僅看最終的程式碼是否通過測試，而是綜合考量兩個維度：
- 最終正確性（Final Correctness）：問題是否被正確解決。
- 互動效率（Interaction Efficiency）：達成目標所需的對話回合數與溝通成本。

🎯 **實務啟示：從「能跑」轉向「好用」**

對於開發 Coding Agent 的工程師來說，這意味著最佳化目標應從單純的 Pass@1 提升，轉向降低與使用者的互動成本。一個優秀的 Agent 不應僅能解決問題，更應能在最少的對話回合內精準理解需求並交付結果。

🔗 **來源**
- 標題：SWE-Together: Evaluating Coding Agents in Interactive User Sessions
- 連結：https://huggingface.co/papers/2606.29957

#AI #CodingAgent #LLM #Benchmark #SoftwareEngineering #MultiTurnInteraction #AIProgramming #SWETogether #Evaluation #DeveloperExperience
