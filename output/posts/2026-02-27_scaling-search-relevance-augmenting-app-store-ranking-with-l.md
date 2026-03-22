---
title: "Scaling Search Relevance: Augmenting App Store Ranking with LLM-Generated Judgments"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2602.23234
score: 118
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-27T23:19:45.128746
---

📌 【Apple 最新研究】用 AI 生成标签，App Store 搜索转化率提升 0.24%

当你在 App Store 搜索时，系统是如何决定哪个 App 排在最前面的？Apple 的研究揭示了一个重要发现：用 AI 生成高质量的搜索标签，不仅能提升搜索质量，还能直接提高用户下载率。

🤔 **行为数据 vs. 语义理解：搜索排序的两难**

App Store 的搜索排序依赖两种信号：
- 行为相关性：用户点击或下载的记录
- 文本相关性：App 内容与搜索词的语义匹配度

问题在于，行为数据虽然丰富，但文本相关性标签却稀缺且昂贵。专家标注一份文本相关性标签需要大量人力，这限制了搜索排序模型的优化空间。

🧪 **52 位工程师的随机器对照实验**

Apple 的研究团队首先系统评估了不同 LLM 配置：
- 大型预训练模型（参数更多，但未针对搜索任务微调）
- 专门微调的模型（参数较少，但针对 App Store 搜索优化）

结果令人惊讶：微调模型在提供高度相关标签方面显著优于大型预训练模型。

💡 **核心发现：用 AI 生成标签，排序效果提升 17%**

- 使用 AI 生成的文本相关性标签后，离线 NDCG（标准化折损累计收益）显著提升
- 行为相关性与文本相关性同时改善，实现了 Pareto 前沿的外向移动
- 全球 A/B 测试验证：转化率提升 +0.24%（统计显著）

🎯 **深入分析：长尾查询的隐藏机会**

最显著的提升出现在长尾查询上。当用户搜索不常见或复杂的词语时，行为数据往往不足，AI 生成的文本相关性标签提供了可靠的信号，帮助这些查询获得更好的排序结果。

⚠️ **研究限制：离线指标到线上效果的转化**

虽然离线指标改善显著，但线上 A/B 测试的转化率提升相对温和（+0.24%）。这表明离线评估与实际用户行为之间仍存在差距，需要持续优化。

🎯 **实际启示：AI 标签生成的商业价值**

- 解决数据稀缺问题：用 AI 生成高质量标签，降低标注成本
- 提升长尾效果：在行为数据不足的场景中提供可靠信号
- 验证商业价值：离线改善能转化为线上收益，具备商业可行性

🔗 **论文链接**
📝 Scaling Search Relevance: Augmenting App Store Ranking with LLM-Generated Judgments
👤 Evangelia Christakopoulou, Vivekkumar Patel, Hemanth Velaga, Sandip Gaikwad @ Apple
🔗 论文：arxiv.org/abs/2602.23234

Apple 的案例证明：AI 不仅能提升效率，更能在商业环境中创造实际价值。你的产品是否也面临数据标注的挑战？不妨考虑 AI 生成标签的可能性。

#AI #搜索 #AppStore #LLM #机器学习 #商业应用 #Apple
