---
title: craft-ai-agents/craft-agents-oss
source: GitHub Trending
url: https://github.com/craft-ai-agents/craft-agents-oss
score: 76
model: google/gemma-4-31b-it:free
generated_at: '2026-06-28T19:28:14.270919'
---

📌 **【開源專案】Craft Agents：以檔案為中心的 AI Agent 協作介面**

TL;DR：基於 Claude 與 Pi SDK 開發，提供非 CLI、以檔案為中心的 UI，讓 Agent 能自動對接 API 與服務。

大多數與 AI Agent 互動的體驗仍停留在聊天視窗或繁瑣的 CLI 設定，但開發者真正需要的是一個能高效多工、且能像操作檔案一樣管理 Agent 工作流的環境。

🤔 **擺脫 CLI 與設定嚮導的繁瑣**

Craft Agents 是由 craft.do 團隊為了提升與 Agent 協作效率而開發的工具。其核心目標是提供一個「非 CLI」且更具主見（opinionated）的互動方式，讓使用者能透過流暢的 UI 進行直覺的多工處理，並將工作重心從單純的「程式碼」轉移到「檔案」導向的工作流。

🧩 **結合兩大 SDK 的 Agent 原生設計**

該專案採用「Agent Native」的軟體設計原則，在技術實作上同時整合了 Claude Agent SDK 與 Pi SDK，旨在結合兩者的優勢並針對不足之處進行改良。其設計特點包括：
- **檔案中心化工作流**：不同於傳統的程式碼編輯器，以檔案為核心來管理 Agent 任務。
- **高度可客製化**：專案採取 Apache 2.0 開源授權，允許使用者自由修改。
- **以 Agent 開發 Agent**：作者宣稱該工具本身就是使用 Craft Agents 開發而成，完全不需要使用程式碼編輯器，所有的客製化僅需透過 Prompt 即可完成。

💡 **自動化對接 API 與 MCP 伺服器**

Craft Agents 試圖簡化最令開發者頭痛的環境設定過程。使用者無需編寫設定檔或操作設定嚮導，只需對 Agent 下指令（例如：「add Linear as a source」），Agent 會自動執行以下流程：
- 尋找公開 API 與 MCP (Model Context Protocol) 伺服器
- 閱讀相關檔案
- 設定憑證（Credentials）
- 完成所有配置

🎯 **實務啟示**

對於需要整合多個第三方服務（如 Slack, Gmail, Linear）且不希望陷入繁瑣設定的工程師，Craft Agents 提供了一種「指令即配置」的新嘗試。其將 MCP 伺服器自動化對接的機制，能大幅降低 AI Agent 進入實際工作流的部署門檻。

🔗 **來源**
- 標題：craft-agents-oss
- 作者／機構：craft-ai-agents
- 連結：https://github.com/craft-ai-agents/craft-agents-oss

#AI #Agent #OpenSource #ClaudeSDK #PiSDK #MCP #Productivity #LLM #SoftwareArchitecture #DeveloperTools
