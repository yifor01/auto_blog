---
title: Scaling Laws for Mixture Pretraining Under Data Constraints
source: Apple ML
url: https://machinelearning.apple.com/research/scaling-laws-mixture-pretraining
model: claude-code/sonnet
generated_at: '2026-08-21T06:28:32.363883'
score: 92
---

📌 稀缺資料到底能重複幾次？Apple 給出混合預訓練尺度法則

TL;DR：橫跨兩千多次訓練實驗，Apple 研究團隊發現稀缺目標資料重複 15 到 20 次仍是預訓練的甜蜜點。

低資源語言、特定領域資料永遠不夠用，這是預訓練圈子的老問題。常見解法是把稀缺的目標資料和大量通用資料混在一起訓練，但混多少一直沒有系統化答案：目標資料放太少，模型學不到位；放太多，同樣的例子重複太多次，報酬遞減甚至過擬合。Apple ML 這篇論文正面處理這個取捨。

🤔 **核心問題：目標資料的曝光量與重複量如何權衡**

隨著語言模型規模擴大，所需資料量跟著成長，但許多有價值的目標資料來源，例如低資源語言或特定專業領域，本質上規模有限。把這些稀缺但有價值的資料與豐富的通用資料混合訓練，會帶來一個根本性的取捨：目標資料佔比太低會讓模型對目標領域曝光不足，佔比太高則會過度重複同樣的樣本，導致報酬遞減甚至最終過擬合。

🧩 **提出重複感知的混合尺度法則**

研究團隊在超過 2,000 次語言模型訓練實驗中，涵蓋多種模型規模與目標資料集大小，以及多語言、特定領域、品質過濾等多種資料類型，系統性研究這個取捨。基於觀察結果，他們提出一套重複感知（repetition-aware）的混合尺度法則，同時考慮重複目標 token 的價值會遞減，以及通用資料所扮演的正則化（regularizing）角色。透過最佳化這套尺度法則，可以用一種有原則的方式計算出有效的混合配置，為資料受限情境下的預訓練提供實用的混合比例建議。

📊 **重複是目標領域表現的核心驅動因素**

在所有測試設定中，研究發現重複次數是決定目標領域表現的核心驅動因素，而且混合訓練能容忍遠高於單一來源訓練的重複次數：稀缺的目標語料可以重複使用 15 到 20 次，最佳重複次數則取決於目標資料規模、運算預算與模型規模。

🎯 **實務啟示**

對於處理低資源語言或垂直領域資料的團隊，這篇研究提供了一個關鍵的心理錨點：不必因為資料量小就放棄，也不必憑直覺猜測混合比例。與其手動試錯調整目標資料佔比，不如依循這套重複感知尺度法則，先依目標資料規模、可用運算預算與模型規模抓出重複次數的合理區間，再據此規劃資料混合配置。

🔗 **來源**
- 標題：Scaling Laws for Mixture Pretraining Under Data Constraints
- 作者／機構：Anastasiia Sedova, Skyler Seto, Natalie Schluter, Pierre Ablin（Apple ML）
- 連結：https://machinelearning.apple.com/research/scaling-laws-mixture-pretraining

#ScalingLaws #Pretraining #LowResourceNLP #MachineLearning #AppleML #DataMixture #LanguageModels #NLP #AIResearch #ModelTraining
