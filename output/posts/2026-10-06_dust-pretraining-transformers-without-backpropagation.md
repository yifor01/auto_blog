---
title: 'Dust: Pretraining Transformers Without Backpropagation'
source: Hacker News
url: https://qlabs.sh/research/dust
model: claude-code/sonnet
generated_at: '2026-10-06T21:51:00.654294'
score: 108
---

📌 不用反向傳播訓練 transformer，這篇論文做到了

TL;DR：Dust 用「擾動活化值」取代梯度反向傳播，在預訓練 transformer 語言模型上首度逼近甚至超越 backprop。

深度學習幾乎是圍繞著反向傳播打造的：架構、優化器、硬體都在過去幾十年裡配合這個需要可微分、產生一階梯度的演算法共同演化。Dust 這篇論文想問的是一個更根本的問題：如果 backprop 不是必要前提，只是低運算量時代的歸納偏誤，那在運算力愈來愈便宜的今天，有沒有更暴力、更通用的搜尋式方法可以取而代之？

🤔 **為什麼要挑戰 backprop**

作者引用 Sutton 的「苦澀的教訓」(bitter lesson)：能隨運算力擴展的通用方法終將勝出，AlphaGo Zero 就是例子——靠人類資料暖身的版本,最終被純自我對弈的版本超越。作者認為可微分與 backprop 或許在低運算量時是好的歸納偏誤,但到了高運算量時代,反而限制了可行架構的搜尋空間;即便在同一個架構內,梯度方法也未必能最佳地探索損失地景。

🧩 **把擾動放在活化值,而非權重空間**

傳統的 evolution strategies（ES）方法如 EGGROLL 是在權重空間擾動,擴大族群(population)規模時,每個成員都得被實際具現化並單獨評估,成本隨之水漲船高。Dust 的做法不同：它在活化值空間做擾動(node perturbation),而且是獨立地對「每一個 token」做擾動——換句話說,每個 token 就是一個虛擬的族群成員(virtual population member),一次前向傳播就能平行評估所有這些成員,完全不需要額外具現化。

論文作者認為活化值本身就是比權重空間更有意思的搜尋空間,並引用機制可解釋性研究指出,推理(無論是否可用語言表達)其實就存在於活化值之中。Dust 搭配了一套通用的 credit assignment 規則,針對 transformer block 內不同的層類型,給予不同的 token 層級獎勵;再加上一些實作細節與效率手段(例如避免被擾動的模組間互相干擾),構成了整個演算法。

📊 **族群愈大愈接近 backprop,大模型反而更划算**

論文的幾項關鍵發現:
- 從 1M token 規模開始,Dust 的效率比 EGGROLL(transformer 版本)高出約 10^3 到 10^4 倍(依論文的外推估計)。
- 在族群規模夠大時,Dust 在多個設定下的表現甚至超越 backprop,顯示在運算力充裕的情境下有機會超越 backprop。
- 與「zeroth-order 方法無法擴展到大型網路」的一般認知相反,論文發現模型愈大,族群效率反而愈高:一個 2.43 億參數的模型,在多數族群規模下表現優於比它小 120 倍的模型。
- Dust 的梯度估計,隨著族群規模增加會愈來愈貼近 backprop 的梯度,而且這個對齊程度在論文測試的所有規模下都成立,最高測到 1B token。

⚠️ **作者自陳:目前還不是拿來取代 backprop 的時候**

論文明確表示,這篇工作的目標是替「以搜尋為基礎的 credit assignment 演算法」打下基礎,並在他們能想到最難的任務——預訓練 transformer——上證明其可行性,但並未試圖讓它在運算效率上已經足以取代今天的 backprop。

🎯 **對工程師的啟示**

這還不是能立刻拿去生產環境用的訓練法,但它揭示了一個值得關注的方向:如果 zeroth-order 方法真的隨模型規模擴大而變得更有效率,未來在運算力不是瓶頸、而可微分架構才是瓶頸的場景下,搜尋式的訓練方法可能會是值得重新評估的選項。

🔗 **來源**
- 標題：Dust: Pretraining Transformers Without Backpropagation
- 連結：https://qlabs.sh/research/dust

#DeepLearning #Backpropagation #ZerothOrderOptimization #EvolutionStrategies #TransformerTraining #MachineLearning #NeuralNetworks #AIResearch #Pretraining #BitterLesson
