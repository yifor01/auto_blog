---
title: 'Agentic Data Operations Platform (ADOP): Data engineering into hours'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agentic-data-operations-platform-adop-data-engineering-into-hours/
model: claude-code/sonnet
generated_at: '2026-08-22T06:12:56.087652'
score: 96
---

📌 【AWS】ADOP:把資料工程從「幾週」壓縮到「幾小時」的代理平臺

TL;DR:ADOP 是建構在 Amazon Bedrock 上的參考架構,用專責 AI 子代理自動產生 ETL、品質檢查與合規控制,但正式環境仍只執行確定性的程式碼。

資料工程團隊要接上一個新的資料來源,常常得花上好幾週:寫 ETL、手刻資料品質檢查、更新語意模型、驗證合規性。Amazon Bedrock 上的 Agentic Data Operations Platform（ADOP）就是為了大幅縮短這段時程而設計的參考架構。

🤔 六個拖慢資料工程速度的老問題

對資料工程主管來說,ADOP 想改變的是三件事:工程師不再把大部分時間耗在管線的水電工程上,轉而專注在真正交付資料產品;合規從下游的關卡,變成資料來源導入時就內建的控制;而架構本身,而不是模型本身,決定每一種 AI 程式碼工具（Claude Code、Kiro、Cursor、Codex）如何與資料系統互動。

🧩 開發環境跑代理,正式環境跑確定性程式碼

這是 ADOP 與一般代理平臺提案最大的差異:它是一個建置期加速器,而不是執行期依賴。代理在開發環境中運作,負責推理、提出方案並生成內容,包括 ETL 程式碼、品質檢查、語意層定義、法規控制,工程師負責審查產出的結果。CI/CD 接著把產出的內容,包括確定性的 PySpark、SQL、Airflow DAG,以及 IAM 與 Cedar 政策,推進到 staging 與正式環境。在 ADOP 的預設模式下,正式環境執行的是確定性內容,不會在執行期呼叫模型;若組織需要執行期的 model-in-the-loop 推論,可以用 Amazon Bedrock endpoint 擴充這套架構,但產出的管線程式碼本身仍維持靜態、可稽核。

具體實作上,ADOP 透過 Amazon Bedrock 在 Claude Code 上啟動一個 Data Onboarding Agent,利用 Claude Code 的 Dynamic Workflow 功能,為管線建構的每個階段孵化專責的子代理:分別處理中繼資料生成、資料本體推導、資料品質檢查、ETL 轉換,以及編排（Airflow 或 AWS Step Functions）。需求會透過與使用者角色的對話持續補充,每個產出的內容都會先在本地驗證,再以人工審核的方式部署到 AWS。

架構中還有 Decision Engine,可以理解為企業架構師的 AI 化身,把組織的準則、技術標準與設計哲學直接內嵌進建置流程,幫助不同團隊在使用一般化程式碼工具時,不會各自產出不一致的架構。子代理則受到架構契約的約束,包括工具路由規則、Cedar 授權政策、不變條件與內嵌的合規提示詞。雖然參考實作以 AWS 為目標,但這套框架可以透過 CLI 或 Model Context Protocol（MCP）介面,延伸到其他服務,支援混合雲與多雲環境。

在合規面,ADOP 讓每個治理框架對應一則法規提示詞,套用在資料來源導入的當下,讓法務審查的是提示詞檔案,而不是應用程式碼,但使用者仍需自行驗證這些控制是否符合實際的法規義務。在可觀測性面,每個代理決策（意圖、選用的工具、結果、成本）都會透過 AgentTrace 追蹤,並可發佈到 Amazon CloudWatch 或 OpenTelemetry sink 供稽核使用。整個堆疊預設在本地開發環境執行,當規模需求出現時,可以在不改變架構契約的情況下,升級到 Amazon Bedrock AgentCore 的 runtime 能力。

⚠️ 代理可能碰觸受管制資料,責任仍在使用者

代理在開發過程中可能會處理受管制或個人識別資料,使用者需要自行檢視資料處理實務、套用適當的存取控制,並在把產出內容推進到正式環境前,驗證代理行為符合組織的負責任 AI 政策。文章也強調,ADOP 提供的是合規相關控制的協助,使用者仍須自行驗證這些控制是否滿足自身的法規義務。

🎯 導入是組織變革,不只是技術導入

架構前期偏重架構本身,因為把組織標準編碼進系統是一次性投資,契約建立之後,每接上一個新的資料來源就變成一則提示詞,而不是一個專案。文章建議的導入方式包含三層溝通對象:高階主管每月看進度儀表板,平臺與資料工程主管每週看衝刺摘要,第一線工程師則透過團隊頻道即時更新,並在第一場導入會議前先發布一頁 FAQ,說明代理產出程式碼品質與工作影響等常見疑慮。訓練規劃則從第一週的架構契約與 Decision Engine 設定工作坊開始,第二週實作提示詞撰寫,由每個團隊端到端導入一個低風險資料來源,第三週檢視產出內容與守則設定,第四到六週提供每週兩次的答疑時段,之後降為每週一次。分階段推展則建議第一到三週先讓兩到三位工程師先鋒與一個非關鍵資料來源試行,驗證輸出品質並回饋修正架構契約,第四到六週再擴大到整個平臺團隊。

🔗 來源
- 標題：Agentic Data Operations Platform (ADOP): Data engineering into hours
- 作者／機構：John Cherian, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/agentic-data-operations-platform-adop-data-engineering-into-hours/

#AmazonBedrock #ADOP #DataEngineering #AgenticAI #ClaudeCode #ETL #DataGovernance #AWS #MCP #AIAutomation
