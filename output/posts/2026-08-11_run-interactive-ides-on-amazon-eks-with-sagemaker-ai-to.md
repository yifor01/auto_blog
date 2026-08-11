---
title: Run interactive IDEs on Amazon EKS with SageMaker AI to power up your AI workflows
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/run-interactive-ides-on-amazon-eks-with-sagemaker-ai-to-power-up-your-ai-workflows/
model: tencent/hy3:free
generated_at: '2026-08-11T07:19:58.466103'
score: 75
---

📌 【AWS】在 EKS 上運行 SageMaker Spaces 互動 IDE  

TL;DR：透過 SageMaker AI Spaces 插件，可在 EKS 快速啟動 JupyterLab 與 Code Editor，提升 GPU 使用率並降低成本。  

🎣 開場鉤子  
當資料科學家想在同一個 EKS 叢集裡使用 JupyterLab 或 Code Editor 時，常必須離開管線所在的叢集，改用獨立的 JupyterHub 或筆記型電腦。這樣的切換會讓他們失去 GPU 節點、共享儲存體以及 IAM 角色，使得原本的工作流程中斷。  

🤔 背景或問題  
資料科學隊伍需要互動式開發環境來探索資料、測試模型與調試程式。然而，在 Amazon EKS 上自行架設 JupyterHub 通常需要平臺團隊花費 3–5 天，且必須額外處理 GPU 存取、持續儲存以及身份驗證。這不僅增加運維負擔，也導致 GPU 資源在等待作業時閒置，進而提升整體成本。  

🧩 方法或架構  
Amazon SageMaker AI Spaces 為 EKS 提供的附加元件，直接在現有叢集上執行受管理的 JupyterLab 與 Code Editor 環境。其核心做法包括：  

1. **前置作業**  
   - 建立符合 Spaces 需求的 EKS 叢集：關閉 EKS Auto Mode，使用 Kubernetes 1.30 或更新版本；VPC 必須具備公有與私有子網（至少兩個可用區域），私有子網經 NAT 網路連線，叢集端點設為 Public 與 Private。  
   - 在建立叢集時先加入 EKS Pod Identity Agent、Amazon EBS CSI Driver、Cert‑manager 與 External DNS 附加元件，但暫不安裝 SageMaker Spaces 與 AWS Load Balancer Controller。  
   - 建立受管理節點組：採用 Amazon Linux 2023、m5.xlarge 或更大型實例，放在私有子網內，節點數為 2。  
   - 為所有子網加上標籤，以便 AWS Load Balancer Controller 後續發現它們；否則 ALB 可能被放置在私有子網，導致 Spaces 無法從外部存取。  

2. **網路與安全設定**  
   - 透過 Helm 安裝 AWS Load Balancer Controller。  
   - 使用 ACM 為自訂域名申請 TLS 憑證，透過 Route 53 的 CNAME 進行 DNS 驗證，等待憑證狀態變為 Issued 後保存其 ARN。  
   - 建立 KMS 金鑰，用於 JWT 加密。  
   - 設定 SSM 服務參數，以支援後續的 SSH‑over‑SSM 遠端連線。  

3. **IAM 與存取控制**  
   - 為 Spaces 控制平面與認證中介軟體各建立 IAM 角色（為了職責分離，建議拆分：一個負責 SSM 動作，另一個負責 KMS 加密/解密）。  
   - 每個角色透過 EKS Pod Identity 由對應的 Kubernetes 服務帳號假定，共用同一個信任原則。  
   - 安裝 SageMaker Spaces 附加元件（版本必須為 0.1.4 或更新）。安裝成功後，附加元件應顯示 ACTIVE 且問題清單為空；控制平面、兩個認證中介軟體副本以及兩個 Traefik 路由器應該都處於 Running 狀態。  

4. **建立與使用 Space**  
   - 建立 EKS 存取條目，限制於單一命名空間，以避免使用者越權存取其他資源。  
   - 透過該存取條目建立第一個 JupyterLab Space。首次啟動大約需要五分鐘，系統會拉取 4 GB 大小的 SageMaker Distribution 映像檔，並將 Pod 註冊至 SSM。  
   - Spaces 控制平面會發行一個帶有 5 分鐘有效期的預簽 URL（URL 中攜帶 KMS 加密的 JWT），使用者可直接在瀏覽器開啟此 URL 進行 JupyterLab 操作。  
   - 若希望獲得更穩定的本機 IDE 體驗，可使用 VS Code 透過 SSM 隧道連線至 Space Pod，此方式不需要瀏覽器、域名或 ALB。  

