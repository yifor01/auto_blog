---
title: How Tamnoon built AI-powered cloud security remediation with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-tamnoon-built-ai-powered-cloud-security-remediation-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-14T21:00:26.101940'
score: 86
---

📌 90 天降低 9 成雲端風險的 Agent 怎麼做到

TL;DR：Tamnoon 用 Bedrock 多模型 agent 架構打造自動雲端安全修復系統 Tami，90 天內讓關鍵雲端暴露降低逾九成，且零正式環境事故。

CNAPP 與雲端掃描工具產出的安全發現，多到沒有任何團隊能全部處理完——不是因為修復本身困難，而是調查上下文、找出負責人、確認修復不會弄壞正式環境，這些工作消耗的時間，遠超過團隊人力的成長速度。

🤔 **發現與修復之間，風險正在悄悄累積**

多數安全發現就這樣被放著，不是因為難修，而是缺乏投入調查與驗證的人力。Tamnoon 打造的 AI 助手 Tami，與人類雲端安全專家協作，在 AWS、Azure、Google Cloud 等多雲環境中調查、排序並安全地修復錯誤設定與問題。

🧩 **4 個專責 agent，一支 API 呼叫多個模型**

Tamnoon 把流程拆成四個階段，交給四個專責 agent 分別負責：蒐集並正規化來自 CNAPP／CSPM 的發現、補充資產與暴露情境並排序、深入調查根因，以及產生並執行修復。選擇 Amazon Bedrock 的關鍵考量在於：

- 透過單一 API，每個 agent 可以呼叫最適合自己任務的基礎模型——最強的模型處理最難的推理，更有效率的模型處理高量且重複的驗證工作，審查用的模型則在輸出品質與成本之間取得平衡；模型要替換或升級時，不需要重新串接整套架構。
- Bedrock 的 Cross-Region inference 會自動把推論請求路由到地理邊界內最佳的 Region，不需要自行建置流量分配邏輯。
- 推論在 Tamnoon 自己的 AWS 環境內執行，透過 IAM 權限範圍管控，客戶的敏感資料不會離開信任邊界。

Tamnoon 透過 API 整合 Wiz、CrowdStrike、Palo Alto Cortex、Upwind、SentinelOne、Orca、Cyera 等 CNAPP，以及 AWS Security Hub、Amazon GuardDuty 等雲原生工具的發現，統一正規化後交給 agent 層處理。基礎設施上，Amazon EKS 跑 dashboard 背後的常駐服務，AWS Lambda 處理事件驅動的蒐集、分析與修復工作，EventBridge、SQS、Step Functions 負責協調大量發現的平行處理，避免單一壞資料拖慢整體流程。AI 層跑在 Bedrock 上，搭配 Amazon Bedrock AgentCore 讓 agent 具備受治理的行動權限，而非開放式存取，Bedrock Guardrails 則在任何修復動作執行前，先審查請求本身與產生的程式碼。

📊 **90 天降 9 成風險，正式環境零事故**

針對每一筆被處理的發現，Tami 都會標上一個 Remediation Confidence Indicator（RCI）：SAFE、RISKY，或 AWAITING DATA，讓團隊清楚知道哪些可以自動化、哪些需要先經過人工審查。導入這套做法後，Tamnoon 在 90 天內讓客戶環境中的關鍵雲端暴露降低超過 90%，且過程中沒有發生任何正式環境事故。

⚠️ **修復前先過一關保守的安全評估**

Tamnoon 把自主性放進一個縱深防禦的安全架構裡，每一層都假設前一層可能會漏掉東西。在任何修復被草擬出來之前，必須先經過一個獨立、刻意偏向保守的安全評估，確認這個變更可以安全執行。調查步驟被嚴格限定為唯讀，理解問題的過程本身不會改動任何東西；只有修復路徑能真正變更環境，且每一次變更都搭配自己的備份、驗證與回滾步驟。

🎯 **先把讀和寫分開，再談自動化程度**

對想導入 agentic 修復的團隊而言，真正該問的不是「要不要讓 AI 動手修」，而是能不能先把調查（讀）與修復（寫）的權限嚴格分離，再用信心分級取代「全自動或全人工」的二元選擇。

🔗 **來源**
- 標題：How Tamnoon built AI-powered cloud security remediation with Amazon Bedrock
- 作者／機構：Ishara Premadasa，AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/how-tamnoon-built-ai-powered-cloud-security-remediation-with-amazon-bedrock/

#CloudSecurity #AmazonBedrock #AIAgents #CNAPP #SecurityAutomation #AWS #Tamnoon #Remediation #GenAI #DevSecOps
