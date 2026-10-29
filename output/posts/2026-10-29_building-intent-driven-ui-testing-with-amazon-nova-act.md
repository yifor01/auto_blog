---
title: Building intent-driven UI testing with Amazon Nova Act
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-intent-driven-ui-testing-with-amazon-nova-act/
model: claude-code/sonnet
generated_at: '2026-10-29T22:07:09.598125'
score: 87
---

📌 Epsilon如何用Amazon Nova Act把UI測試變成平臺服務

TL;DR：行銷科技公司Epsilon用Amazon Nova Act結合Bedrock AgentCore Browser Tool，把意圖導向的UI測試做成多租戶平臺能力。

選擇器（selector）一變，整條UI測試就斷；Epsilon的做法是讓測試步驟直接用自然語言描述「意圖」，不綁死在DOM結構上。

🤔 **既有測試沒壞，但缺一層意圖導向的能力**

Epsilon是Publicis Groupe旗下的資料、技術與行銷服務公司，管理數億消費者檔案與大量品牌關係。公司內部既有的Playwright regression suite運作良好，Epsilon要解決的不是取代它，而是在既有基礎上疊加一層intent-based測試，並且做成多租戶平臺服務，讓其他產品團隊透過統一API取用，不增加各團隊自己的維運負擔。負責這件事的是Agentic Platform團隊，一支50人工程團隊，專門建置skills-based agent builder、federated identity、pre-flight authorization、MCP整合與跨帳戶provisioning等共享基礎設施。Epsilon選擇Amazon Bedrock AgentCore Browser Tool，正是因為它免去了自行管理瀏覽器binary、display server與session生命週期的維運負擔。

🧩 **API、佇列與獨立runner的三層架構**

Epsilon的UI Testing Service分三個核心元件：建立workflow的平臺API、執行workflow的background task runner，以及驅動瀏覽器的Nova Act與Bedrock AgentCore Browser Tool整合。整體pipeline是：使用者請求經Agent Cloud Frontend，通過有身分驗證與權限檢查的API Gateway，進入Django REST API層，對外提供workflows、executions、automation suites、stats等endpoint；再交給Workflow Manager、Execution Orchestrator、Suite Coordinator組成的業務邏輯層。測試任務被放進Amazon SQS佇列，由跑在Amazon ECS上的Runner Service取出執行，Runner內含Nova Act engine與headless Chromium瀏覽器，執行結果、截圖、trajectory與HTML報告則存進Amazon S3。這個能力對外被包裝成一個標準agent（ui-test-agent），已上線的團隊透過和其他平臺agent相同的介面使用。核心整合模式是：開啟一個受管理的瀏覽器session，透過CDP WebSocket連線，再用自然語言驅動操作，Epsilon在這之上疊加自己的多租戶orchestration、結果擷取與observability層。文中舉例的一個18步驟測試流程涵蓋登入、表單輸入、條件判斷、滾動與驗證，其中條件邏輯，例如「如果出現某元素就處理它」、「如果目標元素看不到就持續滾動直到看到」，在傳統框架裡需要寫明確的branching邏輯，Nova Act靠語言理解直接處理。

💡 **幾條從生產環境學到的最佳實踐**

Epsilon把UI測試跑在獨立的FastAPI sidecar runner服務裡，固定使用支援Workflow與IAM authentication的nova-act 3.x版本，搭配Bedrock AgentCore Browser Tool client，刻意與主要後端的Strands agent stack依賴分開，避免衝突；如果runner被停用，worker會fallback成in-process執行，部署期間維持韌性。團隊也發現Nova Act的signing endpoint固定指向us-east-1，不管瀏覽器session實際在哪個region，把它獨立成一個服務並用自己的dependency lockfile可以避免難以除錯的依賴衝突。在重複執行的regression測試上，Epsilon採用trajectory retries：draft狀態下重試並保存成功的trajectory，到active狀態時直接replay，重複執行可以跳過多餘的LLM「思考」過程，同時降低延遲與成本。權限管理上採用cross-account AssumeRole搭配scoped IAM policies，每個租戶的測試在自己帳戶下的角色裡執行，達到隔離、可稽核與失敗範圍控制，不需要額外為每個團隊客製基礎設施。Bedrock AgentCore Browser Tool本身提供live view、session recording與AWS CloudTrail整合，Epsilon直接沿用這些內建能力做observability，省去自建成本，也讓合規團隊有熟悉的稽核介面。在撰寫測試步驟時也要考慮Bedrock AgentCore Browser Tool的瀏覽器viewport預設值，例如明確寫出「往下滾動直到看到Goal Statement文字框」這類指令，確保Nova Act能正確處理頁面下方的內容。

⚠️ **多租戶效益需要額外的服務層設計**

intent-based測試要發揮多租戶效益，需要額外的runner、SQS佇列、ECS執行環境與跨帳戶IAM設計，並非單純替換掉Playwright就能完成；signing endpoint固定在us-east-1的限制也需要額外的依賴隔離設計才能避免衝突。

🎯 **把intent-based測試當成補充，不是取代**

Epsilon團隊的建議是把intent-based測試當成既有regression suite的補充：意圖導向的步驟能撐過UI改版，而且連不寫程式的PM、QA也能直接看懂並審查測試步驟內容。如果你的組織也要讓多個產品團隊共用一套agent能力，這套「平臺API＋佇列＋獨立runner＋IAM隔離」的分層架構，是一個可以直接參考的落地範本。

🔗 **來源**
- 標題：Building intent-driven UI testing with Amazon Nova Act
- 作者／機構：Sakthi Chellapparimanam，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/building-intent-driven-ui-testing-with-amazon-nova-act/

#AmazonNovaAct #BedrockAgentCore #UITesting #AIAgents #AWS #IntentDriven #QAAutomation #MultiTenant #Playwright #AgenticAI
