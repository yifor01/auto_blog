---
title: 'Meet Gigatoken: A Rust BPE Tokenizer that Encodes Text at 24.53 GB/s, up to
  989x Faster than HuggingFace Tokenizers'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/23/meet-gigatoken-a-rust-bpe-tokenizer-that-encodes-text-at-24-53-gb-s-up-to-989x-faster-than-huggingface-tokenizers/
model: tencent/hy3:free
generated_at: '2026-07-24T08:16:44.421216'
score: 87
---

📌 【開源專案】Gigatoken 登場：Rust 實作 BPE Tokenizer，處理速度高達 24.53 GB/s

TL;DR：Gigatoken 是一款 Rust 實作的 BPE Tokenizer，處理效能最高可比 HuggingFace 快 989 倍。

🤔 **Tokenization 往往是被忽略的效能瓶頸**

在語言模型（Language Modeling）的技術堆疊中，Tokenizer（分詞器）幾乎是極少數沒人會去進行效能分析（Profile）的部分。然而，由 Stanford 博士生 Marcel Rød 開源的 Gigatoken 挑戰了這個現狀，他認為這是一個錯誤，並開發出一個能在單機上以 GB/s 等級處理文本的函式庫。

🧩 **核心設計：Rust 驅動與兩種使用模式**

Gigatoken 是一個使用 Rust 語言撰寫並提供 Python 綁定（Bindings）的 Byte-Pair Encoding (BPE) Tokenizer。其程式碼結構由 66.2% 的 Rust 與 33.3% 的 Python 組成。

根據 README，使用者有兩種方式可以使用：
1. **原生 API (Native API)**：讓 Rust 直接讀取檔案，這是達成極致吞吐量（Throughput）的關鍵，也是效能測試資料的來源。
2. **相容模式 (Compatibility mode)**：封裝現有的 HuggingFace 或 tiktoken Tokenizer，以確保輸出結果完全一致（Parity），但會因為仍需支付 Python 在建立 list 與字串與 bytes 轉換時的開銷，導致效能下降約 200–300 倍。

📊 **在相同硬體下，效能表現大幅領先基準測試**

Gigatoken 的速度提升並非特定 CPU 或特定詞彙表的產物，其在處理 GPT-2 任務時展現了驚人的資料：

**在 144 核心 AMD EPYC 9565 雙插槽配置下（處理 11.9 GB owt_train.txt）：**
- **Gigatoken**：24.53 GB/s
- **OpenAI tiktoken**：36.0 MB/s (快 681 倍)
- **HuggingFace tokenizers**：24.8 MB/s (快 989 倍)

**在 Apple M4 Max (16 核心) 上：**
- **Gigatoken**：8.79 GB/s (比 HuggingFace 快 1,268 倍，比 tiktoken 快 140 倍)

**在消費級 AMD Ryzen 7 9800X3D 上：**
- **Gigatoken**：6.27 GB/s (比 HuggingFace 快 106 倍，比 tiktoken 快 68 倍)

💡 **支援廣泛的 Tokenizer 家族**

Gigatoken 的基準測試涵蓋了 23 種不同的 Tokenizer 家族，包含目前主流的 LLM 模型：
- GPT-2, GPT-OSS
- Llama 3 至 4
- Qwen 2 至 3.6
- DeepSeek V3/R1/V4
- GLM 4 與 5
- Kimi K2, Nemotron 3, Phi-4
- OLMo 2/3, ModernBERT, Gemma, Mistral

🎯 **實務啟示**

對於需要處理海量文本資料進行訓練或預處理的工程師來說，Gigatoken 提供了一個極具吸引力的選項。若追求極致效能，應盡量使用其原生 API 讓 Rust 直接處理檔案，而非僅將其作為 Python 函式的封裝。

🔗 **來源**
- 標題：Meet Gigatoken: A Rust BPE Tokenizer that Encodes Text at 24.53 GB/s, up to 989x Faster than HuggingFace Tokenizers
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/23/meet-gigatoken-a-rust-bpe-tokenizer-that-encodes-text-at-24-53-gb-s-up-to-989x-faster-than-huggingface-tokenizers/

#Gigatoken #Rust #Tokenizer #BPE #MachineLearning #NLP #OpenSource #LLM #PerformanceOptimization #DataProcessing
