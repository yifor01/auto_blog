---
title: 'Beyond VLAs: How World Action Models Reshape Robot Manipulation'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/beyond-vlas-how-world-action-models-reshape-robot-manipulation/
model: tencent/hy3:free
generated_at: '2026-08-05T08:32:45.715731'
score: 119
---

📌 【NVIDIA 最新研究】從 VLA 轉向 WAM：機器人如何透過理解物理規律實現泛化？

TL;DR：透過將視覺語言模型（VLM）換成影片世界模型（Video World Model），WAM 能讓機器人具備物理先驗知識，大幅提升泛化能力。

機器人學面臨的核心挑戰在於「泛化」（Generalization）——當環境中的物體形狀、位置或光照發生變化時，訓練好的策略往往會失效。傳統做法是讓機器人模仿動作，但這忽略了一個關鍵：機器人需要理解物理規律，而不僅僅是模仿動作。

🤔 **VLA 的侷限：懂語言，但不懂物理動態**

目前的標準做法是構建視覺語言動作模型（Vision-Language-Action, VLA），即在預訓練的視覺語言模型（VLM）上添加動作模組。雖然這在語義理解上表現出色，但存在致命缺陷：

- **缺乏動態模型**：VLM 的優化目標是描述圖像（例如：「桌上有個杯子」），而不是預測世界如何演變。
- **無法預測物理變化**：它不知道夾具閉合時杯子會發生什麼事、毛巾會如何摺疊，或物體掉落後會落在哪裡。
- **數據效率低下**：VLA 通常需要針對同一任務提供極其相似的示範數據（Demonstrations）才能學習。

🧩 **WAM 的崛起：從「模仿動作」轉向「理解世界演變」**

為了克服這點，研究界開始將背景模型從 VLM 換成「影片世界模型」（Video World Model），進而產生「世界動作模型」（World Action Model, WAM）。

根據 NVIDIA 研究顯示，同時預測影片與動作的 WAM 具有 VLA 無法輕易取得的特性：

- **從多樣化數據中學習**：只要是交互數據都能提供物理知識（如推動、抓取、丟棄），不一定要完全相同的任務示範，這降低了數據收集成本。
- **具備物理通用性**：物理規律比語義更具通用性。一旦模型學會物體滑動或掉落的規律，就能將此知識應用於從未見過的場景。
- **快速適應新硬體**：由於模型已有物理交互的先驗知識（Physics Prior），在面對新機械手臂或夾具時，僅需極少量的示範即可完成專業化訓練（Specialization）。

📊 **Cosmos 3：構建 WAM 的強大基礎模型**

NVIDIA 提出的 Cosmos 3 是一個基於混合專家轉換器（Mixture-of-Transformers, MoT）架構的全能世界基礎模型。

- **架構設計**：透過自回歸轉換器（Autoregressive Transformer）進行推理並產生文本；透過擴散轉換器（Diffusion Transformer）處理連續模態（圖像、影片、音訊與動作）。
- **海量數據訓練**：包含約 7.67 億張圖像、3.48 億段真實世界動態影片，以及 800 萬份涵蓋機器人操作、自動駕駛與相機運動的動作樣本。
- **模型規模**：提供 4B (Edge)、16B (Nano) 與 64B (Super) 三種版本。

💡 **從世界模型到機器人策略：Cosmos 3 Policy**

透過對 Cosmos 3 進行後訓練（Post-training），可以將其轉化為專業的機器人策略（如 DROID 平臺）：

1. **邊緣運算與工作站部署**：
   - **Cosmos3-Nano-Policy (16B)**：適合在工作站運行，透過網路將觀察值傳輸至機器人並接收動作塊。
   - **Cosmos3-Edge-Policy (4B)**：適合直接在嵌入式硬體（如 NVIDIA Jetson Thor）上部署，實現 15 Hz 的即時控制。
2. **「邊行動邊想像」的能力**：當模型輸出動作時，它能同時輸出預測影片——即執行該動作後，相機會看到的畫面。
3. **架構完整性**：後訓練過程並未移除原始的生成能力，策略模型依然保有推理與生成影片的能力。

📈 **實驗數據證明架構的重要性**

NVIDIA 透過對比實驗證明，提升效能不僅靠規模，更靠架構：
兩組使用相同配方與算力的 DROID 策略，一組從基礎模型開始，另一組從具備多領域動作能力的「全能檢查點」（Omni Checkpoint）開始，後者的 RoboLab 成功率從 28.1% 提升至 36.8%。

🎯 **實務啟示**

對於機器人開發者而言，WAM 的出現代表著開發流程的轉變：你不再需要從零開始訓練世界模型，而是可以利用 Cosmos 3 這種具備強大物理先驗的基礎模型，透過將數據轉換為 LeRobotDataset 格式並套用公開的後訓練配方，快速將新硬體（如 Franka、UR、WidowX 等）轉化為具備高度泛化能力的機器人。

🔗 **來源**
- 標題：Beyond VLAs: How World Action Models Reshape Robot Manipulation
- 作者／機構：Michelle Horton @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/beyond-vlas-how-world-action-models-reshape-robot-manipulation/

#AI #Robotics #NVIDIA #Cosmos3 #MachineLearning #WorldModels #VLA #WAM #ComputerVision #EmbodiedAI
