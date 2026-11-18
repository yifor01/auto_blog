---
title: 'Anthropic Adds Code Mode to Claude Code: Claude Now Chains Tool Calls in JavaScript'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/17/anthropic-claude-code-code-mode-javascript-tool-calls/
model: claude-code/sonnet
generated_at: '2026-11-18T23:45:22.509201'
score: 86
---

📌 【Anthropic 新功能】Claude Code 讓 Claude 自己寫 JS 串多步工具呼叫

TL;DR：Claude Code 新增實驗性 Code Mode，讓 Claude 用一段 JavaScript 串連多個工具呼叫，省下來回溝通的 token。

如果 Claude 每做一步操作都要停下來、把結果讀一遍再決定下一步，多步驟任務的 token 消耗很容易失控。Anthropic 的解法很直接：讓 Claude 自己寫程式碼，一次串完整段邏輯。

🤔 **背景：逐步呼叫工具，代價是每一步都要讀一次結果**

在沒有 Code Mode 的情況下，Claude Code 執行多步驟任務時，Claude 會直接發出每一個 Bash、Read 或 Edit 呼叫，並且在選擇下一步之前讀完每一次呼叫的結果。這種模式對於單一、獨立的操作沒問題，但遇到「連續好幾個相關步驟」的任務時，每一次往返都要把中間結果餵回模型，累積起來的 token 成本會很高。

🧩 **Code Mode 怎麼運作**

Anthropic 在上週發佈的 Claude Code v2.1.323 中，把 Code Mode 做成一個實驗性、預設關閉（opt-in）的功能。開啟後，Claude 會寫一段 JavaScript，由 Claude Code 在你的 session 中執行。根據官方文件，這段程式碼可以：

- 平行執行多個指令
- 把一個呼叫的結果直接餵進下一個呼叫
- 只回傳 Claude 真正需要讀的輸出內容，而不是整段原始結果

官方給的範例是：一段程式碼同時完成「調高重試上限、找到目標檔案、修改它、再執行測試」。在對話介面中，你看到的是工具呼叫本身（例如 diff），而不是這段程式碼；要查看程式碼，需按 Ctrl+O 開啟 transcript viewer，展開被收合的 Code 那一行。

啟用方式是在 shell 中設定環境變數 CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1，或寫進 ~/.claude/settings.json 的 env 區塊。第一次啟用時，Claude Code 會要求確認（選擇「Yes, turn on Code Mode」），重啟後會顯示「Code Mode (experimental) is on」。值得注意的細節：session 要恢復 Code Mode，必須該變數仍為 1；只要任何地方把它設為 0，就會關閉，即使其他地方設為 1 也不例外。管理員可以用 managed settings 中的 0 在組織層級封鎖它，但無法反過來強制開啟。

權限與安全機制並未因 Code Mode 而鬆綁：程式碼內的每一個工具呼叫仍會經過原本的 deny／ask 規則，也會以該工具原本的名稱（例如 Bash）觸發 PreToolUse hook。文件也提醒 hook 作者要檢查指令的每一部分，因為像 git push 這種操作，實際傳進來的字串可能是 cd 'app' && git push 這樣的組合指令。要檢視程式碼本身,需比對 REPL 工具並讀取 tool_input.code。執行時間上，若 Claude 處於等待狀態（包含卡在權限確認），程式碼會在 10 分鐘後停止；若在背景執行，則可持續長達 2 小時，期間你仍可以繼續對話——但背景執行需要 session 處於 auto 或 bypassPermissions 模式。

💡 **這個點子不是 Anthropic 先想到的**

「Code Mode」這個詞最早是 Cloudflare 在 2025 年 9 月 26 日提出的，其 Agents SDK 把 MCP schema 轉換成一個在 V8 isolate 中執行的 TypeScript API。Anthropic 後續發表了「code execution with MCP」，其中一個案例顯示 token 用量從 150,000 降到 2,000，省下 98.7%。Anthropic API 層也有對應功能 Programmatic Tool Calling（用 Python 實作），在複雜研究任務上把平均用量從 43,588 token 降到 27,297 token。Claude Code 的 Code Mode，則是把同樣的模式套用到 CLI 自身的工具呼叫上。

📊 **官方沒給數字，但有第三方量到的對比**

文件本身並未附上 Claude Code Code Mode 的具體 token 節省數字。有一項獨立測試回報：開啟 Code Mode 時系統工具的 context 用量為 11.1k token，未開啟則為 24.6k token——這只是單一第三方的量測結果，應謹慎看待,不代表普遍情況。

⚠️ **目前仍是實驗性功能**

Code Mode 目前仍標示為 experimental，需手動 opt-in 才能使用，且官方並未公開正式的效能或節省數據，使用前建議先在非關鍵任務上驗證其行為與 hook 相容性。

🎯 **實務啟示**

如果你的 Claude Code 工作流程經常是「連續好幾個相關的工具呼叫」（例如改檔案、跑測試、依結果再改一次），開啟 Code Mode 值得一試，但要先確認團隊的 PreToolUse hook 是否只檢查了指令的「頭」而忽略了組合指令（像 cd x && git push）的其他部分，避免安全規則被繞過。

🔗 **來源**
- 標題：Anthropic Adds Code Mode to Claude Code: Claude Now Chains Tool Calls in JavaScript
- 作者／機構：Michal Sutter（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/17/anthropic-claude-code-code-mode-javascript-tool-calls/

#Anthropic #ClaudeCode #CodeMode #AIAgents #DeveloperTools #TokenEfficiency #MCP #LLMTooling #AgenticAI #SoftwareEngineering
