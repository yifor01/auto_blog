---
title: OpenAI Decisions API Hits Public Beta With 10x Faster Typed Answers
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/09/openai-decisions-api-hits-public-beta-with-10x-faster-typed-answers/
model: claude-code/sonnet
generated_at: '2026-10-09T22:01:09.403710'
score: 85
---

📌 OpenAI推出Decisions API：讓模型直接吐出「程式碼能分支」的答案

TL;DR：新端點把LLM判斷轉成型別化答案，官方宣稱比Responses API快約10倍。

寫過 agent 或分類管線的人都懂這個痛點：你要的不是一段漂亮的文字，而是一個程式碼可以 if-else 的標籤，卻還是得先讓模型生成一整段 prose，再自己寫 parser 去抽取答案。OpenAI 這次直接把這個 pattern 做成了端點。

🤔 **一個只回答「是非題」的端點**

OpenAI Decisions API 已進入公開 Beta。它評估文字、圖片，或兩者皆有，回傳型別化的答案，而不是生成散文。目前唯一支援的模型是 gpt-6-luna，OpenAI 預期未來幾週內會正式 GA。

🧩 **一個請求裡裝著共用證據與一串問題**

一個 Decisions 請求只有 3 個欄位：model、input、questions。每個 question 都有自己的 name、type 與 instructions，而請求整體攜帶的是共用的 evidence（也就是 input）。回應則是一個 answers 陣列，用這些 name 做 key 對應。

OpenAI 用一個嚴重性分級的範例把機制講得很具體：假如某個嚴重度分類的三個等級機率分別是 0.1、0.7、0.2，加權後得到的分數是 1.1，正好落在「有變通方案（Workaround available）」與「完全阻斷（Fully blocked）」兩個等級之間，程式碼可以直接依這個連續分數做路由判斷，而不需要自己去解析模型吐出的文字再對應等級。

OpenAI 也劃清了三個端點的使用邊界：要機率、選項或分數,用 Decisions；要填自己的 JSON schema 或需要附帶解釋文字,用 Structured Outputs；要模型請求帶參數的工具呼叫,用 function calling。

📊 **號稱快10倍，但沒有附上準確度數據**

OpenAI 文件宣稱 Decisions API 比 Responses API 快約 10 倍。DevDay 現場揭露的數字則是：一次 decision 大約 150 毫秒,相較於一般 Luna 呼叫約 1.6 秒。計費上，gpt-6-luna 的輸入成本是每 100 萬 token 0.10 美元,沒有輸出、cache 讀取或 cache 寫入費用,但區域處理的溢價與長上下文倍率仍然適用——Luna 的 model card 顯示超過 272K token 的 prompt 會以 2 倍輸入費率計價。

值得留意的是，OpenAI 並未公布這個端點的準確度或校準（calibration）數據，文件建議開發者自己用標註過的範例來設定判斷門檻。

💡 **市場上已經有更便宜的對手**

最接近的競品是 2026 年 9 月 15 日上線的 TypeSafe Jev，一款 System One 模型，同樣回傳帶校準機率的型別化數值。Jev 的輸入定價是每 100 萬 token 0.042 美元,輸出免費,換算下來 OpenAI 的基礎費率大約是它的 2.4 倍。Jev 號稱端到端延遲在 70 到 500 毫秒（從美國西岸量測）,支援最多 255 個選項,但目前仍在早期存取階段。OpenAI 的優勢則在於支援圖片輸入、提供合規選項,以及已經開放公開 Beta。

⚠️ **沒有準確度數據就是最大的風險**

速度和價格都好比較，但一個決策端點最該被驗證的其實是它判斷得準不準、機率校準得好不好。OpenAI 目前沒有公開這類資料，意味著團隊在接上生產環境前，自己動手用標註資料驗證門檻設定幾乎是必要步驟。

🎯 **實務啟示**

如果你的 pipeline 裡還在用「prompt 模型生成文字 → regex 或字串比對抽取標籤」這種做法，Decisions API 提供的是一個結構上更直接的替代方案，尤其適合分類、評分、路由這類需要連續機率而非單一標籤的場景。但在導入前，務必自己驗證校準品質，而不是直接信任官方宣稱的速度數字。

🔗 **來源**
- 標題：OpenAI Decisions API Hits Public Beta With 10x Faster Typed Answers
- 作者／機構：Sana Hassan／MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/09/openai-decisions-api-hits-public-beta-with-10x-faster-typed-answers/

#OpenAI #DecisionsAPI #LLM #StructuredOutputs #AIEngineering #API #MachineLearning #GPT #AIInfrastructure #FunctionCalling
