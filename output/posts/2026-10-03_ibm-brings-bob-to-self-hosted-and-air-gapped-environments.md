---
title: 'IBM Brings Bob to Self-Hosted and Air-Gapped Environments: Agentic Software
  Development Without Moving Your Code'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/02/ibm-brings-bob-to-self-hosted-and-air-gapped-environments/
model: claude-code/sonnet
generated_at: '2026-10-03T19:59:54.589126'
score: 69
---

📌 IBM Bob 進駐氣隙網路,程式碼終於不必外送

TL;DR：IBM讓agentic coding平臺Bob支援地端與氣隙部署，但模型要企業自己帶。

對一家銀行的核心交易系統來說,「把程式碼丟到雲端給 AI 分析」本身就是不可承受的風險。IBM 這次更新,正是針對這類不能連外網的環境而來。

🤔 **企業想用 AI 寫程式,但程式碼不能離開機房**

IBM Bob 是 IBM 的 agentic 軟體開發平臺,涵蓋理解程式碼、規劃工作、執行變更、驗證結果的完整流程。這次 IBM 宣布自建(self-hosted)部署選項正式開放給企業客戶,讓 Bob 可以跑在地端機房、私有或主權雲,以及完全對外網隔離的氣隙網路中。

🧩 **模型要自己帶,架構決定資料去留**

值得注意的是,Bob 自建版本本身不內建模型,客戶需要從 IBM 支援的模型清單中自行選用、取得授權並自行架設。IBM 依部署方式將清單分組,這個選擇直接決定了程式碼與開發情境資料實際會被處理在哪裡。IBM 給出的例子是:一家銀行可以把核心銀行應用的推理放在地端執行,同時把限制較少的工作負載路由到經過核准的外部模型。無論哪種架構,開發者在前端看到的都是一致的 Bob 使用體驗,而平臺與安全團隊則在底層掌控整體架構。

⚠️ **定價未公開,多模型路由仍是路線圖**

目前 IBM 尚未公開這項自建方案的定價,有興趣的買家會被導向申請 demo。IBM 也表示計畫擴充模型陣容並加入多模型路由功能,但這部分目前仍屬路線圖,尚未實際出貨。

🎯 **實務啟示**

比較市場上幾類 agentic coding 工具的差異化策略,會發現切入點各不相同:GitLab、GitHub 是把代理整合進自家的 DevOps 平臺;Mistral 則是用自家開源權重模型搭配代理;而 IBM 這次明確瞄準的是 Java、IBM i、主機(mainframe)這類長壽命、無法連外網的既有系統現代化。對正在評估企業級 agentic coding 工具的團隊來說,先確認自己的合規與網路隔離需求,再對照這些廠商的定位差異,會比單看功能清單更有效率。

🔗 **來源**
- 標題：IBM Brings Bob to Self-Hosted and Air-Gapped Environments: Agentic Software Development Without Moving Your Code
- 作者／機構：Sana Hassan／MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/02/ibm-brings-bob-to-self-hosted-and-air-gapped-environments/

#IBM #IBMBob #AgenticAI #AirGapped #EnterpriseAI #SoftwareDevelopment #SelfHosted #DevOps #LegacyModernization #SovereignCloud
