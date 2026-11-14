---
title: AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems
source: Hacker News
url: https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths
model: claude-code/sonnet
generated_at: '2026-11-14T21:38:29.540371'
score: 72
---

📌 Claude兩天讀完哥德爾手稿，揭露數百個未公開定理

TL;DR：Claude協助破解哥德爾速記手稿，揭露他早已超前證明的多項定理。

一位邏輯學家為了不想退休，花了九年時間試著讀懂哥德爾用一種已經絕跡的德文速記寫下的1009頁筆記；人類一週只能啃一頁，直到他找Claude幫忙，兩天內就拿到一份650頁的解讀報告。

🤔 哥德爾留下的、沒人讀懂的筆記

奧地利邏輯學家哥德爾（Kurt Gödel）1931年發表的不完備定理改寫了數學的邊界，也啟發了圖靈寫下1936年那篇開啟現代計算理論的論文。但在那之後，哥德爾公開發表的論文很少，留下的未發表手稿卻多達數萬頁。從2017年起，芬蘭邏輯學家Jan von Plato在赫爾辛基大學主持一個計畫，試圖讀懂哥德爾1940年代寫下的16本筆記，合計1009頁密密麻麻的文字，其中大部分是用一種當年就已經過時的德文速記Gabelsberger寫成，全世界目前只有六個人看得懂這種速記。這個計畫拿到歐洲研究委員會（ERC）250萬歐元的補助，但進度極慢，一年大概只能讀50頁。

🧩 把轉寫稿與六本哥德爾研究著作一起交給Claude

今年八月，von Plato在一場討論AI與定理證明的會議上，被電腦科學家建議試試讓Claude幫忙。回到赫爾辛基後，他把自己的筆記轉寫稿，連同他過去寫的六本哥德爾相關著作與其他二手科學文獻一起交給Claude。短短幾天內，Claude產出一份650頁的解讀報告，雖然仍需要von Plato逐頁核對，但他形容這是「人類幾乎不可能做到的工作」，因為人類一次只能讀一頁、容易忘記前文，而AI可以把上千頁的內容當成一個整體來串連。

📊 663個候選定理，約400個驗證成立

von Plato交給Claude的第一個任務，是確認哥德爾的筆記裡是否藏著「選擇公理（axiom of choice）獨立性」的證明。哥德爾在1966年看到美國數學家Paul Cohen因證明這個獨立性拿下費爾茲獎時，曾表示自己在1940年代就已經證明過，卻在被要求提供證明時無法從筆記中重建出來。Claude給出的答案是：幾乎做到了。筆記裡只有一個定義寫錯，而兩年前的筆記裡其實有正確版本，von Plato認為哥德爾只要再花幾個月就會抓到正確定義。von Plato把Claude重建出的證明丟進證明輔助工具Coq驗證，結果通過。接著von Plato要求Claude找出筆記中哥德爾已經證明、畫出證明草稿或至少有想法的所有定理，Claude找出663個，送進Coq驗證後：

| 驗證結果 | 數量 |
|---|---|
| 完全驗證成立 | 約400個 |
| 需修正敘述或補充假設後成立 | 約200個 |
| 確認為錯誤 | 約50個 |

von Plato指出，哥德爾本人重讀筆記時，偶爾也會在旁邊批註「falsch!（錯了！）」或「schlecht!（糟糕！）」，所以出現約50個錯誤並不意外。

💡 原來他離費爾茲獎只差一步

von Plato認為，如果哥德爾當年發表了選擇公理獨立性的證明，他應該會拿下1940年的費爾茲獎；他推測哥德爾看到Cohen拿獎時，心裡或許覺得那是自己錯過的榮耀。von Plato也特別提到，哥德爾的筆記裡還有十幾個邏輯與數學基礎的主題，是過去80多年來都沒人研究過的方向，其中一些結果要到70、80年代才被其他人獨立發現，哥德爾卻早就寫在筆記裡。他計畫接下來繼續探索哥德爾的物理與宇宙學筆記。

⚠️ 多少是Claude、多少是哥德爾，仍待歷史學家釐清

聖母大學邏輯學教授Joel David Hamkins表示，他還沒看過Claude重建的選擇公理獨立性證明細節，但如果這個重建結果站得住腳，「這會是一項了不起且具歷史意義的發現」；不過他也強調，其中有多少是Claude的貢獻、多少是哥德爾原本就想清楚的，是留給歷史學家去釐清的工作。報導中也提到，Claude產出的解讀報告仍需要von Plato逐頁人工核對，且約50個定理最終確認為錯誤，顯示AI輸出仍需要配合形式化驗證工具與領域專家把關。

🎯 實務啟示

這個案例對做研究或整理大量歷史文件、程式碼庫、法規文件的工程師有參考價值：用LLM處理人類難以一次性掌握全貌的龐大資料，再搭配像Coq這類可驗證的工具把輸出結果「釘住」，是一種能兼顧規模與正確性的組合，而不是直接相信模型輸出。

🔗 來源
- 標題：AI unlocks Gödel's notebooks, said to contain hundreds of proved theorems
- 作者／機構：bookofjoe（Hacker News）
- 連結：https://www.theguardian.com/science/2026/nov/13/kurt-godel-notebooks-ai-helps-unlock-hidden-discoveries-man-who-transformed-maths

#AI #Claude #KurtGodel #MathematicalLogic #TheoremProving #Coq #FormalVerification #HistoryOfScience #IncompletenessTheorem #AIResearch
