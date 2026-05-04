---
title: "AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.00539
score: 104
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:38:05.874058
---

📌 【哈工大&华为】AGoQ 突破4bit激活训练瓶颈

训练LLM想用量化省内存，却总遇到收敛慢、精度掉的坑？
过去4bit激活+8bit梯度的量化方案，根本没法用在实际训练中。
哈工大&华为的AGoQ，终于把这个瓶颈破了。

🤔 **量化省内存，但4bit激活+8bit梯度一直有收敛瓶颈**
LLM分布式训练的内存与通信开销一直是产业痛点，量化技术通过降低参数、激活、梯度的存储精度节省内存，是主流优化方向。但现有量化方案处理4bit激活、8bit梯度时，极易出现收敛慢、精度下降的问题，始终无法落地到大规模训练场景。
当前8B到32B中大规模LLM的训练需求持续增长，分布式训练的资源门槛居高不下，突破低精度量化的收敛瓶颈，对降低训练成本有重要价值。

🧪 **8B-32B LLaMA+64GPU集群验证**
AGoQ提出两项核心技术：一是层感知激活量化算法，根据不同层的类型、流水线并行（pipeline）阶段，为激活分配适配的bit宽度，整体实现接近4bit的激活存储；二是梯度量化算法，采用8bit梯度存储，搭配精度保留的8bit All-Reduce通信，同时降低内存占用与跨节点通信时间。
实验覆盖8B、32B规格的LLaMA模型，在两个GPU集群（最多64张GPU）完成测试，对比基线包括主流训练框架Megatron-LM（含/不含ZeRO优化）、COAT、DeepSpeed。

📊 **内存最多减52%，训练提速1.34倍，精度持平**
实验结果显示，相较于上述SOTA训练系统，AGoQ最多可降低52%的GPU内存占用，训练速度最高提升1.34倍。同时预训练阶段收敛损失与基线一致，下游任务推理精度与同架构LLaMA基线模型相当，未出现精度下降问题。

💡 **层感知分配bit宽+精度保留All-Reduce是核心**
过去4bit激活量化效果不佳，核心原因是不同层、不同训练阶段的激活对量化误差的敏感度差异极大，统一采用低bit宽必然导致关键层精度损失。AGoQ的层感知方案针对性分配bit宽，在整体低存储的前提下保住关键层精度，解决了收敛难题。
梯度量化的8bit All-Reduce设计，避免了通信过程中转回高精度带来的额外开销，同时保留梯度精度，进一步降低通信延迟与内存占用。

⚠️ **实验仅覆盖8B-32B LLaMA与64GPU内集群**
现有公开实验结果仅针对8B至32B的LLaMA架构模型，在最多64张GPU的集群环境中验证，更大参数规模（如70B及以上）的模型、其他主流架构的适配效果尚未披露，相关场景的表现有待进一步验证。

🎯 **分布式训练可尝试AGoQ降低内存开销**
对于从事LLM分布式训练的工程师与研究者，AGoQ的方案在不损失精度的前提下，可大幅降低训练资源门槛，尤其适合算力有限的训练场景。该方案对比均为工业界主流训练框架，兼容性与落地性较强，且具备开源实现潜力与产业应用前景。

🔗 **論文連結**
📝 论文标题：AGoQ: Activation and Gradient Quantization for Memory-Efficient Distributed Training of LLMs
👤 作者单位：哈尔滨工业大学（深圳）计算机科学与技术学院、华为技术有限公司
👤 作者：Wenxiang Lin, Juntao Huang, Luhan Zhang, Laili Li, Xiang Bao
🔗 论文链接：https://arxiv.org/abs/2605.00539

#AI #LLM #大模型训练 #分布式训练 #量化技术 #哈工大 #华为 #AGoQ #机器学习
