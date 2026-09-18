---
title: 'Nunchux AI Introduces VC-Attention: A Training-Free Low-Bit Attention Kernel
  That Speeds Up Video Diffusion Transformers'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/16/nunchux-ai-introduces-vc-attention-a-training-free-low-bit-attention-kernel-that-speeds-up-video-diffusion-transformers/
model: claude-code/sonnet
generated_at: '2026-09-18T19:45:27.818516'
score: 102
---

📌 影片 Diffusion Transformer 的注意力,免訓練也能壓成低位元

TL;DR：Nunchux AI 的 VC-Attention 不需重新訓練,針對 value 量化誤差與 softmax 瓶頸,在 B200 上比 SageAttention2 快 6 倍。

生成一段 5 秒的 720p 影片,光是 attention 計算就可能吃掉超過六成的生成時間。這不是誇張的說法,而是 Nunchux AI 在 RTX 5090 上實測 Wan2.2-14B 得到的數字。

🤔 **兩個推遲已久的瓶頸:value 量化與 softmax**

影片 DiTs(Diffusion Transformers)把一整段影片攤平成一串時空 token,每一層都跑完整的 self-attention。一段 5 秒 720p 的 Wan2.2-14B 影片,序列長度約 70K token,在 RTX 5090 上 attention 佔去超過 64% 的生成時間;研究團隊也指出,在單張 B200 上,attention 約佔 MiniMax-H3 每一步去噪過程的三分之二。

低位元 Tensor Core 理論上能加速 QK 與 PV 這兩個矩陣乘法,但有兩道障礙。第一,像 SageAttention2 這類既有方法會對 query 與 key 做平滑化,但做完 QK 平滑與旋轉之後,value 項反而貢獻了 Wan2.2 上 82% 的輸出誤差,等於沒真正解決問題。第二,QK 與 PV 之間的 softmax 目前仍跑在 FP32,在 B200 與 H200 上,這段指數運算加上轉成 FP8 的過程,是整條 pipeline 中耗時最長的一段。

🧩 **V-Smooth 與 ExpCast-FP8,兩個針對性設計**

Value 的離群值集中在少數 token 上,且其所在的 channel 會隨 head、layer、去噪步驟而變動。Hadamard 旋轉會保留 token 的 norm,因此無法消除這些離群值——實測旋轉 V 只讓誤差變化 0.2%。V-Smooth 改走另一條路:在 100 個 Wan2.2 head 上取平均,以序列順序分塊求平均可消除 8% 的區塊能量,換成 DeltaQuant 的靜態立方分塊可達 12%,排序後則達 36%。每個均值運算的成本是每個 value 元素 0.125 bit,而分組只在去噪過程的前 25% 步驟執行,排列方式在相鄰 4 步之間重複使用,攤平到整個排程後,分組僅佔 attention 時間的 3% 到 4%。

另一個關鍵設計是 ExpCast-FP8。E4M3 格式的一個 byte 本身就很接近其所儲存數值的對數,若把它當整數讀取,約等於 8×log2(v)+56。ExpCast-FP8 因此能用一次融合乘加運算,直接從對數域分數寫出目標 byte,常數 β=-0.35 用來置中殘餘誤差,且不需針對個別模型調整。這條直接路徑在每次數值倍增區間中,有 79.6% 與「先算 FP32 指數再轉型」的路徑寫出完全相同的 byte,其餘情況也只差一個編碼單位。論文證明每一列的 total variation 誤差上界為 3.64%(加上底線溢位尾端),在 204.8K 筆 Wan2.2 attention 資料列上實測平均誤差為 1.6%。由於 NVFP4 沒有單一的仿射對數到編碼映射,ExpCast-FP8 目前只適用於 8-bit kernel。團隊以手寫 CuTe/CUDA 融合前處理鏈,把單次 V-Smooth 呼叫的耗時從 42.2 毫秒壓到 4.8 毫秒(B200)。

📊 **B200 上比 SageAttention2 快 6 倍**

測試涵蓋四個開源權重的影片 DiT:Wan2.2-T2V-A14B、LongCat-Video、HunyuanVideo-1.5、MiniMax-H3,並以 100 個 prompt 對照 BF16 FlashAttention-4 的輸出評估保真度。在 B200 上,VC-Attention 比 SageAttention2 快 6.02 倍(SageAttention2 本身沒有 Blackwell kernel);在 H200 上差距縮小到 1.16 倍。工作站級顯卡方面,4-bit 版 V-Smooth 在 RTX PRO 6000 上與 SageAttention3 打平,在 RTX 5090 上差距在 5% 以內,此時保真度成為真正的區分點。以 MiniMax-H3 在 1344×768 解析度為例,attention 在 B200 上比 BF16 FlashAttention-4 快 1.60 倍,PSNR 為 20.2 dB,略優於 SageAttention2 的 19.9 dB;在 B300 上論文報告 1.47 倍(對照原生 FP8 kernel 的 1.31 倍),部落格圖表則列出 1.51 倍。Nunchux 自家的專有延伸版本 Nunchux Attention,在 MiniMax-H3 attention 上於 B200 達 1.91 倍、B300 達 1.83 倍。

🎯 **實務啟示**

VC-Attention 只改變單次互動的計算成本,因此可以與 Sparse VideoGen、Radial Attention 這類稀疏 attention 方法,以及蒸餾與多 GPU 執行並存疊加,不是互斥的最佳化手段。對正在跑影片 DiT 推論、又苦於 attention 佔用大半生成時間的團隊來說,這是一個免訓練、可直接疊加的加速選項;Nunchux 也表示 MiniMax-H3 的免費存取即將透過 Modelverse waitlist 開放。

🔗 **來源**
- 標題:Nunchux AI Introduces VC-Attention: A Training-Free Low-Bit Attention Kernel That Speeds Up Video Diffusion Transformers
- 作者/機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/16/nunchux-ai-introduces-vc-attention-a-training-free-low-bit-attention-kernel-that-speeds-up-video-diffusion-transformers/

#VideoDiffusion #AttentionKernel #FP8 #Quantization #DiffusionTransformer #GPUOptimization #CUDA #VideoGeneration #NunchuxAI #LowBitInference
