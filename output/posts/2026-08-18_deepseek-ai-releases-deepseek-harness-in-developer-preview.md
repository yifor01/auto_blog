---
title: 'DeepSeek AI Releases DeepSeek Harness in Developer Preview: An MIT-Licensed
  Agent Harness Where Everything is a Plugin'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/17/deepseek-ai-releases-deepseek-harness-in-developer-preview/
model: claude-code/sonnet
generated_at: '2026-08-18T06:32:47.082998'
score: 86
---

📌 DeepSeek 開源 agent harness，連 agent loop 本身都是外掛

TL;DR：DeepSeek Harness 以「一切皆插件」為原則，把模型、工具、session、沙箱全部做成可替換組件，MIT 授權開發者預覽版已上線。

多數 agent harness 把 agent loop、工具註冊表、session 儲存這些核心層硬編碼死，擴充只能透過作者預留的少數 hook 進行。DeepSeek 這次發佈的 Harness 走的是完全相反的路線：README 第一行就寫明「everything is a plugin」，模型、工具、技能、session、沙箱、儲存、迴圈、排程、UI 全部架在插件邊界之上，任何一項都能在設定檔中替換或擴充，不需要動 Harness 本身的原始碼。這不是一個固定的程式碼助手，而是一套組裝 agent runtime 的工具箱——也是這次發佈比它同時附帶的模型公告更值得關注的原因。

🤔 **Agent = Model + Harness**

DeepSeek 將 harness 定義為模型與其行動環境之間的那一層：工具、檔案、沙箱，以及讓 agent 得以持續工作的控制迴圈。Harness 以 dsh 的形式發佈於 deepseek-ai/deepseek-harness，原始碼完整開源，採用 MIT 授權。v0.1 目前是開發者預覽版，定位是開發基礎設施而非生產環境的 agent 產品。

🧩 **底層跑在 Cordis 這個「元框架」上**

Harness 運行於 Cordis 之上，這是一個設計理念發表於論文《A Programming Paradigm for Spatiotemporal Composability》的元框架。Cordis 的 kernel 只負責插件的掛載、卸載與依賴關係管理，實際能力全部存在於插件裡而非特權核心中，插件之間透過 Cordis 提供的服務與事件機制互相協作。這個設計讓開發者能在設定層面選擇、替換或擴充任何一項能力，而不必碰 Harness 的原始碼。

Harness 內建三種預設模式：Standard 是完整的程式碼 agent，涵蓋檔案編輯、shell、檔案與網頁搜尋、技能、規劃、目標設定、子 agent 與工作流程，其中 Code mode 透過 Code Mode SDK 把這些工具暴露成介面，讓模型能用一段 TypeScript 程式把多步驟操作串在一起執行；Minimal 只保留 persistent bash 與 str_replace_editor 兩項工具，用於在最精簡環境下對模型做 benchmark；Creator mode 則額外提供 runtime 檢查、記憶體內插件實驗，以及 preset 撰寫指引。

📊 **每一次上下文注入都被記錄下來**

模型所看到的一切，包括系統提示、推理過程、工具呼叫與結果、子 agent 排程,以及每一次上下文注入，都會被寫入一份僅供附加（append-only）的 session log，並可透過 Trajectory 視圖依來源檢視。多數 agent 框架只記錄工具呼叫，這裡把每一次上下文注入都完整記錄下來,是相對更嚴格的做法，同一份事件流上還支援 resume、fork、search 與 replay。

🧩 **模型接取與安裝**

在 Settings → Models 中輸入 DeepSeek API key，下一次請求即可生效，不需重啟伺服器。內建目錄支援用 API key 直接接入 Anthropic、OpenAI 等 provider；Bedrock、Vertex、Azure、Codex 則需要各自的原生憑證（如 AWS 憑證與區域、ADC 專案、api-version、OAuth）；自訂 provider 可接受任何 OpenAI 相容的 base URL 與協定。憑證僅寫入、儲存在 $DSH_HOME/.credentials.yaml，設定檔本身只保留憑證參照。安裝方式為 npx @deepseek-ai/dsh web 啟動 Web UI（預設服務於 http://127.0.0.1:3080），或從原始碼 checkout 後執行 git clone、pnpm install、pnpm run build、pnpm dsh web。另有 Python SDK deepseek-harness-sdk，需要 Python 3.10 以上，支援 Linux x64、Linux arm64 或 macOS 14+ arm64,其內建 runtime 不需要系統安裝 Node.js。

⚠️ **仍是開發者預覽版**

v0.1 明確定位為開發者預覽，README 與文件強調這是開發基礎設施而非可直接上生產的 agent 產品，採用前應預期 API 與插件介面仍可能變動。

🎯 **實務啟示**

如果你正在自建或評估 agent 框架，DeepSeek Harness 的插件化邊界設計（尤其是模型、沙箱、session 儲存都可替換）值得拿來對照自家架構是否把太多能力鎖死在核心層；它的 append-only session log 與完整上下文注入紀錄,也是做 agent 除錯與可觀測性時值得參考的落地方式。

🔗 **來源**
- 標題：DeepSeek AI Releases DeepSeek Harness in Developer Preview: An MIT-Licensed Agent Harness Where Everything is a Plugin
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/17/deepseek-ai-releases-deepseek-harness-in-developer-preview/

#DeepSeek #AgentHarness #OpenSource #MITLicense #Cordis #AIAgents #DeveloperTools #LLMOps #AgenticAI #PluginArchitecture
