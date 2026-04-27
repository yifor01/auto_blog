---
title: "Contexts are Never Long Enough: Structured Reasoning for Scalable Question Answering over Long Document Sets"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.22294
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-04-27T19:42:59.880503
---

📌 【Stanford 最新研究】结构化推理突破长文档QA瓶颈

你以为长文档QA只要适配LLM上下文窗口就够？
最新研究显示，就算所有基线都符合强LLM的窗口要求，新方法仍平均超GPT-4.1达6.6分。
在3600万token的超长文档集上，更是比第二名高出32分。

🤔 **固定上下文窗口与聚合瓶颈，卡死长文档QA落地**
真实世界的文档问答需要分析师跨多份文档、以及单份文档的不同部分，综合证据给出答案。但LLM的固定上下文窗口，会随着文档集的增长被轻易突破。
业界的常见解法是把文档拆分成块（chunk），再从每个块的输出中组装答案，但这种方法存在致命的聚合瓶颈：当块的数量增长时，系统仍需要组合、推理体量越来越大的提取证据，最终还是会碰到上下文限制或推理效率瓶颈。

🧪 **SLIDERS双核心：结构化存储与数据调和机制**
斯坦福大学团队提出的SLIDERS框架，核心设计围绕两个关键组件：
1. 结构化推理层：将文档中的关键信息提取到关系型数据库，通过SQL查询实现可扩展推理，完全替代传统的文本拼接方案，依托持久化结构化状态处理海量信息，不受文本长度限制。
2. 数据调和相关阶段：为解决局部块提取带来的全局不一致问题，SLIDERS利用信息出处（provenance）、提取理由（extraction rationales）和元数据，自动检测并修复重复、不一致、不完整的记录，保证全局信息的连贯性。

💡 **超GPT-4.1 6.6分，3600万token场景领先32分**
SLIDERS在基准测试中展现了显著优势：
- 在三个现有长上下文基准（所有对比基线都适配强基础LLM的上下文窗口）中，SLIDERS超过所有基线，平均得分比GPT-4
