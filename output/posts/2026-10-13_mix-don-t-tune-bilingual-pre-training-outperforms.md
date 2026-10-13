---
title: 'Mix, Don''t Tune: Bilingual Pre-Training Outperforms Hyperparameter Search
  in Data-Constrained Settings'
source: Apple ML
url: https://machinelearning.apple.com/research/mix-dont-tune
model: claude-code/sonnet
generated_at: '2026-10-13T22:11:41.855770'
score: 80
---

📌 【Apple】資料不足時，混資料贏過調參數

TL;DR：近千次預訓練實驗顯示，混入英文資料比調超參數更能救阿拉伯語低資源模型，且模型越大效果越明顯。

當低資源語言的訓練語料註定要被模型反覆看過好幾遍時，多數團隊的第一反應是調高weight decay硬壓過擬合——但Apple這篇研究用近千次訓練實驗說明，這條路可能從一開始就選錯了方向。

🤔 **低資源語言預訓練的兩條老路**

對世界上多數語言而言，語言模型的pre-training都處在data-constrained的狀態：模型必須把同一批訓練資料重複看過多次，這會傷害generalization。業界常見兩種補救方式。第一種是激進的hyperparameter tuning，例如拉高weight decay，透過壓縮權重來限制網路capacity，達到regularize效果；第二種是混入高資源輔助語言的資料，用一個可調的mixing ratio擴大訓練分布，為訓練訊號注入新知識。這兩種做法都是在data-constrained場景下改善訓練的原則性手段，但過去缺乏系統性比較。

🧩 **4個模型規模、近1000次訓練，阿拉伯語當主角、英語當配角**

研究團隊（Paul Jeha、Anastasiia Sedova、Louis Béthune、Skyler Seto、Jes Frellsen、Pierre Ablin、Natalie Schluter，部分作者同時隸屬DTU）系統性比較了這兩種槓桿，橫跨150M到1.43B參數的4個模型規模，以阿拉伯語作為低資源目標語言、英語作為高資源輔助語言，總共執行了約1000次pre-training實驗。

📊 **三個發現：混資料贏、贏多少、為什麼validation loss會騙人**

第一個發現是，無論在validation loss還是downstream task accuracy上，混資料（mixing）帶來的提升都大於調超參數，而且這個差距隨模型規模擴大而持續拉大。第二個發現是量化結果：在validation loss上，mixing帶來的提升相當於額外多了2到3倍的「目標語言獨特資料量」；在downstream task accuracy上，這個等效倍數更高達2到13倍，且提升幅度隨模型規模急遽放大。第三個發現最關鍵：只看目標語言的validation loss，會系統性低估mixing的真實價值。原因是mixing同時做了兩件事——透過多樣化訓練訊號來regularize，以及注入重複的目標語料本身無法提供的新知識——而validation loss只捕捉到前者，漏掉了後者對下游任務的貢獻。

💡 **作者給出的三條具體建議**

論文給出的實務建議相當直接：混入一個高資源語言；在調校預算有限時，優先調整mixing ratio，而不是一般的超參數搜尋；超參數設定則可以透過μP從一個小型proxy model轉移過來，省去在大模型上重跑搜尋的成本。

🎯 **實務啟示**

對正在訓練低資源語言模型的團隊而言，這篇研究的訊息很直接：別把預算全押在hyperparameter sweep上，先確認資料配方（mixing ratio）有沒有調對；同時，模型選擇與early stopping如果只看target-language validation loss，可能正在低估混資料對下游任務帶來的真實增益，應該搭配downstream task accuracy一起評估。

🔗 **來源**
- 標題：Mix, Don't Tune: Bilingual Pre-Training Outperforms Hyperparameter Search in Data-Constrained Settings
- 作者／機構：Paul Jeha, Anastasiia Sedova, Louis Béthune, Skyler Seto, Jes Frellsen, Pierre Ablin, Natalie Schluter（Apple ML）
- 連結：https://machinelearning.apple.com/research/mix-dont-tune

#MachineLearning #LLM #Pretraining #LowResourceNLP #AppleML #MultilingualNLP #HyperparameterTuning #DataMixing #NLPResearch #ScalingLaws
