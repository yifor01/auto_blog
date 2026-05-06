---
title: "Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.04018
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-06T20:37:05.110930
---

📌 【Yale NLP Lab等】推理密集型检索评估训练新框架

你训练的检索器在静态基准刷到SOTA，实际用在Agent里却不好用？
问题大概率出在评估方式上。
现有主流基准只测单篇相关性，完全忽略了Agent最需要的能力。

🤔 **推理密集型检索需互补证据，现有评估训练双缺失**
推理密集型检索的核心目标是找出支撑下游推理的证据，而非仅匹配主题相似度，这对需要多轮迭代搜索、信息合成的Agentic搜索系统至关重要。当前该领域存在两大核心痛点：评估端，以BRIGHT为代表的现有基准金标集范围窄，且仅孤立评估检索器性能，无法反映实际多轮搜索场景的表现；训练端，主流合成语料库往往优化单段落相关性，而非多证据组合的构建能力，导致训练出的检索器无法适配Agentic场景需求。

🧪 **专家标注基准+方面分解合成语料+LoRA微调**
本研究从评估与训练两方面提出解决方案：
1. 提出BRIGHT-Pro专家标注基准：为每个查询扩展多维度金标证据，同时支持静态检索、Agentic搜索两种评估协议，更贴合实际应用场景。
2. 构建RTriever-Synth合成语料：采用方面分解设计，可生成互补正例与基于正例的难负例，针对性优化检索器的多证据检索能力。
3. 基于Qwen3-Embedding-4B，使用RTriever-Synth语料通过LoRA微调得到RTriever-4B模型。

 **方面感知评估暴露标准指标隐藏行为**
实验覆盖词法检索器、通用检索器、推理密集型检索器三大类模型，得到两项核心结论：
第一，采用方面感知的评估方式、Agentic搜索协议，能够暴露标准静态指标无法发现的行为差异，更精准反映检索器的实际能力。
第二，基于RTriever-Synth微调的RTriever-4B，性能大幅优于其基础模型Qwen3-Embedding-4B，验证了所提训练方案的有效性。

💡 **多证据组合能力是Agentic检索核心**
现有静态基准的设计逻辑停留在“单查询-单相关文档”的匹配范式，无法衡量检索器提供互补证据、支撑多轮推理的能力。本研究的创新点正在于跳出单段落相关性的优化目标，将评估与训练的重心转向多维度证据的构建与组合，让检索器的能力更贴合Agentic系统多轮搜索、迭代合成的实际需求。

⚠️ **公开资料未提及明确研究限制**
目前提供的论文摘要与公开资料中，未明确说明本研究的主要局限，后续可关注论文全文披露的细节。

🎯 **新基准与合成语料可直接用于检索器优化**
对于从事RAG、Agentic搜索、检索器研发的工程师与研究者，可直接使用BRIGHT-Pro基准评估检索器的多证据检索能力，使用RTriever-Synth合成语料训练适配Agentic场景的检索模型。现有通用检索器若需适配推理密集型任务，可参考方面分解、互补正例构建的训练思路，针对性优化模型表现。

🔗 **论文連結**
📝 论文标题：Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems
👤 作者：Yilun Zhao, Jinbiao Wei, Tingyu Song, Siyue Zhang, Chen Zhao
🏫 机构：Yale NLP Lab; National University of Singapore; NYU Shanghai; RTriever
🔗 论文链接：https://arxiv.org/abs/2605.04018

你在开发RAG或Agent系统时，是否遇到过检索器静态评估高分但实际效果差的问题？欢迎在评论区分享你的经验 👇

#NLP #信息检索 #AgenticSearch #RAG #YaleNLP #RTriever #机器学习 #人工智能 #推理检索
