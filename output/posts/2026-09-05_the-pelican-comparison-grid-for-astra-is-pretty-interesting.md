---
title: The Pelican comparison grid for Astra is pretty interesting
source: Simon Willison
url: https://simonwillison.net/2026/Sep/4/astra-pelicans/
model: claude-code/sonnet
generated_at: '2026-09-05T19:21:39.118324'
score: 67
---

📌 一張騎腳踏車的鵜鶘 SVG，洩漏了 GPT-6 Astra 的身世？

TL;DR：Simon Willison 用經典「鵜鶘騎腳踏車」SVG 測試比較 GPT-6 Astra 與 GPT-5.6 系列，意外看出模型家族間可能的血緣關係。

一張畫得歪七扭八的鵜鶘騎腳踏車 SVG，能透露的東西比你想的多。

🤔 **一個非正式但廣為人知的基準測試**

Simon Willison 長期用「請 LLM 畫一隻騎腳踏車的鵜鶘 SVG」作為非正式的視覺化基準，用最直觀的方式比較不同模型的輸出風格與品質。這次他在拿到 GPT-6 Astra 的存取權後，第一時間就用這個老方法上手測試。

🧩 **五種推理強度、四個模型家族的比較格**

Simon 分別在 low、medium、high、xhigh、max 五種推理強度下（Astra 不支援 reasoning=none）讓 GPT-6 Astra 生成鵜鶘 SVG，再把結果與 GPT-5.6 家族的 Sol、Terra、Luna 一起放進同一張比較格中呈現，方便並排檢視。

📊 **意外發現：Astra 和 Luna 可能比表面上更「親近」**

Simon 在文中提出一個觀察：「I wonder if Astra and Luna are more related to each other than OpenAI let on?」（我懷疑 Astra 和 Luna 之間的關聯，可能比 OpenAI 公開說明的更緊密）。這是他純粹從視覺輸出比較後得到的直覺猜測，而非官方證實的資訊。

💡 **非正式基準的價值：捕捉數字看不到的線索**

這類定性、視覺化的跨模型比較雖然無法量化打分，卻能捕捉官方評測分數看不出來的細節，例如不同模型之間的「家族相似性」，進而讓外部觀察者推測供應商內部可能共享的底層架構或訓練脈絡。

⚠️ 這終究只是主觀的視覺比較，並非嚴謹的效能評測，Simon 自己也只是提出「懷疑」，並未給出定論，讀者不應把這當成確定的技術事實。

🎯 **實務啟示**

在評估或選型 LLM 時，除了看官方公布的 benchmark 分數，花點時間用同一組任務對多個模型做定性、可視化的輸出比較，有時能發現 API 文件或評測報告不會告訴你的產品線索，也有助於判斷供應商的模型策略與版本演進脈絡。

🔗 **來源**
- 標題：The Pelican comparison grid for Astra is pretty interesting
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/4/astra-pelicans/

#GPT6Astra #LLMBenchmark #OpenAI #SimonWillison #SVGGeneration #AIModels #PromptEngineering #ModelComparison #AIResearch #GenerativeAI
