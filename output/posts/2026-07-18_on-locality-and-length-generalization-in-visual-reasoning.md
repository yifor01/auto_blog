---
title: On Locality and Length Generalization in Visual Reasoning
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.09061
score: 87
model: tencent/hy3:free
generated_at: '2026-07-18T07:37:26.625934'
---

📌 【視覺推理研究】局部感知如何讓模型真正學會舉一反三？

TL;DR：實驗顯示局部 recurrent 視覺策略能緩解長度泛化失敗，全域性捷徑是元兇。

人類看東西靠一系列局部 foveated 注視（glimpse），而不是一次看完整張圖。但現在主流電腦視覺模型幾乎都是單次、全域性輸入影像——這不只是生物學上的差異，可能還藏著運算上的根本代價。

🤔 **全域性視覺模型與人類視覺的根本差異**

人類視覺系統透過一系列局部的 foveated glimpses 攝取視覺資訊，而非單次全域性運算。這與當前大多數電腦視覺模型截然不同：後者通常將整張影像一次性全域性輸入。一個自然的提問是，局部、序列式的視覺模型除了在生物學上更合理外，是否還能帶來根本的運算優勢。

🧩 **從語言模型長度泛化借鏡，設計視覺狀態追蹤實驗**

作者從近期語言模型（language models）的 length generalization 研究獲得靈感，從視覺狀態追蹤（visual state tracking）與長度泛化角度切入。他們訓練視覺模型處理簡單視覺任務，這些任務需要在影像中聚合跨位置的局部資訊，用以觀察模型在任務長度或複雜度變化時的行為。

📊 **全域性捷徑讓視覺模型在長度上翻車，局部策略能救**

實驗揭露：類似語言模型的現象，視覺模型會學到利用全域性捷徑（global shortcuts），導致在任務長度或複雜度增加時無法泛化。另一方面，基於嚴格局部感知（strictly local perception）的 recurrent vision policies 能緩解這類失敗，使模型在這些任務上成功泛化。

💡 **局部 attention 可能是被忽略的穩健組合泛化要件**

研究結果指出，local attention 或許是一個被忽視的關鍵需求，對於實現穩健的 compositional generalization（組合泛化）而言可能是必要條件。

🎯 **實務啟示**

若你在設計需要處理可變長度或複雜度視覺輸入的系統，與其堆疊全域性 attention，不妨評估引入嚴格局部感知加 recurrent 結構的可行性——這可能比單純放大模型更能換來真正的長度泛化能力。

🔗 **來源**
- 標題：On Locality and Length Generalization in Visual Reasoning
- 連結：https://huggingface.co/papers/2607.09061

#VisualReasoning #LengthGeneralization #LocalAttention #ComputerVision #CompositionalGeneralization #RecurrentModels #VisionModels #StateTracking #ShortcutLearning #HF Papers
