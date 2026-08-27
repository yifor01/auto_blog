---
title: Experiment with Qwen3.8-Flash-Next on NVIDIA GB300 NVL72 for Agentic Coding
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/experiment-with-qwen3-8-flash-next-on-nvidia-gb300-nvl72-for-agentic-coding/
model: claude-code/sonnet
generated_at: '2026-08-27T17:15:56.801682'
score: 113
---

📌 【NVIDIA×Alibaba】Qwen3.8-Flash-Next 用混合架構突破長上下文瓶頸

TL;DR：Alibaba 釋出 Qwen4 架構預覽版 Qwen3.8-Flash-Next,NVIDIA 提供 Day 0 全平臺支援,主打百萬 token 級的 agentic coding 場景。

上下文長度一路衝到百萬 token,但真正卡住推論效能的,往往不是模型多聰明,而是 attention 運算量與 KV cache 記憶體隨長度線性膨脹。Qwen3.8-Flash-Next 想解的,正是這個瓶頸。

🤔 **長上下文的老問題：attention 與 KV cache**

隨著上下文變長,attention 運算與 KV cache 記憶體用量會成為推論瓶頸。Alibaba 釋出的 Qwen3.8-Flash-Next 是一個多模態混合專家（MoE）模型,主模型參數量 125B,另外搭配 51B 參數的 N-gram embeddings,每個 token 實際啟動 6B 參數,原生上下文視窗達 262,144 token,透過 YaRN 可延伸至 1M token。

🧩 **GDN + QSA 混合架構**

模型採用 Gated DeltaNet（GDN）與 Qwen Sparse Attention（QSA）的混合設計：每四層中有三層使用 GDN,持續將歷史上下文壓縮成固定大小的循環狀態,消除 KV cache 隨序列長度增長的問題；剩下一層使用 QSA 做全上下文的精確檢索。與過去依賴 token 級索引、隨上下文變長而運算成本急遽上升的稀疏 attention 方法不同,QSA 將序列聚合成微區塊（micro-block）,在區塊層級估計重要性,只選取最相關的區域,藉此降低每層的 attention 運算與索引開銷,與 GDN／QSA 交替的架構設計相輔相成。

📊 **效能數據：7.6 倍 prefill 加速、GB300 NVL72 破萬 token/秒**

根據 Alibaba 公布的基準測試,QSA 相較全 attention,其 attention kernel 在 prefill 階段最高可加速 7.6 倍,decode 階段加速 4.9 倍。在 1M token 上下文、90% 前綴快取命中率的重快取線上服務測試中,Qwen3.8-Flash-Next 的 prefill 吞吐量達 Qwen3.7-Plus 的 8.6 倍。

在硬體端,GB300 NVL72 機架整合 72 顆 NVIDIA Blackwell Ultra GPU,透過 130 TB/s 的 NVLink 網域實現高效的全對全（all-to-all）通訊,避免專家路由流量跨越傳統網路造成的瓶頸。實測顯示,在 GB300 NVL72 上運行 Qwen3.8-Flash-Next,單 GPU 可達每秒超過 16K token 的吞吐量,單使用者延遲對應每秒超過 200 token。

💡 **從機架到桌機的完整支援**

NVIDIA 提供 Day 0 最佳努力（best-effort）功能支援,涵蓋 SGLang、vLLM 與 NVIDIA TensorRT-LLM 三套推論引擎,並在 GB300 NVL72 上完成驗證。除了機架級部署,模型也能在 NVIDIA DGX Station、DGX Spark 叢集,以及搭載四張 NVIDIA RTX PRO 6000 Blackwell Max-Q Workstation Edition GPU 的工作站上運行,讓開發者可以先在本地硬體上原型驗證 agentic coding 工作流程,再將同一模型擴展到 GB300 NVL72 做正式服務。後訓練方面,NVIDIA NeMo AutoModel 提供 PyTorch 原生的微調函式庫,支援 Hugging Face checkpoint 直接載入（無需模型轉換）,並支援完整 SFT 或記憶體效率更高的 LoRA 微調；若要進一步做強化學習,則可搭配 NVIDIA NeMo RL 的訓練配方。

🎯 **實務啟示**

這個模型鎖定的是高流量、上下文密集的應用場景，例如 agentic coding、文件處理與工具驅動的工作流程。對於需要處理長文件或多輪工具呼叫的團隊，GDN 帶來的固定大小狀態意味著記憶體用量不再隨對話輪數線性增加，是評估長上下文 agent 架構時值得關注的設計方向。開發者可先透過 QwenCloud 試用，或從 Hugging Face、ModelScope 下載權重自行部署評估。

🔗 **來源**
- 標題：Experiment with Qwen3.8-Flash-Next on NVIDIA GB300 NVL72 for Agentic Coding
- 作者／機構：Michelle Horton，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/experiment-with-qwen3-8-flash-next-on-nvidia-gb300-nvl72-for-agentic-coding/

#Qwen #NVIDIA #GB300NVL72 #LongContext #MoE #AgenticCoding #SparseAttention #LLMInference #Blackwell #OpenWeights
