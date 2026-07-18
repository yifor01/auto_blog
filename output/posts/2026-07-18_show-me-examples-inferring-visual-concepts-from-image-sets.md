---
title: 'Show Me Examples: Inferring Visual Concepts from Image Sets'
source: Apple ML
url: https://machinelearning.apple.com/research/visual-concept-inference
score: 105
model: tencent/hy3:free
generated_at: '2026-07-18T07:31:55.299503'
---

📌 【Apple ML】從圖片集合中推論視覺概念：VICIS 新任務與架構

TL;DR：Apple ML 提出 VICIS 任務與訓練框架，補強 VLM 從影像集合推論共享概念的能力。

現今的 vision-language models (VLMs) 能聽懂複雜文字指令，卻在「只給圖、不給文字」的情境下卡關：給它一組共享某概念的範例圖，它往往無法歸納出概念，也沒辦法套用到新圖上。

🤔 **VLM 缺乏從純視覺上下文推理的能力**

摘要指出，目前的 VLMs 雖能遵循文字指令，但難以從純視覺上下文中推理。具體來說，現有模型無法從一組範例影像中推論出共享概念，並將該概念應用到新的輸入上。

🧩 **VICIS：用影像集合定義概念的新任務**

Apple ML 團隊在 ECCV 2026 發表論文，提出 Visual Concept Inference from Sets (VICIS) 這項任務來評估上述能力。任務設定為：給定一個小型的上下文影像集合（這些圖共享某個概念）以及一張查詢影像，模型必須生成新的影像——既要保留由上下文所定義的概念，又要與查詢影像保持一致。

作者觀察到，當前最先進的 VLMs 在 VICIS 上表現很差，經常忽略視覺上下文，或退化成帶有偏誤的生成結果。

為瞭解決這個落差，他們提出一個訓練框架與架構，學習如何從影像集合中推論視覺概念，並從查詢圖中提取特定於該概念的 embeddings（嵌入向量）。

📊 **在合成資料與 ImageNet/WordNet 上的實驗結果**

根據摘要，實驗在合成資料以及大規模的 ImageNet/WordNet 資料上進行。結果顯示，所提出的模型能生成更準確且更多樣化的輸出，並且能泛化到未見過的概念，以及草圖（sketches）等不同模態。素材未提供具體的量化指標或 baseline 對比數字。

⚠️ **素材未提及的限制與細節**

摘要未說明模型的具體架構層數、損失函式、訓練超引數，也未列出作者自述的侷限。相關細節需參閱原論文。

🎯 **實務啟示**

對從事 VLM 應用的工程師來說，若產品需要「給幾張參考圖就能延續風格或類別生成新圖」的能力（例如以圖搜圖後的編輯、少樣本視覺化搜尋），現成 VLMs 可能不可靠。VICIS 框架點出了一個可補強的方向：顯式地從影像集合學出 concept-specific embeddings，而不是依賴文字提示來橋接視覺概念。

🔗 **來源**
- 標題：Show Me Examples: Inferring Visual Concepts from Image Sets
- 作者／機構：Apple ML
- 連結：https://machinelearning.apple.com/research/visual-concept-inference

#ComputerVision #VLM #VICIS #VisualConcept #ImageSets #ECCV2026 #AppleML #ImageGeneration #FewShotLearning #VisionLanguageModel
