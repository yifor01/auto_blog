---
title: 'Robbyant Releases LingBot-VLA 2.0: An Open-Source 6B Vision-Language-Action
  (VLA) Model for Cross-Embodiment Robot Manipulation'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/08/lingbot-vla-2-0/
score: 109
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T07:56:15.556603'
---

📌 【Ant Group】開源 LingBot-VLA 2.0：6B 參數模型實現跨機體機器人操控

TL;DR：Ant Group 發布 6B 參數 VLA 模型，透過 6 萬小時高品質資料與 MoE 設計提升機器人泛化能力。

許多 VLA（視覺-語言-動作）模型在實驗室表現優異，一旦進入實際部署環境就容易失效。Ant Group 的 Robbyant 團隊針對此痛點推出 LingBot-VLA 2.0，旨在縮小研究與部署之間的差距。

🧩 **以 Qwen3-VL 為骨幹的通用策略架構**

LingBot-VLA 2.0 是一個通用機器人策略模型，能將攝影機影像與語言指令直接轉換為機器人動作。

- **模型組成**：公開版本為 `lingbot-vla-v2-6b`，採用 Qwen3-VL-4B-Instruct 作為 VLM 骨幹，並提供一個 6B 的「原生深度（native depth）」權重檔。
- **訓練機制**：利用 LingBot-Depth 與 DINO-Video 兩個教師模型進行知識蒸餾（distillation）來監督訓練。
- **擴展設計**：動作專家（action expert）部分採用混合專家（Mixture-of-Experts, MoE）設計，以支援模型規模的擴展。
- **推論效能**：在 NVIDIA GeForce RTX 4090D 上，單次推論（含 10 個去噪步驟）約需 130 毫秒。

📊 **從 11 萬小時原始資料精煉出 6 萬小時高品質集**

為了提升泛化能力，研究團隊建立了一個龐大的資料集，涵蓋 20 種不同的機器人配置（從單臂裝置到完整的人形機器人）。

- **資料組成**：最終高品質資料集包含 5 萬小時機器人軌跡與 1 萬小時第一人稱人類影片（原始池則為 9 萬小時機器人與 2 萬小時人類資料）。
- **嚴格的過濾機制**：
    - **物理指標**：計算每個機體的三階加加速度（third-order jerk）、速度與加速度的 Z-score，剔除平滑度異常或超過 95% 為靜態訊號的片段。
    - **狀態驗證**：利用機器人的 URDF 檔案檢查影片與回放狀態的一致性。
    - **人工與自動篩選**：移除模糊、遮擋、掉幀與多視角對齊錯誤的片段。
    - **人類影片處理**：第一人稱影片需通過 VLM 篩選、egocentric SLAM 與 MANO 手勢重建，並使用 Qwen3.6-27B 進行自動化時間段切分。

🎯 **實務啟示**

對於開發實體 AI 的工程師而言，LingBot-VLA 2.0 的價值在於其「跨機體（Cross-Embodiment）」的資料處理流程。它證明了透過精準的物理指標（如 jerk 與 Z-score）過濾噪訊，以及結合 VLM 進行自動化標記，能有效將大規模雜亂資料轉化為可訓練的高品質策略集，這對於提升機器人在真實環境的魯棒性至關重要。

🔗 **來源**
- 標題：Robbyant Releases LingBot-VLA 2.0: An Open-Source 6B Vision-Language-Action (VLA) Model for Cross-Embodiment Robot Manipulation
- 作者／機構：Asif Razzaq / MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/08/lingbot-vla-2-0/

#VLA #Robotics #OpenSource #AntGroup #Qwen3 #MoE #MachineLearning #ComputerVision #EmbodiedAI #RobotManipulation
