---
title: 'Tencent Open-Sources DFly2: Speculative Decoding That Reuses the Target’s
  Sparse KV Cache'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/26/tencent-dfly2-speculative-decoding-sparse-models/
model: claude-code/sonnet
generated_at: '2026-11-28T00:39:31.290289'
score: 109
---

📌 【騰訊開源】DFly2免KV快取加速長文本推理

TL;DR：不佔用KV快取的推測解碼，長文本推理最高加速超過3倍。

推測解碼（speculative decoding）是加速LLM推理的常見招式，但在長文本場景下，drafter自己的KV快取反而成了拖油瓶——它得和真正的使用者請求搶記憶體。騰訊混元AI Infra團隊給出的解法很直接：讓drafter完全不保留自己的KV快取。

🤔 **長文本下，drafter的快取是隱藏成本**

推測解碼的原理是：用一個小型drafter提前猜測接下來的token，再讓目標模型一次驗證，確保輸出完全無損。問題是，一般的drafter要注意整個prefix，並儲存自己的KV快取；上下文越長，這份額外快取就越肥大，在高併發的agentic serving場景下，直接排擠掉本可服務更多請求的記憶體空間。

🧩 **讓drafter直接借用目標模型的稀疏注意力**

DFly2是騰訊混元AI Infra團隊打造的區塊平行（block-parallel）推測解碼drafter，專門給DeepSeek-V4.1-Flash、GLM-5.3-Flash、騰訊自家Hy4 flash這類天生具備稀疏注意力的模型使用。它把每一層draft層，與目標模型中對應的一層稀疏注意力層綁在一起，共享其中兩項資訊。

論文指出，在DeepSeek-V4.1-Flash上，提前一步做的selection，能覆蓋後續區塊token實際選中內容的近90%；而同樣大小的滑動視窗（sliding window）只能覆蓋不到20%。靠著這種共享機制，每個draft token最多只需要關注約2K個key，代表無論上下文多長，drafting成本大致維持不變。DFly2還直接跳過prefill階段，prefill到decode的轉換只需傳遞一份最後一層的hidden state；相較之下，一個傳統三層drafter的快取，在每個token上要額外負擔的記憶體遠超過這個數字（bf16，論文Table 2）。

📊 **記憶體省下來，速度也上去了**

- 在32K上下文下，拿掉drafter自己的KV快取，讓同一記憶體池多容納1.73倍的請求數。
- 以重新用相同配方訓練的DFlash、DSpark作為對照：一般工作負載下，平均接受長度（τ）領先較強baseline 3.9%至10.5%；在長文本與agentic工作負載（最長到128K）上，領先幅度擴大到10.0%至31.5%。
- 在agentic測試集上，DFly2的平均表現與一般工作負載相比，差距維持在4%以內；DSpark的表現則下滑11%至21%。
- 端到端加速（greedy、concurrency=1）：DeepSeek-V4.1-Flash達2.97倍，GLM-5.3-Flash達2.36倍，Hy4 flash達3.19倍。
- 在DeepSeek-V4.1-Flash上，於相同serving吞吐量下，每位使用者的decode速度比DSpark快15%至24%。
- 騰訊官方公告另外給出Hy4 flash在agentic任務上的數字：decode最高加速4.2倍，比同配方DSpark快約30%，接受的token數比開源版DSpark多10.4%。

以上數字均為騰訊自行公布，baseline為用同一套配方重新訓練過的DFlash與DSpark。

🎯 **怎麼用上它**

DFly2已經隨tencent/Hy4-flash（總參數220B、約12B啟用的MoE模型，支援1M上下文）一起開源。vLLM可透過vllm/vllm-openai:hy4-flash映像檔，以dfly這個推測解碼方法直接serve，在官方recipe中已預設開啟；SGLang則透過lmsysorg/sglang:hy4-flash映像檔，以DFLY演算法提供同等支援。如果想把DFly2套用在自家的稀疏模型上，可以使用AngelSpec訓練，其quick start設定需要一個節點、8張GPU（4張做推理、4張做訓練）。

🔗 **來源**
- 標題：Tencent Open-Sources DFly2: Speculative Decoding That Reuses the Target's Sparse KV Cache
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/26/tencent-dfly2-speculative-decoding-sparse-models/

#SpeculativeDecoding #Tencent #LLMInference #KVCache #MoE #vLLM #SGLang #DeepSeek #LongContext #AIInfra
