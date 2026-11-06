---
title: Accelerating Reinforcement Learning Weight Refit with the Reshard Collective
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/
model: claude-code/sonnet
generated_at: '2026-11-06T22:17:36.494119'
score: 101
---

📌【NVIDIA】Reshard 集合通訊：把 RL 權重 Refit 的傳輸量砍到理論最小

TL;DR：NVIDIA 提出新集合通訊原語 Reshard，用 DTensor 重新定義 RL 權重同步，省掉重複傳輸。

訓練用的 GPU 和推論用的 GPU，各自用不同的切分方式存放同一份模型權重，每一次強化學習（RL）訓練迭代都要把前者同步給後者。當模型大到數 TB 時，光是這個「同步」動作本身,就可能成為整條訓練流程的瓶頸。

🤔 **Disaggregated RL 訓練裡,weight refit 是什麼問題**

在 RL 後訓練（post-training）中，訓練軌跡是透過對目前的 policy model 做推論即時產生的。為了效率，推論與訓練通常會拆分到不同的 GPU 資源上並行執行，也就是所謂的 disaggregated 架構。policy model 只在訓練 GPU 上更新，系統必須定期把訓練 GPU 上最新的參數同步到推論 GPU，這個同步動作就叫做 refit。

refit 面臨兩個核心挑戰。第一，訓練與推論的運算需求不同，因此權重在兩邊採用不同的平行化配置（data、context、tensor、expert、pipeline parallelism），切分方式自然不同。第二，refit 必須更新推論 GPU 上的全部權重，傳輸量級與模型總權重大小相當,而且這個量級還在持續成長。以 Kimi K3（2.8T 參數）與 Qwen 3.8 2.4T A95B（2.4T 參數）為例，若以 BF16（每參數 2 bytes）計算，權重大小分別約 5.6TB 與 4.8TB。

🧩 **現行 gather-and-broadcast 做法的冗餘，與 DTensor 重新定義問題**

現行做法多採用 gather-and-broadcast：訓練 GPU 先 all-gather 各自的本地 shard 重建出完整參數，再把完整張量 broadcast 給所有推論 GPU，每張推論 GPU 再保留自己需要的那一份 shard。這種方法用「完整張量」當中介表示法雖然直覺，但即使某張推論 GPU 只需要一小部分，也會收到整份參數，造成 gather 與 broadcast 兩階段都有冗餘傳輸。以 all-gather 加 broadcast 估算，邏輯傳輸量約是模型權重大小的兩倍：Kimi K3 約 11.2TB，Qwen 3.8 2.4T A95B 約 9.6TB。對目前最大的開放權重模型而言，每次 refit 的通訊量已達約 10TB 等級，而這個動作在每個訓練步驟都要執行一次。

解決方向是把 refit 重新表述為「DTensor 到 DTensor 的傳輸問題」。NVIDIA 團隊借用 PyTorch 的 distributed tensor（DTensor）抽象，用張量的全域形狀、GPU 的 device mesh，以及張量在這個 mesh 上如何切分或複製（placements）三者來描述一個 layout。無論訓練與推論兩端用什麼平行化配置,refit 都可以視為把一個 DTensor 從訓練端的 layout 重新切分（reshard）成推論端的 layout。

文中以一個 8×8 的權重矩陣為例：兩張訓練 GPU 依「列」切分，每張持有 4×8 的 shard；四張推論 GPU 依「欄」切分，每張需要 8×2 的 shard。只要找出來源與目標 shard 之間的重疊區域，每個目標只需要從每個來源接收一塊 4×2 的區域,就能直接拼出自己需要的 shard，完全不需要先重建完整張量。

🧩 **Reshard 集合通訊，與開源參考實作 NCCL M2N Reshard**

基於這個洞察，團隊定義了一種新的集合通訊呼叫方式,叫做 Reshard：就像 all-reduce、reduce-scatter、all-gather、broadcast 一樣，應用程式只需要描述「來源 DTensor」與「目標 DTensor」，就能發起一次 Reshard 操作，底層的傳輸演算法則被封裝進函式庫，可以獨立於應用程式持續演進。

NVIDIA 已經以 NCCL 為基礎,開源了第一個 Reshard 集合通訊的參考實作：NCCL M2N Reshard，收錄在 NVIDIA/nccl-extensions 這個 GitHub repo 中。它能把一個分布在 M 張來源 GPU 上的張量,轉換成 N 張目標 GPU 所需要的 layout；在 RL refit 的場景中，訓練 GPU 就是來源群組，推論 GPU 則是目標群組。文中以 nccl.m2n.reshard 為例，示範如何把一個在 4 張訓練 GPU 上以 TP4（tensor parallel 4）切分的張量，轉成 4 張推論 GPU 上以 DP4（data parallel 4，即全複製）呈現的 layout。

📊 **用 NVLink 拓撲分組，逼近實體網路頻寬上限**

效能面上，NCCL M2N Reshard 會先精確算出來源與目標 shard 之間的交集，再把這些傳輸對應到實際的 GPU 網路拓撲上。相較於把每個來源的資料獨立送給每一個目標複本，NCCL M2N 會依照 NVLink domain 把目標複本分組處理，藉此提升整體頻寬利用率。

⚠️ **這是給訓練框架的底層原語，不是現成的訓練腳本**

Reshard 本質上是一個通訊原語與參考實作，要在實際 RL 訓練框架中發揮效益，仍需要框架自己把 refit 流程改寫成呼叫這個集合通訊，而非直接得到開箱即用的加速。

🎯 **實務啟示**

如果你的團隊正在自建或維護 disaggregated 架構的 RL 訓練系統，且模型規模已經讓 refit 的通訊時間變得可觀，NCCL M2N Reshard 提供了一個現成的開源起點，值得評估是否能取代既有的 gather-and-broadcast 實作。

🔗 **來源**
- 標題：Accelerating Reinforcement Learning Weight Refit with the Reshard Collective
- 作者／機構：Tanya Lenz, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/

#NVIDIA #NCCL #ReinforcementLearning #DistributedTraining #GPU #DTensor #PyTorch #MLInfra #LLMTraining #HighPerformanceComputing
