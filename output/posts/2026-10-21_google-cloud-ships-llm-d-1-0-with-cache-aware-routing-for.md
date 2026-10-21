---
title: Google Cloud Ships llm-d 1.0 With Cache-Aware Routing for TPU and GPU Fleets
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/
model: claude-code/sonnet
generated_at: '2026-10-21T20:53:55.518211'
score: 107
---

📌 Google Cloud 發布 llm-d 1.0：讓 TPU、GPU 叢集看懂「快取在哪」的推理協調層

TL;DR：開源、Kubernetes 原生的分散式推理框架正式邁入 1.0，多家採用者已公開生產環境實測數據。

當你的 agent 工作流一步步呼叫同一個模型，round-robin 負載平衡卻把每一步丟到不同的伺服器，上下文快取等於白做了。這正是 llm-d 要解決的問題，而它剛剛迎來第一個穩定版本。

🤔 **Round-robin 在 agent 與 RL 工作負載下會失效**

傳統負載平衡器不管每個請求背後的上下文，只負責把流量均分到各個節點。但自架的 agent 與 RL 訓練場景裡，同一個 session 往往會在短時間內反覆呼叫模型，如果每次都被導向不同的 vLLM 或 SGLang 實例，先前算好的 KV cache（鍵值快取）就無法複用，等於每一步都要重新計算一次上下文。llm-d 把這些獨立的模型伺服器整合成一個協調的資源池，讓 agent 呼叫同一個端點時，請求仍會被導向「已經持有該上下文」的那個實例。

🧩 **Prefix-aware 路由、KV 快取分層卸載與 prefill/decode 分離**

llm-d 的 router 建構在 Kubernetes Gateway API Inference Extension 之上，它會追蹤每個 replica 持有哪些快取的 prefix（前綴），再綜合考量當前負載與預測延遲，挑選最合適的 replica 來處理請求。當加速器記憶體被填滿，KV 快取會依序卸載到主機記憶體，再到 SSD 或 Managed Lustre，這套機制借助 vLLM 的 OffloadingConnector、Mooncake 或 SGLang 的 HiCache 來實作。llm-d 也把 prefill（處理輸入、運算密集）與 decode（逐 token 生成、受限於記憶體頻寬）拆成兩個獨立的資源池分別調度,因為兩者的運算特性本質不同。1.0 版的重點不是推出新功能,而是讓這些已經存在的能力（prefix-aware 路由、KV 卸載、prefill/decode 分離、wide expert parallelism、批次推理）能可靠地跑在生產環境,IBM 稱這階段為「day 2 operations」。

📊 **採用者的實測數字：快取命中率 75-80%，吞吐量翻 4 倍以上**

以下數字均為 Google 與 llm-d 採用者自行提供：

| 採用者 | 指標 |
|---|---|
| Snap | prefix 快取命中率達 75-80% |
| Zenteiq | 每千顆 TPU v6e 晶片每日 token 吞吐量從 14.7 億提升至近 60 億，逾 4 倍 |
| IBM 示範 | 同時服務 3,000 個程式碼 agent，成本比呼叫 API 低 5-10 倍 |

在 Google Cloud 上，GKE Inference Gateway 把 llm-d router 作為受管服務執行，可跨叢集、跨地區運作並提供全域容錯；KEDA 與 HPA 依佇列深度與預測延遲自動擴縮資源池；Kueue 則負責依模型分配配額。官方也提供已驗證的 Helm charts，可一次部署橫跨 TPU 與 GPU 的資源池並對外提供單一端點。

💡 **不是互斥的競品，是可以疊加的生態**

值得注意的是，llm-d 與 NVIDIA Dynamo 並非純粹的競爭關係：CoreWeave 同時運行 llm-d 與 Dynamo，NVIDIA 本身也把 Dynamo 的部分元件貢獻回 llm-d 專案。llm-d 由 Red Hat、IBM、Google Cloud、CoreWeave 與 NVIDIA 於 2025 年共同成立，目前由 Red Hat、IBM、Google 擔任主要維護者，吸引超過 25 個組織、500 多位貢獻者參與，已於 2026 年 3 月 12 日成為 CNCF Sandbox 專案，採用 Apache 2.0 授權。

🎯 **實務啟示**

Google 團隊建議採用分階段導入路徑：先在現有的 vLLM 部署前加上 prefix-aware 路由，驗證效果後再逐步加入流量控制、分層 KV 卸載，最後導入 prefill/decode 分離。對於已經在自架模型服務、且工作負載有明顯上下文重用特性（如多步驟 agent、RL rollout）的團隊，這是一條風險可控的升級路線，而且可以在 Prism 上比對已發表的效能數據，評估是否值得投入。

🔗 **來源**
- 標題：Google Cloud Ships llm-d 1.0 With Cache-Aware Routing for TPU and GPU Fleets
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/20/llm-d-1-0-open-source-distributed-inference-stack/

#LLMInference #Kubernetes #vLLM #SGLang #KVCache #GoogleCloud #OpenSource #DistributedSystems #TPU #GPU
