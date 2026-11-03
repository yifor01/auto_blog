---
title: Support New AI Frameworks Faster Using NVIDIA Workload Map
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/support-new-ai-frameworks-faster-using-nvidia-workload-map/
model: claude-code/sonnet
generated_at: '2026-11-03T00:14:20.795120'
score: 73
---

📌 一份 YAML 讓排程器看懂所有分散式 K8s 工作負載

TL;DR：NVIDIA Workload Map 用共用描述取代框架專屬 adapter，加速新 AI 框架的排程支援。

在 Kubernetes 上跑一個分散式訓練任務，從來不是「一個 pod」這麼簡單，而是一整棵由角色、replica 數、pod template 和狀態欄位組成的資源樹——問題是，JobSet、LeaderWorkerSet、PyTorchJob 這些框架各自用不同方式描述這棵樹，工具每多支援一種框架，就得多寫一套 adapter。

🤔 **每個新框架都是一次重複的工程**

NVIDIA Run:ai 團隊在打造自家平臺時就撞上了這個問題：面對每一種新的 CRD（Custom Resource Definition），開發者得重新回答同樣的問題——這個工作負載的結構是什麼？它的 status 要怎麼轉換成一個「階段」？怎麼修改 pod spec 而不破壞工作負載本身？每回答一次，就產生一套專屬 adapter，而客戶每帶來一個新框架,就等於多一個待辦的 roadmap 項目,這也是為什麼支援新工作負載類型往往得等到下一個版本。

文章用一個實際的 JobSet manifest 示範這個痛點：一個 leader、兩個 worker，每個 pod 要求 4 張 GPU，總計申請 12 張 GPU。但用 `kubectl get jobset,jobs,pods` 查詢時，JobSet、三個 Job、三個 pod 全部被列成互不相關的獨立資源，owner reference 雖然串連了 Job 與 JobSet，平臺仍需要額外的定義才能理解它們的角色關係、進而加總 GPU 用量。

🧩 **把「框架知識」從程式碼搬進 YAML**

NVIDIA Workload Map（前身為 Karta，CRD 的 resource kind 仍叫 Karta）以 Kubernetes CRD 加上一套 Go library 的形式提供一份共用的工作負載結構描述，是 NVIDIA DSX AI Factory Platform 的一部分。每份定義只需說明：pod template 在哪裡、replica 數怎麼算、status 欄位怎麼讀。KAI Scheduler 用這些定義來解讀 pod 分組與 gang scheduling 指令，NVIDIA Run:ai 則用它做工作負載管理與可視化，兩者作用在同一份描述上，不必各自維護框架專屬的解析程式碼。

以 JobSet 為例，定義分成兩層。root component 定義這個工作負載本身的 kind，以及如何讀取 status：JobSet 原生並沒有單純的「Running」狀態，定義用 jq 表達式對 `replicatedJobsStatus` 做判斷（任一角色 ready 且 active、且沒有 failed 才算 running），並把原生的 Completed、Failed 條件對應到共用的詞彙上——這一層 statusMappings 等於是翻譯層，換成 RayJob 或 LeaderWorkerSet，只要同樣對應到這套共用詞彙即可。

childComponents 則描述內部結構：JobSet 把角色列表放在 `.spec.replicatedJobs`，定義用 `podTemplateSpecPath` 指到每個 Job 的 pod template，用 `scaleDefinition` 以 jq 計算「replicas 乘以 parallelism」得出 pod 數量（這也是範例 manifest 要明確設定 parallelism 的原因），再用 `instanceIdPath` 取出每個角色的名稱，讓 leader 與 worker 被辨識成不同角色，而不是三個無名的 Job。

💡 **目錄已經覆蓋主流分散式框架**

Workload Map 內建了 JobSet、PyTorchJob、RayCluster、RayJob、RayService、KServe、Knative、MPIJob、NVIDIA NIM、LeaderWorkerSet、Milvus、Grove PodCliqueSet、NVIDIA Dynamo 等框架的預先測試定義；若有新框架，只需要撰寫一份 YAML 定義描述其結構與狀態，而不是重新寫一套編譯進去的 adapter。這個設計把「框架知識」變成開發者可以撰寫、審查、像一般 manifest 一樣套用到叢集上的資料，而不是鎖在程式碼裡的邏輯。

🎯 **對平臺工程團隊的意義**

如果你正在為多租戶 AI 平臺維護排程器、controller 或儀表板，而且不斷被新的訓練/推論框架追著加 adapter，Workload Map 提供的思路值得參考：用一份宣告式定義取代一次性程式碼,新框架的支援成本就能從「等版本」降低到「寫一份 YAML」。

🔗 **來源**
- 標題：Support New AI Frameworks Faster Using NVIDIA Workload Map
- 作者／機構：Alon Lavian, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/support-new-ai-frameworks-faster-using-nvidia-workload-map/

#Kubernetes #NVIDIA #AIInfrastructure #DistributedTraining #MLOps #GPUScheduling #JobSet #CloudNative #PlatformEngineering #AIFactory
