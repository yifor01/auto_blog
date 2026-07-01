---
title: 'DOPD: Dual On-policy Distillation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.30626
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:37:28.487103'
---

📌 DOPD：透過動態 Token 級路由，解決模型蒸餾中的「特權錯覺」

TL;DR：DOPD 透過動態路由 Token 級監督，改善 Large Model 與 VLM 的能力轉移效率。

在模型蒸餾（Distillation）過程中，學生模型往往試圖模仿老師模型的輸出，但如果老師模型擁有學生無法企及的「特權資訊」，這種強行模仿反而會導致所謂的「特權錯覺（Privilege Illusion）」，讓能力轉移的效果打折扣。

🤔 **解決 On-policy 蒸餾中的特權錯覺**

DOPD (Dual On-policy Distillation) 旨在解決 On-policy 蒸餾中的特權錯覺問題。其核心挑戰在於，當老師模型與學生模型在處理相同輸入時，若監督訊號過於僵化，學生模型可能無法有效吸收老師模型的真正能力，導致能力轉移（Capability Transfer）不完全。

🧩 **基於 Advantage Gap 與機率的動態路由**

為了最佳化能力轉移，DOPD 不再採取單一的監督方式，而是引入了一套動態路由機制：

- **Token 級監督**：在 Token 層級對監督訊號進行精細化控制。
- **動態路由邏輯**：系統會根據「優勢差距（Advantage Gaps）」以及「機率（Probabilities）」來決定目前的 Token 應該接收來自老師模型還是學生模型自身的監督訊號。
- **靈活切換**：透過這種動態路由，模型能更靈活地在老師的指導與自我探索之間取得平衡，從而提升學習效率。

💡 **適用於大型語言模型與視覺語言模型**

根據摘要指出，這種方法在 Large Models 以及視覺語言模型（Vision-Language Models, VLM）中均能有效提升能力轉移的品質，證明瞭該機制在不同模態模型上的通用性。

🎯 **實務啟示**

對於從事模型壓縮或蒸餾的工程師而言，DOPD 提醒我們：盲目地讓學生模型模仿老師的每一個 Token 可能並非最佳解。引入基於 Advantage 或機率的動態篩選機制，讓學生模型在「適當的時候」才參考老師的輸出，可能是提升蒸餾效能的關鍵方向。

🔗 **來源**
- 標題：DOPD: Dual On-policy Distillation
- 連結：https://huggingface.co/papers/2606.30626

#AI #MachineLearning #KnowledgeDistillation #LLM #VLM #DOPD #ModelCompression #OnPolicy #DeepLearning #CapabilityTransfer
