---
title: '[AINews] Jensen Is Back! and OpenAI Shows Its Pretraining Curve, joined by
  Microsoft'
source: Latent Space
url: https://latent.space/p/ainews-jensen-is-back-and-openai-shows-its-pretraining-curve-joined-by-microsoft/
model: claude-code/sonnet
generated_at: '2026-11-25T01:47:54.358811'
score: 80
---

📌 黃仁勳回歸，OpenAI 公開五年預訓練曲線

TL;DR：Nvidia CEO 復職同日，OpenAI 首度公開 GPT-3.5 至今的 perplexity 曲線並倡議產業共訂發展上限。

兩則看似不相關的新聞擠在同一天：一位剛被請辭的 CEO 十一天後又被請回來；一家公司把過去被視為「機密智慧財產」的內部指標直接攤在陽光下。兩件事湊在一起，反而讓人更清楚看懂這波 AI 競賽真正在比什麼。

🤔 **董事會的戲碼：黃仁勳十一天後回任**

根據 Latent Space 的 AINews 彙整，Nvidia 董事會在黃仁勳辭職十一天後，一致通過讓他重新擔任 CEO、總裁與董事會成員，過程中還有美國財政部長與總統介入董事會會議提供意見。現任 CFO Colette Kress 留任，獨立董事的調查仍在進行，黃仁勳的參議院聽證會也還有 8 天就要登場。Nvidia 同時成立了一個專責國家安全與出口管制的董事會委員會。Matt Levine 的觀察被引用指出：先解僱又復職的操作，等於讓調查委員會在證據齊全前就已經被迫接受一個預先決定好的結果。

🧩 **OpenAI 把 perplexity 曲線攤開來**

OpenAI 首席科學家 Jakub Pachocki 在〈Perplexity and Intelligence〉一文中，公開了從 GPT-3.5 到現在、在內部固定held-out程式碼資料集上量測的 base model log-perplexity（數值越低代表模型對下一個 token 越不意外，也就是能力越強）。

📊 **幾個關鍵數字**

- GPT-3.5 約 0.99，GPT-4 約 0.91。
- 當模型來到約 0.76（GPT6 Astra）時，大量開放數學難題開始被快速攻破。
- Pachocki 推估下一次能力跳躍會發生在 0.68 到 0.70 之間，並預期 2026 年會有一波明顯加速，2027 年可能出現類似數學領域的「雪崩」。
- Microsoft 在取得 OpenAI 許可後，用同一套評測跑自家 MAI-2 Base，回報 0.819，落在 GPT-5.6 Sol base model 的區間；Mustafa Suleyman 建議未來跨實驗室比較改用 bits-per-byte。
- 內部有一個尚未發布、分數已低於 GPT-6.2 Astra 的模型，一組估計用內部模型 0.732 對照已發布模型 0.761 外推，推算 2027 年 1 到 3 月間會跌破 0.70。

💡 **公開數字背後的倡議：產業自律上限**

Pachocki 的論點不只是秀數字，而是提議產業先訂出第一道共同發展上限，並明確定義要滿足什麼條件（例如下一代 chain-of-thought 監控方法）才能跨過這道線。Sam Altman 引用這個提案，將其連結到白宮 AI Accords 中的標準承諾；Greg Brockman 強調對齊研究的進展恐怕跟不上預訓練的加速；Mark Chen 稱這些數字過去屬於「敏感智慧財產」，並呼籲其他實驗室也公開自家關鍵指標。

⚠️ **質疑聲浪：這個指標真的能拿來訂規則嗎**

多位研究者提出方法論上的疑慮：不同實驗室的 tokenizer 差異可能讓這套共同上限對 OpenAI 有利而對 Anthropic不利；post-training 可能佔掉超過 75% 的 FLOPs，意味著預訓練 perplexity 未必是正確的進度指標；曲線陡降的一部分可能來自模型生成資料在預訓練語料中比例增加；缺乏模型規模與算力數據，也很難區分這是規模效應還是演算法進步。OpenAI 方面回應稱評測集是固定且排除模型生成程式碼的，但外部研究者仍持續要求公開這份 held-out 資料集；Anthropic 則被指出在其 METR 報告中隱去了預訓練指標，引發進一步要求公開的聲音。

🎯 **對工程師的意義**

無論這套「共同上限」最終能否成真，公開 perplexity 曲線本身，等於把過去各實驗室各說各話的「能力到底進步多快」變成了可以互相對照的數字。對工程師而言，這是觀察前沿模型能力拐點、評估下一代模型是否值得等待或換線的一個具體訊號，但也要留意上述幾個方法論上的保留條件，不要把單一指標當成全部真相。

🔗 **來源**
- 標題：[AINews] Jensen Is Back! and OpenAI Shows Its Pretraining Curve, joined by Microsoft
- 作者／機構：Latent Space
- 連結：https://latent.space/p/ainews-jensen-is-back-and-openai-shows-its-pretraining-curve-joined-by-microsoft/

#Nvidia #JensenHuang #OpenAI #Pretraining #Perplexity #AIGovernance #Microsoft #ChainOfThought #FrontierModels #AIPolicy
