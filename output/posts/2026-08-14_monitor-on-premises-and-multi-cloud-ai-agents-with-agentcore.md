---
title: Monitor on-premises and multi-cloud AI agents with AgentCore Observability
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/monitor-on-premises-and-multi-cloud-ai-agents-with-agentcore-observability/
model: claude-code/sonnet
generated_at: '2026-08-14T07:32:27.862973'
score: 86
---

📌 地端、GCP、Azure 都能監控：AgentCore Observability 跨雲實戰

TL;debug；AI Agent 部署在 AWS 外，也能接上原生等級的可觀測性儀表板。

你的 AI Agent 用 Strands、LangGraph 或 CrewAI 寫好了，跑在地端伺服器或另一家雲端上，一旦推理鏈出錯、工具呼叫失敗，你能看到的往往只有零散的應用程式日誌。Amazon Bedrock AgentCore Observability 原生提供完整的追蹤與分析，但只支援跑在 AgentCore runtime 上的 Agent；跑在別處，就得自己接管線。AWS 這篇文章示範了怎麼把管線接起來。

🤔 **問題：可觀測性只顧得到 AWS 內部**

Amazon Bedrock AgentCore 是一個可跨框架、跨模型建構與最佳化 Agent 的平臺，其 Observability 功能能追蹤推理鏈、工具呼叫與模型輸出，這對偵測幻覺、監控有害或離題回應、追蹤 token 用量、稽核 Agent 行為都很關鍵。但這套機制預設只認得部署在 AgentCore runtime 上的流量，跑在地端或 GCP、Azure 的 Agent 若缺乏集中監控，異常輸出很容易被忽略。

🧩 **解法：讓 ADOT 幫忙把遙測資料送回 CloudWatch**

核心做法是在 Agent 應用程式內執行 AWS Distro for OpenTelemetry（ADOT）進行 auto-instrumentation，自動擷取符合 generative AI semantic convention 的 span，再透過 SigV4 簽章、用 IAM 憑證將遙測資料直接送到 Amazon CloudWatch 的 OTLP endpoint。整條管線由三塊拼起來：Amazon CloudWatch 負責遙測資料的接收與儲存，Amazon Bedrock AgentCore Observability 在上面疊加專屬的 Agent 監控儀表板，IAM 則負責驗證外部環境與 AWS 之間的身份。實務操作上，安裝 aws-opentelemetry-distro（內建 ADOT auto-instrumentation 與處理 SigV4 驗證的 aws_configurator）與 strands-agents[otel]，設定好對應的環境變數與 IAM 憑證，接著用 `opentelemetry-instrument` 指令包住你的 Python 程式進程即可，過程中會自動偵測 Bedrock 呼叫與 Strands 框架的操作。

📊 **實測：跨到 Google Cloud Shell 一樣能看到 trace**

文章實際驗證了兩種情境：一個是命名為 my-external-agent 的 Strands Agent 跑在非 AWS 環境，另一個是命名 gcp-hosted-agent、直接跑在 Google Cloud Shell（GCP 基礎設施上的瀏覽器終端機）。兩者執行後，都在兩到三分鐘內於 AgentCore Observability 儀表板上出現，trace 詳情包含四個 span、模型資訊、延遲與 token 用量，資料形式與跑在 AgentCore runtime 上的 Agent 完全相同。

💡 **這套模式不限 Strands**

文中特別提到，雖然示範用的是 Strands Agents，但同樣的 ADOT-based 模式適用於任何相容 OpenTelemetry 的 Agent 框架，代表這不是一次性技巧，而是可以套用到既有多框架 Agent 部署的通用方案。

⚠️ **權衡與安全提醒**

跑在 AgentCore runtime 上的 Agent 有自動的可觀測性設定，跑在非 AWS 環境則需要額外手動配置，換取更大的部署彈性。文章也提醒，正式環境應避免使用長效的 IAM access key，改用 IAM Roles Anywhere，讓地端工作負載能透過 X.509 憑證取得臨時憑證。此外，此方案會用到 Amazon Bedrock、CloudWatch 與 AWS X-Ray，這些服務本身會產生費用。

🎯 **實務啟示**

如果你的 Agent 部署策略本來就橫跨地端與多雲，不必為了拿到集中式可觀測性而被迫遷移到 AgentCore runtime；用 ADOT 把既有部署接上同一套儀表板，就能讓推理鏈、token 成本、異常輸出的監控統一在一處，而不用為每個環境各自搭一套監控系統。

🔗 **來源**
- 標題：Monitor on-premises and multi-cloud AI agents with AgentCore Observability
- 作者／機構：Vipul Rajendra Gargav, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/monitor-on-premises-and-multi-cloud-ai-agents-with-agentcore-observability/

#AWS #AmazonBedrock #AgentCore #Observability #OpenTelemetry #AIAgents #MultiCloud #CloudWatch #StrandsAgents #MLOps
