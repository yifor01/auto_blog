---
title: 'MiniMax Open-Sources MCode Stack: 15 Agent Skills Its Coding Team Uses Daily'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/28/minimax-open-sources-mcode-stack-agent-skills/
model: claude-code/sonnet
generated_at: '2026-10-28T21:57:09.799189'
score: 96
---

📌 MiniMax 開源 MCode Stack：15 個 Coding Agent 技能一次公開

TL;DR：MiniMax 把自家打造 coding agent 的工作流與技能文件全部開源，工程師可直接安裝進 agent 裡執行。

多數團隊分享的「AI coding 心得」停在一篇部落格或一份 prompt 範本，讀完之後還是要自己動手轉譯成可用的流程。MiniMax 這次反其道而行：直接把團隊每天用來打造 MiniMax Code 的工作流、技能與檢查清單整包開源，而且每一份都是可以讓 agent 直接執行的 SKILL.md 檔案，不是單純的 prompt 集合。

🤔 **把工程習慣寫成 agent 能跑的步驟**

MCode Stack 於 2026 年 10 月 28 日以 MIT 授權公開。值得注意的是，這個 repo 本身不含 MiniMax Code 的原始碼，裡面只有 workflows、skills 與 checklists。這些內容搭配一個名為「MCode Engineering Notes」的系列文章，每篇筆記解釋一個工程概念，而 repo 則把這個概念變成可執行的流程。目前已發布的筆記主題包括 subagents、tool context、compaction 與 memory 的取捨，以及長時間執行的 bash 指令；另有一篇關於「per-turn context tax」的筆記標示為即將推出。

🧩 **15 個技能依工作時刻分組，獨立審查是亮點**

整個 stack 共有 15 個技能，依「一天工作中的不同時刻」分組設計。其中 independent-review 這個技能的設計理念特別值得一提：它只給審查者 3 項輸入，分別是 diff、需求與測試結果，刻意不讓審查者看到作者原本的對話紀錄。理由是，如果審查者繼承了作者的上下文，很容易重複作者本身的盲點，審查就失去了獨立性。另外有 6 個 engineering-* 技能改編自 Google Engineering Practices，這部分內容依 repo 的 NOTICE 說明，仍沿用 CC-BY 3.0 授權,與整包 MIT 授權的其他內容分開處理。

🔌 **安裝方式與相容性**

依 README 說明，安裝這套技能有 3 種路徑可選。同一套目錄也能在 Claude Code 中使用，只要執行 `/plugin marketplace add MiniMax-AI/mcode-stack` 即可。MiniMax Code 本身也會讀取 `~/.claude/skills/` 與 `~/.codex/skills/` 這兩個目錄。由於這些技能採用通用的 SKILL.md 格式，理論上大多數支援 skills 機制的其他 agent 也能直接套用。

🎯 **適合誰：設計 harness 的人，而非只是使用 agent 的人**

MCode Stack 的定位比較窄,它瞄準的是「設計 agent harness」的工程師，而不是單純使用現成 agent 的人。文中也提到,目前涵蓋更廣泛 harness 場景的是 Superpowers。對於正在打造自有 coding agent 流程、或想把團隊 review 習慣標準化成可重複執行步驟的工程師來說，這份開源內容提供了一個現成的參考範本,可以直接拿來改寫成符合自己團隊需求的版本。

🔗 **來源**
- 標題：MiniMax Open-Sources MCode Stack: 15 Agent Skills Its Coding Team Uses Daily
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/28/minimax-open-sources-mcode-stack-agent-skills/

#MiniMax #CodingAgent #AgentSkills #OpenSource #LLMOps #DeveloperTools #ClaudeCode #SoftwareEngineering #AgentHarness #MIT
