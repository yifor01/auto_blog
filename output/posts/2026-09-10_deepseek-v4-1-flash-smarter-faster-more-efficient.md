---
title: 'DeepSeek-V4.1-Flash: Smarter, Faster, More Efficient'
source: DeepSeek
url: https://api-docs.deepseek.com/news/news260910
model: claude-code/sonnet
generated_at: '2026-09-10T19:53:27.084981'
score: 109
---

📌 【DeepSeek 官方公告】V4-Pro 即將下線，全面轉向 V4.1-Flash

TL;DR：DeepSeek 推出 V4.1-Flash 並宣布逐步淘汰 V4-Pro，API 呼叫方式與計價同步調整。

如果你的服務串接的是 DeepSeek API，這則公告值得馬上看：官方不只是發新模型，還附上了一份明確的舊模型退場時間表。

🤔 **新架構家族的第一個成員，主打小而強**

DeepSeek 將 V4.1-Flash 定位為新架構家族中最小的模型，具備原生視覺理解能力，設計目標是在更快推理、更高吞吐與可擴展到更大模型規模之間取得平衡。

🧩 **Causal Encoder-Decoder：輸入輸出各自的啟用參數**

官方公告點出的核心技術是「新的 Causal Encoder-Decoder 架構」：輸入端只啟用 8B 參數，輸出端啟用 16B 參數。搭配新的預訓練方法與更大規模的 RL 後訓練，官方表示其 benchmark 表現已超越旗艦模型，包括 DeepSeek-V4-Pro。公告同時強調，相較上一代，V4.1-Flash 的 KV cache 顯著壓縮，而由於 cache-hit 費用往往佔 Agent 使用成本的大宗，壓縮快取直接反映在成本下降上。

📊 **一份明確的遷移時間表**

這次公告最實用的部分其實是營運細節：
- 模型名稱請設定為 `deepseek-flash`。
- V4-Flash 與 V4-Flash-Vision-Exp 已退役，為了相容性，`deepseek-v4-flash` 與 `deepseek-v4-flash-vision-exp` 這兩個名稱暫時會被路由到 V4.1-Flash。
- 多方測試顯示 V4.1-Flash 在效能、成本、速度與總執行時間上都優於 V4-Pro，因此官方正在逐步淘汰 V4-Pro：自 2026 年 9 月 14 日 04:00 UTC 起，所有 `deepseek-v4-pro` 的請求都會被路由到 V4.1-Flash，並以 V4.1-Flash 的費率計費，這個安排會持續到 V4.1-Pro 上線為止。
- 官方合作夥伴 WorkBuddy（含 CodeBuddy）與 OpenCode 已完整支援 V4.1-Flash。

💡 **計價策略維持尖峰/離峰，但門檻更低**

新定價已於 2026 年 9 月 10 日 04:00 UTC 生效。官方延續尖峰/離峰的差別定價策略，離峰費率是尖峰費率的 50%，適合把可彈性排程的工作挪到離峰時段執行。官方也表示 V4.1-Flash 讓他們能以更低成本服務更多使用者，並將這部分節省下來的成本回饋給客戶。針對大規模部署（官方舉例為 2,000 張 GPU 加上儲存叢集規模），DeepSeek 也開放直接聯繫洽談。

🎯 **實務啟示**

如果你的系統目前寫死呼叫 `deepseek-v4-pro` 或 `deepseek-v4-flash`，建議盡快確認遷移計畫：雖然官方提供相容路由，但費率會切到 V4.1-Flash 的計價，行為與延遲特性也可能隨新架構而變化，值得在 9 月 14 日大限前先做一輪回歸測試。對於重度使用 Agent 快取命中的場景，這次的 KV cache 壓縮也是直接可以感受到帳單變化的地方。

🔗 **來源**
- 標題：DeepSeek-V4.1-Flash: Smarter, Faster, More Efficient
- 作者／機構：DeepSeek
- 連結：https://api-docs.deepseek.com/news/news260910

#DeepSeek #DeepSeekV4 #LLMPricing #AIAPI #AgenticAI #ModelDeprecation #CloudAI #Inference #AIInfra #CostOptimization
