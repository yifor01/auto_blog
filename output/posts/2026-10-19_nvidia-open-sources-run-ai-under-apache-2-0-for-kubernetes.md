---
title: NVIDIA Open Sources Run:ai Under Apache 2.0 for Kubernetes GPU Orchestration
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/18/nvidia-runai-open-source-gpu-orchestration-kubernetes/
model: claude-code/sonnet
generated_at: '2026-10-19T21:43:44.772976'
score: 92
---

📌 【NVIDIA】開源 Run:ai，K8s GPU 排程全面開放

TL;DR：NVIDIA 把正式環境等級的 GPU 排程平臺 Run:ai 以 Apache 2.0 開源，K8s 團隊不必付費訂閱也能自架。

過去要在 Kubernetes 叢集上做到生產等級的 GPU 配額管理與排程，多半得簽下商用合約。現在 NVIDIA 把整套 Run:ai 原始碼搬上 GitHub，平臺團隊可以直接檢視、fork、自行部署，這也讓 Run:ai 正式成為 NVIDIA DSX AI Factory 平臺的一部分。

🤔 **Run:ai 是什麼、解決誰的問題**

Run:ai 是一套跑在 Kubernetes 之上的 AI workload 與 GPU 編排平臺，用來排程開發、訓練與推論工作負載，讓這些工作共享同一批 GPU 叢集。它不是要取代 Kubernetes，而是疊加在上面提供 GPU 感知的排程能力。使用者可以透過 Web UI、CLI、REST API，或是給 AI 助理用的 MCP server 來操作。架構上分成控制平面（負責 workload 提交、資源管理與監控）與跑在每個 K8s 叢集上的叢集服務（負責 GPU 感知排程）。

🧩 **四個可獨立採用的元件**

NVIDIA 把這次釋出拆成四個元件，團隊可以依需求分別導入。本地開發的流程靠一支腳本 `local-dev.sh` 完成：它會在容器內從原始碼建置約 50 個 Go 服務，接著建立一個固定在 Kubernetes v1.32.5 的 5 節點 Kind 叢集。預設情況下，一個假的 GPU operator 會模擬 8 張 Tesla A10，所以不需要真實 GPU 硬體就能跑起整套系統；加上 `--gpu-operator` 參數則可切換成真實 NVIDIA GPU，但這個模式需要 Linux、Docker 與 NVIDIA Container Toolkit，目前不支援 AMD 與 Intel 加速器。

部署方式上，團隊可以直接從原始碼建置，或是透過 NGC Community Product 的 Helm chart 安裝，這個版本不需要付費訂閱，但也不包含 NVIDIA 企業級支援。此外，也可以透過八家 DSX 生態系夥伴採用，包括 Crusoe、Mirantis、Nebius、OpenNebula Systems、Rafay、Saturn Cloud、Spectro Cloud 與 vCluster；若需要正式支援，則仍可走 NVIDIA AI Enterprise、NVIDIA Mission Control，或部分雲端市集的商用版本。

🧩 **兩個配套專案：Model Streamer 與 Grove**

Model Streamer 負責把模型權重直接串流進 GPU 記憶體，vLLM 與 SGLang 可透過 `--load-format runai_streamer` 啟用。Microsoft 公布的 benchmark 在 8 張 NVIDIA H100 的 VM 上測試，顯示比預設載入方式快 3 到 6 倍，吞吐量維持在 80 Gbps，相較預設路徑的約 40 Gbps。另一個專案 Grove 則負責編排多元件的推論工作負載，例如把 prefill 與 decode 這類元件當作「全有或全無」的單位一起啟動。

⚠️ **跟 Volcano、Kueue、YuniKorn 的差異**

關鍵差異在於涵蓋範圍：Volcano、Kueue、YuniKorn 專注在排程或佇列管理，而 Run:ai 是在排程器之上提供完整的管理平臺。

🎯 **實務啟示**

對已經在用 Volcano 或 Kueue 做基礎排程的團隊來說，Run:ai 開源版提供了一個可以直接檢視原始碼、依需求自行擴充的管理層選項；本地開發腳本搭配假 GPU operator，也讓評估這套系統不再需要先備好實體 GPU 叢集。

🔗 **來源**
- 標題：NVIDIA Open Sources Run:ai Under Apache 2.0 for Kubernetes GPU Orchestration
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/18/nvidia-runai-open-source-gpu-orchestration-kubernetes/

#NVIDIA #Kubernetes #GPUOrchestration #RunAI #MLOps #OpenSource #ApacheLicense #AIInfrastructure #vLLM #CloudNative
