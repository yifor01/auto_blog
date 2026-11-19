---
title: Enabling Real-Time AI for Scientific Instruments with GPU-Native Data Acquisition
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/enabling-real-time-ai-for-scientific-instruments-with-gpu-native-data-acquisition/
model: claude-code/sonnet
generated_at: '2026-11-19T23:59:54.294809'
score: 77
---

📌 NVIDIA DAQIRI 再進化：感測器資料直通 GPU，電子顯微鏡扛住 500 Gbps 資料流

TL;DR：NVIDIA 更新 GPU 原生資料擷取函式庫 DAQIRI，讓科學儀器邊收資料邊用 GPU 即時運算，不必先寫入硬碟。

一顆感測器每秒鐘灌進 500 Gbps 的資料量，比傳統電子能量損失光譜儀快上 500 倍以上——這不是理論推算，而是 Lawrence Berkeley National Laboratory Molecular Foundry 團隊正在使用的新型高動態範圍電子顯微鏡相機實際吐出的資料流。這麼快的資料，要怎麼在不先存檔的情況下即時處理？

🤔 感測器的極限，往往決定了儀器的設計

文中指出，在科學與工業場域，即時分析感測器量測結果可以讓 AI 動態調整製程、引導實驗、尋找更好的操作條件。但資料能被搬移與處理的速度上限，往往反過來制約了儀器的設計方式，從讀出電子元件到擷取時序都受影響。NVIDIA DAQIRI 是一套軟體定義的資料擷取（data acquisition）函式庫，身為 NVIDIA Holoscan 平臺的一員，它把高頻寬的儀器與感測器資料直接送進 GPU-ready 的工作流程，讓開發者能在擷取過程中就處理量測資料，不必先寫入硬碟。

🧩 電子顯微鏡案例：FPGA 讀出，封包直送 GPU 記憶體

文中以 Berkeley Lab Molecular Foundry 開發的高動態範圍電子顯微鏡相機為例。電子能量損失光譜儀（EELS）量測電子與樣品交互作用後損失的能量，藉此判斷樣品含有哪些元素以及化學鍵結方式。這類訊號同時包含強訊號與弱訊號，傳統做法要用兩套分別最佳化的擷取流程依序進行，須精密協調電子光學系統、曝光時序與偵測器讀出，再把兩次測量結果對齊合併，增加了擷取與後處理的複雜度。

新相機能同時擷取強弱訊號，簡化了實驗架設與顯微鏡光學設計，但也因此產生超過 500 Gbps 的資料流。要吃下這條資料流，Berkeley Lab 與 NVIDIA 合作打造的管線是：FPGA 讀出電子元件透過 Ethernet 傳送偵測器資料，DAQIRI 把封包直接收進 GPU 記憶體，再由 GPU 運算組裝、校正偵測器畫面，最後把資料降維成能量損失光譜。這套運算流程還能改善從偵測器像素還原出的空間資訊，讓 5 微米大小的感測器像素也能達到次微米等級的空間解析度。團隊因此能在量測進行中即時檢視資料，並即時調整擷取參數與感興趣區域，同時處理超過 500 Gbps 的高頻寬資料。

🧩 新版 DAQIRI 的三項更新

文中提到，最新版 DAQIRI 針對「智慧型儀器」的資料路徑新增了三項功能：

- **硬體封包重排序**：多數網路靠協定處理或接收端緩衝來處理失序封包，會增加延遲與記憶體負擔。DAQIRI 現在可以把重排序工作 offload 給支援的 NVIDIA ConnectX-7 或更新的網路卡，對相容的序列格式，NIC 會直接解析序號欄位，把每個 payload 放進記憶體中正確的順序位置，應用程式收到的就是已排序好的資料，不需要額外的軟體重排複製步驟。
- **ibverbs 引擎**：建構在 libibverbs 與 NVIDIA DevX 之上，用於高速率的原始 Ethernet 封包收發，現為原始 Ethernet 串流的預設引擎；開發者也可以在設定中明確指定 engine: "ibverbs" 來啟用，且不需更動應用程式 API 的使用方式。
- **低延遲 NIC 直接輪詢模式**：讓應用程式執行緒直接接收與送出封包，省去交給獨立 I/O worker 的交接過程，適合需要低延遲回饋以調整擷取或控制設定的場景。

📊 ibverbs 引擎吞吐量近乎翻倍

依文中描述的基準測試（在 NVIDIA DGX Spark、IGX Thor 與 RTX PRO 伺服器平臺上進行），在小封包（最高 1024 bytes）且資料率超過 200 Gbps 的情境下，ibverbs 引擎相較於過去預設的 DPDK 後端，每核心吞吐量約提升一倍；IGX Thor 上的單佇列基準測試顯示，64-byte 與 256-byte 封包的吞吐量幾乎翻倍，8 KB 封包的吞吐量則維持相近水準。至於直接輪詢模式，在纜線回送基準測試中，應用程式從送出到接收的延遲達到 2-4 微秒的量級。

💡 不只是電子顯微鏡

文中強調，把感測器直接連到 GPU 運算的好處不限於電子顯微鏡這個案例，能從量測中擷取更多資訊，也讓儀器設計者在資料擷取、分析與即時反應上有更大的彈性。要真正享受這些好處，關鍵在於高效的資料搬移、已排序好可直接處理的 payload，以及低延遲的回饋通訊——這正是這次更新想補上的三塊拼圖。

🎯 實務啟示

對打造高速儀器或邊緣運算系統的工程師來說，DAQIRI 這類「資料直通 GPU 記憶體」的設計模式值得參考：既有的 Ethernet 介面儀器可以藉此加裝即時處理與回饋能力；設計全新儀器時，也能從一開始就把 GPU 運算納入感測器與讀出電子元件的規劃，而不是把「先寫硬碟再分析」當作預設路徑。

🔗 來源
- 標題：Enabling Real-Time AI for Scientific Instruments with GPU-Native Data Acquisition
- 作者／機構：Cara Laasch, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/enabling-real-time-ai-for-scientific-instruments-with-gpu-native-data-acquisition/

#NVIDIA #DAQIRI #GPUComputing #Holoscan #ScientificComputing #EdgeAI #DataAcquisition #ElectronMicroscopy #RealTimeAI #HighPerformanceComputing
