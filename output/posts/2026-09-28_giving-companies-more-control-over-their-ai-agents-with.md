---
title: Giving companies more control over their AI agents, with NVIDIA
source: Claude Blog
url: https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia
model: claude-code/sonnet
generated_at: '2026-09-28T22:38:17.630563'
pinned: true
---

📌 【Anthropic × NVIDIA】給企業 AI Agent 上鎖：憑證進金庫，行為進沙盒

TL;DR：Anthropic 與 NVIDIA 聯手推出分層防護架構，讓企業能實際掌控、稽核並限制 AI agent 的行動範圍。

當你的 AI agent 不只是回答問題，而是能讀寫資料庫、呼叫內部 API、代表使用者採取行動時，一個問題會立刻浮現：誰在檢查它做了什麼，又是誰擋住它不該做的事？Anthropic 這次的答案是「把防護拆成好幾層，每一層都能獨立擋下問題」。

🤔 **Agent 權限越大，公司越需要能查、能擋的機制**

隨著模型能力提升，企業開始把 agent 部署到跨部門的複雜工作中，讓它們存取專屬資料並代表使用者做決策。素材中直言，agent 找到的用途越多、拿到的存取權限越大，公司就越需要控管與檢查它的行為。這正是 NVIDIA 今日發表 Open Agent Safety Platform（開放式 Agent 安全平臺）的背景，Anthropic 與 NVIDIA 合作，把額外的安全與控制層加進 agent 技術堆疊。

🧩 **三層防護：模型內建、Managed Agents 管憑證、OpenShell 管行動**

素材描述的防護是分層設計，每一層各自獨立生效，不依賴單一層就能撐住整體安全：

- **模型內部的安全機制**：最底層，來自模型本身的安全設計。
- **Claude Managed Agents**：一組可組合的 API，用來大規模建置與部署正式環境等級的 agent。它的 agent 迴圈跑在與沙盒（sandbox，也就是實際執行工作的隔離環境）分開的伺服器上，而密碼、存取金鑰等憑證則存放在獨立的金庫（vault）中，agent 本身完全看不到憑證。Managed Agents 也提供稽核軌跡（audit trail），記錄每個 agent 做過什麼，並能整合企業既有的存取控管系統。企業可以自行帶入沙盒環境，決定運作地點與方式。
- **NVIDIA OpenShell**：一套開源的安全執行環境（secure runtime），負責治理與監控所有 AI agent 的行為，並對每個動作執行政策。它的邏輯是「預設全擋，除非規則允許」，會檢查 agent 嘗試使用的每個工具，並對檔案、網路連線與資料存取套用規則。這些規則在 agent 之外強制執行，OpenShell 會記錄每一個允許或阻擋的決策。團隊可以先從最小權限開始，檢視日誌後,再搭配 Claude 逐步收緊規則，朝任務所需的最小存取權限調整。OpenShell 的 policy prover（政策證明器）則用數學證明的方式，確認在團隊撰寫的規則下 agent 究竟能碰到什麼。

💡 **Managed Agents 的產品輪廓**

根據素材，Claude Managed Agents 目前包含：具備安全沙盒、身份驗證與工具執行的正式環境等級 agent；可自主運作數小時、即使斷線也能保留進度與輸出的長時間 session；能自行衍生並指揮其他 agent 以平行處理複雜工作的多 agent 協作；以及具備範圍化權限、身份管理與執行追蹤的可信治理機制。

素材也提到幾個使用案例：Notion 讓團隊在工作區內把任務交給 Claude，工程師用它出程式碼，其他員工則用來產出網站與簡報，可同時平行執行數十個任務；Rakuten 在工程、產品、業務、行銷、財務等部門跑專屬 agent，每個都在一週內完成部署；Asana 則打造了 AI Teammates，讓 agent 與人一起在專案中承接任務、草擬交付物，並藉由 Managed Agents 更快加入進階功能。

⚠️ **模組化不等於零門檻**

素材強調這些防護層是模組化設計，企業可以依自身架構選擇要採用哪些層，這代表落地時仍需要團隊自行評估要接入哪些元件、如何設定沙盒與規則，而非開箱即用的單一方案。

🎯 **實務啟示**

對正在把 agent 推向正式環境的工程團隊來說，這套架構提供了一個可參考的分工方式：憑證管理與執行環境隔離交給 Managed Agents 這類平臺層，行為層級的白名單與稽核則交給 OpenShell 這種獨立於 agent 之外的執行環境。與其等 agent 出事才補救，不如從「預設全擋、逐步放行」的最小權限模型開始設計，並保留完整的稽核軌跡以便事後追查。

🔗 **來源**
- 標題：Giving companies more control over their AI agents, with NVIDIA
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/giving-companies-more-control-over-their-ai-agents-with-nvidia

#Anthropic #Claude #NVIDIA #AIAgents #AgentSecurity #OpenShell #ManagedAgents #EnterpriseAI #AIGovernance #OpenSource
