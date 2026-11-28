---
title: GPT-6.2 Astra is the first model to beat Googlers' code golf records
source: Hacker News
url: https://bjin.github.io/go-codegolf-benchmark/#leaderboard
model: gpt-6.1-terra
generated_at: '2026-11-28T05:51:47.135619'
score: 80
---

📌 GPT-6.2 挑戰程式高爾夫紀錄

TL;DR：程式高爾夫評測觀察模型能否找到更短、不同路徑的解法。

🎣 當工程師花數小時只為節省一個位元組，LLM 還能找到更短的寫法嗎？

作者 bjin 建立了一套評測，讓前沿模型挑戰 Google 員工過去創下的程式高爾夫紀錄。作者指出，GPT-6.2 Astra 是首個超越這些人類紀錄的模型。

🤔 **比的不是執行速度，而是程式碼長度**

程式高爾夫（code golf）的目標是用盡可能短的程式碼解題。作者回憶，2015 年在 Google 時，一群愛好者每週都會花費數小時，嘗試讓解法再少一個位元組。

這類題目不只考驗能否寫出正確答案，也考驗能否從不同角度重新表達問題。作者因此想知道，前沿模型與這些投入大量心力創下的人類紀錄相比，表現如何。

🧩 **模型用複數與 4 的次方找到不同解法**

作者指出，前沿模型在部分題目中找到過去 Google 員工未使用的解法。例如，在「Surviving Queens」與「The Rolling Dice」兩題中，模型利用 Python 和 Ruby 內建的複數支援來解題。

另一題「(-5)-Smooth Numbers」要求列出前 n 個可表示為 (-2)^x、(-3)^y、(-5)^z 乘積的正整數。作者表示，多數解法會使用巢狀迴圈或逐步擴充集合，再進行排序；GPT-6.2 Astra 則給出了以 4 的次方為基礎的解法，並在這題取得唯一最佳紀錄：

```python
g=lambda n:sorted(4**i%(2**999-5)%(2**49-3)for i in range(7000))[:n]
```

這段程式對 4 的次方連續進行兩次取餘數運算，再將結果排序，取出前 n 個。摘要未提供這個構造的推導或適用範圍。

⚠️ **超越紀錄不代表全面評估模型能力**

作者認為程式高爾夫可以作為前沿模型的一種評測，但不是全面性的評測。它鼓勵不同角度的思考，也重視動手實驗，例如撰寫搜尋程式尋找更短的運算式，或探索編譯器、直譯器與函式庫中較少人使用的功能。

摘要沒有提供完整題目數、評分細節或超越紀錄的幅度，因此無法進一步判斷模型在整套評測中的表現分布。

🎯 **把短解法當成探索工具，而非直接採用**

對工程師而言，這項評測展示了讓模型提出不同解題路徑的可能性。實務上可以把這類候選解法作為探索起點，再驗證其正確性與適用範圍；程式碼更短，並不等同於摘要已證實它適合所有使用情境。

🔗 **來源**
- 標題：GPT-6.2 Astra is the first model to beat Googlers' code golf records
- 作者／機構：bjin
- 連結：https://bjin.github.io/go-codegolf-benchmark/#leaderboard

#CodeGolf #LLM #Benchmark #GPT #Python #Ruby #Programming #CodeGeneration #ProblemSolving #AIResearch
