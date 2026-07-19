---
title: anthropics/skills
source: GitHub Trending
url: https://github.com/anthropics/skills
score: 103
model: tencent/hy3:free
generated_at: '2026-07-19T08:01:29.620893'
---

📌 【Anthropic 開源】anthropics/skills：Claude 專用技能資料夾實作範例

TL;DR：Anthropic 釋出 Claude skills 實作庫，含創意、技術與企業流程範例。

當大家還在討論怎麼幫 LLM 接外掛時，Anthropic 直接把自家 Claude 的「技能系統」實作資料夾開源出來了——不是標準規格，而是真的能跑的範例。

🤔 **Skills 是什麼：可動態載入的任務資料夾**

根據 README 說明，skills 是一個個資料夾，裡麵包含 instructions、scripts 與 resources，Claude 會在需要時動態載入，以提升特定任務的表現。它的目的是用可重複的方式，教 Claude 完成具體任務，例如：用公司品牌規範產出文件、用組織內部流程分析資料，或自動化個人任務。

🧩 **每個技能自成一個資料夾，靠 SKILL.md 驅動**

README 指出，每個 skill 都是自含（self-contained）的獨立資料夾，內含一個 SKILL.md 檔案，裡頭存放 Claude 使用的指令與 metadata。這種結構讓技能之間互不幹擾，也方便瀏覽與借鏡。

📂 **範例橫跨創意、技術與企業流程**

此 repository 收錄的 skills 用來展示 Claude skills 系統的可能性，範圍包括：
- 創意應用：art、music、design
- 技術任務：testing web apps、MCP server generation
- 企業流程：communications、branding 等

另外，README 提到在 skills/docx、skills/pdf、skills/pptx、skills/xlsx 子資料夾中，放了驅動 Claude 檔案能力的檔案建立與編輯技能（source-available）。

💡 **多數採 Apache 2.0，可作為自製技能靈感**

許多 skills 以 Apache 2.0 開源；倉庫定位是「展示可能性」與「提供模式參考」，開發者可以瀏覽這些資料夾來獲取自製 skills 的靈感，或理解不同的設計模式。若想了解 Agent Skills 標準本身，README 指引參見 agentskills.io（非本文素材範圍，不延伸）。

🎯 **實務啟示**

如果你正在用 Claude 做品牌檔案、資料分析或內部自動化，可以直接參考這些資料夾結構與 SKILL.md 寫法，複製模式來封裝自己組織的 workflow，而不用從零設計技能系統。

🔗 **來源**
- 標題：anthropics/skills
- 作者／機構：Anthropic — anthropics
- 連結：https://github.com/anthropics/skills

#Anthropic #Claude #AgentSkills #Skills #OpenSource #LLM #Workflow #Automation #SKILLmd #GitHub
