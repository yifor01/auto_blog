---
title: The enterprise guide to securing coding agents
source: Claude Blog
url: https://claude.com/resources/articles/enterprise-guide-to-securing-coding-agents
model: claude-code/sonnet
generated_at: '2026-11-24T03:34:11.878645'
score: 98
---

📌 【Anthropic】企業導入Coding Agent前，先問這六個安全問題

TL;DR：Anthropic發布企業安全指南，列出評估coding agent的六個關鍵問題與四大agent特有風險。

Salesforce在全組織標準化採用Claude Code後，回報每位工程師合併的PR數量多了79%，整體事故反而少了5%。agent做得越多、交付越快，隨之而來的問題是：護欄要怎麼跟上？

🤔 **Agent已經在寫code、開PR，有些甚至直接review與merge**

Anthropic指出，coding agent在不少領先企業裡已經不只是寫程式碼開PR，還負責review、測試，甚至merge。隨著agent承擔的工作越多，prompt injection、權限濫用等風險也必須靠checked permissions（檢查過的權限）與bounded environment（有邊界的執行環境）等多層控制來處理。這份指南分兩大部分：前段界定風險範圍（AI provider該符合哪些要求、四個agent特有風險），後段談如何圈住風險邊界（Claude Code提供的防禦層，以及如何集中管理與落實這些控制）。

Anthropic Deputy CISO Jason Clinton在指南中表示：「在agentic AI時代，CISO的職責不是追求零風險，而是讓agent的風險變得可被看見、可被限定範圍——這樣我們才能有意識地接受自己能管理的風險，讓業務按照我們的節奏推進，而不是被風險牽著走。」

🧩 **評估coding agent的六個問題**

| 該問的問題 | 好答案 | 弱答案 |
|---|---|---|
| 模型該拒絕時會不會拒絕？ | 拒絕能力訓練進權重，並公開拒絕率 | 「系統提示詞要求模型拒絕」 |
| 動作執行前，模型外部有沒有獨立檢查？ | 指令的靜態分析＋獨立評估模型，加上prompt injection測試 | 「這個模型能力很強」 |
| 環境有沒有限制agent的影響範圍？ | 可由管理員強制啟用、失效時預設關閉的核心層級沙箱，或每個session獨立的隔離VM，加上網路層的egress allowlist | 「我們指示agent不要離開工作目錄」 |
| 政策能不能集中鎖定？ | 由管理設定強制、本機使用者無法覆寫的硬性規則 | 「每個開發者各自的設定檔，加上榮譽制度」 |
| agent寫的程式碼安全嗎？ | 自動化安全review，高風險變更需人工核准 | 「模型被訓練寫安全的程式碼」 |
| 事件發生後能不能重建過程？ | Session telemetry匯出、Enterprise的稽核API，並列出已知限制 | 「日誌可依要求提供」 |

除此之外，指南建議把既有的SaaS供應商checklist（SSO、角色權限控管、資料處理條款、稽核日誌）套用到AI provider身上。以Claude Code為例，Anthropic列出的對應能力包括：Enterprise方案的SSO與角色權限控制；在商業條款下不會用客戶的程式碼或提示詞訓練模型（除非客戶主動選擇分享）；分階段推出的Enterprise Frontier Safeguards，結合零資料保留與針對高能力模型的濫用偵測；客戶可用自有金鑰加密、資料保存在客戶可控的儲存空間；Enterprise方案下Claude Code CLI與桌面版Code分頁（本機模式）在完成HIPAA設定後有BAA覆蓋；AWS KMS、Google Cloud CMEK、Azure Hosted等雲端平臺的加密選項；以及SOC 2 Type 2報告與ISO 27001認證。

🧩 **四個隨agent而變化的風險**

指南點出四類風險：洩漏憑證與權限濫用、未經審查的依賴與擴展、資料外洩、以及prompt injection（內部風險的延伸）。

- **憑證洩漏與權限濫用**：agent在Claude Code中預設以負責監督的開發者身分執行。一旦發生事故，需要能區分「哪些動作是agent做的、哪些是開發者做的」才能正確應對——例如在PR流程中，agent的工作會以自己的名義送出，方便追蹤。
- **未經審查的依賴與擴展**：agentic coding加快了程式碼產出速度，連帶也加快了依賴套件被加入的速度。MCP伺服器、plugin、skill、subagent定義，以及repository裡的CLAUDE.md檔案，都是一種「依賴」——不同於被動等待呼叫的被入侵函式庫，它們的描述與指令會在agent動手做任何事之前，就先進入context window。Enterprise方案提供skill與plugin scanning，在有人上傳或編輯第三方skill、plugin時檢查是否含有惡意內容。
- **資料外洩**：傳統上靠網路層的egress allowlist把關，但被入侵的agent可能透過原本就被允許的服務把資料送出去——而且不像傳統惡意軟體，它可以嘗試多條外洩路徑，不需要攻擊者事先定義好。

🎯 **實務啟示**

這六個問題可以直接拿來檢核組織現在或打算導入的coding agent供應商。特別值得注意的是幾個與傳統SaaS安全checklist不同的地方：agent預設沿用開發者身分執行，事故發生時很難單從一般日誌分辨是人還是agent做的；MCP、skill、plugin這類「依賴」在載入的當下、agent還沒開始工作前，指令就已經進入context window，審查節奏必須比對待一般套件更快。

🔗 **來源**
- 標題：The enterprise guide to securing coding agents
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/enterprise-guide-to-securing-coding-agents

#AIAgents #EnterpriseSecurity #ClaudeCode #Anthropic #PromptInjection #DevSecOps #AICompliance #SoftwareSupplyChain #CISO #AgenticAI
