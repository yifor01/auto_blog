---
title: Decoding AI’s Open-Source Course Maps Three Ways to Run an Agent Loop and the
  Provider Economics Behind Each
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/22/decoding-ais-open-source-course-maps-three-ways-to-run-an-agent-loop-and-the-provider-economics-behind-each/
model: claude-code/sonnet
generated_at: '2026-08-23T06:12:19.913554'
score: 108
---

📌 同一顆模型換個執行迴圈，排名從第 30 衝進前五

TL;DR：LangChain 實驗顯示,只換 harness、模型不變,coding agent 排名大幅躍升,開源課程 Decode 拆解出三種執行模式與各自的算力帳單。

多數團隊把「用哪個模型」當成最重要的決策,但 harness 工程的實驗結果一再指向別的地方。在 LangChain 的 Terminal-Bench 實驗中,全程使用同一顆模型,只更動 harness（執行迴圈的程式框架）,就讓一個 coding agent 從排名第 30 名左右衝進前五名。這個結果把問題重新定義了:如果 harness 才是決定品質的關鍵,那麼「怎麼跑這個迴圈」就不是部署細節,而是一項架構決策。

🤔 Agent 的核心其實很小,大頭都在 harness

Paul Iusztin 的開源課程《Building a Coding Agent From Scratch》,透過 Decoding AI 發布,打造了一個名為 Decode 的 Python agent。系統中心是一個沒有自己介面的 headless harness,裡面跑著所有 harness 共用的那個迴圈:LLM 選擇動作、工具執行、觀察結果回饋,一切都讀寫同一個 context window。

Agent 本身其實非常精簡。在 Decode 裡,它只是一段約 20 行的 Pydantic AI 定義,組合模型、工具與輸出型別。作為對照,在 Claude Code 外流的原始碼中,核心迴圈大約也只有 150 行。真正龐大的部分是其餘的 harness:記憶、skills、沙箱、權限管理、LSP 回饋、context 壓縮(compaction)等等。

🧩 三種介面,三種延遲需求,三種供應商選擇

不同介面接上這個核心 harness,就出現三種執行模式:

**終端 UI 模式**:一個 live session 在記憶體中、同一個行程內即時運作,事件透過 async generator 串流回傳。這裡最難處理的是「插話」:如果使用者在工具呼叫進行中打字,立即插入訊息會破壞當下的回合。Decode 的解法是steering queue 加上 priority gate,輸入先被緩衝,只在安全邊界才注入。迴圈公開兩個邊界:下一次呼叫模型前的 MODEL_REQUEST,以及回合即將結束的 WOULD_STOP。對應到三種輸入方式:純 Enter 在回合內插話,Alt+Enter 把後續指令排入佇列、等回合結束才生效,Esc 則在下一個邊界觸發協作式中止,並清空兩個佇列以保持歷史完整。由於有真人正在盯著每個 token,這個模式受延遲限制,因此適合掛在低延遲的 hosted API 上。

**遠端模式**:harness 保持 headless,透過 agent runtime 在伺服器上運行。Decode 使用 ZenML 的 agent runtime Kitaru,部署在 GCP 上,agent 本身則在 Modal 上執行。這裡沒有人在看,一批待辦工單會平行展開成 N 個 harness,各自產出自己的 PR。因為 runtime 會逐步記錄進度,沙箱在任務中途掛掉時可以從最後記錄的步驟接續,而不必重跑;若某次執行暫停等待人工輸入,它會凍結並不消耗運算資源。工具在遠端於 Modal Sandboxes 中執行,本地則用 Docker。這裡在意的指標是「每美元的產出量」,而不是首個 token 的回應時間。

**第三種模式**介於兩者之間:live session 把工作丟給 job queue 後立即返回,背景工作流再展開 LLM 呼叫並事後回報結果。使用者在線,但不是盯著每一步。工作由佇列擁有,執行壽命超越啟動它的 client。這正是 Slack 觸發的 agent、背景 PR 審查這類場景背後的模式,計費方式像批次處理,而非即時對話。

📊 同一件事,互動與離線的帳單可以差七倍以上

成本模型跟著延遲需求走,差距相當可觀。以 1,000 份文件、每份 30,000 input tokens、約 500 output tokens 為例,以前沿 API 費率($3/百萬 input、$15/百萬 output)計算,總成本約落在 97 美元;由於每份文件的前綴都不同,prompt caching 幫不上忙。若改用 serverless GPU 批次處理,以每秒約 3,000 tokens 的速度計算,同樣的工作量在不到三小時的 GPU 時間內完成,成本約 13 美元。

反過來的情境同樣尖銳。Decode 預設的測試模型 Qwen3.6 35B 可在單張 H200 上運行,Modal 公開報價的 H200 SXM 為每秒 0.001261 美元,約合每小時 4.54 美元。如果讓一個互動式 agent 整夜閒置、等一個 y 確認,十個閒置小時就會多花約 45 美元。這正是整篇論述的核心:互動工作按 token 計費,因為有真人在等;離線與非同步工作按 GPU 小時計費,因為目標是吞吐量,閒置時間才是敵人。

還有第二個維度:serverless 與保留容量(reserved capacity)之爭。Modal 的定價分析把它簡化成一個比較:保留容量以尖峰速率支付整個合約期,serverless 則跟著需求曲線走。當尖峰對平均的比值超過保留折扣,serverless 就更划算。Modal 引用的資料顯示,推論、訓練與 agentic 開發場景中,保留折扣通常在 2 到 5 倍之間,而尖峰對平均比則常落在 5 到 10 倍;其引用的產業調查更指出,保留容量的實際使用率往往低於 30%,甚至常常不到 10%。

🎯 實務啟示

在投入更多預算換更強模型之前,先檢視自己的 agent 是互動式還是背景式:如果人在盯著螢幕,重點是低延遲的 hosted API;如果是背景批次或工單處理,重點該轉向 GPU 小時的吞吐效率,並認真評估 serverless 與保留容量哪個更貼近實際使用率。同時,harness 本身的設計(steering、狀態記錄、可續傳的沙箱)可能比換模型更快帶來品質與成本上的改善。

🔗 來源
- 標題：Decoding AI's Open-Source Course Maps Three Ways to Run an Agent Loop and the Provider Economics Behind Each
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/22/decoding-ais-open-source-course-maps-three-ways-to-run-an-agent-loop-and-the-provider-economics-behind-each/

#AIAgents #CodingAgent #AgentArchitecture #LLM #Serverless #GPUComputing #DevTools #OpenSource #InferenceEconomics #Modal
