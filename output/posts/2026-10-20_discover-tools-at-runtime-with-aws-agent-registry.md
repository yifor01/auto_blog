---
title: Discover tools at runtime with AWS Agent Registry
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/discover-tools-at-runtime-with-aws-agent-registry/
model: claude-code/sonnet
generated_at: '2026-10-20T20:50:21.893526'
score: 93
---

📌 工具太多讓Agent迷路?AWS Agent Registry改用runtime搜尋

TL;DR:AWS Agent Registry讓orchestrator在每次請求時動態搜尋並組裝工具,免除硬編碼與重新部署。

Demo裡把幾個工具寫死進orchestrator看起來毫無問題,但企業內部往往有上百個涵蓋定價、客服、訂單、庫存、客戶資料的API——當工具數量膨脹到這個規模,模型花在「搞清楚該用哪個工具」的token,可能比花在真正理解使用者需求上的還多。

🤔 **硬編碼工具,最後變成跨團隊的部署瓶頸**

每多一個新能力,就要改orchestrator的程式碼、重新部署,還得協調各團隊的release節奏,而這些團隊往往更想按自己的步調上線。這種build-time wiring的方式在工具目錄擴張後會變成明顯的瓶頸,尤其是在企業SaaS場景中,團隊需要把龐大的內部API曝露給agentic consumer使用。

🧩 **Discover → Instantiate → Execute 的每請求迴圈**

AWS Agent Registry是一個用來編目與發現MCP伺服器、agent與agent skill的受管服務。發布者註冊協定專屬的descriptor與可被搜尋的描述,orchestrator在runtime時搜尋已核准、可被發現的記錄,並用回傳的endpoint與descriptor內容來建構client——但搜尋結果不會回傳該能力的呼叫憑證或驗證方式。

文章示範的sample架構包含:透過Amazon Bedrock AgentCore Gateway部署的訂單管理MCP伺服器、兩個跑在AgentCore runtime上的agent-to-agent(A2A)agent、一個Registry,以及一個orchestrator。整個流程是這樣運作的:

1. orchestrator把自然語言查詢送進AWS Agent Registry的data plane,回應包含記錄身分、名稱、描述、記錄類型、狀態、版本與協定descriptor(MCP伺服器metadata或A2A agent card),但不含呼叫憑證。
2. 針對每個回傳的記錄,orchestrator依descriptor類型建構對應client:MCP伺服器需要另外透過Cognito OAuth取得access token再建立`MCPClient`;A2A記錄則透過boto3 data-plane client呼叫AgentCore runtime,並用呼叫者自己的AWS憑證簽署請求——也就是說,Registry只提供連線metadata,驗證材料要走獨立且受信任的設定路徑取得。
3. 一個只包含這次動態發現到的工具的ephemeral inner agent被建立出來,由LLM挑選合適的工具完成任務,結果整合回覆給使用者後,這個inner agent與其client就被拆除。下一個請求會重新搜尋、拿到全新的工具組合。

整個reference architecture用到AWS Agent Registry、Amazon Bedrock AgentCore Gateway、Amazon Bedrock AgentCore runtime、Amazon Bedrock、Amazon Cognito、AWS Lambda與AWS Secrets Manager。

📊 **三個示範場景測試不同的發現組合**

Sample跑了三個場景:第一個是純MCP呼叫(查訂單狀態);第二個串接MCP加A2A(查詢定價與折扣);第三個特別測試語意比對能力——使用者問「退貨與退款」,但這些字詞並沒有出現在實際比對到的A2A agent名稱裡,系統仍正確比對到「Customer Support Agent」。

在Registry記錄的生命週期上,建立記錄時`recordType`是必填欄位(MCP伺服器用`"MCP"`,A2A agent用`"AGENT"`),協定metadata存放在descriptor物件底下的`mcpServer`或`a2aAgentCard`。當`autoApproval`設為`false`,新記錄要經過DRAFT → PENDING_APPROVAL → APPROVED三個狀態,送審與狀態更新動作都走IAM授權,讓發布者與審核者的權限可以分開管理;只有APPROVED的記錄才會被discoverable data plane回傳。Data-plane client支援混合關鍵字與語意搜尋,最新的方法名稱是`search_discoverable_registry_records`。

💡 **發現(discovery)與驗證(authentication)被徹底拆開**

這套設計最關鍵的一點,是把「知道這個能力存在、怎麼連」和「有沒有權限呼叫它」拆成兩條路徑:Registry只回傳descriptor與連線metadata,真正的憑證永遠透過另一條受信任的設定流程取得。這讓工具目錄本身可以被廣泛搜尋,卻不會變成憑證洩漏的風險面。

⚠️ **目錄變大不代表搜尋結果自動變好**

文章特別提醒,這篇文章不假設目錄規模越大、排序品質就自動變好,搜尋品質應該用具代表性的查詢去實際評估。文中範例裡的sample為了提高訂單管理領域的召回率,會對同一個請求發出多次搜尋查詢再去重——但這是sample自己的編排選擇,並不是Registry本身的要求。

🎯 **實務啟示**

對於內部API數量已經多到讓orchestrator「選工具比想問題還花力氣」的團隊,把工具綁定從build-time搬到runtime discovery,可以讓新能力上線後不需要改orchestrator程式碼、不需要協調跨團隊的部署排程,只要完成Registry的註冊與審核流程即可被使用——但代價是搜尋品質需要自己用真實查詢去驗證與調校,不能假設規模一大就會變準。

🔗 **來源**
- 標題:Discover tools at runtime with AWS Agent Registry
- 作者／機構:Vibhu Pareek
- 連結:https://aws.amazon.com/blogs/machine-learning/discover-tools-at-runtime-with-aws-agent-registry/

#AIAgent #AWSAgentRegistry #MCP #AgentCore #ToolDiscovery #MultiAgent #AmazonBedrock #AgenticAI #CloudArchitecture #A2A
