---
title: Introducing Personal Finance in Claude
source: Claude Blog
url: https://claude.com/resources/articles/introducing-personal-finance-in-claude
model: claude-code/sonnet
generated_at: '2026-11-05T22:50:44.807468'
pinned: true
---

📌 Claude 新增個人理財功能，用聊天問清楚銀行帳戶裡的錢

TL;DR：Anthropic 讓 Claude 讀取你的銀行與信用卡帳戶，用一般口語問錢去哪了。

月底手頭緊，發薪日還有十天，你打開三個銀行 App 想把帳算清楚，卻只看到一堆流水帳，還得自己動筆分類加總。Anthropic 這次把這個麻煩事直接交給 Claude 處理。

🤔 **為什麼要做這件事**
查帳這件事本來要跨多個 App 手動比對、自己做加總與分類，才能回答「我這個月花多少」「還剩多少可以用」這類問題。Personal Finance 把這個流程變成一句自然語言的問答。

🧩 **唯讀存取，透過 Plaid 連接銀行**
帳戶是使用者自己透過 Plaid（一家把 App 與銀行串接起來的服務）登入銀行並同意授權後才會連接，Claude 本身不會要求也看不到銀行密碼。存取範圍是唯讀，Claude 不能移動、管理或投資資金，也不提供自家的信用卡、貸款或儲蓄帳戶，介面上沒有廣告或贊助推薦。

📊 **實際問答長什麼樣子**
素材給的範例：問「這個月錢花到哪了」，Claude 會把所有已連接帳戶的支出加總並分類，算出 $4,309.37，其中超過一半是房租與水電，$1,024.51 是餐飲。接著可以繼續追問「比平常多嗎」，Claude 會比對過去幾個月，指出是某個會員訂閱續約造成的；再問「發薪日前還剩多少」，Claude 會列出發薪日前會從帳戶扣款的四筆款項，算出剩下 $1,393.22。如果問「有什麼不對勁的地方」，Claude 會跨帳戶檢查，點出容易漏看的重複扣款、意外手續費，或是悄悄漲價的帳單。更大範圍的問題像「我花得比賺得多嗎」或「什麼是 APR，今年因此付了多少利息」，Claude 會先解釋名詞再算出實際金額，也可以要求生成週支出圖表、到期日歷或自訂儀表板。

💡 **資料看得到多少**
對於使用者選擇連接的帳戶，Claude 能看到銀行名稱、帳戶名稱／類型／末四碼、餘額與信用額度，以及最多兩年的交易紀錄。在 Personal Finance hub 內的對話不會用於模型訓練，帳戶可以隨時取消連接，取消後 Claude 就看不到該帳戶的資料。

⚠️ **目前的限制**
Claude 的回答可能出錯，重要數字建議回頭核對銀行官方紀錄；這個功能不是用來提供投資建議的。目前是 beta 階段，僅在美國的 Pro、Max、Ultra 方案開放。

🎯 **實務啟示**
這是把唯讀金融 API（Plaid）包裝成自然語言介面的一個落地案例，權限邊界切得很清楚：只整合資訊、不做任何決策或操作。做 agent 產品設計時，這種「唯讀 + 解釋 + 不建議」的收斂範圍，是在敏感領域（金融、醫療）降低風險的一種可參考模式。

🔗 **來源**
- 標題：Introducing Personal Finance in Claude
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/introducing-personal-finance-in-claude

#AI #Anthropic #Claude #PersonalFinance #Fintech #LLM #AIAssistant #DataPrivacy #Plaid #ConversationalAI
