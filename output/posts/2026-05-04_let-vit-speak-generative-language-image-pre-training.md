---
title: "Let ViT Speak: Generative Language-Image Pre-training"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.00809
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:10:56.749121
---

```
📌 【字节跳动等提出GenLIP】ViT直预测语言token对齐MLLM

做多模态视觉编码器对齐还在用对比学习、加文本解码器？
最新研究反其道而行：让ViT直接用语言建模目标预测语言token，
无需对比批次构建、无需额外模块，用更少数据跑赢强基线。

🤔 **现有ViT对齐MLLM方案复杂，GenLIP提供极简新路径**
当前多模态大语言模型（MLLMs）需要将视觉编码器（ViT）与LLM的自回归生成特性对齐，主流方案要么依赖对比学习的批次构建，要么额外叠加文本解码器，流程复杂且扩展受限。这篇由北京交通大学、字节跳动、南洋理工大学团队提交的GenLIP，正是针对该痛点的极简生成式预训练框架，目标是为ViT对齐MLLM提供更简洁、可扩展的新路径。

🧪 **80亿样本预训练，支持原生长宽比多分辨率优化**
GenLIP的核心设计极简：训练ViT通过标准语言建模目标，直接从视觉token预测语言token，仅用单一Transformer联合建模视觉与文本token，完全去掉对比学习的批次构建流程，也无需额外文本解码器。预训练阶段使用Recap-DataComp-1B数据集的80亿样本，后续支持多分辨率、原生长宽比图像的持续预训练，适配不同粒度的视觉理解需求。

💡 **用更少预训练数据，性能持平或超越强基线**
实验结果显示，GenLIP在多个多模态基准上取得有竞争力或优于现有方法的结果，尽管使用的预训练数据量远少于对比的强基线，仍实现匹配或超越的性能。经过多分辨率原生长宽比图像持续预训练后，GenLIP在OCR、图表理解等细节敏感任务上的表现进一步提升，可作为MLLMs的高性能视觉编码器基础。
