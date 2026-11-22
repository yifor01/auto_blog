---
title: OpenAI’s chief scientist has thoughts on how to limit AI development
source: TechCrunch AI
url: https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/
model: claude-code/sonnet
generated_at: '2026-11-22T22:38:41.550715'
score: 74
---

📌 OpenAI 首席科學家提議：用 perplexity 當 AI 發展的共同速限

TL;DR：Jakub Pachocki 主張以 perplexity（模型預測下一個 token 的準確度）作為跨公司共識的 AI 能力基準，為發展速度設下門檻。

要替 AI 發展設速限，第一個問題不是「要不要減速」，而是「用什麼單位量速度」。這正是 OpenAI 首席科學家 Jakub Pachocki 這篇被 Sam Altman 形容為「OpenAI 近期發表過最重要的內容」的部落格文章想回答的問題。

🤔 **從「我們在拿人命當賭注」到「設一個速限」**

放慢 AI 發展的討論在近期升溫:一位曾任職 OpenAI 與 Anthropic 的研究者稱這些公司是在「拿我們的生命當賭注」，Anthropic 的 IPO 申請文件也提到這項技術可能帶來「對社會的災難性甚至存亡風險」。Anthropic CEO Dario Amodei 隨後提出一份「為前沿設步調」（pace the frontier）的計畫，呼籲各公司就「共同的安全標準，以及對失控 AI 進展速度的限制」達成一致，這份計畫看起來也得到 OpenAI CEO Sam Altman 與 SpaceX CEO Elon Musk 的認同。但問題在於:要設速限，得先有一致的測速方式。

🧩 **為什麼是 perplexity，不是下游能力測驗**

Pachocki 的論點是，聚焦在 AI「下游能力」的 benchmark 會隨技術進步很快過時，而 perplexity 這個「衡量模型平均而言預測下一個 token 有多準、數值越低代表預測越好」的指標，至今仍保持「具參考價值」。他在文章中附了一張圖，呈現 OpenAI 模型自 GPT-3.5 以來 perplexity 持續下降的軌跡，並寫道:「GPT-4，perplexity 約 0.91，已經能有效運用 chain-of-thought 推理，這也促成了後續對這項能力的針對性誘發，進而催生出現代的推理模型。現在，當 loss 降到 0.8 以下，我們在網路安全與數學等領域看到了變革性能力的出現。」

💡 **把 perplexity 當作業界的共同紅線**

依 Pachocki 的構想，perplexity 可以成為「通用智慧的共享 benchmark」，讓各家 AI 公司據此設定「共同限制」:以 perplexity 作為標準化的進度量尺，公司之間可以承諾不超過某個門檻，直到「我們理解與監控 AI 行為的能力達到某個具體里程碑」為止。換句話說，這是把「監控能力是否跟上」設為解鎖下一階段能力的前提,而不是單純比賽把能力做得更強。

⚠️ **目前仍是倡議，不是協議**

文章呈現的是 Pachocki 個人（以及 Altman 似乎認同）的立場陳述，並非已經生效的跨公司協議。要讓 perplexity 真的變成業界共同速限，仍需要其他實驗室跟進採用同一套衡量方式與門檻設計，這篇部落格本身並未提出具體的監督機制或執行細節。

🎯 **實務啟示**

對工程師而言，這場討論的現實意義不在於明天的 API 會不會變慢，而是 perplexity 這個訓練時就在看的老指標，正被嘗試重新賦予「治理工具」的角色。如果這個方向被更多公司採納，未來模型發布的對外溝通裡，perplexity 數值可能會從論文附錄裡的技術細節，變成類似「安全規格」一樣被公開討論的數字，值得留意後續是否有其他實驗室呼應或提出不同量尺。

🔗 **來源**
- 標題：OpenAI's chief scientist has thoughts on how to limit AI development
- 作者／機構：Anthony Ha，TechCrunch AI
- 連結：https://techcrunch.com/2026/11/22/openais-chief-scientist-has-thoughts-on-how-to-limit-ai-development/

#OpenAI #AISafety #Perplexity #AIGovernance #FrontierAI #DarioAmodei #SamAltman #ResponsibleAI #AIPolicy #JakubPachocki
