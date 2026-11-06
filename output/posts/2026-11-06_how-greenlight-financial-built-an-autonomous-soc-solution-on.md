---
title: How Greenlight Financial built an autonomous SOC solution on Amazon Bedrock
  AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-greenlight-financial-built-an-autonomous-soc-solution-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-06T22:24:40.641551'
score: 87
---

📌 Greenlight Financial 打造自主 SOC：AgentCore 上的多層代理

TL;DR：金融科技公司用多代理系統自動處理九成以上安全案件。

每月收到 3,000 到 4,000 件安全與風險警示,若每件都要人工分析師花 15 到 30 分鐘處理,這個數字很快就會壓垮整個團隊。這正是為家庭提供金融服務的 Greenlight Financial 遇到的現實,而他們的解法是建立一個名為 Luna 的自主安全維運中心（SOC）系統。

🤔 一張警示背後,藏著好幾個資料來源要核對

Greenlight 提供 debit card（簽帳金融卡）、儲蓄工具,以及 Family Hub、Pet Tracker 等連網裝置,處理的金融資料規模與一般銀行受同等監管要求。SOC 每月收到來自四個主要來源的 3,000 至 4,000 件警示,包括暗網出現的被盜刷卡資訊、身分異常、金融風險事件等。每一件警示都需要分析師跨多個系統查核：確認卡片是否仍啟用、比對是否已有過往通報紀錄、檢視客戶 session 資料、查詢是否已有客服工單在處理。單一流程耗時 15 到 30 分鐘,乘上每月案件量,人力根本無法打平。

🧩 仿照真實 SOC 的兩層主管架構

Greenlight 在 Amazon Bedrock AgentCore 上打造 Luna,採用分層 supervisor 架構,模擬真實 SOC 團隊 L1 處理量、L2 處理複雜案件的分工方式。

Tier 1 supervisor 跑在 AgentCore runtime（位於 Amazon VPC 私有子網路,透過 ZIP 檔與 Amazon S3 直接部署程式碼),負責初步分類,並協調超過 30 個專職代理。案件經由 Amazon API Gateway 暴露的 Luna Queue API、MCP 端點,或是 Tines SOAR 自動擷取警示進入系統。Tier 1 會依警示類型決定該呼叫哪些專職代理、整合各方發現並做出判定,常規案件的中位數分類時間僅個位數秒。

超過 Tier 1 信心門檻的案件（約 10%),會升級給使用具備延伸推理能力的進階基礎模型的 Tier 2 supervisor,處理需要多步推理的情境。Tier 2 透過 Amazon EventBridge 排程觸發與 Amazon SNS 佇列完成事件批次處理升級案件,緊急案件則可即時處理。

系統另外開放三個進入點,對應不同團隊的工作型態,從全自動警示擷取到互動式即時調查都涵蓋在內。

記憶層建立在 AgentCore memory 之上,是 Luna 與單純的無狀態分類工具的最大差異。短期的 episodic memory 會記住近期事件與處理結果,例如某個基礎架構帳號每週二凌晨 3 點固定排程維護觸發的存取模式,Luna 第一次處理後就學會將其自動列入允許清單,而不是每週都重新標記為異常。長期記憶則保存語意偏好與處理範本,超越 30 天窗口持續累積。

📊 自主解決率從 83% 升到超過 90%

一條專門的回饋管線會把每次案件的處理結果送回系統,持續優化判斷邏輯。這個學習迴路讓 Luna 的自主解決率從僅有 Tier 1 時的 83%,提升到結合 Tier 1、Tier 2 與持續學習後的超過 90%。

以案件量與人工處理時間估算,每月 4,000 件案件若每件耗時 15 到 30 分鐘,約需 1,000 到 2,000 個分析師工時。Greenlight 表示 Luna 自主解決九成以上案件,等於每月省下約 900 到 1,800 個小時的常規人工作業,分析師可以把精力集中在真正需要人類判斷的案件上。風險降低則來自速度（秒級反應縮短暴露窗口）與一致性（Luna 在週六凌晨 3 點與週二上午 10 點套用相同的判斷邏輯,不會疲勞、不會抄捷徑)。

Greenlight 在 SOC 上線兩個月內,就把 Luna 擴展到金融風險評估,做法是在既有架構上新增專職代理與一個風險領域 supervisor,而不是重新打造系統。例如當客戶卡片出現在暗網,Luna 可以在數秒內自動完成原本需要人工登入 Galileo、查 DynamoDB、開 Mixpanel、搜尋 Zendesk 才能完成的 15 到 30 分鐘流程。

💡 先把分類做對,再談自動化

Greenlight 的經驗帶出幾個對打造多代理系統的團隊有參考價值的心得。首先,從成功標準明確的安全分類案件起步（正確解決或升級),等到 83% 解決率證明模式可行後,再擴展到金融風險,只需增加新代理而非重建架構。其次,Tier 1/Tier 2 的分工直接對應既有 SOC 團隊的運作方式,讓安全團隊更容易建立信任,因為這套邏輯符合他們原本的升級直覺。第三,真正把解決率從 83% 推到 90% 以上的關鍵,是 episodic 與長期記憶層,每一次案件的處理都在為 Luna 累積制度性知識,這是新進分析師需要數月才能建立起來的經驗。

⚠️ 自主判斷,但不自主出手

在受監管產業中,Greenlight 將 Luna 定位為「分類與建議」,而非未經政策核准就自主執行修復動作。風險擴展也延續同樣原則:Luna 提供支持其建議的證據,實際的修復授權與執行仍由人工分析師或經核准的自動化政策把關。這種人機協作的分工滿足了 Greenlight 的合規要求,也是取得風險團隊信任的關鍵。

🎯 給正在評估多代理系統的工程團隊

如果要在高度監管領域導入自主代理系統,Luna 的經驗顯示切入點的選擇很重要:先挑選判定標準清晰的場景驗證模式,再逐步擴展領域;同時別忽略記憶層的投資,持續學習才是把解決率從「堪用」推向「生產級」的關鍵,而不是單純堆疊更多代理。

🔗 來源
- 標題：How Greenlight Financial built an autonomous SOC solution on Amazon Bedrock AgentCore
- 作者／機構：Adam Maksimuk
- 連結：https://aws.amazon.com/blogs/machine-learning/how-greenlight-financial-built-an-autonomous-soc-solution-on-amazon-bedrock-agentcore/

#AmazonBedrock #AgentCore #AIAgents #SOC #CyberSecurity #MultiAgentSystems #FinTech #AWS #AIOps #SecurityAutomation
