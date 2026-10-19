---
title: 'The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the
  Router Less to Do'
source: Meta AI Research
url: https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/
model: claude-code/sonnet
generated_at: '2026-10-19T21:38:29.312830'
score: 112
---

📌 【Meta 工程團隊】把 Orchestrator 變笨之後，Agent 系統反而更可靠

TL;DR：用一個只會派工、不做決策的「薄路由」取代全知 Agent，資料欄位上架從數天縮到一小時內。

一個 Agent 什麼都懂，聽起來應該是最強的設計。Meta 工程團隊一開始也是這麼想的：打造一個裝滿所有領域知識的超級 Agent，demo 時表現完美，上線後卻開始胡言亂語。問題不是 prompt 寫得不夠好，也不是 context window 不夠大，而是給了中央 Agent 太多事情做。

🤔 **當 Agent 知道的太多，反而開始出錯**

Meta 的推薦系統資料欄位上架流程橫跨三個程式碼儲存庫、三種程式語言，一個欄位要經過最多六個 pipeline 階段才能完成同步。整套系統是 config-as-code 架構：Python 設定驅動 C++ 程式碼生成，再餵給資料處理服務，最終灌入分析系統。

第一版方案是一個裝載全部領域知識的單一 Agent：設定檔 schema、程式碼生成規則、pipeline 路由邏輯、驗證需求,以及超過 10 種資料來源的填入模式,全部塞進去。結果過了某個 context 門檻後,知識量不增反減—Agent 會把不同子系統的概念混在一起，例如把一個子系統的欄位命名慣例套用到另一個子系統,或是把專屬某個資料來源的程式碼生成模式誤用到別的來源上。

團隊也評估過另一種單 Agent 做法：靠工程師針對每個任務手刻客製化 system prompt,成功率可以到 70-80%；但若少了這種手把手調校,成功率會掉到只剩 10-20%。這證明問題不在 prompt engineering,而是架構設計本身出了錯。

🧩 **拆成兩層：路由只負責排序,領域決策全部下放**

團隊因此提出「薄路由（Thin Orchestrator）」模式：中央 Orchestrator 只負責流程排序與可靠性檢查,所有領域判斷都交給專門的子 Agent。整套系統目前用一支 1,300 行的 Orchestrator,把 20 多種工作流程路由給 14 個專職子 Agent,而且 Orchestrator 本身完全不做任何領域工作。

Orchestrator 遵循固定的 7 步協定,其中步驟 1-5 與 7 都是確定性（deterministic）邏輯,只有步驟 6 涉及 LLM 推理,而且是在一個只載入該領域知識的獨立子 Agent 中執行。Orchestrator 透過「工作流程範本」定義階段順序,這些範本是確定性狀態機,用來限制 LLM 的決策空間;每個範本都重複使用同一批 14 個子 Agent,只是排列順序不同。

當團隊需要支援 pipeline migration 這個全新使用情境時,並沒有另外開發新 Agent,只是寫了一個新的工作流程範本,把既有子 Agent 重新排序—零新增 Agent 程式碼,就達成完整的生產能力。每個子 Agent 都遵循同樣的標準結構,新增第 15 個子 Agent 和第一個在結構上完全相同,等於是模板化工作而非從零開發。知識檔案則是在子 Agent 執行時才動態載入,而不是寫死在 Orchestrator 裡;團隊目前維護超過 25 個依工作流程領域分類的知識檔案,更新後下一次執行就自動套用最新版本,不需要改動 Orchestrator。

📊 **欄位上架：從三四天到不到一小時**

一個新資料欄位的設定準備工作,人工手動需要三到四天,早期的 config 驅動系統可以壓到約一天,而薄路由系統則能在一小時內完成。團隊也提到,系統產出的變更中約有三分之二可以直接落地,不需要人工大幅修改。

文中也引用了 Mount Sinai 的 Windreich Department of Artificial Intelligence and Human Health 一份 preprint 作為旁證：在 80 個任務的批次測試中,多 Agent 協同架構維持 65.3% 準確率,而單一 Agent 掉到 16.6%,同時 token 用量最多可減少 65 倍,作者將此歸因於任務隔離避免了 context 互相干擾。

💡 **薄路由為什麼更可靠**

重量級 Orchestrator 一旦產生幻覺,錯誤會往下游擴散—路由到錯的 Agent、抓錯欄位,或是跳過可靠性檢查。薄路由因為路由與檢查步驟不依賴 LLM 推理,而是走固定協定,幻覺空間被壓到最小;創造性的部分則被限制在下游各個隔離、領域明確的子 Agent 裡,就算出錯也不會擴散。

⚠️ **擴展方式與尚未解決的部分**

團隊表示目前正把這套架構擴展到更多資料欄位與新的 pipeline 領域,預期擴展方式是新增工作流程範本與知識檔案,而不是重建 Agent。另外也在探索讓系統從生產環境用量中持續改進,透過自動化回饋迴路找出失敗模式,並對子 Agent 知識提出改進建議,但所有變更仍需人工審核把關。

🎯 **給正在做生產級 Agent 系統的工程師**

這篇文章最值得帶走的洞見是：不要把所有脈絡都塞進一個「全知」中央 Agent。把路由與可靠性檢查做成確定性邏輯,把領域推理下放到結構統一、知識按需載入的專職子 Agent,系統擴展時只需要新增工作流程範本和知識檔案,而不必重新設計整個 Agent。

🔗 **來源**
- 標題：The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do
- 機構：Meta AI Research（Engineering at Meta）
- 連結：https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/

#AIAgents #MultiAgentSystems #LLMOps #AgentArchitecture #Meta #ProductionAI #Orchestrator #AIEngineering #DataPipeline #MachineLearning
