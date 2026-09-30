---
title: 'OpenAI Releases GPT-6.1 Sol: Near-Astra Coding and Computer Use at One-Fifth
  of Astra’s Token Price'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/30/openai-releases-gpt-6-1-sol-near-astra-coding-and-computer-use-at-one-fifth-of-astras-token-price/
model: claude-code/sonnet
generated_at: '2026-09-30T21:43:47.068218'
score: 88
---

📌 GPT-6.1 Sol：逼近Astra效能，價格剩五分之一

TL;DR：OpenAI 推出 GPT-6.1 Sol，號稱在 agentic coding 與 computer use 上逼近旗艦 Astra，價格卻只要標準版的五分之一。

如果同樣做 agentic coding 的模型，價格直接砍到剩五分之一，對每天要跑上百萬次工具呼叫的團隊來說，這筆帳怎麼算都值得重新盤點一次模型選型。

🤔 **GPT-6家族現在有三個級距**

GPT-6.1 Sol 是 GPT-6 Sol 這個中階模型的升級版，OpenAI 的說法很明確：在 agentic coding、computer use 與專業工作任務上，效果接近旗艦級的 GPT-6 Astra，價格卻只要 Astra 標準輸入與輸出費率的五分之一。目前 OpenAI 一共提供三個級距：GPT-6 Astra 每百萬 token 輸入 10 美元、輸出 50 美元、快取輸入 1 美元；GPT-6.1 Sol 為 2 美元、10 美元、0.10 美元；GPT-6 Luna 則是 0.10 美元、0.50 美元、0.01 美元。

📊 **快取輸入砍半，對agent特別有感**

GPT-6.1 Sol 的快取輸入價格降到每百萬 token 0.10 美元，比 GPT-6 Sol 便宜了 50%；換算下來，快取讀取的費用只剩未快取輸入費率的 5%，低於 GPT-6 Sol 的 10%。這個變化對 agent 工作流特別關鍵，因為 agent 在每一步幾乎都會重新送出同樣的 system prompt、工具schema 與歷史紀錄，快取命中率越高，省下來的成本就越可觀。

💡 **跟對手比價要留意計價基準不同**

以標準第一方 API 牌價（截至 2026 年 9 月 30 日驗證）來看，Claude Sonnet 5.5 的輸入輸出價格跟 Sol 一樣是 2 美元與 10 美元，但 Sol 的快取輸入只要 Sonnet 5.5 的一半價格。Gemini 3.1 Pro 的輸入價格與 Sol 相同，輸出則要 12 美元，且目前仍是 preview 階段。另外 OpenAI 公布的 benchmark 是拿 Sol 跟 Opus 5.5 比較，而非 Sonnet 5.5。值得留意的是，Anthropic 指出自家較新的 tokenizer，針對同一段文字會產生多出約 30% 的 token 數，因此單看牌價並不等於直接的成本比較，OpenAI 也說明競品數字來自公開報告，所有數字都屬廠商自行提供。

🎯 **現在就能用，Ultrafast版本快登場**

GPT-6.1 Sol 已經以 gpt-6.1-sol 之名上線 OpenAI API，並同步進駐 ChatGPT Work 與 Codex。OpenAI 也預告數日內會在 Codex 推出 GPT-6.1 Sol Ultrafast 選項，宣稱 token 產生速度最高可達標準速度的 8 倍。

🔗 **來源**
- 標題：OpenAI Releases GPT-6.1 Sol: Near-Astra Coding and Computer Use at One-Fifth of Astra's Token Price
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/30/openai-releases-gpt-6-1-sol-near-astra-coding-and-computer-use-at-one-fifth-of-astras-token-price/

#OpenAI #GPT6 #LLMPricing #AgenticAI #Codex #CachedTokens #ComputerUse #AICoding #ModelComparison #TokenEconomics
