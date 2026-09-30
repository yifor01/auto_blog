---
title: DeepSeek官方開源昇騰基礎元件，與昇騰共建高效易用的AI晶片軟體生態
source: 量子位
url: https://www.qbitai.com/2026/09/499263.html
model: claude-code/sonnet
generated_at: '2026-09-30T21:36:45.301558'
score: 104
---

📌 DeepSeek開源昇騰元件，V4.1單卡衝上5102 tokens/s

TL;DR：DeepSeek將GPU平臺的核心運算元與通訊庫搬到華為昇騰，並附上實測推理吞吐數據。

當大家還在討論「國產晶片能不能撐起大模型訓練」時，DeepSeek 直接把答案攤在檯面上：9月30日正式開源一整套面向昇騰算力平臺的基礎設施元件，與此前GPU平臺開源的內容一一對應，等於把自己的軟體棧複製了一份到昇騰生態。

🤔 **為什麼要重造一套基礎設施元件**

要讓大模型在不同硬體平臺上都跑得快，光有框架不夠，還需要針對硬體特性深度調優的底層運算元與通訊庫。DeepSeek過去在GPU平臺上已經開源過類似元件，這次則是把同一套設計思路搬到華為昇騰平臺，補齊了非GPU路線的高效能實作，也讓依賴昇騰算力的團隊有了現成的參考實作可用。

🧩 **DeepGEMM、FlashMLA 到 DeepEP，對應GPU版本一條龍**

本次開源涵蓋TileLang高階語言編譯工具、高效能運算元庫（DeepGEMM、FlashMLA、TileKernel、DeepSelect）以及分散式通訊庫DeepEP。華為方面提供了穩定開放的Ascend C API，讓開發者能深入調整訪存路徑與計算流水線；同時底層對接PTO ISA指令體系，支援TileLang這類高階語言直接編譯對接昇騰硬體。這個設計同時照顧到兩種開發者：既能讓資深工程師手工精細調優，也能讓一般開發者透過TileLang這類高階語言快速上手。

在網路架構上，華為與DeepSeek團隊聯合定義了昇騰SuperPoD Flex與UBL128組網方案，可支援128卡3.2Tbps單層交換的Scale-up網路，以及256K卡兩層交換的Scale-out網路，分別對應超低時延推理與前沿基座模型的大規模訓練需求。基於這套全互聯的UBL128超節點，昇騰提供了ASC-COMM高效能自定義通訊庫，而DeepSeek團隊開發的DeepEP通訊庫涵蓋EP／CP／PP／FSDP等模式下的通訊運算元。

📊 **通訊頻寬與推理吞吐的實測數字**

摘要中提到，DeepEP通訊庫實測互聯頻寬達到Dispatch 375 GB/s、Combine 347 GB/s，已接近硬體上限。而在大規模推理場景，基於EP32部署策略，offline推理模式下DeepSeek-V4.1-Flash的純模型效能（不含框架排程開銷）達到：

| TPOT | 每卡輸出吞吐 |
|---|---|
| 5ms | 2469 tokens/s |
| 10ms | 5102 tokens/s |

需要留意的是，這組數據採集自Offline推理模式，不包含Serving排程與框架負載均衡的影響，測試的Context Length為128K，且Dspark投機接受率為0.85，因此不能直接等同於線上服務的實際表現。

💡 **開源之外，還開放了一整套部署實踐**

除了核心元件，華為也把與DeepSeek聯合創新的成果放上了CANN社群，包括大EP低時延推理部署、單卡／單機部署、大規模訓練、超長文本KVcache池化，以及Agentic RL相關的實踐文件，等於是把從推理到訓練的完整鏈路都公開了參考做法。

🎯 **實務啟示**

對於必須在非GPU平臺上部署大模型的團隊，這批元件提供了現成的高效能運算元與通訊庫起點，省去從零調優Ascend C的成本；而TileLang這類高階語言的開放，也讓不打算深入底層指令集的團隊能用更熟悉的方式接入昇騰生態。

🔗 **來源**
- 標題：DeepSeek官方開源昇騰基礎元件，與昇騰共建高效易用的AI晶片軟體生態
- 作者／機構：量子位（本文由華為提供授權轉載）
- 連結：https://www.qbitai.com/2026/09/499263.html

#DeepSeek #Ascend #昇騰 #AIChip #OpenSource #FlashMLA #DeepEP #LLMInference #CANN #AIInfrastructure
