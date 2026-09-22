---
title: Enabling Private High-Performance Production AI Inference with NVIDIA Confidential
  Computing
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing/
model: claude-code/sonnet
generated_at: '2026-09-22T20:33:41.546137'
score: 89
---

📌 NVIDIA機密運算上線，AI推理效能只掉不到5%

TL;DR：CC-aware最佳化讓TensorRT LLM在機密運算開啟下仍保留96%以上的輸出吞吐量。

當LLM推理開始處理病歷、合約、企業機密prompt時，「資料在記憶體裡是明文」本身就是風險。但機密運算過去給人的印象是「安全但慢」，這次NVIDIA用實測資料回應了這個疑慮。

🤔 機密運算為什麼會拖慢推理

NVIDIA Confidential Computing（CC）透過記憶體加密的confidential virtual machines（CVM）、confidential GPU 與加密的NVLink，讓LLM推理全程在受信任環境中執行，藉此保護專有模型與敏感prompt在「使用中」的安全。但CC啟用後，會改變推理框架原本對記憶體搬移、時間量測、排程與多GPU通訊的假設，如果推理框架沒有針對這些變化調整，就會產生額外效能負擔。

NVIDIA以TensorRT LLM為例，說明推理框架該如何跟CC環境「一起最佳化」，才能在啟用安全防護的同時盡量維持效能。

🧩 三個關鍵調整點

NVIDIA的效能工程團隊分析出CC啟用後，TensorRT LLM需要因應的三個主要瓶頸：

- **Host-to-device資料搬移**：在B200 CC架構下，host到device的傳輸必須經過軟體加密的bounce buffer，因為GPU無法直接存取受保護的CVM記憶體。這讓pinned memory失去原本非同步傳輸的優勢，部分複製甚至會阻塞呼叫執行緒。TensorRT LLM因此改用CC-aware的記憶體選擇策略，在受影響路徑改用pageable memory，並把重複的token與取樣資料回讀搬到非同步worker執行，避免decode階段被受保護複製卡住主排程器。
- **Kernel autotuner計時失準**：autotuner原本用CUDA events比較候選執行策略的效能，但在CC環境下CUDA-event時間戳會出現不穩定訊號，可能導致autotuner選到較慢的策略。TensorRT LLM因此在CC環境下改用GPU的%globaltimer量測，非CC環境仍維持CUDA events。
- **多GPU通訊選擇**：B200 CC組態不支援NVLS（NVLink SHARP）multicast，若框架仍預設走NCCL_SYMMETRIC，反而會白白付出記憶體註冊與跨rank同步成本卻拿不到multicast的好處。因應之道是偵測NVLS可用性，依訊息大小、拓撲與工作負載特性選擇合適的通訊演算法。

📊 測試方法與數據：CC on/off對照

為了讓CC造成的效能差異可被觀察到，NVIDIA刻意挑選長輸入、長輸出、低併發的工作負載，這類負載讓prefill階段的資料搬移、decode階段的per-token負擔更明顯，且併發不足以互相掩蓋延遲。

測試以`nvidia/DeepSeek-R1-0528-NVFP4`搭配TensorRT LLM（PyTorch backend）進行，輸入/輸出序列長度為32K/1K，併發數涵蓋1、2、4、8、16，並行策略為TP=8、EP=1、PP=1，KV cache採FP8。硬體為8張NVIDIA B200 GPU的DGX B200系統，Host端為Intel TDX、Ubuntu 25.10；Guest端為Ubuntu 24.04.4 LTS，配置256個vCPU。

在維持模型、硬體、框架版本、序列長度、並行度與併發數完全一致的前提下，僅切換CC on/off做對照，衡量兩項指標：輸出吞吐量保留率（CC on輸出tokens/s ÷ CC off輸出tokens/s）與Time Per Output Token（TPOT）延遲負擔。

結果顯示，在併發1到16的區間，CC on保留了CC off基準96.1%到98.2%的輸出token吞吐量，平均TPOT延遲負擔則落在1.2%到4.3%之間。

💡 安全與效能不是二選一，而是要一起設計

這份實測的意義在於，機密運算並沒有消除效能工程的必要性，反而讓「框架是否感知CC環境」變得更重要。若TensorRT LLM沒有做上述三項調整，直接把CC當成透明的底層開關，實際負擔恐怕會更明顯。

🎯 實務啟示

對正在評估機密推理的AI平臺工程師來說，這篇文章給出一套可複製的方法論：挑選長context、低併發的工作負載來放大CC效應，固定其餘變數只切換CC on/off，量測吞吐量保留率與TPOT延遲負擔。啟用CC前，務必用自己實際要serve的workload做一次CC-on/off的基準測試，而不是假設安全與效能必然互斥。

🔗 來源
- 標題：Enabling Private High-Performance Production AI Inference with NVIDIA Confidential Computing
- 作者／機構：Tanya Lenz, NVIDIA
- 連結：https://developer.nvidia.com/blog/enabling-private-high-performance-production-ai-inference-with-nvidia-confidential-computing/

#NVIDIA #ConfidentialComputing #TensorRTLLM #LLMInference #Blackwell #AIInfrastructure #DataPrivacy #GPU #MLOps #DeepSeekR1
