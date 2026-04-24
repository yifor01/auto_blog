---
title: "DualSplat: Robust 3D Gaussian Splatting via Pseudo-Mask Bootstrapping from Reconstruction Failures"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.21631
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-04-24T19:27:47.832818
---

📌 DualSplat：用失败先验优化3DGS瞬态鲁棒性

3D Gaussian Splatting（3DGS）已是实时实景重建的首选方案，可实现每秒百帧级的光真实渲染。
但训练图像中若混入仅存在于部分视角的路人、车辆等瞬态物体，整体重建精度会直接雪崩。
更棘手的是，现有解决思路本身陷入了「先检测瞬态再重建，还是先重建再检测瞬态」的循环依赖死结。

🤔 **3DGS 受瞬态物体拖累，现有方法陷循环依赖死结**
3D Gaussian Splatting（3DGS）是2023年提出的显式3D重建技术，凭借实时高渲染质量的优势，快速成为产业界落地的主流方案。但3DGS的核心假设是所有训练图像符合多视图一致性，即同一静态场景在不同视角下的观测应当对齐。
实际落地场景中，训练数据往往包含瞬态物体（Transient Objects）：这类物体仅出现在部分训练视角中，比如街景中的行人、车辆，室内场景里临时摆放的杂物等，直接违反多视图一致性假设，导致3DGS的渲染质量大幅下降。
现有鲁
