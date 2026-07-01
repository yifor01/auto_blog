---
title: Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention
  in Vision-Language-Action Models
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.19297
score: 85
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:43:38.042958'
---

📌 VLA 模型真的懂常識嗎？Act2Answer 透過「肢體動作」測試世界知識

TL;DR：新提出的 Act2Answer 評估協議，要求 VLA 模型透過物理動作回答問題，以衡量其常識與世界知識的保留程度。

當我們在討論 Vision-Language-Action (VLA) 模型時，通常關注的是它能否成功抓取物體或執行指令。但一個核心問題被忽略了：這些模型在學習如何「行動」的過程中，是否還記得基本的常識與世界知識？

🤔 **行動與知識的脫節問題**

目前的 VLA 模型旨在將視覺感知與動作輸出結合，但研究者提出一個質疑：模型在執行具身任務時，其內在的知識保留（Knowledge Retention）與泛化能力究竟如何？單純地觀察動作是否成功，無法得知模型是否真正理解背後的語義。

🧩 **Act2Answer：用「動作」來回答問題**

為了量化這一點，研究者提出了 Act2Answer 評估協議。其核心邏輯不再是讓模型輸出文字，而是要求代理人（Agent）透過「物理動作」來回答問題。

這種方法將知識檢索轉化為具身行動，藉此揭露模型在不同語義類別（Semantic Categories）下的知識保留模式與泛化表現。

🎯 **實務啟示**

對於開發 Embodied AI 的工程師而言，這提醒我們在評估 VLA 模型時，不能僅依賴成功率（Success Rate）這類表層指標。透過設計如 Act2Answer 這種將「知識檢索」與「物理動作」繫結的測試，能更精準地診斷模型是「真的懂常識」還是僅僅是「模仿動作序列」。

🔗 **來源**
- 標題：Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models
- 連結：https://huggingface.co/papers/2606.19297

#VLA #EmbodiedAI #VisionLanguageAction #Robotics #CommonsenseKnowledge #Act2Answer #MachineLearning #WorldKnowledge #AI #Evaluation
