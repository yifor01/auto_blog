---
title: "WebGen-R1: Incentivizing Large Language Models to Generate Functional and Aesthetic Websites with Reinforcement Learning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.20398
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-04-23T19:29:22.126071
---

📌 【港科大x阿里等】RL 训练小模型生成多页高质网站

你以为生成可部署、带美感的多页网站，必须用几百B超大模型？
7B小模型经RL训练后，功能成功率追平671B DeepSeek-R1。
其在有效渲染、美感对齐度上，还大幅超过这款671B模型。

🤔 **项目级网站生成仍是LLM的未解难题**
大语言模型擅长函数级代码生成，但生成功能完整、视觉美观的多页网站这类项目级任务，至今仍是行业挑战。当前主流方案存在明显短板：要么仅支持单页静态网站，要么依赖多轮执行的Agent框架搭配专有模型，伴随高昂的token成本、高延迟与脆弱的集成问题。

🧪 **Scaffold驱动生成+级联多模态奖励设计**
该研究提出的WebGen-R1是面向项目级网站生成的端到端强化学习框架，核心解决小模型RL训练中的奖励设计瓶颈。具体设计包含两点：一是scaffold（脚手架）驱动的结构化生成范式，约束网站生成的大开放动作空间，保障整体架构完整性；二是新型级联多模态奖励（结合多维度评估的奖励机制），将结构保证、执行层面的功能反馈、基于视觉的美感监督三者结合，解决了网站生成中难以用单一指标验证的问题（不同于单文件代码可通过单元测试验证，网站需同时评估主观美感、跨页交互与功能正确性）。

💡 **7B小模型追平671B超大模型，美感反超**
实验结果显示，WebGen-R1将原本几乎生成不了可用网站的7B基础模型，转化为可输出可部署、美感对齐的多页网站的模型。性能表现有三个核心亮点：1. 持续优于参数量最高达72B的开源模型；2. 功能成功率与671B参数的DeepSeek-R1相当；3. 在有效渲染率、美感对齐度上大幅超过DeepSeek-R1。

🔍 **小模型端到端RL是项目级生成的低耗路径**
过往项目级网站生成要么依赖高参数大模型，要么采用多轮Agent框架搭配专有模型，部署成本极高。WebGen-R1验证了用强化学习端到端训练小模型，配合合理的生成约束与多模态奖励设计，完全可实现项目级生成能力，且成本远低于超大模型或专有Agent方案，为开源模型的落地应用提供了可参考的路径。

⚠️ **公开摘要未提及作者明确声明的研究限制**
目前提供的论文公开摘要未包含作者自述的研究侷限说明，若需了解完整实验限制、泛化性讨论等内容，可参阅论文全文。

🎯 **小模型+RL是高性价比网站生成的可行方向**
对于有网站生成能力落地需求的团队，无需盲目追求超大参数模型或昂贵的专有Agent方案，可参考WebGen-R1的设计思路：采用7B级别开源模型配合端到端RL训练，结合结构化生成约束与多模态奖励设计，即可实现高性价比的项目级网站生成能力，大幅降低部署与运营成本。

🔗 **论文链接**
📝 论文标题：WebGen-R1: Incentivizing Large Language Models to Generate Functional and Aesthetic Websites with Reinforcement Learning
👤 作者及机构：Juyong Jiang, Chenglin Cai, Chansung Park, Jiasi Shen, Sunghun Kim（所属：香港科技大学（广州）、香港科技大学、阿里通义实验室、韩国电子通信研究院、蚂蚁集团）
📚 来源：ChatPaper/Computation and Language
🔗 论文链接：https://arxiv.org/abs/2604.20398

你所在团队是否尝试过用LLM生成项目级代码？效果如何？欢迎分享经验👇

#AI #LLM #强化学习 #网站生成 #开源模型 #港科大 #阿里巴巴 #DeepSeek #技术落地 #代码生成
