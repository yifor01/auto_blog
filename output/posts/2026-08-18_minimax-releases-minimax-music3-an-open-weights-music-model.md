---
title: 'MiniMax Releases MiniMax-Music3: An Open-Weights Music Model Generating Complete
  Five-Minute Songs From Lyrics and a Structured Caption'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/17/minimax-releases-minimax-music3/
model: claude-code/sonnet
generated_at: '2026-08-18T06:25:31.497299'
score: 109
---

📌 MiniMax 開源 Music3：一次生成完整五分鐘歌曲

TL;DR：開源文字轉音樂模型，輸入歌詞與音樂描述即可一次生成五分鐘完整歌曲，當天就能部署。

多數 AI 音樂生成工具只能吐出幾十秒的片段，剩下的拼接、對齊全靠人工。MiniMax 這次直接把目標訂在「一次生成一首完整歌曲」，而且從權重、推論程式碼到三條部署路徑，都在發佈當天一併釋出。

🤔 **兩個輸入，一次生成到底**

MiniMax-Music3 是一個開放權重（open-weights）的文字轉音樂模型，接收兩個獨立輸入：一段帶有段落標籤的歌詞，以及一份結構化的音樂描述（Structured Caption）。模型會直接輸出長度最長五分鐘的完整歌曲，格式為 32 kHz、16-bit 立體聲 WAV，不需要額外的分段拼接。

🧩 **Hybrid-LM 搭配 Flow-VAE 的兩段式架構**

訓練用的 tokenizer 採用八層 residual vector quantization（RVQ）：第一層是語意 codebook，擁有 16,384 個條目，負責承載核心音樂語意與結構；其餘七層是聲學 codebook，各有 1,024 個條目，負責編碼殘差細節。訓練時先最佳化語意層，再讓八層一起聯合訓練。

生成端則是所謂的 Hybrid-LM：一個 8B 的 Global LLM 逐幀預測第一個 RVQ codebook、掌握長距離結構，搭配一個 0.6B 的 Local LLM 在每一幀內預測其餘的 codebook。值得注意的是，模型卡與授權文件寫的基礎模型是 Qwen3-8B，但 MiniMax 官方研究文章寫的是 Qwen3.5-8B，兩者說法不一致，確切的底層 checkpoint 目前尚未確認。

真正的設計亮點在合成階段。模型並非從離散 RVQ token 直接解碼，而是融合兩個 LLM 的最終隱藏狀態，拿去條件化一個 2.4B 的 flow-matching 模組，映射到潛在空間後，再由一個從 MiniMax Speech 繼承而來的 123M Flow-VAE 解碼。推論時，離散 tokenizer 的解碼器完全不會被載入。

🧩 **輸入格式：段落標籤加三段式描述**

歌詞本身以獨立行標記段落，包含 [Intro]、[Verse]、[Pre-Chorus]、[Chorus]、[Post-Chorus]、[Bridge]、[Instrumental]、[Solo]、[Outro] 等標籤。另外還有一份獨立的 Structured Caption，涵蓋 Global Metadata、Vocal Details、Arrangement 三部分。MiniMax 也附上一個 music-caption-rewriter agent skill，能離線把一句簡短描述展開成這種三段式格式。

🎯 **三條部署路徑，各自對應不同資源**

MiniMax 同時提供三種推論方式：SGLang-Omni 作為官方參考伺服器，GitHub 頁面指定需要兩張 CUDA GPU，GPU 0 跑 Qwen3 與 RVQ 自迴歸生成、GPU 1 跑 flow matching 與 DAV 解碼；diffusers 的 modular pipeline 在全精度下需求低於 24 GB VRAM，搭配自動 CPU offload 可降到約 22 GB，用 leaf-level group offloading 甚至能壓到 8 GB；ComfyUI 則提供原生的 Text to Music 範本，使用 Comfy-Org 重新打包的 FP16/INT8 權重。對於想在本地跑完整歌曲生成、又受限於顯卡資源的團隊，這三條路徑等於直接給出從高階伺服器到消費級顯卡的完整選項。

🔗 **來源**
- 標題：MiniMax Releases MiniMax-Music3: An Open-Weights Music Model Generating Complete Five-Minute Songs From Lyrics and a Structured Caption
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/17/minimax-releases-minimax-music3/

#MiniMax #TextToMusic #OpenWeights #FlowMatching #MusicGeneration #AIMusic #GenerativeAI #DeepLearning #OpenSource #MachineLearning
