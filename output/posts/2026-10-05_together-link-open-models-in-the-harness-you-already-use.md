---
title: 'Together Link: open models in the harness you already use. Start with one
  command today.'
source: Together AI
url: https://www.together.ai/blog/together-link-frontier-quality-open-models-in-the-harness-you-already-use
model: claude-code/sonnet
generated_at: '2026-10-05T23:22:10.084205'
score: 86
---

📌 一行指令切換開源模型,Coding Agent 帳單砍半

TL;DR：Together Link 讓 Claude Code 等既有工具直接接上開源模型,省下一半以上費用。

工程團隊每月在 coding agent 上燒掉數萬到數百萬美元,原因往往不是任務難,而是每個任務——不管是改一行字還是整包重寫——都丟給同一個頂規閉源模型處理。Together Link 想解決的正是這種「用大砲打蚊子」的浪費。

🤔 **開源模型已經追上來了**

Coding agent 如今是工程團隊的標配,但不分任務難度都跑同一個 premium 模型,成本很快失控。Together AI 指出,像 Kimi K3、GLM 5.3 這類開源模型已經能處理許多最難的程式任務,價格只是閉源模型的一小部分;而 GLM 5.3 Flash、DeepSeek V4.1 Flash 這類輕量模型則足以應付日常的程式任務。

🧩 **接進你本來就在用的工具,不用改習慣**

Together Link 支援 Claude Code、Claude Desktop、Codex（ChatGPT app 與 CLI）、OpenCode 與 Pi。設定與登入方式維持原樣,不需要學新東西,要切回原本的閉源模型也只要一道指令。安裝方式是執行:

```
curl -fsSL https://link.together.ai/install | bash
```

執行後 agent 開啟方式跟平常一樣,只是底層連到了 Together AI,使用的是你自己的 Together AI API key（需先註冊帳號取得）。

🧩 **「Auto」模式:依任務難度自動路由**

Together AI Router 提供「Auto」模式,讀取每個 session 的第一個任務內容,決定送去哪個模型:簡單修正交給快速、低成本的模型,困難問題則交給具備 frontier 能力的模型。如果你帶了自己的 Anthropic key,路由會在 Opus 5.5 與 GLM 5.3 之間選擇;沒有的話則在 GLM 5.3 與 GLM 5.3 Flash 之間選擇。路由判斷只在每個 session 開始時執行一次,因此 prompt caching 的效益不受影響。

📊 **每個 session 都看得到省了多少**

Together Link 提供 per-session 的費用追蹤器,直接對照「如果整段 session 跑在 Opus 5.5 上要花多少錢」。計費走你原有的 Together API key,可用 serverless pay-as-you-go 或 credit packs,不需要另外簽約。Together AI 表示,其 serverless 推論基礎設施就是開發者在 OpenRouter 上已經在選用的同一套,截至 2026 年 9 月 30 日,Together AI 在 OpenRouter 上承載 DeepSeek V4.1 Flash 40.8%、GLM 5.3 Flash 28.2%、Kimi K3 23.1% 的 token 流量份額。

⚠️ **省多少因任務組合而異**

「省下 50% 以上」是 Together AI 自家的整體宣稱,實際節省幅度取決於團隊任務難度分布——簡單任務佔比越高,路由到輕量模型的效益自然越明顯。

🎯 **實務啟示**

如果你的工程團隊已經在用 Claude Code 或 Codex,且對逐月攀升的模型帳單有感,Together Link 的切換成本看起來很低:一道安裝指令、既有的工作流程不變、隨時可以切回原廠模型。值得先在小範圍團隊試跑幾個 session,實際比對費用追蹤器給出的節省數字再決定是否全面推行。

🔗 **來源**
- 標題：Together Link: open models in the harness you already use. Start with one command today.
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/together-link-frontier-quality-open-models-in-the-harness-you-already-use

#TogetherAI #OpenModels #CodingAgent #ClaudeCode #LLMRouting #CostOptimization #GLM #DeepSeek #KimiK3 #DevTools
