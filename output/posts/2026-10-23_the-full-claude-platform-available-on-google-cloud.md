---
title: The full Claude Platform, available on Google Cloud
source: Claude Blog
url: https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed
model: claude-code/sonnet
generated_at: '2026-10-23T20:48:18.572053'
score: 77
---

📌 【Anthropic】Claude Platform 全功能登陸 Google Cloud,帳單直接記進既有額度

TL;DR：企業用既有 Google Cloud IAM 與帳單,當天就能用上 Claude 平臺全功能與新模型。

企業導入新的 LLM 功能,卡關的往往不是技術能力,而是流程:IAM 權限要重新申請、帳單要另開合約、合規審查要重跑一輪。Anthropic 這次把這些摩擦直接搬進 Google Cloud 既有的管理體系裡解決。

🤔 **兩條路線,一個決定**

Claude Models on Google Cloud 原本就有「Google managed」版本,由 Google 擔任資料處理者;現在新增的「Anthropic managed」版本正式全面上線(GA),由 Anthropic 擔任資料處理者,目前提供美國與全球端點。差異不只是誰經手資料:Anthropic managed 版本可以沿用既有的 Google Cloud IAM 憑證,帳單統一併入 Google Cloud 發票,Claude 的用量還會直接從既有的 Google Cloud 承諾額度中扣抵。

🧩 **搬過來的是完整功能清單**

Anthropic managed 版本的重點是「新功能、beta 功能跟原生 Claude 平臺同一天上線」,目前涵蓋:
- 建置與部署 agent:Claude Managed Agents(beta)、程式碼執行、computer use(操作瀏覽器或桌面)、Agent Skills、Advisor strategy(beta,讓 agent 諮詢顧問模型)
- 連接系統與知識:Files API、Citations(基於來源文件回答)、網頁搜尋與網頁擷取、MCP connector(beta)
- 管理成本與效能:Prompt caching、批次處理(Batch processing)

客戶同時可以使用 Claude Console 管理 agent、監控用量與成本、設定工作區的存取權限。目前可用模型包含 Claude Fable 5.1、Opus 5.5、Sonnet 5.5 與 Haiku 5.5,新模型上線時也會同步開放。

📊 **Fast Mode 同步跟進**

Opus 5.5 的 Fast Mode 在這個方案上也正式 GA,輸出 token 生成速度最高提升 2.5 倍,適合即時除錯與互動式 agent 等對輸出速度敏感的場景,輸入與輸出價格分別為每百萬 token 8 美元與 40 美元。

💡 **「當天同步」為何值得注意**

文章中引用的兩位客戶代表了這個方案想解決的實際痛點:一位 CTO 提到團隊本來就在用 IAM 架構幫企業建置 AI agent,新功能上線第一天就能用是關鍵考量;另一位 AI 工程負責人提到他們的電商 AI 工具「Moby」靠 Prompt caching 壓低成本運行,換到 Google Cloud 帳單與存取層之後仍保留了這個最佳化機制。這說明 Anthropic managed 想解決的不是能力落差,而是「雲端代管版本功能總是慢一步」的老問題。

⚠️ **不是所有情境都該換這條路**

如果企業需要 Google Cloud 作為資料處理者、有嚴格的區域資料residency 要求,或想串接 Model Armor、Agent Engine 等 Google Cloud 原生整合,Google managed 版本仍是更合適的選擇。另外文章也提醒,已有既有折扣的客戶要先聯繫 Anthropic 或 Google Cloud 業務代表確認折扣能正確套用,折扣不能回溯套用到已產生的用量。

🎯 **實務啟示**

已經在 Google Cloud 上有承諾額度、且重視第一時間拿到新功能的團隊,可以考慮直接切到 Anthropic managed;若資料駐留或原生整合是硬性要求,則維持 Google managed 版本更穩妥。

🔗 **來源**
- 標題：The full Claude Platform, available on Google Cloud
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/claude-models-on-google-cloud-anthropic-managed

#Claude #Anthropic #GoogleCloud #LLM #CloudAI #AIAgents #PromptCaching #EnterpriseAI #MCP #ClaudeAPI
