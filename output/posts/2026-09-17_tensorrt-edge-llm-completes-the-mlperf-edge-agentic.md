---
title: TensorRT Edge-LLM Completes the MLPerf Edge Agentic Benchmark 6.4x Faster on
  Jetson AGX Thor
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/tensorrt-edge-llm-completes-the-mlperf-edge-agentic-benchmark-6-4x-faster-on-jetson-agx-thor/
model: claude-code/sonnet
generated_at: '2026-09-17T20:33:35.374562'
score: 102
---

📌 【NVIDIA 實測】Jetson AGX Thor 跑 Agentic 推理，TensorRT Edge-LLM 快 6.4 倍

TL;DR：NVIDIA 用 NVFP4 量化、KV cache 重用與樹狀多 token 預測，把邊緣裝置上的 agentic 推理耗時砍到六分之一以下。

當 AI agent 從雲端資料中心走進車輛、機器人與其他邊緣裝置時,一個現實問題隨之浮現：agent 不像 chatbot 只回答單一提示,而是要在有限的記憶體與功耗預算內,一邊選工具、一邊評估結果,一邊在愈來愈長的對話歷史中持續推理。在 MLPerf Inference v6.1 的 Edge Agentic 測試中，NVIDIA 交出的成績是：同一顆 Qwen3.6-27B 模型，在單臺 Jetson AGX Thor Developer Kit 上，把完成時間從 2 小時 37 分壓到 24 分 36 秒。

🤔 **邊緣裝置的 Agentic 推理,難在哪裡**

MLPerf Edge Agentic 測的是一個 OpenAI 相容的模型端點,分成效能與準確度兩個階段。效能階段會重播真實記錄下來的軟體工程 agent 對話軌跡：模型接收使用者請求、產生工具呼叫、觀察工具結果，再接續同一段對話。整個工作負載包含 20 段對話、共 1,007 個生成回合，輸入長度會隨對話推進持續增長，最終逼近約 23.5K tokens，因此長上下文（long-context）處理能力是這項測試的核心考驗之一。過程中還會用 IoU（Intersection of Union）指標檢查 agent 是否真的按照劇本正確執行。準確度階段則採用 Berkeley Function Calling Leaderboard（BFCL）v4 的單輪提示，關閉推理模式，用來衡量模型是否選對函式、產生合法參數，以及在不需要工具時不亂呼叫工具。

🧩 **三個工程手段：量化、快取重用、樹狀預測**

NVIDIA 的 TensorRT Edge-LLM 提交版本，讓 Qwen3.6-27B 以 SingleStream 模式在配備 128GB 統一記憶體、MAXN 功耗模式的 Jetson AGX Thor 上運行，用了三項優化：

第一是 NVFP4 量化。邊緣裝置上低批次的 LLM 解碼通常受限於 DRAM 頻寬，縮小權重與激活值的體積能直接降低解碼延遲。這次提交的模型對權重、激活值（含語言模型頭）採用 Jetson AGX Thor 內建 NVIDIA Blackwell GPU 支援的 4-bit 浮點格式 NVFP4，KV cache 則用 FP8。模型體積縮小後，也讓 128GB 統一記憶體能留更多空間給長上下文與推測解碼所需的狀態。

第二是 KV cache 跨回合重用。Agent 對話的每個新請求，幾乎都包含前面全部歷史加上一小段新內容；若不重用快取，每一輪都要重新 prefill 整段歷史，成本隨對話拉長而累積。TensorRT Edge-LLM 會辨識可重用的提示前綴，還原對應的 attention KV 分頁；由於 Qwen3.6 採混合模型架構，runtime 也需一併還原循環狀態，才能正確接續執行,之後只需 prefill 對話新增的部分。

第三是樹狀多 token 預測（tree-based MTP）。一般自迴歸解碼每次只生成一個 token，MTP 則用一個草稿模型一次預測多個未來 token，再由目標模型一次驗證。TensorRT Edge-LLM 沒有只保留單一預測分支，而是把高機率候選組織成一棵樹，目標模型一次前向傳遞驗證多條分支，只要有分支命中就能一次推進多個 token。這次的伺服器設定用了 8 個草稿步驟、每層取前 2 名候選、共 16 節點的驗證樹；這種設計特別適合 function calling，因為工具名稱、JSON 語法等結構高度可預測，樹狀分支則能同時保留參數值的多種可能。

📊 **實測數據：52.33 tokens/秒、6.4 倍加速**

| 指標 | 結果 |
|---|---|
| 輸出吞吐量 | 52.33 tokens/秒 |
| 首個 token 中位延遲 | 247.12 ms |
| 每輸出 token 中位延遲 | 14.68 ms |
| BFCL 整體準確率 | 87.94% |

作為對照，MLCommons 公布的 llama.cpp 參考版本，同樣在 Jetson AGX Thor 上用 Q4_K_M 量化跑 Qwen3.6-27B，完成整個工作負載耗時 2 小時 37 分；TensorRT Edge-LLM 僅用 24 分 36 秒，快了 6.4 倍。素材也指出，這次負載中約 96% 的提示 token 是靠熱快取served，13.6M 總提示 token 裡只有約 0.5M 需要重新 prefill；相較於 3 步的線性 MTP，樹狀 MTP 額外帶來約 40% 的解碼效能提升。

💡 **快取重用與 MTP 是互補關係**

值得注意的是，這三項優化解決的是流程中不同階段的瓶頸：KV cache 重用降低的是「生成開始前」的重複計算成本，樹狀 MTP 降低的則是「生成過程中」目標模型的呼叫次數。兩者疊加，才讓整個 agent 軌跡（而非單次請求）的端到端時間大幅縮短，這也呼應了 agentic workload 與單輪 chatbot 推理在效能瓶頸上的本質差異。

🎯 **實務啟示**

對於要在邊緣裝置部署 agent 的團隊，這份結果指出一條可複製的路徑：先取得官方或社群提供的 NVFP4 校準檢查點（或自行做一次訓練後量化），再確認 runtime 是否支援跨回合 KV cache 重用與樹狀 MTP，而不是只把力氣花在換更大的模型上。NVIDIA 已將此次提交所用的實作開源在 TensorRT Edge-LLM 的 release/0.9.1-mlpinf 分支，包含模型匯出設定、TensorRT 引擎建置指令與 MLPerf client 設定，有興趣的開發者可依文中步驟複現。

🔗 **來源**
- 標題：TensorRT Edge-LLM Completes the MLPerf Edge Agentic Benchmark 6.4x Faster on Jetson AGX Thor
- 作者／機構：Elizabeth Goodman, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/tensorrt-edge-llm-completes-the-mlperf-edge-agentic-benchmark-6-4x-faster-on-jetson-agx-thor/

#NVIDIA #EdgeAI #TensorRT #JetsonAGXThor #MLPerf #LLMInference #AgenticAI #Quantization #KVCache #SpeculativeDecoding
