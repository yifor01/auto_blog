---
title: Make long-running agents faster with message threads
source: Claude Blog
url: https://claude.com/resources/articles/message-threads
model: claude-code/sonnet
generated_at: '2026-11-02T23:58:17.285509'
pinned: true
---

📌【Anthropic 官方發布】Message Threads 讓長對話 Agent 不用重送歷史

TL;DR：Claude Platform 新增 message threads，長對話 agent 免重送整段歷史，TTFT 中位數降約 35%。

一個 coding agent 在同一個 session 裡動輒發出上百次請求，而過去每一次請求都要把之前所有訊息與工具執行結果重新送一遍——當對話累積到數十萬 token，光是把這些內容送出去，就會在 Claude 真正開始回應前先拖慢一段時間。

🤔 **問題：每次都要重送整段對話歷史**

Anthropic 指出，隨著對話規模膨脹到數十萬 token，重送全部內容會增加 time to first token（TTFT，也就是模型開始回應前的等待時間）。這對長時間運作的 agent 尤其不利，因為對話歷史只會越疊越厚。

🧩 **做法：只送「新增的部分」＋上一輪的回應 ID**

Message threads 的機制是，第一次請求照舊送出完整對話並建立一個 thread；之後每次請求只需要附上「新增的訊息」以及前一次回應的 ID。Anthropic 會在兩輪之間把這個 thread 暫存在記憶體中，過程中是加密的，且不會寫入磁碟；若某個 thread 超過 5 分鐘沒有新請求就會過期，此時用戶端需重新送出完整對話以開啟新的 thread。

📊 **50 萬到 100 萬 token 的請求，TTFT 中位數降約 35%**

目前 message threads 已對大多數 Claude Code 使用者預設開啟。Anthropic 表示，對於 50 萬到 100 萬 token 規模的請求，TTFT 中位數下降約 35%。對話攜帶的 context 越多，message threads 能帶來的延遲改善就越明顯。

⚠️ **省的是時間，不是 token 用量**

要注意的是，雖然每次請求傳送的內容變小了，Claude 在每一輪仍然會讀取完整對話，因此 token 使用量並沒有減少，計費方式沿用標準 Claude token 費率與既有的 rate limit。換句話說，這是一項針對延遲最佳化的功能，而非省成本的功能。

🎯 **實務啟示**

Message threads 目前最適合三種情境：長時間運作的 coding agent（每次工具執行結果或檔案編輯都會疊加到對話中）、computer use agent（螢幕截圖留在 thread 裡，不需每輪重新上傳）、以及文件或圖片密集的工作流程（讓每次請求變小）。要使用的話，在 Messages API 請求中加入 thread 參數即可，目前已在原生 Claude Platform、AWS 上的 Claude Platform、Microsoft Foundry 中的 Claude，以及 Google Cloud 上由 Anthropic 管理的 Claude Models 提供公開 beta 測試。如果你手上剛好有長 session 的 agent 在跑，這是一個值得優先導入的低成本改動。

🔗 **來源**
- 標題：Make long-running agents faster with message threads
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/message-threads

#Claude #Anthropic #ClaudeAPI #AIAgents #LLM #CodingAgents #MessagesAPI #Latency #ComputerUse #APIBeta
