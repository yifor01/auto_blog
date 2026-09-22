---
title: 'SpaceXAI Releases Grok 4.7: A Larger Base Model at the Same $2/$6 Price as
  Grok 4.6'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/21/spacexai-releases-grok-4-7/
model: claude-code/sonnet
generated_at: '2026-09-22T20:23:47.867192'
score: 92
---

📌 Grok 4.7 同價登場，Terminal-Bench 分數翻近一倍

TL;DR：SpaceXAI 用更大 base model 與更長 RL 訓練推出 Grok 4.7，維持與 4.6 相同的 2 美元/6 美元定價，多項 benchmark 明顯進步但非全面領先。

同樣的價格，換來大幅提升的 coding 與 agentic 表現，SpaceXAI 這次打的是「免費升級」牌。Grok 4.7 已經可以透過 xAI API、Cursor、Grok Build、OpenRouter、Vercel、Cloudflare 呼叫使用。

🤔 **更大的底子，更長的訓練**

Grok 4.7 是 SpaceXAI 針對 coding、agentic 任務與知識工作推出的新旗艦模型，建立在更大的 base model 與更長的強化學習（RL）訓練之上，但售價與速度都維持在 Grok 4.6 的水準。

📊 **跑分全面優於 4.6，但不是每項都拿第一**

發布時的比較表格把 Grok 4.7（xHigh effort）拿去對比 Grok 4.6（High）、GPT-5.6 Sol Max、Fable 5.1 Max（所有分數皆為廠商自報）：

| Benchmark | Grok 4.7 | Grok 4.6 | 備註 |
|---|---|---|---|
| Terminal-Bench 4.0 | 38.0% | 20.3% | 表中最大進步幅度 |
| EEBench | 64.0% | 53.0% | 表中最高分 |
| Harvey 法務 agent benchmark | 19.6% | — | 對比 Fable 5.1 Max 的 6.7% |
| GDPval (xhigh/high Elo) | 1695 | 1605 | 專業知識工作測試 |

Grok 4.7 在每一項對比 Grok 4.6 的指標上都有進步。不過放到更大的競爭格局裡，它並非全面領先：Fable 5.1 Max 在 7 項 benchmark 中拿下 4 項第一，包括 57.9% 的 Terminal-Bench 分數與 1735 的 GDPval Elo；GPT-5.6 Sol Max 則在 DeepSWE v1.1 上以 72.7% 保持領先（Grok 4.7 的 DeepSWE 分數是以 high effort 跑出）。GPT-6 Astra max 的 GDPval 分數為 1542。

💡 **價格才是 Grok 4.7 真正的賣點**

比較貴的對手貴不少：Fable 5.1 Max 的輸入價格是 Grok 4.7 的 5 倍，輸出約 8.3 倍；GPT-5.6 Sol Max 輸入貴 2 倍，輸出約貴 3.3 倍。SpaceXAI 在 CursorBench 4.0 的成本對任務效益圖表中，把 Grok 4.7 定位在價效比前緣。SpaceXAI 也表示 Grok 4.7 在製作文件與簡報上有所提升。

🧩 **安全性與部署細節**

Grok 4.7 搭配全新的安全防護堆疊，SpaceXAI 稱其為目前測試過在拒答與 jailbreak 抵抗力上最強的版本，在 LatchBio 的生物安全 benchmark 拿下 62.4% 的最高分；在 SpaceXAI 自家的 HackerBench v0.3（針對高風險、雙重用途網路安全任務）測試中，只放行了 3.3% 的風險 prompt，官方表示這幾乎不會擋到合法的資安研究工作，並開放特定資安合作夥伴以邀請制方式使用其紅隊能力做防禦研究。

定價維持 $2/百萬輸入 token、$6/百萬輸出 token，Cursor 全方案可用，並是 Grok Build 的預設模型，也開放透過 Grok API、OpenRouter、Vercel、Cloudflare 使用。另有 Grok 4.7 Fast 版本，跑在更快的基礎設施上，輸出速度快兩倍、價格也貴兩倍，但只能在 Cursor 與 Grok Build 使用，不開放公開 API，也不含在 Grok Build 免費方案內。想把推論留在美國境內的話，`https://us.api.x.ai/v1` 這個區域端點會加收 10% 費用。官方也建議設定 `prompt_cache_key` 以確保 cache 命中率。

⚠️ **沒有全面領先，適合誰要看場景**

Grok 4.7 的優勢集中在對 Grok 4.6 的進步幅度與價效比，但在 DeepSWE、GDPval 等指標上，GPT-5.6 Sol Max 與 Fable 5.1 Max 仍分別保有領先，選型時仍需按實際任務對照對應 benchmark。

🎯 **實務啟示**

如果團隊原本就在用 Grok 4.6，這次升級不需要重新評估預算，$2/$6 的定價不變，卻在 Terminal-Bench、EEBench 等 agentic 相關指標上有明顯進步，值得直接換上；若在意的是 DeepSWE 或頂級 GDPval 分數，GPT-5.6 Sol Max、Fable 5.1 Max 仍是對照組，需要按價格與分數一起權衡。

🔗 **來源**
- 標題：SpaceXAI Releases Grok 4.7: A Larger Base Model at the Same $2/$6 Price as Grok 4.6
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/21/spacexai-releases-grok-4-7/

#Grok47 #SpaceXAI #LLM #CodingAgent #AIBenchmark #TerminalBench #AgenticAI #AISafety #ModelRelease #CursorBench
