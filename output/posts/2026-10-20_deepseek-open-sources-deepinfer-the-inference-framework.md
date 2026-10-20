---
title: DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/
model: claude-code/sonnet
generated_at: '2026-10-20T20:50:21.893464'
score: 94
---

📌 DeepSeek開源DeepInfer:日跑155兆token的推理引擎

TL;DR:DeepSeek把支撐自家生產服務的推理框架DeepInfer開源,連帶公開token編解碼層deepseek-recipe。

多數前沿實驗室把推理堆疊當作最核心的商業機密,DeepSeek卻選擇把DeepSeek-V4.1-Flash背後真正跑在生產環境的引擎直接開源——這對開發者來說,是少有機會窺見frontier lab真實serving架構的時刻。

🤔 **這是什麼,解決誰的問題**

DeepInfer是DeepSeek自家模型的高效能推理引擎,依其GitHub README所述,它驅動著DeepSeek大規模的生產服務。這次釋出涵蓋離線推理(offline inference)在大規模場景下所需的核心功能,以Apache 2.0授權開放。同時釋出的deepseek-recipe則是MIT授權的token編解碼層。框架原本主要基於vLLM打造,並吸收了SGLang與TensorRT-LLM的設計想法。

🧩 **堆疊起來的五個系統層級設計**

DeepInfer在底層疊上DeepSeek自家的kernel:FlashMLA、DeepGEMM、DeepEP、TileKernels、DeepSelect,以及自訂的TileLang kernel。在這之上是五個系統層級的設計理念:

- **Attention用data parallelism**,MoE層則用expert parallelism搭配自家的expert-parallel load balancer(EPLB)。
- **Decode階段**在一個supernode內以EP64到EP128運行;**prefill階段**則用記憶體允許下最小的EP,通常是EP2到EP8。
- **推測解碼(speculative decoding)**:draft model每一步提出5個token,再由一個Confidence Head預測每個draft token的接受率,scheduler只驗證最有價值的prefix。據官方說法,這能把需要驗證的draft token數砍掉約30%(從5.00降到3.2–4.4),而實際被接受的長度幾乎沒變(3.29對3.20)。
- **Sliding window attention的快取命中最佳化**:命中快取時只重新計算最後128個token的attention狀態,讓重算成本固定不受context長度影響,DeepSeek表示這讓decoder層的總prefill運算量接近減半。
- **CPU/GPU重疊排程**:CPU端的batch排程與GPU執行重疊進行,讓GPU在步驟之間不空轉。

另外,batch-invariant inference與deterministic sampling目前僅支援NVIDIA平臺;structured outputs則支援regex、JSON schema與EBNF grammar。

📊 **部署規模與效能數字**

依其公開的部署Q&A,單一cluster每天服務155兆(trillion)個token,在谷值電價時段的GPU-hour整體營收為每小時38美元。DeepSeek針對DeepSeek-V4.1-Flash在131,072 context長度下公布了Pareto曲線(prefill用4張SM100 GPU,decode用64張,數字取自圖表,屬自我回報)。DSpark的動態驗證機制在每rank約60個序列時能帶來4%到7%的throughput提升,但在每rank僅16個序列時,反而比固定5-token驗證慢1.5%。內部版的FlashMLA decoding kernel比公開版快5%到10%,但端到端整體差距在5%以內。

硬體需求相對嚴格:只支援Linux,需要GCC 13以上、Python 3.12,以及CUDA 13或CANN 9.2;官方認為最小的有效生產單位是64張prefill GPU加64張decode GPU。

⚠️ **這只是一部分,完整生產系統還缺很多**

DeepSeek團隊明確說明,一套完整的服務還需要KV cache系統,以及VE/Prefill/Decode的disaggregation與跨data-parallel副本的load balancing,但這些元件與內部基礎設施高度耦合,因此這次並未一併開源。換句話說,拿到的是推理引擎本體,不是整套可以直接上線的serving平臺。

🎯 **實務啟示**

對於自己在跑大規模MoE模型serving的團隊,DeepInfer釋出的EPLB負載平衡、帶Confidence Head的推測解碼、以及sliding window固定成本重算這幾個設計,都是值得拆出來研究、甚至借鏡進自家推理堆疊的具體做法。但受限於嚴格的硬體與CUDA版本要求,加上KV cache與disaggregation等關鍵基礎設施並未隨附,要直接搬進自己的生產環境,仍需要補齊相當多的周邊系統。

🔗 **來源**
- 標題:DeepSeek Open-Sources DeepInfer, the Inference Framework Behind DeepSeek-V4.1-Flash
- 作者／機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/20/deepseek-deepinfer-open-source-inference-framework/

#DeepSeek #DeepInfer #LLMInference #OpenSource #MoE #SpeculativeDecoding #vLLM #GPUComputing #ModelServing #AIInfrastructure
