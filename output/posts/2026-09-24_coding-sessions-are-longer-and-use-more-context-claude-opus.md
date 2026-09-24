---
title: Coding sessions are longer and use more context. Claude Opus 5.5 is built with
  that in mind.
source: Claude Blog
url: https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context
model: claude-code/sonnet
generated_at: '2026-09-24T20:36:01.585619'
pinned: true
---

📌 Claude Opus 5.5：讓快取讀取成本砍 60%，因為你的 coding session 早就變了

TL;DR：Anthropic 官方數據顯示 coding session 變長變重，Opus 5.5 用定價、模型行為與 harness 三管齊下，把費用壓低約 40%。

過去半年，你跟 Claude Code 的互動模式其實悄悄變了：同一個 prompt，Claude 現在願意多花 3.3 倍的時間、多打超過 40% 的 model call 才回覆你。這不是模型變慢，而是開發者已經把 agent 丟去處理更龐大、更開放式的任務。Anthropic 在這篇部落格中，用實際使用數據解釋了 Claude Opus 5.5 為何是為這種新型態工作打造的。

🤔 **coding session 正在變長、變重**

Anthropic 拉取了 2026 年 3 月到 9 月的 Claude Code 聚合使用數據，發現幾個明顯趨勢：每個 session 的 prompt 數量維持穩定，但每個 prompt 的處理深度大幅上升。Claude 在每個 prompt 上工作的時間拉長 3.3 倍，model call 次數增加超過 40%，而中斷次數減少 68%。開發者連接 tool server 或使用 skill 的機率增加約一倍，直接貼文字進 prompt 的頻率則減少三分之一。每個請求的 context 量成長了 2.6 倍，輸入輸出 token 比例也從 189:1 拉高到 324:1。這些數字共同指向同一件事：開發者正把更有能力、資訊更充足的 Claude 導向更大、更開放式的任務，context engineering 的經濟效益也因此被放大。

🧩 **三個讓長 session 更省錢的改動**

Anthropic 指出三個讓長時間、高 context session 更划算的變化：

第一是定價本身。按 token 計費的輸入與輸出 token 價格降低 20%，而快取讀取（cache read）的 token 價格更是直接砍了 60%。這一點格外關鍵，因為快取讀取本來就佔 agentic 與 coding 工作成本的大宗，而過去六個月每個請求的 context 量又成長了 2.6 倍，代表帳單裡快取讀取所佔比例只會愈來愈高。截至發文當下，Opus 5.5 的快取 token 價格僅為競品的五分之一，同時效能表現更好。

第二是 Claude Code harness 本身更擅長運用快取。照理說 session 變複雜，快取命中率應該下降，但實際上輸入未命中快取（cache miss）的比例反而降低超過 50%。Anthropic 修補了會意外打斷快取的小地方（例如重新登入），也處理了較大動作造成的破壞（例如對話中途加入新指令、動態載入 tool）。針對 Opus 5.5 與 Fable 5.1 這類新模型，開發者現在可以在 session 中途切換 effort level 而不用重設快取；API key 與雲端供應商的使用者也能像訂閱用戶一樣設定一小時的快取存續時間，被 fork 出來的 subagent 更能直接沿用 parent 的快取，不必重新付費讀取同一份 context。

第三是完成同樣任務所需的輪次變少。Anthropic 引用 Zeta Labs 的案例：相較 Opus 5，他們在任務中所需的輪次與 tool call 次數更少，成本接近腰斬，同時完成的高難度任務數量翻倍。

💡 **輪次省下的錢，比快取省下的更多**

不過 Anthropic 也坦言這個優勢並非放諸四海皆準。文中引用 Addy 在《The cost of a task on Opus 5.5》的觀察：「在範疇明確的任務上，兩個模型花的輪次差不多，你拿到的就只是降價本身；差距最大的地方會出現在開放式任務，因為模型可能在錯誤方向上耗掉很多輪次。沒有一個數字能套用在所有 codebase 上，你得自己實測。」換句話說，簡單、機械式的任務不會因為換模型而省下輪次，但困難、開放式的任務，Opus 5.5 更有機會避免在錯誤路徑上燒 token——而少一輪對話省下的錢，通常比省一次快取讀取還多。另外值得一提的是，Opus 5.5 的輸出生成速度比 Opus 5 快超過 30%，雖然這不會直接降低 token 用量，但長時間無人看管執行時能大幅減少等待。

🎯 **實務啟示：保護好你的快取命中率**

Anthropic 建議開發者在 Claude Code 中執行 `/usage` 檢查自己有多少用量來自快取讀取，並針對性地保護這個數字：在 session 一開始就選定模型、避免中途切換；離開電腦前先執行 compact 而不是回來後才做；若使用 API key 或雲端供應商，長時間 session 應設定一小時的快取存續時間。隨著 agentic coding 從「不計成本衝規模」轉向「有效率地擴大規模」，把開放式、高 context 的工作交給 Opus 5.5，並養成這些保護快取的習慣，會是接下來降低帳單的關鍵路徑。

🔗 **來源**
- 標題：Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.
- 作者／機構：Michael Segner @ Anthropic
- 連結：https://claude.com/blog/claude-opus-5-5-built-for-coding-sessions-that-use-more-context

#Anthropic #ClaudeCode #ClaudeOpus #LLM #AIcoding #PromptCaching #DeveloperTools #AgenticAI #TokenPricing #SoftwareEngineering
