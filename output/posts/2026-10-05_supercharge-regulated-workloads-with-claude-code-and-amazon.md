---
title: Supercharge regulated workloads with Claude Code and Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/supercharge-regulated-workloads-with-claude-code-and-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-05T23:29:06.155699'
score: 71
---

📌 【Anthropic Claude 進駐 GovCloud】受 ITAR 列管的開發團隊，也能用 AI 寫程式了

TL;DR：Claude Opus 5.5、Claude Sonnet 5.5 登陸 AWS GovCloud，讓受法規管制的團隊能用 Claude Code 做 AI 輔助開發。

對受出口管制、國防合約等高度監管產業的工程團隊來說，「用上最新的 AI coding 工具」長期是奢侈品，不是技術跟不上，而是合規要求不允許。AWS 這次把 Claude Opus 5.5 與 Claude Sonnet 5.5 帶進 GovCloud (US)，試圖打開這道門。

🤔 為什麼法規場域一直進不了 AI coding 的門

AWS GovCloud (US) Regions 是專為美國客戶的高度合規需求設計的環境，涵蓋 ITAR 等出口管制規範。Claude Sonnet 5 已取得 FedRAMP Class D（原 High）認證，以及 DoD Impact Level 4/5（IL4/IL5）授權；Claude Opus 5.5 與 Claude Sonnet 5.5 在 Amazon Bedrock 上同樣取得 FedRAMP Class D 認證（文中提醒需自行查核模型最新認證狀態）。Amazon Bedrock 的客戶內容不會被儲存、記錄或用來訓練 AWS 模型，也不會分享給第三方，這些是此方案能進入監管場域的基礎。

🧩 兩種端點、同一顆推論引擎

AWS GovCloud (US) 上的 Amazon Bedrock 提供兩種端點，皆由同一套具 Zero Operator Access（ZOA）架構的 Mantle 推論引擎驅動：

- bedrock-runtime：走 AWS SDK（InvokeModel、Converse API），支援 Amazon Bedrock Guardrails、Knowledge Bases、Agents 與呼叫紀錄，是大多數新應用、尤其需要稽核軌跡場景的建議選擇。
- bedrock-mantle：原生支援 Anthropic Messages API，可使用目前僅該介面提供的能力，例如伺服器端工具、背景推論與 Projects。

兩種端點皆支援 Claude Opus 5.5、Claude Sonnet 5.5 與 Claude Sonnet 5，其中 bedrock-runtime 同時在 US-West 與 US-East 兩個 GovCloud 區域可用，bedrock-mantle 目前僅限 US-West。

Claude Code 是 Anthropic 的 agentic coding 工具，能讀取整個程式碼庫、編輯檔案、執行指令，並整合既有開發工具，可在終端機、VS Code／JetBrains 等 IDE 中使用，也能透過 Claude Agent SDK 在背景執行。設定流程大致是：先用 AWS CLI 設好憑證並安裝 Claude Code，登入時選擇「3rd-party platform」→「Amazon Bedrock」，依精靈選擇驗證方式、區域（us-gov-west-1）並釘選模型版本；若之前已設定過，可執行 /setup-bedrock 重新開啟精靈調整憑證、區域或模型釘選。大規模或自動化部署則可改用環境變數設定。設定完成後執行 /status，確認 provider 顯示為「Amazon Bedrock」或「Amazon Bedrock (Mantle)」即代表成功連線。

🎯 實務啟示：企業導入前要想清楚的幾件事

文章建議導入前先確立身份與治理架構：用 AWS IAM Identity Center 集中管理 Claude Code 的身份與存取權限，讓開發者改用暫時性、角色型憑證，取代靜態 access key；開 Claude Code 前先以 `aws configure sso --profile <PROFILE_NAME>` 設定好 SSO 設定檔，再用 `aws sso login` 登入。大型企業可考慮採用 AWS 官方的 Guidance for Claude Code with Amazon Bedrock，統一管理 AI 資源存取並取得開發者使用狀況的可觀測性。另外務必依活躍開發者人數檢視並設定足夠的 TPM（每分鐘 token 數）與 RPM（每分鐘請求數）配額。模型版本也建議釘選：若不釘選，Claude Code 的模型別名預設會解析到 Claude Opus 5.5，等於整團隊都用 Opus 的計費費率，要維持在 Sonnet 需明確設定 ANTHROPIC_MODEL 為完整模型 ID，並用 ANTHROPIC_DEFAULT_OPUS_MODEL、ANTHROPIC_DEFAULT_SONNET_MODEL 控制團隊升級新模型的時機。

⚠️ 不是每個組織都適用

文章開頭特別聲明，這篇內容僅供參考，所述方案未必適合所有組織或合規計畫，仍須對照自身組織的合規要求與法規義務逐一評估。另外要注意，Guardrails 與呼叫紀錄功能目前僅透過 bedrock-runtime 端點提供，若合規需求仰賴這兩項功能，就不能只用 bedrock-mantle。

🔗 來源
- 標題：Supercharge regulated workloads with Claude Code and Amazon Bedrock
- 作者／機構：Bradley Wyman（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/supercharge-regulated-workloads-with-claude-code-and-amazon-bedrock/

#ClaudeCode #AmazonBedrock #Anthropic #AWSGovCloud #FedRAMP #AIAssistedDevelopment #RegulatedWorkloads #ITAR #CloudSecurity #DevOps
