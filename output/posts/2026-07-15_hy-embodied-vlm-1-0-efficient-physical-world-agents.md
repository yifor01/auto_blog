---
title: 'Hy-Embodied-VLM-1.0: Efficient Physical-World Agents'
source: arXiv
url: http://arxiv.org/abs/2607.12894v1
score: 90
model: tencent/hy3:free
generated_at: '2026-07-15T08:22:29.602914'
---

📌 Hy-Embodied-VLM-1.0：3B 高效具身代理

TL;DR：具身 VLM 僅啟用 3B 參數，38 項基準超越同級，適合低延遲部署。

🎣 **3B 啟用參數竟能逼近 32B 具身模型**
打造能真正在物理世界行動的 AI，不只是看懂影像就行。新模型 Hy-Embodied-VLM-1.0 僅用 3B 啟用參數，效能卻逼近前代 32B 啟用參數的規格，為具身代理帶來新可能。

🤔 **具身代理需要感知與行動推理並重**
報告指出，建構能力強的 embodied agents（具身代理）不只需要多模態感知與理解，還必須具備代理能力（agentic capabilities）：對行動進行推理、適應動態情況、與物理世界互動。為從預訓練階段就培養這些能力，作者定義了一個以行動為中心的能力分類法（action-centric capability taxonomy），包含三個漸進維度：Action-Relevant State Understanding（與行動相關的狀態理解）、Action-Transition Reasoning（行動轉換推理）、Sequential and Adaptive Reasoning（序列與適應性推理）。

🧩 **行動導向資料管線與 MoE 架構設計**
依據上述分類法，團隊開發了系統化資料管線（systematic data pipeline），並策展橫跨預訓練與後訓練（post-training）的資料混合（data mixtures）。模型本身建立在 Hy3-A3B 語言主幹（language backbone）與 Hy-ViT2 視覺編碼器（vision encoder）之上；其高效的 Mixture-of-Experts (MoE) 架構結合了強大的模型容量與高推論效率（inference efficiency），在支援延遲敏感部署的同時，提供紮實的物理世界理解與互動能力。

📊 **38 項基準中 19 項同級最佳，平均提升 8.4%**
評估涵蓋具身感知、物理世界理解與具身推理的綜合套件共 38 個基準。關鍵結果整理如下：

| 模型 | 啟用參數 | 關鍵表現 |
| --- | --- | --- |
| Hy-Embodied-VLM-1.0 | 3B | 19/38 基準同尺寸最佳；平均較前代 +8.4% |
| Hy-Embodied-0.5 MoT-2B (前代) | 32B | 平均低 8.4%，效能被逼近 |
| Qwen3.6-A3B | 未提及 | 大幅落後 |
| Cosmos 3 | 未提及 | 大幅落後 |

除了靜態基準，該模型在多輪互動（multi-turn interaction）與長程推理（long-horizon reasoning）的具身代理任務上也展現強勁表現。

🎯 **低延遲部署的具身 AI 新選擇**
對工程師而言，此模型證明了「小啟用參數 + 精心設計的資料與架構」能在物理世界任務逼近大模型，適合邊緣或延遲敏感場景。若實際專案需要具身推理與互動，可持續關注其後續釋出的部署資源。

🔗 **來源**
- 標題：Hy-Embodied-VLM-1.0: Efficient Physical-World Agents
- 作者／機構：Ziyi Wang, Xumin Yu, Yongming Rao, Yonggen Ling, Yunheng Li
- 連結：http://arxiv.org/abs/2607.12894v1

#EmbodiedAI #VLM #MixtureOfExperts #Robotics #PhysicalWorld #AgenticAI #EfficientModel #Benchmark #Reasoning #HyEmbeddedVLM
