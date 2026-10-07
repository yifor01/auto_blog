---
title: Scaling Decision Optimization to 100 Million Variables and Beyond with mPDLP
  in NVIDIA cuOpt
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/scaling-decision-optimization-to-100-million-variables-and-beyond-with-mpdlp-in-nvidia-cuopt/
model: claude-code/sonnet
generated_at: '2026-10-07T22:23:57.186648'
score: 85
---

📌 NVIDIA cuOpt 用多 GPU 解上億變數的線性規劃

TL;DR：NVIDIA cuOpt 新推出 mPDLP 多 GPU 求解器，靠 min-cut 分割減少跨 GPU 通訊，單卡記憶體用量最多省 6 倍。

有一道叫 zib03 的線性規劃測試題，2008 年由 Thorsten Koch 提出，光是矩陣裡的非零元素就超過 1 億零 400 萬個。十幾年來它一直是演算法與硬體進步的試金石，而 NVIDIA 剛把這道題的求解速度，又往前推了一大步。

🤔 **一道考驗了十幾年的超大規模 LP 問題**

供應鏈問題正跨越更多 SKU、運輸路線與限制條件，電力網也要即時平衡更多分散式電源——這些都需要在有限的規劃時間窗內評估更大規模的模型與更多不確定性。NVIDIA cuOpt 在單 GPU 上已能比 CPU solver 快 10 倍以上，但今日最大型的規劃問題仍可能需要數小時才能收斂，或直接超出單一 GPU 的記憶體容量，成為業務決策流程的瓶頸。這次 cuOpt 把 zib03 搬到多 GPU 上用新的 mPDLP 求解，解題速率比一年前快了將近 10 倍。

🧩 **PDLP：靠兩次矩陣向量乘法反覆逼近答案**

cuOpt 採用的 PDLP（Primal-Dual hybrid gradient method）是一階梯度下降類方法，天生高度可平行化、對 GPU 友善。整個演算法的熱點迴圈是稀疏矩陣向量乘法（SpMV）加上幾個逐元素的映射運算，疊代對象是兩個向量：primal 解 x 與 dual 解 y，限制條件則抽象成一個矩陣 A（以及它的轉置）。每一輪疊代大致分兩步：先用上一輪的 dual 解 y，結合 A 的轉置與成本向量，算出新的 primal 解 x，並投影回變數的上下界範圍內；再用更新後的 x，結合 A 本身與限制式右手邊的常數，算出新的 dual 解 y。扣掉可平行化的逐元素運算後，真正需要跨裝置溝通的只剩下這兩次 SpMV，而且彼此依賴對方的輸出。

把 SpMV 分散到多 GPU 時，由於它是一個受記憶體頻寬限制的運算，增加 GPU 數量等於直接疊加可用頻寬，但代價是要壓低兩種分散式開銷：等待其他 GPU 傳資料的通訊開銷，以及工作分配不均造成的閒置。硬體上，NVIDIA 用 NVLink 負責兩張 GPU 間的高速交換，NVSwitch 負責協調多張 GPU 之間的通訊；軟體上則靠 NCCL 函式庫提供 GPU 直連的點對點與集合通訊操作（如 AllReduce、AllGather、Broadcast），原生吃滿 NVLink 與 NVSwitch 的頻寬。

💡 **從各自獨立到聯合分割：少掉不必要的跨卡對話**

先前的多 GPU 方案 D-PDLP 採用「2D 分割」：先重新排序矩陣改善負載平衡，再沿著行與列把矩陣切成多個子區塊分散到各 GPU，原始矩陣的 SpMV 由每個子區塊各自計算後，再把對應到同一列的部分結果加總還原。這個方法可行，但它把兩次 SpMV 當成互相獨立的運算來處理。

cuOpt 的 mPDLP 改用「min-cut 分割」：既然同一輪疊代中的兩次 SpMV 透過 x 與 y 向量彼此依賴，就該聯合考慮這兩次運算，而不是各自獨立分割。做法是依據矩陣 A 的稀疏模式，盡量把輸入與輸出向量之間連結緊密的部分留在同一張 GPU 上——因為矩陣稀疏，計算某個 y 值時往往根本用不到完整的 x 向量，只需要對應非零項的那幾個分量。透過這種依賴關係的二分圖分析找出切割點，就能大幅減少連續兩次 SpMV 之間必須跨 GPU 傳輸的資料量。

📊 **記憶體省 6 倍，速度一年快 10 倍**

在 zib03 這道超過 1 億零 400 萬非零元素的基準問題上，cuOpt mPDLP 用多 GPU 求解，解題速率比一年前的版本快了將近 10 倍。相較於單 GPU 版本的 PDLP，mPDLP 在非零元素上限 21 億的 LP 問題上，單卡峰值記憶體用量最多可降低 6 倍。這套方法也已應用在合作夥伴的實際場景：Kinaxis 用於全球性限制條件下的供應與生產規劃，PSR 則用於大型能源系統的產能擴張模型。

🎯 **實務啟示**

如果團隊手上的 LP 問題已經逼近小時級的收斂時間，或開始撞上單 GPU 記憶體上限，而基礎設施已經有 NVLink 互連的多 GPU 叢集，mPDLP 這種善用疊代依賴關係而非天真平行切分的設計，值得作為下一步擴大求解規模的參考方向。

🔗 **來源**
- 標題：Scaling Decision Optimization to 100 Million Variables and Beyond with mPDLP in NVIDIA cuOpt
- 作者／機構：Tanya Lenz（NVIDIA Developer Blog）
- 連結：https://developer.nvidia.com/blog/scaling-decision-optimization-to-100-million-variables-and-beyond-with-mpdlp-in-nvidia-cuopt/

#LinearProgramming #GPUComputing #NVIDIA #cuOpt #HPC #NVLink #NCCL #DecisionOptimization #SupplyChain #ParallelComputing
