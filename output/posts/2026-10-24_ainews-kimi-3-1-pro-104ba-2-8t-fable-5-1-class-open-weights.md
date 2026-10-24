---
title: '[AINews] Kimi 3.1 Pro 104BA-2.8T: Fable-5.1-Class Open Weights narrows Closed-AI
  lead to 1 month... and Pro Highspeed API with 2-3× speed'
source: Latent Space
url: https://latent.space/p/ainews-kimi-31/
model: claude-code/sonnet
generated_at: '2026-10-24T19:39:12.289085'
score: 77
---

📌 Kimi K3.1 Pro 上線：2.8T 參數開源模型把智慧差距縮到 3 分，權重還沒給

TL;DR：Moonshot 的 K3.1 Pro 在獨立評測逼近頂尖模型，但發布當下只有 API，開源權重要等到 11 月 4 日。

一個標榜「開源」的模型，發布當天卻拿不到權重，這正是 Kimi K3.1 Pro 這次上線最矛盾的地方。獨立測試機構把它排進前四，媒體卻在爭論這到底算不算「開源」。

🤔 **從 K3 到 K3.1 Pro，這次升級在哪裡**

根據 Moonshot 官方說法，K3.1 Pro 是 Kimi K3 的 post-trained 版本，用上「大幅增加」的 post-training 運算量。團隊表示為了讓數百個下游領域能做大規模 joint RL，他們重新最佳化了整個技術堆疊，包括 RL 框架、長文本（long-context）推論、訓練效率、sandbox 基礎設施、rollout 排程，以及一套共用的環境品質檢查平臺，目標是讓每一份額外的 RL 運算都能帶來穩定、可預期的提升。這個做法與 Z.ai 從 5.2 升到 5.3 的模式類似：版本號看起來是小改版，實際投入的 post-training 運算卻遠超過字面上的意義。

🧩 **架構概況：3T 級 MoE，主打長任務與多模態**

Moonshot 將 K3.1 Pro 描述為多模態、「3T 級」的 mixture-of-experts 模型，總參數 2.8 兆（trillion）、啟動參數（active parameters）104 億 104B，context window 達 100 萬 token。官方宣傳的強項包括完整專案級程式碼開發、Blender/CAD 作業、財務建模，以及長時間執行的 agent 任務。

上線時提供 Standard 與 Highspeed 兩種版本，涵蓋 Kimi 官網／App、Kimi Work、Kimi Code 與 API。Moonshot 宣稱 Highspeed 版在維持智慧水準的前提下，輸出速度可達一般版本的 2 到 3 倍，但官方帳號也提到費用是雙倍。同時上線的還有 Kimi Hosted Agents，這是一套提供 24 小時執行環境、支援多代理協作的受管理 harness，用於長時間執行的任務。

📊 **獨立評測：智慧指數第四，Cyber 分數意外亮眼**

Artificial Analysis 的 Intelligence Index 把 K3.1 Pro 排在第四，55 分，落後 Opus 5.5（58 分），與 Sonnet 5.5、Muse Wonder Full 同為 56 分的組別接近。AA 指出它的進步主要集中在 agentic 能力，而非平均分布在知識與科學類測驗上。

| 評測 | K3.1 Pro | 對照 |
|---|---|---|
| AA Intelligence Index | 55（第四） | Opus 5.5 58、Sonnet 5.5／Muse Wonder Full 56 |
| Arena Code Arena: WebDev | #8，1,692 分 | 較 K3 的 #17、1,655 分，進步 9 名、37 分 |
| AA Cyber Index | 64%（公開可取得模型最高，整體第二） | 落後具信任存取權限的 GPT-6 Sol Daybreak Blue 69% |
| AA-Omniscience 準確率 | 51% | 較 K3 的 48% 提升 |
| AA-Omniscience 幻覺率 | 44% | 較 K3 的 53% 下降 9 個百分點 |

值得注意的是，AA 表示 K3.1 Pro 在 Cyber Index 的高分，是在團隊「刻意減少」cyber 相關訓練資料的情況下取得的。另外有人整理出一個初步的 ECI 聚合分數 164.7，90% bootstrap 區間落在 152.5 到 169.0 之間，發文者後續修正為 160 到 165 較合理，這是一種不確定性較高的聚合估計，並非獨立執行的測試結果。AA 也指出，一旦權重正式發布，其「開源 vs 閉源」智慧指數差距會從目前的 12 分縮小到 3 分。

💡 **權重未發、「本地可跑」的說法值得存疑**

這次發布最大的爭議在於：上線當下只有 API，權重要等到 11 月 4 日才會公開，而素材中的貼文並未說明最終授權條款、重新分發限制、商用限制、checkpoint 精度或完整推論需求，因此「即將開源」比直接說「開源」更準確，AA 也明確把這次的權重記錄為「尚未發布」。

輿論反應呈現兩極：一邊是對潛在開源前沿模型的期待，另一邊則是對推論成本、部分互動任務表現較弱、評測呈現方式，以及未揭露的付費推廣爭議的擔憂。這些是不同層面的問題，評測品質不代表部署成本低，推廣爭議也不等於模型能力有問題。

另外有人指出，104B 的啟動參數不代表部署成本等同於一個 104B 的 dense 模型，實際上系統仍須容納龐大的專家池與執行期狀態。純粹作為示意計算，2.8T 參數若以 16-bit 儲存約需 5.6 TB 記憶體，4-bit 量化約需 1.4 TB，且這還不包含量化中介資料與服務端額外開銷。素材中並未揭露層數配置、專家路由機制、attention 設計、訓練運算預算，或實測的長文本服務負載，因此有評論特別提醒，不該把需要大量加速器基礎設施才能部署的兆參數模型稱為「本地模型」，可自行部署（self-hostable）與消費級裝置本地執行（consumer-device-local）是兩件不同的事。此外這次發布並未提及 Flash 版本，外界對是否會有更小規格的後續版本仍只是猜測。

🎯 **實務啟示**

對工程師而言，這次發布的真正意義不在「又一個開源模型」，而是提醒評估一個 MoE 模型時，啟動參數只能看出推論運算量的一部分，實際部署仍要評估專家池儲存、長 context 的記憶體需求與服務架構。在權重、授權條款與完整技術報告正式公開前，任何「本地可跑」或「比肩頂尖閉源模型」的宣傳都值得保留判斷，等實測與授權細節落地後再評估是否值得整合進自己的 pipeline。

🔗 **來源**
- 標題：[AINews] Kimi 3.1 Pro 104BA-2.8T: Fable-5.1-Class Open Weights narrows Closed-AI lead to 1 month... and Pro Highspeed API with 2-3× speed
- 作者／機構：Latent Space
- 連結：https://latent.space/p/ainews-kimi-31/

#Kimi #MoonshotAI #OpenWeights #MixtureOfExperts #LLM #AIBenchmark #ArtificialAnalysis #AgenticAI #LongContext #OpenSourceAI
