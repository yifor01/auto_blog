---
title: Up to 3.2x Faster Inference with LFM2.5-DSpark
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm25-dspark
model: claude-code/sonnet
generated_at: '2026-08-21T06:28:32.363743'
score: 117
---

📌 LFM2.5-DSpark：從 H100 到 MacBook 都能吃到推理加速

TL;DR：DSpark 推測解碼讓 LFM2.5 系列在 GPU 上最高提速 3.18 倍、裝置端最高 2.87 倍，輸出品質完全不變。

LLM 推理的 decode 階段其實大多時間不是在「算」，而是在把權重從 DRAM 搬到 SRAM，這個記憶體頻寬瓶頸讓多數使用者以為「模型變大就一定變慢」。LiquidAI 這次針對 LFM2.5 家族釋出的 DSpark 草稿模型（draft model），想解決的正是這個問題。

🤔 **decode 是記憶體頻寬問題，不是算力問題**

推測解碼（speculative decoding）的思路是用一個輕量的草稿模型先產生候選 token，再由目標模型在一次前向傳播中一次驗證所有候選，藉此把「搬權重」的成本攤提到多個 token 上。過去業界已經提出 EAGLE-3、DFlash 等方法，DSpark 是這條路線最新的整合方案。

🧩 **三個模組疊出更高的接受率**

DSpark 結合三個元件：DFlash 風格的平行骨幹（parallel backbone），以目標模型的上下文特徵為條件，一次前向傳播就產生所有草稿 token 的隱藏狀態；一個輕量的循序頭（sequential head），以馬可夫鏈（Markov chain）建模相鄰 token 間的依賴關係，藉此提高後段位置的接受率；以及一個信心排程驗證器（confidence-scheduled verifier），預測每個 token 的存活機率，在驗證成本高於效益時主動剪掉低信心的後綴。

LiquidAI 依循 DSpark 的訓練配方，使用涵蓋 SFT、聊天、程式碼與函式呼叫的更大、更多元資料組合，草稿模型採用 5 層、block size 為 9 的純 attention 架構，每個草稿模型跑了 15 個 epoch，並挑選接受率最高（而非 loss 最低）的那個 epoch。三個草稿模型的參數量都在 300M 上下：

| 元件 | LFM2.5-1.2B-Instruct | LFM2.5-8B-A1B | LFM2.5-2.6B |
|---|---|---|---|
| Decoder stack（5 層） | 241.2M | 241.2M | 241.2M |
| Hidden-state projection | 21.0M | 21.0M | 21.0M |
| Markov head | 33.6M | 65.5M | 65.5M |
| Norms + confidence head | 27.5k | 27.5k | 27.5k |
| 總計 | 295.7M | 327.7M | 327.7M |

由於在 greedy decoding 下，草稿 token 只有在與目標模型分布一致時才會被接受，被拒絕就由目標模型自己的 token 取代，因此輸出序列與 baseline greedy 完全相同，pass@1 或 exact match 這類 benchmark 準確度不受影響。

📊 **GPU 到筆電都測得到明顯加速**

團隊在 H100 80GB（SGLang、BF16）與 M4 Max MacBook Pro（llama.cpp、Metal、FP16 GGUF）上，以 block size 9、batch size 1、temperature 0，在五個資料集上測試：

LFM2.5-2.6B：
| 資料集 | 接受率（滿分10） | H100 加速 | M4 Max 加速 |
|---|---|---|---|
| MATH500 | 5.42 | 3.06x（326→1000 tok/s） | 2.25x（61→137 tok/s） |
| HumanEval | 4.54 | 2.56x（326→835 tok/s） | 2.63x（61→161 tok/s） |
| MBPP | 4.71 | 2.64x（326→861 tok/s） | 2.11x（62→132 tok/s） |
| GSM8K | 4.32 | 2.22x（312→693 tok/s） | 2.36x（60→143 tok/s） |
| MT-Bench | 5.07 | 2.87x（325→933 tok/s） | 1.99x（62→123 tok/s） |
| 平均 | 4.81 | 2.67x | 2.27x |

在多工具（multi-tool）情境下，DSpark 讓 LFM2.5-2.6B 的延遲平均降低 57%。LFM2.5-1.2B-Instruct 的接受率波動較大，加速幅度依文字分布差異可達 52%。LFM2.5-8B-A1B（MoE 架構）在 H100 上接受率最高（平均 6.95），但裝置端加速僅約 18%，低於兩個密集模型。

⚠️ **MoE 模型在裝置端吃不到全部紅利**

團隊指出，LFM2.5-8B-A1B 裝置端加速有限，原因在於 llama.cpp Metal backend 目前的 MoE 實作：驗證 k 個 token 會啟動更多專家（experts），帶來的權重搬運量比單次 decode 更大，抵銷了推測解碼省下的時間。

🎯 **實務啟示：日起支援 SGLang 與 llama.cpp**

DSpark 草稿模型已在 Hugging Face 提供 Safetensors 與 GGUF 兩種格式，並取得 llama.cpp（PR#27383）與 SGLang（PR #31041）的原生支援。SGLang 啟動範例：

```bash
python -m sglang.launch_server \
  --model-path LiquidAI/LFM2.5-2.6B \
  --speculative-algorithm DSPARK \
  --speculative-draft-model-path LiquidAI/LFM2.5-2.6B-DSpark \
  --speculative-draft-attention-backend flashinfer \
  --disable-radix-cache --mem-fraction-static 0.75 --port 30000
```

llama.cpp 啟動範例：

```bash
llama-server -m LFM2.5-2.6B-F16.gguf \
  -md LFM2.5-2.6B-DSpark-F16.gguf \
  --spec-type draft-dspark --spec-draft-n-max 10 --spec-draft-n-min 0 \
  -fa on -ngl 99
```

對於想在邊緣裝置上做 agentic 推理的團隊，這是一個不用改模型、不用犧牲品質，就能換取實質吞吐量提升的選項，值得直接拿現有的 LFM2.5 部署試裝。

🔗 **來源**
- 標題：Up to 3.2x Faster Inference with LFM2.5-DSpark
- 作者／機構：LiquidAI（Leonie Monigatti、Fernando Fernandes Neto、Tarek Dakhran、nathan ranchin 等）
- 連結：https://huggingface.co/blog/LiquidAI/lfm25-dspark

#LLM #SpeculativeDecoding #Inference #EdgeAI #LiquidAI #OnDeviceAI #MachineLearning #ModelOptimization #GPU #AIInfrastructure
