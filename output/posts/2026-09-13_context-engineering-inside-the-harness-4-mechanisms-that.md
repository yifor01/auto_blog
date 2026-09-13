---
title: 'Context Engineering Inside the Harness: 4 Mechanisms That Beat Context Overflow
  and Goal Loss on Long-Horizon Tasks'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/12/context-engineering-inside-the-harness-4-mechanisms-that-beat-context-overflow-and-goal-loss-on-long-horizon-tasks/
model: claude-code/sonnet
generated_at: '2026-09-13T19:34:46.814949'
score: 99
---

📌 拆解 Agent Harness：四招搞定百步任務的 Context 危機

TL;DR：context window 變大沒用，真正救場的是 harness 裡的四個機制。

一個 Agent 跑一小時、打 200 次 tool call 之後會怎樣？如果你以為只是變慢，那還算樂觀，實際上它往往會忘記自己原本要做什麼。MarkTechPost 這篇文章拆解了 AWS Samples 針對自主雲端編碼 Agent 提出的設計指南，指出問題根源不在模型，而在「harness」這層，也就是 AWS 定義的「管理模型以外一切事務」的機制。

🤔 **更大的 context window，解決不了 context 問題**

AWS 指南直接點名 shallow agent 的兩個必然故障：context overflow（塞爆視窗）與 goal loss（被岔開注意力、忘記目標），且無法在長時間任務中維持狀態。直覺的解法是換一個更大的 context window，但證據顯示效果有限。Chroma 的 Context Rot 報告評測了包含 GPT-4.1、Claude 4、Gemini 2.5、Qwen3 在內的 18 個 LLM，發現即使是簡單的檢索任務，效能也會隨輸入長度增加而愈來愈不穩定。Anthropic 的 context engineering 指南解釋了機制：attention 會在 n 個 token 間產生 n² 組配對關係，每多塞一個 token，就在消耗一份有限的「attention 預算」。Manus 則指出，一個典型任務大約需要 50 次 tool call，輸入輸出 token 比例接近 100:1，原始指令會被不斷推向視窗中段，也就是最容易被遺忘的位置。換句話說，goal loss 不只是模型的 bug，而是「不管理 context」在長任務上的必然結果。

🧩 **機制一：先決定什麼「不」進視窗**

Deep Agents 訂出兩條有明確數字的 offloading 規則：當 tool 回應超過 20,000 token，就寫入檔案系統，視窗裡只留檔案路徑加前 10 行預覽；當 session context 超過模型視窗的 85%，較早的 write/edit tool call（其完整內容已存在磁碟上）會被截斷成指標。只有 offloading 用盡空間後，才會退回到摘要化。Claude Code 則把這套預算邏輯用在「進入第一個 prompt 之前」：auto memory 上限是前 200 行或 25KB，MCP tool schema 預設延遲載入，只列工具名稱，完整 schema 靠 tool search 隨需載入；compaction 之後，任何超過 5,000 token 的重新讀取檔案都只回傳路徑參照而非內容。這種「用 subagent 做架構級預算」的做法很具體：Claude Code 文件裡的範例是一個研究型 subagent 讀了 6,100 token 的檔案，卻只回傳 420 token 的結果給父層。AWS AgentCore 的示範走得更遠，一個 coordinator 平行派出 3 個瀏覽器 subagent，各自跑在獨立的 MicroVM 裡，analyst subagent 只拿到它們整理後的結構化結果，AWS 估計整體耗時 4 到 6 分鐘，若循序處理則可能長達 3 倍時間。

🧩 **機制二：offload 不夠時才 compaction**

