---
title: NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/
model: claude-code/sonnet
generated_at: '2026-10-13T22:06:43.129633'
score: 92
---

📌 Run:ai 全面開源：NVIDIA 把 GPU 排程大腦交出來了

TL;DR：NVIDIA 將生產級的 Run:ai 平臺整個開源，MLOps 團隊現在能直接取用其 GPU 排程核心技術。

GPU 一張動輒數十萬元起跳,但大多數叢集的真實使用率長期偏低,原因往往不是硬體不夠,而是排程做得不夠聰明。NVIDIA 這次選擇把壓箱寶 Run:ai 平臺整個打開,讓所有人都能直接站在它的排程引擎上建東西。

🤔 **為什麼要把商用排程平臺開源**

過去幾年,NVIDIA Run:ai 幫助企業在 Kubernetes 上大規模運行 AI workload,透過動態分配 GPU 資源、管理從資料處理、訓練到推論的完整生命週期。這次開源是 NVIDIA DSX AI Factory Platform 擴展的一部分,目的是建立一個開放基礎,讓整個生態系能更快把差異化的解決方案帶到市場上,回應客戶不斷變化的需求。

🧩 **一個完整平臺,拆成四個可獨立使用的元件**

開源範圍包含完整的 Run:ai 平臺,以及四個可以獨立採用的核心元件:

- **KAI Scheduler**:驅動 Run:ai 的 Kubernetes-native 排程引擎,採用 Apache 2.0 授權,並已貢獻給 CNCF 作為 Sandbox 專案。它負責 gang scheduling(搭配記憶體內的預排程模擬,避免多 pod 任務被不必要地驅逐)、公平份額(fair-share,包含時間基礎的公平份額)與配額分配、拓撲感知與 bin-packing,以及 GPU 共享(支援 MIG、MPS、time sharing、HaMi、CUDA 13.4 MPS fractioning),還支援 Dynamic Resource Allocation(DRA)。
- **GPU Fractioning Operator**:支援 GPU 分割分配,讓多個 workload 共享單一 GPU 並具備硬體層級的記憶體隔離,可依需求即時申請,不需管理員事先在每個節點做設定,是互動式 notebook 與小模型推論場景中最常被使用的功能之一。
- **KAI Resource Management**、**Workload Map**:與上述元件、加上額外的平臺程式碼,共同組成完整的 Run:ai 平臺。

💡 **生態系已經動起來**

多家合作夥伴已著手整合這套開源平臺:Crusoe 把它整合進 Crusoe Managed Kubernetes;Mirantis 延伸進 k0rdent AI;Nebius 在 Nebius AI Cloud 提供一鍵部署;OpenNebula Systems 透過 OneKS 整合進其 AI Cloud Platform;Rafay 正把它擴展成全託管服務;Saturn Cloud 整合進 Token Factory 以支援白牌推論服務;Spectro Cloud 整合進 PaletteAI;vCluster 則提供預驗證的部署範本,在單一 GPU 機群上強化租戶邊界。

團隊可以透過 NVIDIA DSX AI Factory GitHub 組織下的 Run:ai 原始碼直接部署,也能在 NVIDIA NGC 以 Community Product 形式取得(含 Helm chart),下載需接受 NVIDIA 軟體授權條款,不需付費訂閱,但也不含 NVIDIA 企業支援。若需要企業級支援,仍可透過 NVIDIA Mission Control、NVIDIA AI Enterprise 或既有商用方案取得。

🎯 **實務啟示**

對於已經在用 Kubernetes 管理 GPU 叢集但苦於排程效率的團隊,KAI Scheduler 可以單獨部署在既有叢集中,不必整套搬遷到 Run:ai 平臺,是個低風險的切入點。若團隊更在意多租戶場景下的記憶體隔離與細粒度 GPU 分配,GPU Fractioning Operator 值得優先評估。

🔗 **來源**
- 標題:NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform
- 作者/機構:Tanya Lenz, NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/

#NVIDIA #GPUScheduling #Kubernetes #MLOps #OpenSource #AIInfrastructure #CloudNative #CNCF #RunAI #GPUOrchestration
