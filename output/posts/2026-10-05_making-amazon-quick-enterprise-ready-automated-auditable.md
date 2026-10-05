---
title: 'Making Amazon Quick enterprise-ready: Automated, auditable cross-account resource
  promotion'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/making-amazon-quick-enterprise-ready-automated-auditable-cross-account-resource-promotion/
model: claude-code/sonnet
generated_at: '2026-10-05T23:31:36.010123'
score: 66
---

📌 讓 Amazon Quick 的 AI 助理資源「跨帳號升版」不再靠手動

TL;DR：AWS 用 Bedrock AgentCore 上的 MCP 伺服器,把 Amazon Quick 代理資源的跨帳號搬遷變成一鍵、可稽核流程。

企業導入 agentic AI 工具時,常常卡在一個很不「AI」的環節:怎麼把開發環境裡測好的代理,安全地搬到正式環境?Amazon Quick 團隊這次公開的解法,是用一個 MCP 伺服器把這整套手動搬遷流程自動化。

🤔 **從開發帳號搬到正式帳號,原來要手動重建一次**

Amazon Quick 是 Amazon 的 agentic AI 工作助理,使用者可以建立能呼叫 action connector、查詢知識庫、完成多步驟任務的代理（agents）。這類資源包括聊天代理、action connector、知識庫、flow 與 space。多數企業會把開發與正式環境拆成不同的 AWS 帳號（有些中間還有 QA 帳號）,但在此之前,把這些資源從開發帳號「升版」到正式帳號,並沒有原生的一鍵機制:團隊得手動重建每一個代理（複製相同的指令與起始提示詞）、重新掛接每個代理的 action connector、重新授予資源權限,並重新佈建知識庫背後的 S3 bucket、bucket 政策與資料來源。這個過程慢、難以稽核,而且容易出現細微錯誤,直接影響企業要的治理（governance）要求。

🧩 **三帳號架構 + 五個 MCP 工具,組成一套冪等（idempotent）搬遷流程**

這套解法之所以可行,關鍵在於 Amazon Quick 的資源（space、agent、action connector、knowledge base、flow）都是透過 Amazon Quick API（屬於 Amazon QuickSight API 的一部分）管理,提供完整的 CRUD 與 list 操作,也就是說使用者在介面上設定的一切,理論上都能用程式碼讀取、重建、更新與治理,包括權限。

文章介紹的 Quick Resource Migrator,是一個部署在 Amazon Bedrock AgentCore runtime 上的範例 MCP 伺服器。架構採三帳號模型:一個中央 runner 帳號負責跑 MCP 伺服器,伺服器透過 AWS STS 分別在來源帳號假設唯讀角色、在目標帳號假設可讀寫角色,因此不需要在任何地方存放長期有效的憑證。

伺服器對外暴露五個工具（皆定義於 server.py）:
- `preview_migration`:傳入來源帳號、資源類型、選取方式（id／名稱／全部）與區域,回傳將被搬遷的資源清單；若同時指定目標帳號,還會標示每個資源是會被 CREATE 還是 UPDATE,作為搬遷前的 dry run 與變更管理審核依據。
- `migrate_resources`:傳入來源與目標帳號、資源類型、選取方式、區域、環境名稱與 QuickSight 服務角色名稱,執行完整的 create-or-update 搬遷,回傳建立、更新與授權內容的結構化報告,因為是冪等設計,可以在每次 release 重複執行,結果會收斂到相同的目標狀態。
- `list_backups`:列出每個資源在搬遷前寫入備份目錄的各版本快照。
- `get_backup`:取得指定資源與版本（預設為最新）的完整備份內容,包含設定與相依關係。
- `restore_backup`:將儲存的備份版本重新套用到目標資源上（更新或在資源已不存在時重建）,且執行回復前會先對當前狀態做一次備份,確保回復動作本身也可逆。

這套工具可以透過 AWS CloudFormation 部署跨帳號 IAM 角色、VPC 網路,以及由 Cognito 驗證的 AgentCore runtime,再把這個 runtime 註冊成 Amazon Quick 的 action connector,之後就能用自然語言在 Amazon Quick 中直接驅動搬遷流程,或透過 repository 附帶的 app-builder 提示詞,快速生成一個點擊式的 Quick App 介面（選擇來源／目標帳號與要搬遷的資源、預覽變更、執行搬遷、檢視歷史記錄）。

💡 **設計上刻意不支援「刪除」,把風險降到最低**

這套遷移工具的一個關鍵設計選擇是:每次執行只會新增或更新資源,絕不對目標帳號發出刪除操作。每次更新前都會先把舊版本寫入 S3 做版本化備份,讓每個資源保有完整歷史可供檢視與回滾。對企業治理場景來說,這種「只增不刪＋版本化備份＋可回滾」的組合,比起單純的手動複製貼上,更貼近一般應用程式發布該有的可稽核性。

⚠️ **目前是範例專案,仍需要自行部署三套 CloudFormation 堆疊**

這套工具目前以 aws-samples repository 的範例程式碼形式提供,要上線使用需要自行部署三套 CloudFormation 堆疊（跨帳號 IAM 角色、VPC 網路、AgentCore runtime）,並手動完成 action connector 註冊等設定步驟,對團隊而言仍有一定的導入門檻。

🎯 **給工程師的啟示：agentic AI 資源也該納入 CI/CD 式的發布流程**

如果你的團隊正在用 Amazon Quick 建立代理與知識庫,這套做法提供了一個明確參考:把 AI 代理資源的升版當成一般應用程式發布來對待,用 API 驅動的 upsert、版本化備份與 dry-run 預覽取代手動複製,是在 agentic AI 工具逐漸進入企業生產環境後,治理與稽核不可或缺的一環。

🔗 **來源**
- 標題：Making Amazon Quick enterprise-ready: Automated, auditable cross-account resource promotion
- 作者／機構：Keshav Ganesh, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/making-amazon-quick-enterprise-ready-automated-auditable-cross-account-resource-promotion/

#AmazonQuick #AWS #AgenticAI #MCP #BedrockAgentCore #CloudGovernance #DevOps #EnterpriseAI #Automation #CloudArchitecture
