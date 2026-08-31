---
title: 'OpenClaw Releases OpenClaw 2.0: Guided Model Setup, 575 ms Control UI Startup,
  and One Trust Boundary Per Gateway'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/30/openclaw-releases-openclaw-2-0-guided-model-setup-575-ms-control-ui-startup-and-one-trust-boundary-per-gateway/
model: claude-code/sonnet
generated_at: '2026-08-31T12:16:18.796202'
score: 23
---

📌 OpenClaw 2.0：575 毫秒啟動速度背後，劃清「非租戶隔離」的安全紅線

TL;DR：安裝流程重寫、Control UI 大幅提速，但官方明講這不是多租戶安全邊界。

在先前 230 天內發布了 106 次版本後，OpenClaw 團隊突然沉寂了近七週——這次沒有推小修小補，而是直接放出了 2.0 大版本，重寫安裝流程、重建瀏覽器端 Control UI，並把 session 與逐字稿全面搬進 SQLite。

🧩 **設定流程：先驗證，再儲存**

導引式設定（guided setup）現在會主動偵測機器上既有的 AI 存取權限：可以重用已驗證的 Codex、ChatGPT 或 Claude CLI 登入狀態、接受 API 金鑰、走供應商登入流程，或直接找出本機安裝的 Ollama 與 LM Studio 模型。系統會先證明「這個選擇真的能回應」，才會儲存該模型與憑證組合。全新 OpenAI 設定預設使用 GPT-5.6。在本機模型端，node-llama-cpp 被替換為受管理的 llama-server，Gemma 4 成為依 RAM 條件開啟的 llama.cpp 預設模型，llama.cpp 的預設 context 也拉高到 64K。

📊 **Control UI 重建：JavaScript 請求少了三分之二**

新版 Control UI 把對話放在畫面中心，檔案、審批（approvals）與即時工作面板則環繞在旁。官方在模擬測試中（mocked Gateway、50ms HTTP/1.1 延遲）記錄下的數據如下：

| 指標 | 舊版 | 2.0 |
|---|---|---|
| JavaScript 請求數 | 140 | 45 |
| 啟動時間 | 約 1.6 秒 | 575 毫秒 |

新增的 docked 面板包括：工作區檔案編輯器（不能新增或刪除檔案）、以 git 為基礎的 Changes 面板（唯讀，顯示 pull request 狀態與 CI 摘要）、具備元素檢視與截圖標註功能的瀏覽器面板，以及全螢幕網頁終端機。值得注意的是 Create PR 功能只會把動作交給 GitHub 處理，並不會在 OpenClaw 內部直接送出。審批請求會顯示在觸發它的對話串內，並保留 30 天的滾動歷史；新增的 /btw 指令則能開啟side conversation，避免臨時提問污染主對話紀錄。

⚠️ **資料遷移與共享 session 的限制要看清楚**

Session 與逐字稿現在存放在 SQLite 中，官方建議升級前務必做好驗證過的備份：若要回退到舊版檔案儲存的版本，目前的 CLI 必須先還原歸檔的舊版逐字稿；而遷移後新建立的 session 也不會出現在舊版本裡。

新推出的共享雲端 session 讓第二個人能加入即時工作、或在保留上下文的情況下接手，擁有者與管理員可以設定對方是唯讀、可建議修改、可在草稿中工作，或直接參與。但官方文件明確聲明：這些控制機制不是租戶隔離，也不是安全邊界，僅適合單一操作者或單一團隊的部署情境，不適用於多租戶產品。Incognito 模式預設關閉，其對話僅存在於程序記憶體中，但仍會把訊息送往模型供應商。Gateway 預設綁定在 loopback，多數聊天頻道遇到不明的私訊來源時會回覆配對碼；openclaw security audit 則會檢查對外存取、工具的影響半徑、網路暴露程度與外掛允許清單。

📊 **模型選擇是抵禦 prompt injection 的第一道防線**

OpenClaw 援引一項 2026 年的群眾外包競技場資料：272,000 次攻擊涵蓋 41 種 agent 情境，只有當 agent 同時「執行了有害行為」且「對使用者隱瞞」才計入成功：

| 模型 | 攻擊成功率 |
|---|---|
| Claude Opus 4.5 | 0.5% |
| Claude Sonnet 4.5 | 1.0% |
| Claude Haiku 4.5 | 1.3% |
| Gemini 2.5 Pro | 8.5% |

同一份資料也提醒：面對具備適應能力的人類攻擊者，成功率仍會超過 80%，因此工具政策、執行審批與沙箱化仍是真正硬性的防護層。

🎯 **實務啟示**

若你把 OpenClaw 用在單人或單團隊場景，2.0 的效能與體驗提升值得升級；但若考慮多租戶部署，官方已明講共享 session 機制不是安全邊界，仍需自行補上租戶隔離層。升級前務必先備份，避免 SQLite 遷移後無法平順回退。

🔗 **來源**
- 標題：OpenClaw Releases OpenClaw 2.0: Guided Model Setup, 575 ms Control UI Startup, and One Trust Boundary Per Gateway
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/08/30/openclaw-releases-openclaw-2-0-guided-model-setup-575-ms-control-ui-startup-and-one-trust-boundary-per-gateway/

#OpenClaw #AIAgent #LLMTooling #PromptInjection #AgentSecurity #DeveloperTools #SQLite #LocalLLM #AISecurity #AgenticAI
