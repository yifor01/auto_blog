---
title: Can gzip be a language model?
source: Hacker News
url: https://nathan.rs/posts/gzip-lm/
model: claude-code/sonnet
generated_at: '2026-09-22T20:39:16.374428'
score: 82
---

📌 不用類神經網路，gzip 也能生成文字？

TL;DR：作者用 zlib 加 beam search 打造出「gzip 語言模型」，驗證壓縮與預測的等價性，且完全可在筆電上重現。

沒有權重、沒有訓練、沒有任何學習到的參數，只有你作業系統內建的壓縮工具——這樣的東西，真的能生成看起來像莎士比亞臺詞的文字嗎？

🤔 從「壓縮即預測」這句話開始的好奇心

作者先前寫過一篇不用神經網路做語言模型的文章，靠一個無界的 n-gram 模型（沒有權重、沒有訓練，純靠計數）生成莎士比亞風格文字。後來他讀到論文《Language Modeling is Compression》，裡面提到「壓縮—預測等價性」：每個預測模型本質上都是一個壓縮器，而所有壓縮演算法也都是預測模型。這個說法引出了一個自然的問題：gzip 能不能拿來做語言模型？

🧩 壓縮器裡，其實藏著一個機率模型

壓縮器的本質，是把很少的 bytes 花在它「預期」的資料上，把很多 bytes 花在它不預期的資料上。一個檔案內容是字母 A 重複一百萬次，可以用一句話描述；一百萬個隨機 byte 幾乎壓不了，因為裡面沒有結構可以利用。這不是巧合，而是資訊理論的核心：編碼一個符號所需要的位元數是負 log2(p)，p 是模型賦予這個符號的機率——機率愈高，需要的位元數愈少。所以任何壓縮器內部都藏著一個機率模型，不管有沒有人把它明確寫出來。

gzip 用的 DEFLATE 演算法，靠在 32 KiB 的滑動視窗內尋找與近期文字的匹配，來壓縮接下來要編碼的 bytes。如果某段延續文字呼應了視窗裡已經出現過的內容，DEFLATE 就能把它編碼成一個便宜的 back-reference，而不是一個一個字元的 literal bytes。這給了我們一個現成的分數：候選延續文字的分數 = len(gzip(context + candidate))，壓縮後的長度愈短，代表這段候選文字愈「被預期」。要「餵」這個模型，只要把一個語料庫（corpus）放進 gzip 的視窗裡，任何長得像語料庫的延續文字壓縮後就會很小，反之則會很大。

📊 用 beam search 解決量化雜訊，重現出可讀的莎士比亞片段

單純每一步都挑「壓縮後最短」的下一個 byte，效果出乎意料地差，原因很微妙：gzip 只給出整數的 byte 長度，沒有小數，多加一個 byte 常常完全不改變壓縮後的長度，導致大量候選同分，真正的訊號被量化雜訊淹沒。解法是往前看一整段 span 再決定要不要提交。作者的工具 gzipt 執行流程如下：先以使用者的 prompt 作為要延續的起始文字（沒有 start token，prompt 的 bytes 本身就是 gzip 看到的 context 一部分）；接著讓 gzip 看到語料庫視窗加上 prompt／已生成文字的最近尾端；然後保留 beam_width 個最容易壓縮的部分延續，對每個候選用語料庫中出現過的每個 byte 做延伸，依壓縮後長度給所有候選打分，再裁剪回 beam_width 個，並對 horizon 個 bytes 重複這個過程；最後取最容易壓縮的完整 span（若 temperature 為正則在最終候選中取樣），接到輸出後面，重新開始整個迴圈。

作者用 tiny Shakespeare 語料庫做測試，輸入 prompt「MENENIUS:」，輸出的文字雖然稱不上完全連貫，卻明顯抓到了原文的某些語感，比作者原本預期 gzip 能做到的還要多。整套實作只是一支用標準庫 zlib 的 Python 檔案，程式碼已公開在 GitHub 上。

⚠️ 只看最近的文字，是為了避免陷入自我複製的迴圈

工具刻意只把最近生成文字的尾端留在 scoring context 裡，這個設計是有原因的：DEFLATE 對鄰近的匹配編碼比對遙遠的匹配便宜，如果讓 gzip 看到自己輸出過的全部歷史，最便宜的做法往往會變成不斷逐字複製自己剛剛講過的話，陷入 verbatim loop。原始論文也嘗試過類似逐 byte 的貪婪解碼，但表現不佳；加入 beam search 之後生成品質明顯改善，這一點論文裡也有提到。

🎯 實務啟示

這個實驗把「壓縮即預測」這個常被留在公式裡的抽象概念，變成一個能在筆電上幾分鐘內重現的小工具。對想直觀理解語言模型與資訊理論關係的工程師來說，動手跑一次 gzipt，可能比讀完整篇論文的推導更快建立起直覺，而且原始碼已經公開，值得拿來把玩、驗證自己的理解。

🔗 來源
- 標題：Can gzip be a language model?
- 作者／機構：networked（Hacker News 投稿）
- 連結：https://nathan.rs/posts/gzip-lm/

#LLM #Compression #DEFLATE #Gzip #LanguageModel #InformationTheory #BeamSearch #NLP #MachineLearning #Python
