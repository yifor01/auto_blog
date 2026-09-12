---
title: Can LLMs Engineer Their Own Agent Harness? ByteDance Seed’s HarnessDev Says
  Only 34 of 64 Changes Generalize
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/11/can-llms-engineer-their-own-agent-harness-bytedance-seeds-harnessdev-says-only-34-of-64-changes-generalize/
model: claude-code/sonnet
generated_at: '2026-09-12T19:32:19.861807'
score: 86
---

📌 LLM能寫出好用的Agent Harness嗎？64次修改只有34次真的有效

TL;DR：ByteDance Seed團隊用HarnessDev實測LLM自建agent框架的能力，結果顯示自我改良的成果多半無法穩定泛化。

同一組模型權重，換一個執行框架，成績就能從35.2%跳到49.6%。這不是模型變強了，而是包在模型外面的那層程式碼變了。這正是ByteDance Seed、新加坡科技設計大學、喬治亞理工、M-A-P與TokenWave.AI團隊想解決的問題：如果框架本身這麼重要，LLM能不能自己把它寫好？

🤔 **多數評測都固定了框架，HarnessDev反過來評測框架本身**

所謂agent harness，指的是包裹在模型外層的執行迴圈、工具呼叫、上下文管理、狀態保存、錯誤恢復與驗證機制。以Terminal-Bench 2.1排行榜為例，GPT-5在Terminus 2框架下只解出35.2%的任務，換成Codex CLI卻能拿到49.6%，模型權重完全相同。多數benchmark只評測模型輸出的答案，卻把框架這個變數鎖死。HarnessDev反其道而行：受測的不是答案，而是模型親手寫出來、可實際運行的harness。

🧩 **兩階段流程：先從零打造，再用回饋自我修訂**

在Creation階段，每個「創造者」模型拿到相同的弱起點：只有被動的檔案、搜尋、行程操作原語，加上結果與軌跡寫入器，沒有執行迴圈、規劃器、驗證器、重試或停止規則，不修改的話在任何任務上都是0分。創造者拿到任務族群規格、一份簡短的設計教學，以及1到3個開發用案例，據此打造完整harness，並在接觸隱藏任務前將其凍結。

進入Evolution階段後，創造者從自己凍結的Creation版harness出發，依據SWE-bench Pro固定100題與Terminal-Bench 2.1全部89題的執行回饋進行修訂。每個正式候選版本必須成對完成兩項評測，總預算為10個版本對，最多穿插2次五題探測。所有正式版本最後都會在創造者從未見過的630個held-out SWE-Pro實例上重新打分，評分同時看能力（任務成功率）與效率（僅計執行者token，不計創造者花費的token）。

研究團隊測試了6個創造者LLM：Opus 4.8、GPT-5.5、Gemini 3.1 Pro、DeepSeek V4 Pro、Qwen 3.7 Max與Seed 2.0 Pro，運行環境為Claude Code 2.1.177（GPT-5.5則用Codex 0.144.3）。Creation階段涵蓋4個領域、5個benchmark，共2,207個實例：SWE-bench Pro公開集（731題）、Terminal-Bench 2.1（89題）、MLE-bench（75題）、EQ-Bench3（46題）、BrowseComp（1,266題）。每個創造者為每個benchmark打造3個harness，取avg@3。

📊 **程式碼寫得多不代表分數高，大量產出的機制根本沒被觸發**

在Self-Eval（用創造者自己的模型執行harness）下，Opus 4.8平均分67.8最高，但相較人類工程師手寫的參考基準86.2仍有明顯差距（SWE-Pro、Terminal-Bench與BrowseComp的參考數字取自OpenAI GPT-5.6報告的外部結果，並非重新跑出來的）。

程式碼量與品質沒有關聯：18個code harness共新增17,111行程式碼，但Gemini新增最少（僅1,006行）卻在Terminal-Bench上領先。自我測試數量與分數幾乎不相關（Spearman係數0.13至0.26），修訂呼叫次數的相關性則到0.57。更值得注意的是，許多生成出來的機制根本是死碼：108個程式元件實例中，有18個從未在實際運行中觸發，且全部集中在狀態與記憶模組——11個harness定義了State類別，但26,679條執行軌跡中沒有出現任何一次checkpoint事件；587個寫入功能中有124個是死碼。

MLE-bench上的token用量差距高達19倍：GPT-5.5用2,930萬token拿到19.1%的獎牌率，DeepSeek V4卻用了2億840萬token才拿到19.6%。把執行者換成Gemini後，排名大洗牌：Qwen在BrowseComp上多拿17.6分、MLE-bench多拿12.9分，但Opus 4.8的SWE-Pro分數從69.3暴跌到33.0，部分原因是它的harness把120步的步數上限寫死在原本針對的執行者身上；Opus的搜尋harness重複查詢率也從10.1%飆升到88.2%。

9條演化路線（5條自身執行環境、4條固定用Gemini執行）共產生73個正式版本與64次相鄰版本切換。5個自身執行環境的創造者全部在held-out任務上進步，幅度從+1.43到+4.44分（平均+3.11）；但固定用Gemini執行時，只有Opus進步，GPT-5.5反而退步10.32分。進步過程也不是單調的：64次切換中，8次兩項benchmark同時退步，16次單項退步，27次的進步落在雜訊區間內，只有2次是明確的正向證據——單一次commit的分數波動幅度可達正負4.75分。回饋分數與held-out分數方向一致的比例只有53.1%（34/64），9個宣告的最終版本裡，只有2個真的是held-out表現最好的版本。169個新增函式或類別中，25個從未被呼叫過。

團隊記錄下最明確的一次成功：Opus 4.8注意到100次執行中有99次回報成功，但實際只有48次真正通過，追查後發現是過早宣告完成，於是加上了完成閘門機制。相對地，失敗診斷是整個流程中最弱的一環——專門設計的軌跡查詢介面全程只被呼叫過兩次。

⚠️ **自我改良的訊號本身不可靠**

這項研究最重要的發現或許是：無論是自我測試次數、程式碼量,還是修訂過程中的回饋分數，都不足以預測harness在未見任務上的真實表現，模型很容易把大量心力花在不會被實際觸發的機制上。

🎯 **實務啟示**

如果你的團隊也在讓agent自己迭代自己的執行框架，這篇研究提醒你：不能只看訓練過程中的回饋分數或自我測試結果來判斷是否要合併變更，一定要保留獨立的held-out評測；同時要定期檢查生成的程式碼裡有多少是從未被觸發的死碼，這往往比表面的分數更能反映harness是否真的可靠。

🔗 **來源**
- 標題：Can LLMs Engineer Their Own Agent Harness? ByteDance Seed's HarnessDev Says Only 34 of 64 Changes Generalize
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/11/can-llms-engineer-their-own-agent-harness-bytedance-seeds-harnessdev-says-only-34-of-64-changes-generalize/

#AgentHarness #LLMAgents #ByteDanceSeed #SWEBench #TerminalBench #AIEvaluation #SelfImprovingAI #AgenticAI #MLResearch #AIAlignment
