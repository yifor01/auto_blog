---
title: DeepSeek Just Released V4.1-Flash-1017, Scores 77.0 on DeepSWE, Opens Search
  API
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/17/deepseek-just-released-v4-1-flash-1017-scores-77-0-on-deepswe-opens-search-api/
model: claude-code/sonnet
generated_at: '2026-10-17T19:31:27.826045'
score: 93
---

📌 DeepSeek V4.1-Flash 再推新 checkpoint，DeepSWE 衝到 77.0 分

TL;DR：DeepSeek 更新 V4.1-Flash checkpoint 並開放 Search／Fetch API，一組 Key 就能串接 coding agent 與網路搜尋。

同一代模型又出新版本，這次 DeepSeek 不只是換個 checkpoint,還順手把自家的網路搜尋引擎開放給所有開發者用——對正在搭 agent 的工程師來說,這代表少裝一套第三方 search API。

🤔 **一個月內的第二次迭代，主打「帕累托改善」**

DeepSeek-V4.1-Flash-1017 是 V4.1-Flash 的最新 post-training checkpoint，已經在 DeepSeek 網站、App 與 API 全面上線，服務名稱仍是 deepseek-flash。DeepSeek 表示相較於 9 月發布的 V4.1-Flash，新版本分數更高、任務完成更快、輸出也更短，官方稱之為效能與成本上的「帕累托改善」（Pareto improvement）。

🧩 **MoE 架構搭配 RL self-feedback，瞄準端到端專案任務**

根據 V4.1-Flash 技術報告，這是一個多模態 Mixture-of-Experts 模型，共 40 層 Transformer，拆分為 20 層的 causal encoder 與 20 層的 decoder。DeepSeek 團隊表示 V4.1-Flash-1017 採用強化學習搭配 self-feedback 來處理端到端的專案型任務,範例涵蓋從遊戲製作到 3D 建模。這個版本針對 DeepSeek Harness、Tencent CodeBuddy 與 WorkBuddy 做了調校,官方建議搭配 DeepSeek Harness v0.2.1-rc.1 以上版本使用。

📊 **DeepSWE 領先，但 Claude Opus 5 仍守住部分戰場**

以下分數均為 DeepSeek 官方自報數字：Terminal-Bench 4.0 在 Claude Code 環境下測試，DeepSWE 在 Mini-SWE-V2 環境下測試，ZeroBench-main 採用 Pass@5 計分。1017 checkpoint 在 DeepSWE（77.0 分）、Automation-Bench、Agents' Last Exam 與 Apex Bench 上都取得領先；不過 Claude Opus 5 在 Terminal-Bench 4.0、ProgramBench、NL2Repo 與 HLE 上仍維持優勢。

💡 **開放 Search／Fetch API：把網路層也變成基礎設施**

這次更新同步開放的 Search API 會回傳排序後的網頁搜尋結果,Fetch API 則能把單一頁面轉成 Markdown 格式回傳。DeepSeek 表示其自建搜尋引擎每天服務數億次請求,這代表開發者不必再額外串接第三方搜尋服務,就能讓 agent 具備即時網路存取能力,等於用同一組 API Key 同時拿到模型推理與網路層。

🎯 **怎麼接：相容端點與定價**

模型可透過 OpenAI 或 Anthropic 格式的端點以 deepseek-flash 呼叫。計價方面，尖峰時段每 1M cache-miss input tokens 收費 0.30 美元,每 1M output tokens 收費 1.20 美元,離峰時段則是半價。對已經在用 DeepSeek 生態系（Harness、CodeBuddy）的團隊,這是一次低摩擦的升級,也值得評估把獨立的 search API 供應商換成 DeepSeek 原生方案。

🔗 **來源**
- 標題：DeepSeek Just Released V4.1-Flash-1017, Scores 77.0 on DeepSWE, Opens Search API
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/17/deepseek-just-released-v4-1-flash-1017-scores-77-0-on-deepswe-opens-search-api/

#DeepSeek #LLM #CodingAgent #MixtureOfExperts #SearchAPI #AgenticAI #OpenAPI #SoftwareEngineering #ModelUpdate #AIInfrastructure
