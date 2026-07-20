---
title: 'From Human-Centric to Agentic Code Review: The Impact of Different Generations
  of Generative AI Technology on Review Quality'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.13196
score: 84
model: tencent/hy3:free
generated_at: '2026-07-20T08:55:26.202168'
---

📌 【研究論文】AI 程式碼審查變快了，但審查品質真的變好了嗎？

TL;DR：百萬筆 PR 實證顯示，AI agent 審查加快決策速度，卻未提升審查品質。

當 LLM reviewer 與 AI agent reviewer 開始和人類並肩審查 pull request（PR），我們直覺認為「又快又準」。但一份橫跨 207 個 GitHub 專案的大規模研究，潑了一盆冷水：效率確實上去了，品質卻沒有。

🤔 **從人類中心到 Agentic 的審查典範轉移**

程式碼審查（code review）能在程式碼合併前維持軟體品質，但對人類審查者負擔沉重。隨著生成式 AI 進入開發流程，審查正從以人為主，轉向人類與 LLM、AI agent 共同參與的型態。然而過去缺乏實證，說明這種轉變如何影響審查效率與品質。

🧩 **用 102 萬筆 PR 建模三個時代的協作序列**

論文分析來自 207 個 GitHub 專案、共 102 萬筆已審查 PR，這些專案經歷了三種審查者組合時代：
- Human-centric review（以人為主）
- LLM-assisted review（LLM 輔助）
- Agentic code review（AI agent 審查）

作者歸納出三種 AI 審查採用實踐：
- Gradual AI Adoption（漸進採用）
- Rapid LLM Adoption（快速採用 LLM）
- Rapid AI Agent Adoption（快速採用 AI agent）

並將 PR 審查討論建模為「審查者互動序列」，用來刻畫人類、LLM、AI agent 在審查過程中的協作方式。

📊 **Agent 主導的協作更快，但品質沒跟上**

結果顯示，在有 agent 參與的協作模式——特別是由 AI agent 發起、或多個 AI agent 共同參與的審查——在漸進採用與快速採用 AI agent 兩種實踐下，都與更快的審查決策相關。

但效率提升並未轉化為更好的審查品質。此外，不論哪個時代，審查活動量與 PR 型別都仍是重要因素；一旦 LLM 與 AI agent 加入，人機協作模式就成為解釋審查效率最強的因子。

⚠️ **效率與品質的脫鉤是核心提醒**

作者指出，這項發現提供實證指引：設計 AI 支援的程式碼審查流程時，應追求效率提升，同時避免削弱審查品質。素材未提及具體品質指標定義與個別基線資料，因此無法進一步量化「品質未提升」的幅度。

🎯 **實務啟示**

對工程團隊來說，匯入 LLM 或 AI agent 做 code review 可以明顯加快合併節奏，但不該誤以為「快」等於「好」。在漸進式匯入並讓 agent 分擔發起審查的情況下，仍須保留人類對品質把關的機制，並監控人機協作模式是否真的兼顧兩者。

🔗 **來源**
- 標題：From Human-Centric to Agentic Code Review: The Impact of Different Generations of Generative AI Technology on Review Quality
- 連結：https://huggingface.co/papers/2607.13196

#CodeReview #LLM #AIAgent #SoftwareEngineering #GitHub #PullRequest #ReviewQuality #ReviewEfficiency #GenerativeAI #EmpiricalStudy
