---
title: Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war
source: Simon Willison
url: https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/
model: claude-code/sonnet
generated_at: '2026-10-01T22:08:56.161880'
score: 86
---

📌 Claude Opus 5.5 對上 GPT-6 Sol/Luna：LLM 價格戰再升級

TL;DR：Anthropic 與 OpenAI 同日發布新模型，API 價格又砍了一輪，開發者的選擇成本正在重新洗牌。

昨天是 Grok 4.7 和 MiMo v2.6 的發布日，今天 Anthropic 推出 Claude Opus 5.5，大約一小時後 OpenAI 緊接著發布 GPT-6 Sol 與 GPT-6 Luna。部落客 Simon Willison 在第一時間做了實測比較，結論很直接：這幾天發生的事，比起技術突破，更像是一場價格戰的開打。

🤔 **半價再半價，便宜到不講道理**

Simon Willison 提到，GPT-5.6 Luna 原本就是他做應用開發時最愛用的模型，因為效能好又便宜。沒想到 GPT-6 Luna 的價格是前代的一半，GPT-6 Sol 相對 GPT-5.6 Sol 也有類似幅度的降價。更值得注意的是，GPT-5.6 系列原本在 11 月有預告中的 25% 漲價計畫，這代表 GPT-6 的現行價格，實際上只是 GPT-5.6 促銷價的一半而已。

📊 **一張表看懂目前的價格帶**

以下整理文章中明確提到的模型定價（每百萬 tokens，輸入／輸出，美元）：

| 模型 | 輸入 | 輸出 | 備註 |
|---|---|---|---|
| GPT-6 Luna | $0.10 | $0.50 | OpenAI 史上最低價模型之一 |
| GPT-4.1 Nano（2025/4） | $0.10 | $0.40 | 僅次於 GPT-6 Luna |
| GPT-5 Nano（2025/8） | $0.05 | $0.40 | OpenAI 史上最低價 |
| Grok 4.7 | $2 | $6 | 輸入已追平 GPT-6 Sol |
| Claude Haiku 4.5 | $1 | $5 | 尚未更新至 5.5 版 |
| Claude Opus 5.5 | $4 | $20 | 較前代 Opus 系列降 20% |
| GPT-6 Astra | $10 | $50 | 與 Claude Fable 5.1 同價 |
| Claude Fable 5.1 | $10 | $50 | 與 GPT-6 Astra 同價 |

文中也特別點出，GPT-5.6 Terra 的舊價格恰好等於新版 GPT-6 Sol 的價格，意味著繼續使用 Terra 已經沒有理由；而 Grok 4.7 原本以 $2/$6 打出低價定位，如今輸入端已經被 GPT-6 Sol 追平，輸出端差距也縮小了。Opus 5.5 的新價則正好等於 GPT-5.6 Sol 調降前的舊價，只是 OpenAI 已經把 Sol 的價格再腰斬一次。

💡 **Opus 5.5 的另一個亮點：cache 讀取降價 60%**

除了標準定價下降 20%，Opus 5.5 的 cache read 價格降了 60%。Simon Willison 指出，這對長時間的 agentic 對話特別關鍵，因為這類場景中超過九成的輸入 tokens 都是以 cache 價格計算的，實際成本下降幅度會比表面的 20% 更明顯。Anthropic 方面也表示 Sonnet 5.5 與 Haiku 5.5 即將推出，但以目前 Haiku 4.5（$1/$5）對比 GPT-6 Luna（$0.10/$0.50，整整十分之一價格）來看，低價位這一層的競爭會更激烈。

⚠️ **"max" 思考模式不一定可靠**

Simon Willison 在他慣用的「畫一隻騎腳踏車的鵜鶘 SVG」測試中，發現 Opus 5.5 在 "max" 思考等級下竟然沒能產出結果。模型陷入過度推理，一路規劃鵜鶘的喙、腿部角度、踏板細節，最終撞上 128,000 tokens 的輸出上限，還沒畫完就被截斷，重試一次結果相同，兩次測試各花費 $2.56、耗時近 20 分鐘。他因此懷疑 "max" 模式在面對簡單任務時可能會「想太多想到當機」，連帶對它處理複雜任務的穩定性打上問號。相對地，Fable 5.1 在 max 模式下沒有過度思考，產出了他認為是目前 Anthropic 模型中最好的鵜鶘圖。

🎯 **實務啟示**

對於正在用 API 堆應用的工程師來說，這輪降價意味著：原本因為成本考量被迫妥協效能的場景，現在可能有更便宜且更強的選項可換。但同時也要留意新模型在特定推理設定下的穩定性，例如本文揭露的 Opus 5.5 "max" 模式的輸出上限問題，建議在正式導入前針對長輸出、高推理需求的任務做壓力測試，而不是只看定價表就直接切換。Simon Willison 自己已經把 GPT-6 Sol 和 Claude Opus 5.5 設為 Codex 與 Claude Code 的預設模型，並將 Datasette Agent demo 換成 GPT-6 Luna。

🔗 **來源**
- 標題：Claude Opus 5.5, GPT-6 Sol, GPT-6 Luna, and a new price war
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/22/opus-and-sol-and-luna/

#Anthropic #OpenAI #ClaudeOpus #GPT6 #LLMPricing #AIAgents #ClaudeCode #Codex #LLM #AIIndustry
