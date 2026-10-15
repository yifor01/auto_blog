---
title: Why do LLM pelicans look like this?
source: Hacker News
url: https://arcfu.com/post/the-emperor-pelican-has-no-clothes/
model: claude-code/sonnet
generated_at: '2026-10-15T20:53:31.634750'
score: 79
---

📌 為什麼 LLM 畫的鵜鶘都長一樣？

TL;DR：從鵜鶘騎單車的 SVG 測試看多樣性崩塌，新 benchmark 量化了 AI 設計創意跟人類的差距。

🎣 把「畫一隻騎腳踏車的鵜鶘」這道題丟給不同的 LLM，照理說應該得到千奇百怪的構圖，可實際收集到的 SVG 卻幾乎長得一個樣，彷彿所有模型腦中共用同一張草稿。

🤔 **一個被忽視的現象：輸出多樣性崩塌**

這篇發表在 Hacker News、獲得 163 points、142 則留言的文章，拿 Simon Willison 長期在跑的「pelican riding a bicycle」SVG 基準（取各次執行中、在最高 reasoning 設定下仍回傳 SVG 的結果）作為切入點，指出不同模型畫出來的鵜鶘高度相似。作者把這稱為「沒人在談的 LLM 多樣性崩塌問題」：模型看起來在解決同一個任務，但創意空間被壓縮到幾乎只剩一種解法。

🧩 **用 Design Creativity Bench 把「創意」量化**

文章引用了 Kombai 團隊發布的 Design Creativity Bench 作為佐證：針對 16 個前沿模型，在兩種不同產品領域下共 80 個開放式 UI 任務中進行評測，並以人類設計師的作品作為參照基準。這個 benchmark 不只看單一輸出品質，而是拆成三個維度：
- **Originality**：同一道題目下，模型的設計跟其他模型的輸出差多少。
- **Creative Range**：產品領域變了之後，模型的設計決策會不會跟著調整。
- **Appropriateness**：生成的 UI 有沒有滿足題目的功能需求。

📊 **人類 92.3 分，最強模型只拿 65.5 分**

| 評測對象 | Creativity Score |
|---|---|
| 人類設計師參照 | 92.3 |
| GPT-6 Astra | 65.5 |
| GPT-6.1 Sol | 63.7 |
| Grok 4.7 | 62.2 |
| Gemini 3.8 Flash | 60.6 |

最佳模型與人類之間仍有超過 25 分的落差，而且這個排名只涵蓋了 16 個模型中的前幾名。

💡 **功能正確，不等於有創意**

把鵜鶘 SVG 的現象與 Design Creativity Bench 的結果放在一起看，可以得到一個共通的訊號：當前的 LLM 在「做出一個可用的東西」這件事上已經相當可靠，但一旦要求的是「跟別人不一樣的做法」，模型傾向收斂到某個看起來安全、常見的解答。這跟多樣性崩塌是同一個問題的兩種表現：鵜鶘 SVG 示範的是同一任務下不同模型之間的構圖收斂，Design Creativity Bench 則是把這種收斂現象在 UI 設計任務上量化成分數。

⚠️ **兩種證據的嚴謹程度不同**

鵜鶘 SVG 的比較偏向案例觀察，素材並未說明總共測試了多少模型、怎麼挑選對照組，嚴謹度不如 Design Creativity Bench 這種有公開 leaderboard、論文與可重現評測框架的研究；兩者放在一起看是合理的佐證，但不該把前者當成嚴格的量化證據。

🎯 **實務啟示**

如果產品需要的是「每次生成都不一樣」的創意輸出（像是設計初稿、素材發想），單靠一次性採樣可能拿到的都是模型最常見的那個答案；可以考慮拉高 temperature、多做幾次採樣，或是引入像 Design Creativity Bench 這類專門衡量多樣性與創意的評測，而不是只看任務有沒有「做完」。

🔗 **來源**
- 標題：Why do LLM pelicans look like this?
- 作者／機構：pcwelder（Hacker News）
- 連結：https://arcfu.com/post/the-emperor-pelican-has-no-clothes/

#LLM #DiversityCollapse #AICreativity #DesignCreativityBench #PromptEngineering #GenerativeAI #UIDesign #Benchmark #SVG #AIResearch
