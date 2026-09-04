---
title: Run agent-driven Amazon SageMaker HyperPod operations with InstantStart
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/run-agent-driven-amazon-sagemaker-hyperpod-operations-with-instantstart/
model: claude-code/sonnet
generated_at: '2026-09-04T19:52:39.410483'
score: 83
---

📌 開源控制平面InstantStart，讓AI代理直接管理HyperPod叢集

TL;DR：AWS開源專案InstantStart把SageMaker HyperPod的多階段維運流程封裝成可對話操作的控制平面，網頁與AI代理共用同一套後端API。

在Amazon SageMaker HyperPod上跑基礎模型（FM）工作負載，從來不是單一任務，而是一連串環環相扣的依賴鏈：建立網路與控制平面、掛載加速運算資源、依序安裝叢集依賴、準備儲存與身分驗證、讓分散式任務撐過硬體故障、部署模型伺服器並持續監看——大部分維運的痛點，其實都藏在這些步驟之間的交接處。HyperPod InstantStart正是針對這個「組合問題」而生的開源控制平面。

🤔 **HyperPod解決了什麼，EKS又把什麼責任留給你**

SageMaker HyperPod提供受管理、具韌性的運算資源，並與Amazon EKS整合健康監控、節點自動擴縮、訓練復原與推論等能力；但EKS仍是使用者自行管理的編排介面，這代表團隊擁有直接的Kubernetes存取權，同時也要負責把AWS資源、附加元件、工作負載與日常維運組合成一個連貫的整體。InstantStart就是為了解決這個組合層問題而生的開源控制平面。

🧩 **同一套後端，兩種操作介面**

InstantStart提供兩種驅動同一控制平面的方式：在網頁介面上，建立一個裝好依賴、開啟自動節點復原、掛載好儲存空間的叢集，是一張表單、一個進度面板加上重新整理按鈕；在終端機上，同樣的事只需要一句話——AI代理會規劃多階段工作流程、依序啟動各階段，並輪詢非同步的AWS操作直到完成，只在真正需要人類決策的地方暫停（例如可用區域、執行個體類型、容量類型），最後交出一個已掛載好儲存空間、可直接使用的叢集。兩種介面呼叫的是同一組後端API、通過同一套驗證邏輯，並讀取同一份持久化的操作狀態，彼此沒有任何一方獨有的邏輯。

InstantStart以單一個「頻外（out-of-band）」管理容器的形式運作在你的AWS帳戶中，呼叫AWS服務API與Kubernetes API，不會介入訓練任務或推論請求的資料路徑；它建立的每一項資源都是標準的AWS或Kubernetes資源，可用AWS CLI或kubectl直接檢視。架構上，網頁UI、REST API，以及AI代理所使用的MCP工具，其實是同一個容器的三張臉，背後共享分階段佈建與冪等（idempotent）調節邏輯。

📐 **兩側API：Kubernetes管的部分 vs. AWS管的部分**

系統背後銜接兩個API層面：Kubernetes這一側是使用者自行管理的Amazon EKS，掌管Kubernetes API、以EKS附加元件形式安裝的HyperPod訓練與推論算子（operator），以及它們調節出的HyperPodPyTorchJob與InferenceEndpointConfig資源；AWS這一側是AWS受管理的SageMaker HyperPod，能力分為四組：基礎設施（健康監控、深度健康檢查、自動節點復原）、容量（持續佈建、受管理的Karpenter自動擴縮）、訓練（行程層級復原、受管理的分層檢查點）、推論（智慧路由、分層KV快取）。這兩側在HyperPod執行個體群組（instance group）交會：Kubernetes把pod排程上去，HyperPod負責管理它們——這是判斷「哪一半由AWS自動運維、哪一半需要你介入」時最關鍵的分界線。周邊還銜接了儲存與可觀測性整合，包括承載映像檔、資料與檢查點的Amazon S3、FSx for Lustre、Amazon ECR；接收健康與使用率資訊的Amazon Managed Prometheus與Grafana；以及接收指標與產出物的Managed MLflow on SageMaker AI。

