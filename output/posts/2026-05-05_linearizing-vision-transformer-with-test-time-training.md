---
title: "Linearizing Vision Transformer with Test-Time Training"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.02772
score: 122
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:38:55.393749
---

📌 【清華大學最新研究】TTT 實現 ViT 線性化權重繼承

🎣 **折疊區優化 (The Hook)**
線性化 Vision Transformer 從此不用從頭燒錢訓練。
清華大學團隊找到權重繼承的關鍵路徑，僅需 1 小時微調，就能讓 Stable Diffusion 3.5 推理速度提升近 1.5 倍，生成質量不打折扣。

🤔 **線性注意力可解二次瓶頸，權重繼承長期受阻**
Softmax 注意力機制的二次計算複雜度，一直是 Vision Transformer（ViT）與大型生成模型推理效率的核心瓶頸，線性複雜度注意力被視為極具潛力的替代方案。但這類線性模型若從頭訓練，計算成本過高；直接繼承預訓練 Transformer 的權重是更高效的路徑，但 Softmax 與線性注意力之間存在本質的表示鴻溝，過去始終無法實現有效的權重轉移。

🧪 **雙對齊策略結合 TTT 架構，實測 SD3.5 線性化**
本研究從架構對齊與表示對齊兩個維度解決上述轉換難題：
1. 架構對齊：團隊發現測試時訓練（Test-Time Training, TTT）作為一種線性複雜度架構，其兩層動態公式在結構上與 Softmax 注意力對齊，可直接繼承預訓練的注意力權重。
2. 表示對齊：為補齊關鍵平移不變性與局部性特徵，團隊引入鍵實例歸一化（key instance normalization）與輕量局部性增強模組。
驗證階段選擇對 Stable Diffusion 3.5 進行線性化改造，推出 SD3.5-T^5（Transformer To Test Time Training）模型。

 **1 小時微調，推理快 1.47 倍，效果持平**
實驗結果顯示：
- 僅需 4 張 H20 GPU 微調 1 小時，SD3.5-T^5 的文生圖質量與微調後的 Softmax 基線模型相當
- 1K 分辨率下推理速度提升 1.32 倍，2K 分辨率下提升 1.47 倍
- 成功實現預訓練權重的直接復用，大幅降低線性化 ViT 的訓練成本

💡 **TTT 結構對齊是權重繼承的核心關鍵**
過去線性注意力架構與 Softmax 注意力的結構差異過大，導致預訓練權重無法直接遷移，而 TTT 的兩層動態設計恰好匹配 Softmax 注意力的結構特性，是本次權重繼承能夠成立的基礎。搭配表示對齊的兩個輔助模組，補齊了 Softmax 注意力的核心表示特性，因此僅需少量微調就能達到與基線相當的生成效果。

⚠️ **目前公開資訊未提及明確研究限制**
根據目前提供的論文摘要與公開資訊，尚未明確提及本研究的研究限制說明，後續可關注完整論文釋出後的詳細實驗與討論內容。

🎯 **生成模型推理優化成本大幅降低**
這項技術解決了線性注意力架構長期以來的權重繼承痛點，對於需要部署 ViT、擴散模型（如 Stable Diffusion 系列）的團隊而言，無需投入大量資源從頭訓練線性模型，僅需少量微調即可獲得最高 1.47 倍的推理加速，尤其適合高分辨率文生圖、邊緣端部署等對推理效率要求高的場景，具備明確的產業應用價值。

🔗 **論文連結**
📝 論文標題：Linearizing Vision Transformer with Test-Time Training
👤 作者：Yining Li, Dongchen Han, Zeyu Liu, Hanyi Wang, Yulin Wang @ Tsinghua University
📍 來源：Computer Vision and Pattern Recognition (CVPR) 透過 ChatPaper
🔗 論文連結：https://arxiv.org/abs/2605.02772

你認為這項技術最適合應用在哪個場景？歡迎留言討論 👇

#AI #ComputerVision #VisionTransformer #線性注意力 #推理加速 #StableDiffusion #清華大學 #機器學習 #大模型部署
