---
title: 'Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours
  of Real-World Trajectories'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.15330
score: 101
model: tencent/hy3:free
generated_at: '2026-07-20T08:49:57.846588'
---

📌 【Xiaomi】百萬小時真實軌跡訓練的 VLA 機器人基礎模型

TL;DR：小米發表 VLA 模型，用 10 萬+ 小時真實軌跡與自動標註，零樣本泛化與微調效率兼備。

當多數機器人模型還在為「換個環境就失效」苦惱時，小米端出了一個用超過 10 萬小時真實世界操作資料餵出來的視覺-語言-動作（vision-language-action, VLA）基礎模型，聲稱能開箱即用處理未見過的移動操作任務。

🤔 **解決什麼問題：開箱即用與低樣本適應**

Xiaomi-Robotics-1 是一個基礎 VLA 模型，目標是兩件事：第一，遵循多樣語言指令，在未知環境中直接執行廣泛的移動操作（mobile manipulation）任務；第二，只需極少 fine-tuning 資料，就能高效適應全新的下游任務。這對現實部署來說，意味著機器人不必每次換場景或換任務都重新收集大量資料。

🧩 **兩階段訓練：預訓練打底，後訓練對齊**

作者提出一個兩階段訓練流程：

- 預訓練（pre-training）：在超過 100K 小時的真實世界操作軌跡上訓練，這些軌跡透過 UMI 裝置收集。關鍵在於他們建了一套可擴展的自動標註 pipeline，用自然語言描述「場景狀態轉換」來標註軌跡片段，為動作學習提供豐富且精確的條件訊號。
- 後訓練（post-training）：將預訓練學到的能力，對齊到具體機器人載體（embodiments）以及人類下指令時自然使用的祈使語句。

📊 **擴展性實驗：資料與模型越大，表現越好**

論文指出明顯的 scaling 行為：預訓練階段，隨資料量與模型規模增加，模型穩定提升；這種擴展性直接延續到後訓練，更強的預訓練模型在未知環境的開箱實機表現更好。

在多個模擬基準上，Xiaomi-Robotics-1 超越既有最佳方法：

| 基準 | Xiaomi-Robotics-1 | 先前 SOTA |
| --- | --- | --- |
| RoboCasa365 成功率 | 57.6% | 46.6% |
| RoboDojo 平均得分 | 20.07 | 13.07 |

此外，它作為機器人基礎策略（foundation policy），能用高資料效率 fine-tune 到複雜靈巧任務上。

⚠️ **限制與未揭露細節**

素材未提及真實機器人部署的失敗案例、UMI 裝置的具體佈建規模，以及自動標註 pipeline 的準確率驗證；作者也尚未釋出程式碼與模型權重（僅宣稱將釋出）。

🎯 **實務啟示**

對機器人團隊來說，這篇展示了一條清晰路徑：用大規模真實軌跡 + 自動語言標註做預訓練，再輕量後訓練對齊載體與指令，能兼顧泛化與適應成本。在權重釋出後，值得拿來當作靈巧操作任務的基底策略做遷移測試。

🔗 **來源**
- 標題：Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories
- 連結：https://huggingface.co/papers/2607.15330

#VLA #Robotics #VisionLanguageAction #Xiaomi #RobotFoundationModel #MobileManipulation #Scaling #FineTuning #RoboCasa #RoboDojo
