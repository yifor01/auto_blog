---
title: "Reading, Not Thinking: Understanding and Bridging the Modality Gap When Text Becomes Pixels in Multimodal LLMs"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2603.09095
score: 110
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-11T18:32:01.389129
---

📌 【HuggingFace 最新研究】為什麼 AI 看圖理解文字，總是輸給直接讀文字？

你有沒有發現，ChatGPT 看圖片裡的文字總是會「看走眼」？同樣一段文字，為什麼 AI 直接讀總是比看圖片裡的文字準？

🤔 **AI 看圖理解文字，總是輸給直接讀文字**

當我們給多模態模型看一張包含文字的圖片（比如截圖、書本掃描），它的表現往往不如直接讀取相同內容的文字。這就是所謂的「模態差距」（Modality Gap）——圖片裡的文字和文字本身，在 AI 眼中是不同的東西。

🧪 **自蒸餾技術，讓 AI 看圖像讀文字一樣準**

這篇論文提出了一種巧妙的解決方案：讓 AI 先用文字模式「想清楚答案」，再讓它用圖片模式「模仿這個思考過程」。透過這種自蒸餾（Self-Distillation）技術，模型學會了用圖片模式進行文字推理，有效縮小了模態差距。

💡 **關鍵洞察：讓圖片模式的 AI 學會「文字模式的思考方式」**

研究發現，當模型在圖片模式下能夠模仿文字模式的推理軌跡時，表現會有顯著提升。這意味著：問題不在於 AI「看不懂圖片」，而在於它沒有學會用適合圖片的策略來處理文字推理。

⚠️ **渲染品質影響表現，但自蒸餾技術有效緩解**

圖片的清晰度、文字的渲染品質都會影響 AI 的表現。但好消息是，自蒸餾技術能有效降低這些因素造成的表現差距，讓模型在各種圖片品質下都能有更穩定的表現。

🎯 **實務啟示：多模態模型的訓練策略值得重新思考**

- 對於需要處理大量圖片文字的應用，可以考慮加入自蒸餾訓練策略
- 圖片文字的預處理品質仍然重要，但不再是決定性的因素
- 未來的多模態模型設計，應該更重視不同模態之間的知識遷移

🔗 **論文連結**
📝 Reading, Not Thinking: Understanding and Bridging the Modality Gap When Text Becomes Pixels in Multimodal LLMs
🔗 論文：arxiv.org/abs/2603.09095

#AI #多模態 #MachineLearning #HuggingFace #文字識別 #圖像理解

你有用過哪些看圖片讀文字的 AI 工具？遇到過什麼有趣的失敗案例嗎？
