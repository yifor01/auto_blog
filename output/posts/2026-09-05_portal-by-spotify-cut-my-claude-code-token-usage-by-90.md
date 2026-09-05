---
title: Portal by Spotify cut my Claude Code token usage by 90%
source: Hacker News
url: https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90
model: claude-code/sonnet
generated_at: '2026-09-05T19:14:22.664660'
score: 84
---

📌 【Spotify 工程部落格】兩個 Hook，把 Claude Code 的 token 用量砍掉九成

TL;DR：Spotify 用內部平臺 Portal 打造分層路由，把純 I/O 工作丟給便宜模型，實測省下約九成 token。

Coding agent 大部分時間都不是在「思考」，而是在讀五個檔案回答一個關於某個方法的問題，或是照著隔壁二十個測試檔案的既有樣式生出第二十一個。這些工作幾乎不需要推理，卻一樣是用最貴的前沿模型跑，直到 Spotify 工程師找到一個只用兩個模式（mode）就解決的方法。

🤔 帳單燒的不是座位，是 token

文章指出，到 2028 年，AI 輔助程式撰寫的成本預期會超過一名工程師的平均薪資；目前已有四分之一的工程主管每位開發者每月要燒 200 到 500 美元的 token，部分團隊甚至超過 2000 美元。作者的觀察是，工具本身值回票價，但前提是不要把大量不需要推理的「粗活」也丟給前沿模型處理。

🧩 用 AiKA Modes 打造分層路由

解法建立在 Portal by Spotify 的 AiKA Modes 上。一個 mode 是跑在一次性執行環境（作者形容像是給 agent 用的 AWS Lambda）上的宣告式 agent：你定義指令、選模型、設定 temperature 等參數、掛上 MCP 工具，Portal 負責其餘的執行細節，不需要自己管基礎設施或 API 金鑰。Mode 可以透過 Portal CLI 或 API 呼叫，也可以設為公開（全公司共用）或私有。

作者建立了兩個 mode，範例中都使用 Gemini 2.5 Flash 當作 worker 模型（這個欄位可換成 Portal 實例中設定的任何模型）：

- bulk-reader：用來取代「Claude 讀多個大檔案只為回答一個問題」的情境，指令要求只輸出結構化條列，不寫客套語與長篇散文，並且每個條列開頭要標明確切名稱、型別或行號。
- code-writer：用在測試、設定樣板、型別 stub 等「輸出可從既有樣式預測」的情境，額外要求「只輸出程式碼」，否則模型會把結果包在 markdown 區塊與說明文字裡，Claude 還得再解析一次。

第一版做法是把路由規則寫進 CLAUDE.md，靠 Claude 自己讀規則、自行決定要不要轉發，但這只是「建議」而非強制，Claude 可以無視它，而且每個專案都得重複貼一份規則。現在的版本是一個叫 shunt 的 Claude Code 外掛，委派動作走 Portal CLI 的 actions registry，所以只要對應的 Portal 實例有啟用 AiKA 外掛，這個外掛就能用。

shunt 註冊了兩個在每次工具呼叫前觸發的 PreToolUse hook：check-file-size 會在每次 Read 呼叫時檢查，若檔案超過可設定的行數門檻（預設 350 行，可透過環境變數 SHUNT_MIN_LINES 調整）就擋下讀取，改指示 Claude 呼叫 /bulk-reader skill；check-bash-read 則攔截針對大檔案的 cat、head、tail、less、more，但像 cat file | grep 這種帶管線、屬於「精準讀取」的指令會直接放行。兩支包好的 bash 腳本負責處理 Portal CLI 呼叫的細節：bulk-read 把檔案內容包進 XML 標籤後連同問題送給 bulk-reader mode，整個呼叫是一次性、伺服器端不留存，所以檔案內容重送並不會累加成本，因為原始語料只進到 worker 模型，從未進入 Claude 的上下文；code-write 把規格與一份參考檔案送給 code-writer mode，拿掉輸出中的 markdown 圍欄後直接寫入磁碟，Claude 完全不會看到產生的程式碼。這裡的參考檔案是必要的，沒有可比對樣式的檔案，worker 模型只會生出脫離專案脈絡的程式碼。

📊 大量讀取省下約九成 token

作者針對一個 Java monorepo，用四種情境測試「Claude 直接讀檔」對比「消費 bulk-reader 摘要，或透過 code-writer 寫入程式碼」所耗費的 token，結果 bulk-read 情境平均省下約九成 token。code-write 情境比較難用 token 直接量化，因為在沒有 shunt 的情況下，Claude 既要讀參考檔案，又要把產生的程式碼當成昂貴的輸出 token 吐出來；用了 shunt 之後，程式碼直接落地，Claude 完全看不到。

⚠️ 不是萬用解方

作者也明確畫出邊界：編輯無法委派，因為 worker 模型的摘要不含可靠的行號，若 Claude 要依分析結果動手改程式碼，還是得直接讀取特定區段，hook 也刻意放行帶 offset/limit 的精準讀取，所以委派省的是「理解」的 token，不是「編輯」的。推理也無法委派，作者測試中 worker 模型只找出表面規律，漏掉一個細微的執行緒安全錯誤，而 Claude 拿到正確脈絡後幾秒內就抓到了，因此路由規則明確排除 debugging、架構決策與安全攸關程式碼。另外，每次委派都是一次網路來回（Claude Code 到 Portal 後端再到 worker 模型），通常要 10 到 30 秒，Portal 也把單次呼叫上限設在 30 秒，對大量讀取划算，但對小檔案反而得不償失，這也是行數門檻存在的原因。

🎯 實務啟示

這篇文章真正有意思的地方，不是省了多少 token，而是把 model routing 從系統工程問題變成設定問題：mode 是可重複使用、可共用、可組合的元件，同一組 bulk-reader、code-writer mode 可以跨專案、跨任何能呼叫 Portal CLI 的工具重複使用，而且路由的「決策」（何時委派）與「執行」（如何回應）是脫鉤的，換模型、換 system prompt、加 MCP 工具都不需要動到外掛本身。如果你的團隊也有類似的內部平臺或能力，拆出「純 I/O」與「需要推理」這兩類任務，是一個立即可以嘗試的成本優化方向。

🔗 來源
- 標題：Portal by Spotify cut my Claude Code token usage by 90%
- 作者／機構：cebert, Spotify Engineering
- 連結：https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90

#ClaudeCode #TokenOptimization #ModelRouting #Spotify #LLMOps #AIAgents #DeveloperProductivity #MCP #CostOptimization #GeminiFlash
