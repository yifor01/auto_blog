---
title: How Cohere Health digitizes clinical policies using Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-cohere-health-digitizes-clinical-policies-using-amazon-bedrock-agentcore/
model: tencent/hy3:free
generated_at: '2026-08-08T06:53:57.781924'
score: 77
---

📌 Cohere Health 使用 Amazon Bedrock AgentCore 建構多租戶代理系統自動化臨床政策數位化  

TL;DR：透過 Amazon Bedrock AgentCore 的多租戶代理架構，Cohere Health 使臨床政策數位化效率提升 30%，每項政策處理時間從 2 小時 15 分縮短至 1 小時 35 分。  

🎣 醫療保險的事先授權流程長期依賴人工審核，導致每年影響數億位患者的決策緩慢且易出錯。  

🧩 方法或架構  
Cohere Health 以 Amazon Bedrock AgentCore 為基礎，打造名為 Cohere Policy Studio 的多租戶代理系統。其核心包含以下要素：  
- **AgentCore Runtime 的安全 MicroVM 隔離**：為每個健康方案客戶提供獨立的運算、記憶體與檔案系統資源，確保租戶間的資料嚴格隔離。  
- **AgentCore Gateway 統一工具存取**：透過單一認證端點整合 AWS Lambda 函式與內部 API，團隊可新增工具而無需重新部署代理。  
- **AgentCore Memory**：儲存政策分析師的回饋，支援人機共同迴流（human‑in‑the‑loop）的政策優化流程。  
- **Agent Skills 開放標準**：將領域知識封裝為可版本化的技能，使臨床政策專家能直接編寫與更新技能，無需重建代理基礎設施。  

為支援多團隊客製化而不重建運行環境，Cohere Health 採用兩層部署架構：  
1. **共用基礎映像**（FROM）：包含 LangChain 代理框架與共用依賴。  
2. **團隊專屬設定檔**（COPY）：例如 `agent_config.yaml`，控制各團隊的代理行為。  

代理透過 AgentCore Gateway 呼叫工具時，Gateway 會呼叫對應的 AWS Lambda 函式，依工具名稱將請求路由至正確的處理器，例如從 Amazon S3 讀取技能定義。  

📊 數據或結果  
實施後，Cohere Health 報告政策數位化效率提升 **30%**，單項政策處理時間從 **2 小時 15 分** 減少至 **1 小時 35 分**。此外，該解決方案亦帶來政策數位化速度、部署速度與涵蓋範圍的可量測改善。  

💡 深入分析  
- 以 **Agent Skills** 為模組，將臨床政策專家的知識與基礎設施解耦，使新功能能以版本化技能形式直接上線，避免每次需求都重建代理。  
- 技能採用 **雙層版本控制**：第一層以語意版本（例如 `skill/policy_ingestion/v1.2.3`）追蹤能力變更並以 Git 標記；第二層利用 Amazon S3 物件版本保存每次上傳的不可變歷史，支援回滾與區分非生產／生產環境。  
- 評估流程結合機器學習工程與資料科學團隊：先以真實標籤資料集定義準確度、完整度與一致性的成功指標，再跑評估套件；失敗時分析失敗模式並迭代技能定義；通過後由資料科學驗證符合驗收標準，交由 Arize AI 追蹤生產環境效能，臨床政策分析師再標註樣本以捕捉自動化指標遺漏的錯誤。  

🎯 實務啟示  
- 想要在多租戶環境中快速部署 AI 代理，可參考 **共用基礎映像 + 團隊專屬設定** 的模式，降低重建開銷與配置漂移。  
- 透過 **統一工具 gateway**（如 AgentCore Gateway）將各種後端服務（Lambda、內部 API）包裝為單一端點，團隊新增工具時無需重新部署代理。  
- 將領域知識封裝為 **可版本化的技能**，並建立嚴格的評估與版本管控流程，有助於在保持臨床專家監督的同時，快速迭代與擴充 AI 功能。  

🔗 來源  
- 標題：How Cohere Health digitizes clinical policies using Amazon Bedrock AgentCore  
- 作者／機構：Oleksiy Kononenko @ AWS ML  
- 連結：https://aws.amazon.com/blogs/machine-learning/how-cohere-health-digitizes-clinical-policies-using-amazon-bedrock-agentcore/
