---
title: Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo
  2 Super
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/
model: tencent/hy3:free
generated_at: '2026-08-05T08:33:46.284281'
score: 108
---

📌 【NVIDIA 新技術】NVIDIA Alpamayo 2 Super：整合推理與動作，加速自動駕駛開發流程

TL;DR：NVIDIA 發佈 34B 參數 VLA 模型，將路徑規劃與因果推理整合，解決自動駕駛開發中模型碎片化的問題。

在自動駕駛（AV）開發領域，工程師通常需要維護多個獨立模型：一個負責路徑規劃（Trajectory Generation）、一個負責意圖預測、一個負責場景理解，還需要專門的標註工具。這種「模型分離」的設計，使得開發者難以比較不同輸出之間的關聯，也難以在開發流程中重複使用相同的表徵（Representations）。

🤔 **打破模型邊界：從單一任務到 VLA 統一架構**

NVIDIA 提出的 Alpamayo 2 Super 是一款擁有 340 億參數的開放式視覺-語言-動作（VLA）推理模型。它不再將感知、推理與動作拆分，而是提供了一個統一的基礎模型，讓開發者可以將其作為離線策略教師（Offline Policy Teacher）、評估評論家（Evaluation Critic）或數據引擎（Data Engine）。

🧩 **雙模型架構：Reasoner 與 Action Expert 的協作**

Alpamayo 2 Super 的核心設計結合了兩個關鍵組件：
1. **NVIDIA Cosmos 3 Super Reasoner (32B)**：負責理解多鏡頭影片、語言上下文以及先前的運動歷史，進行高層次的邏輯推理。
2. **Action Expert (2B)**：基於擴散模型（Diffusion-based），負責將 Reasoner 產生的內部表徵轉換為自車（Ego-vehicle）未來的運動軌跡。

這種設計讓模型不僅能輸出「要做什麼」（軌跡），還能輸出「為什麼這麼做」（因果推理鏈，Chain-of-Cation, CoC），這對於診斷錯誤來源（是感知錯誤、推理錯誤還是動作生成錯誤）至關重要。

📊 **效能數據：在 LingoQA 測試中超越 GPT-4o**

根據官方提供的測試數據，Alpamayo 2 Super 在多項基準測試中展現了強大的競爭力：

| 測試項目 | 評估指標 / 表現 | 備註 |
| :--- | :--- | :--- |
| **LingoQA (視覺問答)** | **79.2** | 在 37 個模型中排名第一，超越 GPT-4o (55.0) |
| **軌跡預測 (minADE_6)** | **0.911 m** | 針對 Physical AI AV Dataset 中的 1,434 個挑戰樣本 |
| **AV 推理評估** | **0.433** | Physical AI AV Reasoning Benchmark |

*註：LingoQA 表現優異，領先 Qwen2.5-VL (72B) 達 17.0 分，領先 Gemini 2.5 Pro 達 15.1 分。*

💡 **多樣化的開發工作流**

透過這個模型，開發者可以實現四種核心工作流：
* **生成軌跡與 CoC 推理鏈**：同時獲取預測路徑與因果解釋。
* **預測高層元動作 (Meta-actions)**：在輸出軌跡的同時，預測如「讓路」、「變換車道」或「停止」等行為。
* **自然語言場景問答**：針對多鏡頭駕駛場景進行對話式提問。
* **自動化標註**：利用 CoC 推理為自有的影片片段生成帶有 2D 基準（Grounding）的自動標註。

⚠️ **評估方法的差異：Open-loop vs. Closed-loop**

在開發過程中，單純的開迴路（Open-loop）評估（將預測值與預錄好的標籤對比）存在侷限，因為它無法模擬模型動作後，周圍車輛產生的反應。因此，NVIDIA 建議結合閉迴路（Closed-loop）模擬，利用 AlpaSim 進行重複渲染與查詢，以捕捉周圍代理人（Agents）的反應行為。

🎯 **實務啟示**

對於自動駕駛工程師而言，Alpamayo 2 Super 的出現提供了一個「共同基礎」，降低了維護多個專用模型的成本。其開放的權限（OpenMDW-1.1 授權）允許進行微調與商業重新發行，這對於需要快速迭代、自定義任務的開發團隊來說，是一個極具價值的工具集。

🔗 **來源**
- 標題：Generate Trajectories, Reasoning Traces, and Auto-Labels with NVIDIA Alpamayo 2 Super
- 作者／機構：Elizabeth Goodman @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/generate-trajectories-reasoning-traces-and-auto-labels-with-nvidia-alpamayo-2-super/

#NVIDIA #AutonomousDriving #VLA #MachineLearning #ComputerVision #AI #Robotics #DeepLearning #Reasoning #AIModels
