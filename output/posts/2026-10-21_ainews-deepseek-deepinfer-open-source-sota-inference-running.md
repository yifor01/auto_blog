---
title: '[AINews] DeepSeek DeepInfer: Open Source SOTA Inference running 155T toks/day/cluster
  making $22m/day at ~80% margin for a 81 day payback'
source: Latent Space
url: https://www.latent.space/p/ainews-deepseek-deepinfer-open-source
model: claude-code/sonnet
generated_at: '2026-10-21T20:50:49.003506'
score: 125
---

📌 DeepSeek 開源 DeepInfer：單叢集日賺2200萬美元的推理堆疊拆解

TL;DR：DeepSeek 開源支撐 V4.1 Flash 的生產推理引擎 DeepInfer，首度揭露架構與營收細節。

PyTorch Conf 開幕當天，DeepSeek 投下一顆技術炸彈：把自家吃下155兆token/日流量的生產推理堆疊開源出來，還附上了營收與成本的第一方數據。

🤔 開源陣營缺一個對標 Fireworks、Baseten 的生產方案

主流大型語言模型的推理服務長期是閉源巨頭的主場，從 Fireworks、Baseten 到 Modal，開源陣營一直缺少對標的生產級方案。DeepInfer 就是 DeepSeek 對這塊缺口的回應：它是 vLLM 的客製化版本，同時致謝 SGLang 與 TensorRT-LLM 的貢獻，並以 Apache 2.0 授權開源。DeepInfer 支援到72小時的 prompt caching，比 OpenAI 剛宣布的12小時更長，並支援 NVIDIA 與華為 Ascend 兩種平臺的分散式推理、speculative decoding、SWA Bounded Replay 與結構化輸出。配套的 deepseek-recipe 元件則負責生產環境的 token 編解碼與官方 API 相容的請求處理。

🧩 把 vision、prefill、decode 三段分開擴展

DeepInfer 把 vision encoding、prefill、decode 三個階段拆開，讓每個階段各自針對自己的瓶頸擴展。根據 DeepSeek 的工程報告：

- Prefill 建議用一般的8加速卡機器；decode 則用64到128張加速卡組成的超節點，並採用寬域 expert parallelism 分散 MoE 專家，同時維持較大的有效 batch size。
- Prefill 排程會估算 attention 的實際運算成本，而非只看請求長度，chunk 大小會隨時間預算動態調整，而不是全域套用固定 chunk。
- 因為快取的前綴被集中存放在共享儲存中，prefill 請求不需要固定路由到曾經處理過這個前綴的那臺機器，可以分配給任何有空的 worker。
- Decode 路由同時考慮執行中請求數與累積 KV 快取長度，前者反映排程壓力，後者反映記憶體與狀態壓力，兩者缺一不可。
- Expert parallel 負載平衡會複製熱門專家並定期重新分配，用更多 HBM 換取更高吞吐，但複製係數的最佳值因工作負載而異。
- CPU 排程與加速卡運算重疊執行，用非同步排程去除 decode 步驟間的閒置空隙。

值得一提的技術觀察是，有評論者指出 DeepInfer 在揭露的 Blackwell 設定中似乎沒有使用 tensor parallelism，並將其追溯到 DeepSeek V3 時代 H800 互聯限制留下的設計慣性，不過這僅是對設定的解讀，並非 tensor parallelism 本身效率較差的證據。

⚠️ KV cache 與負載平衡仍留在黑盒子裡

DeepSeek 自稱 DeepInfer 完全開源，但工程報告也坦言，KV 快取管理與負載平衡這兩塊「皇冠上的珍珠」尚未完整釋出，因為它們仍與內部基礎設施高度耦合。換句話說，引擎本身是開放的，但要重現 DeepSeek 等級的服務編排仍需要自己補完一大塊。

📊 155兆token/日、96%命中率、80%毛利從哪來

以下是 DeepSeek 工程報告中揭露的生產數據，屬於第一方數據，未經獨立稽核：

| 指標 | 數值 |
|---|---|
| 單叢集日處理量 | 155兆tokens/天 |
| 平均首字延遲 | 400毫秒 |
| 生成速度 | 230 tokens/秒，coding 場景可達300 tokens/秒 |
| 輸入快取命中率 | 96% |
| 每張加速卡離峰時段營收 | 38美元/小時 |
| 單張 prefill GPU 處理量 | 150萬tokens/秒（含快取） |
| 單張 decode GPU 處理量 | 14,000 tokens/秒 |
| 叢集規模 | 約2,400張加速卡 |

把這些數字代入全包成本每卡每小時5到8美元的估算，推理毛利率超過80%，換算成叢集經濟效益約為每GW 1,660億美元，回本週期僅81天，遠低於 DeepSeek 一般規劃的10個月回本週期。

💡 vLLM 一出手，差距只剩6%

對「DeepSeek 推理棧是否真的獨門」這個問題，vLLM 團隊給出了目前最具體的反駁數據：在 GB200 上採用對齊設定後，其 decode 吞吐量與 DeepInfer 公開數據的差距僅6%，並同步公開了 AgentX 測試結果與重現腳本。這等於實質性地修正了「DeepSeek 的效率是現有開源引擎做不到的」這個說法。

不過另一個問題，DeepSeek 揭露的數字是否能代表推理業務普遍高毛利，仍要看工作負載組成、快取計算方式、硬體成本假設，以及哪些費用被納入計算，目前仍有爭議空間，未有定論。工程師 Su Jin Yan 的分析也補充了一個規模門檻：寬域 expert parallel prefill 需要足夠的流量與 worker 數才划算，中小規模部署用 pipeline parallelism 反而更合適，而且不同層的異質性會讓 pipeline 切分更複雜。

🎯 排程邏輯可以直接搬進既有的 vLLM/SGLang 部署

對自建推理服務的團隊而言，DeepInfer 釋出的排程邏輯，像是用運算成本而非請求長度做 chunk 調度、解耦快取路由與 worker 親和性、decode 路由同時看請求數與 KV 長度，都是可以直接借鏡到既有 vLLM/SGLang 部署的設計模式，不需要等 DeepSeek 補完 KV cache 與負載平衡模組。

🔗 來源
- 標題：[AINews] DeepSeek DeepInfer: Open Source SOTA Inference running 155T toks/day/cluster making $22m/day at ~80% margin for a 81 day payback
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-deepseek-deepinfer-open-source

#DeepSeek #DeepInfer #LLMInference #vLLM #MoE #OpenSource #AIInfrastructure #KVCache #ExpertParallelism #InferenceEconomics
