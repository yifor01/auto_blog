---
title: "AcademiClaw: When Students Set Challenges for AI Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.02661
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-05-05T20:04:01.318636
---

📌 【上海交大等】学术Agent评测集AcademiClaw

你以为前沿AI Agent已能胜任大学生作业、竞赛与科研项目了？
最新评测给出答案：即便是表现最好的模型，在真实学术任务上的通过率也仅55%。
这些任务全部来自学生真实学术工作流，且是现有Agent无法有效解决的。

🤔 **现有Agent评测偏助手场景，学术级能力空白**
OpenClaw生态下的现有benchmark仅聚焦助手级任务，Agent在真实学术场景的能力长期未被系统检验。随着Agent向复杂长程任务演进，覆盖作业、研究、竞赛的学术场景是高价值落地方向，但此前缺乏对应标准化评测工具，难以精准衡量模型实际能力。

🧪 **80道学生亲测双语难题，覆盖25+专业领域**
研究团队从230份学生提交的候选任务中，经专家评审筛选出80道双语复杂长程任务，全部来自学生真实学术工作流（作业、研究项目、竞赛、个人项目），且均为学生验证现有Agent无法有效解决的题目。任务覆盖25+专业领域，从奥数、语言学问题，到GPU密集型强化学习、全栈系统调试，其中16道需CUDA GPU环境执行。所有任务在隔离Docker沙箱运行，采用结合6种互补技术的多维度评分标准，同时配套独立五类安全审计进行行为分析。评测对象为6个前沿大模型。

🔍 **前沿模型最高通过率仅55%，能力边界清晰**
评测结果显示，即便是表现最优的前沿模型，整体通过率也仅为55%，远未覆盖真实学术场景需求。进一步分析发现，模型在不同任务域的能力边界差异显著，同时不同模型的行为策略存在明显分歧，且token消耗与输出质量无直接相关性，这些细粒度信号比单一聚合指标更具诊断价值。

💡 **细粒度评测诊断Agent能力短板**
与传统benchmark仅输出通过率等聚合指标不同，AcademiClaw通过多维度评分、安全审计、行为策略分析，可定位模型在具体任务类型、执行流程中的能力短板。其设计呼应近期社群对Agent推理与长程任务能力的关注，为理解模型复杂任务执行逻辑提供了可落地的分析框架。

⚠️ **公开资料未提及明确研究限制**
目前公开的论文摘要与介绍资料中，未明确列出本研究的设计局限与边界条件，相关细节可参考后续发布的完整论文版本。

🎯 **开源评测集可直接用于Agent调校**
AcademiClaw已开源全部80道双语任务、Docker沙箱执行框架与评分代码，工程团队可直接用于评测自研Agent在学术场景的能力，快速定位优化方向。对于Agent研究者，其细粒度诊断信号可帮助明确模型长程规划、跨领域任务执行的能力边界，加速学术级Agent的研发迭代。

🔗 **論文連結**
📝 來源：ChatPaper/AI；論文標題：AcademiClaw: When Students Set Challenges for AI Agents
👤 作者：Junjie Yu, Pengrui Lu, Weiye Si, Hongliang Lu, Jiabao Wu @ Shanghai Jiao Tong University; SII; GAIR
🔗 論文：https://arxiv.org/abs/2605.02661
💻 開源代碼：https://github.com/GAIR-NLP/AcademiClaw

你曾用AI Agent處理過學術相關任務嗎？遇到過哪些現有Agent無法解決的問題？歡迎留言分享你的經驗 👇

#AI #Agent #機器學習 #學術評測 #上海交通大學 #GAIR #OpenClaw #人工智慧 #長程任務 #AI研究
