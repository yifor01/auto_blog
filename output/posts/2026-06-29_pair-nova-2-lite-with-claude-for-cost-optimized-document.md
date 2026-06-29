---
title: Pair Nova 2 Lite with Claude for cost-optimized document processing
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/pair-nova-2-lite-with-claude-for-cost-optimized-document-processing/
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:33:11.170474'
---

📌 【AWS 實作】Nova 2 Lite 搭配 Claude：將檔案數位化成本降低 66%

TL;DR：透過 Nova 2 Lite 提取座標與 Claude 進行空間推理，實現高精準且低成本的掃描檔案數位化。

面對一張掃描的畢業紀念冊頁面，裡面可能有上百個姓名與數張照片，但完全沒有機器可讀的結構。要將這些資訊數位化，挑戰在於如何精準偵測照片 bounding boxes、提取姓名，並在沒有結構化資料的情況下，判斷哪個名字對應哪張臉。

🤔 **單一模型處理檔案數位化的成本痛點**

傳統做法通常將整個任務交給單一強大的視覺語言模型（Vision-Language Model），但這在處理大規模檔案時成本過高。AWS 提出了一種「雙模型流水線」（Two-model pipeline）的方案，將任務拆分為「原生提取」與「空間推理」兩個階段，在維持精準度的前提下大幅降低成本。

🧩 **分工協作：從原生提取到空間推理**

此方案在 Amazon Bedrock 上建構，將工作流分為兩個順序階段：

1. **第一階段：Amazon Nova 2 Lite 負責原生多模態提取**
   Nova 2 Lite 處理交錯的文字與影像，透過單次 API 呼叫完成以下工作：
   - 偵測並分類照片，並提供 bounding boxes。
   - 讀取頁面上的可見姓名及其近似位置座標。
   - 產出頁面層級的後設資料（Metadata）。
   （註：為了此任務，作者將 reasoning 設定為 LOW）。

2. **第二階段：Claude Sonnet 4.6 負責空間推理**
   Claude 接收 Nova 2 Lite 產出的所有結果，利用其空間推理能力，根據頁面佈局將姓名與對應的人臉進行匹配。

📊 **處理 336 頁面，精準度與成本雙贏**

針對 336 頁掃描頁面的實測結果顯示：
- **匹配成效**：成功產生 3,122 組「姓名-人臉」關聯。
- **信心水準**：其中 93% 的結果信心分數在 0.95 或以上。
- **成本效益**：與將全部任務交給單一模型的方案相比，這種雙模型組合每頁的處理成本降低了約三分之二（成本僅約原先的 1/3）。

🎯 **實務啟示：將「提取」與「推理」解耦**

這個案例為工程師提供了一個重要的最佳化思路：**不要讓最強的模型做所有事**。

對於複雜的檔案處理，可以將任務拆分為「低成本的視覺提取（提取座標與文字）」$\rightarrow$「高能力的邏輯推理（建立關聯）」。透過 Nova 2 Lite 處理繁重的視覺解析，再由 Claude 處理高階推理，可以在不犧牲精準度的情況下，顯著降低大規模處理檔案的營運成本。

🔗 **來源**
- 標題：Pair Nova 2 Lite with Claude for cost-optimized document processing
- 作者／機構：Sanghwa Na @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/pair-nova-2-lite-with-claude-for-cost-optimized-document-processing/

#AWS #AmazonBedrock #Nova2Lite #Claude #DocumentProcessing #MultimodalAI #CostOptimization #SpatialReasoning #OCR #LLM
