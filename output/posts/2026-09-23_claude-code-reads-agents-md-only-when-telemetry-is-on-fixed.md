---
title: Claude Code reads AGENTS.md only when telemetry is on [fixed]
source: Hacker News
url: https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/
model: claude-code/sonnet
generated_at: '2026-09-23T20:34:24.372024'
score: 106
---

📌 Claude Code 的 AGENTS.md，居然要看 telemetry 臉色

TL;DR：一份逆向工程調查顯示，Claude Code 讀取 AGENTS.md 的功能被綁在一個預設關閉、依賴遠端旗標的隱藏開關上。

你把 telemetry 關掉，只是不想讓使用資料被回傳，結果專案裡的 AGENTS.md 卻悄悄消失，Claude Code 連提都沒提一句。

🤔 **背景：一個「不需連網」的功能，為何要連網才能開**

Claude Code 2.1.277 宣布支援 AGENTS.md，在專案沒有 CLAUDE.md 時應該改讀這個檔案。作者 pszypowicz 發現自己 repo 裡的 AGENTS.md 從未被讀取過，深入研究後在 GitHub issue #95690 找到原因，並補上自己的實測數據，整理成這篇文章。

🧩 **逆向工程：藏在二進位檔裡的遠端旗標**

作者指出，這個 loader 是內建外掛程式 agents-md，在 2.1.280 版本裡，其 isOnByDefault（變數 W）為 false，isAvailable（函式 B）則會去查詢一個叫 tengu_agents_md_mod 的遠端 feature flag，若無法取得，fallback 也是 false。也就是說，當 Claude Code 抓不到這個遠端旗標時，外掛就處於不可用狀態，本地的 AGENTS.md 完全不會被讀取——即便讀一份工作目錄下的 markdown 檔案本身完全不需要網路。

作者的測試方法很直接：建立一個只含 AGENTS.md（裡面放一個 canary word）的空目錄，用 `claude -p` 詢問這個 canary word，每種設定各跑兩次 session（第一次抓旗標，第二次才會用到）。

📊 **實測結果：關掉隱私設定，連帶關掉了讀檔功能**

- 設定 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` 會阻擋此功能，設定 `DISABLE_TELEMETRY=1` 同樣會阻擋，兩者只要有一個生效，AGENTS.md 就不會被讀取。
- 把這兩個變數設為 0 並不會解除阻擋，效果依然存在。
- 在專案的 `.claude/settings.json` 裡用 env block 清空這兩個變數也沒有效果，換句話說，沒有辦法針對單一 repo 單獨開啟這個功能。
- 只有從第二個 session 起，用 session 層級的 `--settings` 參數覆寫才有效。
- 上述所有情況都沒有任何警告訊息，session 直接開始回答，不會告知使用者有檔案被跳過。
- issue 裡也提到，第三方 gateway、Bedrock、Vertex 都有同樣問題，因為那個遠端旗標在這些環境裡永遠無法解析為 true。

💡 **為何作者認為這不可接受**

作者認為，關掉 telemetry 理應只犧牲診斷資訊，不該連帶關掉「讀取自己硬碟上的檔案」這種本地行為。更諷刺的是，這個閘門恰好打在最在乎 AGENTS.md 的那群人身上：同時維護多個 agent 共用指令檔的使用者，通常對外傳資料特別謹慎，而走 Bedrock、Vertex 或 gateway 的團隊，往往是依政策關閉 nonessential traffic。這些人得到的是一個「宣稱可用、實際上什麼都不做」的功能。

作者找到的 workaround 是：CLAUDE.md 支援 `@path` imports，且不依賴這個旗標。只要建立一個內容為 `@AGENTS.md` 的一行 CLAUDE.md，即使 `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` 仍設定著，canary word 測試依然能成功讀到內容，代價是每個 repo 多一個檔案——恰好是 AGENTS.md 支援原本想省掉的東西。

文章另外也提到：目前沒有 user 層級的全域 AGENTS.md（只有專案內的 AGENTS.md 與 `.claude/AGENTS.md`），Codex 則有 `~/.codex/AGENTS.md`；而 skills 方面，Claude Code 只認 `.claude/skills`，作者實測把 canary skill 放進 `.agents/skills` 不會被列出，但用 symlink 把 `.claude/skills` 指向 `.agents/skills` 就能生效。

⚠️ **限制**

這些發現來自單一使用者的逆向工程與 canary 測試，並非官方文件明確確認的規格；標題本身標注了「[fixed]」，暗示問題可能已有後續處理，但摘要中未說明具體的修復內容。

🎯 **實務啟示**

若你的組織因隱私政策關閉 telemetry，或走 Bedrock、Vertex、gateway，別假設 AGENTS.md 一定會生效——先用一行 `@AGENTS.md` 的 CLAUDE.md 當保險，並用 symlink 讓 `.claude/skills` 指向共用的 `.agents/skills`，避免共用指令與 skills 因為一個看不見的遠端旗標而悄悄失效。

🔗 **來源**
- 標題：Claude Code reads AGENTS.md only when telemetry is on [fixed]
- 作者／機構：pszypowicz
- 連結：https://blog.szypowi.cz/p/claude-code-reads-agents.md-only-when-telemetry-is-on/

#ClaudeCode #AGENTSmd #Anthropic #DevTools #Telemetry #Privacy #AIAgents #ReverseEngineering #DeveloperExperience #LLMTooling
