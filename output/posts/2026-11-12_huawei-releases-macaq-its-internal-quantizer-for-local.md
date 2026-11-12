---
title: Huawei releases MACaQ, its internal quantizer for local inference
source: Hacker News
url: https://github.com/huawei-csl/MACaQ
model: claude-code/sonnet
generated_at: '2026-11-12T22:56:07.871773'
score: 95
---

📌 華為開源 MACaQ：跨模態本地量化工具

TL;DR：MACaQ 可量化文字、影像、影片、語音模型，122B 模型 64 分鐘量化完成。

多數量化工具只處理文字模型，而且換一種架構就要重寫 recipe；MACaQ 想解決的，是用同一套量化方法同時跑通文字、影像、影片與語音模型。

🤔 解決什麼問題

本地推理想要省記憶體、省時間，量化是必經之路，但不同模態、不同框架往往需要各自的量化流程。MACaQ 定位為 model-agnostic 的量化器，目標是讓同一套方法可以套用在文字生成（llama.cpp、vLLM）、圖像／影片／音訊生成（Diffusers）、語音生成（PyTorch），甚至支援 Ascend 晶片上的核心實作。

🧩 設計理念：MACaQ 與 MACaQ-R 分工

專案依後端分成四條路線：Diffusers 走 W4A4 處理圖像、影片、音訊生成（image-to-video 任務在校準時會用到條件圖片）；llama.cpp 處理文字生成，支援 2、3、4-bit GGUF 格式，也能在 CPU 上執行；vLLM 把文字模型量化成精簡 checkpoint，預設走 W4A4，也可選擇純權重量化後直接用於生成或透過 HTTP API 服務；PyTorch 則用於語音生成的 W4A4 量化。

另外釋出的 MACaQ-R，用途是在既有的量化 GGUF 模型上精修權重編碼，同時保留原本的格式與 block scale，產生的 GGUF 可以直接用標準的 llama.cpp 執行，不需要額外的 runtime。

🧩 怎麼用

每個後端建議用 Python 3.12 搭配獨立的虛擬環境。以 MACaQ-R 精修一個已量化的 MoE GGUF 為例，官方提供的指令大致是指定原始量化模型、對應的原始 HF 權重、teacher 模型與校準資料，跑完後輸出一個新的 GGUF 檔，之後可以直接用 llama cli -m models/model-macaq-r.gguf 載入，或用 llama serve 提供服務。README 中也列出了針對 Qwen3 系列（dense、hybrid、MoE）、OLMoE 等模型的具體操作說明。

📊 數據：壓縮時間與品質的取捨

README 指出，MACaQ 可以在 64 分鐘、僅用 32.5 GB 裝置記憶體的情況下量化一個 122B 參數模型；在 Llama-3-8B 上，MACaQ 能拿到比 MR-GPTQ、DuQuant++ 更低的 perplexity，或是在量化時間縮短 11 倍的情況下打平這兩者最好的 perplexity 成績。

在 Qwen3.6-35B-A3B 上，官方比較了 MACaQ-R 與 Unsloth 的量化結果（相對 FP16 的 KL divergence，數字越低越好）：

| 模型 | GGUF 檔案大小 | KL divergence（越低越好） |
|---|---|---|
| Unsloth UD-Q4_K_XL | 22.36 GB | 0.015731 |
| MACaQ-R Q4_K_XL | 22.36 GB | 0.013367 |

在 vLLM 上以 Qwen3.8-27B 為例，相對 BF16 基準：

| 精度 | Perplexity（越低越好） | Prefill 速度 | Decode 速度 |
|---|---|---|---|
| BF16 | 2.8463 | 1.00× | 1.00× |
| MACaQ W4A4 | 2.8994 | 2.33× | 2.58× |

⚠️ 使用門檻

每個後端需要各自獨立的環境，且版本之間（Python、PyTorch、CANN）需要對齊；在 Ascend 晶片上，MACaQ 目前釋出的是矩陣乘法 kernel，完整的模型執行還需要額外整合 Ascend 推理 runtime。

🎯 實務啟示

如果你需要在本地跑大型模型卻受限於記憶體或量化時間，MACaQ 提供了一個可以直接複現的開源選擇，尤其是已經有現成 GGUF 模型、只想用 MACaQ-R 精修品質的情況，幾乎不需要更換現有的 llama.cpp 部署流程。團隊也在 GitHub 上附了論文與 BibTeX 引用，方便進一步查證方法細節。

🔗 來源
- 標題：Huawei releases MACaQ, its internal quantizer for local inference
- 作者／機構：thefox96（Hacker News 投稿者）
- 連結：https://github.com/huawei-csl/MACaQ

#MACaQ #Quantization #Huawei #LLMInference #GGUF #llamacpp #vLLM #EdgeAI #OpenSource #ModelCompression
