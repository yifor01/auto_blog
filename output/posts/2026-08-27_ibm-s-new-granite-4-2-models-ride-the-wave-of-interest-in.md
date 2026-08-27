---
title: IBM's new Granite 4.2 models ride the wave of interest in local LLMs
source: Ars Technica AI
url: https://arstechnica.com/ai/2026/08/ibms-new-granite-4-2-models-ride-the-wave-of-interest-in-local-llms/
model: claude-code/sonnet
generated_at: '2026-08-27T17:28:20.763753'
score: 90
---

📌 IBM Granite 4.2 上線：8B、30B 學會用終端機與上網查資料

TL;DR：IBM 最新開源模型全面主打推理能力，128K 原生上下文，中大型版本加入 agentic 訓練。

當地端部署 LLM 的討論愈來愈熱，IBM 選在這個時間點推出開源權重模型家族的最新成員 Granite 4.2。

🤔 **背景：延續開源、可自架的路線**

IBM 這次推出 3B、8B、30B 三種參數規模的變體，延續前幾代的 decoder-only 架構設計，供開發者下載並自行架設。新版本原生支援 128000 token 的上下文長度。

🧩 **8B、30B 多了 agentic 強化學習訓練**

8B 與 30B 兩個版本（3B 沒有）額外經過一段 agentic 強化學習訓練，針對使用終端機、網路搜尋、呼叫外部工具等擴充能力進行訓練。3B 模型雖然也支援工具呼叫，但沒有經過同等程度的專門訓練。

💡 **IBM 自稱這是「推理導向」的一代**

IBM 官方表示,Granite 4.2 是 Granite 語言模型家族中「聚焦推理的一代」。文章特別提醒,業界所說的模型「推理」（reasoning）並非人類意義上有意識地理解問題,而是指功能性的推理,特別是透過 chain-of-thought（思維鏈）,把中間結果一步步帶到後續步驟中。

⚠️ **細節仍有限**

目前公開資訊並未提及具體的基準測試分數或與其他開源模型的效能比較，實際推理能力表現如何，還有待更多評測資料佐證。

🎯 **實務啟示**

如果你正在評估可自架、支援 agentic 工作流程（呼叫終端機、上網、外部工具）的開源模型，Granite 4.2 的 8B/30B 版本值得放進候選清單,並搭配自己的任務進行實測。

🔗 **來源**
- 標題：IBM's new Granite 4.2 models ride the wave of interest in local LLMs
- 作者／機構：Samuel Axon, Ars Technica
- 連結：https://arstechnica.com/ai/2026/08/ibms-new-granite-4-2-models-ride-the-wave-of-interest-in-local-llms/

#IBM #Granite #OpenWeightLLM #LocalLLM #AgenticAI #ReasoningModels #LLM #OpenSourceAI #ChainOfThought #SelfHostedAI
