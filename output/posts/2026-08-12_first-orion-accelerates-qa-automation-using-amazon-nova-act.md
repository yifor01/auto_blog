---
title: First Orion accelerates QA automation using Amazon Nova Act
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/first-orion-accelerates-qa-automation-using-amazon-nova-act/
model: claude-code/sonnet
generated_at: '2026-08-12T07:38:48.609878'
score: 87
---

📌 用英文寫測試案例，AWS Nova Act 如何解決 First Orion 的 QA 塞車

TL;DR：First Orion 用 Amazon Nova Act 讓 QA 分析師直接用英文描述測試案例，取代維護容易失效的 Selenium/Playwright 腳本。

開發團隊的出貨速度越衝越快，QA 卻越來越追不上進度——這聽起來像是人力不足的問題，但 First Orion 的經驗顯示，真正的病灶其實出在傳統測試框架的設計本質上。

🤔 **架構轉型後，QA 反而成了瓶頸**

First Orion 是一家品牌通訊公司，服務涵蓋美國、加拿大、英國、德國多家電信商，包含 T-Mobile、Verizon、AT&T、Boost Mobile、Vodafone、Deutsche Telekom 等，產品線橫跨品牌來電（INFORM）、品牌訊息（ENRICH）、號碼監控（AFFIRM）、來電封鎖（SENTRY）與風險偵測（PROTECT+）。

隨著業務從企業客戶擴展到中小企業（SMB）市場，First Orion 把原本的單體式 Web 入口，改造成去中心化、按產品線劃分、以 cell 為單位的模組化架構，讓各團隊能各自加速開發。但這也讓 Web 應用程式數量暴增，加上 SMB 客戶使用的裝置與瀏覽器組合更加多元，UI 測試需要覆蓋的排列組合急遽膨脹。

First Orion 的 QA 團隊點出三個具體卡點：第一，回歸測試無法自助執行，既有測試案例背負大量相依關係，開發者難以在部署前針對自己改動的路徑隨選跑測試；第二，新功能存在「測試案例真空期」，QA 自動化工程師必須等功能部署到測試環境、拿到 DOM 中的 selector 與 label 後才能寫測試，導致工程師頻繁被迫中斷手邊工作等待；第三，測試腳本本身很脆弱，Selenium 與 Playwright 腳本仰賴的 element ID、class 等 DOM／JavaScript 屬性,變動速度比工程師修復的速度還快。單純擴編 QA 團隊只能緩解表面症狀，無法解決根本問題。

🧩 **用自然語言描述「要測什麼」，而非「怎麼測」**

First Orion 在 2025 年 3 月由 AWS 客戶團隊引介下成為 Amazon Nova Act 的 pre-release 採用者，並在正式發布前就看到成效。他們把核心需求收斂成兩個問題：容易隨 UI 變動而失效的 selector-based 測試，以及撰寫新測試案例耗費的時間。Nova Act 讓 QA 分析師改用類似「登入入口網站，前往帳單頁面，並驗證發票總額」這樣的自然語言描述測試流程，agent 會自行理解目前的 UI 狀態、辨識元素並執行多步驟操作，而不需要工程師預先寫死明確的 element selector。開發者仍可以在 Nova Act 指令之間插入 Python 程式碼、斷言（assertion）、中斷點與平行化執行。

First Orion 圍繞 Nova Act SDK 建立了一套端到端系統：QA 分析師在一個 React 前端的 Test Case Authoring UI 中，用英文瀏覽、建立、編輯與驗證測試案例，搭配自訂的樣板引擎（templating engine）處理電話號碼、Email、企業名稱等動態變數，確保同一組測試集合每次執行都能產生獨特且真實的資料。測試集合以 JSON 格式存放在 Amazon S3 作為中央倉庫；當分析師觸發測試執行，運行在 Amazon ECS（搭配 AWS Fargate）上的 Python 應用程式「Nova Act Test Runner」會從 S3 取出測試案例，透過 Amazon Nova Act SDK 進行協調，並將實際的瀏覽器操作委派給 Amazon Bedrock AgentCore Browser 執行。

💡 **關鍵差異：Nova Act 看的是畫面，不是 DOM**

Selenium、Playwright 這類框架的核心痛點在於，QA 自動化工程師必須撰寫並持續維護明確的 element selector，一旦 UI 改版，這些 selector 就會大量失效。Nova Act 的做法是直接理解畫面上看到的東西——標籤、版面配置、上下文——所以像「點擊 Submit 按鈕」這樣的指令，不會因為底層 CSS class 改變而失效，模型能自行適應版面變化、處理動態內容、關閉彈出視窗，並在出錯時自行嘗試恢復。

🎯 **實務啟示**

對正在為 UI 回歸測試維護成本頭痛的團隊來說，First Orion 的案例提供一個具體的參考路徑：與其持續投入人力修補 selector，不如評估將測試案例的撰寫方式從「操作步驟程式碼」轉為「自然語言意圖描述」，把不穩定的 DOM 綁定交給能理解畫面語意的 agent 處理。若團隊已使用 AWS 生態系（S3、ECS/Fargate、Bedrock），這套架構也提供了一個可直接參考的整合範例。

🔗 **來源**
- 標題：First Orion accelerates QA automation using Amazon Nova Act
- 作者／機構：Avinash Ranganath（與 First Orion 的 Mark Himelfarb、Garrett Wilkerson 共同撰寫）
- 連結：https://aws.amazon.com/blogs/machine-learning/first-orion-accelerates-qa-automation-using-amazon-nova-act/

#AmazonNovaAct #QAAutomation #AIAgent #AWS #TestAutomation #BedrockAgentCore #Selenium #Playwright #DevOps #SoftwareTesting
