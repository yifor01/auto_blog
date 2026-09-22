---
title: Claude Opus 5.5 is now available on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/claude-opus-5-5-is-now-available-on-aws/
model: claude-code/sonnet
generated_at: '2026-09-22T20:30:19.164944'
score: 90
---

📌 【Anthropic】Claude Opus 5.5 上架 AWS 怎麼接

TL;DR：Claude Opus 5.5 上架 AWS Bedrock，AWS 官方整理了呼叫方式與可用區域。

模型上新聞很常見，但工程師真正想知道的往往是更枯燥的問題：從哪個 API 呼叫、哪個 region 支援、怎麼監控用量。AWS 這篇部落格把 Claude Opus 5.5 上架 Bedrock 的細節，整理成了一份可以直接照做的清單。

🤔 **Claude 5.5 家族的第一個模型**

AWS 宣布 Claude Opus 5.5 正式在 Amazon Bedrock 與 Claude Platform on AWS 上線，是 Anthropic Claude 5.5 系列的第一款模型。根據 AWS 部落格的描述，這是 Anthropic 目前最強的 Opus 模型，適合 agentic coding、知識工作與長時間執行的任務。

🧩 **官方宣稱的改進：更省 token、溝通更清楚、思考力道可調**

根據 Anthropic 的說法，Opus 5.5 用更少的 token 就能做到 Opus 5 的效果，新的定價也把這部分效率提升直接反映給客戶：每 token 價格更低，快取讀取的費用更便宜，整體每個任務的平均成本比 Opus 5 更低，讓團隊能用同樣預算跑更多、更有野心的 agentic 工作。

Opus 5.5 也被訓練得更懂得表達自己在做什麼：執行過程中會主動說明做了什麼、發現了什麼、還需要什麼，讓長時間執行的任務更容易被追蹤。Adaptive thinking 這次是預設常駐開啟的，模型自己判斷每個任務該花多少推理力氣，開發者可以用 effort 這個參數當作控制旋鈕，取代過去手動設定思考預算的作法。

值得注意的是，Opus 5.5 是第一款搭載類似 Claude Fable 5.1 安全分類器的 Opus 模型，涵蓋生物、資安與 AI 開發領域，相較過去的 Opus 版本，它會更頻繁地拒絕請求。

AWS 部落格也點出兩個適用場景：軟體開發上，Opus 5.5 在長時間執行的 session 中比 Opus 5 更清楚地溝通、也更容易被理解與信任；知識工作上，處理與撰寫長文件、報告時，需要的人工修正比 Opus 5 更少。

🧩 **怎麼開始用：Console、SDK 到監控**

最直接的方式是打開 Amazon Bedrock console，依序點選 Test → Playground，選擇 Claude Opus 5.5，就能直接對它下 prompt 測試。

程式化呼叫的話，可以透過 Anthropic Messages API 呼叫 bedrock-runtime 與 bedrock-mantle（透過 Anthropic SDK）；也可以繼續用原本熟悉的 Invoke 與 Converse API，經 AWS CLI 或 AWS SDK 呼叫 bedrock-runtime。文章提供了用 AWS SDK for Python（Boto3）呼叫的範例，也示範了用 Bedrock Converse API 做統一多模型呼叫，以及直接用 anthropic 這個 SDK 套件呼叫 Anthropic Messages API 的方式。想看更完整範例，可以參考 Getting Started notebook。上線之後，用量、效能與成本可以透過 Amazon CloudWatch 與 AWS Cost Explorer 追蹤。

📊 **可用區域**

Claude Opus 5.5 目前已在 Bedrock 上透過 US、EU、AU、JP 以及 Global 這幾組 Geo CRIS inference profile 提供服務（走 bedrock-runtime），並且直接跑在美國東部（維吉尼亞北部）與亞太東南部（墨爾本）兩個 region 上（走 bedrock-mantle）。完整支援區域清單可查 Amazon Bedrock 文件，定價資訊則列在 Amazon Bedrock pricing 頁面。除了 Bedrock，北美地區也可以透過 Claude Platform on AWS 使用這個模型。

🎯 **實務啟示**

如果你已經在用 Bedrock 呼叫 Claude 系列模型，切到 Opus 5.5 理論上不需要改動太多程式碼，主要差異在於用 effort 取代原本的思考預算設定，以及安全分類器可能讓部分請求被拒絕的機率提高，值得在正式上線前針對自己的 use case 多測幾輪。多 region 的 CRIS profile 支援，也代表跨區域部署、延遲最佳化的彈性比想像中大。

🔗 **來源**
- 標題：Claude Opus 5.5 is now available on AWS
- 作者／機構：Aamna Najmi @ AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/claude-opus-5-5-is-now-available-on-aws/

#Anthropic #ClaudeOpus #AmazonBedrock #AWS #LLM #AgenticAI #GenerativeAI #CloudAI #MachineLearning #APIIntegration
