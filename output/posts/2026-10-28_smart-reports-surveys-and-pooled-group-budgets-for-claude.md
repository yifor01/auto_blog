---
title: Smart reports, surveys, and pooled group budgets for Claude Enterprise
source: Claude Blog
url: https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets
model: claude-code/sonnet
generated_at: '2026-10-28T21:44:57.078213'
pinned: true
---

📌 【Anthropic 官方發布】Claude Enterprise 推出智慧報告、問卷與共享團隊預算

TL;DR：Claude Enterprise 正式開放 smart reports、in-app surveys 與 pooled group budgets 三項管理功能。

🎣 導入 AI 工具容易，難的是知道「團隊到底拿 AI 做了什麼、花了多少、又卡在哪裡」。Anthropic 這次針對的正是這個企業管理者普遍的盲點。

🧩 **Smart reports：把團隊的 Claude 使用情況變成可行動的報告**
Smart reports 會分析團隊的 transcript 樣本，將工作歸類成不同的 workstream，呈現每個 workstream 的花費、產出的成果，以及最常見的卡點，例如缺少的 connector 或失敗的 tool call。管理者可以選擇特定團隊、日期範圍與產品範圍產生報告，每份報告都附上一份整合建議清單，包括哪些重複性工作值得轉成 skill、哪些規則該加進程式碼庫。報告也能回答關於模型用量與成本的自訂問題，並將常用問題存成範本重複使用。若發現某人卡在支出額度上，具備帳務權限的管理者可以直接從報告中調高額度；擁有者也能授權非管理員的團隊負責人，為自己管理的團隊產生報告。素材特別註明，smart reports 的定位是協助了解採用情況與投資規劃，不適用於評估個人績效或作為人事決策依據。

🧩 **In-app surveys：直接在工作介面中收集團隊回饋**
In-app surveys 讓團隊成員在他們原本使用的工具中，於一次對話回覆後看到簡短問卷卡片。預設問題聚焦在「價值」：最近用 Claude 做過最有價值的事、Claude 改變了多少工作時間、該讓誰的用法被其他人效仿，以及如果明天失去 Claude 存取權，最先受影響的會是什麼。管理者可以自訂或移除問題，決定誰收到問卷、何時發送、出現在哪裡；回覆會即時顯示在問卷頁面，也能匯出成試算表。這項功能目前也開放給使用客戶自管加密金鑰（customer-managed encryption keys）的組織，若組織設定統一的資料保留期限，問卷與回覆也會依同一排程刪除；素材強調問卷內容被視為客戶自身資料，Anthropic 僅在維運服務所必要時才會存取。

🧩 **Pooled group budgets：讓預算流向真正在用的人**
Pooled group budgets 讓一個團隊共用一筆月度預算，避免重度使用者在月初就撞到個人額度上限，而其他成員的額度卻閒置未用。個人額度仍作為防止異常高用量的防護機制，每次請求會同時計入團隊與個人額度，哪個先用完就先卡住。當有人碰到額度上限，可以直接在 Claude 內申請加額，申請會送交管理者審核；系統會根據團隊近期用量建議合理額度，具帳務權限的管理者也會在額度使用達 50%、75%、95%、100% 時收到郵件通知。

💡 **三項功能合起來解決的是同一個問題**
從報告看見「團隊做了什麼」，從問卷聽見「團隊覺得有沒有用」，再用預算機制確保「資源分配到真正在用的地方」，三者形成一個從洞察到行動的管理迴圈，而非單純的用量監控儀表板。

⚠️ 素材提到功能可用性會因組織設定而異，例如採用 HIPAA 合規配置或客戶自管加密金鑰的組織，需另外確認相容性。

🎯 **實務啟示**
若貴團隊使用 Claude Enterprise，可以先用 smart reports 找出目前最常見的卡點（如缺 connector、tool call 失敗），作為下一步整合或寫 skill 的優先順序依據，再搭配 pooled budgets 減少「有人額度用完、有人額度閒置」的管理困擾。

🔗 **來源**
- 標題：Smart reports, surveys, and pooled group budgets for Claude Enterprise
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/smart-reports-surveys-pooled-budgets

#Claude #Anthropic #ClaudeEnterprise #EnterpriseAI #AIAdoption #AIManagement #LLMOps #TeamProductivity #AIGovernance #BudgetManagement
