---
title: 'Language Models for Text Classification: From Bag-of-Words to Jev'
source: Sebastian Raschka
url: https://magazine.sebastianraschka.com/p/classifier-history-and-jev
model: claude-code/sonnet
generated_at: '2026-09-29T21:45:34.739087'
score: 86
---

📌 從詞袋模型到 Jev：一段文字分類的技術演進史

TL;DR：Jev 爆紅背後，其實是文字分類技術數十年演進的縮影，讀懂歷史才看得懂它的真正定位。

過去兩週，Jev 這個新模型在技術社群掀起一波熱議。乍看之下，它「只是」一個分類器，但知名機器學習作者 Sebastian Raschka 坦言，自己對 Jev 的看法從「這種東西我隨手就能做」轉變成「這比我想像中好用很多」。要理解這個轉折，得先回頭看文字分類技術是怎麼一路走過來的。

🤔 Jev 到底是什麼，為什麼難以一句話說清楚

Raschka 指出，Jev 的定位頗為尷尬。比起最新的 GPT 與開源 LLM，Jev 能做的分類任務它們同樣做得到，而且 LLM 還能處理更廣泛的決策任務；但 Jev 的賣點在於，同樣的分類工作它跑得更快、也更便宜。另一方面，若拿 Jev 對比針對單一任務設計的專用分類器，Jev 在準確度、速度、成本上不見得佔優勢，它真正的優勢是「更泛用」，不必為每個任務重新打造一個模型。這也是為什麼「Jev 本質上是個文字分類器」，卻又「不只是」文字分類器。

🧩 從詞袋模型講起：機器怎麼理解一整段文字

在 Transformer 出現之前，文字分類的標準做法是詞袋模型（bag-of-words）。概念很單純：先用訓練集裡所有出現過的字詞建立詞彙表（vocabulary），可以選擇性去除「a」「the」這類幾乎不帶語意的停用詞（stopword），接著把每份文件轉成固定長度的向量，向量中每個位置對應詞彙表裡的一個字，數值則是該字在文件中出現的次數（也可以改用 TF-IDF 之類的正規化方式）。舉例來說，若詞彙表有 5 萬個字，不論輸入文件是 10 個字還是 30 萬個字，最後都會被壓成一個 5 萬維的向量，而且大多數位置是零，因為單一文件通常只會用到詞彙表裡的一小部分字。

有了這種固定大小的向量，就能套用單純貝氏（naive Bayes）、邏輯迴歸（logistic regression）、SVM、隨機森林、XGBoost 等經典分類器來訓練。Raschka 提到一個流傳已久的說法：Gmail 最早的垃圾郵件過濾器，據稱就是用詞袋表示法搭配單純貝氏模型。這套方法運算成本低，在垃圾郵件過濾這類「某些關鍵字就能強烈暗示標籤」的任務上往往已經夠用。

不過詞袋模型有個致命傷：它完全丟失了詞序。「the dog bites the man」跟「the man bites the dog」在詞袋表示法下會產生一模一樣的向量，儘管兩句話描述的是完全不同的事件。雖然可以加入 n-gram（詞組）當作額外特徵保留一些局部順序資訊，但代價是詞彙表會急遽膨脹。即便如此，Raschka 表示詞袋模型加邏輯迴歸至今仍是他面對任何文字分類問題時的第一個 baseline，因為實作起來實在太簡單。

🧩 embedding 登場：用密集向量取代逐字計數

為了保留句子結構，CNN 與 RNN 等神經網路架構改用詞嵌入（word embedding）取代詞袋表示法。兩者差異在於：詞袋向量是用整份文件裡每個詞出現的次數代表整篇文字，詞嵌入則是把「單一個詞」轉換成一個學習出來的密集向量，運作方式跟 LLM 裡的 embedding 層很類似，都是把輸入 token 轉成密集向量。

embedding 可以在模型外部先訓練好，例如 Word2Vec、GloVe 這兩個經典方法，也可以直接作為神經網路架構的一部分，在訓練過程中一併學習與調整。但這些傳統 embedding 有個共同限制：查詢時是與上下文無關的（context-independent）。也就是說，「bank」這個字不管出現在「river bank」還是「bank account」裡，拿到的都是同一個向量，這也是後來 attention 機制被拿來解決上下文問題的原因之一。

💡 Jev 的座標：介於專用分類器與通用 LLM 之間

把這段歷史放回 Jev 身上，會更容易看懂它的定位。從詞袋模型、傳統 embedding 加 RNN/CNN，一路走到 Transformer 與 LLM，文字分類技術其實是沿著「犧牲泛用性換效率」與「犧牲效率換泛用性」這條軸線持續拉扯。Jev 選擇了一個特定的位置：比通用 LLM 更快更便宜，比專用分類器更泛用，這正是它能在技術社群引發討論的原因。

🎯 實務啟示

在動手為新任務訓練或呼叫一個專用分類模型之前，不妨先想清楚自己真正需要的是「泛用的決策能力」還是「特定任務的極致效率」。詞袋模型加邏輯迴歸這種老派做法，至今仍是驗證問題可行性最快的 baseline；而像 Jev 這樣介於兩者之間的模型，也提醒我們分類技術的選型不是只有「上 LLM」或「土法煉鋼」兩個選項。

🔗 來源
- 標題：Language Models for Text Classification: From Bag-of-Words to Jev
- 作者／機構：Sebastian Raschka
- 連結：https://magazine.sebastianraschka.com/p/classifier-history-and-jev

#Jev #TextClassification #NLP #BagOfWords #WordEmbeddings #Word2Vec #MachineLearning #LLM #SebastianRaschka #NaiveBayes
