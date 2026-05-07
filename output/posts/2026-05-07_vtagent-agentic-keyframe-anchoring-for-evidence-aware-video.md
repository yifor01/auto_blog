---
title: "VTAgent: Agentic Keyframe Anchoring for Evidence-Aware Video TextVQA"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.04870
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-05-07T20:42:04.657989
---

📌 【武汉大学新研究】关键帧锚定优化视频文字问答

你以为Video-LLM做不好视频文字问答是推理能力不足？最新研究实测发现，只要能定位到问题对应的关键帧，单帧的回答正确率远高于直接输入整段视频推理的结果。

🤔 **Video-LLM视频文字问答瓶颈不在推理**
视频文字视觉问答（Video TextVQA）需要模型根据视频中出现的视觉文字内容进行推理回答。尽管近期Video-LLM已具备较强的多模态视频理解能力，但其在现有Video TextVQA基准上的表现仍远不及预期。

🧪 **上界分析定位瓶颈，问题引导Agent验证**
研究团队首先通过帧级问答完成上界分析：对样本进行逐帧问答，只要任意一帧能输出正确答案即判定该样本正确，结果显示该上界表现显著优于直接视频推理，明确核心瓶颈在于问题相关关键证据的定位，而非模型推理能力本身。
基于这一结论，团队提出VTAgent框架，即问题引导的Agent架构，在生成回答前先显式锚定与问题相关的关键帧，该框架无需额外训练即可运行，后续进一步通过监督微调（SFT）与强化学习（RL）优化性能。

📊 **训练免费即优于直接推理，SFT+RL提分超12%**
- 训练免费（training-free）版本的VTAgent，表现稳定超过直接视频推理的结果
- 叠加监督微调（SFT）与强化学习（RL）后，在多个基准上平均准确率提升+12.12，ANLS指标提升+11.15，刷新该领域最优（SOTA）成绩
- 研究证实，显式关键帧锚定是推动Video TextVQA发展的核心要素

💡 **关键帧定位是跳出模型缩放的新优化路径**
过往Video TextVQA的优化多聚焦模型规模扩张、推理能力增强，本研究通过上界分析明确了被忽略的核心瓶颈，跳出纯模型缩放的研究思路，为领域提供了新的优化方向，对从事多模态视频QA的工程师具有高实用参考价值。

⚠️ **公开资讯未提及具体限制，代码将开源**
目前公开的论文摘要未明确说明研究的具体局限性，仅确认相关代码将公开释放。

🎯 **多模态视频QA优先优化关键帧定位**
- 针对Video TextVQA任务，优化关键帧定位的收益远高于单纯扩大模型规模
- 训练免费的VTAgent框架可直接复用，无需额外训练即可获得更优效果
- 后续可叠加SFT/RL进一步提升性能，代码开源后可快速落地验证

🔗 **論文連結**
📝 論文標題：VTAgent: Agentic Keyframe Anchoring for Evidence-Aware Video TextVQA
👤 作者：Haibin He, Maoyuan Ye, Jing Zhang, Juhua Liu, Bo Du（武汉大学）
📚 來源：arXiv (Computer Vision and Pattern Recognition)
🔗 論文連結：https://arxiv.org/abs/2605.04870
💻 代碼：論文提及將公開釋出

你認為多模態視頻問答的下一個優化重點是什麼？歡迎留言分享你的觀點 👇

#AI #ComputerVision #VideoLLM #多模態 #武漢大學 #VideoTextVQA #機器學習 #CVPR
