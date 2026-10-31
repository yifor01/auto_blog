---
title: 'Managing Amazon Bedrock costs end to end: A playbook for FinOps and platform
  teams'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/managing-amazon-bedrock-costs-end-to-end-a-playbook-for-finops-and-platform-teams/
model: claude-code/sonnet
generated_at: '2026-10-31T20:40:50.766176'
score: 70
---

📌 誰在為Agent買單?Amazon Bedrock的五階段成本治理迴圈

TL;DR:AWS提出Bedrock成本治理五階段迴圈——歸因、可觀測、強制執行、最佳化、定期檢視,解決agentic workload燒錢卻追不到帳的問題。

一個對話式助理,每輪使用者互動大概對應一次模型呼叫;但一個agentic workflow——規劃變更、讀檔案、呼叫工具、反覆迭代——每個任務可能觸發數十次呼叫,而且每次攜帶的context都更大。這意味著token消耗量跟隨的是workload被賦予的自主程度與context大小,而不是使用者互動次數。這也是為什麼「比較每個模型的token單價」或「要求應用團隊把prompt寫短一點」這類做法,終究答不出財務與工程主管真正關心的問題:這筆錢是誰花的、花在哪個workload上、有沒有在核準的預算內。

🤔 **成本治理是架構與運維問題,不是價格問題**

AWS在這篇playbook裡把這個現象講得很直白:生成式AI的成本管理是應用團隊與雲端支出責任團隊共同的責任。既然消耗量是workload怎麼設計、怎麼運作的函數,那麼成本管理本質上就是一套架構與運維紀律,而不是換一個便宜模型就能解決的事。

🧩 **五個階段,跑成一個持續迴圈**

這套方法分五步:歸因(Attribute)——每一塊Bedrock花費都落在帳務流程中某個身份、團隊、應用上;觀測(Observe)——每個請求都帶著足夠的metadata被記錄下來,能解釋這筆花費是怎麼產生的;強制執行(Enforce)——預算要有實際約束力,至少要有警示,風險夠高時要能硬擋;最佳化(Optimize)——調整平臺層面的預設值(模型路由、快取、token上限),從源頭移除浪費,而不是指望每個團隊自己小心;運維(Operate)——用一個精簡的scorecard與定期檢視節奏,把數據轉成決策。FinOps負責第一與第五階段,平臺工程負責第二到第四階段,檢視則是共同進行。這個順序是刻意設計的:沒有先做好歸因與觀測就直接跳去最佳化的團隊,基本上是在瞎猜。

📊 **歸因的關鍵陷阱:共用IAM角色會讓你什麼都看不見**

Bedrock的granular cost attribution會自動把每次推論花費歸因到發出呼叫的IAM principal,涵蓋所有模型、不需要額外建置資源,呼叫者的ARN會出現在AWS Cost and Usage Report(CUR)2.0的line_item_iam_principal欄位,覆蓋IAM使用者、角色、聯合身份與API金鑰。

但最容易悄悄失去歸因能力的情境是「共用角色問題」:如果一個LLM gateway用單一IAM角色呼叫Bedrock,所有花費都會歸到那一個角色上,等於完全失去逐使用者的可見度。解法是per-user session management——gateway每個使用者只呼叫一次sts:AssumeRole,把使用者身份當作role session name、使用者屬性當作session tag傳入,並把憑證快取最多一小時(也就是每個使用者每小時一次STS呼叫,而不是每次請求都呼叫)。這需要兩個角色:一個擁有sts:AssumeRole與sts:TagSession權限的gateway執行角色,以及它所假扮的Bedrock invocation角色。結果是line_item_iam_principal會出現像assumed-role/BedrockRuntimeRole/gw-alex這樣的紀錄,並帶著該使用者的tag——在共用gateway背後重建出逐使用者、逐租戶的歸因能力。

除此之外還有兩種歸因機制:Application inference profile是預先建立、掛在bedrock-runtime端點上、帶有成本分攤標籤的per-application資源,每個應用、每個模型、每個region建一個profile,適合應用與模型組合小而穩定的團隊;Projects/workspace則服務bedrock-mantle端點(Responses API、Chat Completions API),一個project ID可以橫跨多個模型,適合模型使用會頻繁變動的團隊,也是Bedrock上OpenAI相容workload的歸因路徑。AWS的建議是:bedrock-runtime workload優先用IAM principal加session tag做歸因,因為它跟著身份系統自然擴展、不需要預建資源、覆蓋所有模型與API操作;application inference profile適合不想改動身份設計、又需要發票等級分帳的小型穩定業務單位;projects則用在bedrock-mantle、Responses API或Chat Completions API的workload上。

📊 **CUR告訴你誰花了錢,invocation log告訴你發生了什麼事**

Bedrock支援把request、response與metadata的model invocation log送到CloudWatch Logs與/或S3。CloudWatch適合即時的運維查詢,S3加Athena適合長期的BI分析。文章建議把logging當成基礎設施來對待——用程式碼佈建log group或bucket、定義好retention與加密政策、在環境建置時就驗證傳遞是否正常,因為如果logging只存在於開發環境或單一region,成本治理計畫在用量成長時就會立刻出現缺口。Logging也能補上CUR的延遲缺口:CUR的歸因大約延遲24小時,而CloudWatch加OpenTelemetry可以在數分鐘內做出近即時的逐開發者支出儀表板。原始log只能回答身份層級的問題,要回答workload層級的問題(哪個功能、流程或租戶產生了這些token),就必須在每次呼叫上打上request metadata——但Bedrock並不強制metadata格式,若每個應用各自為政,團隊很快就會漂移出不一致的schema。

🎯 **實務啟示**

對正在規模化使用Bedrock的平臺與FinOps團隊而言,這份playbook點出一個容易被忽略的順序問題:在歸因與觀測還沒做穩之前就去談模型路由、快取這類最佳化,等於是在猜測,而不是在治理。優先檢查自己的LLM gateway是不是正踩在「共用角色」陷阱上,並盡早依workload形態(bedrock-runtime、穩定的少量應用、或OpenAI相容端點)選對歸因機制;同時在組織內盡早統一request metadata的schema,避免每個應用各自發明一套,日後要做workload層級的成本分析時才不會卡在資料不一致上。

🔗 **來源**
- 標題：Managing Amazon Bedrock costs end to end: A playbook for FinOps and platform teams
- 作者／機構：Aswath Ram A Srinivasan, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/managing-amazon-bedrock-costs-end-to-end-a-playbook-for-finops-and-platform-teams/

#AmazonBedrock #FinOps #CloudCostManagement #AWS #LLMOps #GenAI #IAM #CostAttribution #CloudGovernance #MLOps
