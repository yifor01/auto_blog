---
title: Co-Designing Sparse Attention for Efficient Long-Context Inference
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/co-designing-sparse-attention-for-efficient-long-context-inference/
model: claude-code/sonnet
generated_at: '2026-11-18T23:33:25.656524'
score: 116
---

📌 長文本推理的新瓶頸：不是attention，是找attention的那一步

TL;DR：NVIDIA拆解sparse attention的indexer設計，教你怎麼讓它在GPU上真正跑得快。

當context長度從數萬token一路推向數十萬，attention往往吃掉一個transformer層大半的prefill時間。解法聽起來很直覺：讓每個query只看一小部分key就好。但問題是，要先「找出」該看哪些key，這一步本身的成本並沒有消失，只是換了個地方藏起來。

🤔 **稀疏化省下的運算，去哪了**

Dense attention讓每個query對context裡的每個key都打分數，成本隨context長度N增加，128K token時幾乎佔掉一層prefill的大部分時間。Sparse attention的做法是讓每個query只關注少數（通常數千個）最相關的key，核心attention的成本因此不再隨N增加。但找出這k個key的元件，也就是indexer，仍然要為全部N個key打分數──成本沒有消失，只是從核心attention轉移到了indexer上。文章提到，在DeepSeek V3.2的prefill層中，indexer加上Top-k步驟就佔了47%的時間。

🧩 **三個階段：indexer打分、Top-k篩選、核心attention**

Sparse attention分三步：indexer為每個key打分，Top-k留下分數最高的k個，核心attention再對這k個key與value做softmax attention。後兩步的成本隨k增加，indexer的成本則隨N增加。

indexer本質上是一個小型attention區塊：幾個query head對一份indexer key cache打分，再透過ReLU與加權求和之類的後處理，把多個分數壓成一個logit。文章整理了近期模型的設計選擇：

| 方法 | Query heads | Key heads | 後處理 | 選取粒度 |
|---|---|---|---|---|
| DeepSeek Sparse Attention (DSA) | 64 | 1 | ReLU+加權求和 | Token |
| GLM 5.2 | 32 | 1 | ReLU+加權求和 | Token |
| NSA | 64 | 4 | Softmax | Block of 16 |
| MoBA | 32 | 8 | MeanPool on K | Block of 4096 |

多數設計採用單一key head（KH=1）、32到64個query head壓成一個分數，再以token或小區塊為選取單位。

📊 **Group size與推測解碼：prefill跟decode的反應完全相反**

indexer本質上是一個搭配融合epilogue的batched matmul。文章用運算強度（FLOPs對bytes的比例）分析發現：group size（即query head數除以key head數，簡記為G）越大，每個輸出logit能分攤到的運算量就越多；但prefill與decode對G的反應剛好相反。Prefill是運算密集，query head越多，耗時幾乎等比例增加。Decode則是記憶體密集，瓶頸在於讀取key cache，所以即使G從小變到16倍，實測decode的耗時也只變動2%左右，因為限制decode速度的始終是那一次key cache的讀取。

另一個有意思的發現跟推測解碼（speculative decoding）有關：當模型一次起草D個token並與新token一起驗證時，indexer要為D+1個query token打分，但只要這些token還能塞進對key cache的一次讀取裡，額外的草稿token幾乎不會增加額外耗時，相當於「幾乎免費」。

💡 **給模型設計者的具體線索**

這些測量結果意味著，context長度與壓縮比不影響FLOPs對bytes的比例，只會放大整體工作量；而decode階段的效能幾乎只取決於key cache的讀取次數,不是算了多少。這代表在設計indexer時，增加query head數或利用推測解碼的草稿token，在decode端幾乎是「白吃的午餐」，但在prefill端則要謹慎權衡，因為運算量會隨之成長。

⚠️ **這只是indexer設計空間的一角**

文章聚焦在「訓練進模型裡」的sparse attention，而非BLASST、MInference、Quest這類訓練後再套用的方法；測量也以特定的FP8 kernel設定（64K indexer key、Hsz=128、KH=1）為基準，不同設定下的具體數字會有差異。

🎯 **實務啟示**

對正在設計長context模型架構的工程師而言，indexer不是可以隨意塞進去的小元件，它的query head數、group size、是否搭配推測解碼，都直接決定了prefill與decode階段各自的效能曲線。在decode記憶體密集的特性下，多加幾個query head或草稿token幾乎不花額外時間，是值得優先利用的設計餘裕。

🔗 **來源**
- 標題：Co-Designing Sparse Attention for Efficient Long-Context Inference
- 作者／機構：Timmy Liu, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/co-designing-sparse-attention-for-efficient-long-context-inference/

#SparseAttention #LLM #Transformer #NVIDIA #GPU #LongContext #Inference #DeepSeek #AIInfrastructure #ModelArchitecture
