---
title: Building always-on agents
source: Claude Blog
url: https://claude.com/resources/articles/building-always-on-agents
model: claude-code/sonnet
generated_at: '2026-11-13T22:42:03.268404'
pinned: true
---

📌 【Anthropic】Always-on Agent 不是一直在跑，而是睡醒再工作

TL;DR：Anthropic 拆解 always-on agent 的底層架構：事件收件箱、計時器、記憶體三大元件。

一個「全天候在線」的 agent，聽起來像是永遠在運算、燒錢燒算力的怪物。但 Anthropic 指出，實際上它大部分時間都在睡覺，只是定期醒來做一點事而已。

🤔 **為什麼 Always-on Agent 最近又紅了**

Anthropic 在部落格中提到，過去幾個月 always-on agent 重新受到關注。這類 agent 具有「狀態性」與「主動性」,意思是它們會跨多個 session 管理 context，並在沒有人直接監督的情況下採取行動。文章指出，這波復興主要來自模型能力的進步：一是最新模型的判斷力更好，更懂得理解使用者意圖、知道什麼時候該主動回報；二是智慧越來越便宜，長任務受益最明顯。文章舉例，在一項長任務程式碼評測基準上，Opus 5.5 每完成一個任務的成本比 Opus 5 低 78%，相較於一般工作負載只便宜 40%。

🧩 **醒來、工作、存檔、再睡：五個核心元件**

Anthropic 把 always-on agent 的底層架構拆成五個核心元件：事件收件箱（event inbox）、計時器（timers）、記憶體（memory）、權限（permissions）與發送信箱（outbox）。文章對前三者有較完整的說明：

事件收件箱: 多數 AI agent 只在使用者發訊息時才運作，而 always-on agent 要能被 webhook、排程任務、背景工作等多種事件觸發。如果讓每個事件來源直接呼叫 agent，容易出現同時觸發的競爭執行,或是程式當掉導致事件遺失的問題。因此需要一個收件箱：來源把事件寫進一個持久化的清單（通常是資料庫表），由一個 handler 負責寫入，再由一個 worker 讀取並啟動執行。Anthropic 建議每個使用者先用一個收件箱，需要更高平行度再進一步拆分；handler 要快速確認收到事件，較深入的檢查（例如偵測 prompt injection）則留到實際執行時處理；而同一個收件箱同一時間只能有一個 worker 在運作，以免兩個執行互相覆寫對方的結果。

計時器: 計時器讓 agent 能夠主動行動，分成「follow-up」（agent 自己設定的提醒，例如等待回覆後要追問）與「schedule」（固定週期的排程任務，例如每日的電子報）兩類，存放在獨立於收件箱的資料庫表中。一個背景的 scheduler 會定期掃描這個儲存區，找出到期的計時器，依類型更新狀態（follow-up 標記完成、schedule 更新到下一次的到期時間），再把對應事件送進收件箱喚醒 worker。

記憶體: Always-on agent 要跨越許多彼此不連續的執行，因此需要記憶體來維持連續性，同樣要有自己獨立的儲存。文章提到，在 Claude Code 的 auto memory 與 Messages API 的 memory tool 中，這是以檔案目錄的形式實作；對 always-on agent 而言，這個目錄應該對應到資料庫或物件儲存這類持久化儲存，確保記憶不會隨著 worker 消失。文章給出一個原則:記憶體只該存放 agent 無法再次查到的東西，若資訊已經存在其他系統（例如議題追蹤工具），就該存一個指標過去即可。記憶體大致可分成使用者指示、使用者筆記、過去的訊息、以及任務進度四類，分別在每次執行開始時載入，隨筆記或進度增加後可以只載入索引，需要時再拉取細節檔案。文章也提到可以加入「dreaming」機制，回顧過去的 session 來整理記憶、取代過時的條目，找出只有在大量執行中才會出現的模式。

至於權限與發送信箱這兩項元件，文章僅點出名稱，未進一步展開細節。

🎯 **實務啟示**

對想把現有 agent 改造得更主動、或打算從零打造 always-on 體驗的團隊來說，這套「收件箱 + 計時器 + 記憶體」的三件組是可以直接參考的設計骨架：用收件箱統一管理各種觸發來源避免競爭，用計時器讓 agent 有能力主動找上使用者，再用持久化的記憶體讓每次執行都能接續前一次的進度，而不是每醒來都從零開始。

🔗 **來源**
- 標題：Building always-on agents
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/building-always-on-agents

#Anthropic #AIAgents #AgentArchitecture #AlwaysOnAgents #ClaudeCode #AgentMemory #SoftwareArchitecture #LLMEngineering #AIInfrastructure #OpusAI
