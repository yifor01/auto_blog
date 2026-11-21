---
title: 'Meet Thinking Machines Inkling 2 Mini: 26B Looped MoE Runs on a 32GB Mac'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/21/thinking-machines-inkling-2-mini-looped-transformer/
model: claude-code/sonnet
generated_at: '2026-11-21T22:15:45.478117'
score: 106
---

📌 【Thinking Machines 開源】26B 模型循環跑三次中間層，筆電就能帶

TL;DR：Inkling 2 Mini 用「重複使用中間層」取代堆參數，26.4B 模型壓縮到約 20GB，單臺 32GB Mac 就能跑。

多加參數換效能，是大模型的老路。但 Thinking Machines 的新模型反過來問：如果同一組權重多算幾次，是不是就能省下真正堆參數的代價？Inkling 2 Mini 的答案，是把 24 層權重跑出 48 層的效果。

🤔 **小模型想裝進一臺 Mac**

Thinking Machines Lab 釋出 Inkling 2 Mini，一個開放權重的 looped transformer，總參數 26.4B，模型以 Apache 2.0 授權在 Hugging Face 上架，並可透過 Tinker 進行託管推論與微調。它是在 11 月 5 日釋出的 594B 參數版本 Inkling 2 Small 之後的小型化版本，對開發者而言，是一個可以在地端跑 agentic coding、工具呼叫與文件處理的選項。

🧩 **24 層權重，重複使用算出 48 層效果**

模型共 24 層，分成 4 個區塊，每區塊 6 層。首尾兩個區塊各跑一次，中間兩個區塊則用共享權重重複跑 3 次，等於每個 token 實際經過 48 次層運算，但只需要儲存 24 層的權重。每一次重複運算之後，會透過「Attention Residuals」與一個學習出來的閥門（learned gate），把上一輪的「訊息」帶到下一輪。Feed-forward 層採用 Mixture-of-Experts 設計，共 128 個專家，每個 token 路由到其中 8 個。根據 README 揭露的消融實驗，循環中間層帶來 1.51 倍到 1.91 倍的等效運算增益，而循環最後幾層則只有 1.24 倍到 1.36 倍，前者在 28 項評測中贏了 27 項。換算下來，循環雖然要花更多訓練運算量，卻能省下推論運算量：一個不循環的對照模型雖然少用 7.5% 的訓練運算，卻要多花 140% 的推論運算，才能在 51.2 萬 token 長度的 agentic 資料上追上循環模型的 loss。

📊 **訓練配方與重點評測成績**

訓練一開始每層配置 384 個專家、每次啟用 8 個，到了 mid-training 階段剪掉三分之二的專家，只留下使用率最高的 128 個，接著用一個更大的內部 Inkling 模型進行 1T token 的 logit distillation 來「療傷」。後訓練則採用 SFT，再加上涵蓋 2.2T token、2000 個訓練步的強化學習，以及 on-policy distillation。權重部署上，專家層使用 NVFP4，最後 4 層使用 MXFP8，Thinking Machines 表示這樣可以省去量化轉換造成的損耗。以下是官方自評（self-reported）的部分成績：

| 評測項目 | Inkling 2 Mini |
|---|---|
| SWE-bench Verified (bash only) | 79.2% |
| SWE-bench Pro v2 (Hard) | 77.9% |
| DeepSWE v1.1 | 48.2% |
| Terminal Bench v2.1 | 71.6% |
| BrowseComp (with compaction) | 79.0% |
| MCP Atlas | 82.7% |
| OmniDocBench v1.6 | 92.8% |
| MMMU Pro | 74.9% |
| GPQA Diamond | 86.6% |
| ARC-AGI-2 | 49.3% |

在 Stanford 的 Intelligence per Watt 指標上，官方報告其在 DGX Spark 上達到 0.703，作為對照，Qwen3.6-35B-A3B 為 0.430，Gemma-4-26B-A4B 為 0.159（各自數字均來自廠商自己的 model card，測試環境不同，跨廠商比較僅供參考方向）。

⚠️ **知識類與多輪對話是弱點**

循環層數主要改善的是運算效率，而非知識儲備。報導指出，知識表現主要取決於總參數量，循環機制對此沒有幫助：Inkling 2 Mini 在 AA-Omniscience 上得分 -8.6，非幻覺率為 63.4%。多輪對話與限制條件密集的任務也不是強項，MultiChallenge 得 50.0%，ComplexConstraints v1.1 得 33.4%，在 HLE-Diamond（15.2%）與 CritPt v2 上也落後較大模型。

🎯 **怎麼跑起來**

checkpoint 約 20GB（Safetensors 格式），官方列出三種可行環境：1 臺 NVIDIA DGX Spark、32GB 以上記憶體的 Apple Silicon，或 32GB 以上 VRAM 的其他 GPU。Unsloth 與 llama.cpp 提供量化後的 GGUF 版本，推論端支援 Transformers、vLLM、SGLang、Ollama、NVIDIA Dynamo 與 TokenSpeed，vLLM 一行指令即可啟動：`vllm serve "thinkingmachines/Inkling-2-Mini"`。Tinker 上 Mini 版本的計費方式，報導中並未揭露。

🎯 **實務啟示**

如果你的部署環境卡在記憶體上限，又需要不錯的 agentic coding 能力，Inkling 2 Mini 的「循環換參數」路線值得納入評估：它用更多訓練運算換取更小的部署體積，對地端或邊緣裝置特別有吸引力。但若應用場景偏重長時間多輪對話或大量世界知識查詢，報導中的數字顯示它可能不是最佳選擇。

🔗 **來源**
- 標題：Meet Thinking Machines Inkling 2 Mini: 26B Looped MoE Runs on a 32GB Mac
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/21/thinking-machines-inkling-2-mini-looped-transformer/

#ThinkingMachines #Inkling2Mini #LoopedTransformer #MixtureOfExperts #OpenWeights #LocalLLM #EdgeAI #SWEBench #ModelEfficiency #ApacheLicense
