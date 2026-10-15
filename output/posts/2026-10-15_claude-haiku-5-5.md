---
title: Claude Haiku 5.5
source: Simon Willison
url: https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/
model: claude-code/sonnet
generated_at: '2026-10-15T20:47:25.103562'
score: 93
---

📌 【Anthropic】Haiku 5.5 打平對手價格，tokenizer 卻偷偷漲稅

TL;DR：Haiku 5.5 表面價格追平 GPT-6 Luna，但新 tokenizer 讓同一份 prompt 多吃 1.25 倍 token。

🎣 一邊喊著降價，一邊換上更「吃字」的 tokenizer，帳面上的優惠未必是實際到手的優惠。Simon Willison 實測後發現，這次 Anthropic 的定價策略比表面數字複雜得多。

🤔 跟 GPT-6 Luna 正面對決的定價戰

Haiku 4.5 上市將近一年，定價 $1/百萬 input token、$5/百萬 output token，即便在發布當時也不便宜，更是上個月才推出的 OpenAI GPT-6 Luna 的 10 倍價格。新版 Haiku 5.5 直接把價格砍到跟 Luna 一樣：$0.10/$0.50（百萬 token），上限為 100,000 token。超過這個門檻，價格會跳升 5 倍到 $0.50/$2.50。相較之下，Luna 要到 272,000 token 才會漲價，而且只漲到 $0.20/$0.75。

| 模型 | Input（≤100K） | Output（≤100K） | 超過閾值後 |
|---|---|---|---|
| Claude Haiku 5.5 | $0.10/M | $0.50/M | $0.50/$2.50（>100K） |
| GPT-6 Luna | $0.10/M | $0.50/M | $0.20/$0.75（>272K） |
| Claude Haiku 4.5（舊版） | $1/M | $5/M | 不適用 |

結論很直接：workload 若能塞進 100,000 token 以內，Haiku 5.5 價格打平 Luna，且 Anthropic 宣稱 benchmark 分數更高；一旦超過這個門檻，Luna 明顯更划算。

💡 隱藏的漲價：新 tokenizer 更「吃字」

Simon 用自己開發的 Claude Token Counter 工具測試，同一段長 prompt 在 Haiku 5.5 下，耗用的 token 數量大約是 Haiku 4.5 的 1.25 倍。換句話說，即使單位價格打平對手，實際帳單可能因為 tokenizer 效率變差而悄悄墊高，這是只看牌價容易忽略的細節。

📊 Pelican 測試：reasoning 等級的時間與成本

Haiku 5.5 不支援關閉 reasoning，預設為 medium。Simon 用經典的「畫一隻騎腳踏車的鵜鶘」SVG 測試跑過 low、medium、high、xhigh、max 五個等級，除了 low 以外都畫出了不錯的車架。

| Reasoning 等級 | 花費 | 耗時 |
|---|---|---|
| Low | 0.0936 美分 | 7 秒 |
| Max | 3.3826 美分 | 5 分 9 秒 |
| Haiku 4.5（無 reasoning 選項） | 0.7583 美分 | — |

值得一提的是，max 等級的 reasoning trace 一開頭就寫著「This is the classic pelican-on-bicycle SVG test...」，顯示模型已經「認出」這是業界常見的 benchmark 題目。對照一年前的 Haiku 4.5，當時完全不支援 reasoning 等級，畫出來的鵜鶘品質也明顯較差。

💡 Sonnet 5.5 快取降價，訂閱戶多了 API 額度

同一波更新裡，Anthropic 也把 Sonnet 5.5 的 cache read 價格砍半，並宣布從本週起為 Max 與 Team 訂閱戶加發每月 API 額度：Max 5x 用戶 $100、Max 20x 用戶 $200，Team 訂閱戶最高 $500（在團隊內共用）。額度剛好等於訂閱費本身，且不會累積到下個月，用不完就作廢。使用者可以在 Settings → Billing 選擇要套用額度的 API 組織，也能關閉 auto-reload，讓額度用完後 API 直接停止呼叫，避免帳單爆炸。

⚠️ 超過 100K token 要三思

這次更新對小型、短 prompt 的 workload 相對友善，但長 context 的使用情境（例如大量文件分析）反而要留意：Haiku 5.5 超過 100K token 後漲幅是 Luna 的 2.5 倍，加上 tokenizer 本身更吃字，實際成本差距可能比牌價顯示得更大。

🎯 實務啟示

選型時別只看牌價，先用實際 prompt 跑一次 token 計算器，確認 tokenizer 差異不會吃掉表面上的降價優惠；同時評估 workload 是否會頻繁超過 100K token 門檻，再決定 Haiku 5.5 或 GPT-6 Luna 更划算。若已是 Max 或 Team 訂閱戶，記得去 Billing 頁面把每月 API 額度領出來用。

🔗 來源
- 標題：Claude Haiku 5.5
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Oct/7/claude-haiku-5-5/

#Anthropic #ClaudeHaiku #LLMPricing #GPT6Luna #TokenCounter #AIModels #PromptEngineering #LLMBenchmark #APIpricing #AIAgent
