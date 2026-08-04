---
title: 'From weeks to minutes: How Formula 1® uses agentic AI on AWS to accelerate
  data operations'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/from-weeks-to-minutes-how-formula-1-uses-agentic-ai-on-aws-to-accelerate-data-operations/
model: tencent/hy3:free
generated_at: '2026-08-04T08:29:54.369940'
score: 98
---

📌 【AWS 案例研究】F1 如何利用 Agentic AI 將資料整合週期從數週縮短至 40 分鐘

TL;DR：F1 利用 Amazon Bedrock AgentCore 打造 Data Accelerator，實現資料來源自動化入庫，效率提升 95% 以上。

在賽車運動的世界裡，決策速度必須與賽車的速度同步。對於擁有 8 億粉絲的 Formula 1 (F1) 來說，行銷技術（MarTech）平臺「Customer 360」是連結粉絲與商業策略的核心神經系統。然而，面對海量的數位互動數據，傳統的手動工程流程已成為制約業務發展的瓶頸。

🤔 **面對數據爆炸：18 個月的開發積壓與手動工程瓶頸**

F1 的數據來源極其多元，包含售票夥伴、串流媒體、贊助商數據、社群媒體及周邊商品系統。然而，這套系統曾面臨三大嚴峻挑戰：

*   **手動入庫效率極低**：每新增一個數據來源，工程師必須手動編寫 Schema 映射、建立數據管道（Pipeline）、配置數據品質檢查、定義 GDPR 分類並設定治理政策。這導致每個來源平均耗時 6 到 8 週，團隊甚至累積了 18 個月的待辦清單。
*   **上游結構變動頻繁**：供應商經常在未通知的情況下更改欄位名稱或調整 Payload 結構，這些變動往往發生在關鍵的賽事週末或行銷活動期間，導致管線失效。
*   **可視性破碎**：日誌（Logs）分散在 S3、Amazon Redshift、Airflow 與 DBT 等不同服務中，當指標出現問題時，工程師必須花費數小時手動追蹤數據譜系（Data Lineage）。

🧩 **Data Accelerator：基於 Agentic AI 的自動化解決方案**

為了應對挑戰，F1 與 AWS 合作開發了「Data Accelerator」，透過 Amazon Bedrock AgentCore 實現端到端的自動化操作。這不是單純的程式碼生成器，而是一套具備「模組化技能」的 Agent 架構。

該方案透過五個工作流同時運行，其中核心的 Agentic 工作流包含以下階段：

**第一階段：從需求文件到自動化 Pull Request**
1.  團隊將包含數據來源資訊的商業需求文件 (BRD) 上傳至 Amazon S3。
2.  AWS Lambda 觸發 Amazon Bedrock AgentCore Runtime，Agent 讀取 BRD 並生成配置檔案。
3.  Agent 透過 GitHub App 將檔案提交為 Pull Request (PR)，並透過 Jira API 自動建立對應的票券。
4.  工程師僅需進行審核與調整。

**第二階段：自動化基礎設施與轉換**
1.  一旦配置核准，Agent 會進一步生成三組獨立的 PR，分別對應基礎設施 (Infrastructure)、數據轉換 (DBT) 與治理 (Governance) 儲存庫。

**💡 具備合規能力的智慧 Agent**
與一般工具不同，此 Agent 整合了 GDPR 分類功能。它會主動分析每個數據欄位，判斷是否包含個人隱私或敏感資料，並直接將標籤發佈至 SageMaker Unified Studio 的治理註冊表，讓合規團隊能即時掌握狀況。

🧩 **模組化技能與多輪推理架構**

該系統採用模組化設計，每個 Agent 擁有一系列獨立技能，例如：
*   Schema 映射與資料類型推論
*   數據品質驗證
*   治理執行
*   敏感資料分類

在執行時，Agent 會透過「多輪推理過程 (Multi-pass reasoning process)」來精確執行任務：
*   **Pass-0**：處理 Token 管理與清理。
*   **Pass-1**：總結工具輸出結果。
*   **Pass-2**：彙整整體評估，逐步提升準確度與完整性。

📊 **從數週縮短至 40 分鐘的效能飛躍**

透過 Data Accelerator 的導入，F1 取得了顯著的營運成效：

| 指標 | 導入前 (Manual) | 導入後 (Agentic AI) |
| :--- | :--- | :--- |
| 新數據源入庫時間 | 6 至 8 週 | 約 40 分鐘 (程式碼生成) + 數小時 (部署與審核) |
| 自動化程度 | 人工手動處理 | 95% 以上由 Agent 自主處理 |
| 問題修復週期 | 以「天」為單位 | 以「小時」為單位 |

此外，該系統還具備「Schema 演進監控」能力。當上游數據結構變動時，Agent 能透過 Amazon EventBridge 偵測事件，評估對下游管線的影響，並自動生成修復程式碼與 Jira 票券，讓工程師只需進行最終審核。

🎯 **實務啟示**

對於處理大規模、高動態數據的工程團隊，F1 的案例展示了 Agentic AI 的實戰價值：它不只是輔助寫程式，更是在複雜的企業流程中（如合規、治理、跨系統追蹤）扮演了自動化協作的角色，將工程師從重複性的基礎建設工作中解放，轉向更高價值的任務。

🔗 **來源**
- 標題：From weeks to minutes: How Formula 1® uses agentic AI on AWS to accelerate data operations
- 作者／機構：Subhro Bose @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/from-weeks-to-minutes-how-formula-1-uses-agentic-ai-on-aws-to-accelerate-data-operations/

#AI #AgenticAI #AWS #MachineLearning #DataEngineering #Formula1 #DataOps #AmazonBedrock #DataGovernance #Automation
