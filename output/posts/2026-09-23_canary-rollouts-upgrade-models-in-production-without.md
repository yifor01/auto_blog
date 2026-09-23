---
title: 'Canary rollouts: upgrade models in production without downtime'
source: Together AI
url: https://www.together.ai/blog/canary-rollouts-upgrade-models-in-production-without-downtime
model: claude-code/sonnet
generated_at: '2026-09-23T20:41:04.714025'
score: 82
---

📌 【Together AI】Canary Rollouts：換模型不再靠人肉盯 Grafana

TL;DR：Together AI 推出 canary rollout 機制，用平臺化的分階段流量遷移與指標閘門，取代人工換模型的高風險操作。

一次真實案例：把 Qwen2.5-7B 換成 Qwen3.5-9B，流量灌到 10% 時，指標閘門偵測到 p95 延遲飆升 137%，系統自動暫停，工程師取消並反向回滾，過程中沒有任何一個線上請求失敗。這正是 canary rollout 想解決的問題。

🤔 換模型為什麼是個高風險操作

Together AI 指出，只要你在正式環境跑模型，遲早要面對換 checkpoint 或換模型家族的需求：開放模型生態系演進很快，候選模型在 evals 上表現亮眼，或承諾更好的吞吐量。但傳統做法只有兩種選擇：硬切換（hard swap）讓端點直接指向新模型，全部使用者瞬間受影響，一旦 p95 延遲翻倍，往往是從儀表板或客訴才發現，然後在壓力下回滾到一個冷啟動的舊模型；或是自行搭建分階段遷移（DIY staged cutover），用第二套部署加上腳本手動調整流量比例，同時盯著 Grafana，還得記得在流量切回去之前把舊部署的容量調回來。這兩種方式都把「人」當成唯一的安全機制。

🧩 Rollout 如何運作：三種策略、五道防線

Rollout 在同一個端點上，於來源（source，目前服務中的部署）與目標（target，想要服務的新部署）之間遷移流量，可選擇三種策略：

- Canary：依自訂的分階段比例移動流量（預設梯度為 5%→25%→50%→100%），每一步之間有等待時間，並可選擇加上指標檢查。
- Blue-green：單次、有閘門把關的 0%→100% 切換，可視為單步版的 canary。
- Rolling：原地、逐副本（replica-by-replica）替換，總容量維持不變，適合容量吃緊或同模型設定變更的情境。

每個 canary 步驟內部的執行順序經過刻意設計，用來防止特定類型的事故：目標先擴容，才會有流量被導向；健康檢查（health gate）在流量轉移前執行，確保只有引擎已載入並正常回應的副本會接收流量；流量轉移與來源縮減之間有一段「傳播等待」（propagation wait），讓路由快取先收斂；來源要等流量真正轉移完才開始縮減，也就是「擴容先於流量上升，流量先於容量下降」；而等待期與指標閘門都要通過，該步驟才會被標記為完成，確保「已回歸」的步驟不會被誤判為通過。

Rollout 建立後會停在 PENDING 狀態，直到你明確啟動它，這個「先建立、後啟動」的兩段式設計是刻意的，方便你或同事先審視計畫，確認要在真正盯著監控的時候才啟動。執行過程中有兩種暫停狀態值得留意：PAUSED 是你自己按下暫停，會停在原地、之後從同一步驟恢復；SYSTEM_PAUSED 則是平臺自己偵測到問題（例如指標閘門沒通過、容量不足或指標缺失），自動停下並通知你等待人工核准。整個流程沒有 FAILED 這種讓流量卡在中間的結束狀態：rollout 只會以 COMPLETED（目標正式接手服務）或 CANCELED（流量比例凍結在當下，可反向執行回到起點）收尾。

📊 三種策略的取捨

| | Canary | Blue-green | Rolling |
|---|---|---|---|
| 流量模式 | 依自訂比例分步（預設 5%→25%→50%→100%），每步維持一段等待時間 | 單次切換，0%→100%，目標健康後一次到位 | 逐副本替換，依副本比例遷移流量 |
| 額外容量需求 | 接近來源規模，目標先擴一步容量才縮來源 | 兩套部署都維持滿載直到來源縮減 | 來源副本數量＋中途多一個副本 |
| 典型耗時 | 一次冷啟動加上每步等待（含指標閘門時，每步至少 390 秒） | 一次冷啟動加 30 秒傳播等待，數分鐘內完成 | 每個副本一次冷啟動，部署越大越慢 |
| 指標閘門 | 有，每一步之後都會檢查 | 沒有（無等待視窗） | 沒有 |
| 適用情境 | 在正式流量上先驗證，再考慮全量切換 | 能短暫承受雙倍容量、追求最快切換 | 容量吃緊，或同模型引擎／設定變更 |

📊 用一個真實案例驗證：Qwen2.5-7B → Qwen3.5-9B

在單顆 H100 的環境下，作者實際跑了一次 canary rollout：傳播等待的用意是避免尚未更新的全域路由快取，把請求送到正在縮減的來源；等待時間會依據指標視窗加上資料延遲自動拉長；第一步的耗時主要來自冷啟動，之後的步驟因為目標已經在服務中並保持暖機，只需要追加副本。最終這次遷移在 10% 流量時被指標閘門偵測到 137% 的 p95 延遲回歸，系統自動暫停，工程師取消並反向執行，過程中沒有任何線上請求失敗。

🧩 怎麼建立一個 rollout

Together AI 提供 CLI 工具 tg（together Python package 2.34.0 以上版本），可以一行指令建立並啟動一個三階段的 canary rollout，並附加延遲回歸閘門：

```
tg beta endpoints rollout $TARGET_DEPLOYMENT_ID \
  --source $SOURCE_DEPLOYMENT_ID \
  --canary \
  --steps 10,50,100 \
  --interval 600s \
  --metric router_latency --metric-stat p95 \
  --metric-max-regression 10 --metric-direction higher-is-worse \
  --metric-window 300s
```

之後可以用 `tg beta endpoints get $ROLLOUT_ID` 觀察進度，或用 `--pause`、`--resume`、`--promote`、`--cancel` 等控制旗標介入流程。預設情況下，遷移完成後來源會縮減至零副本並停止（`--final-source-replicas` 預設為 0），目標則以來源的副本數作為底線起步（`--final-target-replicas`）。若需要多條指標規則，可透過 REST API 或主控臺設定，REST API 也將「建立」與「啟動」拆成兩個獨立呼叫。

🎯 實務啟示

如果你的團隊目前是靠人工盯著儀表板手動調流量比例來換模型，canary rollout 把「安全機制」從人腦搬進了平臺本身：目標先擴容、健康檢查先於流量、指標閘門守在每一步之後，出問題時反向回滾也是平臺原生支援的操作，而不是臨時寫腳本救火。對於高流量、延遲敏感的正式環境模型升級，這種模式值得作為預設流程，而不是遇到事故後才補上。

🔗 來源
- 標題：Canary rollouts: upgrade models in production without downtime
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/canary-rollouts-upgrade-models-in-production-without-downtime

#TogetherAI #CanaryRelease #MLOps #ModelDeployment #ProductionAI #LLMOps #DevOps #Qwen #AIInfrastructure #ZeroDowntime
