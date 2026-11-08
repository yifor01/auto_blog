---
title: 'Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU'
source: Hacker News
url: https://github.com/synchopate/llama-modchip
model: claude-code/sonnet
generated_at: '2026-11-08T21:15:03.109529'
score: 114
---

📌 【開源專案】64GB記憶體、零GPU，跑起284B參數的MoE模型

TL;DR：llama-modchip讓284B參數的DeepSeek-V4-Flash在純CPU、64GB RAM環境下達到每秒9-14 tokens的生成速度。

多數人預設跑起300B等級的模型得靠多張GPU與上百GB的顯示記憶體撐著，但這個專案給出一個反例：一臺64GB記憶體的桌機，不裝任何GPU，也能把284B參數的MoE模型跑起來。

🤔 標準量化方案為何會OOM

DeepSeek-V4-Flash總參數284.33B，每次推理實際啟用13.17B（43層MLA＋256個routed expert）。標準的UD-IQ1_S量化版本體積是76.87GiB（82.5GB），超過64GB系統上約62.5GiB的可用RAM，結果就是page-cache thrashing或直接被OOM kill。llama-modchip把同一顆模型的checkpoint重新轉碼到56.56GiB（60.73GB），讓模型本體加上256K的KV cache（實測Peak VmRSS約57.61GiB）完全鎖進記憶體，不需要任何NVMe swap。

🧩 怎麼做到的：客製量化＋CPU快取友善的kernel

專案核心是一組ggml/llama.cpp的kernel patch、量化轉碼器與執行工具，針對x86_64（AVX-512/AVX2）與ARM64（NEON/SVE/Apple Metal）處理器設計。量化層面，大部分張量維持原本的精度：embeddings、Dense L0、43個shared expert、MLA的kv_a/q_a/wkv_b保留在Q4_K/Q5_K/F32；MLA的wq_b與attn_output被轉碼成自訂的Fractal-64格式（GGML_TYPE_Q2_0，64-weight區塊搭配8個子scale與BF16 scale，3.75 bpw）；256個routed MoE expert則主要用IQ1_S（1.5625 bpw），邊界層另外用IQ2_XXS、IQ1_M保留精度，整體比原版UD-IQ1_S少了20.31GiB。預設模式下（v2.4.0 Lossless）每層仍完整評估全部6個routed expert加1個shared expert（Top-6），不做expert剪枝，與未修改runtime的輸出logit cosine similarity為1.00000；想換速度可透過LLAMA_MOE_TOP_K=5或4的環境變數犧牲一點perplexity換吞吐量。

kernel層面則是把prompt prefill階段的單欄量化矩陣向量運算，改成4層式（ZMM AVX-512BW暫存器＋32KB L1D＋1MB L2＋64MB L3）的多欄位tiling排程，搭配register-stationary的MQA8 FlashAttention，以及用non-temporal指令讓冷的MoE專家權重不會把L3裡熱的KV cache快取線擠出去。16核Zen5實測下，這一項優化讓prefill提升77%、decode提升53%（25.0→44.36 tok/s）。另外還搭了一個1.64MB的L2/L3 Zobrist n-gram drafter（稱為Stockfish-PVS v2）做自我推測解碼，並用/dev/shm做KV slot快速存取，讓40-tool的Claude Code場景context恢復只要13.1-32.6毫秒。

📊 不同硬體規格的實測吞吐量

| 硬體等級 | RAM | 跑的模型 | 吞吐量 |
|---|---|---|---|
| 開發者筆電/迷你PC | 16-32GB | Nemotron-3.5-30B-A3B（14.35GiB, 3.75bpw） | 25.0-60.4 tok/s |
| 桌機/伺服器 | 64GB | DeepSeek-V4-Flash 284B（56.56GiB, 1.71bpw） | 44.4 tok/s（prefill）、9.1-14.7 tok/s（decode） |
| 混合桌機（CPU+16GB GPU） | 32-64GB | Nemotron-30B / Qwen3-30B（3.75-4.25bpw） | 80.80 tok/s |
| 8通道工作站（Threadripper） | 128GB+ | Nemotron-30B | 111.62 tok/s |

🧩 快速上手

```
git clone https://github.com/synchopate/llama-modchip.git
cd llama-modchip
./modchip chat
```

也可以直接抓官方預編譯的Linux x86_64二進位檔搭配Hugging Face上的GGUF檔案執行，指令中會用到`-m`指定模型、`-c`指定context長度、`-t`指定執行緒數。

⚠️ 使用限制

Fractal-64模型用的是自訂的block-64 BF16-scale張量（GGML_TYPE_Q2_0，tensor type ID 40），未經修改的llama.cpp、Ollama或LM Studio會直接回報「unknown tensor type 40」拒絕載入，必須用專案自帶的`./modchip`或配套的伺服器二進位檔才能跑。

🎯 實務啟示

這個專案示範了本地部署超大模型的工程思路：單靠量化壓縮體積還不夠，還要搭配對CPU快取友善的kernel設計與推測解碼，三者疊加才能把理論上要多GPU才能跑的模型，壓進一臺64GB記憶體的機器裡。

🔗 來源
- 標題：Llama-modchip: 284B DeepSeek on 64GB RAM, no GPU
- 作者／機構：joshcsimmons（Hacker News 發文者）
- 連結：https://github.com/synchopate/llama-modchip

#MoE #DeepSeek #LLM #CPUInference #Quantization #llamacpp #LocalLLM #OpenSource #EdgeAI #MachineLearning
