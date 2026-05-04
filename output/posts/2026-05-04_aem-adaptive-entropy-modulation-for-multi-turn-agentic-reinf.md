---
title: "AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.00425
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-05-04T19:59:22.368419
---

📌 【百度/清华/复旦 联合研究】AEM优化多轮Agent RL训练

多轮Agent RL训练还在靠堆过程奖励模型（PRM）解决信用分配问题？最新研究提出完全无监督的替代方案，在SWE-bench-Verified上比SOTA基线再涨1.4个百分点。

🤔 **稀疏奖励卡住Agent RL训练，现有方案成本高、泛化差**
大型语言模型（LLM）作为Agent通过强化学习（RL）与环境交互、完成多轮任务的能力近年提升显著，但训练效率仍受困于稀疏的最终结果奖励：仅依靠任务是否完成的结果信号，很难对Agent行动轨迹中的单个步骤分配对应功劳（信用分配问题）。
当前主流解法是引入密集中间监督，例如过程奖励模型（PRM）或辅助自监督信号，但这类方案需要额外增加监督成本与调参复杂度，且往往跨任务、跨域的泛化能力较差。

🧪 **无监督自适应熵调节，response级分析降方差**
本研究提出的AEM（Adaptive Entropy Modulation，自适应熵调节）是一种完全无监督的信用分配方法，不需要任何额外的中间监督信号，核心思路是在RL训练过程中自适应调节熵动态，实现更高效的探索与利用平衡。
理论层面，团队将熵分析从传统的token级提升到response（完整响应/轨迹）级，降低token采样的方差；同时证明在自然梯度下，熵漂移本质上由优势函数与相对响应惊喜度（surprisal，信息论中衡量响应与模型预期分布差异的指标）的乘积决定，据此推导出实用的代理指标，可自然引导训练从探索阶段过渡到利用阶段。

💡 **1.5B到32B模型全适用，SWE-bench-Verified涨1.4%**
实验覆盖多个基准测试与1.5B到32B参数规模的模型，充分验证AEM的有效性。其中在极具挑战性的软件工程Agent基准SWE-bench-Verified上，整合AEM后的当前最优（SOTA）基线模型性能提升1.4个百分点，且无需付出任何额外监督成本。

🔍 **跳过密集监督，靠熵动态平衡探索利用**
传统Agent RL训练要么受困于稀疏奖励的信用分配难题，要么付出高昂监督成本换取密集信号。AEM的创新在于完全不需要人工或模型标注的中间监督，仅通过调节response级的熵动态，就能自动完成从探索（尝试多样路径）到利用（锁定高奖励路径）的过渡，从根源上降低token级采样的波动，让每一步的信用分配更准确。
该方法也为Agent RL的训练范式提供了新思路：不需要依赖任务特定的密集奖励设计，仅通过优化训练过程中的熵动态，就能实现跨模型尺度、跨任务的稳定效果提升。

⚠️ **现有公开资讯未提及具体研究限制**
本次基于的论文摘要未披露实验局限性说明，已知信息仅确认其实验覆盖1.5B到32B多尺度模型、多基准验证，后续可关注完整论文发布后的细节补充。

🎯 **跨尺度适用，降低Agent RL训练门槛**
对于从事Agent RL研究与工程的从业者，AEM提供了一种零额外监督成本的信用分配方案，覆盖从边缘端小模型（1.5B）到云端大模型（32B）的训练场景，不需要调整现有奖励体系，仅需在训练过程中加入熵动态调节模块，即可提升训练效率与稳定性。
尤其适合需要频繁跨任务、跨域迁移的Agent训练场景，避免了PRM等方案的任务绑定问题，大幅降低训练适配成本。

🔗 **论文链接**
📝 论文标题：AEM: Adaptive Entropy Modulation for Multi-Turn Agentic Reinforcement Learning
👤 作者：Haotian Zhao, Yuxin Zhang, Songlin Zhou, Stephen S. -T. Yau, Wenyu Zhang（百度、清华大学、复旦大学）
🔗 论文地址：https://arxiv.org/abs/2605.00425
📎 来源：ChatPaper/AI

#AI #强化学习 #Agent #LLM #百度 #清华大学 #复旦大学 #SWEbench #机器学习 #AgentRL
