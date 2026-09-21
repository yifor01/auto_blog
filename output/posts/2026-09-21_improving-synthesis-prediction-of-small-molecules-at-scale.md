---
title: Improving synthesis prediction of small molecules at scale with RetroChimera
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/improving-synthesis-prediction-of-small-molecules-at-scale-with-retrochimera/
model: claude-code/sonnet
generated_at: '2026-09-21T21:14:19.263894'
score: 98
---

📌 【Microsoft】雙模型互補，AI 逆合成路線贏過文獻紀錄

TL;DR：RetroChimera 結合兩個各有所長的逆合成模型，盲測中化學家甚至比文獻紀錄的真實反應更愛它的預測。

開發新藥或新材料，卡關的往往不是想得到什麼分子，而是怎麼把它做出來。逆合成規劃長期仰賴老手化學家的經驗，難以規模化。

🤔 從目標分子往回拆，選擇空間比棋類遊戲還大

逆合成（retrosynthesis）是從目標分子出發，一步步往回拆解成更簡單的原料，概念上類似下棋或圍棋：每一步都要考慮大量可能的拆解方式，同時還要有能通往完整合成路線的整體策略。但逆合成的可能走法遠多於棋類遊戲，而且哪些拆解方式對某個分子是可行的，並不是顯而易見的事。現有系統普遍面臨三個難題：很難記住罕見卻具有策略價值的反應、在訓練分布之外的分子上不夠穩健，以及預測結果和化學家的判斷對不上。這使得逆合成規劃仍高度仰賴專業經驗，難以規模化與自動化。

🧩 一個大膽生成，一個穩健查表，合體互補

發表於 Nature 的 RetroChimera，核心是結合兩個各有所長的模型。R-SMILES 2 是基於 Transformer 的 de-novo 模型，直接從輸入分子生成前驅分子，能靈活地從資料中學習反應規律，但無約束的生成方式也讓它容易產生幻覺。NeuralLoc 則是基於圖神經網路（GNN）的模型，把目標分子與反應模板都編碼成圖，從中挑選反應模板並預測該套用在目標分子的哪個位置，由於預測根植於訓練資料萃取出的反應樣式，結果通常更準確可靠，但遇到模板庫沒涵蓋到的反應類型時就會受限。

這兩個模型的差異反而成了優勢：R-SMILES 2 在反應前後變化幅度大的案例上表現特別好，NeuralLoc 則擅長處理少見且變化較局部的反應。RetroChimera 用一套學習出來的集成策略把兩者的排序預測結合起來，每個模型會為自己預測的每組反應物給出一個與排名相關、且經過學習調整的投票權重，當兩個模型都提出同一個反應時，票數會相加。透過學習在不同排名層級該多信任哪個模型，RetroChimera 得以在各類反應上都逼近表現較好的那個子模型。

📊 化學家盲測：比子模型、比既有方法，甚至比文獻紀錄的真實反應更受青睞

結果顯示，RetroChimera 在常見與罕見反應類型上都表現穩健，產出的逆合成預測也更貼近化學家的判斷。在盲測中，專業化學家對複雜分子的拆解方式，更偏好 RetroChimera 給出的答案，勝過它的兩個子模型單獨的預測、勝過既有的成熟方法，甚至勝過測試集裡文獻紀錄的真實反應。

💡 為什麼這件事值得關注

兩個模型各自的弱點恰好被對方的強項補上：生成式模型的幻覺問題，由模板查表式模型的有憑有據來制衡；模板庫的覆蓋盲區，則交給生成式模型的彈性去補足。這種不追求單一模型全能、而是學習如何信任不同模型的集成方式，對於任何存在多種各有偏誤的預測方法的科學問題，都是可以借鏡的設計思路。

🎯 實務啟示

RetroChimera 已經以 MIT 授權釋出在 GitHub，並可透過 Microsoft Foundry 存取，官方也公開邀請化學界社群實際測試、回報其強項與不足。作者團隊認為，搭配日益成熟的實驗室自動化，這類系統有機會進一步推向閉環、能自我改善的合成規劃與執行流程，對藥物設計與智慧材料的候選分子評估規模化會有直接幫助。

🔗 來源
- 標題：Improving synthesis prediction of small molecules at scale with RetroChimera
- 作者／機構：Microsoft — Felix Pultar, John Gardner, Guoqing Liu, Marwin Segler
- 連結：https://www.microsoft.com/en-us/research/blog/improving-synthesis-prediction-of-small-molecules-at-scale-with-retrochimera/

#RetroChimera #MicrosoftResearch #AI4Science #DrugDiscovery #Retrosynthesis #GraphNeuralNetwork #Transformer #Chemistry #ComputationalChemistry #MachineLearning
