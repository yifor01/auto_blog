---
title: 'DanceOPD: On-Policy Generative Field Distillation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.27377
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-28T19:25:10.253355'
---

📌 DanceOPD：用 On-Policy 蒸餾統一生成與編輯能力

TL;DR：提出 DanceOPD 框架，透過路徑路由與速度訓練，將生成、局部與全域編輯整合進 flow-matching 模型。

目前的生成模型往往在「從無到有的生成」與「對既有內容的精準編輯」之間存在鴻溝，要讓同一個模型同時精通 text-to-image 以及不同層級的編輯任務，通常需要複雜的權衡。

🧩 **透過路徑路由與速度訓練達成能力統一**

DanceOPD 提出了一套全新的 on-policy 生成場域蒸餾 (generative field distillation) 框架。其核心設計在於將 text-to-image 生成、局部編輯 (local editing) 與全域編輯 (global editing) 這三種能力整合在同一個 flow-matching 模型中。

為了達成這個目標，該框架採用了兩項關鍵技術：
1. Capability-specific routing：根據不同的任務需求，將資料引導至對應的能力路徑。
2. Velocity-based training：利用基於速度的訓練方式，最佳化模型在 flow-matching 過程中的生成品質與編輯精準度。

🎯 **實務啟示**

對於開發生成式 AI 的工程師而言，DanceOPD 的設計理念在於「能力的統一」。如果能將生成與編輯能力整合在同一個模型中，將能大幅降低維護多個專門模型（如一個負責生成、一個負責 Inpainting）的成本，並可能提升編輯時的整體一致性。

🔗 **來源**
- 標題：DanceOPD: On-Policy Generative Field Distillation
- 連結：https://huggingface.co/papers/2606.27377

#AI #GenerativeAI #FlowMatching #ImageGeneration #ImageEditing #Distillation #OnPolicy #ComputerVision #MachineLearning #DanceOPD
