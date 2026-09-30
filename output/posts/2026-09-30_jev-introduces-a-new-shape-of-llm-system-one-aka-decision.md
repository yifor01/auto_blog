---
title: Jev introduces a new shape of LLM—System One, aka Decision Models
source: Simon Willison
url: https://simonwillison.net/2026/Sep/21/jev/
model: claude-code/sonnet
generated_at: '2026-09-30T21:41:34.934866'
score: 99
---

📌 TypeSafe推出Jev：把LLM輸出換成一個機率數字

TL;DR：新模型類別「決策模型」用浮點數取代文字輸出，比GPT-5 Nano還便宜。

想像你請一個大型語言模型幫你判斷一封信是不是垃圾郵件，它卻寫了三段解釋還加上免責聲明。TypeSafe AI認為，這正是現有LLM在分類任務上的浪費。上週，他們發表了Jev，一款完全不寫文字的模型。

🤔 背景：什麼是「System One」模型

TypeSafe AI把Jev定位為一種新的模型類別，官方稱為System One models，但Simon Willison引用Maggie Appleton的說法，認為「decision models（決策模型）」是更貼切的名字。TypeSafe自己的形容是：可以把Jev想成是「前沿智慧包裝成的函式呼叫」，丟入未結構化的狀態（state），吐出的是有型別、有機率的決策。它仍然接受文字輸入，但輸出完全不是文字，而是對應類別、是非題、評分的浮點數，並附上信心分數。

🧩 方法或架構：state + questions

使用方式是組成一個「state」物件，可以是一段字串、字串陣列，或一組名稱－數值配對，用來描述一篇文章、一位顧客，或任何一筆紀錄。接著把這個state連同一個或多個問題送進API，每個問題都會得到對應答案。文中提到可以問三種類型的問題，對照前面提到的輸出型態，對應的應是分類、是非、評分。多個問題會平行評估，因此送一整批問題所花的時間跟只送一題差不多。

📊 數據或結果：比GPT-5 Nano還便宜

計價方式跟一般LLM不同，一般LLM的輸出計費通常比輸入貴得多，Jev則是只對輸入收費，輸出完全免費。第一款模型的輸入價格是每百萬token 0.042美元，比OpenAI GPT-5 Nano的0.05美元還便宜。根據Jev 1.13的「jaggedness」（能力不均勻）文件，目前它不擅長處理數字、日期，以及「對抗性內容」。

💡 深入分析：黑箱疑慮與一個怪異的實驗

Simon Willison點出一個讓他不太舒服的地方：Jev讓黑箱化的問題更嚴重。一般LLM好歹能要求它解釋理由（雖然不保證準確），Jev連這個都沒有，丟進去再多文字，回來的只有一個浮點數。如果Jev判定某段內容是垃圾郵件，究竟是哪個訊號觸發的，完全無從得知。這也讓偏見問題變得更需要警惕，作者特別提到希望沒有人拿Jev來為求職者排名，因為那個浮點數背後可能藏著模型裡未被察覺的偏見，事後要拆解也很困難。他做過一個實驗：讓Jev對舊金山灣區每個城市回答「是不是好城市？」的是非題，結果Cupertino排名最高，East Palo Alto最低。正因為黑箱程度更高，作者認為evals（評測）和結構化實驗比一般LLM專案更加重要，好在Jev夠便宜，跑上百上千個實驗提示詞也只要幾分錢。

⚠️ 限制

不擅長數字、日期與對抗性內容的處理；完全無法解釋決策依據，只能得到一個數字；偏見風險難以被察覺與拆解，尤其在牽涉人的評分情境中風險更高。

🎯 實務啟示

Jev的定位很適合能表述成分類任務的工作：垃圾郵件偵測、標籤建議、優先順序排序。Simon本人也在嘗試把它用在搜尋重排（reranking）：先用BM25之類便宜的演算法抓出100個候選結果，再讓Jev針對原始查詢逐一評分相關性。社群已經出現用開放權重模型重現Jev概念的專案，例如Kev基於Qwen 3.5，推出0.8B、4B、9B三種規模的模型，也有人架設了JevBench這樣的基準測試來比較這類「Jev-class決策模型」。Simon Willison另外釋出了llm-typesafe外掛，讓自己的LLM CLI工具與Python函式庫也能呼叫Jev。

🔗 來源
- 標題：Jev introduces a new shape of LLM—System One, aka Decision Models
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Sep/21/jev/

#LLM #DecisionModels #MachineLearning #AIInference #TypeSafeAI #Jev #AIProductivity #Classification #SearchReranking #AIBias
