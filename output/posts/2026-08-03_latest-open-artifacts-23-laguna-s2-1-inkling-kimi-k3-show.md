---
title: 'Latest open artifacts (#23): Laguna S2.1, Inkling, & Kimi K3 show the utility
  of open models on the Pareto frontier'
source: Interconnects
url: https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21
model: tencent/hy3:free
generated_at: '2026-08-03T09:22:37.140776'
score: 61
---

📌 【產業觀察】開源模型進入決定性時代：多個強大 MoE 模型湧現帕累托前緣

TL;DR：隨著訓練成本攀升，開發者正轉向大規模 MoE 架構，開源模型正挑戰效能邊界。

隨著模型訓練成本逐年以數個數量級增長，業界曾預測模型開發將走向整合。然而現況顯示，越來越多公司投入數億甚至數十億美元訓練強大的模型，並釋出開源權重。隨著 Token 需求持續攀升，開源模型在生態系中的角色正進入關鍵的決定性時代。

🧩 **MoE 架構成為主流：從 Thinking Machines 到 Tencent**

目前的趨勢顯示，混合專家模型（MoE）已成為處理大規模參數與高效率需求的核心架構：

*   **Inkling (Thinking Machines)**：首款 975B-A41B 多模態 MoE 模型。它支援文字、圖像與音訊輸入，並輸出文字。雖然在同規模模型中未必是最強，但其設計目標是作為微調（fine-tuning）的強大基座，並透過其商業服務 Tinker 提供支援。此外還釋出了一個極具競爭力的 276B-A12B 版本。
*   **Hy3 (Tencent)**：一個 295B-A21B 的 MoE 模型。效能較前代全面提升，且授權方式從限制性授權轉為 Apache 2.0。值得注意的是，該模型能透過專用工具與 Sol 作為裁判，證明一個擁有 50 年歷史的數學問題。

🚀 **開源透明度與效能的競賽：Poolside 與 DeepSeek**

*   **Laguna S2.1 (Poolside)**：這款 118B-A8B 的 MoE 模型已連續三個月出現在技術追蹤中。它經過重新預訓練與後訓練，且模型大小適合運行於 DGX Spark。Poolside 採用了 OpenMDW 授權（類似 Apache 2.0 但對 AI 具備更完善的法律支持），並公開了完整的評估軌跡，展現了極高的透明度。此外還推出了 33B-A3B 的小版本 Laguna-XS-2.1。
*   **DeepSeek-V4-Flash-0731 (DeepSeek)**：在 OpenAI 調降小型模型價格後，DeepSeek 立即更新了 V4 Flash 模型，在參數效能比（performance per parameter）上挑戰帕累托前緣（Pareto frontier）。

📊 **中國技術力量與硬體在地化：Kimi 與 Meituan**

*   **Kimi K3 (MoonshotAI)**：這是近期最大的開源釋出之一。它採用非商業授權，要求推理與微調供應商必須簽署商業協議。這引發了關於政策工具是否會限制美國實體使用中國開源模型的討論。
*   **LongCat-2.0 (Meituan)**：這是一款擁有 1.6T 參數的大型 MoE 模型。其技術亮點在於完全使用 Ascend 910 硬體進行訓練，成為首個完全在中國加速器上訓練的非玩具級（non-toy）模型。

💡 **全球範圍內的技術佈局**

*   **Motif-3-Beta (Motif-Technologies)**：來自韓國，預覽版本為 314B-A13B MoE，引入了 GDLA 與 mHC 等架構創新。
*   **Apertus-v1.5-70B (Swiss-AI)**：透過增加 2T Token 對 Apertus 1.0 進行持續預訓練。
*   **Instella-MoE-16B-A3B-Think (AMD)**：AMD 利用其 Instinct 系列顯示卡訓練的 16B-A3B MoE 模型，並提供從 Base 到 SFT（監督式微調）、MidTrain 到 DPO（直接偏好優化）的所有階段檢查點（checkpoints）。

🎯 **實務啟示**

對於工程師而言，MoE 架構的普及意味著未來開發者可以利用較小的計算成本，獲得接近巨型模型的效能。同時，隨著像 Poolside 這樣具備高度透明度的開源模型出現，以及 AMD 等硬體商提供完整的訓練階段權重，開發者在選擇模型基座與進行微調時，將擁有更多元的技術路徑與硬體優化空間。

🔗 **來源**
- 標題：Latest open artifacts (#23): Laguna S2.1, Inkling, & Kimi K3 show the utility of open models on the Pareto frontier
- 作者／機構：Florian Brand @ Interconnects
- 連結：https://www.interconnects.ai/p/latest-open-artifacts-23-laguna-s21

#AI #MachineLearning #OpenSource #MoE #LLM #DeepLearning #ArtificialIntelligence #AIHardware #AIModels #TechTrends
