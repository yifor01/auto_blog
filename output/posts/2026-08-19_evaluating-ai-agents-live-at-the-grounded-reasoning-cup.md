---
title: Evaluating AI Agents Live at the Grounded Reasoning Cup
source: Databricks
url: https://www.databricks.com/blog/evaluating-ai-agents-live-grounded-reasoning-cup
model: claude-code/sonnet
generated_at: '2026-08-19T06:29:48.019498'
score: 101
---

📌 Stanford 用 63.3% 準確率贏了首屆企業級 AI 推理競賽

TL;DR：Databricks 首辦即時 AI 競賽測試 agent 泛化能力，平均隊伍僅 41%，顯示企業級 grounded reasoning 遠未解決。

如果一個 agent 在既有 benchmark 上表現亮眼，換一份全新的企業文件它還能撐得住嗎？Databricks 舉辦的首屆 Grounded Reasoning Cup，就是為了在真實競賽壓力下回答這個問題。

🤔 **賽制：兩個月準備，正式上場才給新題目**

比賽找來美加地區 11 支頂尖學術隊伍，分別搭配 OpenAI、Anthropic、Google DeepMind 其中一家提供模型與指導。兩個月開發期間，各隊在 Databricks 的旗艦 grounded-reasoning benchmark「OfficeQA」（設計上反映具經濟價值的企業工作流程）上開發並最佳化自己的 agent，且被要求只能使用合作實驗室的模型家族。到了比賽當天，題目換成全新發布的 OfficeQA Pro V2，用來檢驗這些改進是否真的能泛化，而不是單純過擬合在已知題目上。

📊 **平均隊伍 41%，近兩成題目全軍覆沒**

Stanford 以 63.3% 準確率奪冠，比平均隊伍高出約 22 個百分點，比前沿 agent 的離線基準高出約 35 個百分點。前三名隊伍準確率都超過 50%。然而，18.8% 的題目所有隊伍都沒能解出，顯示企業級 grounded reasoning 還有很大的進步空間。

💡 **三種奪牌路線：技能庫、速度優先、多分支驗證**

Stanford 的獲勝策略是把過往在 OfficeQA 上發現的失敗模式，逐一轉化成 Claude Opus 4.8 Claude Code agent 可重複使用的技能，包括表格定位、答案格式化、財務用語的釐清規則等，累積到比賽當天已備妥超過 100 個技能，並整合了「何時該查詢解析後的文件文字／Markdown 表示、何時該回退查原始 PDF」的判斷邏輯。他們在嘗試的 88 題中答對 57 題，居全場之冠。過程中團隊也臨場調整策略：前三輪用另一個 Claude Code agent 做驗證（重新提取中間值、檢查資料世系與單位換算等常見失誤），但只換來 2 次速度加分，因此後三輪拿掉驗證步驟以降低延遲，換來 14 次速度加分；直到最後一輪才把驗證器重新打開，靠一次重新提交修正答案，鎖定冠軍。

UMass Amherst 押注速度：以 Claude Opus 4.8 Fast 為主力模型，事先把文件語料整理成 metadata catalog 加速搜尋過濾，每題平行跑三個 agent 再由 Opus 做最終驗證選出最佳答案。他們正確答案的平均提交時間僅 4 分鐘（隊伍平均為 8 分 30 秒），因此拿下 36 次速度加分（每次 0.25 分），是 Stanford 的兩倍多，一度在中場建立 10.25 分領先，直到比賽最後 56 秒才被 Stanford 較慢但更精準的 agent 以 1.75 分之差逆轉。

Yale 則打造了多分支驗證架構：四個獨立分支平行運作，涵蓋兩種 agent 策略——兩個分支是自主式 ReAct agent（分別使用 Gemini 3.1 Pro 與 Gemini 3.5 Flash），另兩個分支是以 Gemini 3.1 Pro 驅動的規劃者—驗證者（planner-verifier）流程，由規劃者整理出包含證據的 scratchpad，驗證者再核對引用來源並執行最終計算。最後由一個 Gemini 3.1 Pro meta-verifier 檢視四個分支的答案與推理，只能從既有分支中挑選答案，若無法決定則退回多數決。

🎯 **實務啟示**

三支隊伍的共通點是：準確率往往不是靠單次模型呼叫堆出來的，而是取決於文件前處理、檢索精準度、結構化工具使用與答案驗證這整套系統設計。這也提醒工程師，在企業文件問答場景中，投資在 pipeline 的工程細節，可能比單純換更強的模型更有效益。

🔗 **來源**
- 標題：Evaluating AI Agents Live at the Grounded Reasoning Cup
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/evaluating-ai-agents-live-grounded-reasoning-cup

#AIAgents #GroundedReasoning #Databricks #LLMEvaluation #EnterpriseAI #ClaudeOpus #Gemini #RAG #AgentBenchmark #DocumentQA
