---
title: 'Preparing data for supervised fine-tuning Part 2: Advanced data strategies'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/preparing-data-for-supervised-fine-tuning-part-2-advanced-data-strategies/
model: claude-code/sonnet
generated_at: '2026-08-27T17:28:20.763484'
score: 91
---

📌 SFT 資料準備進階篇：2000 筆是起點，別急著衝量

TL;DR：監督式微調的關鍵不是資料夠不夠多，而是用學習曲線、子集篩選、增強與混合把每一筆資料的效益榨乾。

資料清乾淨、格式也對了，你以為 SFT（supervised fine-tuning，監督式微調）的準備工作結束了？真正難的問題才剛開始：要收集更多資料，還是從現有資料裡挑出更好的子集？

🤔 **先問：你的資料夠不夠？答案藏在學習曲線裡**

AWS 這篇文章（Amazon Nova 客製化系列的第二篇）給出一個粗略起點：典型 SFT 任務約需 2000 筆高品質訓練樣本。但這只是概略值，簡單的格式或風格調整 500 筆就夠，複雜的多步驟推理任務可能要 10000 筆以上，每個任務的飽和點都不同。

文章強調，比訓練資料本身更難準備的是「評估基準」：一個能代表實際生產流量、指標定義清楚的評估集。有了基準之後，才能透過學習曲線分析（訓練一次、保存多個 checkpoint）實際判斷資料量是否足夠——如果資料量翻倍後主要指標的提升不到 1 到 2 個百分點，代表同類型的資料再加也沒用。

🧩 **量不等於質：SFT 不是 pretraining 的縮小版**

文章指出 SFT 並不遵循 pretraining 那種單調的冪律（power-law）縮放，資料量本身不保證等比例的效果提升，關鍵在於指令集的覆蓋度（coverage）與深度（depth）。文中引用的 Data Repetition Beats Scaling 研究顯示：在固定運算預算下，對 400 筆推理範例訓練 128 個 epoch，效果比對 51200 筆範例只訓練 1 個 epoch 高出 12 到 26 個百分點（在 AIME、GPQA 上）。訓練 token accuracy 是一個實用的停止訊號，因為模型接近完全記憶訓練集後，提升就會趨緩。

當邊際效益遞減時，智慧型資料選擇可能比用全部資料訓練更好。文章提到 DEITA、DELIFT、coreset selection 等方法，會根據品質、多樣性以及「這筆資料到底教會模型什麼」來為候選樣本評分，找出覆蓋任務空間又保持品質與多樣性的最小子集。

📊 **資料不夠？用增強擴充，但驗證不能省**

當資料集太小或太窄時，資料增強可以在不成比例增加標註成本的情況下擴充資料。文章指出，對現代 SFT 而言最有影響力的增強形式是生成推理軌跡（reasoning traces）與合成示範。此外，Self-Instruct 能從小型種子集自舉出新的指令-回應配對，Evol-Instruct 則沿著特定維度（例如加入限制條件或加深推理需求）演化既有指令；改寫措辭、調整輸出格式等簡單變換也有幫助。

文章特別點出兩個品質原則：第一，風格的多樣性和內容一樣重要，兩個結構不同的正確解法比兩份相同解法更有價值（MAmmoTH 即利用這個特性）；第二，驗證不可妥協——合成資料是重複樣本和細微錯誤最常見的來源，增強後的資料一樣要通過與人工整理資料相同的品質關卡，並套用前一篇文章提到的去重與過濾步驟。

💡 **資料混合：保住舊能力的保險，不是提升新任務的加速器**

針對特定任務微調模型時，可能會犧牲模型在其他能力上的表現，也就是「災難性遺忘」（catastrophic forgetting）。資料混合的做法是把目標任務資料和能保留既有能力的樣本按比例混合成訓練批次，Amazon Nova Forge 支援在客製化的每個階段混合專屬資料與 Amazon 整理的訓練資料。

文章特別提醒一個容易被忽略的細節：資料混合不一定能提升目標任務表現，它的主要目的是在專精化的同時保留通用能力,因為每一個通用資料的 token 都會擠掉一個領域資料的 token。但當不同資料來源共享底層推理模式時，確實會出現正向遷移——Qwen2.5-Coder 發現以 70:20:10 比例混合程式碼、文字、數學,即使在程式碼基準測試上表現都優於百分之百使用程式碼資料訓練。反過來,如果序列長度失衡,混合也可能有害:即使樣本數只佔 5% 的通用資料,若其序列長度遠長於其他資料,按 token 數計算可能貢獻超過 80% 的梯度訊號,所以要監控 token 層級的比例,而非只看樣本層級比例。

文章也引用幾個 SFT 混合文獻的實證發現：Dong et al. 指出每項技能的資料絕對量比類別間的精確比例更能決定表現，技能弱就先補資料再談重新平衡；Dual-stage Mixed Fine-Tuning 顯示先訓練專屬資料、再用「通用資料混少量專屬資料」訓練,效果優於循序訓練（會遺忘）與扁平混合（會互相干擾）；Cao et al. 則發現最佳混合比例會隨模型大小與資料預算變動，沒有放諸四海皆準的比例，必須實際實驗。

🎯 **實務啟示**

在投入更多標註前，先用學習曲線分析確認資料是否已經飽和；資料混合請當成保留通用能力的保險,而不是提升目標任務分數的手段；監控 token 層級的資料比例,而非只看樣本數比例。

🔗 **來源**
- 標題：Preparing data for supervised fine-tuning Part 2: Advanced data strategies
- 作者／機構：Krishnateja Killamsetty, AWS Machine Learning
- 連結：https://aws.amazon.com/blogs/machine-learning/preparing-data-for-supervised-fine-tuning-part-2-advanced-data-strategies/

#SupervisedFineTuning #LLM #DataAugmentation #MachineLearning #AmazonNova #AWS #ModelTraining #DataMixing #MLOps #FineTuning
