---
title: Claude for Financial Advisors
source: Claude Blog
url: https://claude.com/blog/claude-for-financial-advisors
model: claude-code/sonnet
generated_at: '2026-09-14T21:03:18.658970'
pinned: true
---

📌 理財顧問只有六分之一時間在見客戶，Claude 想幫忙補回來

TL;DR：Claude for Financial Advisors 整合 Schwab、Addepar 等平臺連接器與客戶會議技能，讓顧問少花時間拼資料。

一項 Kitces 研究指出，典型的理財顧問業務中，只有六分之一的時間真正用在客戶會議上，其餘都耗在會議前後於各系統間拼湊資訊。與此同時，EBRI 2026 退休信心調查顯示，超過四成美國勞工不知道該找誰諮詢財務或退休規劃。Anthropic 今天推出的 Claude for Financial Advisors，就是想把顧問從這些系統拼接工作中解放出來。

🤔 **問題：時間都花在會議之外**

顧問省下的每一分鐘研究與文書時間，都能用來服務現有客戶或接下暫時沒有餘力照顧的新客戶。Claude for Financial Advisors 由「連接器」與「技能」兩部分組成：連接器讓 Claude 存取顧問依賴的 custodian、資產管理與財富科技平臺；技能則運用這些資料，協助會議準備、投資組合分析與合規檢查，最終決策仍交由顧問判斷。

🧩 **連接器：把顧問常用的系統都接進來**

新推出的連接器涵蓋顧問工作的主要環節：

- Addepar：跨公開與私募市場的投資組合資料、分析與工作流程
- BlackRock（透過 Advisor Center）：模型投資組合與機構級分析
- Charles Schwab（Schwab Advisor Services）：餘額、部位、交易紀錄、成本基礎、提醒與資金移動狀態
- Envestnet：以自然語言彙整 Tamarac 帳戶與家戶資訊，搭配 MoneyGuide 的財務規劃摘要
- iCapital：另類投資的 NAV、承諾資本、未動用資本與近期資本活動
- Orion：投資組合報告與 Redtail CRM 洞察
- SS&C Black Diamond：投組、績效、持股與再平衡資料
- Wealthbox：客戶紀錄與會議歷史
- Wealth.com：結構化的遺產與稅務資訊，包含信託、遺囑摘要與稅務申報洞察
- Vanguard：模型投資組合與投資解決方案資訊
- Zocks：會議中擷取的客戶輪廓、目標、生活事件與承諾事項

這些連接器與既有的 Microsoft 365、Salesforce、DocuSign、Box、FactSet、S&P Global、Morningstar 等並存。Claude for Financial Advisors 外掛把顧問技能與上述多數連接器打包在一起，顧問可在設定過程中自行選擇要連接哪些系統；BlackRock、S&P Global、LSEG 也各自提供獨立外掛。

📊 **技能：對應顧問一天中的具體時刻**

每個技能對應顧問工作流程中的特定環節，包括新顧問上任時自動完成首次會議準備的 Advisor onboarding、彙整另類投資的 Alternative investments brief、篩查合規疑慮的 Compliance and AI policy、比對遺產規劃與實際帳戶登記的 Estate and tax brief、標示投組偏移與集中部位的 Portfolio rebalance review、把逐字稿轉成摘要與追蹤事項的 Post-meeting notes and follow-up、彙整客戶資訊供會議前參考的 Pre-meeting prep，以及整理新客戶資料的 Prospect intake。這些技能可直接從官方 skill repository 採用，也能依各公司服務模式調整。

💡 **設計上刻意讓顧問掌握最終決定權**

Claude 準備的是簡報、摘要與草稿分析，CRM 更新或客戶溝通草稿等行政動作都會先暫存等待顧問核准。合規技能會依 SEC Marketing Rule 篩查對客戶溝通的用語，並協助公司在既有治理與紀錄流程中留存審查紀錄，還內建自助式 AI 政策工作流程，幫助公司依 SEC 規範記錄自身的 AI 使用情況。

⚠️ **投資建議與合規判斷仍須人工把關**

投資建議、客戶溝通、合規判定等受監管活動，都明確標註仍須經過人工審查與核准，Claude 的角色是準備與彙整，而非取代顧問的專業判斷。

🎯 **實務啟示**

對受高度監管的專業服務而言，AI 落地的可行路徑不是取代決策者，而是先把「找資料、拼資料、寫初稿」這類會議前後的重複工作自動化，把顧問的時間還給真正需要判斷力的客戶對話。

🔗 **來源**
- 標題：Claude for Financial Advisors
- 連結：https://claude.com/blog/claude-for-financial-advisors

#Anthropic #Claude #FinTech #FinancialAdvisors #WealthTech #AIAgents #Compliance #EnterpriseAI #PortfolioManagement #ProductLaunch
