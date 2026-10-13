---
title: Run multi-node inference workloads using Ray LLM Deep Learning Containers
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/run-multi-node-inference-workloads-using-ray-llm-deep-learning-containers/
model: claude-code/sonnet
generated_at: '2026-10-12T23:59:43.451144'
score: 80
---

📌 用 Ray LLM DLC 在 EKS 上做 Prefill/Decode 分離推理

TL;DR：AWS 推出支援多節點的 Ray LLM Deep Learning Container，讓你不必手動拼裝 GPU 相依性，就能跑 prefill/decode 分離的 LLM 推理服務。

LLM 推理有兩種性格完全不同的階段：prefill 負責一次性消化整段輸入、吃的是算力；decode 負責逐 token 生成、吃的是記憶體頻寬。把兩者塞在同一張 GPU 上，長 prompt 的運算很容易拖慢正在進行中的生成請求。AWS 這篇文章示範了如何把兩個階段拆開，分別跑在不同節點上。

🤔 **為什麼要把 prefill 和 decode 拆開跑**

當模型太大塞不進單一 GPU、需要更高輸出量，或是想避免長 prompt 干擾正在生成的回應時，客戶通常得自己搭建相依性：挑選相容的 GPU 堆疊函式庫，並在某個元件版本飄移時除錯，這是會吃掉大量工程時間、卻無法直接產生價值的工作。AWS Deep Learning Containers（DLC）原本就是為了解決訓練與推理場景的這類問題而生，而這次推出的多節點 Ray LLM DLC，把同樣的做法延伸到多節點推理。

🧩 **架構：一個 OpenAI 相容端點，背後兩種節點各司其職**

這套 DLC 內建 vLLM 作為推理引擎、Ray Serve LLM 作為服務層、NIXL 負責跨節點的 KV cache 傳輸，以及 EFA 堆疊（libfabric 與 aws-ofi-nccl）負責節點間的高頻寬通訊。

實際部署在一個 Amazon EKS 叢集內：一臺 CPU 系統節點（m7i.xlarge）跑 KubeRay operator 與 Ray head pod；兩臺 GPU 工作節點（g6.8xlarge）各自負責 prefill 與 decode 階段，並且兩臺 GPU 工作節點的所在的節點群組被限定在單一可用區（Availability Zone），因為 EFA 無法跨可用區運作。

一筆請求的流動路徑大致是：使用者請求先抵達 CPU 系統節點上的 Ray head → 轉給 prefill 工作節點，平行處理整段輸入 prompt 並建立 KV cache → KV cache 透過 NIXL、經由 EFA 的 libfabric 後端傳給 decode 工作節點 → decode 節點逐 token 生成回應並回傳。

由於 Ray Serve LLM 內建應用程式建構器，整個服務應用其實就是一份 YAML：一個名為 `build_pd_openai_app` 的輔助函式，接收 prefill 設定與 decode 設定，就能把兩者之間的 KV cache 傳輸串接起來，背後統一對外暴露一個 OpenAI 相容端點，不需要寫 handler class，也不需要自建映像檔。

幾個關鍵設定值得注意：`max_model_len: 4096` 讓上下文長度對齊實測的 KV cache 大小；`dtype: bfloat16` 與 `gpu_memory_utilization: 0.90` 控制精度與 vLLM 可佔用的顯示記憶體；`enforce_eager: true` 跳過 CUDA graph 擷取以降低峰值 GPU 記憶體用量（效果依模型與輸入而異）。真正讓分離架構運作起來的關鍵，是 `kv_transfer_config`：兩端都使用 `NixlConnector`，`kv_role` 設為 `kv_both`，並各自配置獨立的 `engine_id`。文中特別強調，最關鍵的一行設定是 `kv_connector_extra_config: { backends: ["LIBFABRIC"] }`——沒有這行，NIXL 會預設走 UCX，即使底層有 EFA，速度也只會停在 TCP 等級。

工作節點的 pod 各自請求一張 GPU 與一個 EFA 介面（`nvidia.com/gpu: "1"`、`vpc.amazonaws.com/efa: "1"`），並以 `privileged: true` 執行，因為 NIXL 需要把 CUDA 顯示記憶體註冊給 EFA 網卡，單靠 IPC_LOCK 權限並不夠。

📊 **權重載入時間從約 145 秒降到約 2 秒**

文中提到，針對 Qwen3.5-9B 模型，在 g6.8xlarge 搭配上述快取設定下，重啟時的模型權重載入時間從約 145 秒降到約 2 秒。

🎯 **實務啟示**

這套方案特別適合 RAG、文件摘要、agentic 應用這類同時存在長 prompt 與延遲敏感生成的場景。如果團隊已經在用 EKS 搭配 KubeRay，直接拉這個 DLC 映像檔，可以省掉自行兼容 CUDA、vLLM、NIXL、EFA 版本相依性的工作，把時間留給模型與應用邏輯本身。

⚠️ **限制**

GPU 節點群組必須限定在單一可用區內，因為 EFA 無法跨可用區運作；整篇文章聚焦在既有工具（Ray Serve、vLLM、NIXL、EFA）的整合與部署流程，屬於基礎設施工程落地，而非新的演算法突破。

🔗 **來源**
- 標題：Run multi-node inference workloads using Ray LLM Deep Learning Containers
- 作者／機構：Ananth Raghavendra（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/run-multi-node-inference-workloads-using-ray-llm-deep-learning-containers/

#AWS #RayServe #vLLM #LLMInference #KubernetesML #EKS #PrefillDecode #NIXL #DeepLearningContainers #DistributedInference
