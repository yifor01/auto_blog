---
title: 'Agents you can coach: how Asana builds human-agent teams with Claude'
source: Claude Blog
url: https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude
model: claude-code/sonnet
generated_at: '2026-09-29T21:34:28.581782'
pinned: true
---

📌 Asana 用 Claude 打造「可教練」的 AI 隊友

TL;DR：Asana 讓 Claude 驅動的 AI 代理人（agent）直接運作在既有的 Work Graph 上，用角色、權限與共享記憶把「人機協作」變成可管理的日常工作機制。

招募一個新同事，你會寫職位說明、劃定權限範圍、指定誰來帶他上手。Asana 把同一套邏輯原封不動搬到 AI agent 身上，讓「AI teammate」不只是行銷詞彙，而是真的在專案裡有角色、有任務、也有人負責訓練它。

🤔 為什麼選擇讓 agent 融入既有系統，而非另起爐灶

Asana 在導入 AI agent 之前，早已建立了 Work Graph® 模型，把每一項任務、專案、目標與對話都描繪成一張有明確擁有者、貢獻者與依賴關係的關係網。Asana 產品長 Arnab Bose 表示，當公司開始打造 AI agent 時，決定不為 AI 另外設計一套新的情境結構，而是讓 agent 直接在這個既有模型裡運作：有明確角色、能被指派任務、能讀寫訊息，也會出現在人類同事都看得到的活動動態中，只是額外加上了存取與分享上的安全機制。在 Asana 內部，Claude 是員工預設的 AI 工具，串接 Google Drive、Slack 與 Asana 本身；員工會先把腦中零散的想法、Slack 對話、會議紀錄或文件內容，跟 Claude 討論整理清楚，再把可執行的部分放進 Asana 的專案與任務結構，之後 agent 才會接手行動。

🧩 每個 agent 都有職位說明與權限邊界

Asana 的 agent 是圍繞角色或工作類型建立的，例如內容寫手、洞察分析師、專案經理、需求彙整專員、行銷活動分析師等，每個都根據 Asana 對客戶實際工作方式的研究，內建對應技能與所需整合工具（例如 HubSpot 或文件雲端硬碟）。每個 agent 也有自己的個人檔案頁面，列出名稱、用途、可使用者、管理員、指令、技能、整合工具與權限。Arnab 形容 Asana 是一個「受限的工作介面」：你可以選擇只授權特定專案而非全部、特定文件，或是文件與應用程式的組合。與人類使用者一樣，agent 受明確的存取控制約束，但多了一層保障：agent 的實際有效權限，會被觸發它的那個人的權限所限制，這讓 agent 可以擁有較廣的公開內容存取範圍，同時降低任何人取用它在私人情境中學到的資訊的風險。

💡 誰能「訓練」agent，誰只能「使用」它

Asana 的 AI teammate 有一項關鍵功能：共享記憶（shared memory），讓 agent 保留先前指令的內容，讓多位使用者能重複利用這份記憶更快完成任務。Arnab 說，AI teammate 可以像團隊裡的真人一樣被指導與訓練，但這裡有一項角色限制：任何人都可以針對某項任務給 agent 回饋，但只有管理員與編輯者能把回饋寫進永久記憶，或是撤銷、刪除記憶中的內容；對其他人來說，回饋只作用於當下這項任務。這個切分是刻意的，例如負責公司口吻與語氣的溝通團隊，會是內容寫作 agent 的編輯者與管理員，Arnab 自己可以跟這個 agent 一起草擬內容，但無法修改它的行為。Arnab 也提到，團隊裡大多數人根本不需要理解技能、行為、記憶這些概念，只要有一兩位專家把設定做對，其他人就能持續享受同樣的效益。

🎯 實務啟示

Asana 分享的做法可以整理成幾個可直接套用的步驟：先把零散的想法、Slack 對話或筆記帶給 Claude 討論，理清脈絡後再放進專案與任務結構；建立 agent 前先寫清楚它的角色、指令與負責的具體工作，就像替新人寫第一季目標一樣；明確劃分可存取的專案、文件與可執行的動作；為每個 agent 指定「使用者」與「管理員／編輯者」兩種不同角色，只有後者能真正改變 agent 的行為與記憶；此外，Asana 讓 agent 在任務中公開發布研究計畫與執行步驟，任何有權限查看該任務的人都能即時看到、留言並引導 agent 調整方向，例如 Arnab 曾在任務中 @ 提及一個他用過多次的 agent，簡短要求它納入舊有的談話要點，溝通團隊的同事也能同步看到請求與 agent 的回應，並直接介入調整。

🔗 來源
- 標題：Agents you can coach: how Asana builds human-agent teams with Claude
- 作者／機構：Anthropic（Claude Blog）
- 連結：https://claude.com/blog/agents-you-can-coach-how-asana-builds-human-agent-teams-with-claude

#Claude #Anthropic #Asana #AIAgents #HumanAgentTeams #WorkGraph #ProductivityTools #EnterpriseAI #AgenticAI #AIWorkflow
