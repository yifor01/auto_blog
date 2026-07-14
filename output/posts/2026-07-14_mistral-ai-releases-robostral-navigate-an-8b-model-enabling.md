---
title: 'Mistral AI Releases Robostral Navigate: An 8B Model Enabling Robots to Navigate
  Complex Environments Using a Single RGB Camera'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/14/mistral-ai-releases-robostral-navigate-an-8b-model-enabling-robots-to-navigate-complex-environments-using-a-single-rgb-camera/
score: 88
model: tencent/hy3:free
generated_at: '2026-07-14T08:07:19.754583'
---

這是一篇關於 Mistral AI 最新發布的機器人導航模型的技術報導。

📌 【Mistral AI】首款具身智慧導航模型 Robostral Navigate：單靠 RGB 相機即可應對複雜環境

TL;DR：Mistral AI 發布 8B 導航模型，僅需單一 RGB 相機即可在未見過的複雜環境中達成 76.6% 成功率。

🎣 傳統機器人導航往往需要昂貴的 LiDAR 或多組深度感測器來建構環境，但 Mistral AI 的最新研究證明，僅憑一個普通的 RGB 相機，也能讓機器人在充滿變數的現實世界中精準穿梭。

🤔 **擺脫對深度感測器的依賴**

目前的導航系統多半依賴深度感測器、LiDAR 或多鏡頭組合來獲取空間資訊，這不僅增加了硬體成本，也降低了系統效率。Mistral AI 推出的 Robostral Navigate 則專注於「具身導航」（embodied navigation），旨在透過單一 RGB 影像與自然語言指令，驅動機器人在辦公室、住宅、商業建築及戶外等複雜場景中自主完成任務。

🧩 **核心機制：結合「指向」與「位移」的雙模態決策**

Robostral Navigate 的技術核心在於它如何決定下一步該往哪裡走。該模型並非直接從現有的開源 VLM（視覺語言模型）開發，而是基於 Mistral 專為 grounding 任務（如指向、計數、物件定位）所開發的視覺語言模型進行演進。

其決策邏輯如下：

1. **指向法 (Pointing)**：在給定任務與觀察歷史的情況下，模型會推測目標在當前相機視角中的影像座標，並預測到達目標時應有的朝向。這種方式的優點是對於相機內引數（camera-intrinsic）與世界尺度（world-scale）的變化具有強大的魯棒性（robustness）。
2. **位移法 (Displacements)**：當目標物位於當前視野（field of view）之外時，「指向法」會失效。此時模型會自動切換至機器人區域性座標系下的位移指令，例如：「向前移動 2 公尺、向左移動 1.5 公尺、向左轉 25 度」。

📊 **在未知環境中展現高成功率**

Robostral Navigate 的強大之處在於它能處理訓練過程中從未見過的「活生生」空間，即便環境中充滿了行人與障礙物，它仍能根據單一指令（例如：「離開大廳，穿過走廊，進入供應室，並停下面向第二層架子」）獨立完成整個任務。

在 R2R-CE 驗證集（未見過的環境）測試中，該模型僅使用單一 RGB 相機便達到了 76.6% 的成功率。

🎯 **實務啟示**

對於機器人開發者而言，Robostral Navigate 提供了一種降低硬體門檻的可能性。透過將複雜的導航問題轉化為基於視覺座標的「指向」與「位移」決策，開發者可以在不增加感測器成本的前提下，提升機器人在動態、多變環境中的適應能力。

🔗 **來源**
- 標題：Mistral AI Releases Robostral Navigate: An 8B Model Enabling Robots to Navigate Complex Environments Using a Single RGB Camera
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/14/mistral-ai-releases-robostral-navigate-an-8b-model-enabling-robots-to-navigate-complex-environments-using-a-single-rgb-camera/

#MistralAI #Robotics #EmbodiedAI #ComputerVision #Navigation #LLM #RGB #MachineLearning #RobostralNavigate #AIResearch
