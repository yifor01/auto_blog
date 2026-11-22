---
title: 反超Gemini之後，Karpo新作再開源，瀏覽器Agent速效雙贏
source: 量子位
url: https://www.qbitai.com/2026/11/511791.html
model: claude-code/sonnet
generated_at: '2026-11-22T22:36:09.377192'
score: 97
---

📌 決策模型開源：Karpo Decision 31B，一次推理取代逐字生成

TL;DR：MachinePulse 開源決策模型與瀏覽器 Agent 框架，省掉大模型逐字生成的開銷。

同一場篩選任務，Karpo Decision 31B 花 2.6 秒做完，Gemini 3.5 Flash 用了 14.96 秒，準確率卻同樣是 100%。這不是模型變聰明了，而是它根本沒有在「寫答案」。

🤔 為什麼大家突然都在做決策模型

Agent 愈來愈能幹之後，一個尷尬的事實浮現：每次選工具、篩結果、判斷任務是否完成，如果都呼叫通用大模型逐字生成答案,既慢，Token 也燒得快。於是專門處理這類高頻、瑣碎判斷的「決策模型」成了新賽道，今年 9 月 Jev 爆紅後,背後的 TypeSafe AI 在 24 天內拿到 75 億美元估值，OpenAI、微軟、亞馬遜、Cloudflare 也陸續跟進。但現有方案各有缺口：Jev 與 Google 的 Gemini Decision 1 速度快卻不開源，開發者難以自行部署；已開放權重的模型（如 GLiDE）則不一定能把速度和判斷力同時拉滿。MachinePulse 這次開源的 Karpo Decision 31B，定位正是補上「開源且兼顧速度與準度」這塊缺口。

🧩 省掉逐字生成：Readout Head 怎麼一次算出整組機率

通用大模型面對選擇題，通常要逐個 token 生成答案文字，再由程式解析出選項。Karpo Decision 31B 把這道工序直接省掉：它為候選選項安排專門編碼，題目後面放一個用於讀取結果的標記，模型讀完輸入後，Readout Head 就在這個位置為各選項打分並轉換成機率。整個過程只需一次前向推理，輸出 token 數直接降到 0。

這套機制可以同時處理三種決策類型：Choice（選擇題，最多在 255 個候選選項間分配機率）、Noul（Yes/No 判斷題，直接給出任務是否完成的機率）、Score（評分題，為不同評分等級分別給出機率）。三種題型共用同一個 Readout Head。

🧩 一次請求塞幾十道題：Branch Attention 的分工

Agent 實際運作時往往要同時篩選幾十條搜尋結果或工具選項，背後還跟著一大段網頁內容或任務上下文。為避免每道題都重算一次背景材料，Karpo 設計了 Branch Attention 機制，支援 256K 上下文：輸入分成共用的 Shared Block（任務說明、問題清單、網頁內容，只算一次）與各題自己的 Branch（題目、選項、讀取標記，分別作答互不干擾）。效果是在一張 RTX PRO 6000 上，單獨回答一題中位耗時 371 毫秒，一次請求塞 16 到 63 道題時，中位耗時也只是 653 毫秒，沒有隨題數成倍增長。

📊 跑分與實測：Decision Index 登頂、瀏覽器任務省下八成成本

在涵蓋 300 個模型的 Decision Index 評測總榜上，Karpo Decision 31B 以 Full 分 73.9 登頂，單題最多可同時判斷 255 個候選選項，校準誤差（ECE）2.3%。面對公開集 14 萬多次請求，中位回應時間僅 94 毫秒。

MachinePulse 同時開源了已用於自家 Personal Agent 產品的瀏覽器操作框架 karpo-browser，採用 System 1 + System 2 架構：通用大模型（如 DeepSeek V4.1 Flash）負責理解需求、拆解任務；專門訓練的 Karpo Decision 27B Act 負責在頁面上選輸入框、點按鈕，單次決策時延中位數僅 931 毫秒。在 Browserbase Benchmark v2 的 102 道核心任務上，這套方案做到 89% 平均成功率、201 秒平均耗時，單任務模型成本僅 0.096 美元；相比榜首 Claude Fable 5.2 搭配 Claude Code，速度快約 1.9 倍，成本只有對方的十三分之一。團隊三輪實測也發現，網頁上約 78% 的操作交給了決策模型完成,但這些操作僅佔整個 Agent 執行耗時的 14%、模型成本的 13%。

💡 校準與泛化：RLCD 讓模型誠實報告把握度，RSI 解決偏科

快和準之外，Karpo 還處理了兩個容易被忽略的問題。第一是「模型該不該對自己的判斷有自知之明」：團隊用 RLCD（面向校準決策的強化學習）訓練,不只獎勵選對答案，還依整組預測機率計算獎勵，鼓勵模型如實報告把握度，即便訓練資料標籤存在分歧，也盡量保留這種不確定性而非強行壓成唯一答案，最終在 JevBench 公開題上做到 2.3% 的預期校準誤差。

第二是訓練中出現的「偏科」：隨著訓練推進，公開測試成績從 73.1 漲到 75.1，但 13 個陌生領域的評測準確率反而從 72.1% 跌到 70.7%。團隊引入 RSI（遞迴自我改進）框架應對：先訓練出多個候選模型（其中 3 個全參數微調、2 個 LoRA 微調），再透過 Model Fusion 做權重平均，把早期模型的泛化能力與後期模型的專精能力結合，融合後的模型只有勝過當前版本才能晉級下一輪。結果是公開測試成績維持 75.1，陌生領域準確率回升到 72.3%，而且融合後仍是標準的 31B 參數模型，結構與推理開銷都沒有增加。在團隊自組的 13 領域測試中，Karpo 最終以 72.3% 準確率超過此前 Decision Index Full 榜單前三名 KnowLine 31B Gen1（71.5%）、Sieve 31B v3（70.4%）與 GLiDE 1.2（69.1%）。

🎯 實務啟示

這次 MachinePulse 開源的不只是模型權重，還包括用 TypeScript 寫的 karpo-browser 框架，以及覆蓋 584 個真實網站、23,075 步網頁操作的 KBB 評測集。框架可透過 MCP 接入 Claude Code、Codex 等現有 Agent,不需要從零搭建瀏覽器操作能力。對正在把 Agent 做成面向大量使用者產品的開發者來說，把高頻、瑣碎的判斷從通用大模型移到專門的決策模型，是一個可以直接落地、且已經有公開成本與基準數據可參考的方向。

🔗 來源
- 標題：反超Gemini之後，Karpo新作再開源，瀏覽器Agent速效雙贏
- 作者／機構：衡宇、文婷 @ 量子位
- 連結：https://www.qbitai.com/2026/11/511791.html

#DecisionModel #AIAgent #OpenSource #LLM #BrowserAgent #MCP #ModelFusion #ReinforcementLearning #Calibration #AIInfrastructure
