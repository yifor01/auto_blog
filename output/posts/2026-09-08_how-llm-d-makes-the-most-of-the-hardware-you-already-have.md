---
title: How llm-d makes the most of the hardware you already have
source: IBM Research
url: https://research.ibm.com/blog/running-open-models-on-h100-gpus-with-llmd?utm_medium=rss&utm_source=rss
model: claude-code/sonnet
generated_at: '2026-09-08T20:07:46.905306'
score: 92
---

📌 219 個真實 session 告訴你：Agent 流量根本不是傳統 chatbot

TL;DR：IBM、Red Hat、Google 主導的開源推論框架 llm-d，靠六項能力在 544 張 H100 上把 753B 參數模型的自架成本壓到 API 的十分之一。

一個編碼 Agent 的請求，中位數帶進去將近 19.5 萬個 token，吐出來的卻只有 317 個。這種「讀多寫少」到誇張的比例，正在把過去針對 chatbot 設計的推論架構逼到極限。

🤔 Agentic 流量到底有什麼不一樣

隨著 AI Agent 能力提升，它們對推論基礎設施提出了新的要求。不同於傳統聊天機器人，像編碼助理這類 agentic 系統會重複處理巨量的上下文、在多次互動間重複使用資訊，並且會叫出並行的 sub-agent，產生難以預測的活動高峰。llm-d 團隊分析 219 個真實的 Claude Code session 後歸納出三個特徵：極長的上下文、大量重複使用先前資訊、以及來自 sub-agent 沒有預兆的並行爆發流量。其中一個數字特別驚人：96% 的主 agent 請求，逐字重複使用了前一個請求至少 90% 的輸入內容；此外超過一半的請求，是以並行子任務群組的方式毫無預警地同時抵達。這意味著計算的挑戰壓倒性地落在「處理輸入」而不是「生成文字」上，也代表能快取並重複利用先前計算結果的系統，會比每次都重新計算的系統更有優勢。

🧩 六項能力疊在一起才有效果

llm-d 把六項能力組合起來，用來減少重複的 context 處理、在高負載下保住 cache 命中率，並讓 prefill 與 decode 的產能可以獨立擴縮：

- **Prefix-aware routing**：把請求導向已經持有對應快取的伺服器，重複利用先前的計算而非從頭開始。在 CyberGym agentic benchmark 上，從近似路由改成精確的 prefix matching，吞吐量提升 79%，首個 token 生成時間（TTFT）降低 67%。
- **分層 KV-cache 管理**：把常用的快取延伸進 CPU DRAM，讓有用的 prefix 在 GPU 記憶體吃緊時能存活，而不是被驅逐後重算。
- **P2P KV-cache 共享**：如果最佳的快取命中在別的伺服器上，就直接從那個 peer 拉取，而不是在本地重新計算 prefix。
- **wide expert parallelism 搭配 data-parallel attention**：把模型分散到多個節點，同時避免 tensor parallelism 在 GLM-5.2 這種 multi-head latent attention 架構下會造成的 KV-cache 重複。
- **Prefill/decode 分離部署**：把上下文處理與 token 生成拆成兩個各自調校、可依需求獨立擴縮的資源池，兩池間透過 NVIDIA 的 NIXL zero-copy 傳輸函式庫溝通，整場 benchmark 沒有觀察到任何傳輸失敗。
- **Multi-token prediction（MTP）**：一次前向傳播生成多個輸出 token，在高並發下顯著提升輸出吞吐量，且因為建立在其他最佳化之上，增益會疊加。

📊 544 張 H100，3,000 個並行 coding agent

團隊用 llm-d 把 GLM-5.2（約 753B 參數、啟用約 39B 的 mixture-of-experts 開源權重模型）部署在 544 張 NVIDIA H100 GPU 上，採用分離式的 prefill／decode 拓撲。

| Benchmark | 條件 | 結果 |
|---|---|---|
| AutomationBench | 2,500 個並行 coding agent | 每分鐘 7,612 個請求，輸入峰值 1.3489 億 tokens/分鐘，輸出峰值 605 萬 tokens/分鐘，零 preemption |
| AutomationBench | 3,000 個並行 coding agent | 輸出達 660 萬 tokens/分鐘，逼近服務邊界但無 preemption 或失敗 |
| CyberGym | 400 個並行 agent，每個處理 37.6 萬字元的上下文、跑 10 輪 | 400 條 agent 軌跡全部在 248 秒內完成 |

在數百個並行 agentic session、高度重複使用上下文的工作負載下，該部署尖峰時每分鐘輸出超過 660 萬個 token，同時服務多達 3,000 個並行編碼 agent，且零 preemption。以目前的雲端租賃費率計算，在 H100 上自架 GLM-5.2 搭配 llm-d，每個 token 的成本比對等的商用 API 便宜 5 到 10 倍，其中在 Agentic 工作負載典型的輸入密集流量上，省下的成本最多。

💡 重點不是單一技巧，是六項一起在生產環境跑

IBM Research 傑出工程師、llm-d maintainer Carlos Costa 表示，他們想證明的是自架的開源權重模型能在多數組織已經擁有的 GPU 上，於長上下文的 agentic 工作負載中，跑出有競爭力的互動式吞吐量；llm-d 已經證明能在這種規模下運作，這次是把同等規模的模型部署驗證，延伸到一般企業與雲端 GPU 機隊常見的上一代硬體 H100 上。他也強調，llm-d 的價值不在於單一功能，而在於這六項能力一起在生產環境的實際基礎設施上協同運作。

🎯 實務啟示

如果你的團隊正在評估要不要自架開源模型來承接 Agentic 流量，這份benchmark 給出的訊號是：與其單純堆算力，先補上 prefix-aware routing、分層 KV-cache、P2P cache 共享這類「減少重複計算」的能力，可能是投報率更高的優化方向，尤其是輸入密集、上下文重複使用率高的編碼 Agent 場景。

🔗 來源
- 標題：How llm-d makes the most of the hardware you already have
- 作者／機構：IBM Research
- 連結：https://research.ibm.com/blog/running-open-models-on-h100-gpus-with-llmd?utm_medium=rss&utm_source=rss

#LLMInference #llmd #AgenticAI #KVCache #OpenSource #H100 #MixtureOfExperts #InferenceOptimization #IBMResearch #LLMServing
