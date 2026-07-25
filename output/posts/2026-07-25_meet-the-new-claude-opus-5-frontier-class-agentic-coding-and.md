---
title: 'Meet the New Claude Opus 5: Frontier-Class Agentic Coding and Computer Use
  at Unchanged Opus Pricing'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/24/meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing/
model: tencent/hy3:free
generated_at: '2026-07-25T07:49:05.766589'
score: 80
---

根據您提供的資訊，本文屬於「產業新聞／部落格報導」型別。

📌 【Anthropic 重磅更新】Claude Opus 5 登場：以不變的價格，挑戰代理型編碼與電腦使用能力

TL;DR：Claude Opus 5 取代 4.8 成為旗艦模型，以相同定價展現強大的 Agentic 編碼與電腦使用能力。

Anthropic 正式發布了 Claude Opus 5，這款新模型不僅取代了 Claude Opus 4.8 成為 Opus 等級的旗艦，更在維持原定價格的前提下，大幅提升了在代理型編碼（Agentic Coding）與電腦使用（Computer Use）方面的表現。

🧩 **核心規格與定價保持不變**

Opus 5 目前已成為 Claude Max 的預設模型，並成為 Claude Pro 中最強大的模型。

- 定價：輸入每百萬 token 為 5 美元，輸出每百萬 token 為 25 美元（與前代相同）。
- Context Window：預設與最大皆為 1M tokens，且不提供更小版本的變體。
- 輸出限制：在同步 Messages API 上最大輸出為 128k tokens；透過 Message Batches API（需使用 `output-300k-2026-03-24` beta header）可達到 300k tokens。
- 快取最佳化：可快取的最小 Prompt 從 1,024 tokens 降至 512 tokens。
- 模型 ID：`claude-opus-5`

📊 **Agentic 能力與 Benchmark 表現大幅提升**

Opus 5 在多項衡量代理能力的基準測試中展現顯著優勢，特別是在複雜任務的處理上。

- **OSWorld 2.0**：Opus 5 達到 70.57%，優於 Opus 4.8 的 55.7%。
- **Zapier AutomationBench**：Opus 5 取得 26.0%，超越 Opus 4.8 (17.0%) 與 Fable 5 (17.4%)。在中等難度下，平均每個任務的成本為 0.89 美元。
- **SWE-bench**：
  - 在 SWE-bench Verified 上取得 96.0% 的高分。
  - 在 SWE-bench Pro 上取得 79.2%（Fable 5 為 80.0%）。
  - 在 SWE-bench Multimodal 上，從 38.4% 大幅躍升至 59.4%。
- **FrontierBench v0.1**：在最大努力（max effort）下取得 43.3% 分數（Opus 4.8 為 18.7%）；而在最高難度（xhigh effort）下，平均獎勵（mean reward）達到 44.4%。

💡 **數學推理與安全性表現**

Opus 5 在高難度數學問題與安全性控制上亦有亮點。

- **IMO 2026 數學問題**：在不使用工具或代理架構的情況下，Opus 5 針對所有 6 個 IMO 2026 問題生成的 24 個解法，經由三模型評審團判定皆為正確。
- **安全性與拒絕率**：在 API 呼叫中，Opus 5 的安全性分類器標記並拒絕了 5% 的呼叫（涵蓋 4% 的測試案例）；相比之下，Fable 5 的分類器標記率則高達 42%（涵蓋 26% 的測試案例）。

🎯 **實務啟示**

對於需要處理複雜工作流（Workflow）或自動化任務的工程師而言，Opus 5 提供了一個高價效比的選擇。它在維持原有定價的同時，大幅強化了在視覺與電腦操作層面的代理能力，對於開發自動化 Agent 應用程式具有極高的實務價值。

🔗 **來源**
- 標題：Meet the New Claude Opus 5: Frontier-Class Agentic Coding and Computer Use at Unchanged Opus Pricing
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/24/meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing/

#AI #Anthropic #ClaudeOpus5 #AgenticAI #MachineLearning #LLM #Coding #ComputerUse #SoftwareEngineering #AIModels
