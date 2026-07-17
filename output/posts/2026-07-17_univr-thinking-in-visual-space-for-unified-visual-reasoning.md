---
title: 'UniVR: Thinking in Visual Space for Unified Visual Reasoning'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.12800
score: 110
model: tencent/hy3:free
generated_at: '2026-07-17T08:05:00.700923'
---

📌 【HuggingFace Daily Papers】UniVR：在純視覺空間中統合推理與規劃

TL;DR：UniVR 從原始視覺示範學推理與規劃，VR-X 基準最高提升 25% 且全開源。

當多數模型依賴圖文配對來學習常識，UniVR 反其道而行：只給原始視覺資料，不給文字標註，模型卻能學會複雜推理、細微物理動態與長期規劃。這挑戰了我們對「智慧如何從感知中誕生」的既定假設。

🤔 **從原始視覺資料直接學世界知識**

論文指出，從原始視覺資料直接學習廣泛世界知識是智慧的一項基礎能力。UniVR 是首個嘗試同時從純視覺示範（pure visual demonstrations）中學習複雜推理、細粒度物理動態（fine-grained physical dynamics）與長期規劃（long-term planning）的研究。

🧩 **VR-GRPO：全域性與步級獎勵互補的強化學習範式**

UniVR 的核心方法是 VR-GRPO，一種具備互補的全域性獎勵（global rewards）與步級獎勵（step-level rewards）的 reinforcement learning 範式。README／摘要指出，這種設計能在不依賴任務特定啟發式（task-specific heuristics）或 image-text pairs 的情況下，於整個推理過程中強制邏輯連貫性與物理一致性。

📊 **VR-X 大規模基準與最高 25% 的改進**

為了訓練與評估，作者建構了 VR-X：一個從 16 個多元來源整理而成的大規模基準，涵蓋長程操作（long-horizon manipulation）、空間謎題（spatial puzzles）與物理推理（physical reasoning）。摘要宣稱這是首個在純視覺協定下評估上述異質能力的綜合套件。

實驗結果方面，UniVR 在 VR-X 上最高達到 25% 的改進幅度；且其優異的視覺推理能力也提升了多項 multimodal understanding 基準的表現。

🎯 **開源資源降低純視覺推理研究門檻**

作者將所有 code、data 與 models 開源，供後續研究使用。對工程師而言，這代表不需從零搭建訓練框架與基準，即可基於 UniVR 與 VR-X 進行純視覺推理方向的實驗或擴充。

🔗 **來源**
- 標題：UniVR: Thinking in Visual Space for Unified Visual Reasoning
- 連結：https://huggingface.co/papers/2607.12800

#VisualReasoning #UniVR #VRGRPO #ReinforcementLearning #PureVisualLearning #VRX #Multimodal #PhysicalReasoning #LongTermPlanning #OpenSource
