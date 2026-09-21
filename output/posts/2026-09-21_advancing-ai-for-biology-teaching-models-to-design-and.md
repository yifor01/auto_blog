---
title: 'Advancing AI for biology: Teaching models to design and characterize antibodies'
source: Amazon Science
url: https://www.amazon.science/blog/advancing-ai-for-biology-teaching-models-to-design-and-characterize-antibodies
model: claude-code/sonnet
generated_at: '2026-09-21T21:14:19.263741'
score: 110
---

📌 Amazon 用 AI 拆解抗體設計三大難題

TL;DR：Amazon 團隊用兩個新模型加一個 agent 化流程，分別攻克抗體設計的排序、跨實驗室校正與選點難題。

一款單株抗體藥物，從鎖定目標到選出候選分子，常態需要六到十二個月。真正卡住流程的不是缺乏預測模型，而是這些模型換了個陌生的目標蛋白就容易失靈。

🤔 抗體開發卡在哪三件事

一款抗體藥物能否成功，取決於三個問題：目標蛋白上哪個位置最適合結合、哪些候選分子結合得最緊、以及有沒有候選能撐過量產與臨床。這個領域雖然已經有針對每個問題的預測模型，但普遍面臨同一個困境：在熟悉的目標與檢測方法上表現不錯，換成沒看過的目標就明顯變差，而過去以「同分布準確度」為主的評測基準，讓這個落差很難被量測，也就難以被縮小。

Amazon Bio Discovery 團隊發表的三篇論文分別針對這三個問題出手，其中兩篇聚焦預測（親和力排序、跨情境穩定性預測），第三篇則把預測整合進端到端的設計流程，用 agent 導航結合位點的選擇，並針對一個新的癌症標的產出經實驗驗證的候選抗體命中。

🧩 MochiBind：不猜絕對值，只比大小

在《A systematic evaluation framework for universal antibody-antigen binding affinity prediction and candidate recommendation》（發表於 iScience）中，團隊指出多數親和力預測模型的評測方式本身就有問題：預測「絕對結合強度」，只在訓練時看過的抗原上測試，測試集裡幾乎沒有不結合的候選者。這些條件都讓評測比真實使用情境容易，而真實情境是要從數千個候選裡篩出值得送實驗室驗證的少數。

MochiBind 因此把任務重新定義：不預測絕對數值，而是判斷同一個抗原的兩個抗體誰結合得比較緊。流程是用預訓練的蛋白質語言模型 ESM-2 將抗體-抗原複合物的殘基嵌入表徵空間，取每個複合物殘基嵌入的平均值成為單一嵌入，再用一個專門訓練的投影層把嵌入映射到低維空間，並從兩個投影的差值預測相對結合強度。所有 pairwise 比較結果最後用 TrueSkill（原本用來為電玩對戰玩家評分的貝氏評分演算法）彙整成候選池的全域排名，整個過程不需要任何結構輸入。

📊 跨抗原測試，贏過所有以結構為基礎的基準

評測使用 AlphaBind 資料集，涵蓋 TIGIT、PD-1、HER2、SARS-CoV-1 RBD 四種抗原系統，每種約三萬筆經實驗驗證的變異體，且抗原之間的序列相似度接近零。協定採嚴格跨抗原設計：兩個抗原訓練，第三個驗證，第四個測試，並輪流讓每個抗原都當一次 held-out 目標。

結果顯示，MochiBind 在全部四個 held-out 抗原上的 pairwise 準確率都高於所有以結構為基礎的基準模型，平均比最接近的對手高出近 10%。排序表現上，MochiBind 在四個抗原上都拿下最高的檢索準確率，並在其中三個拿下最高的檢索精確率（即最低的偽陽性率）。速度上，MochiBind 在一顆 CPU 上為 20 萬組抗體配對評分僅需約 13 秒，比競爭方法快上百倍以上，足以支撐大型候選庫的篩選。

🧩 CA-MAP：讓模型自己抓出「這間實驗室的偏差」

第二篇論文《Context-aware multi-property antibody predictor: A novel framework integrating text and protein language models》（發表於 npj Systems Biology and Applications）處理的是另一個老問題：不同實驗室做出來的資料存在系統性差異（batch effect），用單一實驗室資料微調出來的模型，會不自覺把該實驗室的偏差也學進去。

CA-MAP 的做法是在推論時給模型一個提示，裡面包含數量不定的範例抗體及其實測性質，後面接一個要預測的查詢抗體與要預測的性質名稱。如果範例來自和查詢抗體同一間實驗室，這些範例的實測值就會帶有該實驗室的偏差資訊，模型的輸入本身就包含校正 batch effect 所需的線索，不需要重新訓練。

但要讓模型真的去用這些範例並不容易：單一來源資料訓練出來的模型，可能學會直接忽略範例，只依賴查詢序列本身。團隊提出的訓練策略 AB-context-aware，對每個提示隨機重新取樣一次隱藏的變換，同時套用在範例性質與期望答案上，使得這個變換只能從範例中回推，逼模型必須使用上下文。

架構上，CA-MAP 是一個相對小的多模態模型：序列用 ESM-2 編碼，性質名稱用句子嵌入編碼，數值則各自有專屬的編碼器與投影層，再由基於 MAMBA 這個序列建模架構的 state space model 將三者組合起來。訓練資料是涵蓋六種可開發性（developability）性質、共 876,898 條抗體重鏈的合成資料集。

📊 有 batch effect 時，兩種訓練方式差距巨大

團隊在微調過的多模態 LLM TxGemma 上測試預測疏水性的效果：沒有 batch effect 時，標準微調與 AB-context-aware 訓練表現相當，與真實值的 Spearman 相關係數都是 0.99。但加入 0 到 0.3 範圍的模擬加性 batch effect 後，標準微調的相關係數掉到 0.58，AB-context-aware 訓練的模型仍維持在 0.99。整體而言，CA-MAP 在六種可開發性性質中的多項上達到 Spearman 相關係數大於 0.8，並在四項聯合測試的性質上全面超越微調過的 TxGemma 基準。

⚠️ 還沒被完全解決的部分

MochiBind 的跨抗原評測目前只涵蓋 AlphaBind 資料集裡的四個抗原系統；而抗體開發三大關卡中「能否撐過量產與臨床」這一項，素材中僅提及由第三篇論文以 agent 方式處理，並未透露其具體方法與評測細節，這部分仍有待更完整的資訊補充。

🎯 實務啟示

這兩篇論文示範了一個值得借鏡的思路：與其硬解「預測絕對數值」這種難題，不如把任務重新定義成模型真正擅長且貼近實際使用情境的形式，例如 MochiBind 把親和力預測換成相對排序，CA-MAP 則是把校正批次差異變成一個上下文學習問題，而不是每換一批資料就重新訓練。這種「重新定義任務以貼近推論時真實情境」的做法，在其他跨來源資料一致性堪憂的場景也值得參考。

🔗 來源
- 標題：Advancing AI for biology: Teaching models to design and characterize antibodies
- 作者／機構：Amazon Bio Discovery / Amazon Science
- 連結：https://www.amazon.science/blog/advancing-ai-for-biology-teaching-models-to-design-and-characterize-antibodies

#AI4Science #DrugDiscovery #Antibody #ProteinLanguageModel #ESM2 #MachineLearning #Bioinformatics #ComputationalBiology #AmazonScience #InContextLearning
