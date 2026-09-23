---
title: Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war
source: Simon Willison
url: https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
model: claude-code/sonnet
generated_at: '2026-09-23T20:34:24.372398'
score: 98
---

📌 【Anthropic ／ OpenAI 同日發布】Opus 5.5 對決 GPT-6：輸出價砍半才是新常態

TL;DR：Claude Opus 5.5 與 GPT-6 Sol／Luna 同日發布，價格戰全面升溫，工程師該重新盤點模型選型。

短短一天內，Anthropic 和 OpenAI 前後腳發布新模型，真正讓人意外的不是效能，而是價格砍到讓 Grok 原本的「破壞式定價」瞬間變成了主流水準。

🤔 **背景：一天內三場發布**

Simon Willison 在文章中提到，前一天是 Grok 4.7 與 MiMo v2.6 Flash／Pro 發布（他一如既往用「畫一隻騎腳踏車的鵜鶘 SVG」測試各家模型）。今天 Anthropic 發布了 Claude Opus 5.5，大約一小時後 OpenAI 接著發布 GPT-6 Sol 與 GPT-6 Luna。

📊 **價格全面下砍：Luna 只要對手的十分之一**

作者指出，GPT-5.6 Luna 原本就是他最愛用來建構應用的模型，因為效能好又便宜，而 GPT-6 Luna 的價格是 GPT-5.6 Luna 的一半，只要 $0.10／$0.50（每百萬 token 輸入／輸出）；GPT-6 Sol 相對 GPT-5.6 Sol 也有類似幅度的降價。值得注意的是，GPT-5.6 系列原本 11 月就要漲價 25%，所以 GPT-6 的價格等於是那波促銷價再打五折。作者也提到，GPT-5.6 Terra 現在跟 GPT-6 Sol 同價，讓人找不到理由繼續用 Terra。

Grok 4.7 原本定價 $2／$6，已經比 GPT-5.6 Sol 便宜一半以上，但現在 GPT-6 Sol 的輸入價已追平 Grok，輸出價也更接近了。$0.10／$0.50 的 GPT-6 Luna 是 OpenAI 少數幾個最便宜的模型，只有明顯較弱的 GPT-4.1 Nano（$0.10／$0.40，2025 年 4 月）與 GPT-5 Nano（$0.05／$0.40，2025 年 8 月）比它更便宜。

Claude Opus 5.5 把價格從 Opus 5 系列一路沿用的 $5／$25（每百萬輸入／輸出 token）降到 $4／$20，降幅 20%，cache read 的價格更下砍 60%——這對長時間 agentic 對話特別有意義，因為那類場景通常有九成以上的 input token是走 cache read 價格。新的 Opus 5.5 價格恰好等於 GPT-5.6 Sol 降價前的價格，但 OpenAI 已經把 Sol 價格砍半了。GPT-6 Astra 與 Claude Fable 5.1 目前同樣定在 $10／$50，價格戰主要發生在這個級別以下的模型。Anthropic 表示 Sonnet 5.5 與 Haiku 5.5 即將推出，作者特別點出：目前 Haiku 4.5 是 $1／$5，而 GPT-6 Luna 只要它的十分之一，這將是觀察 Haiku 能否重新拿回低價競爭力的關鍵。

💡 **溝通風格改善了，但 max 模式「想過頭」直接卡死**

作者提到，Anthropic 的 Thariq Shihipar 表示 Opus 5.5 是根據使用者對 Opus 溝通風格的回饋做出的調整，號稱 token 效率更好、在各個 effort level 都適用，也對 Blender 操作有加強。

但作者在做他標準的鵜鶘 SVG 測試時，Opus 5.5 在「max」thinking level 下兩次都沒能給出回應——它一直在推理各種細節（腿的長度、齒輪咬合、圖層順序等），直到打到 128,000 token 的最大輸出上限，還沒推理完就被切斷。兩次測試各花費 $2.56、耗時將近 20 分鐘。作者因此懷疑「max」模式在這類任務上可能形同無用，也不敢保證它不會在其他更有意義的工作上同樣「想過頭」而卡死。相對地，Fable 5.1 在 max 模式下沒有過度思考，反而畫出了作者認為目前 Anthropic 模型裡最好的鵜鶘。

🎯 **實務啟示**

作者目前已把 GPT-6 Sol 與 Claude Opus 5.5 設為 Codex 與 Claude Code 裡的預設模型，並把自己的 Datasette Agent demo 升級成使用 GPT-6 Luna，認為它在 SQL 查詢與撰寫 HTML／JavaScript 上速度快且能力足夠。對還在選型的工程師來說，這波降價意味著中低階模型的成本門檻大幅降低；但像 Opus 5.5 的「max」模式踩到輸出上限這種邊界案例，提醒我們選型時仍要用自己實際的工作流測試，不能只看價格或跑分數字。

🔗 **來源**
- 標題：Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/

#ClaudeOpus #GPT6 #Anthropic #OpenAI #LLMPricing #AIModels #PriceWar #GenerativeAI #Grok #DeveloperTools
