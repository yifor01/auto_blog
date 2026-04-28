---
title: "The Chameleon's Limit: Investigating Persona Collapse and Homogenization in Large Language Models"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.24698
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:06:44.879431
---

📌 【CMU/MIT等最新研究】LLM多智能体模拟现人格崩解

你给每个AI智能体设了独一无二的人设，模拟结果却全变成同一种行为？
最新研究反直觉结论：人设保真度越高，种群反而越刻板。

🤔 **多智能體模擬需多樣性，人格崩解卻普遍存在**
基于LLM的应用如多智能体模拟、角色扮演、社会模拟，都需要不同agent之间具备足够的种群多样性，才能支撑有效的模拟结果。但研究团队识别出一种普遍存在的失效模式「人格崩解（Persona Collapse）」：即使每个agent被分配到完全不同的人设，最终仍会收敛到狭窄的行为模式，产出同质化的模拟种群，完全失去预设的多样性。

🧪 **三維評估框架，10款LLM測3類任務**
为量化人格崩解的程度，研究团队提出包含3个核心指标的评估框架：
1. 覆蓋度（Coverage）：衡量模拟种群占据的人格空间比例；
2. 均勻度（Uniformity）：衡量agent在人格空间中的分布均匀程度；
3. 複雜度（Complexity）：衡量最终生成的行为模式丰富度。
团队使用上述框架评估
