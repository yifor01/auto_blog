---
title: 'Grabette: an open system to record robot-manipulation data'
source: HuggingFace Blog
url: https://huggingface.co/blog/grabette
model: tencent/hy3:free
generated_at: '2026-07-22T00:44:02.504252'
score: 103
---

內容型別判斷：開源專案

📌 【HuggingFace 新釋出】Grabette：無需機器手臂，手持夾具即可產出機器人學習資料

TL;DR：Grabette 是一個低成本開源系統，讓人類透過手持夾具即可記錄操作任務，並自動轉化為機器人可用的資料集。

🤔 **機器人學習的瓶頸不在模型，而在資料**

當前的機器人學習領域已經擁有強大的策略架構（如基於 Transformer 的 VLA、擴散模型 diffusion 與 flow-matching 策略，甚至是世界模型），也有充足的 GPU 資源。然而，真正的瓶頸在於缺乏大量、多樣化且來自真實世界的運算元據。

目前收集資料的主要障礙包括：
- 昂貴且耗時的遠端操作（teleoperation）：需要專業機器人裝置。
- 擴充套件性困難：收集各種任務與環境的資料需要面對巨大的硬體與物流挑戰。

🧩 **不需要機器人，只要「手 + 夾具 + 相機」**

Grabette 的設計理念是打破對昂貴遠端操作裝置的依賴。開發者不需要複雜的實驗室環境，只需要：
1. 一隻人類的手。
2. 一個夾具（gripper）。
3. 一臺相機。
4. 一種能回收手部 6-DoF（六自由度）軌跡的方法。

透過這種方式，使用者只需拿起裝置記錄任務，系統就能自動將示範動作轉化為乾淨、且機器人可以直接學習的資料集。

💡 **目標是建立一個大規模、協作性的開放資料集**

HuggingFace 釋出 Grabette 的最終目標，是希望降低資料收集的門檻。如果記錄示範動作能像拍攝影片一樣簡單，那麼任何人都能參與其中。透過這種方式，Grabette 旨在種下一個龐大且開放的協作式運算元據集，這是任何單一實驗室都無法獨自完成的壯舉。

🎯 **實務啟示**

對於機器人研究者與工程師而言，Grabette 提供了一種極低成本的資料獲取管道。它將資料收集從「硬體驅動」轉向「人手驅動」，這對於需要大量多樣化資料來訓練通用機器人策略（Generalist Robot Policies）的開發流程具有重要意義。

🔗 **來源**
- 標題：Grabette: an open system to record robot-manipulation data
- 作者／機構：HuggingFace
- 連結：https://huggingface.co/blog/grabette

#AI #Robotics #MachineLearning #HuggingFace #Grabette #RobotLearning #OpenSource #DataCollection #ComputerVision #EmbodiedAI
