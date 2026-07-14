---
title: 'ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.10350
score: 90
model: tencent/hy3:free
generated_at: '2026-07-14T08:02:52.059376'
---

📌 【新論文】ABot-AgentOS：透過多模態記憶與自演化機制，打造機器人通用的代理作業系統

TL;DR：ABot-AgentOS 提供通用的代理層，透過多模態圖形記憶與自演化機制，提升機器人長程任務的執行能力。

🎣 雖然現有的視覺語言模型（VLM）與視覺語言動作模型（VLA）已經大幅提升了機器人的感知與動作預測能力，但面對需要長時程（long-horizon）規劃的具身智慧任務時，機器人仍缺乏一個能處理推理、記憶、工具使用與驗證的通用執行層。

🤔 **機器人需要一個「大腦層」來協調底層控制**

目前的系統往往直接從感知跳到動作，但在複雜場景中，機器人需要一個位於底層控制器（low-level controllers）之上的代理層（agent layer），來負責以下關鍵功能：
- 場景條件下的規劃（scene-conditioned planning）
- 隔離背景知識的技能執行（context-isolated skill execution）
- 多階段驗證（multi-stage verification）
- 邊緣與雲端協作（edge-cloud collaboration）

🧩 **引入通用多模態圖形記憶（Universal Multi-modal Graph Memory）**

為了讓機器人擁有持久且可追蹤的記憶，ABot-AgentOS 提出了「通用多模態圖形記憶」，這是一個以來源為基礎的底層架構，能將以下資訊轉換為具備型別（typed）的節點與邊：
- 對話內容、視覺觀察、空間上下文、時間關係以及任務軌跡（task traces）。

💡 **透過失敗驅動的自演化機制實現持續進步**

為了避免機器人在訓練過程中發生「資料洩漏」（ground-truth leakage），ABot-AgentOS 採用了一種獨特的機制：
1. 將診斷出的記憶失敗（memory failures）轉換為執行時演化資產（runtime evo-assets）。
2. 這些資產僅會在後續的評估分割（evaluation splits）中被啟用。
3. 這種「失敗驅動」的迴圈讓系統能在不破壞評估嚴謹性的前提下，實現持續的自我演進。

📊 **在 Embodied WorldBench 表現優於單一控制器**

為了評估此類系統，研究者推出了 EmbodiedWorldBench，這是一個包含 16 種場景（涵蓋室內、室外及混合場景）、4 種難度等級，以及超過 200 個任務（包含導航、物件搜尋、NPC 對話、動態事件）的可執行基準測試。

在初步的實驗資料中，ABot-AgentOS 在任務成功率與目標完成率上均優於單一控制器的基準線（single-controller baseline）。在記憶基準測試中，其表現如下：

| 基準測試專案 | Static 版本分數 | 自演化後分數 |
| :--- | :--- | :--- |
| LoCoMo | 87.5 | 88.7 |
| OpenEQA | 59.9 | 60.4 |
| Mem-Gallery | 88.6 | 89.0 |
| NExT-QA | 76.5 (Acc@All) | — |

🎯 **實務啟示**

對於機器人工程師而言，ABot-AgentOS 的研究方向指出，未來的具身智慧（Embodied AI）可能不再僅僅是最佳化感知與動作的對映，建立一個具備「可審計記憶（auditable memory）」與「自演化能力」的作業系統層，將是實現長程複雜任務的關鍵。

🔗 **來源**
- 標題：ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory
- 連結：https://huggingface.co/papers/2607.10350

#Robotics #EmbodiedAI #AgentOS #MachineLearning #MultiModal #ComputerVision #ArtificialIntelligence #GraphMemory #SelfEvolution #AIResearch
