---
title: "Cline Releases Cline SDK: An Open-Source Agent Runtime Now Powering Its CLI and Kanban, With IDE Extensions Being Migrated"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/14/cline-releases-cline-sdk-an-open-source-agent-runtime-now-powering-its-cli-and-kanban-with-ide-extensions-being-migrated/
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:30:48.573071
---

📌 **【Cline 釋出】開放原始碼 Agent SDK @cline/sdk 重塑 AI Coding Agent 架構**

你以為 AI Coding Agent 只是裝在 IDE 裡的外掛？現在它的核心被抽離出來，可以跨平台、跨 UI 運行，長時間工作也不會因視窗重置而中斷。

🤔 **AI Coding Agent 的結構債問題**  
Cline 已經是數百萬開發者使用的開源 AI coding agent，但隨著功能不疊加在原始的 agent loop 與 VS Code 擴展上，維護與遷移到新環境變得愈來愈困難。團隊發現，繼續在既有架構上「再加一層」只會加深結構債，影響跨平台移植與長期運行的穩定性。

🧪 **將 agent harness 抽離為獨立的 TypeScript SDK**  
本週 Cline 發布了 @cline/sdk，一個開放原始碼的 TypeScript 套件，內部結構分層：  
- @cline/shared：放置類型、schema、工具函式、hook 合約與擴充註冊工具，不依賴上層。  
- @cline/llms：位於其上，負責提供者閘道與模型目錄，支援 Anthropic、OpenAI、Google、AWS Bedrock、Mistral、LiteLLM 以及任何 OpenAI‑compatible 端點（如 vLLM、Together、Fireworks），提供者邏輯完全與 agent loop 分離，切換僅需修改設定。  
- @cline/agents：再上層的瀏覽器相容、無狀態 agent 執行迴圈，負責迭代、工具編排與事件發射，但不擁有 session 儲存、內建檔案/殼層工具或其他 UI 特定功能。  

這樣的設計使得 agent loop 變得 **無狀態且可重複使用**，而運行時層變得 **耐久、可攜帶且與產品無關**。

🚀 **核心發現：長時間工作不再隨 UI 重置而終止，工作階段可跨介面移動**  
因為 agent 本身不依賴特定 UI，所有狀態被外部化，SDK 可以在 VS Code、JetBrains、CLI 甚至未來的自訂介面上運行。使用者在一個介面上啟動的長任務（例如大規模重構或多步驟除錯）不會因該介面被關閉或重新載入而中斷；同一工作階段也能透過 SDK 在不同介面間無縫遷移。

💡 **關鍵洞察：將「提供者邏輯」與「agent 核心」分離，讓 LLM 切換變成純粹的設定變更**  
所有 LLM 特定的程式碼被封裝在 @cline/llms 中，agent loop 只透過抽象介面呼叫。這意味著開發者若想換用另一個模型服務（例如從 OpenAI 切換到本地 vLLM），只需要修改 SDK 的設定檔，而無需觸碰 agent 核心程式碼。這樣的「提供者與執行環境解耦」大幅降低了建構多模型、多平台 agent 的複雜度。

⚠️ **目前的限制：SDK 仍在早期階段，IDE 擴展正在遷移中**  
公告中明確提到，IDE 擴展（VS Code、JetBrains 等）正在逐步遷移到新 SDK 上，因此部分功能可能仍依賴舊實作。此外，SDK 以 TypeScript 為主，若團隊主要使用其他語言 stack，可能需要自行建置適配層。最後，文件僅列出了已支援的 LLM 提供者，未來新增提供者仍需看社群貢獻。

🎯 **實務啟示：開發者可直接利用 @cline/sdk 建構跨平台、可換模型的 AI coding agent**  
- 如果你正在打造自己的 agent 工具，可將 @cline/sdk 作為基礎，專注於業務邏輯與工具開發，而不必重新實作 agent loop 或 provider 介面。  
- 想要在 CLI、IDE 甚至自訂儀表板間共享同一個 agent 實例？SDK 的無狀態設計讓這變得可行。  
- 需要快速測試不同 LLM？只需更改 @cline/llms 的設定，即可切換提供者，無需重新編譯 agent 核心。  

🔗 **資訊來源**  
📝 Cline Releases Cline SDK: An Open-Source Agent Runtime Now Powering Its CLI and Kanban, With IDE Extensions Being Migrated  
👤 作者：Asif Razzaq (MarkTechPost)  
🔗 連結：https://www.marktechpost.com/2026/05/14/cline-releases-cline-sdk-an-open-source-agent-runtime-now-powering-its-cli-and-kanban-with-ide-extensions-being-migrated/

你有試過在不同工具間移動 AI agent 的工作嗎？歡迎在留言區分享你的經驗或對這個 SDK 的看法 👇

#AI #Agent #Cline #SDK #TypeScript #LLM #VSCode #JetBrains #CLI #開發工具 #GenAI
