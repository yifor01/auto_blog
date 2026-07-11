---
title: Disaggregated prefill and decode for LLM inference on SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-llm-inference-on-sagemaker-hyperpod/
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:07:50.481447'
---

📌 【AWS 技術分享】拆分 Prefill 與 Decode，解決 LLM 推理的延遲尖峰問題

TL;DR：透過 DPD 將計算密集與記憶體密集的推理階段分開，消除長文本導致的 Token 生成停頓。

當你部署 LLM 時，是否發現只要有一個使用者輸入超長 Prompt，其他所有人的對話生成速度會突然卡頓？這是因為在傳統的共置（Colocated）部署中，Prefill 與 Decode 共享同一組 GPU，導致兩者產生嚴重的資源競爭。

🤔 **Prefill 與 Decode 的天生矛盾**

LLM 的推理過程分為兩個特性截然不同的階段，將它們強行放在一起會導致效能互搶：

- **Prefill 階段**：屬於「計算密集（Compute-bound）」。它需要平行處理整個輸入 Prompt 以生成初始的 KV cache。
- **Decode 階段**：屬於「記憶體密集（Memory-bound）」。它每次只生成一個 Token，極度依賴記憶體頻寬來存取模型權重與不斷增長的 KV cache。

當這兩個階段共用 GPU 時，一個長文本的 Prefill 任務會佔據大量計算資源，導致所有正在進行的 Decode 請求被迫停頓，造成每 Token 延遲（Inter-token latency, ITL）出現尖峰。

🧩 **DPD 架構：將推理階段徹底解耦**

為了消除幹擾，AWS 提出了 Disaggregated Prefill and Decode (DPD) 方案。其核心邏輯是將兩個階段執行在不同的 GPU 池中：

1. **獨立引擎**：將 Prefill 與 Decode 分配給專門的引擎，讓兩者可以採取不同的平行策略。
2. **高速連線**：透過 Elastic Fabric Adapter (EFA) 與遠端直接記憶體存取 (RDMA) 將兩個 GPU 池連線，確保 KV cache 能高效傳輸。
3. **獨立調優**：開發者可以分別針對「首個 Token 延遲 (TTFT)」與「Token 間延遲 (ITL)」進行獨立最佳化，這比單純調整分塊預填 (Chunked Prefill) 能更可靠地控制尾端延遲 (Tail latency)。

📊 **實作路徑與適用場景**

作者說明如何利用 vLLM 在 Amazon SageMaker HyperPod 上實作 DPD，並透過 HyperPod Inference Operator 進行部署。雖然 vLLM 已透過 continuous batching 與 PagedAttention 提升單機效率，但在大規模多節點部署時，路由最佳化與編排仍是挑戰。

**DPD 帶來最顯著增益的場景（長文本、高併發串流）：**
- 聊天助手 (Chat assistants)
- 代理工作流 (Agentic pipelines)
- 檔案分析端點 (Document-analysis endpoints)
- 帶有大量檢索內容的 RAG 應用

🎯 **實務啟示：你該選擇 DPD 還是共置部署？**

並非所有場景都需要 DPD。在選擇架構時，請根據工作負載決定：

- **選擇共置部署 (Colocated)**：若 GPU 競爭不是問題，例如離線批處理（追求 TTFT）、低併發部署，或僅處理短文本流量。
- **選擇 DPD 分離部署**：若你的應用面臨高併發且包含長文本輸入，且不能容忍因單一長 Prompt 導致的所有請求延遲飆升。

🔗 **來源**
- 標題：Disaggregated prefill and decode for LLM inference on SageMaker HyperPod
- 作者／機構：Xuan Lu @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-llm-inference-on-sagemaker-hyperpod/

#LLM #Inference #vLLM #AWS #SageMaker #HyperPod #KVcache #Latency #RAG #GPU
