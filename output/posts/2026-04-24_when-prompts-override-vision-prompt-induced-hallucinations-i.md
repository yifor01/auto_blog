---
title: "When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.21911
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-04-24T19:48:44.869168
---

📌 【索邦大学×Valeo.ai 研究】提示词诱导LVLM幻觉与解法

你以為提示詞越詳細，LVLM的輸出就越精準？最新研究發現，文本指令中自帶的先驗資訊，反而會讓模型忽略視覺輸入，產生與圖片完全無關的幻覺。

🤔 **LVLM幻觉归因不明，文本先驗影響被低估**
大型視覺語言模型（LVLM，Large Vision-Language Models，兼具視覺理解與文本生成能力的多模態模型）落地面臨的核心痛點之一是幻覺問題，即模型輸出內容與輸入的視覺資訊不匹配。過去研究將幻覺歸因於視覺骨幹（Vision Backbone）的特徵提取限制，或是語言組件的主導性過強，但兩類因素的相對重要性始終沒有明確結論，產業界也缺乏針對性的優化方向。

🧪 **構建HalluScope基準，量化不同幻覺誘因**
來自索邦大學ISIR實驗室與Valeo.ai的研究團隊提出HalluScope基準測試，專門用於區分不同因素誘發的LVLM幻覺，量化視覺限制、語言主導、文本先驗等不同變量對幻覺的影響程度，解決過去歸因模糊的問題。

 **文本指令先驗是幻覺首要誘因**
透過HalluScope的分析結果顯示，LVLM的幻覺絕大部分並非來自視覺編碼器能力不足，也不是語言模型組件本身過於強勢，而是源於對文本先驗與背景知識的過度依賴，其中用戶輸入的文本指令引入的資訊，是誘發幻覺的核心因素。當提示詞中包含與圖片無關的先驗描述時，模型會傾向直接採用文本資訊，忽略視覺輸入。

💡 **偏好優化讓模型回歸視覺依據**
針對提示詞誘導的幻覺問題，團隊提出HalluVL-DPO微調框架，可直接對現成的LVLM進行優化，無需修改模型原有結構。該框架採用偏好優化（Preference Optimization）思路，其中DPO（Direct Preference Optimization，直接偏好優化）是高效的實現方式，基於專門構建的訓練數據集，讓模型學習區分「基於視覺輸入的可靠回答」與「文本先驗誘導的幻覺回答」，引導模型優先依賴視覺資訊生成輸出。實驗