Compaction 是把接近視窗上限的對話摘要化，再用摘要重新初始化 context。這也是 goal loss 最常發生的環節，因為一次失真的摘要可能剛好丟掉最關鍵的限制條件。Claude Code 的 compaction prompt 會保留架構決策、未解決的 bug 與實作細節，丟棄重複的 tool 輸出；compaction 後會重新讀取最近修改的最多 5 個檔案，重新載入對應規則，並重新注入被呼叫過的 skill 內容（每個 skill 上限 5,000 token，總計上限 25,000 token）。文件明言，對話早期的細節指令可能會遺失，所以持久性規則應該寫進專案根目錄的 CLAUDE.md，這份檔案會在每次 compaction 後從磁碟重新注入；使用者也能用 `/compact focus on the auth bug fix` 引導摘要方向，或用 `/autocompact` 調整觸發點。Deep Agents 把「保留目標」做成結構化欄位：摘要文件有專屬欄位記錄 session 意圖、已建立的產出物與下一步，LangChain 團隊是在強制摘要實驗顯示這樣改善效能後才加上這些欄位；完整原始對話紀錄仍會寫入檔案系統，被摘要掉的事實日後可用 read_file 找回。OpenAI 的 Responses API 也把 compaction 搬進 API 層，提供 `context_management` 搭配 `compact_threshold`，以及一個獨立的 `/responses/compact` endpoint，回傳含有加密壓縮項目的視窗，OpenAI 要求開發者原封不動把這個視窗傳入下一次呼叫；OpenAI 表示 Codex 就是靠這個機制撐住長時間的編碼任務。Claude Developer Platform 則提供 `compact_20260112` 這個 context-management edit，可自訂指令並搭配 `pause_after_compaction` 選項，在模型繼續之前插入內容。

🧩 **機制三：todo-state，每一輪都重申目標**

Compaction 保護的是摘要那一刻的目標，todo-state 保護的是兩次摘要之間的每一輪。Manus 的做法很直白：Agent 建立 todo.md 並逐步改寫、勾選完成項目，重寫清單等於把目標重新唸進 context 的最尾端，把全域計畫推進模型最近的注意力範圍，藉此降低「lost in the middle」的漂移，且不需要改架構。不過這個做法並非全然正面：Deep Agents 原本預設內建 write_todos 工具，直到 2026 年 7 月的 v0.7 版，LangChain 才把 TodoListMiddleware 改成選用，原因是他們在 3 種任務類別上的評測顯示，關掉 todo 反而有更好的 reward 和更低的成本；儘管如此，LangChain 仍建議在長多步驟任務、能力較弱的模型、以及需要顯示進度的 UI 場景中重新打開它。Claude Code 則持續維護 todo 清單，並在 compaction 後從磁碟重新注入 plan mode 寫下的計畫。Anthropic 的指南把這種通用模式稱為結構化筆記：Agent 在視窗外寫一份 NOTES.md 或 TODO 檔案並重新載入，其 Claude Plays Pokémon 範例就是在數千個遊戲步驟中維持計數，每次 context 重置後讀回自己的筆記，藉此延續長達數小時的多步驟序列。

🧩 **機制四：任務結束後，記憶怎麼留下來**

Claude Code 在每次 compaction 後都會重新注入專案根目錄的 CLAUDE.md 與 auto memory。AgentCore Memory 會儲存事件並在背景執行配置好的萃取策略，讓 coordinator 在下一次執行時呼叫 recall 工具，而不用重新研究一次；AWS 特別警告，如果沒有配置至少一種萃取策略，原始事件雖然會被儲存，但不會有任何內容可供檢索。Anthropic 在自家平臺上的檔案式記憶工具，扮演的是同樣的角色。

🎯 **實務啟示**

這四個機制指向同一個原則：目標必須是可變的「檔案」，而不只是歷史訊息裡的一句話。訊息會老化、會被摘要掉，但一份每隔幾輪就重寫的檔案永遠是最新、最短，也撐得過任何一次重置。在設計自己的 Agent harness 時，與其一味追求更大的視窗，不如先問：什麼東西可以完全不進視窗（offloading）、視窗滿了要怎麼摘要（compaction）、目標怎麼在每一輪被重申（todo-state）、任務結束後什麼該留下來（persistent memory）。

🔗 **來源**
- 標題：Context Engineering Inside the Harness: 4 Mechanisms That Beat Context Overflow and Goal Loss on Long-Horizon Tasks
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/12/context-engineering-inside-the-harness-4-mechanisms-that-beat-context-overflow-and-goal-loss-on-long-horizon-tasks/

#AIAgents #ContextEngineering #LLM #ClaudeCode #LangChain #AmazonBedrock #AgentCore #PromptEngineering #AIInfrastructure #SoftwareEngineering
