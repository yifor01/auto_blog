---
title: Decisions API is in public beta
source: Hacker News
url: https://developers.openai.com/api/docs/guides/decisions
model: claude-code/sonnet
generated_at: '2026-10-07T22:17:45.939116'
score: 97
---

📌 【OpenAI 新品】Decisions API 公測，結構化判斷快 10 倍

TL;DR：OpenAI Decisions API 公測上線，用單一端點回傳機率、分類或評分，據稱比 Responses API 快約 10 倍。

一篇在 Hacker News 衝到 381 分、221 則留言的貼文，主題其實是工程師每天都在手動解決的問題：怎麼快速用 LLM 做分類、路由、排序這類結構化判斷。過去得自己寫 prompt、解析回傳的 JSON、再處理各種邊界情況，OpenAI 現在把它收斂成一個專用的 API 端點。

🤔 不是每次呼叫都需要「生成」

當應用程式需要的只是「這個條件成立的機率有多高」「該選哪個固定選項」「依照評分標準打幾分」，用完整的 Responses API 跑一輪生成流程其實是殺雞用牛刀。Decisions API 針對文字、影像或兩者混合的輸入，直接回傳型別化（typed）的答案，速度號稱比 Responses API 快約 10 倍。

🧩 一個請求，三個部分

每個請求包含三個欄位：

| 欄位 | 用途 |
|---|---|
| model | 評估請求的模型，目前只支援 gpt-6-luna |
| input | 問題共用的證據，可以是純文字，也可以是含文字與影像的訊息 |
| questions | 要評估的內容，包括每個問題的類型、指示，以及允許的選項或評分等級 |

每個問題可以取一個獨一的名稱，API 會在回傳的 `answers` 陣列中原樣回傳這個名稱，方便對應結果。

三種問題類型對應三種用途：

- **predicate**：檢查某個條件是否成立，例如「這張照片上的商品有明顯損傷嗎？」，回傳 0 到 1 之間代表該條件成立機率的 `probability`。
- **choice**：從一組固定選項中選一個，例如該由哪個部門處理，回傳其中一個 `choice` 值，適合沒有順序關係的分類。
- **score**：依照有序等級評分，例如問題嚴重程度，結果是各等級機率加權後的平均值，因此分數可以落在等級之間，適合有順序關係的評估。

官方建議：需要上述三種型別答案時用 Decisions API；需要依照自訂 JSON schema 產生物件（例如抽取欄位、生成說明文字）時用 Responses API 搭配 Structured Outputs；需要模型請求帶參數的工具呼叫時用 function calling。

目前支援的 SDK 版本為 Python 3.26.0、JavaScript 7.30.0、Go 3.73.0、Ruby 0.101.0、Java 4.78.0 及以上。

🎯 一個檢查商品損傷的實例

以下是用 predicate 問題檢查商品照片是否有明顯損傷的簡化範例：

```python
decision = client.decisions.create(
    model="gpt-6-luna",
    input=[{
        "role": "user",
        "content": [
            {"type": "input_text", "text": "Inspect the product in this photo."},
            {"type": "input_image", "image_url": f"data:image/png;base64,{image_base64}"}
        ]
    }],
    questions=[{
        "type": "predicate",
        "name": "visible_damage",
        "instructions": "Does the product have visible damage, such as a crack, tear, or dent?"
    }]
)
```

類似的邏輯可以套用在工單分類、客服回覆相關性檢查、內容審核或優先度評分等場景，端點固定為 `POST /v1/decisions`。

⚠️ 公測階段的限制

目前 Decisions API 仍在公測，官方預期「未來幾週內」會正式 GA（正式發布），目前唯一可用的模型是 gpt-6-luna；若需要產生自訂結構的 JSON 物件，仍得搭配 Structured Outputs 與 Responses API，而非 Decisions API。

🎯 實務啟示

如果你的應用程式大量呼叫 LLM 只是為了拿到「是否、選哪個、打幾分」這類結構化判斷，Decisions API 省去了自行解析生成文字的環節，也避免了用完整生成管線處理簡單判斷的延遲成本，值得在內容審核、工單路由、優先度排序等場景先行試用評估。

🔗 來源
- 標題：Decisions API is in public beta
- 作者／機構：OpenAI（Hacker News 貼主：chiefstorm）
- 連結：https://developers.openai.com/api/docs/guides/decisions

#OpenAI #API #LLM #MachineLearning #AIEngineering #StructuredOutputs #ContentModeration #DeveloperTools #GPT6 #AIProductivity
