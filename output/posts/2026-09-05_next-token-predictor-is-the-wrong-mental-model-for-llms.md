---
title: “Next-token predictor” is the wrong mental model for LLMs
source: Hacker News
url: https://gmcgoldr.github.io/2026/09/04/llm-next-token-predictors.html
model: claude-code/sonnet
generated_at: '2026-09-05T19:14:22.664740'
score: 83
---

📌 「next-token predictor」只講對了 LLM 的外形，沒講到它學到了什麼

TL;DR：把 LLM 說成只會猜下一個字，忽略了它也能從 RLVR 探索中學到新東西。

幾乎每個人都聽過「LLM 只是在預測下一個 token」這句話，聽起來像是給這整套技術澆了一盆冷水。不過這篇部落格文章認為，這句話只對了一半，而且是不重要的那一半。

🤔 predict next token 這個說法，對預訓練模型是成立的

作者先承認，說 LLM 是 next-token predictor 並不算錯，這個描述有真實的根據。Transformer 語言模型確實以自迴歸（autoregressive）方式逐個吐出 token：不斷把已生成的 token 餵回去，取樣出下一個。預訓練的訓練迴圈，概念上就是不斷拿一段既有 token，看真實語料裡接下來出現的是哪個 token，然後讓模型更傾向於取樣出那個 token。文章強調關鍵一點：預訓練階段，每一個「真正的下一個 token」都來自訓練資料裡已經存在的既有序列。所以基底模型（base model）確實可以說是在預測訓練資料中會出現的下一個 token。

🧩 RLVR：模型開始向自己探索出的序列學習

但我們實際使用的 LLM 不只是 base model，而是經過後訓練（post-training）的版本，其中一個關鍵環節是「帶可驗證獎勵的強化學習」（RLVR, reinforcement learning with verifiable rewards）。文章指出兩種訓練迴圈的本質差異：預訓練只從訓練資料裡已經存在的序列學習；RLVR 則是讓模型自己生成全新的序列，再根據這些序列的結果來學習。也就是說，同樣一個「讓某個 token 更容易被取樣」的更新動作，在預訓練裡是因為那個 token 出現在訓練資料中，在 RLVR 裡則是因為包含這個 token 的探索序列獲得了高分獎勵。模型依然保有「一次吐一個 token」的外形，但它不再只靠模仿既有文字學習，也透過自己的探索學到新東西。

💡 用西洋棋來看這個差異更清楚

文章用兩個假想的西洋棋系統做類比。第一個系統只在大量特級大師對局資料庫上訓練，學到特級大師在不同棋局下傾向下哪一步，本質上就是一個「下一步預測器」。第二個系統是一個理想化的棋類引擎，窮舉探索過所有可能的對局，從中得知每個棋局狀態下獲勝的機率，面對新局面時，它選的是通往最高勝率的那一步，而不是模仿任何特級大師的既有棋譜。把第二個系統稱為「下一步預測器」會顯得很奇怪，因為它追求的根本不是預測資料集裡接下來會出現哪一步，而是選出能贏的那一步。作者也簡短提到，人類回饋強化學習（RLHF）雖然沒有在文章中深入展開，但同樣讓模型從單純模仿整個預訓練資料，轉向模擬一個「樂於助人的助理」，而 RLVR 則讓模型能進一步探索、學到訓練資料裡從未出現過的想法。

🎯 實務啟示

對工程師來說，這篇文章提醒的重點是：同一套「逐 token 生成」的機制外形，底下可能編碼著完全不同的東西，既可能是對訓練語料的模仿，也可能是透過探索學到的、資料裡本來不存在的策略。評估或選用一個模型時，單純把它當成「下一個字的統計機器」去理解其行為，可能低估了後訓練（尤其是 RLVR）帶來的能力，這也是為什麼作者主張要換一個心智模型來看待 LLM。

🔗 來源
- 標題："Next-token predictor" is the wrong mental model for LLMs
- 作者／機構：garrinm（Hacker News 投稿，原文作者 gmcgoldr）
- 連結：https://gmcgoldr.github.io/2026/09/04/llm-next-token-predictors.html

#LLM #MachineLearning #RLVR #ReinforcementLearning #AIAlignment #DeepLearning #NLP #Transformers #PostTraining #MentalModels
