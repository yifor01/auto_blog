---
title: 'TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient'
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/
model: claude-code/sonnet
generated_at: '2026-11-17T00:56:40.902382'
score: 124
---

📌 讓 Coding Agent 學會「省錢」：TokenEconomizer 砍 Token 成本近三成

TL;DR：Microsoft 等機構推出開源插件，讓 coding agent 從過去工作經驗自動學會省 token，不改模型也不改 agent。

你有沒有想過，AI coding agent 每次接手同一個 repository 的任務，是不是都在「重新發明輪子」？重新摸索怎麼跑測試、載入用不到的工具、在同一個錯誤上卡關打轉——這些浪費的 token，其實是可以被記住並避免的。

🤔 **三種重複出現的浪費，現有插件各有盲點**

Microsoft Research 與 UC Berkeley、Microsoft Security 合作的研究團隊先用 Claude Code 在 SWE-Bench（真實開源 Python 專案的 bug 修復任務集）上跑了 60 個任務，依序處理同一個 repository 的多個任務後發現，有三種浪費模式會不斷重複出現。他們也測試了三個主流的開源插件，每個都內建固定的省成本策略，結果是在某些 repository 省了錢、在另一些卻沒用。這說明有效的成本控制必須因 repository 而異，不能套用同一招打天下。

🧩 **三個機制：micro-skills、工具裁剪、卡關介入**

TokenEconomizer 的做法是，每次 session 結束後讀取該次的日誌，更新它對這個 repository 的理解，再透過三個機制作用在 agent 原本就提供的介面上：

- **Micro-skills**：把 repository 特有的知識濃縮成一句話筆記。系統會先辨識跨多個 session 反覆出現的模式，等累積足夠 session 驗證過後才把筆記加進 agent 的起始上下文，若後續證據與筆記矛盾則會撤回。
- **工具裁剪（Tool pruning）**：根據歷史紀錄移除 agent 不太會用到的工具，但永遠保留執行指令與編輯檔案這類核心工具；被移除的工具之後若需要仍可恢復。
- **失敗迴圈介入（Failure-loop intervention）**：監控 agent 是否反覆卡在同一個錯誤，由一個判斷模型（judge model）決定它是真的卡住還是仍在進展。若判定卡住，就給一則建議換個方向的簡短提示；開源版插件在提示後若仍卡住，會通知開發者，而不是自行中止工作。

整個控制器的設計允許隨新證據不斷修正自己的判斷，而報告的省錢數字也已經扣除 TokenEconomizer 自身呼叫模型的成本。

📊 **277 個任務、6 個 repository，平均省 18.4% 到 30.9%**

研究團隊在 6 個 repository、5 種不同的 coding agent 與模型組合上，共測試 277 個 SWE-Bench 任務，每個 repository 都是從零開始，沒有任何先前的 session 紀錄。結果顯示 TokenEconomizer 平均降低成本 18.4% 到 30.9%，在全部 30 組 repository 與組合的配對中省最多，且沒有造成效能下降；相較之下，單純調低模型的推理強度（reasoning effort）雖然能省下類似甚至更多成本，卻伴隨明顯的效能衰退。省下的成本也會隨經驗累積而增加：早期任務可能因為系統還在學習而成本較高，但在每個 repository 中,到第六個任務時累積成本就已經低於預設值。這套方法也能延伸到其他場景，在 Web-Bench 上省下 16.0% 到 21.2%，在每次都是全新 repository 的安全稽核任務上省下 6.4% 到 19.6%。

💡 **三機制各自有效，合併使用效果最大**

三種機制單獨使用都能帶來省錢效果，但把 micro-skills、工具裁剪與失敗迴圈介入三者合併時，降低的成本最多。這也呼應了前面的觀察：成本控制需要因地制宜地組合策略，而不是依賴單一的固定規則。

🎯 **實務啟示**

TokenEconomizer 是開源插件，設計上可以搭配現有的 coding agent 運作，不需要修改底層模型，也不需要自己的 API key，學到的知識會留在開發者的機器上。對於長期維護同一批 repository 的團隊，這類「經驗驅動」的成本控制或許比單純調低模型推理強度更值得優先嘗試，因為它不犧牲任務成功率。

🔗 **來源**
- 標題：TokenEconomizer: Learning from Experience to Make AI Coding Agents More Efficient
- 作者／機構：Microsoft — Aaron J. Li, Weijia Xu, Chandan Singh, Jeevana Priya Inala, Bin Yu, Ion Stoica, Michel Galley, Jianfeng Gao
- 連結：https://www.microsoft.com/en-us/research/blog/tokeneconomizer-learning-from-experience-to-make-ai-coding-agents-more-efficient/

#AICodingAgent #TokenEconomizer #MicrosoftResearch #LLMCostOptimization #SWEBench #ClaudeCode #AgentEfficiency #OpenSource #DeveloperTools #AIAgents
