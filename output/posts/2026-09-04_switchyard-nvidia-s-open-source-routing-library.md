---
title: 'Switchyard: NVIDIA’s Open Source Routing Library'
source: KDnuggets
url: https://www.kdnuggets.com/switchyard-nvidias-open-source-routing-library
model: claude-code/sonnet
generated_at: '2026-09-04T19:46:50.339958'
score: 98
---

📌 NVIDIA開源Switchyard：讓便宜模型先接手

TL;DR：NVIDIA開源路由層 Switchyard，依任務難度自動在便宜與強力模型間切換，直接省成本與延遲。

你的AI agent是不是不管任務難易，一律把請求丟給最貴的frontier model？分類步驟、簡單工具呼叫、進度檢查、真正需要推理的難題，全部打到同一個endpoint，結果就是白白多花的成本與延遲。

🤔 **每個請求都用最貴模型，其實是浪費**

多數正式環境中的AI agent，架構長得像「Application → GPT／Claude／本地LLM」，沒有分流機制。NVIDIA NeMo Switchyard要解決的正是這件事：它是一層開源的路由代理（proxy + library），插在你的agent與模型之間，逐請求或逐輪次決定該由哪個模型處理。應用端不需要知道最終是哪個模型在服務，Switchyard負責選定實際目標並轉發。

🧩 **從隨機路由到分類器路由**

安裝方式很單純，透過uv：

```
uv tool install "nemo-switchyard[cli,server]"
```

驗證版本會看到 `switchyard 0.2.0`。若走原生Rust伺服器，也可以用 `cargo install --locked switchyard-server`。教學中示範透過OpenRouter串接模型，需要先 export `OPENROUTER_API_KEY`（切記不要把金鑰直接寫進設定檔）。

最簡單的設定是兩個模型加隨機路由，設定檔中的關鍵欄位是 `strong_probability: 0.3`，意思是大約30%的請求會落到強力模型（如 `openai/gpt-4o`），70%落到較弱模型（`openai/gpt-4o-mini`）。這種隨機路由本身不算「智慧」，但很適合拿來做A/B測試，也能在導入分類器之前先驗證代理是否正常運作——啟動伺服器（`switchyard serve -c routes.random.yaml`）失敗就代表設定有誤，這本身就是驗證步驟。

真正進階的是分類器路由（`type: deterministic`）。設定裡多了一個classifier角色，同樣用一個較便宜的模型（如 `gpt-4o-mini`）先判斷：這個請求，弱模型能不能解決？分類器會輸出一個叫 `p_solve` 的估計值（弱模型成功完成任務的機率），再依門檻決定要不要升級到強模型。

📊 **實測：簡單問題與難題走了不同路**

教學中送出兩種請求進行比較：

| Prompt | 實際服務模型 | Tier | 延遲 |
|---|---|---|---|
| "What is 15% of 200?" | openai/gpt-4o-mini | weak | 1,428 ms |
| Redis race condition重新設計問題 | openai/gpt-4o | strong | 4,475 ms |

整個過程沒有寫死model名稱，客戶端呼叫的 `"model": "smart"` 只是一個路由標籤，實際模型由分類器依照prompt難度即時決定。文章也提到，Switchyard還支援根據coding agent的執行進度來路由——例如agent前期在探索檔案、除錯、推理架構，後期則多半在依既定計畫做重複性編輯，若每一輪都用最強模型，等於浪費推理預算，不過具體的進度判斷機制素材未展開細節。

🎯 **實務啟示**

對於已經在跑production agent的工程團隊，Switchyard提供了一條低成本的漸進路徑：先用random_routing驗證代理層可用，再換上classifier route依難度自動分流。比起手動硬編碼「這類任務用小模型、那類用大模型」，用session_affinity搭配分類器可以讓路由決策更貼近實際內容，而不用大動作重構應用程式碼。

🔗 **來源**
- 標題：Switchyard: NVIDIA's Open Source Routing Library
- 作者／機構：Kanwal Mehreen, KDnuggets
- 連結：https://www.kdnuggets.com/switchyard-nvidias-open-source-routing-library

#NVIDIA #LLMRouting #Switchyard #AIAgents #OpenSource #InferenceCost #LLMOps #MachineLearning #ModelRouting #AIInfrastructure
