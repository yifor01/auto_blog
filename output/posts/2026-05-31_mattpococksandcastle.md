---
title: "mattpocock/sandcastle"
source: GitHub Trending
url: https://github.com/mattpocock/sandcastle
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-31T19:31:51.140476
---

📌 Sandcastle AI  

你是否曾想讓多個 AI 編程 Agent 同時工作，又不互相干擾？  
Sandcastle 提供了一種在隔離沙箱中協調 Agent 的方式，只要一行 sandcastle.run()。  
它把每個 Agent 的變更放在獨立分支，最後自動合併回主線。  

🤔 AI 編程 Agent 需要安全且可重複的執行環境  
隨著 AI 輔助編程工具的普及，單靠本機直接執行容易造成環境污染或安全風險。開發者需要一種能在乾淨、隔離的容器中運行 Agent，且能夠追蹤每次變更的機制。  

🧪 透過分支策略與可插拔沙箱提供者實現隔離  
Sandcastle 使用 Git 分支作為隔離單位：每次呼叫 sandcastle.run() 會在新分支上啟動 Agent，所有提交會在該分支上記錄，任務完成後自動合併回 main。該庫本身與具體沙箱技術無關，內建支援 Docker、Podman 與 Vercel（透過 @vercel/sandbox 的 Firecracker microVM），開發者也可透過 createBindMountSandboxProvider 或 createIsolatedSandboxProvider 自行實作其他提供者。  

🚀 讓多個 Agent 並行執行、建置審核管線變得直接  
因為每個 Agent 都在獨立分支與沙箱中運行，開發者可以輕鬆啟動多個 AFK（遠端鍵盤）Agent 進行平行任務，或將 Sandcastle 整合到 CI 流程中作為程式碼審核的前置步驟。快速開始步驟僅需：  
1. npm install --save-dev @ai-hero/sandcastle  
2. npx @ai-hero/sandcastle init . （產生 .sandcastle 目錄）  
3. 編輯 .sandcastle/.env 填入 ANTHROPIC_API_KEY（或參考 #191 使用 Claude 訂閱）  
4. npx tsx .sandcastle/main.ts 執行範例，或在程式碼中直接 import { run, claudeCode } from "@ai-hero/sandcastle" 並搭配想要的沙箱提供者（例如 import { docker } from "@ai-hero/..."）。  

💡 分支式沙箱帶來的好處與權衡  
使用分支作為隔離單元使得每次執行都有完整的 Git 歷史可追蹤，異動可透過標準合併流程審核；同時，沙箱確保執行不會影響主機環境。這種設計雖不是全新概念（類似的分支＋容器模式在某些 CI 系統中已見），但把它包裝成可直接 npm 安裝、零設定的庫，降低了使用門檻。  

⚠️ 依賴 Git 與特定沙箱工具，早期階段功能尚未完備  
Sandcastle 前提條件包括已安裝 Git 以及一支支援的沙箱提供者（Docker Desktop、Podman 或 Vercel）。此外，該專案仍屬早期階段，文件與範例主要圍繞基本的 sandcastle.run() 流程，進階功能如自訂合併策略、多階段管線或更細緻的錯誤處理尚需社群貢獻。  

🎯 適合想要快速搭建 Agent 協作流程的工程師  
如果您希望在本機或雲端快速測試多個 AI 編程 Agent 的協同作業，或希望在現有工作流程中加入可重複的沙箱執行步驟，Sandcastle 提供了即用的 npm 包與明確的設定指南，無需自行從零建置分支與容器的樣板碼。  

🔗 **專案連結**  
📝 mattpocock/sandcastle  
👤 作者：mattpocock  
🔗 https://github.com/mattpocock/sandcastle  

#AI #TypeScript #Sandbox #AgentOrchestration #GitHubTrending #Sandcastle #DevTools #CodingAssistant
