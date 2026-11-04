---
title: Tencent WeVisOne-VL Unifies Detection, OCR, Segmentation and Matting
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/03/tencent-wevisone-vl-vision-language-model/
model: claude-code/sonnet
generated_at: '2026-11-04T22:47:12.598624'
score: 106
---

📌 一個模型搞定偵測、OCR、分割與摳圖,騰訊開源 WeVisOne-VL

TL;DR：騰訊微信視覺團隊開源 2B/4B 視覺語言模型,單模型可取代偵測器、OCR 引擎與分割器三套工具。

如果你的影像辨識 pipeline 裡同時掛著一個偵測器、一個 OCR 引擎、一個分割模型,現在騰訊給了另一個選項:把這三件事(再加上計數、指向與摳圖)都丟進同一個模型。

🤔 **感知任務太碎片化,工程師得維護一整套工具鏈**

WeVisOne-VL(WeChat Vision All-in-One)是騰訊微信視覺團隊基於 Qwen3-VL 打造的感知型模型,主打的不是開放式對話,而是細粒度定位(fine-grained localization)。根據素材描述,它一個模型就能處理偵測(detection)、指稱(referring)、計數(counting)、指向(pointing)、OCR、分割(segmentation)與 alpha 摳圖(matting),而輸出像素結果靠的是一個僅 9.6M 參數的解碼器,因此不需要額外掛一個 SAM 做分割。這對開發者的實際意義很直接:原本要串接的偵測器、OCR 引擎、分割模型三套系統,理論上可以收斂成一個模型呼叫。

🧩 **座標當 token 預測,配一顆專職像素解碼器**

WeVisOne-VL 讓使用者自行選擇輸出粒度:點、框、二值遮罩或連續的 alpha 摳圖值。每個任務都被轉成結構化的 next-token 預測問題,模型為此新增了 `<0>` 到 `<1000>` 的座標 token,用來表示正規化後的框與點座標。如果查詢的目標物根本不存在畫面中,模型會直接輸出 "None",而不是硬猜一個框出來。

針對需要輸出像素層級結果的任務,模型會在每個預測框之後產生一個 `<OBJ>` token,根據模型卡的說明,這個 token 的隱藏狀態(hidden state)會作為查詢向量(query)餵給像素解碼器,由解碼器負責產生實際的遮罩或摳圖。

🧩 **1 億張圖、36 億個框打底的資料引擎**

訓練資料來自一套知識圖譜驅動的資料引擎,標註了超過 1 億張影像、約 36 億個框。流程上,SAM3、Rex-Omni 與騰訊自家偵測器負責提出候選區域(region proposal),再由 Qwen3-VL 負責驗證這些候選是否正確。

訓練分成三個監督式微調(SFT)階段:第一階段用 9000 萬筆資料對齊輸出格式;第二階段把輸入視覺 token 數提高到 1,960,並讓單筆回應最多包含 500 個框;第三階段訓練像素解碼器,再用 1.3 億筆樣本專門針對摳圖任務做特化。最後還有一個 GRPO 強化學習階段,使用 17.8 萬筆經過不確定性篩選(uncertainty-filtered)的樣本,相關細節記載於論文中。

📊 **自報數據:4B 整體領先,但 2B 在特定摳圖任務反超**

素材特別強調以下數字都是自我報告(self-reported),採用 greedy decoding,每張影像最多使用 1,960 個視覺 token;偵測、指稱與 OCR 任務的指標是 IoU 0.5 到 0.95 區間的平均 F1。整體而言 2B 模型在多數任務上落後 4B 模型,但在 P3M-500-NP 資料集的框提示摳圖(box-prompted matting)任務上,2B 反而以 6.6 MAD 的成績表現更好。

⚠️ **目前的限制**

素材提到兩項明確限制:微調(fine-tuning)程式碼目前仍在 TODO 清單上,尚未釋出;另外 GGUF 格式的建置版本無法產生遮罩,因為像素解碼器需要模型原生的視覺特徵,GGUF 轉換後拿不到這些特徵。

🎯 **實務啟示**

2B 與 4B 權重已上架 Hugging Face,並提供 wevisone_vl 套件包裝 Transformers 與 vLLM 兩種後端,涵蓋 detection、referring、point、count_box、ocr、segmentation、matting 等任務介面,也有對應的線上 demo。對需要在同一條 pipeline 裡做多種影像感知任務的團隊來說,這是一個值得評估的「一個模型頂多個工具」選項,但在微調能力與 GGUF 部署這兩塊,目前還有實際落地上的限制要留意。

🔗 **來源**
- 標題：Tencent WeVisOne-VL Unifies Detection, OCR, Segmentation and Matting
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/03/tencent-wevisone-vl-vision-language-model/

#VisionLanguageModel #Tencent #OpenSource #ComputerVision #OCR #ImageSegmentation #Matting #Qwen3VL #MultimodalAI #ObjectDetection
