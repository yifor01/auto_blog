---
title: 'LeRobot v0.6.0: Imagine, Evaluate, Improve'
source: HuggingFace Blog
url: https://huggingface.co/blog/lerobot-release-v060
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:31:26.651590'
---

📌 【HuggingFace】LeRobot v0.6.0：引入世界模型與自動化回饋迴路，縮短機器人學習路徑

TL;DR：LeRobot v0.6.0 推出世界模型政策、新 VLA 模型與 Reward Models API，並提供完整的評估與部署工具鏈。

機器人學習最困難的環節在於「如何從失敗中學習」。如果機器人只能盲目執行指令而無法預測結果，或是缺乏明確的成功定義，訓練過程將極其緩慢。HuggingFace 這次更新旨在閉合這個學習迴路：讓機器人能在行動前「想像」未來，並透過獎勵模型判斷成敗。

🧩 **引入世界模型：讓政策具備「想像」能力**

LeRobot v0.6.0 引入了世界模型政策 (World Model Policies)，使機器人能夠在採取行動前預測未來狀態。本次更新包含以下模型：
- VLA-JEPA
- LingBot-VA
- FastWAM

🧩 **擴充 VLA 模型庫：更多視覺語言行動模型**

為了提升機器人的泛化能力與執行力，模型庫 (Model Zoo) 持續增加，新增了多款 VLA 模型：
- GR00T N1.7
- MolmoAct2
- EO-1
- EVO1
- Multitask DiT

🧩 **定義成功標準：Reward Models API**

為了讓開發者能量化機器人的表現，新版本提供了 Reward Models API，讓系統能明確告知機器人何時成功，包含：
- Robometer
- TOPReward

📊 **資料集升級：更豐富的資訊與更快的讀取**

針對資料處理流程，v0.6.0 進行了多項效能與功能最佳化：
- 支援深度感測 (Depth sensing) 資料。
- 提供 VLM 驅動的自動化語言標記管線 (Language annotation pipeline)。
- 支援自定義影片編碼 (Custom video encoding)。
- 資料讀取速度提升至最高 2 倍。

📊 **評估與部署：統一的基準測試與部署工具**

為了讓開發者能快速迭代，LeRobot 強化了評估與部署的工具鏈：
- `lerobot-eval`：將六個新的模擬基準測試 (Simulation benchmarks) 統一在一個 CLI 下。
- `lerobot-rollout`：專門的部署 CLI，支援 DAgger 風格的人機協作修正 (Human-in-the-loop corrections)，將執行失敗轉化為訓練資料。

💡 **訓練效能與雲端整合**

針對大規模訓練需求，本次更新在基礎設施上做出調整：
- 支援 FSDP (Fully Sharded Data Parallel)，允許訓練超過單一 GPU 記憶體上限的大型模型。
- 整合 HF Jobs，支援在雲端進行訓練。
- 簡化安裝流程，使安裝過程更加精簡 (leaner installation)。

🎯 **實務啟示**

對於機器人工程師而言，這次更新將「資料採集 $\rightarrow$ 訓練 $\rightarrow$ 部署 $\rightarrow$ 修正」的流程模組化。特別是 `lerobot-rollout` 提供的 DAgger 風格修正機制，讓開發者能直接在部署階段將失敗案例回饋至訓練集，大幅降低了手動標記資料的成本。

🔗 **來源**
- 標題：LeRobot v0.6.0: Imagine, Evaluate, Improve
- 作者／機構：HuggingFace
- 連結：https://huggingface.co/blog/lerobot-release-v060

#LeRobot #HuggingFace #Robotics #WorldModels #VLA #MachineLearning #RobotLearning #VLM #FSDP #Simulation
