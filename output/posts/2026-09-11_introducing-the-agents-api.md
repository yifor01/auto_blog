---
title: Introducing the Agents API
source: OpenAI Blog
url: https://openai.com/index/introducing-the-agents-api
model: claude-code/sonnet
generated_at: '2026-09-11T19:47:55.062280'
pinned: true
---

📌 【OpenAI 官方發布】Agents API 上線:雲端代理也能像部署服務一樣簡單

TL;DR:OpenAI 推出代管式 Agents API,以 Codex harness 為底層,讓開發者能建置具備長時間執行與工具使用能力的雲端代理。

寫一個能自主完成任務的 AI agent 不難,難的是把它穩定地部署、監控、長時間運作。OpenAI 這次要解決的正是這個「從 demo 到生產環境」的落差。

🤔 **開發者面對的落差:能寫出 agent,卻難以上線**

根據 OpenAI 官方部落格,Agents API 是一個代管服務(managed service),讓開發者可以直接建置並launch雲端 agent,而不需要自己搭建底層的執行與管理基礎設施。

🧩 **由 Codex Harness 驅動的核心能力**

文章指出,這套 API 由 Codex harness 提供動力,涵蓋三項核心能力:
- 協調(orchestration):管理 agent 執行流程中的各個步驟。
- 長時間執行的 session:讓 agent 能持續運作,而非僅限於單次短暫的請求回應。
- 工具使用(tool use):讓 agent 能呼叫外部工具來完成任務。

💡 **從「函式庫」走向「代管服務」的轉變**

值得注意的是產品定位的轉變:Agents API 並非單純提供一組 SDK 讓開發者自行組裝,而是以代管服務的形式,把 orchestration、長時間 session 管理等原本需要自建的基礎設施都包進去。這意味著開發 agent 應用的重心,可能會從「如何自己搭建 agent runtime」轉移到「如何設計 agent 的任務邏輯與工具串接」。

🎯 **實務啟示**

對於正在開發 agent 應用的工程師來說,這代表原本需要自行處理的 session 持久化、任務排程、工具呼叫管理等基礎設施工作,有機會直接交給代管服務處理。若你的團隊正在評估要自建 agent 執行框架還是採用代管方案,這會是值得納入評估的選項,尤其是在長時間執行任務與多工具協調的場景。

🔗 **來源**
- 標題:Introducing the Agents API
- 作者/機構:OpenAI
- 連結:https://openai.com/index/introducing-the-agents-api

#OpenAI #AgentsAPI #Codex #AIAgents #LLM #CloudComputing #ToolUse #Orchestration #DeveloperTools #AIInfrastructure
