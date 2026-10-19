---
title: 'Harness Engineering 101: The LLM is the brain, the harness is the body'
source: Hacker News
url: https://github.com/IsuruMaduranga/harness-engineering-101
model: claude-code/sonnet
generated_at: '2026-10-19T21:41:35.566659'
score: 97
---

📌 LLM 是大腦,Harness 是身體:16 章拆解 Agent 設計心法

TL;DR：一本從「~300 行玩具 agent」出發、系統化拆解 agent 設計演進的開源書,在 Hacker News 拿下 127 分、63 則留言。

LLM API 其實很單純：它是 stateless 的,每一輪你把整段對話包成 JSON array 傳過去,換回一段文字。業界現在講的「agent」,本質上都是對這個迴圈打的一個個補丁,而且每個補丁都是因為某件具體的事情壞掉了才出現。《Harness Engineering 101》就是用這個角度,把 agent 設計史拆成 16 個章節講清楚。

🤔 **一個迴圈,無數個補丁**

作者 Isuru Wijesiri 在開發 WSO2 MI Copilot、WSO2 BI Copilot 與 One Code 的過程中歸納出一個核心觀點：LLM 是大腦,harness（負責建構、維護、保護那個 JSON array 的程式)才是身體。每一章都遵循同樣的結構：先講某個失敗情境,再講最小的修補方式,最後講這個補丁付出的代價。

🧩 **四個 Part,從基礎到信任**

全書分成四個部分。Part I「The Wire」從最基礎的「這東西到底怎麼溝通」講起,涵蓋 JSON array、next-token 黑盒、工具呼叫如何映射成函式、agent loop,以及為何快取順序很重要。Part II「Running Long」處理 context 被塞爆之後的問題：context 是預算不是無底袋、用 subagent 分拆 context、如何在執行中途「導正」大腦、以及背景工作與非同步時間的處理。Part III「The Ecosystem」把市面上各種框架說穿──每個都只是 Chapter 1 的包裝,再講到 MCP、Skills、hooks 這些擴充能力,以及怎麼除錯那個 JSON array。Part IV 則談 Reflexes/Guardrails、以 coding agent 為案例的專精程度討論,以及「RAG 其實一直都是一種 harness pattern」。書末附錄另外談了 model routing、worktree 隔離、plan mode、重試與串流等進階主題。

🧩 **可以跑起來的玩具 harness**

這本書不只是文字,repo 裡 `src/harness/` 放的是可執行的玩具 harness,每個檔案對應書中一個發展階段；`src/diagrams/` 則是用來產生書中圖表的 Python 腳本。本機建置方式是先裝 `cargo install mdbook mdbook-mermaid`（或 `brew install mdbook`),再用 `mdbook serve --open` 即時預覽,`mdbook build` 產生靜態網站；圖表則可用 `cd src/diagrams && python3 gen_all.py`（需 Python 3.10+ 與 matplotlib)重新產生。

💡 **AI 輔助寫作,但內容自己把關**

作者在開頭揭露：每一章都是自己親手起草,但借助 Claude Code 與 One Code 重新排序章節（讓每章先講結論,也就是 Minto pyramid 寫法)、潤飾英文、產生圖表,以及撰寫畫圖用的程式碼。這種透明揭露本身也呼應了書裡談的「harness 只是輔助大腦」的主旨。

⚠️ **授權方式分兩套**

文字內容（`src/` 下的 `.md` 章節)採 CC BY-NC-ND 4.0,可分享但不得商用、不得發布修改版；程式碼（`.py` 檔與書中引用的程式碼片段)則採 MIT 授權,可自由使用並附上出處即可。

🎯 **實務啟示**

對正在評估該用哪個 agent 框架的工程師來說,這本書提供的是拆解底層原理的視角：與其糾結於 LangChain、AutoGPT 或任何新框架的術語差異,不如先搞懂「JSON array + 工具呼叫 + context 管理」這套基本功,再回頭看每個框架到底解決了哪個具體的失敗情境。

🔗 **來源**
- 標題：Harness Engineering 101: The LLM is the brain, the harness is the body
- 作者／機構：Isuru Wijesiri
- 連結：https://github.com/IsuruMaduranga/harness-engineering-101

#AIAgents #LLM #AgentArchitecture #PromptEngineering #OpenSource #SoftwareEngineering #MCP #RAG #DeveloperTools #TechnicalWriting
