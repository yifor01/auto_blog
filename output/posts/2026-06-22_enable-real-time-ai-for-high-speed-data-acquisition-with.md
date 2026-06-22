---
title: Enable Real-Time AI for High-Speed Data Acquisition with DAQIRI
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/enable-real-time-ai-for-high-speed-data-acquisition-with-daqiri/
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-22T21:03:45.889606'
---

📌 【NVIDIA】DAQIRI：打破硬體瓶頸，將高頻資料直接串流至 GPU 進行即時 AI 分析

TL;DR：DAQIRI 透過零複製 (zero-copy) 技術將高速感測器資料直連 GPU，實現即時 AI 處理與分析。

當前的 AI 模型不再缺乏資料，真正的挑戰在於資料產生的速度太快。從 1 MHz 重複率的光子脈衝到工業 CT 掃描器，傳統的「收集 $\rightarrow$ 儲存 $\rightarrow$ 分析」架構已成為瓶頸，導致大量珍貴資料在儲存前就被捨棄。

🤔 **從「儲存後分析」轉向「即時處理」**

在科學研究中，資料量過大往往導致研究者無法將所有原始資料存入硬碟，只能在前端進行粗略過濾。NVIDIA 推出的 DAQIRI 旨在改變這一點，將軟體定義的高吞吐量管線 (pipeline) 引入資料採集過程，讓 AI 能在資料產生的瞬間即時做出反應。

🧩 **零複製串流與模組化工作流**

DAQIRI 的核心設計在於繞過傳統硬體瓶頸，將高頻寬的偵測器資料以 zero-copy 方式直接傳輸至 GPU 記憶體。其技術特點包括：

- **整合 NVIDIA Holoscan 平臺**：結合 TensorRT（加速推理）與 nvCOMP（高效壓縮），讓開發者能快速建構低延遲的工作流。
- **模組化功能**：支援過濾 (filtering)、推理 (inference)、壓縮 (compression) 與適應性控制 (adaptive control)。
- **靈活的開發介面**：提供 YAML 驅動的配置方式，並支援 C++ 與 Python API。

📊 **CERN A-GHOST 專案的實務應用**

在 CERN 的 A-GHOST 專案中，DAQIRI 被用於將基於 FPGA 的硬體直接連線到 GPU 叢集。這使得科學家能對先前在 HL-LHC 資料流中被捨棄的資料，進行即時 AI 分析。該專案採用的模型架構包括：
- 卷積自動編碼器 (Convolutional Auto-Encoders)
- Transformer 基礎架構 (transformer-based architectures)

🎯 **實務啟示**

對於處理高頻寬資料（如高能物理、醫療影像或軟體定義無線電）的工程師而言，DAQIRI 的設計理念顯示出「將 AI 推向資料來源頭」的趨勢。透過減少記憶體複製次數並利用 GPU 的平行計算能力，可以在資料進入儲存裝置前就完成特徵提取或異常檢測，大幅提升資料利用率。

🔗 **來源**
- 標題：Enable Real-Time AI for High-Speed Data Acquisition with DAQIRI
- 作者／機構：Cara Laasch @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/enable-real-time-ai-for-high-speed-data-acquisition-with-daqiri/

#NVIDIA #EdgeComputing #GPU #RealTimeAI #DAQIRI #Holoscan #TensorRT #CERN #DataAcquisition #HighThroughput
