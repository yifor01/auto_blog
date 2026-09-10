---
title: How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-full-stack-nim-optimizations-deliver-2-5x-more-users-on-nemotron-3-ultra/
model: claude-code/sonnet
generated_at: '2026-09-10T20:02:51.115143'
score: 91
---

📌 【NVIDIA 實測】Nemotron 3 Ultra 用 NIM 優化，同延遲下多撐 2.5 倍用戶

TL;DR：NVIDIA NIM 全端優化，讓 Nemotron 3 Ultra 同延遲下多撐 2.5 倍使用者。

🎣 部署好一個大型語言模型，只是產線之路的第一步。真正決定成本效益的，是同一批 GPU 到底能撐住多少個並發使用者，而且還不能犧牲互動性，這在 agentic AI 場景下尤其棘手：prompt 可能很長、context 需要跨步驟重複使用，應用又常常要把冗長的回應以串流方式即時吐回給使用者。

🤔 推論效能是一整套系統工程

NVIDIA NIM 把模型與 GPU 感知的服務化決策打包成可部署的微服務。精度與 kernel 選擇、平行化策略、排程、批次處理、記憶體配置、prefix 重複使用、模型專屬的 state cache、解碼策略，這些環節彼此牽動，一個設定只有在「提升吞吐量的同時仍守住應用的延遲目標」時才有意義。NIM 把這整套最佳化工作變成一個經過驗證的起點：NVIDIA 工程師針對支援的模型、GPU 與精度組合驗證設定，再把執行環境與模型檔案包裝在標準 API 之後；正式產線版本 NIM Certified 另外提供定期的推論堆疊更新、CVE 處理、更廣泛的硬體驗證，以及透過 NVIDIA AI Enterprise 提供的商業支援。

📊 4xB200 上，同延遲吞吐量翻 2.5 倍

素材給出的基準測試定義是：硬體為 4xB200，agentic 工作負載參數為 64K/400/76% KV reuse/50 TPS/user（20 ms ITL）。

| 設定 | 原生 256K 最大 context 吞吐量 | 說明 |
|---|---|---|
| NIM Off（基準） | 718 tok/s | 未套用任何 NIM 優化 |
| NIM On（2.0.12，優化後） | 1,997 tok/s | 相對基準 2.5 倍 |

在 50 TPS/user 的目標下，NIM-on 曲線的系統吞吐量超過基準的 2.5 倍，直接反映在同樣互動性水準下能多撐的並發使用者數量。

🧩 五層優化堆疊分別做了什麼

素材指出，這個提升來自多個彼此互動的優化組合，而不是可以單獨加總百分比的獨立開關：

- **精度與自動調校的模型感知 kernel**：針對 mixture-of-experts 與 Mamba 的自動調校 kernel，把混合式架構有效映射到 NVIDIA Blackwell GPU。
- **平行執行**：張量平行（tensor parallelism）把模型分散到四張 GPU，並針對 mixture-of-experts 層做 expert-aware 執行以提升利用率。
- **Prefix 與模型 state 重複使用**：prefix caching 避免重算重複的 context，partial-prefix matching 在只有部分 prefix 吻合時仍能回收重用，Mamba 的 state-cache 設定也依模型架構調校。
- **排程、批次與記憶體調校**：並發序列數上限、批次 token 數上限、block size 與 GPU 記憶體配置，讓更多工作能同時在飛而不越過延遲目標。
- **MTP 投機解碼（speculative decoding）**：NIM 2.0.12 優化服務堆疊把 MTP 及其相關修正納入同一套優化堆疊，實際帶來的增益取決於接受率（acceptance rate）與可用的記憶體餘裕。

🧩 自己重播流量，找出符合你 SLO 的 Pareto 點

素材強調，公開的曲線只是一個起點，不保證每個應用都能拿到相同結果，建議的做法是：使用固定的 NIM 2.0.12（或更新版本）並釘住 image tag 或 digest；準備具代表性的流量（Mooncake 格式的 JSONL trace，或蒐集受控的 NIM 請求，並注意存取控管與敏感資料清理）；用 NVIDIA AIPerf 重播流量取得效能基準；再從滿足延遲限制的各點中挑出輸出吞吐量最高的 Pareto 點。

```
for C in 1 4 8 16 32 64; do
  aiperf profile \
    --model nvidia/nemotron-3-ultra-550b-a55b \
    --endpoint-type chat --streaming \
    --url localhost:8000 \
    --input-file ./agentic-trace.jsonl \
    --custom-dataset-type mooncake_trace \
    --no-fixed-schedule \
    --concurrency "$C"
done
```

要在四張 B200 的系統上針對 agentic 工作負載挑選優化設定檔，可以把 `NIM_MODEL_PROFILE` 設為 `vllm-nvidia-b200-nvfp4-tp4-pp1-throughput-90.0` 並開啟投機解碼：

```
export NGC_API_KEY=<your-personal-api-key>
export LOCAL_NIM_CACHE=$HOME/.cache/nim
export NIM_TAG=2.0.12
export NIM_MODEL_PROFILE=vllm-nvidia-b200-nvfp4-tp4-pp1-throughput-90.0

docker run --gpus all --shm-size=16GB \
  -e NGC_API_KEY \
  -e NIM_MODEL_PROFILE \
  -e NIM_SPECDEC_ENABLE=1 \
  -v "$LOCAL_NIM_CACHE:/opt/nim/.cache" \
  -p 8000:8000 \
  nvcr.io/nim/nvidia/nemotron-3-ultra-550b-a55b:$NIM_TAG
```

⚠️ 公開數字是起點，不是承諾

素材明確提醒，這份 Pareto 曲線是一個起點而非保證，實際效益需要用自己的代表性流量重新量測才能確認是否適用。

🎯 實務啟示

如果你的團隊正在評估要自己手刻服務堆疊，還是直接採用 NIM，這篇案例給了一個具體的量化依據：在相同延遲目標下，一套經過驗證的服務堆疊組合（kernel、平行化、prefix 重用、排程批次、投機解碼）可以帶來數倍的吞吐量差距，而這些優化彼此高度耦合，很難靠單點調參複製。實務上更務實的做法是採用素材建議的 AIPerf concurrency sweep，用自己的 agentic 流量重跑一次，再決定要不要自建。

🔗 來源
- 標題：How Full-Stack NIM Optimizations Deliver 2.5x More Users on Nemotron 3 Ultra
- 作者／機構：Elizabeth Goodman, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-full-stack-nim-optimizations-deliver-2-5x-more-users-on-nemotron-3-ultra/

#NVIDIA #NIM #Nemotron #LLMServing #Inference #AgenticAI #Blackwell #B200 #SpeculativeDecoding #MLOps
