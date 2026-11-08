---
title: Google AI Releases Elephant-Goldfish Model Plugin for Spec-First Coding
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/08/google-elephant-goldfish-model-plugin-spec-review-coding-agents/
model: claude-code/sonnet
generated_at: '2026-11-08T21:15:03.109681'
score: 94
---

📌 【Google開源】寫規格先過AI審查，再動手寫code

TL;DR：Google開源Elephant-Goldfish Model plugin，讓coding agent先寫規格書，交給無記憶的子agent挑錯，問題抓在Markdown而非PR裡。

如果程式碼動工前的規格文件，能先被一群「什麼都不記得、只看文件本身說了什麼」的審查者挑毛病，是不是能少掉很多事後才發現的架構誤解？這正是Google這次開源方案想解決的問題。

🤔 問題：AI產出的「slop」與context collapse

Google的出發點是修正AI coding agent常見的程式碼品質不穩定（文中稱為「slop」）與長對話後的context collapse問題。官方部落格說內部已有數千名工程師在用這套流程。方法的靈感來自Dave Rensin寫的一篇關於「大象與金魚」的文章。EGM本身是Apache 2.0授權的一組skills、reviewer persona與文件標準，不是新的語言模型，README也特別聲明這不是Google官方支援的產品。

🧩 架構：Elephant寫稿，Goldfish挑錯

- Elephant：一個長時間運作的session，持有整個專案的context與過去的決策，負責起草規格書，自己不寫程式碼。
- Goldfish：每一個都是無狀態的subagent，只讀規格草稿與其中引用到的檔案，用來抓出錯誤的假設。
- 人：負責在Elephant與Goldfish之間拍板trade-off、核准最終設計。
- `/egm-drift-report`：事後拿程式碼和規格書做比對，官方文件建議每週跑一次。

Review skill固定走5個連續階段，每個階段最多允許1次re-audit，發現的問題分成Blocker、Major、Nit三個等級。如果執行環境沒有subagent工具，EGM會直接停止運作，因為文件明確指出「在同一個context裡做審查，不算真正的Goldfish review」。

🧩 支援現況

目前的harness指南涵蓋Antigravity CLI、Antigravity App、Claude Code、Claude Cowork、Codex、ChatGPT、omp與Muse，其中Antigravity CLI、Claude Code與Codex可以通過自動化的end-to-end測試。用Claude Code的話需要2.1.271以上版本，而且審查階段只給Read、Grep、Glob三個工具，CLAUDE.md檔案會被排除在context之外。上線時的報導稱目前僅完整支援Antigravity，其他host陸續補上。

💡 和同類工具的差異

文章指出EGM最獨特的地方，在於「用完全沒有上下文的agent去審查規格書本身」。相比之下，Spec Kit與Kiro是在不同開發階段之間插入人類審查，Superpowers則主要是在實作階段才對subagent做隔離。

🎯 實務啟示

如果團隊已經在用多agent的coding流程，值得參考的不是具體工具本身，而是「審查者故意不給上下文」這個設計：它強迫規格書必須寫得自洽、能被獨立理解，而不是依賴審查者腦補專案脈絡去填補漏洞，這對降低後期才發現架構誤解的成本應該有幫助。

🔗 來源
- 標題：Google AI Releases Elephant-Goldfish Model Plugin for Spec-First Coding
- 作者／機構：Asif Razzaq（MarkTechPost）；方法出自Dave Rensin
- 連結：https://www.marktechpost.com/2026/11/08/google-elephant-goldfish-model-plugin-spec-review-coding-agents/

#Google #AICoding #SpecDriven #CodingAgent #OpenSource #SoftwareEngineering #LLM #DeveloperTools #AgenticAI #CodeReview
