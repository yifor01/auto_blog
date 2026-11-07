---
title: Speed Up Image Generation with FLUX 3 Image Klein on NVIDIA Blackwell GPUs
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/
model: claude-code/sonnet
generated_at: '2026-11-07T20:59:25.398500'
score: 93
---

📌 【NVIDIA 實測】FLUX 3 Image Klein 在 Blackwell B200 衝上 3.46 倍生成速度

TL;DR:疊加 NVFP4、量化注意力與稀疏注意力後，單張 B200 生成速度最高提升 3.46 倍。

想像你在設計工具裡按下「生成」，畫面卻要等上十幾秒才跑完一輪 diffusion 的多次反覆運算，解析度一拉高，attention 的運算量更是直線上升。NVIDIA 在這篇教學中，示範如何用 TensorRT LLM VisualGen 把 Black Forest Labs 的 FLUX 3 Image Klein 從「等得不耐煩」調校到接近即時可用。

🤔 高解析度 diffusion 的老問題：每一步都要等

FLUX 3 Image Klein 是 Black Forest Labs（BFL）打造的影像編輯與生成模型，訓練於 NVIDIA GB200 NVL72，並針對 NVIDIA GPU 最佳化。它提供 Base 與 distilled 兩種 checkpoint，分別對應不同的延遲與畫質需求。架構上，Klein 結合 Qwen3-VL-4B-Instruct 做文字條件化、一個 diffusion transformer（DiT）負責細化影像 latent，再由 autoencoder 將 latent 解碼成影像（I2I 模式下也負責編碼參考影像）。文字、帶噪的目標影像、以及可選的參考影像這三條串流會先分別處理，再透過 joint attention 融合。

🧩 從 NVFP4 起跑，層層疊加最佳化

TensorRT LLM VisualGen 是 TensorRT LLM 內專門處理視覺生成的執行環境，支援 BF16、FP8、NVFP4 三種精度。在 Blackwell GPU 上，NVFP4 相較 BF16 就能帶來 1.62 倍的 T2I 與 1.58 倍的 I2I 加速，因此教學以 NVFP4 作為後續最佳化的起點。接下來的加速手段分成三層：

- GEMM 核心最佳化：採用 FlashInfer 的 PrimsTS FP8/NVFP4 GEMM 核心（以 CUTLASS Primitives and Task Scheduling 打造），針對 FLUX 3 的張量形狀調校，並把 GEMM 與 SwiGLU、QKV 投影、RoPE 等運算融合進同一個 epilogue，讓 NVFP4 T2I 比原本自動調校的 TensorRT LLM NVFP4 GEMM 再快 1.02 至 1.10 倍。
- 量化注意力：在 2048×2048 的 T2I 測試中，VANILLA BF16 attention 佔了 DiT GPU 運算時間近六成。換成 cuDNN FP8 可帶來 1.08 倍（Base）與 1.09 倍（distilled）的加速；換成 TensorRT LLM 的 VC-Attention FP8（repair budget ρ=0.005，用來校正量化誤差最大的那批 token），加速幅度進一步提升到 1.18 倍與 1.16 倍。
- 稀疏注意力：Sol-Attention 透過 τ 參數控制稀疏程度，搭配 PrimsTS 的 block-sparse attention 核心。在 FLUX 3 Image Klein Base、τ=1.0 的設定下，搭配 16 步初始 dense 步驟時，denoising 加 decode 比 compiled dense VANILLA 快 1.24 倍；若把初始 dense 步驟降到 12，則提升到 1.30 倍。

📊 denoising 吃掉九成以上時間，也最值得優化

在 B200、2048×2048、NVFP4＋VANILLA attention＋torch.compile 的條件下，完整 pipeline 的延遲拆解如下（Base 用 50 步 denoising、CFG scale 3.5；distilled Klein 用 16 步、不含 CFG）：

| 任務 | 模型 | 文字處理＋前處理 | Denoising | 解碼＋後處理 | 總延遲 | Denoising 佔比 |
|---|---|---|---|---|---|---|
| T2I | Base | 47 ms | 14.24 s | 416 ms | 14.70 s | 96.8% |
| T2I | Distilled | 24 ms | 2.28 s | 410 ms | 2.71 s | 84.0% |
| I2I | Base | 468 ms | 39.40 s | 417 ms | 40.29 s | 97.8% |
| I2I | Distilled | 407 ms | 6.65 s | 418 ms | 7.48 s | 89.0% |

無論任務類型，denoising 都是壓倒性的大頭，這也是後續優化手段幾乎都繞著 DiT 加速打轉的原因。把上述優化全部疊加後，NVIDIA 報告在單張 B200、2048×2048 的條件下，FLUX 3 Image Klein Base 相較未編譯的 BF16 推論，T2I 最高加速 3.46 倍，I2I 最高加速 4.45 倍。

💡 加速不是免費的，LPIPS 分數記錄了畫質代價

每種注意力最佳化都附上了 LPIPS（Learned Perceptual Image Patch Similarity）分數，數字越低代表跟 VANILLA 基準輸出越相似。cuDNN FP8 的 LPIPS 落在 0.072（Base）與 0.161（distilled）；VC-Attention FP8 則是 0.086 與 0.151。這組數字說明，在 2048×2048 解析度上，VC-Attention FP8 同時拿到更快的速度與更接近基準的畫質，是教學中建議的量化注意力選項。

⚠️ 稀疏程度拉太高，劃不來

教學特別提到，提高 Sol-Attention 的 τ 雖然理論上能再省運算，但實測畫質下降的幅度，換不來多少額外的速度提升。稀疏注意力的收益在 τ=1.0 附近就接近飽和，盲目調高只是在犧牲畫質。

🎯 實務啟示

這類優化多半只需要改 YAML 設定檔，例如把 `pipeline_config.variant` 設為 `nvfp4`，或在 `attention_config` 裡切換 `CUDNN`、`TRTLLM`（VC-Attention）、或 `sol_attn` 等後端，不需要重寫推論程式碼。對於要把 diffusion 模型部署進設計工具、影像編輯器的工程師來說，這份教學提供的是一套「延遲 vs 畫質」的實測取捨表：追求極速可選 NVFP4＋Sol-Attention，追求畫質穩定則優先疊加 VC-Attention FP8，再視情況加入稀疏注意力。

🔗 來源
- 標題：Speed Up Image Generation with FLUX 3 Image Klein on NVIDIA Blackwell GPUs
- 作者／機構：Olivia Stoner／NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/

#FLUX3 #NVIDIA #Blackwell #TensorRTLLM #DiffusionModels #NVFP4 #ImageGeneration #GPUOptimization #BlackForestLabs #AIInference
