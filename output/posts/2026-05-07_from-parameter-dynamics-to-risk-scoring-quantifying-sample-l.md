---
title: "From Parameter Dynamics to Risk Scoring : Quantifying Sample-Level Safety Degradation in LLM Fine-tuning"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.04572
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:40:51.331698
---

📌 【美国东北大学最新研究】量化LLM微调样本级安全风险

用完全良性的数据微调大语言模型，居然会悄悄抹掉它之前学的安全对齐能力。
更关键的是，现在终于能量化每个训练样本的风险高低了。

🤔 **安全退化机制不明，样本风险无法量化**
大语言模型的安全对齐极其脆弱，过往实验证实，仅用少量良性样本做微调，就能抹除模型从数百万条偏好样本中学习到的安全行为。现有研究大多通过对比微调前后的参数、隐藏状态来解释这一现象，但完全忽略了微调过程中参数的动态演化，既无法明确安全退化的核心机制，也没有办法逐样本评估微调风险。

🧪 **提出SQSD方法，量化样本级微调风险**
研究团队通过分析微调过程中的参数动态，发现良性微调会导致参数持续向危险对齐的方向累积漂移，最终削弱模型安全性，且对漂移贡献越大的样本，微调风险越高。基于此提出SQSD（Sample-Level Quantification of Safety Degradation，样本级安全退化量化）方法：具体通过计算单个训练样本引发的参数更新，在「危险方向」与「安全方向」上的投影差，得到每个样本的连续风险分数。

 **参数向危险漂移，SQSD可精准量化风险**
实验覆盖多个模型、多个数据集，结果证实SQSD能有效量化每个训练样本的微调风险。同时该方法具备强迁移性，可跨不同模型架构、参数规模、参数高效微调方法使用，无需针对特定场景重新训练。

 **兼具机制洞察与工程实用价值**
相较于现有仅对比微调前后静态参数的研究，该工作首次从动态视角解释安全退化机制，补全了领域研究空白。SQSD既提供了LLM安全退化的机制性洞察，也可直接供工程师用于审计微调数据集、提前识别高风险样本，兼顾学术价值与工程落地性。

⚠️ **公开信息未提及具体研究限制**
本次披露的论文摘要与评测信息中，未明确说明该研究的具体局限性，后续可关注论文全文的详细披露。

🎯 **可审计微调数据，提前识别高风险样本**
对于AI工程师与LLM运维团队，SQSD可直接用于微调前的训练数据集审计，逐样本计算风险分数，提前过滤高风险训练样本，避免安全退化。该方法的强迁移性也意味着无需针对每个模型单独开发风险评分工具，可大幅降低落地成本。

🔗 **论文連結**
📝 论文标题：From Parameter Dynamics to Risk Scoring : Quantifying Sample-Level Safety Degradation in LLM Fine-tuning
👤 作者：Xiao Wang, Yifei Zhang, YongKang Liu, Xiaocui Yang, Zihan Wang @ Northeastern University
📎 来源：ChatPaper/AI
🔗 论文链接：https://arxiv.org/abs/2605.04572

你在LLM微调过程中遇到过安全退化的问题吗？欢迎分享经验 👇

#LLM #大模型安全 #AI微调 #AI安全 #机器学习 #NLP #美国东北大学 #AI研究
