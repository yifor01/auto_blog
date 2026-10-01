---
title: '[AINews] Gemini 4 Argon: GDM’s answer to Astra/Fable, with 1M output'
source: Latent Space
url: https://www.latent.space/p/ainews-gemini-4-argon-gdms-answer
model: claude-code/sonnet
generated_at: '2026-10-01T22:08:56.162283'
score: 83
---

📌 【Google DeepMind】Gemini 4 Argon 登場，衝著 Astra、Fable 而來

TL;DR：Google 推出輸出上限 1M tokens 的 Gemini 4 Argon，宣稱 19 項基準測試中拿下 13 項第一，但目前僅限受邀預覽。

GDM 上一次推出比 Flash 更大的模型是今年二月的 3.1 Pro，之後幾個月陸續只有 3.x Flash 的小改款，再加上上個月的管理層大調整，業界最大的疑問一直是 Google 何時能追上同儕已經發布的 Astra、Fable 等級模型。答案是 Gemini 4 Argon，而且一出手就帶著業界首見的百萬輸出 token 能力。

🤔 **先給政府與資安團隊，一般開發者還得等**

根據 Latent Space 整理的 AI News，Google DeepMind 將 Gemini 4 Argon 定位在程式開發、企業知識工作與網路防禦場景，開放對象目前僅限政府使用者與 Fairwind Program 中的受信任資安防禦團隊，Google 表示會先完善防護機制（guardrails），之後才會開放給開發者、企業與一般消費者，開放時程只說「盡快」。

🧩 **Long Decode Continuation：百萬輸出 token 是怎麼做到的**

Argon 最受關注的特性是輸出上限從 64K 大幅拉高到官方宣稱的 1M tokens，不過 Vals 的測試顯示實際最大輸出是 262K；Artificial Analysis 說明他們是透過一項名為 Long Decode Continuation 的新 API 功能達到 1M tokens，做法是讓長篇回應在中途暫停、再透過後續呼叫接續產生，而不是一次性吐出百萬 tokens。定價方面，標準價為每百萬 tokens 輸入 $4、輸出 $20，目前有 50% 的早鳥折扣（無截止日期），折扣後為 $2/$10，cached input 則有 95% 折扣。

📊 **Google 自家公布的基準分數**

Google 宣稱 Argon 在 19 項公開基準測試中有 13 項拿下第一，對比對象是 GPT-6 Astra 與 Claude Opus 5.5。以 DeepSWE 為例，Argon 得分 77.9%，Opus 5.5 為 74.2%，Astra 為 74.1%。第三方機構 Artificial Analysis 的 Intelligence Index 評測中，Argon 得分 53 分，與 GPT-6 Astra（53 分）打平，略高於 GPT-6.1 Sol（52 分）。在每任務成本上，折扣價下 Argon 每任務約 $1.99，低於 Astra 的 $3.26，但如果用標準價計算則會升到 $3.98；Artificial Analysis 特別指出，這個成本優勢來自價格而非效率本身，因為 Argon 平均每個任務要用掉 62K 個輸出 tokens，遠高於 Astra 的 27K。在 agentic 任務上，Argon 在 AutomationBench-AA 拿下第一（77.5%），但在 Terminal Bench 4 只拿 57%，落後於 Sonnet 5.5、Opus 5.5 與 Astra。幻覺率方面，Argon 在 AA-Omniscience 上為 15%，遠低於 Astra 的 51%，但代價是準確率也較低，Argon 為 50%，Astra 為 63%。另一個評測機構 Vals 則給出 Vals Index 第一名（68.9%，平均每任務 $15.68）的結果，並指出 Argon 完美完成了 30 個 Vibe Code Bench 應用，高於 Opus 5（25 個）與 Astra（24 個）；Terminal-Bench 4.0 分數從前代的 19.0% 跳升到 57.6%，CyberBench 概念驗證任務拿下 70%，IOI 2024–2026 則是滿分 100%，且在 Vals Index 任務上平均只用掉 Sonnet 5.5 約四分之一的輸出 tokens。在 Arena 排名上，Argon 在 Text Arena 排名第一（1525 分），在 Code Arena WebDev 排名第八（1679 分），在 Agent Arena 初步 3000 場對戰中排名第八，但在「可操控性（steerability）」單項排名第一。PostTrainBench 分數為 45.3%，相較前代 Gemini 3.1 Pro 的 21.99% 有明顯提升。

💡 **內部用例：遷移 80 萬行 C/C++ 到 Rust**

Google 表示內部部署的 Argon agent 已經釋放超過 300 TiB 的資料中心記憶體，並正在將超過 80 萬行 C/C++ 核心程式碼遷移到 Rust；一個具體案例是影片解碼器，agent 用安全的 Rust 取代了 3.2 萬行 SIMD 程式碼，讓既有的 Rust 移植版本速度提升 2.7 倍，且輸出結果保持一致。Google 另外表示，建構在 Argon 上的內部 agent 迴圈協助完成了 CK 猜想的證明。

⚠️ **外界對數字的質疑不少**

並非所有人都照單全收這些基準數據。有評論者指出 Argon 在 Harvey 法律基準測試上的 19.6% 落後於 Muse Spark 1.2 公布的 25.42%；也有人質疑是否存在針對偏好資料做「benchmaxxing」的情況，並對包括 DeepSWE 在內的部分數字提出異議。

🎯 **實務啟示**

對正在評估模型的工程團隊來說，Argon 目前最大的限制不是效能而是取得管道：預覽僅開放給政府與資安團隊，一般開發者短期內用不到。即便日後開放，從數據上看 Argon 傾向用更多輸出 tokens 換取較低的幻覺率與較高任務成功率，這種「用 tokens 換品質」的取捨對成本敏感的應用未必划算，建議等正式開放後，針對自己的任務型態實測每任務成本與 tokens 消耗量，而不是只看官方或單一評測機構公布的排行榜數字。

🔗 **來源**
- 標題：[AINews] Gemini 4 Argon: GDM's answer to Astra/Fable, with 1M output
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-gemini-4-argon-gdms-answer

#GeminiArgon #GoogleDeepMind #LLM #AIBenchmarks #LongContextAI #AgenticAI #GPT6 #ArtificialAnalysis #CodingAI #AIIndustry
