---
title: Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k
source: Hacker News
url: https://systima.ai/blog/claude-code-vs-opencode-token-overhead
score: 79
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T09:09:04.049910'
---

📌 Claude Code 與 OpenCode Token 消耗對比：前者單次請求多出 2.6 萬個 Token

TL;DR：實測顯示 Claude Code 的快取策略與框架 Token 消耗遠高於 OpenCode，單次請求開銷差距顯著。

當開發者開始將 Agentic Coding 工具整合進工作流時，最直接的體感差異往往不是產出品質，而是 API 帳單跳錶的速度。

🤔 **從直覺到資料：為什麼 Token 消耗速度如此之快？**

作者 systima 在使用過程中發現一個反直覺現象：在被迫從 OpenCode 切換到 Claude Code 的一段時間內，Token 使用量計量表上升的速度明顯快得多。為了驗證這個直覺，作者進行了一項小規模研究，在 AI 程式碼工具與 Anthropic 的端點（endpoint）之間加入日誌記錄，直接捕捉所有請求及其回傳的 usage 區塊。

📊 **Claude Code 請求開銷遠高於 OpenCode**

根據捕捉到的實證資料，兩者在讀取 prompt 之前的 token 消耗（overhead）存在巨大差異：

- Claude Code：在讀取 prompt 前會先傳送 33k 個 tokens。
- OpenCode：相同情境下僅傳送 7k 個 tokens。

研究結果明確指出，Claude Code 在快取策略（cache strategy）以及工具框架（harness）的 token 使用效率上，明顯低於 OpenCode。

🎯 **實務啟示**

對於極度在意 API 成本或在大規模專案中頻繁呼叫 AI Agent 的工程師來說，工具的「框架開銷」是隱形成本。在使用這類 Agentic 工具時，除了關注模型能力，應留意工具本身的快取機制如何影響 token 消耗，因為即使是相同的 prompt，不同工具的封裝方式可能會導致數倍的成本差異。

🔗 **來源**
- 標題：Claude Code sends 33k tokens before reading the prompt; OpenCode sends 7k
- 作者／機構：systima
- 連結：https://systima.ai/blog/claude-code-vs-opencode-token-overhead

#AI #ClaudeCode #OpenCode #TokenUsage #LLM #CostOptimization #Anthropic #AgenticCoding #SoftwareEngineering #API
