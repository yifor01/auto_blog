---
title: "Beyond Static Best-of-N: Bayesian List-wise Alignment for LLM-based Recommendation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.04559
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-05-07T21:03:05.561572
---

📌 贝叶斯动态对齐LLM推荐系统

LLM推荐系统用Best-of-N调优效果好但算不起？现有BoN对齐方案看似解决了部署成本问题，却悄悄丢失排序信号，还越训练信号越弱。

🤔 **LLM推荐系统的列表级优化陷入两难**
LLM驱动推荐系统（LLM4Rec）近年依托大语言模型的生成能力，在建模复杂用户偏好上表现突出，但现有方法大多采用token级优化目标（如下一个token预测），难以直接优化NDCG、公平性、多样性等不可微的列表级核心指标，而这些才是衡量推荐质量的真正标准。
推理时直接搜索的Best-of-N（BoN）方法可以优化这类指标，但每次推理需生成N个候选并排序，计算成本极高，无法落地部署。后续的BoN对齐方法试图将BoN的搜索能力蒸馏到模型内部，避免推理时的额外计算，但现有方案存在两个
