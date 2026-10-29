---
title: 'Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index
  v5'
source: Hacker News
url: https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1
model: claude-code/sonnet
generated_at: '2026-10-29T22:03:32.041418'
score: 90
---

📌【Google DeepMind】Gemini 4 Carbon 登頂智慧指標，但寫程式仍輸 Claude Opus 5.5

TL;DR：第三方評測機構 Artificial Analysis 的數據顯示，Gemini 4 Carbon 奪下智慧指標第一，但 coding agent 排名仍落後 Claude Opus 5.5。

一個模型同時拿下「全站最聰明」和「coding agent 第二強」,代表的不是全面碾壓，而是一張值得細看的能力地圖。

🤔 **背景：Gemini 4 Carbon 是誰**

根據 Artificial Analysis 的報告，Google 的 Gemini 4 Carbon 已成為 Artificial Analysis Intelligence Index v5 的新任第一名，在 Coding Agent Index 上也僅次於 Claude Opus 5.5。和前代 Gemini 4 Argon 上線時一樣，Carbon 目前只開放給部分使用者，尚未公開供所有人使用，Google 提供 50% 的上線折扣，且未訂出結束日期；文中所有圖表與數據皆以標準定價計算。

📊 **9 項評測贏 4 項，但 coding 與知識工作還不是第一**

在高推理模式（high reasoning）下，Gemini 4 Carbon 在 Intelligence Index v5 的 9 項評測中拿下 4 項第一：HLE-Diamond、Terminal-Bench-Science、AA-Omniscience、AutomationBench-AA，整體分數為 59。其他項目則是明顯進步但未登頂，尤其是在 coding 與知識工作類別。

| 評測項目 | Gemini 4 Carbon (high) | 對照模型 |
|---|---|---|
| Intelligence Index v5 | 59（第 1） | — |
| AA Coding Agent Index（Antigravity CLI） | 59 | Claude Opus 5.5 / Claude Code（max）62，第 1 |
| Terminal-Bench 4.0 | 64%，第 2 | Claude Opus 5.5（max）56% |
| FrontierCode v1.1 | 51%，第 2 | Claude Opus 5.5（max）56% |
| AA-Briefcase（Elo） | 1609 | Gemini 4 Argon（high）1483；Grok 4.7（xhigh）1638；Muse Wonder（max）1659；Kimi K3.1 Pro 1678 |
| AA-Omniscience v1.1 | 54 | Claude Opus 5.5（max）48；Gemini 4 Argon 46 |

報告特別指出，Google 過去在 coding agent 領域表現相對弱勢，這次 Terminal-Bench 4.0 與 FrontierCode v1.1 都排到第二、僅次於 Claude Opus 5.5，算是明顯的進步。

💡 **幻覺率上升到 11%，但依舊是指標中數一數二低**

在 AA-Omniscience v1.1 上，Gemini 4 Carbon 得分 54，比 Claude Opus 5.5（max，48）高 6 分，比自家前代 Argon（46）高 8 分；正確率來到 58%，比 Argon 高出 10 個百分點。但幻覺率也從 Argon 的 4% 上升到 11%，雖然仍是目前評測中第二低（僅次於 Argon），對照 Claude Opus 5.5（max）與 GPT-6 Astra（max）都是 50% 的幻覺率，Carbon 的表現依然突出,只是比起上一代確實有所取捨。

在知識工作類別的 AA-Briefcase 評測中，Carbon（high）拿下 1609 Elo，比 Argon（high，1483）提升 126 分，但仍落後 Grok 4.7（xhigh，1638）、Muse Wonder（max，1659）與 Kimi K3.1 Pro（1678）。其中最大的進步來自 Presentation 子項，提升 293 Elo 來到 1598，Analytical Quality 也提升 120 分來到 1671。

📊 **成本效率：比 Opus 5.5 便宜，但比 GPT-6 Astra 貴一些**

以標準定價計算，Gemini 4 Carbon 每個 Intelligence Index 任務成本為 7.76 美元，比 Claude Opus 5.5（max，10.04 美元）便宜約 23%，但比 GPT-6 Astra（max，6.25 美元）貴約 1.2 倍。它平均每個任務使用 12.3 萬個輸出 token，比 Claude Opus 5.5（max，17.3 萬）少 29%。在與 Argon 相同的 4/20 美元標準定價下，Carbon 的每任務成本（7.76 美元）與 Argon（7.68 美元）相近，但 Intelligence Index 分數高出 9 分。模型本身上下文視窗為 100 萬 token，支援文字、圖片、影片與語音輸入，輸出為文字；快取輸入 token 享有 95% 折扣，標準定價下每百萬 token 只要 0.20 美元。

🎯 **實務啟示**

挑選模型時，「智慧指標第一」不等於「所有任務都該換這個模型」。如果你的工作負載以 coding agent 或知識型工作流為主,Claude Opus 5.5 和部分競品在對應指標上仍領先；但若著重整體推理能力、成本效率與相對低的幻覺率，Gemini 4 Carbon 目前的性價比值得納入評估,尤其是在限時折扣期間。實際導入前，建議用自己團隊的任務類型小規模跑一輪基準測試,而不是只看單一綜合指標排名。

🔗 **來源**
- 標題：Gemini 4 Carbon is the new #1 on the Artificial Analysis Intelligence Index v5
- 作者／機構：Artificial Analysis（Hacker News 討論由 theHocineSaad 提交）
- 連結：https://artificialanalysis.ai/articles/gemini-4-carbon-new-number-1

#Gemini #GoogleDeepMind #LLM #Benchmark #ArtificialAnalysis #AIAgents #ModelComparison #CodingAgent #IntelligenceIndex #AIResearch
