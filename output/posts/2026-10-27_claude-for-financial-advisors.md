---
title: Claude for Financial Advisors
source: Claude Blog
url: https://claude.com/resources/articles/claude-for-financial-advisors
model: claude-code/sonnet
generated_at: '2026-10-27T21:26:53.364702'
pinned: true
---

📌 Anthropic 讓 Claude 接管理財顧問的瑣事

TL;DR：Anthropic 發布理財顧問專用 connectors 與 skills，把會議之外的瑣事交給 Claude 處理。

根據 Kitces 的研究，一般理財顧問practice只有六分之一的時間真正花在與客戶見面上，剩下的時間都耗在不同系統之間來回搜集資料、準備與記錄會議內容。Anthropic 今日發布 Claude for Financial Advisors，試圖把這段被瑣事佔據的時間還給顧問。

🤔 顧問的時間都去哪了

文章引用 Kitces research 指出，一般顧問事務所只有六分之一的時間花在客戶會議中；而根據 EBRI 2026 Retirement Confidence Survey，超過四成的美國勞工表示不知道該找誰尋求可靠的理財或退休規劃建議。Anthropic 認為，顧問在準備與文書作業上省下的時間，可以轄移到現有客戶身上，或是用來服務目前還沒有餘力接待的新客戶。

🧩 Connectors：把顧問常用的系統一次接進 Claude

Claude for Financial Advisors 新增了一批連接顧問常用 CRM、custodian、投資組合報告、財務規劃軟體、遺產規劃工具與會議記錄系統的 connectors，包括 Addepar、BlackRock（透過 Advisor Center）、CAIS、Charles Schwab（Schwab Advisor Services 的餘額、持倉、交易與資金異動狀態）、Conquest Planning（Strategic Advice Manager 規劃引擎）、Envestnet（Tamarac 帳戶摘要搭配 MoneyGuide 的財務規劃快照）、FactSet、FINNY、Flourish、Franklin Templeton、iCapital（另類投資的 NAV、承諾資本與績效）、Invesco、J.P. Morgan Asset Management 的 55ip（評估稅務轉換影響）、Jump、MSCI、Nevis、Orion、SS&C Black Diamond、Wealthbox、Wealth.com（整合遺產與稅務資訊）、Vanguard，以及會議助理 Zocks。這些與既有的 Microsoft 365、Salesforce、DocuSign、Box、S&P Global、Morningstar 等 connector 並存。

其中 Claude for Financial Advisors 外掛（plugin）把常用的 skill 與 connector 打包成單一安裝，目前支援 BlackRock、Charles Schwab、Addepar、Envestnet、iCapital、Orion、Wealthbox、Wealth.com 與 Zocks，顧問可在導入流程中自行選擇要連接哪些。部分合作夥伴另外推出自己的外掛，例如 BlackRock 針對 Advisor Center 推出的新外掛，加入原本就有的 S&P Global 與 LSEG 外掛。

🧩 Skills：圍繞顧問一天的五個情境

Claude for Financial Advisors 外掛內的每個 skill 都對應顧問一天中的特定時刻，並會串接事務所既有的工具：

- Advisor onboarding：串接事務所的工具並自動執行第一次會議準備，讓新顧問第一天就能上手，而不是等到第三週。
- Alternative investments brief：從 iCapital 或 Addepar 拉出一個家戶的另類投資，整理成會議可直接使用的摘要，取代顧問手動對照各家對帳單。
- Compliance and AI policy：依使用者設定的標準，標示出可能需要額外合規複核的內容，協助事務所記錄複核流程與 AI 治理文件。
- Estate and tax brief：核對客戶的遺產規劃與實際帳戶的登記名義、受益人是否一致，並回顧前一年度的稅務狀況，必要時在 CRM 中建立後續追蹤任務，讓不一致之處浮現供顧問檢視。
- Portfolio rebalance review：比對客戶的目標配置，標示出偏移與過度集中的持倉，並產出顧問原本需要從零開始寫的草稿說明。

文章指出，事務所可以直接採用 Claude for Financial Advisors skill repository 中的這些 skill，也可以依自己的服務模式與風格調整。

🎯 實務啟示

這次發布展示了一種企業級的「plugin ＋ skill」組合模式：connector 負責把分散在不同系統的資料統一進來，skill 則針對具體工作情境把資料轉化成可用的產出，而最終判斷與風格仍交還給使用者（顧問）本人。對於正在設計垂直領域 AI 應用的工程團隊，這是一個值得參考的分層架構案例。

🔗 來源
- 標題：Claude for Financial Advisors
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/claude-for-financial-advisors

#Anthropic #Claude #FinancialAdvisors #WealthTech #Fintech #AIConnectors #ClaudeSkills #FinancialPlanning #EnterpriseAI #LLM
