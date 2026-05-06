---
title: "vercel-labs/open-agents"
source: GitHub Trending
url: https://github.com/vercel-labs/open-agents
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:17:35.862664
---

📌 【Vercel Labs 開源】解耦式背景編碼智能體實作

你搭建背景編碼智能體（Agent）時，是否遇到執行流程被沙箱生命周期綁死的問題？
Vercel Labs 開源的 Open Agents 用一個核心架構決策解決了這個痛點：Agent 完全不運行在執行沙箱內。
這種反直覺的設計，讓長時運行的編碼任務支援休眠、恢復，甚至不需要開著你的筆電。

🤔 **背景編碼智能體需脫離本地，長時間獨立運行**
近期 Agent 與推理編排成為技術熱潮，開發者對能後台運行、不需要持續佔用本地資源的編碼智能體需求大增。Vercel Labs 開源的 Open Agents 正是針對這個場景打造的開源參考實作，目標是實現從 Prompt 到代碼變更的全自動流程，且不需要保持筆電處於運行狀態。
該專案明確定位為可 fork 修改的參考實作，而非封閉黑盒，鼓勵開發者根據自身需求調整使用。

🧪 **三層架構、Agent 與沙箱徹底解耦**
Open Agents 採用清晰的三層架構設計：Web 層、Agent 工作流層、沙箱 VM 層（隔離執行環境）。
Web 層負責處理認證、會話管理、聊天交互與串流 UI；Agent 工作流跑在 Vercel 平台的持久化工作流（Durable Workflow）上，由 Workflow SDK 提供支持；沙箱 VM 是純執行環境，包含檔案系統、Shell、Git、開發伺服器與預覽端口。
最核心的架構決策是 Agent 與沙箱完全解耦：Agent 不運行在 VM 內，而是在外部透過文件讀寫、編輯、搜索、Shell 命令等工具與沙箱交互。這種設計帶來四個關鍵優勢：
1. Agent 執行不再被單次請求的生命周期綁定
2. 沙箱生命周期可獨立休眠、恢復
3. 模型、供應商選擇與沙箱實作可各自獨立迭代
4. 沙箱始終保持純執行環境定位，不會演變為控制平面

🧠 **支援可中斷恢復的多步編碼工作流**
目前 Open Agents 已具備完整的背景編碼智能體能力：
- 聊天驅動的編碼智能體，支援文件操作、搜索、Shell、任務管理、技能調用、Web 工具等
- 基於 Vercel Workflow SDK 的持久化多步執行，支援串流輸出與
