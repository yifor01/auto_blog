---
title: Claude Code regularly sends each background agent’s transcript to its model
source: Hacker News
url: https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce
model: claude-code/sonnet
generated_at: '2026-10-29T22:03:32.041294'
score: 92
---

📌 Claude Code 背景 Agent 偷偷燒 token，一個 70 行的修補救回近兩成用量

TL;DR：Claude Code 每 30 秒把背景 agent 的完整對話記錄重送模型，只為了更新一行三到五個字的狀態文字；開發者寫了個 Bun preload 關掉它。

你面板上那行「正在搜尋檔案…」的狀態文字，看起來只是個貼心小提示。但有人用 OpenTelemetry 量過，這行字背後燒掉的 token，比你跟 Claude 的主對話還多。

🤔 **問題：狀態列比主對話還貴**

根據這篇 gist 的說法，Claude Code 每隔約 30 秒,會對每一個背景 agent 執行一次動作：把該 agent 完整的對話記錄重新送給它自己的模型（通常是 Opus），請模型用三到五個字描述「你最近做了什麼」。這個答案只用來更新 agent 面板上的狀態列，從不會進入模型推理或使用者的對話內容。而且沒有任何設定可以關掉它，自 2.1.232 版（2026 年 8 月）起更是預設開啟。

🧩 **怎麼發現的：OpenTelemetry 裡的異常**

這個異常是作者 DRIM 在 Claude Code 的 OpenTelemetry 匯出數據中發現的：把 `claude_code.api_request` 事件依 `query_source` 分組後，`agent_summary` 這個來源的花費居然超過主對話本身。裝上修補前一週，`agent_summary` 佔整體花費的 16.4%（主對話是 15.7%），佔全部 API 請求的 19.7%，大約每五個請求就有一個是在產生狀態文字；裝上修補兩天後，這兩個比例都掉到 0%。其中 96% 的花費落在 Opus 模型上，而輸入與輸出 token 的比例高達約 9000 比 1，因為每次都要重送整份 transcript，換回來的只是三五個字。作者也強調，這裡的「花費」是 Claude Code 自己估算的 `cost_usd`，不是真正的帳單；如果是訂閱制用戶，損失的其實是速率限制的餘裕。另外有一個 GitHub issue（#86879）彙整了四組獨立測量結果，數字落在 18% 到 26% 之間，印證這不是單一用戶的個案。

🧩 **修補原理：攔截計時器，不碰二進位檔**

修補檔 `no-agent-summary.js` 是一個約 70 行的 Bun preload 腳本，只攔截全域的 `setTimeout`，也就是狀態摘要計時器被設定的入口。當某個計時器的回呼函式原始碼中含有摘要器的特徵字串（例如 `[AgentSummary] Timer fired`）時，就回傳一個不會真正觸發的假 timer handle，其他所有計時器照常運作不受影響。作者解釋為什麼選擇攔截計時器而非更直接的方式：這個模組是以預編譯的 Bun bytecode 形式出貨，修改二進位檔內的 JS 文字字串不會有任何效果，而 API 請求也沒有經過可以包裝的全域 `fetch`；但 `Function.prototype.toString` 即使在 bytecode 執行下仍會回傳原始函式碼文字，所以能靠字串特徵識別出該計時器。假的計時器延遲時間設為 2 的 31 次方減 1 毫秒，因為 Node 與 Bun 對超過這個上限的延遲會直接當成 1 毫秒處理，等於立刻觸發，反而弄巧成拙。

🧩 **怎麼用**

安裝方式是下載腳本後，設定環境變數 `BUN_OPTIONS=--preload=<腳本路徑>`，然後重啟 daemon（`claude daemon stop --any`）讓所有背景行程套用新環境。作者特別提醒等號寫法（`--preload=<path>`）與空格寫法在 bun 子指令底下行為不同，用錯會讓 `bun install` 之類的指令失效。環境變數 `CC_AGENT_SUMMARY_MODE` 可以切換關閉（預設）或保留摘要行為做 A/B 對照，`CC_AGENT_SUMMARY_LOG` 則能記錄每次攔截事件方便驗證。

⚠️ **適用範圍與限制**

作者在 Linux 上針對 Claude Code 2.1.257 到 2.1.312 版本實測，macOS（darwin-arm64）有其他使用者回報可行，Windows 則尚未驗證。由於 Claude Code 更新可能悄悄改掉底層機制，作者提醒每次更新後都要重新執行驗證步驟，確認 preload 仍正常載入、計時器確實被攔截。

🎯 **實務啟示**

如果你的團隊大量使用 Claude Code 的背景 agent，這類「看不見卻持續燒錢」的隱藏開銷值得定期用 OpenTelemetry 之類的工具稽核,而不是只看帳單總數。對於開發 agent 平臺的團隊，這也是一個提醒：任何定期輪詢式的 UI 更新機制，一旦接到 LLM 推理上，都該先問一句「這真的需要重新推理嗎，還是可以用更便宜的方式維護狀態」。

🔗 **來源**
- 標題：Claude Code regularly sends each background agent's transcript to its model
- 作者／機構：Flamerix AI（gist 作者），Hacker News 討論由 NikZaal 提交
- 連結：https://gist.github.com/flamerix-ai/c3905705cc4205e5de3011fa2e74efce

#ClaudeCode #AIAgents #TokenOptimization #DevTools #Anthropic #OpenSource #LLM #AgenticAI #CostOptimization #Bun
