---
title: 'Meet TokenEconomizer: Microsoft’s Plugin That Cuts Coding Agent Costs by Up
  to 30.9%'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/
model: claude-code/sonnet
generated_at: '2026-10-30T21:36:01.037848'
score: 102
---

📌 TokenEconomizer:不碰模型權重,靠學習歷史 session 就把 Coding Agent 成本砍掉三成

TL;DR:微軟與 UC Berkeley 開源外掛,讓 Coding Agent 從重複任務裡自動省錢。

每次 coding agent 開新的回合,系統提示、所有載入的工具 schema、完整對話歷史都要重新計費一次。這筆隱性成本平時很容易被忽略,微軟研究院與 UC Berkeley 的團隊決定把它量化,再做成一個外掛直接解決。

🤔 **先把浪費找出來,再決定怎麼修**

研究團隊先用 Claude Code 搭配 Opus 4.8,在 6 個 repository 裡剖析了 60 個 SWE-Bench 任務,確認了前述「每回合重新計費系統提示、工具 schema 與完整歷史」正是重複出現的成本浪費來源。他們也試過三種現成的開源策略:RTK、Serena,以及 Aider 的 RepoMap,結果沒有一種在所有情境下都更省錢,三者在 Django 上都能降低成本,卻同時在 SymPy 上把成本推高,顯示單一固定策略難以通用。

🧩 **把 agent 當黑盒子,從提示、工具、事件流三個切入點動手**

TokenEconomizer 是一個不碰模型權重、不碰 agent 程式碼的外部控制器,目前支援 Claude Code、Codex、GitHub Copilot CLI 與 Pi。它會針對每個 repository 維護一份狀態,這份狀態由已完成的任務軌跡(trace)累積而成,並在每個新任務開始前,透過提示內容、工具設定與事件流三個管道套用對應的策略。

具體機制上,一個 LLM proposer 會把 trace 摘要轉換成一條條單行事實(例如「這個 repo 實際跑測試的指令是什麼」),每條事實都附帶正規表示式(regex)偵測器,之後不需要再呼叫模型就能檢查新的 trace 是否符合。一條事實要進入系統提示,必須在「修改檔案不重疊」的任務上累積 3 次確認,且需求命中率至少維持 0.4 以上;一旦出現矛盾,直接扣抵 5 次確認,讓錯誤的事實很快被淘汰。

工具層面,shell、read、write、edit 這幾個基本工具永遠保留;其他工具若連續 3 個任務都沒被用到,或被 LLM 判斷為不相關,就會被遮罩起來,但完整工具目錄每 5 個任務會重新稽核一次,避免永久誤判。另外,系統會學習一個「回合預算」,設定為過去成功任務回合數的第 90 百分位乘以 1.25 倍;當低成本的規則檢查發現重複失敗或密集錯誤時,再交給一個 LLM 判官以 0.7 以上的信心門檻判斷 agent 是否卡住,卡住的 agent 會先被重新導向一次,若問題再次出現就直接停止。

以 Django 搭配 Claude Code 為例,文中提到第二個任務的首次請求提示 token 數,從 43,351 降到 16,295,是一個相當直觀的具體縮減案例。

📊 **277 個 SWE-Bench 任務,5 種 agent-model 組合都更省錢**

在 277 個 SWE-Bench 任務、5 種 agent-model 設定下,TokenEconomizer 把平均成本降低了 18.4% 到 30.9%,且在其中 4 組設定裡 Pass@1 還同步提升(相較之下,單純調低模型的推理努力程度雖然也能省錢,卻會讓 Pass@1 掉 1.8 到 10.3 個百分點)。對照組的 RTK 在 30 個 repository × 設定組合裡有 12 格反而讓成本上升,RepoMap 則是 15 格。

省錢效果會隨任務次數累積:大多數 repository 在最初幾個任務時成本其實更高(因為控制器還在學習狀態),但到第 6 個任務之後全部變得更便宜。單獨拆解各機制在 Claude Code 上的貢獻:工具裁剪(tool pruning)省下 13.2% 到 17.7%,micro-skills 省下 11.8% 到 14.3%,迴圈防護(loop guard)省下 5.4% 到 7.1%。這套方法也在 SWE-Bench 之外驗證過:Web-Bench 省下 16.0% 到 21.2%,CredData 省下 16.5% 到 19.6%,ReposVul 只省下 6.4% 到 9.3%(作者解釋是因為原本任務就較短,可砍的空間本來就少)。

🎯 **實務啟示**

TokenEconomizer 的安裝方式不複雜:只要有 Claude Code、Codex、GitHub Copilot CLI 或 Pi 其中之一,加上 Python 3.10 以上版本即可。以 Claude Code 為例,把它加成 marketplace 後執行 `claude plugin install tokeneconomizer@tokeneconomizer` 即可啟用,學習到的資料會留在本機的 `~/.tokeneconomizer`。預設啟用工具裁剪與迴圈防護,micro-skills 則預設關閉(因為它的 proposer 本身要額外呼叫模型,有成本)。對任何在同一個 repository 上長期跑 coding agent 的團隊來說,這是一個不需要改 agent 程式碼、也不用換模型,就能隨任務次數增加逐步降本的現成選項,尤其適合重複性高、repo 固定的 CI/維運場景。

⚠️ **限制**

效果需要時間累積,初期任務反而可能更貴;而在任務本身就偏短、歷史與工具 schema 本來就沒多少冗餘的場景(如 ReposVul),省錢幅度明顯縮水。micro-skills 這類涉及額外模型呼叫的機制也需要權衡「省 token 但多付模型呼叫費用」的淨效益。

🔗 **來源**
- 標題:Meet TokenEconomizer: Microsoft's Plugin That Cuts Coding Agent Costs by Up to 30.9%
- 作者/機構:Asif Razzaq(MarkTechPost);研究團隊來自 Microsoft Research 與 UC Berkeley
- 連結:https://www.marktechpost.com/2026/10/30/microsoft-tokeneconomizer-coding-agent-cost-control/

#TokenEconomizer #CodingAgent #LLMCostOptimization #ClaudeCode #SWEBench #OpenSource #MicrosoftResearch #AIAgents #PromptEngineering #DevTools
