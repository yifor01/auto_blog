---
title: Tiered KV cache for large LLMs on Amazon SageMaker HyperPod with Curvine
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/tiered-kv-cache-for-large-llms-on-amazon-sagemaker-hyperpod-with-curvine/
model: claude-code/sonnet
generated_at: '2026-08-13T07:33:08.085477'
score: 98
---

📌 跨副本共用 KV Cache：Curvine 讓 SageMaker HyperPod TTFT 快 2.7 倍

TL;DR：用共享 NVMe 當 L2 KV cache 層，讓 vLLM 多副本免重複 prefill，TTFT 最高提升 2.7 倍。

相同的 prompt，只因為路由到不同的 vLLM 副本，就得重新計算一次，這是許多團隊在跑 LLM 推理時正在默默付出的隱形代價。

🤔 背景：KV Cache 的兩難

大量部署公開基礎模型（如 Qwen、Llama、DeepSeek 等）給多個 business line、RAG pipeline 或多輪對話應用的團隊，常陷入一個取捨：要嘛用超額配置的 GPU 機型硬撐持續成長的 KV cache，要嘛忍受變慢的 TTFT，因為相同的 prompt 在每次請求都被重新計算。

根因很直接：vLLM 在生成過程中會把每個已處理 token 的 attention key 與 value 存進 KV cache，避免重複計算；prefix caching 則讓有相同前綴（例如共同的 system prompt）的請求共用這份 cache。但在 ml.g6e.4xlarge（每 GPU 48 GB）這類高性價比機型上，扣除模型權重與 runtime 配置後，留給 prefix caching 的記憶體本就有限，模型越大、併發越高，這個空間就越緊。結果是長 prompt 的 cache 命中率下降，相同 system prompt 在每個請求都被重新 prefill，水平擴充的 vLLM 副本各自維護獨立 cache，一旦路由到不同副本，等同一次冷啟動。

🧩 三層快取架構：L0 GPU、L1 CPU、L2 Curvine 共享 NVMe

解法是在 Amazon SageMaker HyperPod 上建立一套分層 KV cache 架構，把快取延伸到 GPU 與 CPU 記憶體之外，進到共享的分散式 NVMe pool。這套架構建立在 HyperPod 的 Managed Tiered KV Cache 與 Intelligent Routing 兩項能力上，並加入輕量分散式快取檔案系統 Curvine，作為共享的 L2 層。

L0 是 vLLM 原生的 GPU prefix cache，即 paged-attention 層，存放存取延遲最低的熱門 KV block，容量取決於扣除模型權重後剩餘的 GPU 記憶體。以 7B 模型 bf16 為例，48 GB GPU 上權重約佔 14 GB，留給 KV block 的空間超過 30 GB，餘裕充足；但 32B 模型權重就約佔 64 GB，連單張 48 GB GPU 都放不下，分片後留給 KV 的空間更少，併發下很快被填滿並驅逐。

L1 是 CPU 記憶體卸載層，由 LMCache 接住從 GPU 被驅逐的 block，存進 host DRAM，在每個推理 Pod 內執行，透過 InferenceEndpointConfig CRD 中的 enableL1Cache: true 由 SageMaker HyperPod Inference Operator 自動管理，容量大小由 InstanceMemoryAllocationPercentage 決定（建議先設 20%）。

L2 才是跨副本重複使用真正發生的地方。Curvine 把 G6e／P5 機型內建的本機 NVMe 硬碟整併成單一命名空間，透過 FUSE client 以 ReadWriteMany PVC 掛載進每個推理 Pod；LMCache 透過 fs:// 連接器讀寫，讓分散式 pool 看起來就像本機目錄。由於所有 Pod 掛載相同命名空間，某個副本寫入的 KV block 可以立刻被其他副本讀取。Curvine 的 Primary Node（文件中稱 Master）負責 metadata 與 journaling，持久化在 Amazon EBS 上；Worker 元件跑在每個 GPU 節點，資料存在節點本機的 NVMe（通常掛載於 /opt/dlami/nvme/curvine-data）。若某個 Worker 掛掉，它持有的 cache 會被重新計算，因為這些 KV block 本來就是可重現的，沒有資料遺失疑慮。

前端則靠 HyperPod Inference Operator 內建的 router 做智慧路由：router 會維護一棵 prefix tree（prefix-aware 策略），或查詢每個 worker 的 cache 狀態（kv-aware 策略），挑選最可能命中 cache 的副本，整個過程對 client 端透明，不需要修改用戶端程式碼。

📊 測試結果：跨 Pod 命中率最高 100%，TTFT 最快提升 2.7 倍

在一次測試部署中，這套架構做到最高 100% 的跨 Pod cache 命中率、最高 2.7 倍的 TTFT 改善，以及約 1,900 token 的 prompt 在跨節點 L2 讀取延遲約 56 毫秒。對於 prompt 重疊度中高（粗估共享 leading token 超過 40%，例如共同 system prompt 或共用 RAG context）的 workload，跳過重新 prefill 能大幅降低 TTFT。這套架構也讓原本需要 P5 機型的 workload 得以改跑在成本更低的 G6e 機型上，降低每個 endpoint 的成本，實際節省幅度取決於模型大小與流量特性。

⚠️ 目前的限制

InferenceEndpointConfig CRD 的 l2CacheBackend 欄位原生只支援 redis 或 tieredstorage；要把 L2 指向 Curvine 的 FUSE 掛載點，需要手動 patch vLLM 容器規格中的 LMCACHE_REMOTE_URL 環境變數，指向 fs://localhost:0/mnt/curvine/l2cache/。

🎯 實務啟示

若推理流量有中高比例的 prompt 前綴重疊（共用 system prompt、共用 RAG context），把 KV cache 從單一 Pod 延伸成跨節點共享層，是用比升級 GPU 機型更低的成本換取 TTFT 改善的路徑。Curvine 讓 Worker 故障直接重算而非復原，代表這套架構不需要額外的資料保護機制，可以用相對簡單的方式擴充 NVMe pool 容量。

🔗 來源
- 標題：Tiered KV cache for large LLMs on Amazon SageMaker HyperPod with Curvine
- 作者／機構：Qingyuan Tang，AWS ML Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/tiered-kv-cache-for-large-llms-on-amazon-sagemaker-hyperpod-with-curvine/

#KVCache #vLLM #SageMakerHyperPod #Curvine #LLMInference #TTFT #AWS #DistributedSystems #LMCache #InferenceOptimization
