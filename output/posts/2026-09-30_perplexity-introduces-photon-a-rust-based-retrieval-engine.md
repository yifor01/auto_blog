---
title: 'Perplexity Introduces Photon: A Rust-Based Retrieval Engine That Cuts p99
  Latency From 800 ms to 65 ms'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/30/perplexity-introduces-photon-a-rust-based-retrieval-engine-that-cuts-p99-latency-from-800-ms-to-65-ms/
model: claude-code/sonnet
generated_at: '2026-09-30T21:43:47.067953'
score: 91
---

📌 Perplexity自研Rust引擎 p99延遲砍至65毫秒

TL;DR：Perplexity 用 Rust 打造全新檢索引擎 Photon，取代原本的開源 fork，並以 API 形式對外開放 Fast Search 模式。

查詢送出後要等 800 毫秒才看到結果，跟等 65 毫秒的差別，對即時 agent 應用來說幾乎是能不能用的分水嶺。Perplexity 這次直接把底層檢索引擎整套換掉。

🤔 **舊引擎撐不住成長中的索引**

Perplexity 原本的 AI 原生搜尋堆疊，用的是一套經過自行 fork 的開源檢索引擎。隨著索引規模持續擴大，這套 fork 陸續碰上瓶頸，團隊評估後認為，從零打造一套新引擎，反而比繼續維護 fork 來得簡單也更省成本，於是有了 Photon。

🧩 **Broker 分派、Shard 兩階段排序**

Photon 的架構是負載平衡器把每個請求導向一個 Photon broker，broker 再把請求分散給一組 shard，並監控逾時狀況。每個 shard 各自完成檢索、初步排序與第二階段排序，broker 最後合併候選結果並抓取關鍵文件欄位。目前完整的網頁索引可以在個位數小時內建置完成。Fast Search 模式則是把 Photon 搭配一套針對 agentic 工作流程調校過的輕量排序邏輯。

📊 **同樣任務省下近七成成本，但準確度打了折扣**

Perplexity 在 WideSearch、BrowseComp、DSQA、FRAMES、SEAL-0、SEAL-Hard 這 6 個 benchmark、共 3,554 個任務上做了測試：Fast 模式拿下 64.3% 的分數，估計模型加搜尋成本為 59.73 美元；預設模式拿下 64.0%，成本卻要 187.60 美元，Fast 模式便宜了約 68%。

不過代價也反映在內部長尾 benchmark 上：relevance（DCG）從 2.45 降到 2.21，答案可用率從 0.596 降到 0.567，下滑 2.9 個百分點。Photon 本身的單次呼叫延遲為 p50 160 毫秒、p95 230 毫秒。

💡 **兩種模式各有適用場景**

Perplexity 建議把 Fast 模式用在日常的 agent 迴圈中，而困難、語意模糊的查詢則建議維持使用預設模式。要留意的是，這些延遲數字都是 Perplexity 自行提供、在不同設定下測得，並非同一基準下的公平比較。

🎯 **怎麼用：API 開個參數就能切換**

Photon 目前不開源，也無法自行架設，只能透過 Perplexity 的託管 API 使用。在 POST /search 呼叫中設定 search_type: "fast"，費用為每 1,000 次請求 1 美元；若使用 Python SDK 0.43.4 或 0.43.5，依官方文件傳入 extra_body={"search_type": "fast"} 即可。

🔗 **來源**
- 標題：Perplexity Introduces Photon: A Rust-Based Retrieval Engine That Cuts p99 Latency From 800 ms to 65 ms
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/30/perplexity-introduces-photon-a-rust-based-retrieval-engine-that-cuts-p99-latency-from-800-ms-to-65-ms/

#Perplexity #Rust #SearchEngine #Latency #AgenticAI #InfoRetrieval #APIPricing #Benchmarking #SearchAPI #SystemsEngineering
