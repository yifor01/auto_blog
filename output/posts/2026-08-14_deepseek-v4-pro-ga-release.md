---
title: DeepSeek-V4-Pro GA Release
source: DeepSeek
url: https://api-docs.deepseek.com/news/news260813
model: claude-code/sonnet
generated_at: '2026-08-14T07:37:08.891730'
score: 63
---

📌 DeepSeek-V4-Pro 正式發布:Agent 能力升級,離峰 API 價格砍半

TL;DR：DeepSeek-V4-Pro 正式 GA,主打 Agent 能力升級、彈性推理強度,並導入離峰半價的 API 計費。

如果你正在用 API 大量跑 agent 任務,DeepSeek 這次的更新可能直接影響帳單——它把 API 定價拆成了尖峰與離峰兩種費率。

🤔 **Agent 能力升級,但沒有具體數字佐證**

DeepSeek 今日發布 DeepSeek-V4-Pro,官方表示這次帶來「Agent 能力的重大升級」,並宣稱有明顯的生產環境效益提升(原文為「strong production gains」),但未附上具體量化數據。

🧩 **三段式推理強度、原生支援 Responses API**

V4-Pro 與 V4-Flash 都支援彈性推理強度設定:low 適合簡單任務、high 適合日常 agent 工作流程、max 適合複雜任務。此外,兩者也原生支援 OpenAI Responses API,並針對 Codex 做了最佳化,提供一鍵設定。V4 Pro 目前已上線 App／網頁版,可透過「Expert Mode」使用,同時也開放 API 存取,模型名稱維持不變。

📊 **離峰價砍半,8/16 生效**

隨著 V4 系列發布,DeepSeek 同步調整 API 定價,導入尖峰與離峰兩種費率:離峰時段價格較尖峰低 50%,讓使用者能更彈性地排程工作負載。新定價將於 2026 年 8 月 16 日 16:00 UTC 生效。

⚠️ **公告偏產品發布,技術細節付之闕如**

這次官方公告性質偏向產品發布,並未提供模型架構、參數規模、訓練細節或具體 benchmark 數字,「strong production gains」等說法目前也缺乏量化佐證可供評估。

🎯 **實務啟示**

如果你的 pipeline 中有不需要即時回應的批次任務(例如批次分類、離線報告生成),可以評估把工作排程移到離峰時段,直接省下一半 API 成本;而 Responses API 與 Codex 的原生整合,對已在使用 OpenAI 生態工具鏈的團隊,遷移門檻可能較低。

🔗 **來源**
- 標題:DeepSeek-V4-Pro GA Release
- 作者/機構:DeepSeek
- 連結:https://api-docs.deepseek.com/news/news260813

#DeepSeek #LLM #AIAgents #APIPricing #Codex #OpenAI #ReasoningModels #GenerativeAI #ModelRelease #AIInfrastructure
