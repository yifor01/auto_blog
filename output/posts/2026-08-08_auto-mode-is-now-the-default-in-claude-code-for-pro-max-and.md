---
title: Auto mode is now the default in Claude Code for Pro, Max, and Team plans
source: Claude Blog
url: https://claude.com/blog/auto-mode-default-in-claude-code
model: tencent/hy3:free
generated_at: '2026-08-08T06:41:53.644185'
pinned: true
---

📌 【Anthropic】Claude Code 預設開啟 Auto mode：比人工審核更安全，且能提升 25% 的開發效率

TL;DR：Claude Code Pro/Max/Team 用戶將預設進入 Auto mode，透過分類器取代人工逐一確認，安全性與效率雙增。

當開發者每天需要處理數百個權限確認時，「點擊同意」往往會變成一種肌肉記憶。Anthropic 發現，開發者在面對 Claude Code 的權限請求時，有 97% 的情況會直接點擊同意。這種習慣性的操作，反而讓錯誤的指令更容易溜進開發環境。

為了打破這種「審核疲勞」，Anthropic 宣布從 2026 年 8 月 14 日起，Pro、Max 與 Team 計畫的 Claude Code 新對話將預設開啟 **Auto mode（自動模式）**。

🧩 **Auto mode 的運作機制：用分類器取代「點擊確認」**

Auto mode 的核心設計理念，是在「減少干擾」與「確保安全」之間取得平衡。它不再針對每個工具調用（tool call）跳出視窗詢問，而是透過一個專門的分類器（classifier）來進行路由：

- **攔截機制**：分類器會針對「不可逆」、「具破壞性」或「超出當前環境範圍」的指令進行攔定。
- **自動處理**：當分類器攔截到風險指令時，Claude 通常會自動尋找更安全的執行路徑；若無法繼續，則會直接詢問使用者。
- **退回機制**：若在單次對話中連續遇到 3 次攔截，或整個對話中累積 20 次攔截，系統會自動退回到手動確認模式（manual approvals）。
- **成本優化**：為了推廣此功能，Anthropic 已決定不再向 Pro、Max 與 Team 用戶收取分類器運行的額外 Token 費用。

📊 **實驗數據：Auto mode 在安全性上勝過人類審核**

Anthropic 進行了大規模的對照實驗（包含內部紅隊演練、第三方滲透測試及 1,053 位專業測試者的受控研究），結果顯示 Auto mode 在安全性上表現優異：

- **攔截率對比**：在針對危險指令的測試中，人類測試者僅能捕捉 13.6% 的危險指令；而 Auto mode 的攔截率高達 89%。
- **疲勞度影響**：隨著對話進行，人類的攔截能力會隨之下降（從 17% 降至 5%），但 Auto mode 的攔截率能保持穩定。
- **非預期傷害**：在分析實際生產環境的紀錄時，手動確認模式中出現「非使用者明確要求之傷害行為」的機率，是 Auto mode 的兩倍以上。

💡 **對開發流程的實際影響：更高的生產力**

Auto mode 不僅僅是為了安全，它更釋放了模型處理長時程任務的能力。

- **任務連續性**：對於像 Claude Opus 5 這樣專為長時間工作設計的模型，Auto mode 讓其能長時間自主執行大型任務，無需頻繁等待人工點擊。
- **產出量提升**：根據數據，使用 Auto mode 的 Teams 與 Enterprise 用戶，其 Pull Requests (PR) 的提交量增加了約 25%。

⚠️ **限制與部署建議**

目前 Auto mode 仍採取「選擇性加入（opt-in）」策略給予以下平臺，以供管理員審核：
- Claude Enterprise
- Claude API
- AWS Amazon Bedrock
- Google Cloud Agent Platform
- Microsoft Foundry

若您是 Enterprise 管理員，可以透過管理設定來預設開啟 Auto mode。此外，若您在 Claude Code 中設定了極度寬鬆的規則（例如 `python:*` 允許任何 shell 指令），這些規則在 Auto mode 下會被暫時擱置，以確保分類器能發揮作用。

🎯 **實務啟示**

對於追求開發效率的工程團隊來說，Auto mode 的轉向代表 AI 代理（AI Agent）正從「指令執行者」轉向「自主工作者」。開發者應從「逐一審核指令」的思維，轉向「定義環境邊界與安全規則」的思維。

🔗 **來源**
- 標題：Auto mode is now the default in Claude Code for Pro, Max, and Team plans
- 連結：https://claude.com/blog/auto-mode-default-in-claude-code

#AI #ClaudeCode #Anthropic #LLM #SoftwareEngineering #AIAgent #Productivity #DeveloperTools #MachineLearning #CodingAssistant
