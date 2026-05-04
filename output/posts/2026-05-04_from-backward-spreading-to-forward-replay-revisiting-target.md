---
title: "From Backward Spreading to Forward Replay: Revisiting Target Construction in LLM Parameter Editing"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.00358
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:17:19.322634
---

📌 【Google DeepMind 最新研究】革新LLM参数编辑目标构建

用了多年的LLM参数编辑核心方法，竟从未被系统研究过底层逻辑。
Google DeepMind团队提出全新替代路径，效果更优。
新方案计算量不变，层目标精度反而更高。

🤔 **向后扩散成默认方案，底层逻辑却从未被系统验证**
现有LLM参数编辑方法普遍采用向后扩散（backward spreading）思路：先在目标层（锚点）计算理想目标隐状态，再将该向量分配到多个前置层实现协作编辑。这一方案已沿用多年，但从未有人系统研究过其底层基础，能力边界、实践考量与潜在失效模式均不明确。

🧪 **先系统梳理传统方法
