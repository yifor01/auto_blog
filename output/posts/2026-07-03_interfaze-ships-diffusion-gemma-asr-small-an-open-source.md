---
title: Interfaze Ships diffusion-gemma-asr-small, an Open-Source Diffusion ASR Model
  Transcribing Six Languages via DiffusionGemma’s Parallel Denoising Decoder
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/02/interfaze-ships-diffusion-gemma-asr-small-an-open-source-diffusion-asr-model-transcribing-six-languages-via-diffusiongemmas-parallel-denoising-decoder/
score: 100
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:51:18.394367'
---

📌 【Interfaze】首個多語言擴散式 ASR 模型：用 Parallel Denoising 取代逐字生成

TL;DR：Interfaze 開源 diffusion-gemma-asr-small，透過擴散解碼器實現 6 種語言的平行語音轉文字。

大多數的語音辨識（ASR）模型都遵循自回歸（Autoregressive）邏輯，也就是一個 token 接一個 token 地生成文字。但如果我們能像影像生成模型一樣，讓所有 token 同時被「去噪」並平行生成，效率與結果會如何？

🤔 **擺脫自回歸，改用平行去噪解碼**

Interfaze 推出 diffusion-gemma-asr-small，其核心差異在於捨棄了傳統的自回歸解碼，改用 DiffusionGemma 的平行去噪解碼器（Parallel Denoising Decoder）。

- 自回歸模型：逐一生成 token。
- 擴散模型：同時精煉所有 token。

該模型採用離散擴散（Discrete Diffusion）方式生成文字。與大多數使用 `<mask>` 遮蓋方案的擴散 LLM 不同，DiffusionGemma 採用「均勻隨機 token 擴散」：首先在固定長度的畫布上填滿隨機詞彙 token，隨後在每一步迭代中保留信心值較高的預測，並將其餘部分重新隨機化，直到雜訊逐漸退火（Anneal）並凝結成最終文字。

🧩 **僅訓練 0.16% 權重，將 ASR 能力注入 26B 模型**

此模型將語音能力整合進 Google 的 26B MoE 模型 DiffusionGemma（每次啟用 4B 參數，包含 128 個專家與 top-8 路由）。

為了達成此目標，研究團隊採取了極其輕量化的訓練策略：
- 凍結 26B 的主幹網路（Backbone）。
- 僅訓練一個約 42M 參數的介面卡（Adapter）。
- 訓練參數僅佔整體權重的約 0.16%，但足以讓單一介面卡處理 6 種語言。

⚠️ **為何不能直接餵入原始波形？**

在開發過程中，團隊曾嘗試直接將原始波形餵給 LLM，但結果失敗。原因是凍結的 LLM 從未接觸過聲譜圖（Spectrogram），其 Embedding 空間缺乏對共振峰（Formants）或音素（Phonemes）的概念，導致模型選擇忽略音訊輸入，直接幻覺出流利的無意義文字。

因此，最終設計改用 frozen whisper-small 作為特徵提取器（Feature Extractor）：
1. 由 Whisper-small 將 30 秒音訊轉換為 1500 個 frames。
2. 將這些特徵透過介面卡傳遞給 DiffusionGemma。
3. 由擴散解碼器平行生成文字。

🎯 **實務啟示**

對於 ML 工程師而言，這個專案展示了「模組化組合」的強大潛力：利用 Whisper 做特徵提取 $\rightarrow$ 輕量化 Adapter 做對接 $\rightarrow$ 強大的 MoE 模型做平行生成。這證明了即使主幹網路完全凍結，只要特徵對齊正確，極少量的參數更新（42M）也能賦予大型模型全新的跨模態能力。

🔗 **來源**
- 標題：Interfaze Ships diffusion-gemma-asr-small, an Open-Source Diffusion ASR Model Transcribing Six Languages via DiffusionGemma’s Parallel Denoising Decoder
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/07/02/interfaze-ships-diffusion-gemma-asr-small-an-open-source-diffusion-asr-model-transcribing-six-languages-via-diffusiongemmas-parallel-denoising-decoder/

#ASR #DiffusionModel #DiffusionGemma #Whisper #OpenSource #SpeechToText #MoE #Multilingual #MachineLearning #Interfaze