5. **團隊登入方式的升級**  
   - 預設依賴 IAM 使用者與角色。若想讓團隊以企業身份（例如 Amazon Cognito）登入，則需要在叢集上註冊 OIDC 提供者，並將 Kubernetes RBAC 與身份提供者群組綁定。  
   - 本文引用的開源 `jupyter-deploy` 專案提供 `aws-eks-oidc` 範本，內含 Dex 作為 OIDC 提供者，Amazon EKS 信任 Dex，並附帶網頁 console 供團隊自助管理工作空間。該範本會自行佈建 VPC 與叢集，可與既有的 EKS 叢集並行運行。  
   - Dex 的 GitHub 連接器直接使用；Amazon Cognito 則透過 Dex 的通用 oidc 連接器，並需要兩個聲明映射：將 `preferred_username` 聲明映射自 `email`（因為 Cognito 不會直接發出 `preferred_username`）。  

📊 數據或結果  
- 使用 SageMaker Spaces 後，啟動一個完整配置的 Space 大約只需 **5 分鐘**，相較於傳統的獨立 JupyterHub 部署（需平臺團隊 3–5 天）大幅縮減準備時間。  
- 將互動式開發與訓練工作負載整合在同一個 EKS 叢集上，可讓 GPU 節點在作業間保持忙碌，相較於專用筆記型電腦陣列，**GPU 使用率最高可提升 30%**。  
- 避免維持長時間運行的 GPU 環境，可減少每月可能達到 **數千美元** 的固定成本。  
- 進階 SSM 執行個體層會為每個 Space Pod 額外產生約 **$0.00695/hr** 的費用。  

💡 深入分析  
該方案的核心價值在於「不離開叢集」：資料科學家仍能使用熟悉的 JupyterLab 或 Code Editor，同時繼承叢集原本的 GPU 節點、EBS 共享儲存體以及 IAM 權限。這意味著既有的機器學習管線（例如訓練作業、模型註冊）不需要額外的資料搬移或權限重新設定，減少了因環境切換而導致的設定錯誤與調試時間。  

透過將 Space 的存取限制於單一命名空間的 EKS 存取條目，進一步強化了最小權限原則，避免使用者誤觸及其他團隊的資源。同時，採用預簽 URL 與 SSM 隧道的雙管齊下方式，既提供了快速瀏覽器存取的便利，也給予需要更深入終端操作的開發者一個安全的遠端連線路徑。  

在身份驗證方面，從純 IAM 過渡至 OIDC（特別是 Amazon Cognito）不僅符合企業單點登入的常見需求，也透過 Dex 的彈性擴充，允許未來整合其他身份提供者（如 GitHub、Azure AD）而不必改動 EKS 本身的設定。  

⚠️ 限制  
- 本文說明的步驟假設您已具備建立 EKS 叢集、管理 IAM 權限以及操 Helm 的經驗；若缺少相關前置知識，可能需要額外參考 EKS 入門指南。  
- 預簽 URL 的有效期固定為 5 分鐘，目前無法經由附加元件調整；若需要更長的瀏覽器存取時間，必須改用 VS Code 遠端連線方式。  
- 為確保 ALB 能正確定位至公有子網，必須在安裝 Spaces 附加元件之前完成子網標籤；否則會導致 Space 無法從外部存取。  
- 文中提到的費用（ALB、EBS、EKS 叢集以及 SSM 進階層）僅為示範環境可能產生的費用，實際成本仍會依使用流量與資源規模而異。  

🎯 實務啟示  
- 若貴團隊目前正在 EKS 上運行訓練管線，卻仍分散使用筆記型電腦或獨立 JupyterHub，可評估導入 SageMaker Spaces 附加元件，以將互動式開發工作負載拉回同一個叢集，提升資源利用率並簡化運維。  
- 在建立叢集時，請先確認子網標籤與 VPC 結構符合 Spaces 需求，這是後續安裝 Load Balancer Controller 與 ALB 的關鍵前置條件。  
- 對於需要符合企業身份管理的環境，可直接採用 `jupyter-deploy` 所提供的 `aws-eks-oidc` 範本，快速佈建 Dex 與 Amazon Cognito 的整合，讓團隊以現有的 SSO 認證登入 Space，而無須為每位使用者建立獨立的 IAM 帳號。  
- 最後，務必在測試完成後依照文章的 Cleanup 步驟釋放 ALB、EBS 卷以及任何測試用的 EKS 節點，以避免不必要的持續費用。  

🔗 來源  
- 標題：Run interactive IDEs on Amazon EKS with SageMaker AI to power up your AI workflows  
- 作者／機構：Rajat Jain  
- 連結：https://aws.amazon.com/blogs/machine-learning/run-interactive-ides-on-amazon-eks-with-sagemaker-ai-to-power-up-your-ai-workflows/  

#AWS #EKS #SageMaker #Spaces #JupyterLab #CodeEditor #OIDC #Cognito #GPUUtilization #AIWorkflow
