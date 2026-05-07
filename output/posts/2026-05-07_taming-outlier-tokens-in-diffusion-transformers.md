---
title: "Taming Outlier Tokens in Diffusion Transformers"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.05206
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:31:59.242977
---

📌 【Apple & 莱斯大学最新研究】DSR控制DiT异常Token提升生成质量

你训练的DiT生成质量总差一口气？问题可能出在不到1%的高范数Token上。
过去Vision Transformer的异常Token问题，在生成模型领域长期未被重视。
Apple与莱斯大学联合提出DSR方案，实测可稳定减少伪影、提升生成质量。

🤔 **ViT异常Token问题，在DiT生成模型中未被重视**
Vision Transformer（ViT）中出现的异常Token（outlier tokens，指少数范数极高、吸引过多注意力却携带极少局部信息的Token）现象已被学界确认，但这类现象在生成模型中的作用长期未被深入探索。当前主流的表征自编码器（RAE）-DiT生成管线，同时包含预训练ViT编码器与DiT解噪器，恰好是异常Token的高发场景，直接影响最终生成质量。

🧪 **同时检测编码器与解噪器的异常Token分布**
研究团队针对RAE-DiT管线的两个核心组件展开系统分析：一方面检测预训练ViT编码器的输出表征，另一方面追踪DiT解噪器各层的内部Token分布，重点观察高范数Token的出现位置与影响。实验覆盖ImageNet类别条件生成与大规模文本生成图像任务，全面验证干预方案的有效性。

 **单纯屏蔽高范数Token无效，根源是语义损坏**
研究首先明确：RAE-DiT的预训练ViT编码器会产生异常表征，DiT解噪器尤其是中间层，也会自发形成内部异常Token。但测试发现，单纯屏蔽高范数Token并不会提升生成质量，说明问题不止是极端数值的存在，更核心的是这些Token对应的局部图像块语义已经发生损坏。

💡 **双阶段寄存器干预，针对性修复两类异常**
团队提出Dual-Stage Registers（DSR，双阶段寄存器）方案，针对不同组件的异常问题设计对应干预策略：编码器端若有预训练寄存器则直接调用，否则采用递归测试时寄存器；解噪器端则部署专属的扩散寄存器。实验结果显示，该方案在ImageNet与大规模文生图任务中，均能稳定减少异常伪影，显著提升生成质量。

⚠️ **当前验证集中于RAE-DiT管线，其他架构待覆盖**
本研究的实验验证均围绕RAE-DiT管线展开，未提及在其他非RAE架构的DiT模型上的适配效果，相关泛化性仍有待后续验证。

🎯 **DiT管线可快速集成DSR，无需大幅改架构**
对于正在使用RAE-DiT管线的AI工程师，可尝试集成DSR方案：针对编码器与解噪器分别部署对应寄存器模块，无需大幅调整原有训练或推理流程，即可降低异常Token带来的伪影问题，提升生成质量。正如论文评审指出，这是一项可直接落地实验的实用技术，适合集成到现有DiT管线中。

🔗 **论文连结**
📝 论文标题：Taming Outlier Tokens in Diffusion Transformers
👤 作者：Xiaoyu Wu, Yifei Wang, Tsu-Jui Fu, Liang-Chieh Chen, Zhe Gan
🏫 机构：Rice University（莱斯大学）; Apple
🔗 论文链接：https://arxiv.org/abs/2605.05206

#AI #扩散模型 #DiT #计算机视觉 #Apple #莱斯大学 #生成式AI #机器学习
