---
title: 'Tokenomics at scale: How Jamf built real-time spend enforcement for Amazon
  Bedrock'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-how-jamf-built-real-time-spend-enforcement-for-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-09-02T10:26:20.516330'
score: 79
---

📌 Jamf 如何為 Amazon Bedrock 打造即時個人層級花費管控

TL;DR：Jamf 用 IAM 客製政策、Athena 成本視圖與 Lambda 執行迴圈，實現不需中斷工程師工作階段的即時 Bedrock 花費上限管控。

「花費」這件事，在生成式 AI 時代變得不一樣了：傳統運算成本隨已佈建的容量而變化，AI 花費卻是隨行為而變化。一位工程師跑一個 agentic coding 迴圈打高階模型，幾小時燒掉的 token 可能超過整個團隊一週的用量。用量在帳單來之前幾乎是隱形的，這讓成本控管與投資報酬率都很難證明，這正是「tokenomics」問題的核心。管理超過 76,000 個組織裝置的 Jamf，在把 Amazon Bedrock 開放給整個工程團隊使用後，直接撞上了這個問題。

🤔 **上線前想清楚三個問題**

在擴大 AI 使用範圍之前，領導層想知道：每人平均花費多少？能不能在不拖慢工程師速度的前提下設上限？生產力提升是否真的划算？Jamf 因此打造了一套能做到「個人層級」精細度的系統。

🧩 **三個元件各司其職**

整套架構分成三個關注點：量測花費、決定要限制誰並通知、以及執行限制，各由一個 serverless 元件負責：

- **量測**：Bedrock 的呼叫紀錄以 JSON 落地到 S3，架構上以 Athena 建表，再建立一個把 token 數換算成美金的 view，依每個模型的公開單價分別乘上輸入與輸出 token 數，並依使用者身分與當天日期分組。每個模型家族都需要一條明確的計價分支，未被對映的模型會以最高階單價計費作為 fail-safe，避免未知模型繞過限制。
- **執行限制**：透過 IAM Customer Managed Policies（CMP），針對特定使用者（以 saml:sub 識別）封鎖特定模型家族的存取權，初始使用者清單為空，由 Lambda 在執行時動態發布新的政策版本；當以 iam:CreatePolicyVersion 更新這些政策時，變更會立即生效，不需要重新佈建。
- **決策與通知**：一個排程在 Amazon EventBridge 上每 15 分鐘執行一次的 Lambda，查詢 Athena view、讀取 DynamoDB 例外表，計算各層級的受限使用者清單，再發布更新後的 CMP 版本。

具體的分級規則是：花費達到當日預算 80% 時，禁用 Anthropic Claude Opus；達到 100% 時，禁用 Anthropic Claude Sonnet；但不封鎖 Anthropic Claude Haiku，讓工程師仍保有一個低成本模型可以繼續工作。限制在幾分鐘內生效，不需要重新登入，並在隔天重置時自動解除。

💡 **冪等設計省掉了「解除封鎖」的程式碼路徑**

這套系統的一個關鍵設計是每次執行都從當天的累計花費重新計算完整的受限清單，而不是套用增量變更，這代表連續執行兩次、或整段時間漏跑，最終收斂的結果都一樣，沒有東西需要重複套用或回滾。每日重置也是隱性的：Athena view 把花費範圍限定在以指定時區為準的當日滾動視窗內，一旦跨過午夜，下一次執行重新計算出的清單自然就不包含已不超標的使用者，對應的 CMP 限制會在下一次 iam:CreatePolicyVersion 呼叫時自動解除，不需要額外維護一套「解除封鎖」的邏輯。

對於確實需要更高額度的工程師（例如大型遷移、客戶緊急事件或模型評估），系統提供一個 Slack 斜線指令 /bedrock-limit，管理員可用它核發限時額度。指令會在 DynamoDB 例外表寫入一筆紀錄，包含工程師身分、提高後的額度與到期時間戳記，並記錄誰核發、何時核發，以及（選擇性地）核發依據的工單編號，並設定 DynamoDB TTL 屬性讓例外資料到期後自動清除。

🎯 **實務啟示**

這套架構的價值不在於用了什麼新穎演算法，而在於它把「花費治理」拆成量測、決策、執行三個獨立又可各自替換的元件，並用冪等設計避免了狀態同步的麻煩。對於任何正在把 LLM 存取權開放給大量工程師、又擔心成本失控的團隊，這是一個可以直接參考、甚至照抄部署模式的範例（Jamf 已將程式碼以 aws-samples/sample-bedrock-spend-enforcement 之名公開在 GitHub 上）。

🔗 **來源**
- 標題：Tokenomics at scale: How Jamf built real-time spend enforcement for Amazon Bedrock
- 作者／機構：Arun Chandapillai, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-how-jamf-built-real-time-spend-enforcement-for-amazon-bedrock/

#AmazonBedrock #AIFinOps #CostGovernance #AWSLambda #IAM #AmazonAthena #LLMCostControl #CloudArchitecture #Serverless #EnterpriseAI
