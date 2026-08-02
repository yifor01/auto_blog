---
title: Qwen’s Former Lead on What Hybrid Thinking Got Wrong — and Why He Now Backs
  Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/04/qwens-former-lead-on-what-hybrid-thinking-got-wrong-and-why-he-now-backs-agents/
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:33:14.958099'
---

📌 【前 Qwen 技術領袖觀點】從訓練模型轉向訓練 Agent：Hybrid Thinking 的挑戰與未來

TL;DR：Qwen 前技術領袖 Junyang Lin 揭露 Hybrid Thinking 實作難點，並主張 AI 進化路徑將從「訓練模型」轉向「訓練 Agent」。

當我們習慣於在「快速回應」與「深度推理」之間做選擇時，業界試圖將兩者整合為 Hybrid Thinking（混合思考模式），但這在技術實作上是否存在根本性的衝突？

🎣 **從模型家族演進到單一行結論**

Alibaba Qwen 專案的前技術領袖 Junyang Lin 在其演講「Qwen: Towards a Generalist Model / Agent」中，回顧了 Qwen 家族的發展歷程。在介紹過 QwQ-32B、Qwen2.5-Max、Qwen3、Qwen2.5-VL 與 Qwen2.5-Omni 等模型及其對比 DeepSeek-R1、Grok 3 Beta、Gemini 2.5 Pro 及 OpenAI o-series 的效能後，整場演講以一句話收尾：「Training models $\rightarrow$ training agents」。

🧩 **Qwen3 的核心設計：混合思考與動態預算**

在 Qwen3 的詳細介紹中，Lin 提出了 Hybrid Thinking 的設計理念，旨在讓模型具備兩種模式：
- **思考模式 (Thinking mode)**：用於逐步推理 (step-by-step reasoning)。
- **非思考模式 (Non-thinking mode)**：用於提供近乎即時的回應。

此外，Qwen3 引入了「動態思考預算 (Dynamic thinking budgets)」，允許呼叫者設定模型推理的上限。在語言支援方面，Qwen3 將支援範圍從 29 種擴展至 119 種語言與方言。

📊 **模型規模與架構細節**

Qwen3 提供了從 0.6B 到 235B 參數的不同規模，並以 Apache 2.0 協議釋出 GGUF、GPTQ、AWQ 與 MLX 等量化格式。其架構設計分為兩類：
- **小型 Dense 模型**：綁定輸入與輸出 Embedding，支援 32K 上下文。
- **大型 Dense 與 MoE 模型**：取消 Embedding 綁定，將上下文擴展至 128K。
- **MoE 機制**：在 128 個專家中，每個 token 僅啟用 8 個專家。

💡 **Hybrid Thinking 的實作困境**

雖然在簡報中 Hybrid Thinking 看起來是一個簡潔的功能，但 Lin 在隨後的詳細文章中坦言，實際建構過程非常困難。他指出，「思考模式 (thinking mode)」與「指令模式 (instruct mode)」在訓練方向上是相互拉扯的 (pull in opposite directions)，這使得在單一模型中平衡兩者成為一大挑戰。

🎯 **實務啟示：未來重心在於環境回饋**

Lin 的結論明確指出，未來的開發重心將從單純的模型訓練轉向 Agent 訓練。這意味著接下來的技術突破將聚焦於：
- 增加更多預訓練量。
- 匯入具備「環境回饋 (environment feedback)」的強化學習 (RL)。
- 擴展更長的上下文與更多模態 (modalities)。

對於工程師而言，這暗示了單純提升模型參數或推理能力已不足夠，如何讓模型在與環境互動中學習（Agentic workflow），將是下一階段的關鍵。

🔗 **來源**
- 標題：Qwen’s Former Lead on What Hybrid Thinking Got Wrong — and Why He Now Backs Agents
- 作者／機構：Michal Sutter / MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/04/qwens-former-lead-on-what-hybrid-thinking-got-wrong-and-why-he-now-backs-agents/

#Qwen #LLM #AI #Agent #HybridThinking #MoE #MachineLearning #Reasoning #Alibaba #DeepLearning
