---
title: "BAMI: Training-Free Bias Mitigation in GUI Grounding"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.06664
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:15:22.451207
---

📌 【清华×联想】免训练GUI定位去偏方法BAMI

GUI智能体复杂界面点不准？不用重训就能解决。
现有优化要么堆数据要么调模型，成本高适配难。
新研究找到误差根源：分辨率和元素复杂度惹的祸。

🤔 **GUI智能体落地难，复杂界面定位是核心瓶颈**

GUI grounding 是支撑 GUI 智能体执行点击、拖拽等任务的核心能力，但在 ScreenSpot-Pro 这类复杂场景基准中，现有模型的表现始终不尽理想，成为可靠 GUI 智能体落地的关键阻碍。

🧪 **MPD归因定位误差，多模型验证效果**

研究团队首先提出掩码预测分布（Masked Prediction Distribution, MPD）归因方法，系统分析现有模型的误差来源，明确两大核心偏差：高图像分辨率导致的精度偏差（precision bias）、复杂界面元素导致的模糊偏差（ambiguity bias）。随后提出免训练的 BAMI 方法，并通过多款 GUI 定位模型、ScreenSpot-Pro 基准测试与消融实验验证效果。

 **TianXi-Action-7B精度从51.9%升至57.8%**

实验结果显示，BAMI 作为免训练方法，可显著提升各类 GUI 定位模型的准确率：应用于 TianXi-Action-7B 模型时，其在 ScreenSpot-Pro 基准的准确率从 51.9% 提升至 57.8%，涨幅达 5.9%。消融实验进一步验证，BAMI 在不同参数配置下均保持鲁棒性，效果稳定。

💡 **双操作针对性解决两类定位偏差**

BAMI 全称为 Bias-Aware Manipulation Inference（偏差感知操作推理），核心包含两个针对性操作：一是粗到细聚焦（coarse-to-fine focus），解决高分辨率带来的精度偏差；二是候选选择（candidate selection），缓解复杂界面元素带来的模糊偏差。这种方法无需重新训练模型，直接适配各类已有 GUI 定位模型，部署成本极低。该方法核心思路基于现有归因与操作技术，但针对 GUI 智能体的特定场景做了定制化设计，新颖性值得关注。

⚠️ **公开摘要未提及明确研究限制**

本次整理基于论文公开摘要与第三方评分信息，未提及作者明确说明的研究局限，若后续获取全文细节将同步更新。

🎯 **免训练即插即用，开源代码可直接复用**

对于 GUI 智能体相关的工程师与研究者，BAMI 提供了一条低成本的性能优化路径：无需重新训练模型，可直接将方法适配到现有 GUI 定位模型中，且官方已开源完整实现代码，可快速验证效果。该方法针对当前可靠 GUI 智能体的热点需求，实用性较强。

🔗 **論文連結**
📝 標題：BAMI: Training-Free Bias Mitigation in GUI Grounding
👤 作者：Borui Zhang, Bo Zhang, Bo Wang, Wenzhao Zheng, Yuhao Cheng（清華大學、聯想研究院）
📚 來源：ChatPaper / Computer Vision and Pattern Recognition
🔗 論文：https://arxiv.org/abs/2605.06664
💻 開源代碼：https://github.com/Neur-IO/BAMI

你在开发GUI智能体时遇到过定位不准的问题吗？欢迎在评论区分享经验👇

#GUI #AI #计算机视觉 #清華大學 #聯想研究 #開源 #機器學習 #GUI智能體
