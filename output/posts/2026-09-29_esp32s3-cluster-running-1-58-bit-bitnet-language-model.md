---
title: ESP32S3 cluster running 1.58-bit (BitNet) Language model
source: Hacker News
url: https://github.com/Low-Zi-Hong/ESP32s3-LLM-Cluster
model: claude-code/sonnet
generated_at: '2026-09-29T21:42:39.675668'
score: 92
---

📌 在7顆ESP32S3上跑BitNet：開源分散式LLM推理叢集

TL;DR：7顆ESP32S3串成SPI菊鏈，分散式跑1.58-bit BitNet架構的0.5B LLM。

一顆ESP32S3的記憶體通常只夠處理藍牙訊號或閃爍幾顆LED，但如果把7顆串在一起呢？這個開源專案示範了在極限邊緣硬體上跑語言模型推理的可能性。

🤔 **為什麼要在微控制器上硬跑LLM**

在記憶體以KB計、沒有GPU的ESP32S3上跑LLM，唯一的出路是把模型壓到極致小，並把運算拆給多顆晶片分攤。這個專案採用BitNet的1.58-bit三元量化（ternary quantization）把權重壓縮到極小體積，再透過分散式架構把Transformer的層數切分到7顆ESP32S3上執行。

🧩 **Master/Node架構：SPI菊鏈接力跑Transformer**

整體是一個master節點加6個compute node的pipeline：
- Master節點：負責BPE tokenizer與token embedding（INT4量化，約14MB存於Flash），並在推理結尾做最終RMSNorm、LM Head（與embedding權重tied）與貪婪取樣（greedy sampling），輸出下一個token。
- Compute Node 1至6：每個節點各自負責4層Transformer block，內含RMSNorm（FP16 scale到FP32）、1.58-bit Attention（Q/K/V/O投影＋RoPE）、存於PSRAM的KV Cache，以及1.58-bit MLP（Gate/Up/Down投影）。

節點之間透過雙通道SPI菊鏈（daisy chain）傳遞hidden state向量：master送出提示的embedding後，依序流經Node 1到Node 6，最後傳回master完成最後一層運算與取樣。程式碼中還包含assembly最佳化的1.58-bit MAC運算（bitlinear_forward.S）與look-up table（lut_table.cpp）以榨出微控制器有限的運算力。

🛠 **怎麼跑起來**

專案提供完整流程：`python_tools/`目錄下有詞彙裁剪（縮到3.2萬個token）、embedding矩陣切片、BitNet QAT（quantization-aware training）微調、INT4權重打包，以及把量化後的模型與tokenizer序列化成ESP32可讀的`.bin`格式的工具鏈；`master_board/`與`node_firmware/`則是以ESP-IDF撰寫的master與node韌體，搭配自訂的partition table分配token、model、fnorm等分區。README建議依`workflow.md`的步驟指南進行燒錄與模型準備。

⚠️ **這是概念驗證，不是產品**

專案本身標明靈感來源包括單節點ESP32S3量化LLM部署專案，以及既有的多節點分散式AI架構專案，加上BitNet的1.58-bit量化概念。README未提供推理速度、token throughput等效能數字，也未說明穩定性與可靠度細節，讀者評估可行性時應以此為前提。

🎯 **實務啟示**

這個專案的價值不在於效能，而在於證明「用一堆便宜的微控制器分散式跑LLM」這條路徑是可行的，且完整開源了從模型量化、tokenizer裁剪到韌體通訊的整條pipeline。對想在極限邊緣場景（無GPU、記憶體以KB計）探索LLM部署的工程師，這是一份很值得參考的實作範本。

🔗 **來源**
- 標題：ESP32S3 cluster running 1.58-bit (BitNet) Language model
- 作者／機構：nkko（Hacker News 分享者）
- 連結：https://github.com/Low-Zi-Hong/ESP32s3-LLM-Cluster

#ESP32 #BitNet #EdgeAI #TinyML #DistributedComputing #Quantization #Microcontroller #OpenSource #LLM #EmbeddedAI
