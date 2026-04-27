---
title: "Context-Fidelity Boosting: Enhancing Faithful Generation through Watermark-Inspired Decoding"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.22335
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-04-27T20:13:43.287464
---

📌 【腾讯混元】水印解码提升LLM忠实度

提升 LLM 上下文忠實度，不用重訓模型、不用改架構，甚至不用加 RAG？
這項研究把水印技術的思路用到了解碼階段，輕量到可以直接落地。

🤔 **LLM 忠实性幻觉普遍，现有解法成本偏高**
大型语言模型（LLM）生成内容时，常出现与输入上下文矛盾、或忽略上下文信息的问题，被称为「忠实性幻觉」。例如基于给定文档做摘要时编造未提及的信息，基于参考材料回答问题时无视材料内容自行生成答案，这类问题严重阻碍LLM在Agent、医疗、法律等需高事实一致性场景的落地。现有解决方案多依赖模型微调、RAG检索增强或架构修改，普遍存在成本高、通用性差的痛点。

🧪 **受水印启发的解码框架，无需重训改架构**
腾讯混元AI数字人团队联合McGill大学、Mila、武汉大学、清华大学等机构的研究者，提出Context-Fidelity Boosting（CFB）轻量化解码阶段框架。其核心思路源自水印技术的logit-shaping（对数几率调整）原理：水印技术通过给特定token增加logit偏置嵌入隐式标记，CFB则针对「有输入上下文支持的token」增加logit偏置，提升其生成概率，从而减少幻觉生成。CFB无需重新训练模型，也无需修改模型架构，可兼容各类开源LLM。
研究提出三种递进的偏置策略：静态提升对支持token加固定偏置；上下文感知提升通过对比有无上下文下的next-token分布散度，动态缩放偏置；
