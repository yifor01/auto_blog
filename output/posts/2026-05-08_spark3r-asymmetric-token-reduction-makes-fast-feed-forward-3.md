---
title: "Spark3R: Asymmetric Token Reduction Makes Fast Feed-Forward 3D Reconstruction"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.06270
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:22:30.641874
---

📌 北大Spark3R：3D重建最高提速28倍

你以为加速3D重建只能无脑压缩所有token？
北大团队发现，query和key-value的功能差异决定压缩策略不能一刀切。
他们提出的Spark3R，最高实现28倍加速，还无需重新训练。

🤔 **前馈3D重建的长视频瓶颈：全局注意力二次方成本
