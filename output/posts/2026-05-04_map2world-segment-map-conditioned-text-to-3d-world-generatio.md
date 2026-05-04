---
title: "Map2World: Segment Map Conditioned Text to 3D World Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.00781
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:21:56.070582
---

📌 【微软亚研院×首尔大学】分割图条件3D世界生成

做3D世界生成的开发者，是不是常遇到两个头疼问题？
布局被固定网格绑死，没法自定义任意形状。
物体尺度全局不一致，调起来费时费力。

🤔 **现有3D生成受网格限制，尺度一致性不足**
3D世界生成是沉浸式内容创作、自动驾驶仿真等场景的核心技术，近年相关研究已取得不少进展。但现有方法普遍存在两大痛点：一是生成布局受预设网格限制，灵活性不足；二是整个场景中的物体尺度容易出现不一致问题，影响落地效果。

🧪 **任意形状分割图条件，兼顾细节与全局一致**
针对上述问题，研究团队提出全新框架Map2World，核心设计包含三点：
1. 首次支持以用户自定义的任意形状、任意尺度的分割图（segment map）作为生成条件，从输入层保证全局尺度一致，支持超大规模场景的灵活生成。
2. 提出专用细节增强网络（detail enhancer network），通过融入全局结构信息，在生成世界细粒度细节的同时，不破坏整体场景连贯性。
3. 整个生成管线复用资产生成器（asset generators）的强先验知识，即使在场景生成训练数据有限的场景下，也能实现跨域的鲁棒泛化。

💡 **可控性、尺度一致、连贯性均优于现有方法**
研究团队通过大量实验验证，Map2World在用户可控性、尺度一致性、内容连贯性三大核心指标上，均显著优于现有主流3D世界生成方法，支持用户在更复杂的条件下完成3D世界生成。

⚠️ **公开摘要未提及具体研究限制**
本次公开的论文摘要未披露具体研究限制与不足，若需了解完整实验边界与局限性，可参考arxiv上的完整论文版本。

🎯 **沉浸式内容与自动驾驶仿真可直接落地**
对于GenAI工程师与研究者，Map2World的条件控制逻辑、细节增强网络设计、资产生成器先验复用思路，对3D生成管线设计具有直接参考价值。其解决的尺度一致性、可控性痛点，可快速落地于沉浸式内容创作、自动驾驶仿真等实际场景。

🔗 **論文連結**
📝 Map2World: Segment Map Conditioned Text to 3D World Generation
👤 Jaeyoung Chung, Suyoung Lee, Jianfeng Xiang, Jiaolong Yang, Kyoung Mu Lee
🏫 Seoul National University; Microsoft Research Asia
📚 領域：Computer Vision and Pattern Recognition (CVPR)
🔗 論文：https://arxiv.org/abs/2605.00781

做3D生成的你，遇到过尺度不一致的問題嗎？歡迎留言分享你的經驗👇

#3D生成 #计算机视觉 #CVPR #微软亚研院 #首尔大学 #GenAI #自动驾驶仿真 #沉浸式内容 #AI研究
