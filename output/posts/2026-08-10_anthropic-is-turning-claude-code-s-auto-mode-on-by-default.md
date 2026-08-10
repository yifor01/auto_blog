---
title: Anthropic is turning Claude Code’s auto mode on by default
source: TechCrunch AI
url: https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/
model: tencent/hy3:free
generated_at: '2026-08-10T07:07:21.374366'
score: 62
---

📌 【Anthropic 重大更新】Claude Code 開啟「自動模式」預設值：讓 AI 替你做決定

TL;DR：Claude Code 將於 8 月 14 日起對 Pro、Max 與 Team 用戶預設開啟 Auto mode，提升開發效率。

當 AI 助手不再每一步都徵詢你的同意，開發流程會變得更順暢，還是會失控？Anthropic 正準備迎接這個轉折點。

🤔 **從「詢問許可」轉向「自動執行」**

Anthropic 宣布，從 8 月 14 日開始，Pro、Max 與 Team 帳戶在使用 Claude Code 時，將預設開啟 Auto mode（自動模式）。

在以往的模式中，AI 每執行一個步驟都需要人類點擊確認；但在 Auto mode 下，除非該動作被判定為「不可逆（irreversible）」、「具破壞性（destructive）」或「針對環境外部的操作（aimed outside your environment）」，否則 Claude Code 將直接推進流程，不再停下來詢問。

📊 **數據顯示：自動化比人工審核更安全？**

這項改動背後有一個令人意外的研究結果。根據 Anthropic 對 1,053 位付費測試者的研究顯示：

- **Auto mode 表現**：能成功攔截 89% 的有害行為。
- **人工審核表現**：僅能攔截 13.6% 的有害行為。

研究指出，這可能是因為「人工審核容易變成一種習慣」——在 Claude Code 的測試中，使用者對權限請求的核準率高達 97%，這意味著人類往往只是機械式地點擊「允許」，反而失去了審核的實際意義。

🧩 **強化安全性：防止資料外洩與指令注入**

為了降低自動化帶來的風險，Anthropic 表示已加入多項安全功能，包括：
- Prompt injection（指令注入）篩選機制。
- 可自定義的 Hard deny rules（強制拒絕規則），用以防止資料外洩（data exfiltration）等問題。

🎯 **實務啟示**

對於依賴 AI 進行開發的工程師而言，Auto mode 雖然能大幅提升開發速度，減少頻繁點擊確認的干擾，但仍需善用「自定義拒絕規則」來確保敏感資料的安全。

🔗 **來源**
- 標題：Anthropic is turning Claude Code’s auto mode on by default
- 作者／機構：Anthony Ha @ TechCrunch
- 連結：https://techcrunch.com/2026/08/09/anthropic-is-turning-claude-codes-auto-mode-on-by-default/

#Anthropic #ClaudeCode #AI #SoftwareEngineering #Productivity #Automation #LLM #CodingAssistant #SoftwareDevelopment #TechNews
