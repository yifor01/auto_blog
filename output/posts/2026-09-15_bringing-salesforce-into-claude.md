---
title: Bringing Salesforce into Claude
source: Claude Blog
url: https://claude.com/blog/salesforce-in-claude
model: claude-code/sonnet
generated_at: '2026-09-15T20:25:11.701717'
pinned: true
---

📌 【Anthropic × Salesforce】業務員的 CRM 資料，現在直接搬進 Claude 對話框

TL;DR：Salesforce in Claude 外掛內建 37 個 skill，讓業務員在 Claude 裡就能讀寫 CRM 資料。

業務員的一天常常在 Salesforce、Email、通話記錄、Slack 之間來回切換，光是把客戶資訊拼湊完整就耗掉大半天。Anthropic 這次和 Salesforce 聯手推出的外掛，試圖把這段行政工作直接搬進 Claude 裡完成。

🤔 **會議前後的整理工作，佔掉業務員多少時間**

Anthropic 指出，業務員經常花上數小時做會議準備或會後追蹤，原因是資訊分散在 Salesforce、Email、通話錄音和 Slack 裡，得手動彙整。新外掛的定位，就是讓 Claude 接手這些行政工作，並在業務員核准後更新回 Salesforce。

🧩 **37 個 skill，建立在既有 Salesforce 權限之上**

Salesforce in Claude 目前以 beta 版本釋出，涵蓋帳戶研究、通話準備、業績（pipeline）檢視、CRM 更新等日常工作。外掛提供兩個連接器：Salesforce 連接器讓 Claude 能讀取資料並執行動作，例如彙整帳戶歷史、更新商機、記錄通話或建立追蹤任務；Slack 連接器則涵蓋交易頻道摘要與帳戶團隊討論串的讀寫。業務員第一次使用時，一個設定 skill 會辨識其工具與連接器，並依角色與客戶名單建立一份客製化的 Claude Artifact。權限設計上，Salesforce 仍是系統紀錄的權威來源，業務員以自己的 Salesforce 帳號登入，Claude 只能讀取權限允許的範圍；預設情況下，Claude 在寫入任何變更前都會先請業務員核准。Anthropic 也提到，在 Team 與 Enterprise 方案下，預設不會用客戶資料訓練模型。

📊 **從每日簡報到業績儀表板**

外掛支援的使用情境包括：每天早上自動產出一份簡報，內容涵蓋當天會議、即將成交的交易、有風險的商機、未回覆的訊息串，業務員可以直接在簡報裡請 Claude 更新成交日期或階段；通話前請 Claude 彙整 Salesforce、Slack、Email 中的相關資訊，若發現討論串裡有還沒建檔的關鍵聯絡人，會自動加入帳戶聯絡人；針對特定商機，Claude 可依團隊的銷售方法論評分，並草擬商業論證與雙方共同的成交計畫；會議結束後，Claude 能把逐字稿或筆記轉成追蹤郵件、Slack 摘要與商機欄位更新草稿；業務員也能請 Claude 建立互動式業績儀表板，並草擬符合主管期待格式的預測報告。

Anthropic 提到 GitLab、Siemens、Legora 已將此外掛部署到組織中，目前有 7,000 名 Salesforce 業務員在使用。Legora 財務長 David Eckstein 表示外掛讓業務員能在數秒內把即時資料轉成會議簡報；Salesforce 總裁暨營收長 Alexa Vignone 則提到，業務員一早上工時業績檢視與帳戶歷史就已備妥，省下的時間能直接投入客戶對話。

🎯 **實務啟示**

Salesforce in Claude 目前為 beta，開放於所有付費 Claude 方案，Salesforce MCP 已可透過 marketplace 直接安裝，管理員可透過 AgentExchange 申請安裝外掛，並為整個組織連接一次 Salesforce。對工程團隊而言，這類「讀寫現有系統權限 + 動作前人工核准」的設計模式，值得作為評估其他企業系統 AI 整合時的安全基準。

🔗 **來源**
- 標題：Bringing Salesforce into Claude
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/salesforce-in-claude

#Anthropic #Claude #Salesforce #CRM #EnterpriseAI #SalesTech #AIAgents #MCP #B2BSaaS #Automation
