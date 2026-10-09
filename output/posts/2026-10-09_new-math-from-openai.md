---
title: New Math from OpenAI
source: Don't Worry About the Vase
url: https://thezvi.wordpress.com/2026/10/09/new-math-from-openai/
model: claude-code/sonnet
generated_at: '2026-10-09T21:55:35.333929'
score: 111
---

📌 【OpenAI】單一模型一天解開90道世界頂級數學難題

TL;DR:OpenAI內部前沿模型解出90個頂級開放數學問題，並把Lean證明全部公開在GitHub上。

2026年10月6日，一個原本應該佔據全球新聞頭條的消息，卻幾乎沒人注意到：OpenAI把一個內部模型解出的數百篇數學手稿直接丟上GitHub，其中包含全世界最難的500個開放數學問題裡的90個。有人說這是數學史上最重要的一天，也有人說，這恐怕只是指數曲線上又一個不起眼的局部極大值。

🤔 一個模型、一個提示，攻克4000題中的722篇

OpenAI這次公開的722份手稿（撤回3篇沒有Lean證明的之後剩719篇），被整理成372個問題家族。據描述，這些成果出自單一模型，很可能就是先前發布Navier-Stokes證明的那個模型，而且絕大多數問題只用了同一個提示（quasi-Riemann Hypothesis是少數例外）。模型被要求嘗試大約4000個問題，平均每個解答花費約3小時運算時間。提示內容直白到近乎挑戰：「即使問題是『開放』的，你的任務也是把它解決，並給出完整解答。」換句話說，OpenAI這次測試遠談不上全力以赴。

📊 從Riemann到圖論，幾個最受矚目的結果

- quasi-Riemann Hypothesis：證明了zeta函數的「zero-free strip」（無零點窄帶），且不存在Siegel zeros。數學家Alex Kontorovich形容，若這是人類做出的成果，「絕對是Fields Medal等級，甚至是兩個」。
- 矩陣乘法指數上界壓到2.25：此前的世界紀錄約為2.37。Steven Strogatz將這次進展比作Bob Beamon當年那驚人的跳遠世界紀錄。
- 整數乘法的漸進式簡化：與矩陣乘法類似，屬於asymptotic reduction，目前都還不是能直接在實務中變快的解法，但打破了極少人認為能被突破的舊有界線。
- Unique Games Conjecture：雖然不是直接處理P vs NP，但揭露了NP-hard問題在根本限制上的新結果，與Riemann一樣被視為最具份量的突破之一。
- Hodge猜想與Birch猜想：兩個對代數幾何極為關鍵的抽象問題，重要性僅次於Riemann相關結果。
- Hilbert第十問題的延伸：不是在問「這類問題算起來困不困難」，而是在問這類問題是否存在可計算的解。
- Hadwiger猜想（圖論著色）：被形容為整批結果中最令人意外的一項，推翻了長期以來被視為圖論基本關係之一的假設。
- 量子資訊領域：物理學家Isaac Kim特別列出2D area law證明、spin-one Haldane gap、「parity不在QAC^0」、常數誤差的Aaronson-Kuperberg猜想，以及unitary VOA生成conformal net等成果。

💡 奇怪的是，這則新聞幾乎沒上新聞

will depue用GPT-6 Pro與Fable 5.1，把過去三年所有數學發現按「人類發現」與「AI發現」分類比對，結果10月6日公開的這批成果就佔了AI發現總數的81%；Fable 5.1自己排的前100大發現裡，今天公開的清單佔了59%，AI發現整體佔87%。經濟學者Kevin A. Bryan直言，若真的理解這代表什麼，這應該是全球頭版新聞。但多數媒體隻字未提，連AI相關的評論文章裡也看不到這條新聞的蹤影。有評論者拿1957年史普尼克號（Sputnik）發射後蘇聯媒體一開始也沒當回事來類比，認為頭條新聞有時就是會慢半拍才被意識到重要性。OpenAI研究員roon則提出另一種解讀：「在一條分段式指數曲線上，每一個局部極大值，從稍遠處看都顯得微不足道。」

⚠️ 還沒蓋章的部分：驗證與是否真的「會出題」

這批結果都附上了Lean形式化證明，這也是外界還沒能大量挑出錯誤的原因之一，想找漏洞的數學家並不會少。但目前仍無法判斷，這個模型是否真的更擅長「提出猜想」，還是只是在既有猜想上更擅長「完成驗證」，這部分還需要時間讓數學社群逐篇檢視。矩陣乘法與整數乘法的突破目前也都只是漸進式結果，尚未找到能在實務中真正變快的應用場景。

🎯 對工程師與研究者的意義

如果這個規模的結果驗證屬實，代表「同一個前沿模型，換一批提示，就能批量產出研究級數學成果」已經不是假設。對做AI4Science或基礎研究工具的團隊來說，下一步的優先順序很直白：把同樣的方法套到醫學、腫瘤學、電池材料等有明確現實回報的領域，可能比繼續攻克下一個數學猜想更有價值。

🔗 來源
- 標題：New Math from OpenAI
- 作者／機構：TheZvi，Don't Worry About the Vase
- 連結：https://thezvi.wordpress.com/2026/10/09/new-math-from-openai/

#OpenAI #Mathematics #RiemannHypothesis #AIResearch #LeanProver #MatrixMultiplication #AI4Science #FrontierModels #ComputationalMath #MachineLearning
