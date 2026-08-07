---
title: Run Claude Code sessions on your own compute
source: Claude Blog
url: https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
model: tencent/hy3:free
generated_at: '2026-08-07T07:22:52.887224'
pinned: true
---

📌 【Anthropic 公布】Claude Code 支援私有運算環境，讓 Agent 深入企業內部網路

TL;DR：Claude Code 推出公測版私有化部署，讓 AI Agent 能在企業內部基礎設施執行。

隨著 AI Agent 逐漸深入開發流程，安全性與網路存取權限成為企業導入的核心考量。Anthropic 正式宣布，現已開放公測「自託管環境（Self-hosted environments）」，讓 Claude Code 的執行運算能直接在企業自己的基礎設施上運行。

🤔 **為什麼企業需要將 Claude Code 部署在自己的基礎設施？**

根據 Anthropic 在預覽計畫中的觀察，企業選擇自託管主要基於三大需求：

- **網路存取權**：Session 直接在企業網路內執行，可以存取內部的服務、資料庫與 Registry，無需將這些資源暴露於公開網路。
- **高度客製化**：開發者可以在環境中預先安裝編譯器 (compilers)、SDK 以及內部的 CLI 工具，確保每個 Session 一啟動即可直接進行建置。
- **合規性與安全性**：原始碼 (source code) 與建置產出物 (build artifacts) 都能保留在企業可控的基礎設施中。

🧩 **架構設計：Runner 模式與隔離機制**

在自託管模式下，企業需要部署一系列的 Runner（長駐程序），當使用者從 Web、Mobile 或 Desktop 發起 Session 時，Runner 會接手並啟動對應的 Claude Code 程序。

Runner 提供兩種運作模式：
- **固定模式 (Fixed)**：維持固定數量的 Runner 運行，並將 Session 分配至其中。
- **按需模式 (On-demand)**：透過編排器 (orchestrator) 監控排隊的 Session，隨需求啟動 Runner 並在工作結束後停止，以實現容量隨需求變動。

⚠️ **資料流向：對話內容仍需傳送至 Anthropic**

需要特別注意的是，雖然程式碼與建置產出物留在本地，但**對話過程（包含 Prompt、回應以及工具執行結果）仍會傳送到 Anthropic 進行推理 (inference)**，且 Session 的對話紀錄會被儲存，以便使用者能從不同介面接續工作。

💡 **與 Remote Control 的差異**

這項功能與「遠端控制 (Remote Control)」不同：
- **Remote Control**：讓開發者能從手機或瀏覽器接續在「自己電腦上」執行的 Session，Session 會隨電腦關機而結束。
- **Self-hosted environments**：由平臺團隊營運的共享基礎設施，任何使用者皆可使用。

🎯 **實務啟示：準備好工程人力進行維護**

對於 Claude Team 與 Enterprise 計畫的組織，此功能目前處於公測階段（預設為關閉狀態）。由於需要負責建立與維護 Runner 映像檔 (runner image)、更新 Runner 以及運行編排器，建議企業應指派專門的平臺 (Platform) 或開發者體驗 (DevEx) 團隊來負責設定與持續維護。

🔗 **來源**
- 標題：Run Claude Code sessions on your own compute
- 機構／作者：Anthropic
- 連結：https://claude.com/blog/run-claude-code-sessions-on-your-own-compute

#Anthropic #ClaudeCode #AIAgent #SelfHosted #DevOps #SoftwareEngineering #EnterpriseAI #LLM #DeveloperTools #Infrastructure
