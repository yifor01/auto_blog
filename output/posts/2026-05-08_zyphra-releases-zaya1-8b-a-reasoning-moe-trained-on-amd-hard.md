---
title: "Zyphra Releases ZAYA1-8B: A Reasoning MoE Trained on AMD Hardware That Punches Far Above Its Weight Class"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/06/zyphra-releases-zaya1-8b-a-reasoning-moe-trained-on-amd-hardware-that-punches-far-above-its-weight-class/
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:35:46.113834
---

📌 【Zyphra 新发布】8B MoE 小参数推理越级

用AMD硬件训练、激活参数仅760M的小模型，推理性能居然超过了Claude 4.5 Sonnet、GPT-5-High？
总参数8.4B的MoE架构，在HMMT’25数学测试中获得89.6分，高于Claude 4.5的88.3分。
模型已开源，Apache 2.0协议可直接部署，甚至支持端侧运行。

🤔 **密集模型参数效率瓶颈，MoE架构成小模型破局关键**
当前主流密集语言模型在推理时会激活所有参数，算力与内存带宽成本高企。而Mixture of Experts（MoE，混合专家）架构仅会在推理时激活部分「专家」参数，有望用更低的资源实现接近大模型的性能。但小参数MoE的推理能力能否对标前沿大模型，一直是行业验证的重点。Zyphra本次发布的ZAYA1-8B，正是这一方向的最新成果。

🧪 **全AMD集群训练，MoE++架构+Markovian RSA方法**
ZAYA1-8B基于Zyphra自研的MoE++架构，相比标准MoE设计有三项特定改进，核心设计目标是「智能效率」——即最大化每参数、每FLOP提取的模型能力。模型从预训练、中期训练到监督微调，全流程运行在AMD Instinct MI300集群上，是端到端AMD硬件训练的推理模型。同时引入了全新的test-time compute（测试时计算）方法Markovian RSA，进一步优化推理表现。

 **760M激活参数，数学推理超越Claude 4.5**
ZAYA1-8B总参数8.4B，但每次前向传播仅激活760M参数，在多项数学与编程基准测试中，表现超过数倍于自身大小的开源权重模型。在挑战性数学推理任务中，其分数与DeepSeek-R1-0528、Gemini-2.5-Pro、Claude 4.5 Sonnet等第一代前沿推理模型相当；搭配Markovian RSA方法后，在HMMT’25测试中取得89.6分，超过Claude 4.5 Sonnet的88.3分，也高于GPT-5-High，仅略逊于DeepSeek-V3.2等前沿开源模型。

 **架构与推理双优化，实现参数效率最大化**
ZAYA1-8B的性能优势来自两方面：一是MoE++架构的基础优化，在同等参数规模下提升模型表征能力；二是Markovian RSA测试时计算方法，在推理阶段动态分配计算资源，进一步强化复杂任务的推理表现。由于仅激活760M参数，其推理所需的算力与内存带宽远低于同性能密集模型，也保留了8.4B总参数带来的表征容量。

⚠️ **公開資訊未提及具體研究限制**
本次Zyphra公开的模型信息中，未披露具体的研究局限、测试任务的覆盖范围、以及其他场景下的性能表现。现有信息仅涵盖基准测试结果、训练配置与部署特性，后续若有完整技术报告发布，可进一步补充评估。

🎯 **小参数高效率，端侧与低成本推理首选**
对于需要本地部署、低延迟推理的场景，ZAYA1-8B是非常实用的选择：760M激活参数意味着它可以在端侧设备运行，适配本地LLM应用；同性能下
