---
title: Introducing managed cluster extensions for observability and user management
  in Amazon SageMaker HyperPod Slurm
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-managed-cluster-extensions-for-observability-and-user-management-in-amazon-sagemaker-hyperpod-slurm/
model: claude-code/sonnet
generated_at: '2026-11-21T22:24:07.156359'
score: 68
---

📌 【AWS 新功能】HyperPod Slurm 叢集擴充功能，用 API 管好節點上的軟體

TL;DR：Amazon SageMaker HyperPod 新增 cluster extensions，把節點軟體設定變成可宣告、可驗證的 API 管理對象。

共享的 Slurm 叢集最容易出問題的地方，往往不是硬體，而是一堆分散維護的設定檔案：叢集形狀、節點軟體、網路拓撲、使用者名單,各自散落在不同地方，久而久之悄悄跑偏,而且沒有任何機制會告訴你哪裡對不上了。

🤔 **六層設定，前五層已經宣告式化**

AWS 把 Slurm 叢集的設定拆成六層：叢集定義、節點設定、容量、網路拓撲、硬體健康，以及節點上執行的軟體。2026 年期間，HyperPod 已經替前五層導入了 API 驅動的宣告式管理：API-driven Slurm configuration 讓管理者在 CreateCluster、UpdateCluster 請求中定義節點角色、partition 與 Amazon FSx for Lustre／OpenZFS 掛載點，並串接外部 accounting 資料庫；AMI-based configuration 用預先裝好 Slurm、Docker、Enroot、Pyxis 與家目錄的映像檔取代繁瑣的初始化腳本；continuous provisioning 在背景持續重試容量請求；automatic topology management 在節點擴縮或更換時自動維護網路拓樸（Slurm 25.11 以上支援 partition 層級的 tree 或 block 拓樸）；deep health checks 則對 GPU 與 NVIDIA NCCL 連線做壓力測試，檢測中的節點會留在 Slurm maintenance reservation，避免被排入工作。

🧩 **第六層不一樣：軟體會一直改變**

節點上執行的軟體這一層跟前五層本質不同，因為它在叢集生命週期中會持續變動——研究人員加入或離開、某團隊臨時需要更細的 GPU 指標、監控 exporter 推出新修補。過去這層只能靠 lifecycle scripts 維護，缺點很明顯：腳本只在節點 provision 時執行一次，之後每次改動都要編輯腳本再重跑或替換整個節點；出錯只有在腳本真正跑過才會曝光；也沒有任何東西回報節點目前裝了什麼，導致節點之間逐漸跑偏。

2026 年 11 月，AWS 推出 cluster extensions，把節點軟體變成由 AWS 管理的套件，可透過 API 或 Amazon SageMaker AI 主控臺安裝、設定、更新與移除，首批提供兩種：可觀測性（observability）與使用者管理（user management，含目錄整合）。運作方式是 HyperPod 記錄所需的設定狀態，node agent 在每個節點（包含新建與替換的節點）套用對應的擴展，再由健康探測器回報狀態與健康狀況。重要的是，團隊仍保留對每個節點（包括控制節點）的完整 SSH 存取權，以及執行自訂 lifecycle script 的能力,API 讓你少維護東西,直接存取讓你保留控制權,兩者可以自行取捨比例。

📊 **驗證、分角色套用與健康回報**

AWS 提供六個 cluster extension API，涵蓋安裝、更新、查詢與列出可升級版本等操作，可以用 AWS CLI 或 SDK 來腳本化安裝流程、做版本控管，或在多個叢集間重複套用同一組設定。主控臺上，叢集詳情頁的 Extensions 分頁會列出每個擴充功能的狀態、版本與 ARN,可觀測性擴充多了指標儲存與開啟 Grafana 儀表板的按鈕,使用者管理擴充則顯示使用者與群組數量及管理使用者的按鈕。建立或更新擴充功能時，HyperPod 會在 API 呼叫當下依該版本的 schema 驗證設定，拼錯的設定會立即被拒絕；套用時每個節點只會安裝其角色實際需要的部分，例如 GPU exporter 只會裝在 GPU 節點上；新建或替換的節點在啟動後幾分鐘內就會收到相同的狀態；更新只會送出要改動的設定，由 HyperPod 合併進既有的設定。若某個節點出現特定問題（例如 port 或使用者 ID 被佔用），會依原因分類顯示在 DescribeClusterExtension 的 Health 欄位中，附帶代碼、訊息與受影響節點數量；內部錯誤 HyperPod 會自動重試，其他問題則需要先排除原因，再呼叫一次不帶變更內容的 UpdateClusterExtension 來重試受影響節點。擴充功能狀態分為 Creating／Updating（套用中）、Active（所有節點皆套用成功且無異常）與 Degraded（部分節點失敗或回報問題）。

💡 **權責可以依擴充功能拆分**

每個擴充功能都有自己的 ARN，意味著像 sagemaker-user-management 與 sagemaker-observability 這類擴充可以分別由不同團隊擁有，例如平臺團隊負責使用者管理、監控團隊負責可觀測性。這等於把過去混在一堆 shell script 裡、權責不清的維運工作，拆成了邊界清楚、可各自授權與稽核的宣告式資源。

⚠️ **目前的範圍**

目前 managed cluster extensions 只提供可觀測性與使用者管理兩種,屬於組織特有的軟體或初始化需求,仍需透過自訂 AMI 或 lifecycle script 處理,並未被這套機制取代。

🎯 **對 ML infra 團隊的意義**

如果你的團隊維護的是多人共用的 HyperPod Slurm 叢集，這次更新值得關注的重點是：節點軟體設定終於有了跟容量、拓樸一樣的宣告式管理與健康回報機制，可以在下一輪叢集維運排程中評估導入，降低配置長期漂移、難以追蹤的風險。

🔗 **來源**
- 標題：Introducing managed cluster extensions for observability and user management in Amazon SageMaker HyperPod Slurm
- 作者／機構：Austin Cherian, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-managed-cluster-extensions-for-observability-and-user-management-in-amazon-sagemaker-hyperpod-slurm/

#AWS #SageMaker #HyperPod #Slurm #MLOps #MLInfrastructure #Observability #ClusterManagement #GPUComputing #CloudComputing
