---
title: anthropics/skills
source: GitHub Trending
url: https://github.com/anthropics/skills
score: 129
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T20:58:25.632944'
---

📌 【Anthropic 開源】Claude 的「Skills」機制：讓 AI 透過動態載入資源完成專業任務

TL;DR：Anthropic 開源 Claude 的 Skills 實作，透過指令、指令碼與資源的組合，讓 AI 能以可重複的方式處理專業工作。

當我們要求 AI 完成特定任務時，最頭痛的往往不是 AI 不夠聰明，而是它缺乏對企業品牌規範、特定工作流或專業工具的深度理解。如果每次都要在 Prompt 中重複輸入同樣的背景資訊，不僅浪費 Token，且一致性難以維持。

🧩 **將專業知識模組化：什麼是 Skills？**

Anthropic 定義的 Skills 是一組包含「指令 (instructions)」、「指令碼 (scripts)」與「資源 (resources)」的資料夾。其核心邏輯在於「動態載入」：Claude 會根據任務需求，動態載入對應的 Skill 資料夾來提升在特定任務上的表現。

這種設計讓 Claude 能以可重複的方式完成專業任務，例如：
- 依照公司品牌指南 (Brand Guidelines) 建立檔案。
- 使用組織特定的工作流 (Workflows) 進行資料分析。
- 自動化處理個人化的日常任務。

📂 **實作結構：一個 SKILL.md 決定一切**

根據該專案的設計，每個 Skill 都是自包含 (self-contained) 的獨立資料夾。其中最關鍵的檔案是 `SKILL.md`，該檔案包含了 Claude 執行任務所需的指令與後設資料 (metadata)。

此儲存庫提供了多種範例，展示了 Skills 的應用範圍：
- 創意應用：涵蓋藝術、音樂與設計。
- 技術任務：包含 Web App 測試以及 MCP server 的生成。
- 企業工作流：涉及溝通與品牌管理等。

💡 **揭露 Claude 內部的檔案處理機制**

值得開發者關注的是，Anthropic 在此專案中公開了驅動 Claude 檔案能力的核心實作。在 `skills/docx`、`skills/pdf`、`skills/pptx` 與 `skills/xlsx` 等子資料夾中，包含了 Claude 處理這些檔案格式的底層技能實作，讓開發者能直接觀察 AI 如何操作不同格式的檔案。

🎯 **實務啟示：從 Prompt 工程轉向「技能工程」**

對於開發 AI Agent 的工程師而言，這個專案提供了一個重要的設計模式：與其試圖寫一個巨大的 System Prompt 涵蓋所有功能，不如將能力「模組化」。將特定的專業知識與工具定義為獨立的 Skill，讓模型在需要時才載入，能有效提升任務的精準度與可維護性。

🔗 **來源**
- 標題：anthropics/skills
- 作者／機構：Anthropic
- 連結：https://github.com/anthropics/skills

#Anthropic #Claude #AIAgents #LLM #OpenSource #AgentSkills #MCP #PromptEngineering #SoftwareArchitecture #Automation
