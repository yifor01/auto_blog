---
title: 'Kev: Tiny Jev-like family of decision models built on top of Qwen3.5'
source: Hacker News
url: https://github.com/jaredpalmer/kev/tree/main
model: claude-code/sonnet
generated_at: '2026-09-21T21:22:24.422239'
score: 78
---

📌 Kev：可自行訓練的小型決策模型家族，站上 Qwen3.5 肩膀

TL;DR：Kev 是開源、可自訓自跑的 0.8B～9B 決策模型，API 相容 TypeSafe 的 System One SDK。

客服工單一進來，究竟該轉給退貨、物流還是帳務部門？這種「窄範圍是非題／選擇題／評分題」的判斷，過去多半得靠規則引擎或叫用大型 LLM API。Kev 想證明：一顆幾 GB 大小、能在自己機器上訓練與部署的模型，也能把這件事做好，而且答案帶著機率，不是非黑即白的單一標籤。

🤔 **為什麼要有自己的決策模型**

Kev 的介面刻意對齊 TypeSafe 的 System One，意味著原本用 TypeSafe Python SDK 呼叫雲端服務的專案，只要把 base_url 指向本地伺服器，幾乎不需要改程式碼就能換成自架模型。這對想要掌控資料、降低延遲或省下 API 成本的團隊來說，是很直接的動機。

🧩 **架構理念：三種問題共用輸入，但互不知情**

Kev 基於 Qwen3.5 的 0.8B、4B、9B 三種基底模型，架構參考「Jev's Architecture Unmasked」一文所述的設計。核心特色是同一次請求裡可以混合三種問題型態：
- noul：是非題（例如「這張工單需要緊急處理嗎？」）
- choice：多選題（例如判斷該轉給哪個部門）
- score：評分題（例如評估客戶憤怒程度）

這些問題共享同一段輸入文字，但彼此看不到對方的答案，避免一個問題的判斷污染另一個問題。輸出不是單一標籤，而是完整的機率分佈，README 給出的範例中，一張同時提到退貨、延遲出貨、重複扣款的工單，department 欄位就同時給出 returns 0.47、shipping 0.28、billing 0.25 的機率，如實反映了工單本身的模糊性。

模型內建校準機制：每個 checkpoint 會在自己的 development set 上擬合一個溫度值（約 2.1～2.4），載入時自動套用，只影響機率的可信度，不會改變最終答案本身。

🚀 **快速上手**

安裝與啟動只需要幾行指令：

```
git clone https://github.com/jaredpalmer/kev.git && cd kev
uv sync --extra serve
KEV_DTYPE=bf16 uv run --extra serve python -m kev.serve --run jaredpalmer/kev-4b --port 8009
```

啟動後用 curl 打 `/v1/systemone` 端點即可拿到 JSON 格式的判斷結果；也能透過內建的 TypeSafe SDK（`typesafe_sdk`）以 `Noul`、`Choice`、`Score` 物件描述問題。另外還附上一個以 Node 20.9+ 執行的網頁 playground，可以測試「一次問完 vs 逐一問」、「選項順序是否影響答案」等實驗，甚至有個西洋棋 demo，把棋盤當輸入、合法走法當 choice 選項。

📊 **三種規模的準確率與校準表現**

README 提供了在開發集／測試集上的比較：

| 模型 | 基底 | 已訓練來源準確率 | 新來源準確率 | 新來源 Brier 分數 |
|---|---|---|---|---|
| Kev-0.8B | Qwen3.5-0.8B-Base | 0.825 / 0.834 | 0.652 / 0.684 | 0.499 / 0.460 |
| Kev-4B | Qwen3.5-4B-Base | 0.872 / 0.871 | 0.797 / 0.837 | 0.299 / 0.255 |
| Kev-9B | Qwen3.5-9B-Base | 0.872 / 0.874 | 0.822 / 0.852 | 0.286 / 0.237 |
| Jev（託管服務） | – | 0.845 / – | 0.857 / – | 0.211 / – |

Kev-9B 在「新來源」開發集上的 Brier 分數落後 Jev 3.5 分（0.822 對 0.857），測試集上則拿到 0.852，但 Jev 並未在同一測試集上跑過，作者也坦言不清楚 Jev 的訓練資料組成，所以這並非嚴格對照的比較。

💡 **校準比原始答案更值得關注**

作者特別強調，校準是「事後套用溫度」而非改變模型判斷：在新來源資料上，Kev-9B 的校準誤差從 0.106 降到 0.042，高信心錯誤（機率 ≥0.9 但答錯）比例從 8.7% 降到 4.0%，接近 Jev 的 3.7%，但整體準確率沒有變化。這代表對於需要「知道模型有多不確定」的應用（例如自動化升級處理），Kev 提供的機率輸出比單純的準確率數字更有實務價值。

⚠️ **限制：日期運算能力仍然薄弱**

README 坦承 Kev 無法可靠地對日期做減法運算。透過 `KEV_DATE_FACTS=1` 這個選項，系統會先把輸入文字中兩個日期之間的天數算好、以文字形式附加進去，讓 Kev-9B 在涉及截止日期的政策判斷題上從 0.80 提升到 0.90（Jev 為 0.93），但這仍是繞過而非解決模型本身的弱點。此外，上一代基於 Qwen3 的 Kev 模型雖然在 Mac 上跑得更快，但已不再持續開發。

🎯 **實務啟示**

如果你的系統目前用雲端 LLM API 做工單分類、內容審核這類窄範圍判斷，Kev 提供了一條可以自己掌控、可離線訓練評估的替代路線。機率輸出加上內建校準，對需要「什麼時候該交給人工複審」這種閾值決策的場景尤其實用，但要留意日期推理等已知弱點，必要時搭配像 `KEV_DATE_FACTS` 這類前處理手段。

🔗 **來源**
- 標題：Kev: Tiny Jev-like family of decision models built on top of Qwen3.5
- 作者／機構：tosh（Hacker News 提交者）
- 連結：https://github.com/jaredpalmer/kev/tree/main

#Kev #Qwen3 #LLM #DecisionModels #OpenSource #MachineLearning #Calibration #AIAgents #ModelServing #TypeSafe
