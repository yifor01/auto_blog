---
title: Extend Claude Code to remote sessions on Amazon Bedrock AgentCore with security
  controls
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/extend-claude-code-to-remote-sessions-on-amazon-bedrock-agentcore-with-security-controls/
model: claude-code/sonnet
generated_at: '2026-11-06T22:19:57.781227'
score: 88
---

📌 讓 Claude Code 離開你的筆電：在 Amazon Bedrock AgentCore 上跑遠端編碼 Agent

TL;DR：AWS 示範如何把 Claude Code 搬到 Bedrock AgentCore 遠端執行，每個任務在隔離 microVM 中跑完直接回傳 GitHub PR。

交出一個任務、關上筆電、回來看結果——這是遠端編碼 agent 想解決的核心問題。AWS 這篇文章給出了一套在自己 AWS 帳戶內落地這個流程的具體架構，還附上了完整的安全控制清單。

🤔 **本地跑 Claude Code 很方便，但一次只能跑一件事**

許多團隊已經在本機上以 Amazon Bedrock 作為模型供應商執行 Claude Code。文章指出，選用 Bedrock 的理由包括：透過既有 AWS 帳戶計費與抵免額、不需要按席位授權、透過 AWS CloudTrail 做稽核紀錄，以及可選擇地理推論設定檔以滿足資料落地（data residency）需求。但本地執行有其限制：任務彼此競爭同一臺機器的運算資源,且每次只能盯著一個任務跑。

遠端編碼 agent 把任務變成一次「交辦」：指派任務後可以關閉筆電或去做別的事,多個任務能同時在各自獨立、用完即棄的環境中執行,不受本機憑證影響,結果以 PR 形式交回,讓同事能像審查其他程式變更一樣審查它。代價是：任務執行過程中你能介入的程度較低、環境需要額外設定、成本也較難預估。

🧩 **架構：AgentCore Runtime Session + GitHub App + Guardrails**

AWS 提供的範例專案 sample-remote-coding-agent，把整套流程架在你自己的 AWS 帳戶中。任務從 Claude Code 或網頁控制台出發，經過控制平面，進入 VPC 內一個獨立的 AgentCore runtime session 執行，最後以 GitHub PR 形式輸出；每一步的狀態都會寫入 DynamoDB，供 Claude Code 與控制台追蹤任務進度，審查階段也可以把任務退回規劃階段重跑。

文章列出了幾項具體的安全控制設計：

- **模型呼叫**：每個 session 中 Claude Code 僅以 Amazon Bedrock 為模型供應商，呼叫經由私有 Bedrock endpoint，並以該 runtime 的 IAM 執行角色簽署，容器內不持有其他 AWS 憑證，因此遠端任務的模型呼叫維持與本機執行相同的安全特性。
- **隔離環境**：每個任務在專屬的 AgentCore runtime session（一個獨立 microVM）中執行，session 結束後記憶體會被清除；AgentCore memory 只在同一個 repository 的不同任務之間延續經驗教訓。
- **GitHub 憑證**：agent 從不持有長效的 GitHub 憑證。範例會建立一個具 Contents 與 Pull requests 讀寫權限的 GitHub App，並註冊到 AgentCore Identity，由其 token vault 保管 client secret；每個容器取得的 user-to-server token 會在 8 小時後過期並自動更新，且只能存取該 App 已安裝且授權使用者有權限的 repository，commit 會以 App 的 bot 帳號署名。
- **提示詞過濾**：任務排入佇列前，API 會透過 Amazon Bedrock Guardrails 的 ApplyGuardrail API 篩檢提示詞，使用理解程式碼的 Standard tier，在低強度設定下阻擋 jailbreak、prompt injection 與惡意請求（如要求撰寫 malware），也會阻擋 AWS access key 等機密資訊；若 guardrail 無法回應，任務會被拒絕執行。文章也坦言這道防線只篩檢「你輸入的內容」，不會檢查 agent 執行過程中讀到的 repository 檔案或指令輸出，因為逐次呼叫都重新檢查整段上下文的成本太高，且會誤判 Claude Code 自身的 system prompt。
- **網路隔離**：每個 AgentCore runtime 跑在你 AWS 帳戶 VPC 的私有子網路中，透過 VPC endpoint 呼叫所需的 AWS 服務，相關提示詞、任務狀態與日誌不會經過公開網路；唯一對外路徑是供 GitHub 與套件註冊表使用的 NAT gateway，安全群組只允許 outbound HTTPS，並以 Amazon Route 53 Resolver DNS Firewall 封鎖模型供應商自身網域（如 api.anthropic.com）；文章也提醒這只是 denylist，正式環境建議改用 AWS Network Firewall 的網域白名單機制。
- **權限最小化**：AgentCore runtime 的 IAM 角色僅能呼叫 Bedrock 上的 Anthropic 模型、讀寫自己 repository 的任務紀錄與記憶，以及拉取 agent 映像檔；且明確禁止存取 AgentCore Identity 控制平面，避免單一任務更改所有 repository 共用的 GitHub 憑證供應商。agent 只會開 PR，不會自動合併，文章建議對預設分支啟用分支保護（branch protection），確保每個變更都經過審查。

🎯 **實務啟示**

對已經在用 Bedrock 跑 Claude Code 的團隊，這套架構提供了一條把「單人本機工作流」擴展成「多任務並行、可稽核」管線的現成路徑，而不必自建 agent 執行環境與憑證管理機制。部署前要注意：範例文件標示整套部署耗時 15–25 分鐘、註冊 repository 另需 8–12 分鐘，且即使閒置也會持續產生費用（NAT gateway、interface endpoint、AWS WAF、Cognito user pool、DNS Firewall、映像檔與日誌等），部署時會設定預設每月 200 美元的 Bedrock 預算提醒，但不會自動封頂花費，官方也明確表示未提供成本估算，用完建議照文件的 Clean up 步驟清理資源。

🔗 **來源**
- 標題：Extend Claude Code to remote sessions on Amazon Bedrock AgentCore with security controls
- 作者／機構：Andrew (Qingjie) Ren, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/extend-claude-code-to-remote-sessions-on-amazon-bedrock-agentcore-with-security-controls/

#ClaudeCode #AmazonBedrock #AgentCore #AWS #AIAgent #CloudSecurity #DevOps #RemoteAgent #GitHub #CodingAgent
