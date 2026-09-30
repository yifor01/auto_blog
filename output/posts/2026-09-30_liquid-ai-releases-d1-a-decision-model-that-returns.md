---
title: 'Liquid AI Releases d1: A Decision Model That Returns Calibrated Probabilities
  With Zero Output Tokens'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/29/liquid-ai-releases-d1-a-decision-model-that-returns-calibrated-probabilities-with-zero-output-tokens/
model: claude-code/sonnet
generated_at: '2026-09-30T21:41:34.934970'
score: 95
---

📌 Liquid AI發布d1：每次呼叫輸出token數永遠是0

TL;DR：d1是不寫文字的決策模型，回傳固定選項的校準機率，API已可用。

當多數團隊還在用完整的LLM做分類、路由、審核這類「選答案」任務時，Liquid AI選擇反其道而行，直接砍掉輸出token，讓模型只回傳機率。

🤔 背景：這解決什麼問題

Liquid AI推出的d1，鎖定的正是許多團隊目前仍丟給一般LLM處理的工作：分類、工單路由、評分、內容審核、重排序，以及LLM-as-judge這類判斷型任務。官方定義很直接：決策模型會評估一個情境，並從你事先定義好的選項中回傳一個有型別的答案，它不寫文字，每一次回應中usage.output_tokens都是0。Liquid的遷移指南給了一個簡單原則：如果答案是N個已知選項之一，就用決策模型；如果模型必須組出一段全新的字串，就繼續用LLM。

🧩 方法或架構：一次呼叫三種提問

d1目前以Liquid API的方式提供服務，模型名稱是d1:free，可以直接串接使用。根據Liquid的模型庫說明，它是「僅限API」且「不可訓練」，因此沒有GGUF、MLX或ONNX格式的權重可以自行部署。每個請求包含三個部分：模型、state（可以是純文字或JSON物件），以及questions。一次請求裡可以混用三種提問類型，模型會在同一次往返中針對同一個state評估所有問題。呼叫端點是POST https://api.liquid.ai/decisions/v1/systemone，API金鑰從console.liquid.ai取得，開頭是liquid_。官方提供Python的typesafe-sdk與TypeScript的@typesafe-ai/sdk兩種客戶端，皆由TypeSafe AI提供。

📊 數據或結果：機率讓門檻值變得可用

Liquid官方的內容審核範例：機率超過0.8就封鎖，低於0.2就放行，中間地帶交由人工審查。路由範例則是當路由器的信心分數低於0.5，系統就會退回到能力最強的模型層級處理。Liquid也表示，同一筆輸入重複評估時結果更一致，能減少判定結果忽上忽下的情況。

💡 深入分析：道路決策Demo與狀態設計的教訓

Liquid提供的road-decider cookbook是一款像素風的生存賽車遊戲：d1用一個Choice問題，在每個決策時間點選擇往左、置中或往右，依遊戲速度大約每秒判斷2到5次。這個範例用純JavaScript寫成、跑在Node.js 18以上，並透過Vite proxy把API金鑰留在伺服器端，不外洩到前端；其中還有個「Jev vs d1」模式，讓d1透過OpenRouter和TypeSafe的typesafe/jev-1.13模型互相競速。從這個demo得到的教訓是：state的設計方式很關鍵，官方發現把賽道拆成「每個車道的摘要＋到第一個障礙物的距離」，會比丟一整張原始賽道網格資訊，讓模型做出更有信心的決策。

⚠️ 限制

d1完全走API-only路線，沒有開放權重，無法自行部署或微調。官方也明確劃出界線：摘要、草擬文案、多輪對話、程式碼生成、複雜多步驟推理，這些仍然要交給一般LLM，決策模型不是萬用替代品。

🎯 實務啟示

如果你手上的任務本質是「從已知選項中選一個」，例如工單分類、審核分級、路由決策，d1這類決策模型能省下生成token的成本與延遲，機率輸出也讓你可以設計清楚的門檻策略，例如高分自動放行、低分自動擋、中間交給人工。這個賽道目前正快速形成小型但活躍的競爭格局，Liquid的d1與TypeSafe的Jev已經被直接放在一起比較，值得持續關注這類「零輸出token」模型的定價與能力邊界。

🔗 來源
- 標題：Liquid AI Releases d1: A Decision Model That Returns Calibrated Probabilities With Zero Output Tokens
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/29/liquid-ai-releases-d1-a-decision-model-that-returns-calibrated-probabilities-with-zero-output-tokens/

#LiquidAI #DecisionModels #LLM #API #MachineLearning #Classification #ModelRouting #ContentModeration #AIInfrastructure #TypeSafeAI
