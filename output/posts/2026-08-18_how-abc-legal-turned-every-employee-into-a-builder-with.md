---
title: How ABC Legal turned every employee into a builder with Claude Managed Agents
source: Claude Blog
url: https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents
model: claude-code/sonnet
generated_at: '2026-08-18T06:22:49.885627'
pinned: true
---

📌 【Anthropic 官方案例】法律科技公司靠 Claude Managed Agents，讓非工程師也能上線 50 個 Agent

TL;DR：ABC Legal 用 git-based 治理框架，讓 1,100 名員工人人都能建置生產級 AI agent。

當多數企業還在煩惱「AI 落地」該由誰主導時，美國法律文件送達公司 ABC Legal 的答案是：讓每個部門的人自己動手，而且不用寫一行程式碼。這篇 Anthropic 官方部落格記錄了 CTO Brandon Fuller 如何把一場自發性的 AI 熱潮，收斂成一支可版控、可觀測、隨時在線的 agent 艦隊。

🤔 **從「桌面排程」到「治理不了的影子 IT」**

ABC Legal 今年稍早為全公司 1,100 名員工導入 Claude Enterprise 後，效果立竿見影：服務送達、電子歸檔（eFiling）、出庭律師協調，乃至行銷、法遵、財務等團隊都自發開始用 connector 與 tools 自動化日常工作。但問題也隨之而來，早期的 agent 散落在各員工的個人電腦上，以排程任務形式運作。Fuller 想要的不只是熱情,而是一套統一部署結構、共享工作空間、單一稽核與計費介面的基礎設施,讓 agent 脫離個人筆電、在雲端常駐運作。他的解法是導入 Claude Managed Agents。

🧩 **把 Agent 當成程式碼來管理**

Fuller 的核心理念是：「一個 agent 本質上就是結構化文字,一段 prompt 加上設定,而任何文字都可以放進 repository,讓全公司都能看見、審查、改進它。」在這個框架下,agent 的 prompt、工具清單、排程、憑證與記憶體全部寫成設定檔,存放在與公司軟體同一個 git repository。任何變更都必須透過 pull request 並經人核准,這讓每個 agent 都有版本歷史、程式碼審查、回滾能力與稽核軌跡。

他花一週時間建立了一套包含兩種範本的 starter kit：事件驅動型（一有新工作或法院文件退回就觸發）與排程型（依小時、日、週定時執行）。每個 agent 各自一個資料夾,包含 JSON 設定檔、Markdown 格式的 system prompt、部署腳本與操作文件。把變更合併進 main branch 就會自動部署。建置者不需要寫軟體,只要 clone repository、複製範本、告訴 Claude Code 這個 agent 該做什麼,就能拿到完整的設定、prompt、憑證儲存與記憶體。

📊 **15 位非工程師,一週內全數做出可用的 Agent**

為了驗證非開發者也能自建生產級 agent,Fuller 找來公司 15 人的跨部門指導委員會（財務、行銷、營運、開發,但沒有一位是軟體工程師）,讓他們 clone repository 並用 Claude Code 建置 Managed Agents。因為他們填寫的是設定與 prompt,而不是撰寫程式,風險相對可控。Fuller 提到一個細節：「我得跟他們解釋什麼是 PR,很多人以為那是指開車開到最快。」一週內,15 人全數做出可運作的 agent；一個月內,全公司運行的 agent 數量達到 50 個以上。截至 2026 年 7 月,ABC Legal 已追蹤到 50 多個生產環境 agent、部分 agent 涵蓋的人工任務成本降低最多約 50%（尚未經過深度最佳化）,以及約 310 名員工每天使用 Claude 工作。

🧩 **法律文件流程幾乎每個環節都有 Agent 在跑**

素材列舉了多個實際案例：AI Code Reviewer（暱稱 Hank）會審查四個程式碼庫的所有 pull request,以多模型分析抓出安全漏洞、效能退化與誤提交的憑證,工程師現在會等它審完才合併。EvidenceChain™ Delivery Agent 接手了客戶經理原本每週手動執行的工作,從資料庫撈出符合條件的工作紀錄、用內建瀏覽器的 Managed Agent 取回每份 PDF,再每日送到客戶的 FTP 伺服器,這位客戶經理過去從未做過自動化,卻靠著跟 Claude Code 描述需求,大約一小時就建好它。eFiling Rejection Diagnoser 在法院退回文件的當下自動觸發,讀取工作細節、比對法院規則,約一分鐘內把診斷結果貼到 Slack。另外還有職務驗證 agent 透過瀏覽器查核法院網站上的開庭資訊、律師出庭協調 agent 負責聯繫律師確認檔期與報價、財務端的應收帳款核銷 agent、行銷端的 Google Ads 週報分析、營運端與法遵團隊判斷一致率約 98% 的審核 agent Charvis,以及處理逾期案件第一輪催辦訊息的 Service-Overdue-Nudger。

💡 **把 Slack 上的表情符號回饋,變成調校訊號**

這些 agent 都在人類監督下運作,把執行結果或建議貼到 Slack,員工在討論串回覆、用表情符號反應。Fuller 認為這些互動資料是被浪費掉的訓練訊號,不過素材也提到,並非每個 agent 都需要這類訊號,艦隊裡多數是單一任務的執行者,產出沒有人特別評分,獨立運作即可。

🎯 **實務啟示**

這個案例對工程團隊的啟發在於：把 agent 視為「prompt + 設定」這種結構化文字資產,配上 git 工作流（PR、code review、版本回滾）,就能把 AI 自動化的建置權下放給非工程背景的員工,同時保留稽核與治理能力。與其把每個自動化需求都塞進開發團隊的 backlog,不如投資一套標準化的 event-driven / scheduled 兩種範本與部署骨架,讓業務單位自己填空。

🔗 **來源**
- 標題：How ABC Legal turned every employee into a builder with Claude Managed Agents
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents

#Anthropic #ClaudeEnterprise #ManagedAgents #AIAgents #EnterpriseAI #LegalTech #Automation #ClaudeCode #GitOps #AIAdoption
