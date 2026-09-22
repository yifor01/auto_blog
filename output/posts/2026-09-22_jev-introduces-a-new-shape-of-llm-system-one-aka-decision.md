---
title: Jev introduces a new shape of LLM—System One, aka Decision Models
source: Simon Willison
url: https://simonwillison.net/2026/Sep/21/jev/
model: claude-code/sonnet
generated_at: '2026-09-22T20:23:47.867092'
score: 94
---

📌 Jev：不回你文字，只丟一個浮點數的新型 LLM

TL;DR：TypeSafe AI 推出 Jev，把 LLM 輸出換成機率分數，定價只算輸入 token。

如果一個模型不回答你任何一個字，只回一個浮點數，你還敢說它是 LLM 嗎？TypeSafe AI 上週發布的 Jev，就是這麼一個反直覺的東西，而它引發的討論熱度，讓 Simon Willison 特地寫了一篇文章來拆解。

🤔 **一種新形狀的模型：System One，或者說決策模型**

TypeSafe 把 Jev 稱為「System One models」，Simon Willison 則認同 Maggie Appleton 的說法，覺得「decision models（決策模型）」是更好的命名。Jev 依然接受文字輸入，但輸出不再是文字，而是對應到分類、是非題、評分與信心分數的浮點數。TypeSafe 自己的形容是：把它想成一個「前沿智慧等級的 function call」——丟進非結構化的 state，吐出有型別的機率決策。

🧩 **怎麼用：一個 state 物件配上幾個問題**

使用方式是組出一個「state」物件，內容可以是一個字串、字串陣列，或一組 name-value pairs，用來描述一篇文章、一位客戶或任何一筆紀錄。接著把這個 state 連同一個或多個問題送進 API，每個問題都會得到各自的回覆。Jev 支援三種類型的問題，而且問題是平行評估的，所以丟很多題目跟丟一題花的時間差不多。

定價上，Jev 只針對輸入收費，輸出完全免費，第一代模型的輸入價格是每百萬 token 0.042 美元，比 OpenAI GPT-5 Nano 的 0.05 美元還便宜。

📊 **強項與弱項：Jev 1.13 的 jaggedness 文件說了什麼**

官方的 Jev 1.13 jaggedness 文件坦承，Jev 目前不擅長處理數字、日期，以及「adversarial content（對抗性內容）」。它適合的是能表達成分類任務的工作，例如垃圾郵件偵測、建議標籤、優先順序排序。Simon 自己也拿它做搜尋 reranking 實驗：先用 BM25 這類便宜演算法抓出 100 個候選結果，再讓 Jev 針對原始查詢逐一評分相關性。

💡 **比 LLM 更黑箱：只給分數，不給理由**

Simon 對 Jev 感到不太自在的一點是，它比一般 LLM 更往黑箱機器學習系統倒退。一般 LLM 至少還能要求它解釋自己的判斷（即使解釋不保證準確），但 Jev 連這一步都省了：丟進再多文字，拿回來的就只有一個浮點數。如果 Jev 把某段內容判成 spam，到底是哪個訊號觸發的，完全無從得知。這也讓偏見問題變得格外重要，Simon 特別提到千萬別拿 Jev 去替求職者排名，那個浮點數背後可能藏著模型未被察覺的偏見，事後要拆解出來會很棘手。他自己做過一個實驗，讓 Jev 對舊金山灣區每個城市回答「是不是 Good city？」的是非題，結果 Cupertino 排最高、East Palo Alto 排最低。

⚠️ **便宜到能跑上千次實驗，但也代表評測不能少**

正因為這些疑慮，evals 與結構化實驗在 Jev 專案裡比一般 LLM 專案更重要。好在 Jev 夠便宜，跑個幾百甚至幾千次實驗性 prompt 也只要幾分錢，這讓大規模驗證變得可行，只是能不能真的去做，取決於團隊有沒有把這一步排進流程。

🎯 **實務啟示**

Jev 釋出還不到一週，社群已經出現大量創意應用，也出現了用開放權重模型仿造 Jev 的專案：Kev 用 Qwen 3.5 打造出 0.8B、4B、9B 三種規模的版本，還有專門比較「Jev-class 決策模型」的 JevBench 基準測試出現在 Hacker News 討論串裡。如果你的場景是分類、排序或 reranking，且輸出本來就不需要自然語言解釋，Jev 這類決策模型可能比一般 LLM 更划算；但只要牽涉到會影響人的決策（招募、信用評分等），黑箱程度加上潛在偏見風險，都值得在導入前先想清楚。

🔗 **來源**
- 標題：Jev introduces a new shape of LLM—System One, aka Decision Models
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/21/jev/

#Jev #DecisionModels #LLM #MachineLearning #AIBias #Classification #SearchReranking #TypeSafeAI #OpenWeights #AIEvals
