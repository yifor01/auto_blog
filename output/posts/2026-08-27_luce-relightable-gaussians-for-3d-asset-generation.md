---
title: 'Luce: Relightable Gaussians for 3D Asset Generation'
source: Apple ML
url: https://machinelearning.apple.com/research/relightable-gaussians-3d-generation
model: claude-code/sonnet
generated_at: '2026-08-27T17:15:56.801790'
score: 110
---

📌 【Apple ML】Luce:一張圖生成可重新打光的 3D 資產

TL;DR：Apple ML 提出 Luce,用統一的多模態高斯表示同時捕捉幾何與 PBR 材質，讓單張圖片生成的 3D 資產可直接重新打光。

3D 生成模型近年在「形狀對不對」上進步飛快，但生成出來的物件放進遊戲引擎或渲染管線後，往往打光就露餡——因為模型只學到了顏色，沒學到材質。

🤔 **image-to-3D 生成缺的那一塊：材質**

高品質的 image-to-3D 生成，需要一種同時捕捉幾何與外觀的 3D 表示。若要支援重新打光（relighting）並整合進標準渲染管線，這個表示還必須包含物理基礎渲染（PBR）所需的模態，例如反照率（albedo）、金屬度／粗糙度（metallic-roughness）與表面法線（surface normals）。這正是 Apple ML 團隊在論文中要解決的問題。

🧩 **體素化的多模態高斯雲**

Luce 提出一種 3D 表示，將幾何與 PBR 材質統一在一個體素化（voxelized）的多模態高斯雲（Gaussian cloud）中，每種模態各自使用專屬的高斯基元（Gaussian primitives）。整套生成流程可以拆解為：

- 一個變分自編碼器（VAE）先將這個多模態高斯表示壓縮進一個統一的、具材質感知能力的潛在空間（latent space）。
- 一個 rectified-flow transformer 從單張輸入圖片生成這個潛在表示，條件輸入是一個預訓練圖片編碼器的多層特徵，同時保留語意上下文與精細的空間細節。
- 潛在表示解碼後，輸出可重新打光的 PBR 高斯，並可選擇性地輸出一個帶有切線空間法線貼圖（tangent-space normal map）的貼圖網格（textured mesh）。

換言之，流程是：單張圖片 → 預訓練編碼器多層特徵 → rectified-flow transformer 生成潛在表示 → VAE 解碼 → 可重新打光的 PBR 高斯與選用的貼圖網格。

📊 **在 Toys4K 上刷新 FID，AI 生成圖片基準也領先**

在 Toys4K 資料集上，Luce 在單圖生成 3D 的任務上達到當前最佳（state-of-the-art）表現，FID 較最強基準線改善 28%。研究團隊另外建立了一個以 AI 生成圖片為輸入的新基準，在這個基準上，Luce 的 CLIP 圖像對齊分數為 0.8519，優於最佳基準線的 0.8299。論文也指出，Luce 生成的資產在保留文字、標誌與刻痕等精細細節上，同時兼顧幾何準確性與材質真實性。

🎯 **實務啟示**

對做 3D 內容生成或資產管線的工程師而言，Luce 的價值不只是「生成得更像」，而是輸出格式直接對齊了 PBR 渲染管線所需的材質模態，理論上可以省去額外的材質估計或手動貼圖步驟，更容易接入現有的遊戲或渲染引擎工作流程。

🔗 **來源**
- 標題：Luce: Relightable Gaussians for 3D Asset Generation
- 作者／機構：Mayank Singh、Michele Stoppa、Alvise Memo、Rui Yu、Sree Harsha Kalli、Srimanth Gunturi、Muhammad Ahmed Riaz、Behrooz Shahsavari、Waleed Abdulla、David E. Jacobs（Apple ML）
- 連結：https://machinelearning.apple.com/research/relightable-gaussians-3d-generation

#AppleML #3DGaussianSplatting #Image2 3D #PBR #Relighting #ComputerVision #GenerativeAI #RectifiedFlow #3DGeneration #NeuralRendering
