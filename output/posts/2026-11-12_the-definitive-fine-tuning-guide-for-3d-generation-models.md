---
title: The Definitive Fine-Tuning Guide for 3D Generation Models
source: HuggingFace Blog
url: https://huggingface.co/blog/3d-lora-finetuning
model: claude-code/sonnet
generated_at: '2026-11-12T22:58:47.763513'
score: 94
---

📌 【HuggingFace 實戰教學】只動9.3M參數，用LoRA修好TRELLIS.2的鞋底幾何

TL;DR：HuggingFace釋出TRELLIS.2的LoRA微調腳本與容器，教你只調整關鍵模組就能修正3D生成細節。

3D生成模型畫出來的鞋子乍看沒問題，拿近一看才發現鞋底的幾何完全不對。這正是通用3D生成模型最棘手的狀況：整體看起來「差不多對」，但對特定應用來說，差的那一點就是致命傷。

🤔 **通用模型的細節誤差，誰來修？**

3D生成在機器人、模擬、媒體娛樂等領域都有應用，但這個領域長期被檔案格式（GLB、PLY）與表示方式（NeRF、3D Gaussian splatting）的分裂所困擾，不同表示法各有優缺點，難以統一。TRELLIS 率先提出了一套統一的潛在表示（unified latent representation），讓同一個模型可以透過不同的 decoder 輸出各種格式；後續推出的 TRELLIS.2 則進一步改善了3D結構的表示能力。但兩個模型都沒有提供簡單的方式，讓使用者針對特定任務做調整。

HuggingFace 團隊以 Google Scanned Objects（GSO）資料集中188個鞋類物件的子集做實驗，發現預訓練模型產生的鞋子外觀通常正確，但鞋底經常出錯，於是測試能否用 LoRA 讓鞋底的幾何更準確。

🧩 **拆解TRELLIS.2的五個階段，決定在哪裡動手**

TRELLIS.2 的生成流程可以用文字拆成五個步驟：

1. 去背：BiRefNet 移除輸入圖片的背景。
2. 影像編碼：DINOv3-L 將圖片編碼為特徵 token，作為後續生成的引導訊號。
3. 粗略結構生成：一個 diffusion transformer（DiT）預測物件的粗略形狀，產生 16³ × 8 的小型 latent，再由 VAE decoder 轉換成 64×64×64 的 occupancy grid（記錄每個 voxel 是否屬於物件本體）。
4. 細節幾何生成：shape flow DiT 根據 occupancy grid 與 DINOv3 特徵 token，產生 latent，再由另一個 VAE decoder 轉成解析度 512×512×512 的 O-Voxel 幾何。
5. 材質生成：texture flow DiT 根據形狀 latent 與 DINOv3 特徵，決定表面材質，VAE decoder 再輸出每個 voxel 的 base color、metallic、roughness、alpha 值，最後整合成帶材質的 mesh，匯出為 GLB 檔。

其中 O-Voxel 是 TRELLIS.2 的3D格式，只保留物件表面的 voxel；而結構化稀疏 latent（structured sparse latents）讓模型只需要處理約10%的 voxel，因此 shape flow DiT 與 texture flow DiT 都是稀疏 transformer，只有負責粗略結構的 sparse-structure flow DiT 是密集 transformer。

團隊只在 sparse-structure flow DiT 與 shape flow DiT 這兩個控制形狀與幾何的模組加上 LoRA adapter，刻意凍結 texture flow DiT。原因是他們的資料集只有 diffuse color map，混雜了烘焗（baked）光影效果，缺乏訓練材質階段所需的獨立材質圖；如果硬訓練，模型可能把光影誤學成表面材質的屬性，甚至造成 catastrophic forgetting（遺忘原本學到的能力）。選擇凍結哪些模組，和選擇微調哪些模組一樣重要。

💡 **為什麼是LoRA，不是全參數微調**

188個鞋類物件只是 GSO 全部1030個物件中的一小部分，資料量不大。全參數微調成本更高，也更容易蓋掉模型原本學到的先驗知識（priors）。這次設定在兩個目標 DiT 上總共只訓練約9.3M個 adapter 參數：sparse-structure flow DiT 的 attention 與 MLP 層用 rank 8，shape flow DiT 的 attention 層用 rank 16。rank 越高，adapter 能學到的東西越多，但參數量也隨之增加。

🎯 **實務啟示**

HuggingFace 提供了兩個 Docker 映像檔，一個負責前處理，一個負責微調，可以在 Hugging Face Jobs 上跑，也能在本機 GPU 上執行。要開始之前需要準備 HF_TOKEN，並確保帳號有權限存取 DINOv3（屬於 gated model）；若要用自己的資料集，記得先把 mesh 上傳到 Hub。對於想微調大型3D生成模型的工程師來說，這個案例示範了一個可複製的方法論：先拆解 pipeline 各階段的職責，再根據資料是否齊備決定凍結或微調，而非盲目對整個模型下手。

🔗 **來源**
- 標題：The Definitive Fine-Tuning Guide for 3D Generation Models
- 作者／機構：Suvaditya Mukherjee、merve、Pedro Cuenca @ HuggingFace
- 連結：https://huggingface.co/blog/3d-lora-finetuning

#3DGeneration #LoRA #PEFT #HuggingFace #TRELLIS #DiffusionTransformer #FineTuning #MachineLearning #3DAssets #AIInfra
