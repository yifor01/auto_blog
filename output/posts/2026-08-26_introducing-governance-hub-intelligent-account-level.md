---
title: 'Introducing Governance Hub: Intelligent, account-level governance over your
  Databricks estate'
source: Databricks
url: https://www.databricks.com/blog/introducing-governance-hub-intelligent-account-level-governance-over-your-databricks-estate
model: claude-code/sonnet
generated_at: '2026-08-26T06:32:28.325582'
score: 62
---

📌 Databricks 推出 Governance Hub，把治理、AI 用量與成本收進同一個帳戶級視角

TL;DR：Databricks 新推的帳戶級治理平臺 Governance Hub 進入 Beta，讓分散在系統表與各工作區的資料治理、AI 用量與成本資訊集中可查。

當一個企業橫跨數百個 workspace、分佈在多個地區時，「哪些資料表缺少標籤？哪個使用者正在推高 AI 成本？」這類問題往往要靠工程師手動拼湊多個系統表和第三方工具才能回答。

🤔 **治理團隊看不到全貌的老問題**

Databricks 表示，這是他們反覆從客戶那裡聽到的痛點：FinOps 團隊需要下鑽支出來源卻不想維護幾十個查詢和儀表板；資料治理團隊自建的分類覆蓋率追蹤工具很快就過時；AI 部署團隊搞不清楚開發者到底在用哪些模型和 agent。負責跨數百個 workspace、多區域治理的團隊，經常拿不到需要的洞察，即便拿得到，資料也散落在系統表、workspace 層級視圖與第三方工具中。

🧩 **三大面板：資料、AI、成本**

Governance Hub 是一個橫跨 AWS、Azure、GCP 的帳戶級集中視圖，提供資料健康度、AI 用量與成本的洞察，並附上優先建議，目前已進入 Beta。

- **Data 頁面**：一眼看出資產總數、已標籤／已指定擁有者／已分類的比例，以及哪些資產進度落後。點進 asset inventory 可精確看到哪些資料表和 schema 缺少必要標籤或說明；點進 data quality 可找出不健康或缺乏文件的 metastore；還能在頁面內直接管理受治理標籤（governed tags），建立政策、編輯數值、授予權限。
- **Access Insights**：以「principal」為中心的視圖，選定任一使用者、群組或 service principal，即可看到其在整個帳戶中的所有存取權限，包括直接授權、透過群組成員身份繼承的權限，以及其擁有的物件，並可依 catalog 或 privilege 篩選。適用情境包括：偵錯使用者為何無法存取某表、在導入供應商前檢視某群組的權限、稽核 service principal 的存取範圍，或在員工離職前確認其擁有哪些物件。
- **AI 頁面**：透過 Unity AI Gateway 作為單一治理面板，統一管理 Databricks 託管與外部託管模型、agent、工具與 MCP 的用量、存取與成本，追蹤 token 消耗、模型活躍度、每位使用者的支出與 guardrail 覆蓋率，使用者超過額度門檻時會即時提示。
- **Cost 頁面**：顯示過去 30 天支出、當月至今支出與每日平均，並與前一期比較。其中一項關鍵洞察是「已標籤支出佔比」，點擊後會自動篩選出未標籤的資源，也就是那些對 chargeback 和預算流程而言「隱形」的支出。任何一個指標卡片都能開啟 Explorer，依產品、workspace、資源或標籤切分，兩次點擊就能從高層 KPI 下鑽到具體的 job、cluster、endpoint 或 warehouse。

💡 **用自然語言問治理問題**

Governance Hub 整合了 Genie，使用者可以直接問「為什麼成本突然飆升」或「哪些表存有敏感資料卻缺少遮罩政策」，不需要寫 SQL 就能得到基於實際治理資料的回答與建議。Genie 能理解 Data、AI、Cost 三個面板各自的情境，官方也預告未來 Genie 將能直接代為執行動作，例如設定政策、建立告警、落實建議。

啟用方式上，帳戶管理員可在 Account Console 的 Previews 頁面開啟 Governance Hub，帳戶管理員擁有完整存取權，workspace 管理員只能看到自己 workspace 的 Cost 與 AI 面板，metastore 管理員則只能看到自己 metastore 的 Data 面板；整個系統沿用既有權限體系，不需要另外設定新的存取控制。

⚠️ **仍在 Beta，功能持續補齊中**

目前 Governance Hub 仍是 Beta 階段，官方表示效能、安全性洞察、可委派的可執行建議，以及大規模治理的 agentic 能力等功能都還在規劃中，尚未全部到位。

🎯 **實務啟示**

對於管理多 workspace Databricks 環境的平臺或治理團隊而言，Governance Hub 的價值在於把原本要靠自寫查詢和拼接第三方工具才能拿到的治理視角，收斂成一個遵循既有權限體系的原生介面，特別是「已標籤支出佔比」和「principal 存取總覽」這兩項功能，直接對應資安稽核與成本歸因這兩個長期痛點。

🔗 **來源**
- 標題：Introducing Governance Hub: Intelligent, account-level governance over your Databricks estate
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/introducing-governance-hub-intelligent-account-level-governance-over-your-databricks-estate

#Databricks #DataGovernance #UnityCatalog #FinOps #AIGovernance #CloudCost #DataPlatform #Genie #AccessControl #EnterpriseAI
