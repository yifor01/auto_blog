---
title: Reducing cost and improving performance with Claude Platform
source: Claude Blog
url: https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
model: claude-code/sonnet
generated_at: '2026-09-08T20:01:29.757664'
pinned: true
---

📌 【Anthropic 官方發布】Claude Platform 省成本三招,效能不打折

TL;DR:調校 prompt caching、清理過時 prompt 與校準 reasoning effort,能在不犧牲效能下降低 Claude API 成本。

「省錢等於犧牲效果」幾乎是每個導入 LLM 應用團隊的預設假設。但 Anthropic 在最新的 Claude Platform 部落格文章裡指出,多數應用其實有辦法在幾乎不影響效能的前提下大幅降低成本,問題往往出在幾個容易被忽略的設定細節。

🤔 效能與成本真的只能二選一嗎

文章作者、Anthropic 的 Lance Martin 指出,許多使用 Claude Platform 的應用可以透過三個方向省錢而不犧牲效能:最大化 prompt cache 命中率、在升級到前沿(frontier)Claude 模型時移除 prompt 中的反模式(anti-pattern),以及依任務校準 reasoning effort。這些建議已整合進 claude-api skill。

🧩 Prompt Cache:別讓 KV 快取白白浪費

Claude 在產生回應前,會先把 prompt 處理成內部的運算狀態,這個步驟稱為 prefill,是輸入處理中成本最高的部分。Prompt caching 會把這個狀態(也就是 key–value、KV 快取)保存下來:當請求的開頭與先前 prompt 的前綴完全相同時,Claude 就能直接讀取快取,而不必重新計算,快取讀取的計費也只是原價的一小部分。

要有效利用 prompt cache,有幾個限制要注意:快取綁定特定模型;快取讀取必須與先前 prompt 的整段前綴逐位元組(byte-exact)相符;快取本身有存活時間(TTL)限制。

文章給出的具體做法包括:
- 避免在對話中途變更 effort 或 thinking 設定(這些設定會渲染在 prompt 最前面,屬於快取前綴的一部分;不過 Opus 5 與 Fable 5.1 可以在對話中途調整 effort 而不破壞快取)。
- 讓易變動的內容(如動態時間戳記或 ID)遠離 prompt 前綴。
- 避免工具定義的順序被打亂,因為 Claude Messages API 會把工具定義固定渲染在 prompt 最前段,任何變動都會讓快取失效。
- 分支(fork)對話或使用 subagent 時要留意,只有在前綴逐位元組相同、模型相同、effort 相同的情況下才能共用父層快取。
- 避免同步工具呼叫或執行時間超過快取 TTL 的 subagent,否則下一輪請求要以 1.25 倍(若快取設為 1 小時 TTL 則是 2 倍)的原價重寫快取,而非享受便宜的讀取價。

除此之外,Anthropic 也建議善用 Claude Console 的 prompt cache 診斷功能監控命中率、用 defer_loading 讓不常用的工具定義延後載入以避免佔用快取前綴、用訊息(message)而非直接編輯 system prompt 來套用更新、把穩定內容放在前面而動態內容放在後面、在 compaction 等本來就會重寫快取的時間點順便切換模型或 effort、讓自動快取斷點(breakpoint)隨對話成長而移動,以及在使用者輸入時提前發送 max_tokens: 0 的請求來預熱快取。

🧩 Prompt 反模式:舊時代的補丁,拖累新模型

隨著 prompt 不斷疊加用來修正舊模型弱點的指令,這些指令可能與最新 Claude 模型的能力脫節。文章列出幾種常見的反模式:要求「再三檢查」的驗證儀式;「務必極度徹底」之類的強調字眼;強制的步驟流程或 scratchpad 推理範本;針對舊模型失敗模式微調的 few-shot 範例;彼此矛盾的規則;以及針對舊世代模型撰寫的過時設定(例如手動 thinking budget)。這些反模式在前沿模型上不僅沒有幫助,反而容易造成不必要的冗長輸出或多餘的工具呼叫。

📊 拿 Opus 4.8 升級到 Opus 5 做實測

Anthropic 團隊在一個客服(customer support)基準測試上做了實驗:從乾淨的 prompt 出發,依序埋入退役的 thinking 設定、一組互相矛盾的退款規則、手動 scratchpad、「再三檢查」、「務必極度徹底」,以及強制的六步驟流程,總共產生六份「舊版」prompt。接著分別在 Opus 4.8、僅換模型 ID 的 Opus 5,以及跑過一次 /claude-api prompt-audit 之後的 Opus 5 上執行。

結果顯示,「再三檢查」這類驗證儀式會讓 Opus 5 在每一次退款流程中重複查詢訂單,徒增 token 消耗;「務必極度徹底」這類強調字眼則讓模型多做了數十次不必要的知識庫搜尋。這說明針對舊模型寫的補丁式指令,搬到前沿模型上反而可能拖累效能與成本。

💡 用工具而非手動審查抓出問題

為了讓開發者能系統性抓出這些反模式,Anthropic 把偵測邏輯做成指令,在 Claude Code 中執行 /claude-api prompt-audit 即可掃描工作目錄下的 prompt、skill 與工具描述,涵蓋呼叫 Claude API 的應用程式碼,也包含 Claude Code 自身的設定檔(如 CLAUDE.md 或 skills)。

🎯 實務啟示

如果你的團隊正在升級到前沿 Claude 模型,或單純想壓低現有的 API 成本,不妨先檢查 prompt cache 命中率是否異常偏低,再用 /claude-api prompt-audit 掃一遍現有的 prompt、skill 與工具描述,找出那些原本為了修補舊模型而寫、如今反而拖累新模型的指令。

🔗 來源
- 標題:Reducing cost and improving performance with Claude Platform
- 作者／機構:Lance Martin, Anthropic
- 連結:https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform

#Anthropic #ClaudeAPI #PromptEngineering #PromptCaching #LLMOps #CostOptimization #ClaudeCode #AIEngineering #LLM #DeveloperTools
