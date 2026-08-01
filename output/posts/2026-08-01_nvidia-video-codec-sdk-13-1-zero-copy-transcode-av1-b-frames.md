---
title: 'NVIDIA Video Codec SDK 13.1: Zero-Copy Transcode, AV1 B-Frames, and Frame-Accurate
  Seek'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-video-codec-sdk-13-1-zero-copy-transcode-av1-b-frames-and-frame-accurate-seek/
model: tencent/hy3:free
generated_at: '2026-08-01T08:20:27.624764'
score: 69
---

📌 【NVIDIA 更新】Video Codec SDK 13.1 發布：支援 AV1 階層式參考與精準跳轉

TL;DR：SDK 13.1 透過 AV1 階層式 B-frames 與 GOP 感知跳轉，大幅提升影片編碼品質與解碼效率。

隨著串流媒體、生成式 AI 媒體工具與遠距協作需求的激增，開發者對高效能影片處理管線（Video Pipeline）的需求日益嚴苛。NVIDIA Video Codec SDK 13.1 正式發布，透過 GPU 加速的硬體編碼與解碼引擎，為開發者提供更強大的格式處理能力與工作負載效能。

🧩 **AV1 階層式參考模式：提升 B-frames 數量至 31 個**

在 AV1 編碼中，使用 B-frames 作為參考幀能有效提升畫質。SDK 13.1 引入了「階層式參考模式」（Hierarchical Reference Mode），其設計理念如下：

- **樹狀結構設計**：將 B-frames 排列成樹狀參考結構，葉節點為非參考 B-frames，而根節點則是中間的 B-frame。
- **提升時域冗餘利用率**：此模式將 NVENC 的最大 B-frames 數量從 7 個大幅提升至 31 個。
- **效能表現**：使用此模式不會增加效能負擔，但會增加顯存（Video Memory）消耗。在高品質編碼下，使用 15 個 B-frames 的階層式參考模式，相較於高品質預設值，能節省顯著的位元率（Bitrate）。

💡 **迭代編碼與 UHQ 調校的結合**

SDK 13.1 整合了先前版本推出的兩項關鍵技術，讓延遲容忍型編碼（Latency-tolerant encoding）達到最佳的品質與效能平衡：

1. **迭代編碼 (Iterative Encoding)**：允許使用者對同一幀使用不同參數進行多次重新編碼，並能從中選擇最佳狀態提交。
2. **UHQ 調校 (UHQ Tuning)**：結合了 Lookahead（預視）層級與時間濾波（Temporal Filtering）。時間濾波透過動作估計（Motion Estimation）來減少自然影片的雜訊，平均可帶來 4–5% 的編碼增益。

📊 **解碼效能提升：獲取逐宏區塊（Per-macroblock）統計數據**

針對 H.264 與 HEVC 內容，NVDEC API 現在能直接提取詳細的逐宏區塊解碼統計數據，且無需額外的 CPU 負擔：

- **提取資訊**：包含亮度量化參數 (QP)、編碼單元類型（Intra, Inter, Skip, 或 PCM）以及最多兩個動作向量（Motion Vectors）。
- **應用場景**：這些數據能直接解鎖 GPU 加速的影片分析工作流，例如場景變更檢測、物體追蹤與鏡頭邊界分析，無需再透過 CPU 端進行位元流解析（Bitstream Parsing）。

🎯 **精準跳轉：實現 GOP 感知的隨機存取**

在 AI 推理管線或影片編輯中，開發者往往需要直接存取特定幀，而非依序解碼。SDK 13.1 透過 `NvVideoDecoder` 類別提供了全新的跳轉 API：

- **GOP 感知架構**：當請求第 N 幀時，SDK 會定位到該目標前的最近一個 IDR 幀，從該處開始解碼並跳過非參考幀，直到到達目標幀，確保僅對目標幀執行完整的解碼與後處理流程。
- **靈活的存取方式**：支援單一索引（如 0, 10, 20）、帶步長的範圍（如 0:100:10）或基於時間的存取（如 -t 1.5）。
- **快取機制**：透過 LRU（Least Recently Used）機制快取解碼器實例，避免重複建立的開銷。

⚠️ **限制**

- 使用階層式參考模式會增加顯存（Video Memory）的消耗。
- H.264 與 HEVC 的階層式參考模式預計將於未來的驅動程式版本中提供。

🔗 **來源**
- 標題：NVIDIA Video Codec SDK 13.1: Zero-Copy Transcode, AV1 B-Frames, and Frame-Accurate Seek
- 作者／機構：Elizabeth Goodman @ NVIDIA Developer
- 連結：developer.nvidia.com/blog/nvidia-video-codec-sdk-13-1-zero-copy-transcode-av1-b-frames-and-frame-accurate-seek/

#NVIDIA #VideoCodecSDK #AV1 #NVENC #NVDEC #GPUAcceleration #VideoEncoding #VideoDecoding #MachineLearning #VideoAnalytics
