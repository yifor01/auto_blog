---
title: "Meta AI Releases NeuralBench: A Unified Open-Source Framework to Benchmark NeuroAI Models Across 36 EEG Tasks and 94 Datasets"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/07/meta-ai-releases-neuralbench-a-unified-open-source-framework-to-benchmark-neuroai-models-across-36-eeg-tasks-and-94-datasets/
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-08T20:29:46.738123
---

📌 【Meta AI 开源】NeuralBench 脑电统一基准框架

NeuroAI 领域的模型评估，长期处於混乱状态。
不同团队用不同数据、不同任务，宣称的“通用性”根本没法验证。
Meta AI 最新开源的 NeuralBench，终于给出了统一标准。

🤔 **NeuroAI 评估碎片化，模型通用性宣称缺乏依据**
神经AI（NeuroAI，深度学习与神经科学交叉领域）近年快速发展，原本用于语言、语音、图像的自监督学习技术，正被适配用于构建脑基础模型：即在无标签脑信号记录上预训练，再微调用于临床癫痫检测、视听觉解码等下游任务。
但领域内的评估长期处於碎片化状态：不同研究团队使用不同的预处理流程、训练数据集，仅报告少量任务的结果，根本无法横向对比模型性能。现有基准如 MOABB 虽覆盖 148 个脑机接口（BCI）数据集，却仅支持 5 个下游任务；EEG-Bench、EEG-FM-Bench、AdaBrain-Bench 等基准也各有局限；脑磁图（MEG）、功能性磁共振成像（fMRI）等模态甚至完全没有系统基准。这也导致不少研究宣称脑基础模型“通用”“基础”，实则是挑选有利任务的结果，缺乏共同参考点。

🧪 **覆盖94数据集、36任务、1.3万小时EEG数据**
Meta AI 团队发布 NeuralBench，这是首个统一开源的 NeuroAI 模型基准框架。其首个版本 NeuralBench-EEG v1.0 是目前规模最大的开放脑电图（EEG）基准，核心参数包括：
- 36 个下游任务、94 个公开数据集
- 覆盖 9478 名受试者、累计 13603 小时 EEG 数据
- 单一标准化接口下评估 14 种主流深度学习架构
框架基于三个核心 Python 包构建模块化管线：已披露的两个组件分别为 NeuralFetch，负责从 OpenNeuro、DANDI、NEMAR 等公共仓库拉取策展后的脑电数据；NeuralSet 负责数据准备流程。

💡 **首个大规模标准化EEG基准，填补评估缺口**
NeuralBench-EEG v1.0 解决了 NeuroAI 领域长期缺乏统一评估标准的问题，所有模型可在同一预处理流程、同一数据集、同一任务集下公平对比，此前被滥用为营销话术的“通用”“基础”宣称，终于有了可验证的共同参考点。
其任务覆盖广度远超现有基准：对比 MOABB 仅支持 5 个下游任务，NeuralBench 的 36 个任务可更全面地验证模型的泛化能力。

💡 **模块化开源设计，降低NeuroAI研究门槛**
NeuralBench 的模块化设计大幅降低了研究者的重复劳动：无需再手动收集、清洗不同来源的数据集，无需搭建自定义预处理流程，可直接基于框架快速复现已有结果、对比不同模型性能。
对于从事脑基础模型、脑机接口应用的工程师而言，这套框架可大幅缩短评估周期，加速模型迭代优化。

⚠️ **目前仅覆盖EEG模态，其他脑信号基准仍缺失**
目前 NeuralBench 仅发布 EEG 模态的首个版本，脑磁图（MEG）、功能性磁共振成像（fMRI）等其他脑信号模态尚未纳入，暂无对应系统评估标准。后续还需扩展更多模态、更多任务的覆盖，才能完全满足 NeuroAI 领域的评估需求。

🎯 **标准化基准助力脑基础模型迭代优化**
- 从事 NeuroAI 研究的团队可直接使用 NeuralBench 作为统一评估工具，避免重复造轮子
- 开源模块化设计支持自定义扩展，可按需添加私有数据集、专属任务
- 对比基准结果可更客观地验证模型性能，避免“挑任务”式的结果宣称

🔗 **相關連結**
📝 報導標題：Meta AI Releases NeuralBench: A Unified Open-Source Framework to Benchmark NeuroAI Models Across 36 EEG Tasks and 94 Datasets
👤 報導作者：Asif Razzaq @ MarkTechPost
🔗 報導連結：https://www.marktechpost.com/2026/05/07/meta-ai-releases-neuralbench-a-unified-open-source-framework-to-benchmark-neuroai-models-across-36-eeg-tasks-and-94-datasets/

你所在的团队有遇到 NeuroAI 模型评估的痛点吗？欢迎在评论区分享你的经验 👇

#MetaAI #NeuralBench #NeuroAI #脑机接口 #BCI #深度学习 #开源框架 #AI基准 #脑电图
