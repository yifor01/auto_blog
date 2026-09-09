---
title: DeepSeek launching v4.1 flash cheaper and more capable than v4 pro
source: Hacker News
url: https://news.ycombinator.com/item?id=49624603
model: claude-code/sonnet
generated_at: '2026-09-09T20:07:39.718111'
score: 79
---

📌 DeepSeek V4.1 Flash 即將上線，效能超越 V4 Pro 且更便宜

TL;DR：DeepSeek V4.1 Flash 上線後，Pro 模型的請求會直接轉發到 Flash 並以 Flash 價格計費。

如果你的 API 請求打的是 Pro 模型，帳單卻是 Flash 的價格，這不是計費出錯，而是 DeepSeek 這次更新的設計。

🤔 **Pro 模型的請求，悄悄被轉去跑 Flash**

DeepSeek 計畫於北京時間 2026 年 9 月 10 日左右正式發布 V4.1 Flash。根據官方說法，經過大量內部與外部測試後，V4.1 Flash 在效能、成本、速度與任務完成時間等關鍵指標上，已全面超越 V4 Pro。基於對使用者負責的原則，DeepSeek 表示在 V4.1 Flash 正式上線、V4.1 Pro 尚未發布之前，所有打向 Pro 模型的請求都會被轉發到 V4.1 Flash 執行，並以 Flash 的價格計費。官方也提到，如果使用者在比較 V4 Pro 與 V4.1 Flash 的過程中發現任何問題，歡迎回饋。

📊 **Flash 系列調價，離峰與尖峰價差一倍**

Flash 系列的價格將於北京時間 9 月 10 日中午 12 點起調整：

| 項目 | 離峰時段 | 尖峰時段 |
|---|---|---|
| Input（cache hit） | $0.003 | 離峰的兩倍 |
| Input（cache miss） | $0.15 | 離峰的兩倍 |
| Output | $0.6 | 離峰的兩倍 |

（以上單價皆為每百萬 token，尖峰時段價格為離峰時段的兩倍）

🎯 **對接 API 的工程師，記得重新檢視成本模型**

如果你的應用原本呼叫的是 V4 Pro，接下來實際跑的運算會變成 V4.1 Flash，計費也一併切換成 Flash 價格，值得重新檢視尖峰／離峰的使用時段分布，並在正式調價生效前，用官方提供的比較管道確認輸出品質與延遲是否符合原本 Pro 模型的預期。

🔗 **來源**
- 標題：DeepSeek launching v4.1 flash cheaper and more capable than v4 pro
- 作者／機構：nickweb, Hacker News
- 連結：https://news.ycombinator.com/item?id=49624603

#DeepSeek #LLM #AIModels #OpenSourceAI #ModelPricing #InferenceCost #AIInfrastructure #APIDevelopment #ChinaAI #MachineLearning
