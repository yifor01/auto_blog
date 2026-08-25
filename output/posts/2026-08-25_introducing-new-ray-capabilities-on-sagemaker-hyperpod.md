---
title: Introducing new Ray capabilities on SageMaker HyperPod
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-new-ray-capabilities-on-sagemaker-hyperpod/
model: claude-code/sonnet
generated_at: '2026-08-25T06:31:54.983163'
score: 76
---

📌 SageMaker HyperPod 把 Ray 叢集管理搬進主控臺，不用再手寫 YAML

TL;DR：AWS 為 SageMaker HyperPod 新增 Ray 整合，讓分散式訓練與推論的叢集管理、觀測性、容錯都能在 Studio 主控臺完成。

過去要在 Kubernetes 上跑好一套 Ray 分散式訓練環境，資料科學家得自己寫 YAML manifest、為每次依賴變動重建 Docker 映像檔、設定 kubectl port-forward 才能看 Ray Dashboard，還要手動架設 Prometheus 與 Grafana。AWS 這篇部落格宣布，SageMaker HyperPod 現在把這整套流程收進了主控臺。

🤔 **背景：Ray 好用，但維運成本不低**

Ray 是一套開源框架，讓資料科學家能把分散式 Python 工作負載擴展到多臺 GPU 叢集，涵蓋從 Ray Train 的分散式訓練到 Ray Serve 的模型服務。在 Kubernetes 上，Ray 叢集由開源的 KubeRay operator 管理，透過 RayCluster、RayJob、RayService 等自訂資源控制生命週期。而 SageMaker HyperPod 本身則是針對大規模機器學習打造的基礎設施，建於 Amazon EKS 之上，內建節點健康監控與自動復原能力。這次更新就是把 Ray 與 HyperPod 這套既有基礎設施做深度整合。

🧩 **新能力：從建立叢集到觀測性全都在 Studio 完成**

文章列出幾項具體整合：

- **叢集建立與管理**：在 SageMaker Studio 中選擇 HyperPod 叢集，進入 Tasks 頁籤選擇 RayCluster 任務類型，即可在主控臺看到所有 Ray 叢集的狀態、機型與可用操作；建立時只需填入叢集名稱、head／worker 機型、worker 數量與容器映像檔（預設使用內建 Ray 且由 AWS 定期修補漏洞的 SageMaker Distribution 映像檔），也保留內嵌 YAML 編輯器供進階客製化使用。KubeRay operator 也整合了 HyperPod task governance，管理員可對 Ray 工作負載設定運算配額與排程優先權。
- **Dashboard 存取**：叢集建立時可啟用遠端端點，之後從 Actions 選單開啟 Ray Dashboard，系統會產生一個以 IAM 驗證、限定叢集建立者使用的短效 URL，不需要本地 kubectl port-forward。
- **遠端提交工作**：透過 `toolkit-for-ray-on-sagemaker-ai` 這個 Python 套件，可以從 Studio、筆電或 CI/CD pipeline 遠端提交工作到 Ray 叢集，套件會處理端點解析與透過 IAM 驗證產生的 EKS API 憑證，因此可直接沿用標準 Ray job submission API。
- **Notebook 整合**：HyperPod 的 JupyterLab 或 Code Editor 空間可以直接掛載到一個 Ray 叢集，該空間會以「零運算 worker 節點」的身分加入叢集，notebook 因此擁有原生的 Ray driver 存取權，呼叫 `ray.init(address="auto")` 即可連上叢集，並可用 `runtime_env` 參數在不重建容器映像檔的情況下即時注入 Python 依賴。
- **觀測性**：新推出的 HyperPod Observability EKS add-on 會自動探測 Ray head 與 worker pod、抓取指標端點，並在 Amazon Managed Grafana 中自動佈建 Ray Core、Ray Data、Ray Train、Ray Serve 四個預建 dashboard，不需要手動建立 PodMonitor／ServiceMonitor 或匯入 dashboard JSON 檔案，且這些 dashboard 會與既有的 GPU、EFA、task governance dashboard 並列在同一介面。

📊 **容錯與復原機制**

文章說明 SageMaker HyperPod 為 Ray 訓練工作負載提供三層韌性：硬體故障時的自動節點復原、訓練停滯時的 hung job 偵測，以及分層式 checkpoint 帶來的快速復原能力。節點被替換時，Ray 會將 worker pod 重新排程到新的健康節點上；只要訓練程式碼定期存 checkpoint 並具備從最新 checkpoint 續跑的邏輯，工作就能從中斷處接續執行，無需人工介入重啟。

此外，SageMaker JumpStart 現在也能將模型權重直接載入 Ray Serve 端點，並透過 KV cache offload 到分層式儲存空間，用於服務長 context 的請求。

💡 **與既有工作流的相容性**

文章強調這些能力是建立在開源 KubeRay 與標準 Ray API 之上，既有的腳本與工作流程可以不經修改直接運作，這意味著採用門檻主要落在基礎設施管理層面，而非重寫應用程式碼。

🎯 **實務啟示**

如果你的團隊已經在用 Ray 做分散式訓練或推論，但苦於維護一整套 Kubernetes 觀測性堆疊與手動 YAML 設定，這次整合把「建立叢集、開 Dashboard、掛載 Notebook、看 Grafana 指標」這些日常操作都收斂到 SageMaker Studio 介面裡，同時保留 kubectl／YAML 的進階路徑給需要客製化的場景，值得評估能否降低團隊在維運面的重複勞動。

🔗 **來源**
- 標題：Introducing new Ray capabilities on SageMaker HyperPod
- 作者／機構：Nilesh PS, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-new-ray-capabilities-on-sagemaker-hyperpod/

#AWS #SageMaker #HyperPod #Ray #DistributedTraining #Kubernetes #MLOps #KubeRay #ModelServing #CloudComputing
