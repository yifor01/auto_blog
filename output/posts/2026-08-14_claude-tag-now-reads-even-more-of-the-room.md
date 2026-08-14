---
title: Claude Tag now reads even more of the room
source: Claude Blog
url: https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room
model: claude-code/sonnet
generated_at: '2026-08-14T07:20:18.091480'
pinned: true
---

📌 Claude Tag 學會讀懂整個對話串，而不只是單一訊息

TL;DR：Claude Tag 現在能綜合整個 Slack 頻道脈絡判斷是否該主動發言，準確度提升約 30%。

兩位工程師在同一個 Slack 頻道裡各自追查同一個 bug：一人提出理論，另一人貼出證據，卻誰都沒空把兩者兜在一起。過去的 Claude Tag 只會逐則訊息判斷，兩則訊息單獨看都「與己無關」，於是它什麼都不做——即使把兩則放在一起看，答案已經呼之欲出。

🤔 **舊版的盲點：一次只看一則訊息**

Anthropic 說明，先前 Claude Tag 由一個輕量分類器負責決策，每則新訊息都被獨立判斷「要不要回應」，看不到訊息與訊息之間的關聯。

🧩 **從被動回應到主動判斷的四種動作**

拿掉分類器後，Claude Tag 改用整個頻道的脈絡、自身記憶，以及使用者給的常設指令來決策，可執行以下四種動作之一：

- **直接回覆**：答案簡短、可驗證，且頻道裡尚無人提過。
- **開一個討論串深入處理**：訊息值得投入真正的時間。
- **併入既有工作**：這則訊息與 Claude 手上正在進行的工作相關。
- **保持沉默**：沒有需要它插手的地方。

在前述兩位工程師的例子中，Claude Tag 即使沒被 @ 提及，也能看出理論與證據之間的關聯，主動開啟討論串並把兩人都拉進來調查——動作範圍仍受限於使用者設定的權限、工具與範疇。討論串之間也不再各自孤立：當其中一人稍後貼出更新，會被正確歸入對應的工作串，兩個原本各自獨立的調查若其實是同一個 bug，也會被連結起來。

📊 **判斷準確度提升約 30%**

Anthropic 表示，這次更新讓 Claude 判斷「該不該主動回應」的準確度提升約 30%，且不會增加額外費用；雖然保留更多脈絡會提高 Claude Tag 的用量，但這部分不計入任何方案的用量或花費上限。

💡 **懂得什麼時候該閉嘴，也懂得什麼時候該裝睡**

Anthropic 團隊用一套依「回應是否有用」「Claude 有多少把握」「是否有更適合回答的人」等原則構成的評分標準，來持續評判 Claude 在各頻道的發言選擇。Claude 也會像人類使用 Slack 一樣，密切關注部分頻道、對其他頻道逐漸降低關注度；若在某頻道裡連續判斷「無需插話」，它會進入類似「睡眠」的狀態，直到被 @ 提及才立刻甦醒。使用者也能用白話文直接下指令，例如「除非被標記，否則不要在這裡回應」或「只要跟部署流程有關都可以主動回覆」；任何頻道成員也可以直接關閉「自動回應」功能。

🎯 **實務啟示**

對已在使用 Claude Tag 的團隊來說，這次更新代表可以更放心地把它放進活躍度高、跨話題交錯的頻道，而不必擔心它漏接跨訊息的關聯，或反過來變成打擾對話的「話癆」。若團隊尚未使用，可先從一個頻道開始，觀察它主動加入對話的判斷是否符合預期，再逐步用白話指令調整敏感度。此功能現已對 Claude Teams 與 Enterprise 客戶開放。

🔗 **來源**
- 標題：Claude Tag now reads even more of the room
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room

#Anthropic #ClaudeTag #Slack #AIAgent #ProductivityTools #EnterpriseAI #TeamCollaboration #AIAssistant #WorkflowAutomation #ConversationalAI
