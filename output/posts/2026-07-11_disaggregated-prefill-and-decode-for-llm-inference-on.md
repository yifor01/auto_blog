---
title: Disaggregated prefill and decode for LLM inference on SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-llm-inference-on-sagemaker-hyperpod/
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T09:39:31.033536'
---

📌 **SageMaker 實戰：用 DPD 解耦 LLM 推理延遲**

TL;DR：AWS 展示在 HyperPod 上將 LLM 的 Prefill 與 Decode 分離至不同 GPU 群組，徹底消除長提示對即時生成的阻塞。

🎣 **單一長提示讓所有請求停擺？**

當多個使用者同時傳送包含大量上下文的請求時，傳統的共用 GPU 架構會發生什麼事？處理最長的提示會佔用所有運算資源，導致其他正在生成 Token 的請求被迫暫停。這不僅是效率問題，更是體驗災難。

🤔 **背景：LLM 推理的兩張面孔**

大型語言模型的推理過程，本質上由兩個截然不同的階段組成，它們對硬體資源的需求也完全不同：

1.  **Prefill（預填充）**：這是**運算密集型**階段。模型需要並行處理整個輸入提示（Prompt），計算出初始的鍵值快取（KV Cache）。這需要大量的矩陣乘法運算能力。
2.  **Decode（解碼）**：這是**記憶體頻寬密集型**階段。模型一次只生成一個 Token，但必須頻繁地從記憶體中讀取模型權重和不斷增長的 KV Cache。這嚴重依賴記憶體頻寬，而非單純的運算速度。

當這兩個階段共用同一張 GPU 時，運算密集的 Prefill 會搶走記憶體頻寬資源，導致正在進行 Decode 的請求出現延遲 spike。

🧩 **方法：Disaggregated Prefill and Decode (DPD)**

AWS ML 工程師 Xuan Lu 在 Amazon SageMaker HyperPod 上實作了一種稱為「解耦預填充與解碼」（Disaggregated Prefill and Decode, DPD）的架構。其核心設計理念如下：

*   **物理分離**：不再讓 Prefill 和 Decode 共享 GPU，而是將它們分配到獨立的 GPU 群組（GPU pools）。
*   **高速互連**：這兩個獨立的群組透過 Elastic Fabric Adapter (EFA) 連線，利用 Remote Direct Memory Access (RDMA) 技術進行低延遲、高頻寬的 KV Cache 傳輸。
*   **專屬最佳化**：由於硬體資源分離，工程師可以針對每個階段採用不同的平行策略。例如，Prefill 節點可以專注於最大化吞吐量，而 Decode 節點則專注於最小化延遲。

這種架構讓 vLLM（透過 HyperPod Inference Operator 整合）能夠獨立調控首字延遲（TTFT）和詞間延遲（ITL），且比傳統的 chunked prefill 調參更穩定、更容易控制尾部延遲。

📊 **適用場景與收益**

根據文章指出，DPD 並非適用於所有情況，它在特定負載下展現最強優勢：

*   **高併發串流工作負載**：如聊天機器人（Chat assistants）、Agentic pipelines。
*   **長上下文應用**：檔案分析端點、以及檢索增強生成（RAG）系統，特別是當檢索到的上下文非常龐大時。

**為什麼有效？**
在傳統共置部署中，一個長提示的 Prefill 會阻塞在途中的所有 Decode 請求。DPD 從架構上消除了這種幹擾，確保長提示的處理不會影響其他使用者的即時反應速度。

**何時不適用？**
如果 GPU 爭用不是主要問題，共置部署仍是更簡單的選擇。這包括：
*   批次處理或離線工作負載。
*   低併發量的部署。
*   僅有短提示的交通流量。

💡 **深入分析：工程價值的轉移**

過去，最佳化 LLM 推理往往集中在單節點的效能提升，如 vLLM 引入的 Continuous Batching 和 PagedAttention。然而，當規模擴展到多節點叢集時，資源排程與路由成為瓶頸。

DPD 的意義在於它承認了「運算」與「記憶體頻寬」的爭奪是本質衝突。透過 RDMA 將中間狀態（KV Cache）從運算節點傳送到解碼節點，雖然增加了網路複雜度，但換來了極高的隔離性。對於服務於成千上萬使用者的企業級 RAG 系統而言，這種「寧願多花一點網路延遲，也不願讓單一請求卡住所有人」的設計哲學，是提升 SLA（服務等級協議）可靠性的關鍵一步。

🎯 **實務啟示**

1.  **檢視你的負載特徵**：如果你的應用經常處理超過 10k tokens 的上下文，且要求低延遲回應，考慮評估 DPD 架構。
2.  **基礎設施準備**：實作 DPD 依賴於高速網路（如 AWS EFA）。確保你的叢集具備支援 RDMA 的網路硬體，否則分離帶來的收益可能被網路瓶頸抵消。
3.  **工具鏈整合**：目前此方案透過 SageMaker HyperPod Inference Operator 與 vLLM 整合。若你已在使用 AWS 生態系，這是一個無需改寫模型程式碼即可提升效能的基礎設施選項。

🔗 **來源**
- 標題：Disaggregated prefill and decode for LLM inference on SageMaker HyperPod
- 作者／機構：Xuan Lu @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/disaggregated-prefill-and-decode-for-sagemaker-hyperpod/

#AWS #SageMaker #LLM #Inference #DeepLearning #vLLM #RDMA #CloudComputing #MLOps #PerformanceOptimization
