---
title: Why is AI generated language so hard to understand?
source: Hacker News
url: https://arxiv.org/abs/2610.29162
model: claude-code/sonnet
generated_at: '2026-10-25T19:48:02.663695'
score: 83
---

📌 AI寫的句子為何比人類文章更難讀懂？

TL;DR：AI模型比人類更愛用難懂句構，根源可能是最佳化目標轉向資訊密度。

你是不是也覺得，最近讀AI生成的文字比以前更費力？這篇研究沒有停在直覺，而是真的拿心理語言學的量尺去量了一遍。

🤔 從「感覺變難讀」到可以量化的問題
研究團隊鎖定一組已知與人類閱讀處理難度相關的心理語言學特徵(psycholinguistic features)，包括object relative clauses、過長的syntactic dependencies，以及低頻n-grams，試圖用它們來量化「AI文字是不是真的變難懂」。

🧩 跨領域語料庫，對照人類寫作與回譯版本
作者建立了一套涵蓋多個領域的AI生成文字語料庫，並設了兩組對照：一組是對同樣內容做round-trip translation（來回翻譯）得到的paraphrase，另一組是人類原始寫作。分析對象涵蓋9個frontier與near-frontier模型。

📊 九個模型，一致地偏好難懂句構
- AI模型使用這些困難特徵的頻率，高於round-trip translation產生的paraphrase。
- 跟人類寫作相比，全部9個模型都用了更多「無生命主詞配有生命動詞」的句型，以及更多低頻n-grams。
- 多數模型在對話情境中，還會用更長的句法依存關係、更多疊加名詞(stacked nouns)、更多reduced object relatives。
- 不同模型家族之間，這些特徵的使用程度有明顯差異。

💡 假說：AI文字在替數學、程式碼、推理讓路
作者提出一個假說：人類語言的演化是為了「成功溝通」，但AI生成文字正越來越朝數學、程式碼、推理這類任務最佳化，而這些任務看重的是資訊密度(information density)，不是溝通的順暢度。為了驗證，他們對一個語言模型施加length penalty進行fine-tuning，結果觀察到模型的語言行為明顯偏離人類習慣的模式，作為這個假說的概念驗證。

🎯 實務啟示
如果你的產品把LLM輸出直接端給使用者看，這篇研究提醒：模型在推理、程式碼類任務上被訓練得越強，它的自然語言輸出可能就離「好讀」越遠。對需要高可讀性的場景（客服回覆、文件摘要），可能需要額外的可讀性約束或人類風格對齊，而不是假設模型能力越強、文字自然就越好懂。

🔗 來源
- 標題：Why is AI-generated language so hard to understand?
- 作者／機構：Thomas Hikaru Clark, Matias B. Martin, Kyle Mahowald
- 連結：https://arxiv.org/abs/2610.29162

#LLM #NLP #Linguistics #AIWriting #Psycholinguistics #LanguageModels #Readability #ComputationalLinguistics #AIAlignment #ArtificialIntelligence
