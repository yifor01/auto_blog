---
title: Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio
source: Apple ML
url: https://machinelearning.apple.com/research/mlx-distributed-inference
model: claude-code/sonnet
generated_at: '2026-10-15T20:30:53.900587'
score: 105
---

📌 四臺 Mac Studio 串連，跑出 816B 模型的 36 tokens/s

TL;DR：Apple 公開 MLX 分散式推論實測，用 RDMA over Thunderbolt 串連多臺 Mac Studio，在桌面環境跑起近兆參數的模型。

兆級參數的模型通常意味著要排隊搶雲端 GPU 機房的資源。這篇文章給出的實測數據卻是：四臺 Mac Studio 用 Thunderbolt 接起來，就能讓一個 816B 參數的模型產生超過人類平均閱讀速度的輸出。

🤔 **MLX 在地端跑模型的起點**

MLX 是 Apple silicon 上的開源陣列框架，利用 Apple silicon 的統一記憶體架構，讓研究者與開發者能在私有環境中直接跑最新的模型與方法。這篇文章示範如何用最新版 MLX，從單臺 Mac Studio 開始，一路擴展到透過 RDMA over Thunderbolt 驅動程式串連多臺 Mac Studio，跑起當前的旗艦級模型 Muse Spark Open（近兆參數）。

macOS 26.2 引入了低延遲的 RDMA over Thunderbolt 5 驅動程式，MLX（v0.30.1 及之後版本）在此基礎上提供了新的通訊集合操作 `jaccl`（念作「jackal」），支援不同的平行化方案。

🧩 **測試設定：三個模型，兩代晶片**

文章用 MLX LM 套件在 Mac Studio 上，比較 M5 Ultra 與前一代 M3 Ultra 的表現，測試對象涵蓋三個不同規模的頂尖開放權重模型：

| 模型 | 總參數 | 啟用參數 | 原生精度 | 評測精度 |
|---|---|---|---|---|
| Muse Spark Open | 816B | 42B | BF16 | NVFP4 |
| Mistral Medium 3.5 | 128B | 128B | FP8 | FP8 |
| Qwen 3.8 | 27B | 27B | BF16 | BF16 |

Muse Spark Open 是 MoE 模型，推論時只動用一部分專家，評測採用 NVFP4 精度；Mistral Medium 3.5 與 Qwen 3.8 則是密集架構，所有參數都會參與運算，分別以原生的 FP8 與 BF16 精度評測。

評測指標涵蓋首個 token 產生時間（TTFT）、生成吞吐量（tokens/秒）與峰值功耗，測試情境涵蓋 8,192 與 65,536 兩種上下文大小，貼近 agentic coding 應用常見的長上下文需求。指令範例如下：

```
mlx_lm.benchmark --model Qwen/Qwen3.8-27B -p 8192 -g 128 -b 1
```

📊 **單臺機器能跑什麼，跑多快**

Qwen 3.8 與 Mistral Medium 3.5 在 512GB 記憶體的單臺 Mac Studio 上都能輕鬆容納，在 65,536 token 的大上下文情境下分別佔用最多 68GB 與 158GB 記憶體。

TTFT 是計算瓶頸（compute bound），這正是 M5 Ultra GPU 上 Neural Accelerator 專用矩陣乘法硬體發揮作用的地方：相較 M3 Ultra，TTFT 最多快了 4.6 倍。生成速度則受記憶體頻寬限制（memory-bandwidth bound），M5 Ultra 提供 1.2TB/s 的統一記憶體頻寬，相較 M3 Ultra 的 819GB/s 大幅提升，直接反映在生成速度上，M5 Ultra 比 M3 Ultra 快 1.6 倍。

峰值功耗方面，M3 Ultra 的 Mac Studio 約 200W，M5 Ultra 約 300W，都遠低於一般烤麵包機的耗電量，意味著 Mac Studio 可以部署在任何家庭或辦公室環境執行 AI 工作負載。

🧩 **當模型大到放不進一臺機器：分散式推論**

Muse Spark Open 若以原生 BF16 精度載入，模型參數本身就需要超過 1.6TB 記憶體；即便量化為 4-bit 的 NVFP4，模型的記憶體佔用也降到約 493GB，加上推論過程中間運算所需的記憶體，仍無法容納在單一機器上，必須跨多臺 Mac Studio 做平行化。

MLX 支援兩種切分方式：管線平行化（pipeline parallelization）是把模型依「深度」切開，例如讓第一臺 Mac Studio 執行模型的前半層，算完再把輸出傳給第二臺機器執行後半層，實作上只需要很小的程式碼改動；張量平行化（tensor parallelization）則是把模型依「寬度」切開，分散到多臺機器上。這些方案都仰賴機器之間的高速通訊，也就是前面提到的 RDMA over Thunderbolt 與 `jaccl` 通訊集合操作。

📊 **四臺機器，36 tokens/s**

在 8,192 token 的上下文大小下，文章比較了三種平行化方案：兩臺 Mac Studio 的管線平行化、兩臺與四臺 Mac Studio 的張量平行化。結果顯示，在四臺搭載 M5 Ultra 的 Mac Studio 以張量平行化運作下，Muse Spark Open 的生成速度超過每秒 36 個 token，高於人類平均閱讀速度。

💡 **TTFT 與生成速度，吃的是不同的硬體資源**

這組數據清楚區分了兩種瓶頸：TTFT 吃的是運算能力，所以 M5 Ultra 的 Neural Accelerator 專用矩陣乘法硬體帶來明顯加速；生成速度吃的則是記憶體頻寬，M5 Ultra 在這塊的優勢同樣直接反映在 tokens/秒上。這個區分對選擇硬體世代、評估能否跑長上下文的 agentic 應用相當關鍵。

🎯 **實務啟示**

對想在私有環境跑大型模型、又不想排隊搶雲端 GPU 的團隊，這份實測提供了一條具體路徑：先確認模型能否塞進單臺 Mac Studio 的統一記憶體，塞不下就用管線或張量平行化串接多臺機器。對於需要長上下文的 agentic coding 應用，M5 Ultra 在 TTFT 與生成速度上的提升，以及遠低於資料中心 GPU 的功耗，都讓「桌上跑旗艦模型」從展示用途逐漸變得實際可行。

🔗 **來源**
- 標題：Local and Distributed Large LLM Inference with MLX and RDMA on Mac Studio
- 連結：https://machinelearning.apple.com/research/mlx-distributed-inference

#MLX #MacStudio #AppleSilicon #DistributedInference #LLMInference #RDMA #Thunderbolt #MuseSparkOpen #LocalAI #EdgeAI
