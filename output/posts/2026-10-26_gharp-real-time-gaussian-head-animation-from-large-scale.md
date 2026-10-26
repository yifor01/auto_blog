---
title: 'GHARP: Real-Time Gaussian Head Animation from Large-Scale Reconstruction Prior'
source: Apple ML
url: https://machinelearning.apple.com/research/gharp-head-animation
model: claude-code/sonnet
generated_at: '2026-10-26T21:49:49.662542'
score: 86
---

📌 【Apple ML】即時3D頭像動畫，速度快13倍的秘密

TL;DR：Apple 提出 GHARP，把頭部身份重建與表情動畫拆成兩階段，在 Ava-256 基準上跑出 SOTA 品質且快 13 倍。

要讓一張人臉在幾張照片的基礎上，即時跟著表情訊號動起來，而且品質還要夠好到能上線，這件事一直卡在「品質」與「即時運算」之間難以兩全。Apple ML 在 ACCV 2026 發表的 GHARP，試圖把這道取捨拆解開來。

🤔 **即時頭像動畫的核心難題**

表情驅動的虛擬頭像方法有一個共通問題：表情碼（expression code）只描述臉部，不包含身體姿勢與衣著位置，導致這些區域在輸入資訊中是「欠規格」的。這會讓動畫網路面對一個病態（ill-posed）的映射問題，只能對衝突的身體樣貌做平均，結果就是模糊與時間上的閃爍（flicker）。

🧩 **兩階段架構：身份離線建模，動畫即時推論**

GHARP 把問題拆成兩個階段：

- 身份階段（Identity stage）：離線建立受試者的幾何與外觀表示，可以承受較高運算成本。
- 動畫階段（Animation stage）：在身份表示之上，即時預測「表情相關的殘差」（expression-dependent residuals），使用輕量化網路，針對行動裝置最佳化。

動畫運算發生在一個預訓練重建模型的「語意結構化潛在空間」（semantically structured latent space）中，表情變化在這個空間裡保持空間上的局部性，使殘差預測更有效率。這個重建先驗（reconstruction prior）也提供一致的空間佈局，讓多個輸入視角可以融合成一個固定大小、緊湊的 canonical Gaussian 表示。

為了解決前述身體與衣著欠規格的問題，團隊額外設計了一個「身體對齊網路」（body alignment network），學習把目標影像中人物的身體對齊到輸入的參考影像，從訓練訊號中移除這個歧義來源。

📊 **Ava-256 基準上的結果**

論文宣稱 GHARP 在 Ava-256 基準上達到 state-of-the-art 的品質，同時在 A100 GPU 上運算速度最高快 13 倍，且使用的 Gaussian 數量少了 8 倍。

⚠️ **論文揭露的侷限**

即便經過兩階段設計優化了運算與品質的取捨，論文指出 GHARP 仍繼承了所有表情驅動頭像方法共通的問題：表情碼無法涵蓋身體與衣著資訊，這部分僅靠身體對齊網路緩解，而非從根本解決。

🎯 **實務啟示**

對做即時虛擬人像或 AR/VR 應用的工程師，GHARP 提出的「離線身份建模＋輕量線上殘差推論」架構，是在行動裝置上追求即時表情驅動動畫時值得參考的設計思路；而身體對齊網路處理欠規格輸入的做法，也提示了在設計表情驅動系統時，不能只盯著臉部訊號，身體與場景一致性同樣是品質瓶頸。

🔗 **來源**
- 標題：GHARP: Real-Time Gaussian Head Animation from Large-Scale Reconstruction Prior
- 作者／機構：Ali Benlalah, Sepehr Johari, Patricia Vitoria, Armin Kappeler 等（Apple ML，ACCV 2026）
- 連結：https://machinelearning.apple.com/research/gharp-head-animation

#AppleML #ComputerVision #GaussianSplatting #3DAvatar #RealTimeRendering #FacialAnimation #ACCV2026 #NeuralRendering #AR #ComputerGraphics
