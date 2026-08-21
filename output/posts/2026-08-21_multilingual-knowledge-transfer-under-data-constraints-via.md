---
title: Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions
source: Apple ML
url: https://machinelearning.apple.com/research/multilingual-knowledge-transfer-lexical-interventions
model: claude-code/sonnet
generated_at: '2026-08-21T06:33:25.357936'
score: 92
---

📌 【Apple ML研究】換幾個詞，低資源語言訓練提速2倍

TL;DR：換詞不換模型，讓低資源語言預訓練最快提速2倍。

多數語言模型的「世界知識」，其實是從英文這類高資源語言裡學來的。但當目標語言的資料量不足時，這些知識要怎麼搬過去？過去的做法幾乎都得靠平行語料、翻譯系統或額外訓練階段，這些資源對大多數語言而言根本不存在。Apple ML 最近提出的方法，卻只靠「換幾個詞」就辦到了類似效果。

🤔 高資源語言撐起了低資源語言的知識

論文指出，跨語言知識轉移（cross-lingual knowledge transfer）對建構低資源語言的高效能語言模型至關重要。當目標語言資料稀缺時，涉及科學推理、常識推論與世界知識的下游任務，其所需知識主要必須從高資源語言取得，因此有效的知識轉移就變得格外關鍵。但現有方法大多需要大量平行資料、翻譯系統、輔助模型或額外訓練階段，而這些對許多語言而言幾乎都不可得。

🧩 LINK：只換詞，不加訓練

作者提出的方法叫 LINK，是一種在預訓練階段就進行的資料層介入（data-level intervention）。做法很直接：在高資源語言（英文）預訓練語料的一部分裡，利用雙語詞彙表，隨機挑選詞彙替換成目標語言的對應翻譯詞。

這個做法有兩個特點值得注意。第一，不需要額外訓練任何模型；第二，只需要一份雙語詞彙表，而這種詞彙表對幾乎任何語言而言都能以近乎零成本取得。替換比例可以自由調整，實作門檻相當低。

📊 八種語言、五種模型規模，訓練最快提速2倍

論文在八種語言、五種模型規模上進行評估，結果顯示目標語言的下游任務表現有明顯提升。其中，訓練達到同等效能所需的時間最多可縮短一半，也就是最高2倍的加速效果。

🎯 實務啟示

對於資源有限、無法取得大規模平行語料或翻譯系統的團隊而言，LINK 提供了一個低成本切入點：只要有一份雙語詞彙表，就能直接介入既有的預訓練流程，不必新增訓練階段或輔助模型。對想擴展多語言涵蓋範圍、但工程資源有限的團隊來說，這是值得評估的方向。

🔗 來源
- 標題：Multilingual Knowledge Transfer under Data Constraints via Lexical Interventions
- 作者／機構：Anastasiia Sedova, Natalie Schluter, Skyler Seto, Maartje ter Hoeve（Apple ML）
- 連結：https://machinelearning.apple.com/research/multilingual-knowledge-transfer-lexical-interventions

#MultilingualNLP #LowResourceLanguages #CrossLingualTransfer #LanguageModels #Pretraining #AppleML #NLP #MachineLearning #DataEfficiency #LLM
