---
title: 'MemCurrent: Designing Persistent Memory for Production Agents'
source: Databricks
url: https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents
model: claude-code/sonnet
generated_at: '2026-10-20T20:47:10.841143'
score: 102
---

📌 MemCurrent:企業 Agent 記憶架構實測通過率翻三倍

TL;DR:Databricks 公開 MemCurrent 記憶架構,讓企業 agent 通過率提升 3 倍,token 少用 31%、速度快 26%。

直覺上,給 agent 看越多歷史對話,它應該表現越好。但 Databricks 的實驗顯示,把所有過去的 session 全部塞進 context,反而會讓 agent 被過時、矛盾的資訊搞糊塗,表現不如精心篩選過的記憶。問題不是「要不要記憶」,而是「該記什麼、怎麼維護、如何證明它真的有用」。

🤔 **品質與效率的拉扯,記憶被當成解方**

在正式環境中跑 agent,開發者常被迫在「答案品質(尤其是長尾任務)」與「成本延遲」之間二選一。記憶被視為能同時改善兩者的方法:讓 agent 跨任務攜帶使用者偏好、過去的修正、指標定義與成功的工作流程,理論上可以提升準確率、減少重複犯錯、避免白做工。但塞入過多歷史紀錄,會引入過時、衝突或不相關的 context,所以核心挑戰在於「保留什麼、如何維護、如何衡量有用性」。

🧩 **三種存取模式 + 兩層記憶結構**

Databricks 指出記憶可以用三種方式接入 agent:作為 plugin(在固定時間點自動讀寫)、作為 tool(agent 自己決定何時讀寫)、作為離線 pipeline(背景排程或觸發更新,供之後的 session 使用)。MemCurrent 三種都用,各自用在最適合的地方。

架構上分成兩種記憶:episodic memory 儲存原始 session 紀錄,是 append-only 的;derived memory 則是從這些紀錄中提煉出來的學習結果,以結構化知識庫的檔案形式儲存,並有一份自動產生的 memory.md 索引描述檔案結構。寫入有兩條路徑:agent 可透過 add_memory、update_memory、delete_memory 等工具處理明確指令(例如「不要在 /tmp 目錄寫程式」);其餘的隱性學習則由離線的「dreaming」pipeline 負責提煉,同時清理整個記憶庫,拆分過大的檔案、合併重複內容、解決衝突。讀取則分層進行:session 開始時 plugin 會注入記憶索引,過程中 agent 可用 search_memory(找出最相關的過去片段)與 fetch_memory(依識別碼取出完整內容)。

📊 **12 萬字的 session 篩出 114 個測試案例**

為了評測,Databricks 自建了 Internal Memory Benchmark:從 12K+ 筆真實 Genie 對話中,先篩出 3K 筆含「值得記憶訊號」的候選,再草擬後續問題與評分標準,並讓對抗性 judge 依 7 項準則(例如知識是否真的存在、是否針對該使用者、是否為回答所必需等)檢核,最終人工複核後留下 114 個測試案例,涵蓋 29 位使用者與 2,233 筆歷史 session。

在三個開源基準(LoCoMo、LongMemEval、ConvoMem)上,MemCurrent 平均準確率 88.1%,與「把所有歷史塞進 context」的上限(87.8%)相當,但輸入 token 少了約 12 倍(8.4K vs 103K)。在歷史最長的兩個基準上,MemCurrent 甚至超越了全文塞入的做法。

在自家的 Internal Memory Benchmark 上差距更明顯:MemCurrent 通過率 68.4%、延遲 252 秒、用了 418K tokens,拉近了「無記憶」(22.3%)與「只注入標準答案記憶」上限(78.6%)之間超過 80% 的差距。相較無記憶,MemCurrent 讓通過率翻三倍(22.3% → 68.4%),同時快 1.35 倍、省 1.44 倍成本。值得注意的是,另一個開源方案 Mem0 在開源基準上表現也不錯,但到了內部企業基準只拿到 43.9%,延遲與成本都更高。

💡 **找到答案不等於會用答案**

這份基準測試刻意和既有的開放式聊天基準不同:它用真實的企業資料工作場景,包含表格語意、指標定義、工作流程等知識;更重要的是,它要求記憶必須能「餵給行動」,而非只是在過去對話中找到正確字串 — agent 得把取回的知識實際套用到多步驟任務上才算過關。這也解釋了為何某些在開放式基準上表現亮眼的方案,到了企業場景會明顯落後。

🎯 **給工程團隊的啟示**

如果你的 agent 需要長期記住使用者,「全部塞進 context」不是答案,反而可能拖慢速度又讓模型困惑。把記憶拆成「原始紀錄」與「提煉後的知識庫」兩層,並用離線流程持續整理、去重、解衝突,是目前看來兼顧品質與成本的做法。同時,挑選記憶方案時別只看開放式聊天基準的分數,企業場景下「記憶能否被正確套用到任務」才是真正的考驗。

🔗 **來源**
- 標題:MemCurrent: Designing Persistent Memory for Production Agents
- 作者/機構:Databricks
- 連結:https://www.databricks.com/blog/memcurrent-designing-persistent-memory-production-agents

#AI #AgentMemory #Databricks #LLMAgents #MachineLearning #ProductionAI #MemCurrent #EnterpriseAI #RAG #AIEngineering
