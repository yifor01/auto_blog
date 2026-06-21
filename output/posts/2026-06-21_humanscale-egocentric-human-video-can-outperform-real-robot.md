---
title: 'HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied
  Pretraining'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.20521
score: 81
model: google/gemma-4-31b-it:free
generated_at: '2026-06-21T19:50:45.908583'
---

📌 第一人稱人類影片，能讓具身智慧預訓練超越機器人實測資料？

TL;DR：研究顯示用第一人稱人類影片取代遠端操作的機器人軌跡，能降低資料成本並提升模型效能。

在開發具身智慧（Embodied AI）模型時，最昂貴的成本往往在於收集高品質的機器人運算元據。傳統上，我們依賴遠端操作（Teleoperation）來獲取精確的軌跡，但這種方式效率低且成本極高。

🤔 **資料獲取的成本瓶頸與替代方案**

目前預訓練具身模型的主要挑戰在於資料稀缺。為了讓機器人學會操作，工程師必須花費大量時間進行遠端操作以紀錄軌跡。然而，這項研究提出了一個反直覺的觀點：我們或許不需要這麼多機器人實測資料，只要使用「第一人稱人類影片」（Egocentric human video）即可。

🧩 **用人類視角資料強化預訓練**

該研究提出的 HumanScale 方法，核心理念是利用人類在第一人稱視角下的操作影片來進行預訓練。這種方式將人類的行為模式轉化為模型的先驗知識，使模型在進入實際機器人環境前，就已經掌握了操作的邏輯與空間關係。

📊 **效能提升且降低資料成本**

根據研究結果，使用第一人稱人類影片進行預訓練的成效，不僅能有效取代傳統的遠端操作軌跡，在最終表現上甚至能超越僅使用真實機器人資料的結果。這意味著開發者可以用更低的資料獲取成本，達到更好的模型效能。

🎯 **實務啟示**

對於開發具身智慧的工程師而言，這項研究提供了一個重要的方向：不要過度依賴昂貴的機器人實測資料。在預訓練階段，優先挖掘大量的第一人稱人類操作影片（如 YouTube 或專門的 Egocentric 資料集），可能比強行收集機器人軌跡更具成本效益且效果更佳。

🔗 **來源**
- 標題：HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining
- 連結：https://huggingface.co/papers/2606.20521

#EmbodiedAI #Robotics #Pretraining #EgocentricVideo #MachineLearning #ComputerVision #HumanScale #DataEfficiency #RobotLearning #AI
