---
title: 'Zyphra Releases ZUNA1.1: An Apache 2.0 EEG Foundation Model With Variable-Length
  Inputs From 0.5 To 30 Seconds'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/17/zyphra-releases-zuna1-1-an-apache-2-0-eeg-foundation-model-with-variable-length-inputs-from-0-5-to-30-seconds/
score: 83
model: tencent/hy3:free
generated_at: '2026-07-18T07:38:37.818218'
---

📌 【Zyphra 開源】ZUNA1.1：支援 0.5–30 秒可變長度輸入的 Apache 2.0 EEG 基礎模型

TL;DR：Zyphra 釋出 ZUNA1.1 EEG 基礎模型，可接受任意通道佈局與可變長度訊號，採 Apache 2.0 授權。

🎣 **開場鉤子**
真實的 EEG 紀錄永遠不乾淨：通道會中途雜訊飆高或掉訊，錄製長度不一，從四電極頭帶到 256 通道研究帽都有。過去的開源模型卻只吃固定五秒片段——這道鴻溝現在被補上了。

🤔 **真實 EEG 的亂度，逼出模型彈性**
Zyphra 本週釋出 ZUNA1.1，延續早先開放授權的 EEG 基礎模型 ZUNA1。這次主要改動是「彈性」而非原始準確度躍進。實務上，EEG session 長度參差不齊，montage（電極配置）從消費級頭帶到高密度研究帽差異極大；ZUNA1 僅能處理固定五秒區段，ZUNA1.1 則接受 0.5 到 30 秒的可變長度輸入，並能跨任意通道佈局運作。

🧩 **380M 參數的 masked diffusion autoencoder**
README 指出，ZUNA1.1 是一個 380M 參數的 masked diffusion autoencoder（遮罩擴散自動編碼器），針對頭皮 EEG 訊號設計。給定部分通道子集時，它可：
- 對現有 EEG 段落與通道去雜訊（denoise）
- 重建缺失通道
- 根據頭皮上的物理座標，預測未曾記錄位置的新通道訊號

參數量與 ZUNA1 相同，可在消費級 GPU 執行，多數工作負載在 CPU 上也有可接受表現。

⚙️ **靠 4D 旋轉位置編碼做到 channel-agnostic**
彈性來自 tokenization 設計。ZUNA 是 transformer encoder–decoder 擴散自動編碼器，流程如下：
- 每個通道切為 0.125 秒區段（256 Hz 下為 32 個取樣點）
- 每段成為一個連續值 token
- token 以「通道 × 時間」順序序列化
- 每個 token 帶有基於 (x, y, z, t) 的 4D rotary positional encoding（旋轉位置編碼），即電極 3D 頭皮座標加粗粒度時間索引

因為模型是靠位置而非陣列索引判斷通道所在，故為 channel-agnostic：接受任意電極佈局，也能生成從未記錄過位置的訊號，進而實現依位置的任意通道上取樣（upsampling）。

🎯 **研究可用的開源落地方式**
對工程師而言，ZUNA1.1 已可直接取用：權重放於 Hugging Face，推論與前處理程式碼在 GitHub，用 `pip install zuna` 即可安裝；Zyphra 另提供免費瀏覽器版 EEG Playground。需注意，這一切僅供研究使用（research use only），且採 Apache 2.0 授權釋出。

🔗 **來源**
- 標題：Zyphra Releases ZUNA1.1: An Apache 2.0 EEG Foundation Model With Variable-Length Inputs From 0.5 To 30 Seconds
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/17/zyphra-releases-zuna1-1-an-apache-2-0-eeg-foundation-model-with-variable-length-inputs-from-0-5-to-30-seconds/

#EEG #FoundationModel #Zyphra #ZUNA1 #Apache2 #Diffusion #Transformer #Neuroscience #OpenSource #BrainSignal
