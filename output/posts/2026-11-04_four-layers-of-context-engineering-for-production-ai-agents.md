---
title: 'Four layers of context engineering for production AI agents: How Deep Insight
  applies them in working code'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/four-layers-of-context-engineering-for-production-ai-agents-how-deep-insight-applies-them-in-working-code/
model: claude-code/sonnet
generated_at: '2026-11-04T22:47:12.598817'
score: 98
---

📌 四層 context engineering,AWS 實測砍掉 95% 的 token 消耗

TL;DR：AWS 以開源專案 Deep Insight 示範四層 context engineering 落地,寫入執行工具與按需載入 skill 大幅省下 token。

「200K 的 context window 聽起來很大」,直到一個真實任務在幾分鐘內就燒光大半。AWS 這篇文章用一個開源多代理系統的實際程式碼,拆解出可以直接套用的四層解法。

🤔 **一個看似簡單的請求,十五分鐘燒掉十五萬 token**

文中舉了一個例子:使用者只是要求「分析銷售資料並產出 DOCX 報告」,但這個任務實際上要走過資料載入與探索(5 分鐘)、依類別進行銷售分析(3 分鐘)、產生五張時間序列圖表(10 分鐘)、統計驗證(3 分鐘)、最終報告生成(5 分鐘)五個階段,合計消耗超過 15 萬個 token、耗時 15 分鐘。如果把整個流程塞進單一 context,問題會接連浮現:視窗中途溢出、過時的舊內容拖累模型表現、出錯時得重跑整條 pipeline。Anthropic 在 2025 年 9 月的文章中將這個現象稱為「context rot」:隨著 context 中的 token 數增加,模型從中準確回憶資訊的能力會下降。更麻煩的是,按 token 計費的架構下,context 越肥,成本也越高。

🧩 **第一層:把每個子代理關進自己的 context,只傳壓縮後的結果**

Deep Insight 是一套基於 Strands Agents SDK 與 Amazon Bedrock AgentCore 打造的開源多代理資料分析系統,也是本文的參考實作。第一層的做法是讓每個專職 agent 擁有自己獨立的 context window,只把壓縮後的結果傳給協調者(orchestrator)。Deep Insight 用 Coordinator、Planner、Plan Reviewer、Supervisor 與一組工具型 agent(Coder、Validator、Reporter、Tracker、Auditor)組成層級結構。單一 agent 架構下,從使用者請求到資料探索、分析、圖表生成、驗證、報告產出的所有資訊都會疊加在同一個 context 裡,很容易超出視窗上限;而給每個 agent 獨立 context 後,即使是耗用最多的 Coder agent,總 token 量也能控制在 2.5 萬以內。

隔離的關鍵在於盡量縮小代理之間共享的資訊量。Deep Insight 用一個叫 `shared_state` 的 Python 字典,只儲存固定四項內容,並用統一的 `CLUES_FORMAT` 格式傳遞壓縮後的核心結果,而不是把每個 agent 數萬 token 的完整對話記錄原封不動傳下去。這個模式對應到 Anthropic《How We Built Our Multi-Agent Research System》一文中描述的 orchestrator-worker 模式:一個主導 agent 把任務分派給專職子代理,各自只在自己的 context 內工作。文中也提到,開發者不必自己從零實作這層隔離,Strands Agents SDK 內建的 agents-as-tools 模式就能在框架層級提供這種隔離。

🧩 **第二層靠提示詞限流,第三層把重內容搬到檔案系統**

單靠第一層的隔離還不夠:即使 context 互相獨立,只要某個 agent 回覆過長,照樣會把協調者(Supervisor)的 context 撐大。第二層的做法是用提示詞限制每個 agent 的輸出量,Deep Insight 給每個 agent 的 system prompt 都設定最大回應 token 數,並要求統一的簡潔格式,呼應 Anthropic《Writing Effective Tools for Agents》中建議工具提供 CONCISE 或 DETAILED 回應選項的做法,只是把同樣的概念套用到 agent 層級。

Coder agent 的提示詞更明確規定「變數不會在腳本之間保留」,每份腳本都必須自帶完整的 import 並直接重新載入資料,提示詞裡也附上正確與錯誤的範例對照。這條規則背後的 context engineering 考量是:如果允許引用前一份腳本的變數,agent 就必須「記得」先前的對話,導致舊程式碼必須持續留在 context 中;而要求腳本自包含(self-contained),舊程式碼就可以安全地從 context 移除。Supervisor 的提示詞還包含一條規則:「在目前 agent 清單上所有項目都打勾之前,不要進到下一個 agent」,這類判斷需要 Supervisor 綜合計畫內容與 Tracker 的更新資訊,難以單純用程式碼表達,因此寫進提示詞裡。

但當 Coder agent 產出上百行 Python 程式碼時,這些程式碼本身一樣會進入 context,即使提示詞要求「簡潔回覆」,程式碼內容也無法被簡化。第三層的做法是透過工具設計把重內容搬出 context,存到檔案系統。文中提到,傳統做法是用分開的「寫入檔案」與「執行」兩個工具,這樣每份腳本都會讓 100 行程式碼直接進入 context,累積下來輕易超過 1000 行。Deep Insight 改用單一的「寫入並執行」工具,根據文章開頭的量化結果,這個改動讓每份腳本加入 context 的 token 量減少約 95%;另外搭配「按需載入 skill」(而非把所有 skill 說明都塞進系統提示詞),系統提示詞本身的大小也縮減了約 97%。

🎯 **實務啟示**

對正在建置生產級多代理系統的工程師來說,這篇文章提供的不是抽象原則,而是可以直接比對自己程式碼的具體模式:agent 之間是否共享了不必要的完整對話記錄?提示詞有沒有明確限制回應長度與格式?長內容(程式碼、檔案、日誌)是否真的有必要留在 context 裡,還是可以寫進檔案系統再按需讀取?Deep Insight 作為開源參考實作,這幾項改動帶來的 95% 與 97% token 節省,是在實際量化後得出的數字,值得作為自家系統重構 context 管理時的參照基準。

🔗 **來源**
- 標題：Four layers of context engineering for production AI agents: How Deep Insight applies them in working code
- 作者／機構：Yoonseo Kim, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/four-layers-of-context-engineering-for-production-ai-agents-how-deep-insight-applies-them-in-working-code/

#ContextEngineering #AIAgents #MultiAgentSystems #AWS #AmazonBedrock #StrandsAgentsSDK #LLM #PromptEngineering #AgentArchitecture #ProductionAI
