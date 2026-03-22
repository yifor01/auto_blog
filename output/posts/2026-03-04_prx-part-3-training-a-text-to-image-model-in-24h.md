---
title: "PRX Part 3 — Training a Text-to-Image Model in 24h!"
source: HuggingFace Blog
url: https://huggingface.co/blog/Photoroom/prx-part3
score: 113
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-04T19:07:19.940857
---

# 📌 24小時訓練出文生圖模型？Photoroom 的 PRX 速度挑戰

你以為訓練一個競爭力的文生圖模型需要幾百萬美金和數週時間？Photoroom 用 24 小時和 1,500 美元，用一場極限速度跑告訴你：這一切正在改變。

## 🤔 為什麼要做 24 小時速度跑？

在前兩篇深入分析各種 Diffusion 模型優化技巧後，Photoroom 團隊面臨一個實際問題：**當我們把所有有效的技巧堆疊在一起，能走多遠？**

他們設定了嚴格的限制條件：
- **32 顆 H200 GPU**
- **24 小時時間限制**
- **約 1,500 美元預算** (2$/小時/顆 GPU)

這與早期訓練文生圖模型動輒數百萬美元的時代形成鮮明對比，展示了透過精密工程，我們能在一天內達到什麼樣的成果。

## 🧪 他們用了哪些關鍵技術？

### X-prediction 與像素空間訓練
跳過傳統的 VAE 壓縮，直接在像素空間進行預測，減少資訊損失和計算開銷。

### 感知損失 (Perceptual Losses)
使用預訓練的感知模型來指導訓練，確保生成的圖片在人眼看起來更真實，而不只是數學上接近。

### TREAD Token Routing
創新的 Token Routing 機制，讓模型能更有效地分配計算資源到重要的影像特徵上。

### 表徵對齊 (REPA + DINOv3)
結合 REPA 和 DINOv3 進行表徵對齊，提升模型的泛化能力和穩定性。

### Muon Optimizer
使用 Muon 優化器，這是一種針對大規模訓練優化的新一代優化演算法。

## 🎯 為什麼這很重要？

這不只是一場技術表演。Photoroom 表示，這場 24 小時速度跑很可能成為他們未來大規模訓練的基礎配方。

更重要的是，**他們開源了所有程式碼**，包含：
- 這次速度跑的完整訓練程式碼
- 前兩篇部落格使用的實驗框架
- 所有技術組合的實作細節

## ⚠️ 關鍵洞察

這項工作的真正價值在於展示了**當前擴散模型訓練的效率革命**。透過正確的技術組合，我們可以用以前 1% 的成本獲得可比的結果。這不僅降低了研究門檻，也讓小型團隊能夠參與文生圖領域的創新。

## 🎯 實務啟示

如果你正在考慮訓練自己的文生圖模型：
- 不要從頭重複造輪子，站在巨人的肩膀上
- 像素空間訓練可能比傳統 VAE 更有效率
- 感知損失能顯著提升人眼感知品質
- 開源框架讓你可以快速驗證想法

## 🔗 論文連結

📝 PRX Part 3 — Training a Text-to-Image Model in 24h!
👤 David Bertoin, Roman Frigg, Jon Almazán @ Photoroom
🔗 論文：huggingface.co/blog/Photoroom/prx-part3
🔗 GitHub：github.com/Photoroom/prx (開源程式碼)

你認為未來文生圖模型的訓練成本還能壓到多低？歡迎分享你的看法 👇

#AI #文生圖 #DiffusionModels #MachineLearning #開源 #Photoroom #HuggingFace #技術創新
