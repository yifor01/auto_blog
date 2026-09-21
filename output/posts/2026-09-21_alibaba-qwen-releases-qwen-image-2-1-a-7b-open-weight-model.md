---
title: 'Alibaba Qwen Releases Qwen-Image-2.1: A 7B Open-Weight Model for Image Generation
  and Editing'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/21/alibaba-qwen-releases-qwen-image-2-1/
model: claude-code/sonnet
generated_at: '2026-09-21T21:16:39.319215'
score: 97
---

📌 Qwen-Image-2.1：7B 就打贏對手的生圖模型

TL;DR：Alibaba 把生成與編輯合併進單一 7B checkpoint，靠 KV 快取重用衝出多圖編輯速度優勢。

模型越大越強，這個假設在 Alibaba Qwen 團隊手上被打了折扣。他們剛發布的 Qwen-Image-2.1，體積只有前代的三分之一左右，卻在自家 benchmark 上超越所有列出的開源模型，甚至贏過 Nano Banana 2.0。

🤔 **從兩顆模型合併成一顆**

去年（2025 年）8 月上線的初代 Qwen-Image 是 20B 參數、Apache 2.0 授權，文字轉圖和影像編輯分屬兩個獨立 checkpoint（編輯功能在 Qwen-Image-Edit）。Qwen-Image-2.1 把這兩件事收進同一個模型：一個 checkpoint 同時涵蓋文字轉圖、多參考圖編輯、局部編輯，以及透明 RGBA 輸出。視覺生成核心是 7B 參數、32 層 single-stream DiT，Qwen 團隊稱其為 Qwen-Image 系列中「最均衡、最具成本效益」的版本。

值得留意的是，這個 7B 只是 diffusion transformer 本身的規模；完整 pipeline 還要載入一顆 8B 的 Qwen3-VL 編碼器，做容量規劃時得把這塊算進去。

🧩 **速度秘密在 attention mask 的分工**

Qwen 把這套機制稱為 mixed-granularity attention：文字 token 使用 token-level causal mask，圖片 token 則在各自影像內使用 chunk-level bidirectional mask。條件前綴（condition prefix）被放在 noisy latent 之前，因此它永遠不會關注（attend to）noisy latent，這代表它的 key/value 在整個去噪過程中維持固定。

實際運作上，模型只在第一步計算一次文字與輸入圖片的表徵，之後每一個去噪步驟都重複使用同一份 prefix KV 快取。參考圖片數量越多，這份快取省下的重複計算就越多，這也是官方強調的多圖編輯速度優勢的來源。

📊 **Qwen-Image-Bench 上的名次**

在 Qwen 自家的 Qwen-Image-Bench 上，Qwen-Image-2.1 拿下 60.28 分，高於 Nano Banana 2.0 的 59.82，也高於榜上所有其他開源模型，包括 32B 的開源模型 FLUX 2 Max（55.33 分）。不過在封閉模型陣營中仍有 6 款分數更高，榜首是 GPT Image 2.5 Sunburst 的 67.01 分。

🧩 **部署與生態系支援**

環境需求為 PyTorch 2.4.0 以上、transformers 5.17 以上、從原始碼安裝的 Diffusers，以及 accelerate、pillow。同一個 pipeline 只要傳入 image= 參數（1 張或多張參考圖）即可切換到編輯模式；GPU 記憶體吃緊時可用 pipe.enable_model_cpu_offload() 降壓。

Day 0 支援涵蓋 Diffusers、ComfyUI、vLLM-Omni、SGLang、LightX2V。其中 vLLM-Omni 提供 FP8 量化、prefix KV 快取、CUDA Graph decode 與 tensor parallelism；SGLang 則有 Cache-DiT、CUDA graphs、多 GPU 平行化與元件卸載（component offload）；ComfyUI 已備妥原生節點與轉換後權重。硬體支援也不侷限 NVIDIA，還涵蓋 AMD Radeon（透過 ROCm）以及透過 FlagOS 支援的 8 種晶片平臺。

Qwen 團隊同時釋出兩個 prompt 改寫模型，是基於 Qwen3.5-VL 9B 微調出的文字轉圖、編輯專用 checkpoint，可將簡短 prompt 擴寫成詳細描述，並能自動挑選長寬比。

⚠️ **研究可用，商用要另外談**

目前的權重與授權定位是研究與評估用途；若要商業部署，需要向 Qwen 另外取得授權，這點和初代 Apache 2.0 的開放程度不同，評估導入前務必先確認授權範圍。

🎯 **實務啟示**

對於需要文字轉圖與編輯共用一套 pipeline 的團隊，Qwen-Image-2.1 把部署複雜度從「兩個 checkpoint 各自維運」降成「一個模型走天下」，加上 prefix KV 快取對多參考圖編輯場景特別友善，值得在需要頻繁多圖迭代編輯的產品中優先評估；但商用授權與 8B 編碼器帶來的實際顯存需求，都是上線前該先算清楚的成本項。

🔗 **來源**
- 標題：Alibaba Qwen Releases Qwen-Image-2.1: A 7B Open-Weight Model for Image Generation and Editing
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/21/alibaba-qwen-releases-qwen-image-2-1/

#QwenImage #AlibabaAI #ImageGeneration #ImageEditing #DiffusionModel #OpenWeightModels #DiT #KVCache #Diffusers #AIInference
