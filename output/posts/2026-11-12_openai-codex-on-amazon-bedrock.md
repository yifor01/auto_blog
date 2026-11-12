---
title: OpenAI Codex on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-11-12T23:04:19.020467'
score: 87
---

📌 Codex 接上 Amazon Bedrock：企業導入的關鍵不是模型，是治理

TL;DR：Codex 可透過 Amazon Bedrock 呼叫 OpenAI 模型，真正的難題是怎麼套進既有的身分、權限與監控體系。

當開發者在自己的工作站上裝 Codex 探索陌生程式碼、處理重複性工程工作時，平臺團隊的壓力點往往不是「模型夠不夠聰明」，而是「要不要為此多養一套身分驗證、模型存取和維運系統」。AWS ML 這篇由 Shivi Bhatia 撰寫的文章給出的答案很直接：不用重建一套，把 Codex 的模型請求路徑接進你組織現有的 AWS 身分、IAM、區域與監控流程就好。

🤔 **問題不在模型，在請求怎麼走**

Codex 本身仍然跑在開發者的工作站上，文章強調的設計重點是「模型請求如何送到 Amazon Bedrock、組織在哪裡套上政策與維運控管」。範例使用 GPT-5.6 Sol，作者提醒導入前要先查「Amazon Bedrock 支援模型地區對照表」，確認 Sol、Terra 或 Luna 在你要用的 AWS 區域與推論路徑上是否可用。

🧩 **三條存取路徑，各自對應不同治理需求**

文章列出三種接入方式，並建議依「現在就需要的控管程度」來選,而不是一開始就上最複雜的方案:

- **Native AWS Access**(建議的預設起點):用於小規模、最小權限的試點。身分驗證沿用現有的 identity provider(文章範例用 Okta 透過 SAML 做驗證、SCIM 佈建使用者到 IAM Identity Center),Codex 本身不直接設定 identity provider,而是由 IAM Identity Center 發出臨時 AWS 憑證。
- **AgentCore Gateway**:當你需要 AWS 代管的閘道基礎設施來做集中路由,或是要套用 Amazon Bedrock Guardrails 時選用。
- **LLM Gateway**:如果平臺團隊想在請求路徑上強制套用控管規則,且組織已經在跑一套 LLM Gateway,就直接沿用。
- **客製整合**:是 LLM Gateway 模式中最進階、最複雜的形式,文章特別強調這不是「快速上手版」,而是平臺工程與安全團隊要從頭自己設計、維運的獨立服務,只有在前三者都無法滿足特定需求時才考慮。

這些範例都來自開源的 Guidance for Codex on AWS 專案,裡面提供 Native AWS Access、AgentCore Gateway、LiteLLM on ECS、Portkey、ADOT(AWS Distro for OpenTelemetry)以及 CloudWatch 設定的快速上手範本,可以依架構選用再調整。

📊 **試點怎麼跑:三個檢查點,兩個使用者**

Native AWS Access 的試點流程分三步:先用 IAM Identity Center 的 AWS CLI profile 直接呼叫 Amazon Bedrock Runtime,確認 AWS 存取沒問題;接著把 Codex 指向核准的模型(設定 model、profile、region,且建議放在使用者層級或受管設定,避免被單一儲存庫改動);最後跑一個安全的 Codex 任務驗證整條設定。

文章特別提到,單一使用者只能證明「登入可以用」,要測試「歸因是否清楚區分」,至少需要兩位試點使用者分別登入、執行同樣的無害任務,確認各自的 assumed-role session、稽核紀錄,以及(若有設定)telemetry 紀錄是彼此獨立的,才能放心擴大試點範圍。

至於觀測資料,文章區分了四種不同性質的紀錄:Codex OpenTelemetry 描述的是「用戶端活動」,Amazon Bedrock 的服務指標與模型呼叫日誌(若啟用)顯示的是「服務端活動」,AWS 身分紀錄與 Cost and Usage Report(CUR)則提供身分與計費證據。文章提醒不要把 token 用量直接當作成本報表來用,也要求開發者在合併程式碼前自行審查與測試 Codex 產生的變更,因為 telemetry 本身不能證明程式碼的正確性或安全性。

🎯 **實務啟示**

對平臺團隊來說,這篇文章的價值在於給出一個「由簡到繁」的決策順序:先用 Native AWS Access 跑最小權限試點,驗證身分歸因與核准模型路徑都沒問題,再視需求升級到 AgentCore Gateway 或既有的 LLM Gateway。能滿足需求的最簡單路徑,通常維運負擔也最低,這比一開始就打造客製閘道更務實。

🔗 **來源**
- 標題:OpenAI Codex on Amazon Bedrock
- 作者／機構:Shivi Bhatia(AWS)
- 連結:https://aws.amazon.com/blogs/machine-learning/openai-codex-on-amazon-bedrock/

#AWS #AmazonBedrock #OpenAICodex #IAM #EnterpriseAI #AIGovernance #Observability #CloudSecurity #DevTools #PlatformEngineering
