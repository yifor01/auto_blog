---
title: Implementing synthetic monitoring using Amazon Nova Act
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/implementing-synthetic-monitoring-using-amazon-nova-act/
model: claude-code/sonnet
generated_at: '2026-09-28T22:49:17.629248'
score: 78
---

📌 用Nova Act做網站監控：讓AI看畫面而不是抓DOM選擇器

TL;DR：Amazon Nova Act搭配Bedrock AgentCore，用多模態視覺理解取代傳統選擇器，做出更耐用的synthetic monitoring。

Selenium或Playwright腳本最讓人頭痛的，不是寫的時候，而是維護的時候：前端一改CSS class，測試就整套壞掉。這篇AWS部落格提出了另一種做法，讓監控agent像人一樣「看畫面」而不是去抓DOM節點。

🤔 **問題：使用者旅程失敗，後端訊號卻看不出來**

多數團隊透過metrics、logs、traces與API層級的檢查來監控基礎設施健康度，但高影響力的故障往往發生在使用者旅程層級，這些後端訊號未必能即時反映問題。常見情境包括：前端部署把結帳按鈕弄壞了、第三方登入頁面悄悄改版、或是UI回歸讓關鍵元素失去反應。傳統瀏覽器自動化框架依賴明確的DOM定位器與選擇器，一有小改動就容易整套失效，團隊往往花更多時間在維護選擇器、處理時序不穩定，而不是打造新的自動化測試。這類需求橫跨電商（商品搜尋、價格庫存顯示、購物車、結帳確認）、金融服務（帳戶存取、交易流程）、旅遊訂房、SaaS訂閱升級，以及醫療掛號系統。

🧩 **架構設計：Nova Act看畫面，AgentCore管生命週期**

Amazon Nova Act使用多模態大型語言模型直接處理UI截圖，而不是解析DOM選擇器，這讓它對UI變動更有韌性，因為模型是根據畫面上實際看到的東西做推理，而不是依賴CSS class或元素ID，樣式改變時不需要更新腳本。文章指出，在早期的企業客戶案例中，Amazon Nova Act在瀏覽器工作流程上展現出超過90%的準確率，比選擇器一有元素變動就直接失效的傳統做法有明顯改善，但作者也提醒團隊應該在自己的網站上實測，並為適應失敗的情況設計重試邏輯。整體架構結合Amazon Nova Act與Amazon Bedrock AgentCore：agent的動作透過act()以自然語言驅動UI操作，驗證則透過act_get()搭配布林值schema在關鍵檢查點做斷言；部署到AgentCore Runtime後，執行環境會透過Browser工具管理瀏覽器session的生命週期。當旅程失敗時，agent會發布旅程類型、目標URL、耗時、已完成步驟與失敗步驟，詳細的例外資訊則保留在runtime日誌中。

🧩 **怎麼用：從定義旅程到排程執行**

實作的第一步是定義最重要、必須驗證的顧客旅程。以電商應用為例，通常包括首頁載入、商品搜尋、商品詳情頁瀏覽、加入購物車驗證與結帳準備。重點是明確驗證結果，例如確認搜尋結果正確顯示、購物車確實包含商品、頁面上沒有出現錯誤橫幅，而不是只驗證流程有沒有跑完，這能同時降低「檢查不完整導致的假陽性」與「斷言過於寬鬆導致的假陰性」。部署上，需要先用Nova Act CLI的act workflow指令把agent打包、推送容器映像檔到Amazon ECR並佈建runtime；部署完成後端點ARN維持不變，之後的更新只會建立新的runtime版本，不需要更改Scheduler的目標設定。範例程式庫中的deploy.py腳本把這些指令包裝起來，並加入前置檢查（Docker、AWS憑證）、建立SNS警示主題、串接Amazon EventBridge排程，讓一行python deploy.py就能完成端到端部署；若要更正式的可重複部署流程，範例也提供CDK stack作為替代方案，內建最小權限IAM、SNS警示主題，以及用來捕捉失敗InvokeAgentRuntime呼叫的SQS死信佇列，並設置兩個CloudWatch警示：一個監控死信佇列深度，一個監控排程是否有漏跑（利用AWS/Scheduler的InvocationAttemptCount指標，把資料缺失視為異常）。實測中，一個六步驟的旅程通常在2到4分鐘內完成，實際時間依頁面載入速度而定。

⚠️ **限制與最佳實務**

文章特別提醒一個容易忽略的盲點：這些CloudWatch警示只能偵測基礎設施層級的故障，例如排程沒有觸發或呼叫沒有送達agent；如果顧客旅程在功能上已經壞掉、但HTTP層級仍回傳200，這種情況會透過agent的SNS發布訊息被發現，而不會觸發CloudWatch警示。另外，建議監控重點應放在3到5個高價值的關鍵旅程（登入、結帳、帳戶存取），而不是追求頁面覆蓋率，過度監控反而會製造雜訊，讓團隊對真正的故障失去敏感度；斷言也應該針對有意義的結果，而不是逐一檢查每個DOM元素，過度細緻的斷言只會增加假陽性卻不會提升故障偵測能力。範例程式碼採用單次嘗試執行每個步驟，用意是把Browser session的成本降到最低。

🎯 **實務啟示**

如果你的團隊正被選擇器維護成本壓得喘不過氣，這個架構提供了一個值得評估的方向：用視覺推理取代DOM定位，把監控重心從「頁面覆蓋率」轉移到「關鍵旅程的結果驗證」。但既然準確率是90%而非100%，落地前務必在自家網站上實測，並設計好重試與例外處理機制，而不是直接假設AI一定能像人一樣穩定地完成每一步操作。

🔗 **來源**
- 標題：Implementing synthetic monitoring using Amazon Nova Act
- 作者／機構：Sarath Krishnan, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/implementing-synthetic-monitoring-using-amazon-nova-act/

#AmazonNovaAct #BedrockAgentCore #SyntheticMonitoring #AWS #AIAgent #BrowserAutomation #MultimodalAI #DevOps #Observability #CloudMonitoring
