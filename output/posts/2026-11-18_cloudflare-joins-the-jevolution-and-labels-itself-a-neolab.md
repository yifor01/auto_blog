---
title: Cloudflare Joins the Jevolution and Labels Itself a Neolab
source: Latent Space
url: https://latent.space/p/cloudflare/
model: claude-code/sonnet
generated_at: '2026-11-18T23:45:22.509120'
score: 87
---

📌 Cloudflare 自稱「neolab」，兩週做出一款 System One 模型

TL;DR：Cloudflare 推出 Clef 與 Clairic 兩款 System One 模型，並把自己定位成「neolab」，用來降低對外部模型的依賴風險。

一家年營收破 30 億美元、剛公布史上最佳財季的上市公司，會自稱是研究導向的 AI 新創「neolab」嗎？Cloudflare 的 AI Platform 產品負責人 Michelle Chen 在 AI Engineer Code Summit 上，就是這樣介紹自家最新的兩款模型。

🤔 **Neolab 原本不是這個意思**

Neolab 一詞由 The Information 的 Stephanie Palazzolo 在去年 11 月提出，原指「新一代、研究導向的 AI 新創」。AI 投資人 Deedy Das（Menlo Ventures 合夥人）維護的 neolab 名單中，收錄了 Thinking Machines Lab、Poolside，以及 TypeSafe AI（在該名單中名列前 20）。Das 認為 neolab 的共同特徵是：僱用頂尖研究員、投入大量運算（通常用於訓練自己的模型)、沒有明顯的營收成長，且多為募資龐大的新創公司。

照這個定義，Cloudflare 幾乎一項都不符：它是上市公司，而且剛公布「本季是公司史上最好的一季」（CEO Matthew Prince 語），年化營收突破 30 億美元，當季營收 7.82 億美元，年增 39%。文章也直言，Cloudflare 把自己稱作 neolab，某種程度上是在挑戰這個詞原本的定義。

🧩 **從基礎設施、運算、儲存，走到「自己做模型」**

Chen 在演講中把這個轉變描述成自然演進：Cloudflare 從基礎設施起步，擴展到運算（Workers 平臺，現在也支援 agent）、儲存，再到在 Workers AI 上提供 Kimi、GLM、DeepSeek 等開源權重模型，最後走到自己訓練模型。

Cloudflare 目前推出了兩款 System One 模型：Clef 是一款決策模型，直接受 TypeSafe AI 的 Jev 模型啟發；Clairic 則是 Cloudflare 自己發明的新類型，官方稱之為「extraction 模型」。Chen 透露，Clef 其實就是 Jev 的複製品，Cloudflare 只花了兩週就做出來，相對於 TypeSafe AI 當初花了兩年打造 Jev——她特別強調這是對 TypeSafe AI 的讚美,因為後者「真正去攻克了這個全新的空間」，而 Cloudflare 做的只是在已經知道 API schema 長什麼樣子之後快速跟進。

System One 模型的核心賣點，是把原本要送進 LLM 的工作，改用更小、更快的模型處理，輸出以毫秒計算而非秒計算，不必每個請求都丟給一個完整的 LLM。

💡 **Clairic 要解決的是「答案就在那裡，LLM 卻猜錯」**

Clairic 上個月發佈，被稱為「System One extraction 模型」這個新類別的第一款模型。它的任務是從非結構化輸入中，直接萃取、計算、估計或預測出數值。Chen 舉的例子是發票上的訂單編號：由於 LLM 是 autoregressive（自迴歸）架構，面對這類任務容易產生幻覺，甚至回傳格式錯誤的 JSON——即使答案清清楚楚寫在輸入裡，LLM 有時還是會猶豫「是三號，還是四號，還是五號」。Clairic 則用同樣的 System One 原則，在單次前向傳播（one forward pass）中直接輸出一個型別化的數值。

Chen 也透露，Cloudflare 的路線圖不會止步於 System One 模型，團隊也在實驗 reasoning 模型與其他 LLM，但重心會放在「post-training」而非從零開始的 pretraining——「我不覺得那是我們的重點,但我認為我們可以拿現有的資源,把它做得更有效率、更有效果」。

⚠️ **自建模型，也是一種風險管理**

Chen 提到，自己做模型是在為 Cloudflare 的 AI 業務「derisk」：Jev 是閉源的，萬一供應端有變動,Cloudflare 無法自行運行；中國開源模型存在潛在的法規風險；而許多模型實驗室也想透過授權費獲利,未來授權可能變貴。這些都是促使 Cloudflare 走向自建模型的現實考量。

🎯 **實務啟示**

對正在評估「要不要什麼都丟給 LLM」的工程團隊，Cloudflare 的 System One 思路值得參考：先盤點你的流程裡有哪些任務其實不需要完整 LLM 的推理能力（像是結構化資料萃取、簡單決策分類），改用更小、更快、更可控的模型處理，可能比無差別呼叫大模型更划算，也更不容易被單一供應商綁住。

🔗 **來源**
- 標題：Cloudflare Joins the Jevolution and Labels Itself a Neolab
- 作者／機構：Latent Space
- 連結：https://latent.space/p/cloudflare/

#Cloudflare #Neolab #SystemOneModels #AIInfrastructure #WorkersAI #ModelExtraction #AIAgents #EdgeComputing #LLMAlternatives #AIStrategy