一項關鍵設計原則貫穿兩種介面：MCP工具包裝的是後端自己的REST API——也就是瀏覽器實際呼叫的那條程式碼路徑，而不是AWS CLI或SDK。這代表任何一次新增的驗證邏輯，會同時保護網頁與AI代理兩種操作方式。

📊 **分階段佈建：讓失敗不會拖垮已成功的步驟**

從空帳戶到可用的HyperPod容量，需要經過多個耗時且彼此依賴順序的長流程。InstantStart刻意把它們拆成EKS控制平面建立、啟用中叢集選取、依賴關係調節、HyperPod叢集建立、儲存設定五個階段——拆分的意義在於，後面階段失敗不會回滾已經成功的前面階段。EKS控制平面建立約需8到12分鐘，之後每個階段都各自記錄狀態，並可獨立重試。網頁介面上這對應到Cluster Management頁面：輸入叢集標籤、按下建立、觀看分階段進度指示；透過代理，整條流程則變成一場對話——文中提供了一段使用hypd-inst-agent（載入本專案MCP伺服器與skills、供Kiro CLI使用的代理設定）的實際精簡對話紀錄，其中三項行為來自專案agent skill中編碼好的工作流程規則，而非代理臨場發揮。

網路層面，CloudFormation路徑可以建立或重用VPC，並把EKS控制平面子網路與HyperPod運算子網路分開，因為兩者所需的位址空間量級差距懸殊；運算子網路以/20大小配置，以容納大規模加速器叢集。所有容量佈建路徑都會經過同一個函式ensureComputeSubnet()，並依固定優先順序執行：使用明確指定的子網路，或重用相容的每可用區子網路，或直接建立一個完整子網路（含路由表與S3 gateway endpoint關聯）——叢集建立與後續容量擴充共用這套邏輯，代表整個系統中只有一處會決定網路布局是對是錯。

⚙️ **叢集建好之後：自動節點復原成為日常**

控制平面建好之後，容量管理就成了日常反覆進行的操作：為新工作負載新增執行個體群組、選擇付費方式，並信任控制平面持續維持其健康狀態。InstantStart建立的叢集預設開啟自動節點復原，HyperPod可依據其健康監控代理、基本健康檢查，以及（在有設定的情況下）深度健康檢查的結果，重啟或替換故障節點；深度健康檢查會在節點正式接收工作之前，先對GPU與Elastic Fabric Adapter（EFA）連線進行壓力測試。

⚠️ **部署前要注意的兩個容量前置作業**

文中特別提醒，建議採用最低權限的IAM角色進行部署與日常維運，遵循AWS的CloudFormation存取控制與SageMaker HyperPod IAM指引，並將S3存取權限限制在專案指定的儲存桶內。另外有兩項容量相關作業需要AWS審核時間，建議提早申請：針對打算使用的每種執行個體類型申請SageMaker Cluster Usage服務配額提升，以及針對高階加速器類型購買SageMaker Flexible Training Plan以預留容量；同時也要留意VPC配額，因為預設情況下，分階段佈建流程會為每個叢集建立一個獨立VPC。

🎯 **實務啟示**

對正在維運HyperPod叢集的基礎設施團隊而言，InstantStart示範了一種讓AI代理安全操作生產基礎設施的做法：不是把原始CLI丟給代理自由發揮，而是把維運規則封裝進控制平面的API與驗證邏輯裡，讓網頁與代理共用同一套「護欄」。這個思路值得在自家的agent-driven infra專案中借鏡：與其信任代理的臨場判斷，不如把可重試、可稽核的操作規則寫進後端本身。

🔗 **來源**
- 標題：Run agent-driven Amazon SageMaker HyperPod operations with InstantStart
- 作者／機構：Hao Zheng, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/run-agent-driven-amazon-sagemaker-hyperpod-operations-with-instantstart/

#AWS #SageMakerHyperPod #MLOps #AIAgents #Kubernetes #EKS #MCP #InfrastructureAsCode #GPUCompute #CloudNative
