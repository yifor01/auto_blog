---
title: 'Introducing Olmo-core 3: Open, scalable training infrastructure for large
  MoEs'
source: HuggingFace Blog
url: https://huggingface.co/blog/allenai/olmocore3
model: claude-code/sonnet
generated_at: '2026-10-01T21:59:51.306370'
score: 109
---

📌 Ai2 Olmo-core 3：開源訓練框架衝向兆參數 MoE

TL;DR：Ai2 釋出 Olmo-core 3，MoE 訓練吞吐量提升達 2.7 倍，架構可撐到兆參數規模。

訓練大型語言模型的帳單，從來不是算力本身貴，而是「把算力用好」更貴。Mixture-of-Experts（MoE）架構原本承諾用部分參數換取更大容量，但當專家數量一多，光是把 token 路由到正確專家、跨 GPU 協調通訊，就可能把稀疏運算省下的效率吃光。Ai2（Allen Institute for AI）這次把矛頭對準這個問題，公布了訓練框架 Olmo-core 的第三代版本。

🤔 **MoE 的理論效率，卡在通訊成本上**

MoE 的賣點是讓模型擁有更多可學習參數，卻不必讓每個輸入都用到全部參數。但問題在於，完整模型仍得分散儲存在 GPU 記憶體裡並持續更新，而把資料導向叢集中正確的專家（expert，MoE 裡的專職子模組）會產生額外的通訊與協調開銷。隨著 MoE 規模擴大，這些開銷很容易侵蝕掉「只用部分模型」原本該有的計算優勢。

🧩 **從 FSDP 轉向 DDP，重新設計路由與計算**

Olmo-core 的 MoE 血統可追溯到 OlmoE（64 個 routed experts），而上一代 Olmo 3 用的是密集（dense）架構，訓練棧也是圍繞密集模型設計。舊版 MoE 實作採用 fully sharded data parallelism（FSDP），每個小批次訓練資料都要重新蒐集與重新分片模型權重。Olmo-core 3 改用 distributed data parallelism（DDP）為基礎的新系統，讓專家常駐在 GPU 上、直接把相關資料路由過去，省下反覆蒐集權重的開銷。

框架同時結合三種切分技術：expert parallelism 把專家分散到不同 GPU；pipeline parallelism 把模型的層（layer）切成多組 GPU 分段處理，降低單一 GPU 需要保留的模型比例；distributed optimizer 則把優化器狀態（optimizer state，即用來計算與套用更新的額外資料）分散儲存，而非每張 GPU 都存一份完整副本。

在路由與計算效率上，Olmo-core 3 也做了幾項最佳化：rowwise expert parallelism 讓路由後的資料直接進入專家輸入緩衝區，減少重新排列的額外工作；GPU-resident routing 把路由中繼資料留在 GPU 上，CPU 不必等資料複製回來就能排隊工作；grouped GEMM 則把大量小型專家計算合併執行，提升 GPU 利用率。此外，框架也支援 MXFP8 這種低精度數字格式，用更少位元表示部分數值，以減少計算量與 GPU 間資料搬移量。

📊 **8 到 128 個專家，吞吐量僅掉不到 5%**

在一項基準測試中，研究團隊把專家池從 8 個擴增到 128 個，但每個 token 仍只選用 4 個專家，使每個 token 的活躍參數量大致固定在約 32 億；總參數容量則從 46 億成長到 470 億，訓練吞吐量只下降不到 5%。

在 8 張 NVIDIA B300 GPU 上的初步測試裡，一個 470 億參數的 MoE 用新訓練棧達到每 GPU 每秒處理 5.2 萬個 token，相較舊版 FSDP 實作的 1.94 萬個，吞吐量約為 2.7 倍。在 4 張 B300 GPU、工作均勻分散到各專家的受控基準測試中，啟用 MXFP8 後訓練吞吐量比 BF16 基線高出約 21%，尖峰活躍記憶體則從 103 GiB 降至 95 GiB，主要增益來自前饋計算與專家間資料搬移，而非 attention 本身。

團隊也把框架推向更大規模：一個 1.2 兆總參數、每個 token 活躍 583.6 億參數的模型在 512 張 GPU 上測得最高 858 TFLOP/s/GPU；搭配另一套跨 GPU 專家間通訊方案 DeepEP v2，更測到總參數達 2.38 兆的配置，不過這是短時容量測試，用來驗證可擴展的規模上限，而非持續訓練的效能表現。

💡 **幾個反直覺的工程教訓**

技術報告也記錄了一些意外發現：一個原本用來鼓勵均衡路由的分數，竟可能在實際工作負載變得更不均衡時反而上升，團隊稱之為「token gerrymandering」；降低處理 token 較少的專家的學習率，在他們測試的模型家族中並未帶來更好結果；相同矩陣維度下，GPU 計算耗時會因處理的實際數值不同而改變，意味著效能比較必須同時對齊輸入值而非只對齊形狀；而把通訊與計算疊加到不同 GPU stream 上並不總是加速訓練，有些測試裡反而拖慢了整體執行時間。

⚠️ **這些是系統效能測試，不是模型品質驗證**

需要留意的是，大規模基準測試大多使用隨機路由來衡量系統吞吐量，而非評估真正訓練出來的模型品質，2.38 兆參數的測試也只是短時容量驗證，並非完整訓練紀錄。

🎯 **實務啟示**

對想自行訓練大型 MoE 卻缺乏超大叢集的團隊或研究者而言，Olmo-core 3 的開源意義在於把「專家並行＋管線並行＋分散式優化器＋低精度格式」這套組合拳的具體取捨攤開來，報告中列出的失敗嘗試（如均衡分數的度量陷阱、學習率調整無效）同樣值得在設計自己的訓練系統時參考。

🔗 **來源**
- 標題：Introducing Olmo-core 3: Open, scalable training infrastructure for large MoEs
- 作者／機構：Kyle Wiggers；Ai2（Allen Institute for AI）
- 連結：https://huggingface.co/blog/allenai/olmocore3

#MoE #LLMTraining #OpenSource #Ai2 #Olmo #DistributedTraining #GPU #MXFP8 #MachineLearning #AIInfrastructure
