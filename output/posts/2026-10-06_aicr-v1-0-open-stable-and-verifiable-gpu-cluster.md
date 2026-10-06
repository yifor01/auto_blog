---
title: 'AICR v1.0: Open, stable, and verifiable GPU cluster configuration'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration/
model: claude-code/sonnet
generated_at: '2026-10-06T22:05:57.183076'
score: 68
---

📌 GPU 叢集版本地獄有解了：NVIDIA AICR 推出 v1.0 穩定版

TL;DR：NVIDIA AI Cluster Runtime v1.0 為 GPU Kubernetes 叢集提供版本鎖定、可驗證的設定配方，並正式凍結公開介面相容性承諾。

host kernel、GPU driver、container runtime、網路、儲存、operator、workload framework，每一項都有自己的發布節奏。一個在某個服務、某代 GPU、某版 Kubernetes 上跑得好的設定組合，換個環境可能就默默失敗，事後追版本衝突既慢又痛苦。這正是 NVIDIA AI Cluster Runtime（AICR）要解決的問題。

🤔 **為誰而做：被版本相容性折磨的 GPU 叢集維運者**

AICR 的定位很明確：它不是在教你怎麼寫新的訓練演算法，而是替 GPU 加速的 Kubernetes 叢集提供「版本鎖定、經過驗證的配方」。每份配方固定一組已知可以互相搭配的元件版本，並產出適用於 Helm、Argo CD、Flux、Helmfile 的部署產物，同時附帶在實測硬體上取得的簽署驗證證據。

🧩 **四個核心能力：Snapshot、Recipe、Bundle、Validation**

README 描述 AICR 提供四項刻意保持獨立的能力：Snapshot 記錄觀測到的叢集狀態（Kubernetes、作業系統、kernel、GPU、拓樸資訊）；Recipe 描述想要的、版本鎖定的元件設定，以及適用的限制條件與驗證階段；Bundle 把 Recipe 轉譯成操作者慣用部署工具的產物；Validation 則拿 Recipe 與觀測狀態比對,並在有宣告的情況下對叢集執行部署、相容性與效能檢查。舉例來說，操作者可以選定 EKS、GB300、Ubuntu、training、Kubeflow這些條件，解析出對應配方，為 Argo CD 渲染部署產物，透過既有 GitOps 流程部署，再用同一份配方驗證正在跑的叢集；就算改用 Helm、Flux 或 Helmfile 渲染，想要的設定結果也不會因此改變。

📊 **v1.0 的重點：把公開介面凍結成一份可依賴的相容性契約**

v1.0 針對 CLI（aicr）、REST API 與 OpenAPI 合約（aicrd）、Go SDK（github.com/NVIDIA/aicr/pkg/client/v1）、產出的 bundle 結構與 artifact schema 都設定了相容性規則，每個公開介面在合併變更前都要檢查既定基準線，v1.0 之後若要移除或不相容地變更一個穩定的公開介面，必須發新的主版本。文章提到，過去六個月 AICR 已從少數配方成長為涵蓋主要 Kubernetes 服務與目前 NVIDIA 加速器產品線的配方庫，並加入了線上叢集驗證、簽署證據、公開證據彙整與供應鏈驗證。目前專案已有超過 100 位貢獻者，近半數來自 NVIDIA 以外。生態系整合方面，Pulumi Labs 將 AICR 包裝成 infrastructure-as-code provider，Mirantis 的 k0rdent 則將其整合進多叢集管理。

⚠️ **安裝成功不代表配置正確**

文中特別點出一個容易被忽略的風險：就算每個元件都安裝成功，叢集也未必真的達到配方預期的設定。Installation 不會確認元件是否健康、gang scheduling 或 accelerator discovery 等能力是否真的可用,或是量測結果是否達到配方設定的效能門檻——這正是 Validation 這一步存在的理由。

🎯 **實務啟示**

如果你的團隊正在維護多個 GPU Kubernetes 叢集、同時要支援不同 GPU 代、不同雲端服務與部署工具，AICR 提供的價值不在於新演算法,而在於把「哪些版本組合能一起跑」這件事,從散落在維運手冊與個人經驗裡的知識,變成一份可查詢、可驗證、可版本化的配方。v1.0 的相容性承諾也意味著現在開始基於其 CLI／API／SDK 建自動化流程,風險比之前低很多。

🔗 **來源**
- 標題：AICR v1.0: Open, stable, and verifiable GPU cluster configuration
- 作者／機構：Elizabeth Goodman, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration/

#NVIDIA #Kubernetes #GPU #MLOps #DevOps #AICR #CloudInfrastructure #GitOps #OpenSource #InfrastructureAsCode
